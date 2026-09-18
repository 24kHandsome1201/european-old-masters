"""把 Met 原始数据 + 中文策展文案，合成网站用的数据文件并下载图片。

输入：
  data/met_raw.json     —— scripts/fetch_met.py 抓下来的 CC0 记录
  data/curation.json    —— { "<objectID>": { titleZh, artistZh, era, look, note, tags } }

输出：
  assets/images/<id>.jpg        馆方原图，sips 压到长边 1600px
  assets/images/thumbs/<id>.jpg 长边 560px，供目录页
  assets/js/works-data.js       （挂到 window.WORKS，供 file:// 直接打开）
  data/works.json               （同一份数据的纯 JSON，便于检查）
"""
import json
import pathlib
import re
import shutil
import struct
import subprocess
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "met_raw.json"
CURATION = ROOT / "data" / "curation.json"
IMG_DIR = ROOT / "assets" / "images"
THUMB_DIR = IMG_DIR / "thumbs"
TMP_DIR = ROOT / "data" / "originals"
OUT_JS = ROOT / "assets" / "js" / "works-data.js"
OUT_JSON = ROOT / "data" / "works.json"

FULL_PX = 1600      # 详情页用的长边
THUMB_PX = 560      # 目录页用的长边
QUALITY = 74

SIPS = shutil.which("sips")

UA = {"User-Agent": "old-paintings-study-site/0.1 (personal learning project)"}

PROVINCES = {
    "Alsace": "阿尔萨斯", "Bohemia": "波希米亚", "Brittany": "布列塔尼",
    "Burgundy": "勃艮第", "Flanders": "佛兰德斯", "Lorraine": "洛林",
    "Normandy": "诺曼底", "Provence": "普罗旺斯", "Tuscany": "托斯卡纳",
    "Umbria": "翁布里亚", "Veneto": "威尼托", "Bavaria": "巴伐利亚",
    "Saxony": "萨克森", "Catalonia": "加泰罗尼亚", "Andalusia": "安达卢西亚",
}
COUNTRIES = {
    "Austria": "奥地利", "Belgium": "比利时", "Denmark": "丹麦", "England": "英格兰",
    "France": "法国", "Germany": "德国", "Italy": "意大利",
    "The Netherlands": "荷兰", "Netherlands": "荷兰", "Norway": "挪威",
    "Poland": "波兰", "Portugal": "葡萄牙", "Russia": "俄罗斯", "Scotland": "苏格兰",
    "Spain": "西班牙", "Sweden": "瑞典", "Switzerland": "瑞士",
    "United Kingdom": "英国", "Ireland": "爱尔兰", "Greece": "希腊",
}


def jpeg_size(data: bytes):
    """不依赖 Pillow 读 JPEG 宽高。"""
    i = 2
    n = len(data)
    while i < n - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        seglen = struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + seglen
    return None


def download(url: str, dest: pathlib.Path):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            dest.write_bytes(data)
            return data
        except Exception as e:
            if attempt == 4:
                print("   下载失败:", url, e)
                return None
            time.sleep(2 * (attempt + 1))
    return None


def sips_resize(src: pathlib.Path, dest: pathlib.Path, max_px: int):
    """用 macOS 自带的 sips 缩放并重压 JPEG，避免引入 Pillow 依赖。"""
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [SIPS, "-Z", str(max_px), "-s", "format", "jpeg",
         "-s", "formatOptions", str(QUALITY), str(src), "--out", str(dest)],
        check=True, capture_output=True,
    )


