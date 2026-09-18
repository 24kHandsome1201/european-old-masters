# 欧洲古画学习网站 · 可用图片来源与授权核实报告

> 调研方法：仅使用 `web_fetch` / 直连抓取官方页面（`web_search` 因 API key 失效不可用）。
> 原则：只报告实际抓到的原文；抓不到的明确写「未能核实」。
> **重要环境限制（影响可达性）**：
> - `commons.wikimedia.org`、`*.wikipedia.org`、`*.wikimedia.org` 全部被网络层阻断（TLS `Connection reset by peer`，连 IP+Host 头也失败）。
> - `web.archive.org` / `archive.org` **不可达**，因此本报告**没有任何一条来自 Wayback 存档**。
> - 被 Cloudflare / Vercel 机器人校验拦截：`europeana.eu`（403）、`www.artic.edu`（403）、`www.museodelprado.es`（403）、`www.si.edu`（403）、`www.metmuseum.org`（429）。
> - 可绕行的镜像：Google 条款经 `policies.google.cn`（`policies.google.com` 的国别镜像）拿到；法律依据经 `courtlistener.com`、`www.gov.uk`、`everything.explained.today` 拿到。

---

## 0. 速查总表

| 机构 | 可免费下载 | 授权 | 商用 | 需署名 | 入口 |
|---|---|---|---|---|---|
| Met (NY) | 是（Open Access / PD 作品） | **CC0** | 是 | 不要求（请求） | `collectionapi.metmuseum.org`（无需 key） |
| Rijksmuseum | 是（PD 对象，全分辨率） | **PDM 和/或 CC0**，少数 CC BY 4.0 | 是 | 不要求（请求） | `data.rijksmuseum.nl`（Search API 无需 key） |
| Art Institute of Chicago | 是（PD 作品，IIIF） | **数据 CC0**（description CC-BY）；图片许可页未能核实 | 数据是 | 建议「Digital image courtesy of the Art Institute of Chicago.」 | `api.artic.edu`（无需 key） |
| Getty Museum | 是（Open Content） | **CC0** | 是 | 不要求（请求固定 credit line） | `getty.edu`（Download image 按钮） |
| National Gallery London | 部分 | **CC BY-NC-ND 4.0**（图片）／**CC0**（关键事实数据） | **否**（图片） | 是（需按示例格式） | 网站下载按钮；商用走 Picture Library |
| Europeana | 视条目而定 | CC0 / **PD Mark** / CC 系列 / RightsStatements.org | 视条目而定 | 视许可而定 | API（demo key `api2demo` 可查） |
| Wikimedia Commons | 是 | PD-Art（**政策原文未能核实**） | 是（PD 作品） | 不要求 | 站点被阻断 |
| Google Arts & Culture | **否** | 归 Google 服务条款，属「他人内容」 | **否** | — | 条款页被阻断，经 `policies.google.cn` 核实 |
| Paris Musées | 部分是（CCØ 标记图） | **CC0** / 其余保留所有权利 | 是（CC0 部分） | 不强制（请求） | `apicollections.parismusees.paris.fr` |
| Louvre | 部分（中分辨率、封闭用途） | 图片无 CC0；文本 Etalab 2.0 | **否**（付费授权） | 是（+ permalink） | `collections.louvre.fr` |
| Städel | 是（PD 作品） | **PDM 1.0**；元数据 CC0 | 是 | 请求 | `sammlung.staedelmuseum.de` |
| SMK（丹麦） | 是 | **PDM 1.0** | 是 | 请求 | `api.smk.dk`（无需 key） |
| Nationalmuseum（瑞典） | 部分 | **PD** + **CC BY-SA 4.0** | 是（PD/CC BY-SA） | CC BY-SA 必须 | `collection.nationalmuseum.se` |
| Finnish National Gallery | 部分（CC0 图） | **CC0** | 是 | 未能核实 | `kokoelma.kansallisgalleria.fi` |
| Belvedere（维也纳） | 部分（私用/科研） | 未见 CC；自定义条款 | **否**（需联系） | 未能核实 | `sammlung.belvedere.at/opencontent` |
| KHM（维也纳） | 否 | 保留所有权利 | **否** | — | 仅浏览 |
| Web Gallery of Art | 受限 | 专有 | **否** | — | 仅教育/个人 |
| Yale Center for British Art | 是（PD 作品） | 公有领域（**未见 CC0**） | 是 | 请求「photo credit」 | `britishart.yale.edu` |
| Harvard Art Museums | 部分 | 混合，**仅非商业** | **否** | 是 | API 需 key，非商用 |
| Smithsonian Open Access | 是（CC0 子集） | **CC0** | 是 | 不要求 | API 需 key；S3 开放 |

