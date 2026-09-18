#!/usr/bin/env python3
"""当 github.com:443 不可达（但 api.github.com 正常）时，走 Git Data API 推送。

背景：某些网络环境下 git 的 HTTPS 通道连不上 github.com，`git push` 会超时，
但 REST API 可用。这个脚本用 API 复刻一次完整的 push，并且保证远端提交对象
与本地提交逐字节一致（同样的 tree、parent、author/committer、message）。

用法：
    python3 scripts/push_via_api.py            # 推送当前 HEAD 到 origin 的默认分支
    python3 scripts/push_via_api.py --dry-run  # 只检查，不改动远端

前提：
    - 本地已 commit、工作区干净
    - gh CLI 已登录（脚本用 `gh auth token` 取凭证）
"""
import argparse
import base64
import concurrent.futures
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORKERS = 12


def git(*args, **kw):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, **kw).strip()


def blob_sha(data: bytes) -> str:
    """git blob 的 sha1，和 GitHub 的 blob sha 是同一个值。"""
    h = hashlib.sha1()
    h.update(b"blob %d\0" % len(data))
    h.update(data)
    return h.hexdigest()


def tracked_files():
    """用 -z 取路径，避免中文文件名被 core.quotepath 转义成八进制。"""
    out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT, text=True)
    return [f for f in out.split("\0") if f]


def api_base():
    url = git("remote", "get-url", "origin")
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", url)
    if not m:
        sys.exit(f"无法从 origin 解析 owner/repo：{url}")
    return f"https://api.github.com/repos/{m.group(1)}/{m.group(2)}", m.group(1), m.group(2)


def make_api(token):
    def api(method, url, payload=None, timeout=45, tries=6):
        data = json.dumps(payload).encode() if payload is not None else None
        last = None
        for attempt in range(tries):
            req = urllib.request.Request(url, data=data, method=method)
            req.add_header("Authorization", f"Bearer {token}")
            req.add_header("Accept", "application/vnd.github+json")
            req.add_header("X-GitHub-Api-Version", "2022-11-28")
            if data:
                req.add_header("Content-Type", "application/json")
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return json.loads(r.read().decode() or "null")
            except urllib.error.HTTPError as e:
                body = e.read().decode()[:300]
                last = RuntimeError(f"{method} {url} -> HTTP {e.code}: {body}")
                if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                raise last
            except Exception as e:
                last = e
                if attempt < tries - 1:
                    time.sleep(1.0 + attempt)
                    continue
                raise
        raise last
    return api


def head_meta():
    """读出本地 HEAD 提交的原始元数据，用于在远端复刻同一个对象。"""
    sha = git("rev-parse", "HEAD")
    raw = subprocess.check_output(["git", "cat-file", "commit", sha],
                                  cwd=ROOT, text=True)
    head, _, message = raw.partition("\n\n")

    def field(name):
        m = re.search(rf"^{name} (.+)$", head, re.M)
        return m.group(1) if m else None

    def parse(line):
        name, email, when = re.match(r"^(.*?) <(.*?)> (\d+ [+-]\d{4})$", line).groups()
        return name, email, int(when.split()[0]), when.split()[1]

    return {
        "sha": sha,
        "tree": git("rev-parse", "HEAD^{tree}"),
        "parents": git("rev-list", "--parents", "-n", "1", "HEAD").split()[1:],
        "message": message,
        "author": parse(field("author")),
        "committer": parse(field("committer")),
    }


