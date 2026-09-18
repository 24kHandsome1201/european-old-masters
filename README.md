# 古画 · European Old Masters

一个非营利的欧洲古典绘画学习站：从乔托到塞尚，46 幅作品的高清图、中文导览，以及一条 1300—1900 的时间线。

纯静态站点，无构建工具、无依赖、无框架。双击 `index.html` 就能打开，也可以直接部署到 GitHub Pages / Vercel。

---

## 为什么这个站可以放心用图

站内所有图片来自**纽约大都会艺术博物馆的 Open Access 数据**，适用 **CC0 1.0 公有领域贡献**：

- 原作本身：作者最晚卒于 1906 年，早已进入公有领域。
- 数字图片：馆方主动放弃著作权，明确允许「unrestricted commercial and noncommercial use」，不需要 key、不需要申请。

版权核查的完整结论见 [`版权调研报告.md`](版权调研报告.md)，站内版本见 [`about.html`](about.html)。要点是：

> 画随便用，图片看是哪一张。真正要防的不是五百年前的画家，而是近五十年里拍那张照片、扫那本书、卖那张图的人。

---

## 目录结构

```
.
├── index.html              主页：主视觉 + 时间线 + 作品目录
├── work.html               作品详情页（?id=<objectID>）
├── about.html              版权与图片来源
├── 404.html
├── assets/
│   ├── css/site.css        唯一样式表（手写，无框架）
│   ├── js/
│   │   ├── works-data.js   自动生成的数据，挂到 window.WORKS
│   │   └── app.js          时间线、画廊、详情页渲染
│   └── images/
│       ├── <id>.jpg        本地大图（长边 1600px）
│       └── thumbs/<id>.jpg 目录页缩略图（长边 560px）
├── data/
│   ├── met_raw.json        从 Met API 抓到的 CC0 原始记录
│   ├── curation.json       中文策展文案（手写，这是内容源）
│   ├── works.json          合成后的纯 JSON（便于检查）
│   └── originals/          临时缓存，已 gitignore
├── scripts/
│   ├── fetch_met.py        抓取 Met Open Access 数据
│   └── build_site.py       合成数据 + 下载压缩图片 + 生成 works-data.js
└── docs/原始调研/          三份调研 agent 的原始记录
```

---

## 本地预览

因为数据以 `<script>` 形式内联到 `assets/js/works-data.js`，`file://` 直接打开即可，不需要服务器：

```bash
open index.html
```

若想更接近线上环境（相对路径、404 页面行为一致）：

```bash
python3 -m http.server 8000
# 然后访问 http://localhost:8000
```

---

## 重新生成数据

只在需要增删作品或更新图片时执行。

```bash
# 1. 抓取 Met 的欧洲绘画精选（CC0，约 119 幅，需几分钟）
python3 scripts/fetch_met.py

# 2. 编辑 data/curation.json，为你选中的作品补中文文案
#    key 是 Met 的 objectID，必填字段：titleZh / artistZh / era / look / note
#    可选：artistDates / year / mediumZh / tags

# 3. 合成数据并下载图片
python3 scripts/build_site.py
```

第 3 步会把馆方原图下载到 `data/originals/`，用 macOS 自带的 `sips` 压到长边 1600px 存进 `assets/images/`，同时生成 560px 的缩略图。非 macOS 环境没有 `sips` 时，会自动退回馆方约 600px 的 web-large 图。

`era` 取值（对应 `assets/js/app.js` 里的 `ERAS`）：

| 值 | 时代 |
|---|---|
| `1` | 晚期哥特与早期文艺复兴（约 1300—1500） |
| `2` | 文艺复兴盛期与北方文艺复兴（约 1500—1600） |
| `3` | 巴洛克（约 1600—1700） |
| `4` | 洛可可与启蒙（约 1700—1780） |
| `5` | 新古典与浪漫主义（约 1780—1850） |
| `6` | 写实、印象与后印象（约 1850—1900） |

---

## 设计说明

- **方向**：博物馆图录风。暖白纸底、活字衬线、大留白，时间线像一条贯穿全页的书脊。
- **字体**：拉丁用 EB Garamond（旧体衬线，与展品年代同源），中文落到 `Songti SC` / `Noto Serif SC`。界面标签用 Archivo。字体从 Google Fonts 加载，取不到时回落系统衬线，不影响阅读。
- **颜色**：全部用 OKLCH。唯一强调色是朱砂（vermilion），六个时代各有一种低彩度的「颜料色」——绿土、群青、沥青褐、胭脂、普鲁士蓝、铬黄。
- **图片**：目录页用 `object-fit: contain`，不裁切。画作的形状本身就是信息。
- **图片来源切换**：页首的「本地图 / 馆方在线图」开关，用 `localStorage` 记住选择，本地文件缺失时自动回落到馆方链接。

---

## 部署

线上地址：<https://24khandsome1201.github.io/european-old-masters/>

GitHub Pages 已配置为 `main` 分支根目录，无需构建命令。`404.html` 会自动生效。作品详情页通过查询参数寻址（`work.html?id=436535`），Vercel 不需要额外 rewrite。

### 推送

正常情况就是 `git push`。但如果 `github.com:443` 连不上（`git push` 报超时或 HTTP/2 错误），而 `api.github.com` 正常，可以用 Git Data API 推送：

```bash
python3 scripts/push_via_api.py --dry-run   # 先检查 tree 是否一致
python3 scripts/push_via_api.py             # 推送当前 HEAD
```

这个脚本会用 REST API 复刻一次完整的 push，并且校验远端生成的 tree 与提交对象和本地逐字节一致，保证两边历史不会分叉。blob 缓存写在 `.git/dsh/`，中断后重跑可以续传。

判断当前网络属于哪种情况：

```bash
curl -s -o /dev/null -w "%{http_code}\n" -m 10 https://github.com          # 000 表示不通
curl -s -o /dev/null -w "%{http_code}\n" -m 10 https://api.github.com      # 200 表示可用
```


---

## 许可

- **代码**（HTML / CSS / JS / Python 脚本）：可自由使用。
- **中文导览文案**：本站原创，欢迎在注明出处的前提下引用；若发现史实错误，欢迎提 issue。
- **图片**：CC0 1.0，来自 The Met Open Access。本站不主张任何权利。
- **作品本身**：公有领域。

本站不投放广告、不接受赞助、不销售任何商品或服务。若你打算把类似项目用于商业用途，请先阅读 [`版权调研报告.md`](版权调研报告.md) 第 5 节，并咨询执业律师。