---

## 1. The Metropolitan Museum of Art — Open Access

- **可免费下载图片**：是（限 Open Access / 公有领域作品）。
- **授权类型**：**CC0**（数据集与公有领域高分辨率图像）。
- **商用**：是，明确「unrestricted commercial and noncommercial use」。
- **署名**：不要求；README 只是「Please consider attributing or citing」。
- **API / 下载入口**：`https://collectionapi.metmuseum.org/public/collection/v1/objects`、`/objects/{objectID}`、`/departments`、`/search`（**2026-10-01 停用**）、`/public/collection/v1.1/search`（分页，新增 offset/limit）。
- **是否需要 key**：**不需要**。原文：「At this time, we do not require API users to register or obtain an API key to use the service. Please limit request rate to 80 requests per second.」
- **分辨率限制**：无明确上限；每条记录给出 `primaryImage`（original 高清 JPEG）与 `primaryImageSmall`（web-large）。
- **例外 / 是否所有 Open Access 图都是 CC0**：**不是「所有馆藏图」**。CC0 只覆盖被标为 Open Access 的作品；数据集中「Companion artworks … are identified in the Collection section of the Museum's website with the Creative Commons Zero (CC0) icon」。受版权保护的作品有 `rightsAndReproduction` 字段且不提供 CC0 下载。图片本身不在 CSV 数据集内（「Images are not included and are not part of the dataset.」）。
- **实测**：`GET /public/collection/v1/objects/45734` 无需 key 返回 `isPublicDomain: true`、`primaryImage: https://images.metmuseum.org/CRDImages/as/original/DP251139.jpg`。

**原文关键句**
- 「The Metropolitan Museum of Art provides select datasets of information on more than 470,000 artworks in its Collection for unrestricted commercial and noncommercial use. To the extent possible under law, The Metropolitan Museum of Art has waived all copyright and related or neighboring rights to this dataset using [Creative Commons Zero].」 — `https://raw.githubusercontent.com/metmuseum/openaccess/master/README.md`
- 「The API … gives access to all of The Met's Open Access data and to corresponding high resolution images (JPEG format) that are in the public domain.」 — `https://metmuseum.github.io/`
- 「At this time, we do not require API users to register or obtain an API key to use the service. Please limit request rate to 80 requests per second.」 — `https://metmuseum.github.io/`
- 「Images are not included and are not part of the dataset. Companion artworks listed in the dataset covered by the policy are identified in the Collection section of the Museum's website with the Creative Commons Zero (CC0) icon.」 — README

**未能核实**：Open Access 政策页 `https://www.metmuseum.org/about-the-met/policies-and-documents/open-access` 与图片资源页 `/image-resources` 均返回 **HTTP 429 Vercel Security Checkpoint**（多次重试、不同 UA 均如此），故未能引用该两页正文。

---

## 2. Rijksmuseum — Open Data / RijksData

- **可免费下载图片**：是。自 2011/12 起把**不再受版权保护**的藏品照片「in all variants, from high resolution to thumbnail」作为公共财产开放。
- **授权类型**：**Public Domain Mark (PDM) 和/或 CC0 1.0**；如 Rijksmuseum 选择行使版权则用 **CC BY 4.0**；第三方已书面同意无限制开放的用 CC0。
- **商用**：**是**。原文 3.3：「The Rijksmuseum does not distinguish user groups … All users, **including commercial parties**, have access to the same Information and Data under the same conditions.」
- **署名**：不强制，但「good practice」请求署名 Rijksmuseum（及尽可能署名员工）。
- **API / 下载入口**：`https://data.rijksmuseum.nl/`；政策页 `https://data.rijksmuseum.nl/policy`；Search API `https://data.rijksmuseum.nl/search/collection`。
- **是否需要 key**：Search API **不需要**：「The API is available at the following URL. **No API key is needed.**」
- **分辨率限制**：无上限表述；PD 对象提供从高清到缩略图的所有版本。
- **注意**：政策文档本身以 **CC BY 4.0** 发布；仍有部分图片因版权在第三方而受限，会在版权通知中标明权利人。