def bootstrap_if_empty(api, url):
    """空仓库的 Git Data API 会返回 409，需要先用 Contents API 建一个提交。"""
    try:
        api("GET", f"{url}/git/ref/heads/main")
        return
    except RuntimeError as e:
        if "HTTP 409" not in str(e) and "HTTP 404" not in str(e):
            raise
    files = tracked_files()
    if not files:
        sys.exit("仓库里没有已跟踪文件")
    path = files[0]
    raw = (ROOT / path).read_bytes()
    res = api("PUT", f"{url}/contents/{path}", {
        "message": "chore: 初始化仓库",
        "content": base64.b64encode(raw).decode(),
    })
    print("引导提交:", res["commit"]["sha"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if git("status", "--porcelain"):
        sys.exit("工作区不干净，请先提交")
    token = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    url, owner, repo = api_base()
    api = make_api(token)
    meta = head_meta()
    print(f"仓库 {owner}/{repo}")
    print(f"本地 HEAD {meta['sha'][:12]}  tree {meta['tree'][:12]}")

    bootstrap_if_empty(api, url)
    remote_head = api("GET", f"{url}/git/ref/heads/main")["object"]["sha"]
    if remote_head == meta["sha"]:
        print("远端已经是这个提交，无需操作")
        return 0
    print(f"远端 HEAD {remote_head[:12]} -> {meta['sha'][:12]}")

    files = tracked_files()

    # 远端已有 tree 里的 blob sha 可以直接复用；只有内容变了的文件才需要重传。
    # 这比"按路径缓存"可靠：路径没变但内容变了也能正确识别。
    remote_blobs = {}
    try:
        rt = api("GET", f"{url}/git/trees/{remote_head}?recursive=1")
        remote_blobs = {e["path"]: e["sha"] for e in rt.get("tree", [])
                        if e["type"] == "blob"}
    except RuntimeError:
        pass

    def upload(path):
        raw = (ROOT / path).read_bytes()
        blob = api("POST", f"{url}/git/blobs", {
            "content": base64.b64encode(raw).decode(), "encoding": "base64"})
        return path, blob["sha"]

    shas, todo = {}, []
    for p in files:
        local_sha = blob_sha((ROOT / p).read_bytes())
        if remote_blobs.get(p) == local_sha:
            shas[p] = local_sha
        else:
            todo.append(p)

    print(f"新增或改动 {len(todo)}/{len(files)} 个文件，其余复用远端 blob")
    failed, done = [], 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = {pool.submit(upload, p): p for p in todo}
        for fut in concurrent.futures.as_completed(futures):
            path = futures[fut]
            try:
                p, sha = fut.result()
                shas[p] = sha
            except Exception as e:
                failed.append(path)
                print("  失败:", path, str(e)[:150])
            done += 1
            if done % 20 == 0 or done == len(todo):
                print(f"  {done}/{len(todo)}")
    if failed:
        sys.exit(f"{len(failed)} 个文件上传失败，重跑即可续传")

    tree = [{"path": p, "mode": "100644", "type": "blob", "sha": shas[p]} for p in files]
    created = api("POST", f"{url}/git/trees", {"tree": tree}, timeout=90)
    if created["sha"] != meta["tree"]:
        sys.exit(f"tree 不一致：远端 {created['sha']} vs 本地 {meta['tree']}，"
                 "请检查 .gitattributes 或文件权限位")
    print("tree 一致:", created["sha"][:12])

    def gh_date(t):
        """把 git 的 `<epoch> <±HHMM>` 转成 API 要的 ISO 8601，并保留原时区偏移
        （偏移变了提交对象的字节就变了，sha 也就对不上）。"""
        name, email, epoch, tz = t
        sign = 1 if tz[0] == "+" else -1
        offset = sign * (int(tz[1:3]) * 3600 + int(tz[3:5]) * 60)
        local = time.gmtime(epoch + offset)
        return {"name": name, "email": email,
                "date": time.strftime("%Y-%m-%dT%H:%M:%S", local)
                        + tz[:3] + ":" + tz[3:]}

    if args.dry_run:
        print("dry-run：跳过建提交与更新 ref")
        return 0

    commit = api("POST", f"{url}/git/commits", {
        "message": meta["message"],
        "tree": meta["tree"],
        "parents": [remote_head],
        "author": gh_date(meta["author"]),
        "committer": gh_date(meta["committer"]),
    }, timeout=90)
    if commit["sha"] != meta["sha"]:
        sys.exit(f"提交对象不一致：远端 {commit['sha']} vs 本地 {meta['sha']}")
    print("提交对象一致:", commit["sha"][:12])

    api("PATCH", f"{url}/git/refs/heads/main", {"sha": commit["sha"], "force": False})
    print("已推送：", commit["sha"])
    subprocess.run(["git", "update-ref", "refs/remotes/origin/main", commit["sha"]],
                   cwd=ROOT, check=True)
    print("本地 origin/main 已同步")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