def build_images(oid: str, original_url: str, web_large_url: str):
    """返回 (本地大图相对路径, 缩略图相对路径)；本地图优先，失败则回落到馆方 web-large。"""
    full = IMG_DIR / f"{oid}.jpg"
    thumb = THUMB_DIR / f"{oid}.jpg"
    src = TMP_DIR / f"{oid}.jpg"

    if not (full.exists() and full.stat().st_size > 8000) and SIPS:
        if not (src.exists() and src.stat().st_size > 8000):
            download(original_url, src)
        if src.exists() and src.stat().st_size > 8000:
            try:
                sips_resize(src, full, FULL_PX)
                sips_resize(src, thumb, THUMB_PX)
                print(f"   压缩 {oid} -> {jpeg_size(full.read_bytes()[:200000])}")
            except subprocess.CalledProcessError as e:
                print("   sips 失败", oid, e)

    if not (full.exists() and full.stat().st_size > 8000):
        # 没有 sips 或下载失败：退回馆方 web-large（约 600px）
        download(web_large_url, full)
        download(web_large_url, thumb)

    return (f"assets/images/{oid}.jpg" if full.exists() else web_large_url,
            f"assets/images/thumbs/{oid}.jpg" if thumb.exists() else web_large_url)


def artist_dates(rec):
    b = (rec.get("artistBeginDate") or "").strip()
    d = (rec.get("artistEndDate") or "").strip()

    def yr(s):
        m = re.match(r"^-?\d+", s)
        return m.group(0) if m else ""

    b, d = yr(b), yr(d)
    if b and d:
        return f"{b}–{d}"
    if d:
        return f"†{d}"
    if b:
        return f"{b}–"
    return ""


def place_zh(rec):
    parts = []
    for key, table in (("country", COUNTRIES), ("region", PROVINCES), ("city", None)):
        v = (rec.get(key) or "").strip()
        if not v:
            continue
        if table:
            parts.append(table.get(v, v))
        else:
            parts.append(v)
    return "，".join(dict.fromkeys(parts))


def main():
    raw = {str(r["objectID"]): r for r in json.loads(RAW.read_text())}
    curation = json.loads(CURATION.read_text())
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    THUMB_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "js").mkdir(parents=True, exist_ok=True)

    works, missing = [], []
    for oid, cur in curation.items():
        rec = raw.get(str(oid))
        if not rec:
            missing.append(oid)
            continue

        small = rec.get("primaryImageSmall") or ""
        original = rec.get("primaryImage") or small
        local_rel, thumb_rel = build_images(oid, original, small)

        w = h = None
        local_abs = ROOT / local_rel
        if local_abs.exists():
            size = jpeg_size(local_abs.read_bytes()[:200000])
            if size:
                w, h = size

        dates = cur.get("artistDates") or artist_dates(rec)
        death = (rec.get("artistEndDate") or "").strip()
        m = re.search(r"(\d{3,4})\s*$", dates)
        if m:
            death = m.group(1)

        works.append({
            "id": int(oid),
            "title": rec.get("title", ""),
            "titleZh": cur["titleZh"],
            "artist": rec.get("artistDisplayName", ""),
            "artistZh": cur["artistZh"],
            "artistDates": dates,
            "deathYear": death,
            "year": cur.get("year") or rec.get("objectEndDate") or 0,
            "yearLabel": (rec.get("objectDate") or "").strip(),
            "origin": place_zh(rec),
            "medium": rec.get("medium", ""),
            "mediumZh": cur.get("mediumZh", ""),
            "dimensions": rec.get("dimensions", ""),
            "repository": rec.get("repository", ""),
            "credit": rec.get("creditLine", ""),
            "department": rec.get("department", ""),
            "era": cur["era"],
            "look": cur["look"],
            "note": cur["note"],
            "tags": cur.get("tags", []),
            "local": local_rel,
            "thumb": thumb_rel,
            "remote": original,
            "remoteSmall": small,
            "source": rec.get("objectURL") or "",
            "license": "CC0 1.0",
            "licenseUrl": "https://creativecommons.org/publicdomain/zero/1.0/",
            "w": w, "h": h,
        })

    works.sort(key=lambda x: (x["year"], x["artist"]))
    if missing:
        print("!! curation 里有 raw 中不存在的 id:", missing)

    payload = json.dumps(works, ensure_ascii=False, indent=1)
    OUT_JSON.write_text(payload)
    OUT_JS.write_text(
        "/* 由 scripts/build_site.py 自动生成，请勿手改。\n"
        f"   数据源：The Met Open Access (CC0)。共 {len(works)} 幅。 */\n"
        "window.WORKS = " + payload + ";\n"
    )
    print(f"完成：{len(works)} 幅 -> {OUT_JS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