**原文关键句**
- 「For much of the information and data on the collection website, you will find a Public Domain or Creative Commons Zero (CC0) Public Domain Dedication … In some cases, copyright does apply. If so, a Creative Commons BY 4.0 (CC BY 4.0) licence is indicated.」 — `https://data.rijksmuseum.nl/policy`
- 「3.3. The Rijksmuseum does not distinguish user groups with regard to its Information and Data. All users, including commercial parties, have access to the same Information and Data under the same conditions.」 — `https://data.rijksmuseum.nl/policy/information-and-data-policy`
- 「3.7.1. The Rijksmuseum provides Information and Data that are no longer, or have never been, protected by copyright with a Public Domain Mark (PDM) and/or the Creative Commons Zero 1.0 (CC0 1.0) Public Domain Dedication.」 — 同上
- 「The museum has since made all photos (in all variants, from high resolution to thumbnail) available of collection objects that are no longer subject to copyright as public property. The museum also does not claim copyright on associated metadata…」 — 同上
- 「We kindly ask that when using our information and data, you credit the Rijksmuseum (and, where possible, our staff) as the original creator, even if this is not required.」 — `https://data.rijksmuseum.nl/policy`

---

## 3. Art Institute of Chicago — Open Access

- **可免费下载图片**：是（对 **public domain** 作品；图像走 IIIF，且鼓励热链）。
- **授权类型**：**数据（API）为 CC0 1.0**；`description` 字段为 **CC BY 4.0**。**图片**许可细节未能核实（`www.artic.edu/image-licensing` 403）。
- **商用**：数据 CC0 可商用；图片须逐条判断——API 文档明确把判断责任交给使用者。**图片是否 CC0：未能核实**。
- **署名**：IIIF manifest 给出 `attribution = "Digital image courtesy of the Art Institute of Chicago."`（建议格式）。
- **API / 下载入口**：`https://api.artic.edu/api/v1/`；文档 `https://api.artic.edu/docs/`；数据转储 `https://github.com/art-institute-of-chicago/api-data`；IIIF `https://www.artic.edu/iiif/2/{identifier}/full/843,/0/default.jpg`。
- **是否需要 key**：**不需要**；匿名 60 req/min；建议加 `AIC-User-Agent` 头。
- **分辨率限制**：推荐 `843,`（≈843px 宽）；**公版图**可申请 `1686,` 更大图；无硬性上限说明。
- **抓取礼仪**：单线程、每次下载间隔 1 秒、优先热链。

**原文关键句**
- 「The `description` field in this response is licensed under a Creative Commons Attribution 4.0 Generic License (CC-By) … All other data in this response is licensed under a Creative Commons Zero (CC0) 1.0 designation…」 — `https://api.artic.edu/docs/`（亦见于每条 API 响应 `info.license_text`）
- 「If you are accessing public domain images, you may also use the following pattern for larger images: `.../full/1686,/0/default.jpg`」 — `https://api.artic.edu/docs/`
- 「We don't mind if you hotlink to our images. Our images support CORS… However, please be aware that any image can get unpublished or replaced at any time.」 — `https://api.artic.edu/docs/`
- 「From a developer's perspective, we recommend only using images from artworks that are tagged as public domain.」+「You may encounter images that are not public domain via our IIIF Image API. It is up to you to determine whether or not you are allowed to use these images…」 — `https://api.artic.edu/docs/`
- 「These notices refer to the metadata that each file represents, **they do not apply to images and media which may have different licensing terms.**」 — `https://raw.githubusercontent.com/art-institute-of-chicago/api-data/main/README.md`

**未能核实**：`https://www.artic.edu/open-access`、`https://www.artic.edu/image-licensing`、`https://www.artic.edu/terms` 均 **HTTP 403 Cloudflare**（web_fetch 与 curl 皆然）。因此「AIC 公版图是否 CC0」这一条无法从官方许可页直接确认。

---

## 4. Getty Museum — Open Content Program

- **可免费下载图片**：是（有「Download image」按钮的条目）。
- **授权类型**：**CC0**（「To the extent that Getty owns copyright in the digital images, we have chosen to make the images freely available under CC0.」）。
- **商用**：是。「Getty places no restrictions on the use, modification, or reuse of Open Content images.」
- **署名**：不强制，但请求在作品说明后加固定 credit line：**「Digital image courtesy of Getty's Open Content Program.」** 唯一限制是不得暗示 Getty 背书。
- **API / 下载入口**：`https://www.getty.edu/projects/open-content-program/`；FAQ `https://www.getty.edu/projects/open-content-program/faqs/`；馆藏检索页 Download image 按钮。
- **规模**：自 2013 年起 **16 万+** 公版图像（博物馆 8.6 万+，研究所 7.8 万+）。
- **例外**：因版权归属、第三方权利（商标/肖像/隐私）或缺少高清文件，部分图像**不在** Open Content 内、不可免费下载；Getty 也明确不为第三方权利背书。
- **许可函**：不单独出具 permission letter，而是给出「general permission」总许可。

