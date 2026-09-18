"""拉取 Met Open Access（CC0）欧洲绘画数据。

只用 Met 官方标注 isHighlight 的欧洲绘画（约 125 幅），这批是馆方自己挑的代表作，
覆盖面横跨 13—20 世纪，正好适合做「欧洲古画」学习站的骨架。

注意：
- /v1/search 将于 2026-10-01 下线且不支持分页，搜索走 /v1.1/search。
- /v1.1 只提供 search，取单件仍走 /v1/objects/{id}。
- 只保留 isPublicDomain 且带图的记录（CC0，可自由下载与商用）。
"""
import json, time, urllib.request, urllib.parse, pathlib

API = "https://collectionapi.metmuseum.org/public/collection/v1"       # 单件
API_SEARCH = "https://collectionapi.metmuseum.org/public/collection/v1.1"  # 分页搜索
UA = {"User-Agent": "old-paintings-study-site/0.1 (personal learning project)"}
DEPARTMENT_EUROPEAN_PAINTINGS = 11


def get(url):
    req = urllib.request.Request(url, headers=UA)
    last = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # 502/超时都重试
            last = e
            time.sleep(2.0 * (attempt + 1))
    raise last


def search(**params):
    """分页取全部 objectID。"""
    q = urllib.parse.urlencode(params)
    ids, offset = [], 0
    while True:
        d = get(f"{API_SEARCH}/search?{q}&offset={offset}&limit=100")
        batch = d.get("objectIDs") or []
        ids += batch
        offset += 100
        if offset >= d.get("total", 0) or not batch:
            return ids


def main():
    out = pathlib.Path("data/met_raw.json")
    out.parent.mkdir(exist_ok=True)

    print("== 搜索 European Paintings(11) 精选有图 ==", flush=True)
    ids = search(departmentId=DEPARTMENT_EUROPEAN_PAINTINGS,
                 isHighlight="true", hasImages="true")
    print("highlights:", len(ids), flush=True)

    # 已抓过的跳过，断点续跑
    records, done = [], set()
    if out.exists() and out.stat().st_size > 2:
        records = json.loads(out.read_text())
        done = {r["objectID"] for r in records}
        print("已存在", len(records), "条，续跑", flush=True)

    for i, oid in enumerate(ids, 1):
        if oid in done:
            continue
        try:
            o = get(f"{API}/objects/{oid}")
        except Exception as e:
            print("  !", oid, e, flush=True)
            continue
        if o.get("isPublicDomain") and o.get("primaryImageSmall"):
            records.append(o)
        if i % 10 == 0 or i == len(ids):
            records.sort(key=lambda r: (r.get("objectEndDate") or 0,
                                        r.get("artistAlphaSort") or ""))
            out.write_text(json.dumps(records, ensure_ascii=False, indent=1))
            print(f"  {i}/{len(ids)} -> 已收 {len(records)} 条 CC0（已落盘）", flush=True)
        time.sleep(0.05)

    records.sort(key=lambda r: (r.get("objectEndDate") or 0, r.get("artistAlphaSort") or ""))
    out.write_text(json.dumps(records, ensure_ascii=False, indent=1))
    print("完成，写入", out, len(records), "条", flush=True)


if __name__ == "__main__":
    main()