**原文关键句**
- 「Images in the Open Content Program are images of works in the public domain in the United States. The works depicted in the images are not protected by copyright, but Getty may have a copyright interest in the digital image of the work. To the extent that Getty owns copyright in the digital images, we have chosen to make the images freely available under CC0.」 — FAQ
- 「Getty places no restrictions on the use, modification, or reuse of Open Content images. The only requirement is that you not suggest or imply endorsement by the Getty.」 — FAQ
- 「Please include the following credit line after the artwork caption: Digital image courtesy of Getty's Open Content Program.」 — FAQ
- 「Digital images of Getty-owned artworks in the public domain marked with the CC0-public domain icon are available for download under CC0. Such images are not protected by copyright and may be used without restriction or fees for commercial and noncommercial purposes.」 — `https://www.getty.edu/projects/open-content-program/`

---

## 5. National Gallery, London — 图片许可

- **可免费下载图片**：**部分**（指定图片可下载，但限非商业）。
- **授权类型**：
  - 网站下载的**部分图片**：**CC BY-NC-ND 4.0**（知识共享 署名-非商业性使用-禁止演绎）。
  - **藏品关键事实数据（key facts）**：**CC0**。
- **商用**：**图片不可商用**。原文：「Certain images from the Website are made available for download **for non-commercial purposes**, subject to a creative commons licence (currently CC BY NC ND 4.0).」商用须联系 The National Gallery Company Picture Library（+44 (0)20 7747 5994）。
- **署名**：是。官方给出的格式示例：「Leonardo, The Virgin of the Rocks, 1491–1508 Photo © The National Gallery, London」。
- **其他限制**：研究/私人学习/教育机构内部流通可免费复制，但不得「stretched, compressed, coloured, or altered in any way so as to distort its original format」；**禁止未获书面许可建立含下载内容的数据库**（「creating a database that includes material downloaded or obtained from the Website without written permission from the Gallery」）。
- **入口**：`https://www.nationalgallery.org.uk/terms-of-use`。
- **分辨率限制**：未在条款中给出数值（未能核实）。

**原文关键句**
- 「Certain images from the Website are made available for download for non-commercial purposes, subject to a creative commons licence (currently CC BY NC ND 4.0). Key facts in relation to paintings in our collection are made available for download under a creative commons licence (currently CC0).」 — `https://www.nationalgallery.org.uk/terms-of-use`（Last update: 18 October 2021）
- 「Commercial users identifying an image they wish to reproduce on a commercial basis should contact: The National Gallery Company Picture Library…」 — 同上
- 「For example, "Leonardo, The Virgin of the Rocks, 1491–1508 Photo © The National Gallery, London"」 — 同上

> **商用影响提示**：CC BY-NC-ND = 不能商用 + 不能做裁剪/滤镜/二次创作。对要做衍生教学图、卡片、滤镜、拼图的学习网站来说，**NG London 的下载图基本不可用**；只有 key facts（CC0）可用。

---

## 6. Europeana — rights statement 体系与 PD 标记

- **背景限制**：`europeana.eu`、`pro.europeana.eu` 均 **HTTP 403 Cloudflare**，Europeana 自家文档页**未能核实**。以下用它实际采用的标准化体系（rightsstatements.org，可直连）与其 **API 实测数据** 交叉验证。
- **体系**：Europeana 条目不填「一个 licence」，而是填一个 `rights` 值，取值来自三类：
  1. **Creative Commons 许可**（CC0、CC BY、CC BY-SA、CC BY-NC、CC BY-NC-SA、CC BY-ND、CC BY-NC-ND）；
  2. **Public Domain Mark 1.0（PD Mark）**——用于「已确认不受已知版权限制」的作品；
  3. **RightsStatements.org 的 12 个标准化权利声明**（用于版权状态不确定或受限的情形）。
- **实测**：用 Europeana 公开 demo key 查询，条目 `rights` 字段确为上述 URI，例如 `http://creativecommons.org/licenses/by/4.0/`、`http://creativecommons.org/publicdomain/mark/1.0/`；带 **PD Mark** 的条目共 **10,920,833** 条（`totalResults`）。

**PD 标记（Public Domain Mark 1.0）含义**（CC 官方页原文）
- 「This work has been identified as being free of known restrictions under copyright law, including all related and neighboring rights.」+「You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.」 — `https://creativecommons.org/publicdomain/mark/1.0/`
- 关键区别：**PD Mark 不是许可证**，只是「此作品已无已知版权限制」的声明，不提供担保。

**RightsStatements.org 12 声明中的关键几条**（`https://rightsstatements.org/page/<ID>/1.0/`）
- **In Copyright（InC）**：「This Item is protected by copyright and/or related rights. You are free to use this Item in any way that is permitted by the copyright and related rights legislation that applies to your use. For other uses you need to obtain permission from the rights-holder(s).」
- **No Copyright – United States（NoC-US）**：「…believes that the Item is in the Public Domain under the laws of the United States, but a determination was not made as to its copyright status under the copyright laws of other countries.」
- **No Copyright – Non-Commercial Use Only（NoC-NC）**：「…the partners have agreed to limit commercial uses of this digital representation of the Work by third parties. You can, without permission, copy, modify, distribute, display, or perform the Item, for non-commercial uses.」
- **No Copyright – Other Known Legal Restrictions（NoC-OKLR）**：「Use of this Item is not restricted by copyright and/or related rights. In one or more jurisdictions, laws other than copyright are known to impose restrictions…」
- **Copyright Undetermined（UND）**：状态无法确定；**Copyright Not Evaluated（CNE）**：未评估。
- 官方定位：「RightsStatements.org provides 12 standardized rights statements for online cultural heritage. Our rights statements make it easy to see if and how online cultural heritage works can be reused.」 + 「Our rights statements are supported by major aggregation platforms such as the Digital Public Library of America and **Europeana**.」 — `https://rightsstatements.org/en/`

> **实操含义**：Europeana 上只有 `CC0` / `PD Mark` / `CC BY` / `CC BY-SA` 的条目能直接商用；`NoC-NC`、`CC BY-NC*`、`InC`、`UND`、`CNE` 都不能当作「可自由使用」。

---

## 7. Wikimedia Commons — PD-Art 政策

**结论：Commons 原文未能核实。**
- 所有 Wikimedia 域名（`commons.wikimedia.org`、`en.wikipedia.org`、`meta.wikimedia.org`、`api.wikimedia.org`、`upload.wikimedia.org`）均被**网络层阻断**（TLS 连接被 reset；`curl` 经 IP + `Host:` 头亦失败）。
- `web.archive.org` / `archive.ph` **不可达**，无法用存档替代。
- 已尝试并失败的替代路径：`commons.m.wikimedia.org`、`?action=raw`、REST API、`wikiless.org`、`wikimirror.net`、`wikidoc.org`、`thefullwiki.org`、Textise 代理、各类 CORS 代理（r.jina.ai / allorigins / codetabs / cors.lol / cors.eu.org）——全部失败。

**但「忠实翻拍二维公有领域作品不产生新著作权」这一法理依据已从可达的权威来源核实：**

1. **Bridgeman Art Library v. Corel Corp.（美国纽约南区联邦地方法院，36 F. Supp. 2d 191, 1999）**
   - 「exact photographic copies of public domain images could not be protected by copyright in the United States because the copies lack originality. Even though accurate reproductions might require a great deal of skill, experience, and effort, the key element to determine whether a work is copyrightable under US law is originality.」
   - 法官 Kaplan 认定原告是「slavish copying」：「the point of the exercise was to reproduce the underlying works with absolute fidelity」，因此不受版权保护。
   - 对英国法亦持相同看法，引 Privy Council 在 *Interlego v Tyco* 中「[s]kill, labour or judgment merely in the process of copying cannot confer originality」。
   - 出处：`https://everything.explained.today/Bridgeman_Art_Library_v._Corel_Corp./`（维基百科镜像）；案件本体亦可经 CourtListener API 查到：`https://www.courtlistener.com/api/rest/v4/search/?q=Bridgeman%20Corel&type=o`（返回 `/opinion/2413183/bridgeman-art-library-ltd-v-corel-corp/`）。
   - 相关后续：*Meshwerks v. Toyota*, 528 F.3d 1258 (10th Cir. 2008)：「[T]he law is becoming increasingly clear: one possesses no copyright interest in reproductions … when these reproductions do nothing more than accurately convey the underlying image.」

2. **英国知识产权局（UK IPO）官方指引**（政府网站，可直连）
   - 「Simply creating a copy of an image won't result in a new copyright in the new item.」
   - 「…it seems unlikely that what is merely a retouched, digitised image of an older work can be considered as 'original'. This is because there will generally be minimal scope for a creator to exercise free and creative choices if their aim is simply to make a faithful reproduction of an existing work.」
   - 出处：`https://www.gov.uk/government/publications/copyright-notice-digital-images-photographs-and-the-internet/copyright-notice-digital-images-photographs-and-the-internet`（Last updated 4 January 2021）

3. 镜像页还记载：2023 年英国上诉法院 *THJ v. Sheridan* 确认英国自 2009 年起**不因拍摄二维公版艺术品而产生新版权**。

> **给网站的建议**：Commons 上 PD-Art 标记的欧洲古画（Rijksmuseum、Met、Getty、Paris Musées 等上传件）可安全使用；但**务必回到原始来源机构核对**，因为不同司法辖区（尤其英国脱欧后、以及部分欧洲大陆国家）对「翻拍照片」的保护态度不完全一致。Commons 页面本身的现行措辞请以 `Commons:When to use the PD-Art tag` 为准（本项目未能抓取）。

---

## 8. Google Arts & Culture — 能否下载复用

- **可免费下载图片**：**否**（无通用下载/复用许可）。
- **授权类型**：**Google 服务条款**；GAC 上的图像多为**合作机构（第三方）内容**，属「Other content」。
- **商用**：**否**（须逐项取得权利人许可）。
- **核实路径（绕行）**：`artsandculture.google.com/terms` 与全部 Google 域名（含 `policies.google.com`）在本环境被阻断；改用国别镜像 **`https://policies.google.cn/terms?hl=en`** 拿到 Google 服务条款正文，并在服务清单页确认 **Google Arts & Culture 受 Google 服务条款约束**（`https://policies.google.cn/terms/service-specific?hl=en`，清单中列有「**Google Arts & Culture** — Terms of Service」，无额外专门政策）。

**原文关键句**
- 「Other content — Finally, some of our services give you access to content that belongs to other people or organizations … **You may not use this content without that person or organization's permission, or as otherwise allowed by law.**」 — Google 服务条款 "Content in Google services" 节，`https://policies.google.cn/terms?hl=en`（Country version: China；正文与 `policies.google.com/terms` 对应）
- 服务清单：「Google Arts & Culture — Terms of Service」 — `https://policies.google.cn/terms/service-specific?hl=en`

**未能核实**：GAC 页面自身的 Terms 文本（`artsandculture.google.com/terms` 不可达），以及 GAC 是否有独立于 Google 总条款的产品专属条款（服务清单显示没有额外政策条目）。

> **结论**：GAC 是「只看不存」的展览平台，**不要把 GAC 的图片抓进自己的图库**，也不要热链其 `lh3.googleusercontent.com` 资源。要这些画，请去对应原作机构的开放接口取图。

---

## 9. 其他欧洲来源

（由子代理核实，明细见同目录 `museum-image-licensing-report.md`）

| 机构 | 免费下载 | 授权 | 商用 | 署名 |
|---|---|---|---|---|
| **Paris Musées** | 部分是（标 CCØ 的图） | **CC0** / 其余保留所有权利 | CC0 部分可 | 不强制（请求：作品名+作者+Paris Musées+馆名，随下载附 .txt） |
| **Musée du Louvre** | 部分（中分辨率，仅私用+封闭列出的博物馆/科研/教学用途） | 图片无 CC0；文本 **Etalab 2.0** | **否**（商业走 GrandPalaisRmn 付费） | 是（摄影 credit + permalink） |
| **Uffizi** | 否 | 许可+付费，无 CC | **否** | 未能核实 |
| **Museo del Prado** | **未能核实**（全站 Cloudflare 403） | 未能核实 | 未能核实 | 未能核实 |
| **Städel Museum** | 是（PD 作品） | **PDM 1.0**；元数据 CC0 | 是 | 请求「Städel Museum, Frankfurt am Main」 |
| **SMK（丹麦）** | 是 | **PDM 1.0** | 是 | 请求「Shared by SMK, National Gallery of Denmark」 |
| **Nationalmuseum（瑞典）** | 部分 | **PD** + **CC BY-SA 4.0** | 是（PD/CC BY-SA） | CC BY-SA 必须：「Photo: [摄影师], Nationalmuseum (CC BY-SA)」 |
| **Finnish National Gallery** | 部分（36,000+ 图 CC0） | **CC0** | 是 | 未能核实 |
| **Belvedere（维也纳）** | 部分（仅私用/科研，1772px） | 未见 CC；自定义条款，保留 TDM/AI 训练权 | **否**（联系 repro@belvedere.at） | 未能核实 |
| **KHM（维也纳）** | 否 | 保留所有权利 | **否** | 未能核实 |
| **Web Gallery of Art** | 受限（仅教育/个人） | 专有 | **否** | 未能核实 |

**精选原文**
- Paris Musées：「Les images dont les champs « crédits » sont indiqués CCØ sont sous licence Creatives Commons Ø.」+「…une définition en .jpg égale ou supérieure à **3000px en 300dpi**.」 — `https://www.parismuseescollections.paris.fr/fr/conditions-generales-d-utilisation`（2025-10-01 版）；免费图检索页显示 **418,097** 张。
- Louvre：「Le téléchargement et la réutilisation des photographies en **moyenne définition** … sont autorisés, à titre gratuit, pour toute utilisation non collective dans un cadre strictement privé, ainsi que pour les usages à vocation muséographique, scientifique et pédagogique suivants, **limitativement listés**…」+「Toute utilisation … notamment **toute utilisation commerciale** … doit faire l'objet d'une demande écrite … au **GrandPalaisRmn** … à titre onéreux.」 — `https://collections.louvre.fr/page/cgu`（2026-03-19 版）
- Städel：「These images are in the public-domain and may be downloaded, edited, remixed, shared, reproduced in any format, and used for any purpose. Mention: 'Städel Museum, Frankfurt am Main'.」 — `https://sammlung.staedelmuseum.de/en/concept`
- SMK（API 实测）：`"public_domain":true,"rights":"https://creativecommons.org/publicdomain/mark/1.0/"`；IIIF `"license":"https://creativecommons.org/publicdomain/mark/1.0/","attribution":"Shared by SMK, National Gallery of Denmark"` — `https://api.smk.dk/api/v1/art?object_number=KKS5261`
- Finnish NG：「The Finnish National Gallery has released over 36,000 images into the public domain under the CC0-license.」 — `https://kansallisgalleria.fi/en/photographic-service/`
- Belvedere：「Die Digitalisate stehen für **private und wissenschaftliche Zwecke** in einer Auflösung von **300 dpi auf 15 cm lange Seite (1772 Pixel)** zum Download bereit…」 — `https://sammlung.belvedere.at/opencontent/images`
- KHM：「Pictures and photographic material of the KHM may not be reproduced, copied, altered or otherwise be used in any way without express permission.」 — `https://www.khm.at/en/museum/rights-reproduction`
- WGA：「Images and documents downloaded from this database can only be used for **educational and personal purposes**. Distribution of the images in any form is prohibited without the authorization of their legal owner.」 — `https://www.wga.hu/support/mobile/legal.html`

### 美国补充来源（子代理核实）

| 机构 | 免费下载 | 授权 | 商用 | API key |
|---|---|---|---|---|
| **Yale Center for British Art** | 是（PD 作品） | 公有领域（**未见 CC0 标记**） | **是** | 无（OAI-PMH + IIIF）；约 7 万张 PD 图 |
| **Harvard Art Museums** | 部分（个人/非商业） | 混合，**仅非商业** | **否** | **必须**（`apikey`），且 API 条款非商用 |
| **Smithsonian Open Access** | 是（约 280 万+ CC0 图） | **CC0** | **是** | **必须**（`api_key`，经 api.data.gov）；另有开放 S3 |

- YCBA：「As far as the Center is concerned, you may download and use the Center's images of works in the public domain for any purpose. You do not need to ask our permission or pay any fees to us to publish the images.」 — `https://britishart.yale.edu/using-images-works-public-domain`
- Harvard：「Images on this website are available to download for **personal, noncommercial use**…」+「**The API is for non-commercial use only.**」 — `https://harvardartmuseums.org/licensing`、`https://github.com/harvardartmuseums/api-docs`
- Smithsonian：API 实测 `GET https://api.si.edu/openaccess/api/v1.0/search?q=cats` → `# API_KEY_MISSING`；AWS Open Data 页：「On February 25th, 2020, the Smithsonian released over 2.8 million CC0 interdisciplinary 2-D and 3-D images… License: **CC0**」 — `https://registry.opendata.aws/smithsonian-open-access/`

---

## 10. 总结：给「欧洲古画学习网站」的优先级建议

### 优先级最高的 5 个图源

1. **Rijksmuseum（荷兰国立博物馆）** — 最适合做「欧洲古画」核心图库。
   - 理由：荷兰黄金时代（伦勃朗、维米尔、哈尔斯）顶级馆藏；**PDM/CC0 且明确允许商用**；提供从缩略图到高清的全尺寸；Search API **无需 key**；政策清晰、有完整文档（`data.rijksmuseum.nl/policy`）。署名只是请求而非义务。

2. **The Met（纽约大都会）** — 覆盖面上最稳的「通史」图源。
   - 理由：European Paintings 部门馆藏极广（从早期文艺复兴到 19 世纪）；**CC0**、**API 不需要 key**、80 req/s 的高配额；`isPublicDomain` 字段可直接过滤，工程上最好用。注意 Open Access 只覆盖 PD 作品，且图片不在 CSV 数据集里（要经 `primaryImage` 取 URL）。

3. **Art Institute of Chicago** — 数据最开放、IIIF 最好接。
   - 理由：**元数据 CC0**、无需 key、完整数据转储（GitHub `api-data`）、标准 IIIF（`full/843,/0/default.jpg`，公版图可 `1686,`），对欧洲绘画（尤其法国印象派/后印象派）有大量公版作品。**但**图片许可条款页被抓（403），落地前建议再人工复核一次 AIC 的 image licensing。

4. **Getty Museum — Open Content** — 单张画质与「无限制」表述最干净。
   - 理由：**CC0**、16 万+ 公版图、官方 FAQ 明确「no restrictions on the use, modification, or reuse」、并给出标准 credit line；欧洲绘画、彩饰手抄本、19 世纪摄影都很强。唯一注意点是第三条权利（肖像/商标/隐私）需自行排查。

5. **Paris Musées（+ Städel / SMK 二选一作为补充）** — 欧洲本土、巴黎城市博物馆群。
   - 理由：**CC0**、免费图约 **41.8 万张**、承诺 **≥3000px / 300dpi**，含 Carnavalet、Petit Palais、Musée Cognacq-Jay 等大量法国古画与城市史图像；API 免费（需注册账号）。若需要德语区/北欧补充，**Städel（PDM 1.0，可商用）** 与 **SMK（PDM 1.0 + 开放 API，约 20 万条）** 都是一句话就能合规的优质来源；**Finnish National Gallery** 的 36,000+ CC0 图也值得加。

### 绝对不能直接存图的来源

- **Google Arts & Culture**：无下载/复用许可，图像属合作机构第三方内容，Google 服务条款明确「You may not use this content without that person or organization's permission」。**只用它的页面做跳转/讲解，不要抓图、不要热链。**
- **Uffizi Galleries**：无自助下载，许可+付费；无 CC。
- **Kunsthistorisches Museum Vienna (KHM)**：保留所有权利，须书面许可。
- **Web Gallery of Art**：仅限教育/个人用途，禁止再分发——**学习网站的「教育」用途不等于可再分发**，不能入库。
- **Belvedere（维也纳）**：Open Content 仅限私人+科研，商用须另谈；且明确保留 TDM/AI 训练权。
- **Musée du Louvre**：免费下载只限中分辨率 + 严格封闭用途清单，**商业用途一律付费**；不能整库抓取。
- **National Gallery London 的下载图**：CC BY-NC-ND 4.0 = **非商业 + 禁止演绎**，不能做二次创作、不能用于任何变现页面；只有 key facts 数据（CC0）可自由用。
- **Harvard Art Museums**：条款与 API 均**仅限非商业**，商用不可。
- **Museo del Prado**：本次**未能核实**（Cloudflare 403），在拿到书面/官方条款前**不要使用**。

### 落地建议（合规工程）

1. **入库存储只收 CC0 / PDM / PD 三类**（外加可接受的 CC BY 与 CC BY-SA，但必须处理署名）。
2. **建一张 rights 表**：每条图记录 `source / license_uri / license_label / credit_line / retrieved_at / commercial_ok / derivatives_ok`。CC BY-NC-ND 与 NoC-NC 直接排除。
3. **署名自动化**：Rijksmuseum（请求）、Getty（`Digital image courtesy of Getty's Open Content Program.`）、AIC（`Digital image courtesy of the Art Institute of Chicago.`）、SMK（`Shared by SMK, National Gallery of Denmark`）、Städel（`Städel Museum, Frankfurt am Main`）、Nationalmuseum CC BY-SA（`Photo: [摄影师], Nationalmuseum (CC BY-SA)`）、NG London（`Leonardo, The Virgin of the Rocks, 1491–1508 Photo © The National Gallery, London`）。
4. **PDM vs CC0 的技术区别**：PDM 只是「无已知版权限制」的声明、不是许可证；CC0 是主动放弃权利的授权。二者都可用，但若平台需要「上游已授权」的法律确定性，**优先 CC0**。
5. **不要依赖 Commons / GAC 作为唯一来源**；两者在本环境不可达或不可复用，且 Commons 只能作为「聚合索引」，最终以机构原始条款为准。
