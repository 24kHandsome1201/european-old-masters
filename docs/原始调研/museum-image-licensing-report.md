# European Art Museum Image-Licensing Verification Report

**Method:** All findings below come from pages I actually fetched with `web_fetch` during this session. Nothing is from memory. Where a page could not be reached or no licensing statement could be found, the field is marked **未能核实 (could not verify)** together with the exact URLs attempted.

**Environment limitations encountered (important):**
- The `web_search` tool was not used (reported broken by the requester).
- **The Wayback Machine was unreachable.** Every attempt failed with a network error (`TypeError: fetch failed`):
  - `https://web.archive.org/web/2024/https://www.museodelprado.es/`
  - `https://web.archive.org/web/20240601000000/https://www.museodelprado.es/en/banco-de-imagenes`
  - `https://web.archive.org/web/2024/https://www.museodelprado.es/en/banco-de-imagenes`
  - `http://archive.org/wayback/available?url=museodelprado.es/en/banco-de-imagenes`
  - `https://archive.ph/newest/https://www.wga.hu/info/copyright.html`
  **Therefore no page in this report was verified via a Wayback snapshot.**
- Museu Nacional del Prado (`museodelprado.es`) is fully behind a Cloudflare JavaScript challenge; every request returned HTTP 403 "Just a moment..." even through third-party proxies.

**Page-fetch date context:** the sites themselves self-report dates in 2026 (e.g. Louvre CGU "dernière mise à jour : 19 mars 2026"; Belvedere "© 2026"), i.e. these are the live pages as served at fetch time.

---

## 1. Paris Musées (Paris Musées / Musées de la Ville de Paris)

- **Institution:** Paris Musées — city of Paris museums (Musée Carnavalet, Petit Palais, Musée d'Art Moderne de Paris, Musée Cognacq-Jay, Maison de Victor Hugo, Musée Cernuschi, Palais Galliera, Musée de la Vie romantique)
- **Can images be freely downloaded?** **Partial — yes for CC0-marked images.** The portal distinguishes CC0 images from "Tous droits réservés" images.
- **License type:** **CC0 (Creative Commons Zero)** for images tagged "CCØ"; all other images "Tous droits réservés" (all rights reserved, view-only).
- **Commercial use allowed?** **Yes for CC0 images** (CC0 permits any use). **No** for the remaining copyrighted images.
- **Attribution required?** Legally no under CC0, but Paris Musées contractually requires/requests credit: title of the work, artist name, "Paris Musées" and the museum name. A `.txt` credit file is supplied with each CC0 download.
- **API / download entry URL:**
  - Portal: `https://www.parismuseescollections.paris.fr/`
  - Free-image browse: `https://www.parismuseescollections.paris.fr/fr/recherche/image-libre/1` (page states **418 097 free images**)
  - API (free, account registration required): `http://apicollections.parismusees.paris.fr/`
- **Resolution limits:** CC0 downloads are high-definition; the CGU promises **≥ 3000 px / 300 dpi JPG** with daily updates.

**Key quotations (original + source):**
> « Les images dont les champs « crédits » sont indiqués CCØ sont sous licence Creatives Commons Ø. »
> (Images whose "credits" field is marked CCØ are under the Creative Commons Zero licence.)
— https://www.parismuseescollections.paris.fr/fr/conditions-generales-d-utilisation

> « …l'utilisateur à mentionner le titre de l'œuvre, nom de l'auteur de l'œuvre représentée sur la photographie au minimum ainsi que Paris Musées et le nom du musée. Ces informations sont regroupées dans un fichier .txt fourni à chaque téléchargement d'œuvres placées sous licence CCØ. »
> (…the user must mention the title of the work, the name of the author, and at minimum Paris Musées and the museum name. This information is grouped in a .txt file supplied with each CC0 download.)
— same URL

> « Télécharger des reproductions d'œuvres en haute héfinition sous la licence Creative Commons CC0 : Paris Musées effectue des mises à jour journalières pour donner à l'utilisateur une définition en .jpg égale ou supérieure à 3000px en 300dpi. »
— same URL

> « L'ensemble des images présentes sur le portail … sont soit placées sous licence Creative Commons, soit demeurent « Tous droits réservés » à leurs auteurs ou aux ayants-droit des auteurs. »
— same URL

> « L'API de Paris Musées est accessible via http://apicollections.parismusees.paris.fr/ … Les contenus sont mis à disposition des utilisateurs par Paris Musées à titre gratuit. »
> (The Paris Musées API is accessible at … Content is made available to users free of charge.)
— same URL

> On the portal homepage, a featured CC0 work is credited: « … CC0 Paris Musées / Musée Cognacq-Jay … Cette œuvre fait partie des reproductions numériques d'œuvres accessibles librement grâce à l'Open Content. »
— https://www.parismuseescollections.paris.fr/

**Notes:** The French CGU is the substantive version (updated 01/10/2025). The English CGU page (`/en/general-terms-and-conditions-of-use`) exists but renders essentially empty, so the French text is the citable source.

---

## 2. Musée du Louvre (Louvre Museum)

- **Institution:** Musée du Louvre / Louvre Museum (collections site also covers Musée national Eugène-Delacroix)
- **Can images be freely downloaded?** **Partial.** Medium-definition photographs of **out-of-copyright** works can be downloaded free, but only for a **closed list** of non-commercial/museum/scientific/teaching uses. All other uses (including all commercial use) require a paid licence.
- **License type:** **Not CC0.** Free-use permission limited by the CGU for public-domain work photographs; **commercial licensing via GrandPalaisRmn (paid)**. Textual metadata is under the **French Etalab Open Licence 2.0** (attribution required; declared compatible with CC BY).
- **Commercial use allowed?** **No, not free** — any commercial use (derivative products, audiovisual/multimedia production, other print editions) must be requested in writing and is licensed **for a fee** by GrandPalaisRmn.
- **Attribution required?** **Yes.** For photographs: the photo credit exactly as shown on the collections site **plus the permalink** of the object record. For textual metadata under Etalab: attribution of source (at minimum citing the Musée du Louvre) and last-update date.
- **API / download entry URL:**
  - Collections database: `https://collections.louvre.fr/` (states "plus de 500 000 œuvres")
  - Terms: `https://collections.louvre.fr/page/cgu`
  - Commercial image licensing portal: `https://photo.grandpalaisrmn.fr/`
- **Resolution limits:** Only **"moyenne définition" (medium-definition)** photographs are free; high-resolution is not offered free.
- **Exclusions:** ADAGP-repertoire works and specified living/recent artists (Kiefer, Twombly, Braque, etc.) cannot be reproduced without rights-holder permission; GrandPalaisRmn photos of other institutions' works need that institution's prior agreement; text/data mining for AI training on ADAGP works is expressly prohibited.

**Key quotations (original, French) + source URL:**
> « Le téléchargement et la réutilisation des photographies en moyenne définition figurant sur le site internet des collections et représentant des œuvres non protégées au titre du droit d'auteur … sont autorisés, à titre gratuit, pour toute utilisation non collective dans un cadre strictement privé, ainsi que pour les usages à vocation muséographique, scientifique et pédagogique suivants, limitativement listés : … »
— https://collections.louvre.fr/page/cgu

> « Toute utilisation d'une ou plusieurs Photographie(s) doit impérativement être accompagnée du crédit photographique tel que figurant sur le site internet des collections, ainsi que du permalien de la notice d'œuvre où a été téléchargée la Photographie. »
— same URL

> « Toute utilisation autre que celles limitativement listées à l'article 4.1.1.2 a. ci-avant, et notamment toute utilisation commerciale … doit faire l'objet d'une demande écrite adressée par l'Utilisateur au GrandPalaisRmn via le site internet de son agence photographique https://photo.grandpalaisrmn.fr/. … De telles utilisations sont consenties à titre onéreux, aux tarifs pratiqués par le GrandPalaisRmn. »
— same URL

> « Les contenus textuels des notices d'œuvres et des albums thématiques … sont des informations publiques mises à disposition sous licence Ouverte « Etalab » … L'Utilisateur dispose d'un droit non exclusif et gratuit de libre réutilisation des Informations, à des fins commerciales ou non, dans le monde entier et pour une durée illimitée… »
— same URL

> « L'ADAGP interdit expressément toute reproduction des œuvres de son répertoire et des données qui s'y rapportent … en vue de fouilles de textes et de données, en particulier celles destinées à alimenter ou entraîner des dispositifs d'intelligence artificielle… »
— same URL

**Note on `https://www.louvre.fr/`:** fetched successfully (HTTP 200); it is the visitor-facing homepage and **carries no image-licensing/open-access statement**. The licensing terms live on `collections.louvre.fr`.

---

## 3. Uffizi Galleries (Le Gallerie degli Uffizi), Florence

- **Institution:** Le Gallerie degli Uffizi / Uffizi Galleries (Uffizi, Palazzo Pitti, Giardino di Boboli, Corridoio Vasariano)
- **Can images be freely downloaded?** **No.** There is no self-service free download. Image supply/permission is handled by the museum's photographic archive and commercial department; requests must be submitted by form/e-mail, and fees apply under Italian ministerial tariff rules.
- **License type:** **Unclear / not a Creative Commons licence — permission-and-fee-based ("concessione/autorizzazione").** No CC mark found on the pages fetched.
- **Commercial use allowed?** **Not free; only by authorisation**, under a fee schedule (DM 108 of 21 March 2024, ex DM 161/2023; artt. 107–108 D.Lgs 42/2004).
- **Attribution required?** **未能核实** — no explicit attribution string was stated on the pages I fetched.
- **API / download entry URL:**
  - Professional services hub: `https://www.uffizi.it/servizi-professionali`
  - Editorial use: `https://www.uffizi.it/servizi-professionali/pubblicazioni`
  - Promotional/commercial use: `https://www.uffizi.it/servizi-professionali/uso-di-immagini-di-opere`
  - Photographic archive & online inventories: `https://fotoinventari.uffizi.it/`
  - Request forms (PDF): commercial-use form and study/research-use form are linked from the editorial-use page.
  - Contacts: `ga-uff.fotografico@cultura.gov.it` (image supply); `ga-uff.permessi@cultura.gov.it` (permissions)
- **Resolution limits:** 未能核实 (not published on the pages fetched; high-res supplied on order via the photographic service).
- **Collection pages:** `https://www.uffizi.it/opere/cerca` (works search) — I did not find any download licence on the site.

**Key quotations (Italian) + source URL:**
> « Il Dipartimento Valorizzazione e Strategie economiche si occupa delle concessioni e autorizzazioni all'uso delle immagini per finalità promozionali e commerciali, ai sensi degli artt. 107-108 del D.Lgs 42/2004 e ss.mm.ii. e del DM 108 del 21 marzo 2024 "Linee guida per la determinazione degli importi minimi dei canoni e dei corrispettivi per la concessione d'uso dei beni in consegna agli istituti e luoghi della cultura del Ministero della cultura"… »
— https://www.uffizi.it/servizi-professionali/uso-di-immagini-di-opere

> « Il Gabinetto Fotografico e il Dipartimento Valorizzazione e Strategie economiche si occupano della fornitura, concessione e autorizzazione all'uso delle immagini per finalità editoriali… »
— https://www.uffizi.it/servizi-professionali/pubblicazioni

> Attachment labels on the editorial-use page: « Modulo richiesta pubblicazione immagini per usi di studio e ricerca » and « Modulo richiesta pubblicazione immagini per usi commerciali » (request forms for study/research use and for commercial use).
— https://www.uffizi.it/servizi-professionali/pubblicazioni

**Conclusion:** consistent with the Galleries' known pay-for-image practice — **view-only on the website; every reuse requires an authorised, usually paid, grant.**

---

## 4. Museo Nacional del Prado — **未能核实 (could not verify)**

**Nothing could be verified.** Every attempt to reach the Prado failed with an HTTP 403 Cloudflare JavaScript challenge ("Just a moment...", `cf_chl` managed challenge). The Wayback Machine was also unreachable from this environment.

**URLs / methods attempted (all failed):**
- `https://www.museodelprado.es/` → HTTP 403
- `https://www.museodelprado.es/en/banco-de-imagenes` → HTTP 403
- `https://www.museodelprado.es/en/legal-notice` → HTTP 403
- `https://www.museodelprado.es/en/explore/opendata` → HTTP 403
- `https://museodelprado.es/en/banco-de-imagenes` → redirect back to www (403)
- Via CORS proxies: `https://api.allorigins.win/raw?url=…` (timeout; `/get?url=…` returned the Cloudflare 403 HTML), `https://api.codetabs.com/v1/proxy?quest=…` (HTTP 522), `https://corsproxy.io/?url=…` (401 API key required), `https://r.jina.ai/…` (network failure), `https://whateverorigin.org/get?url=…` (400)
- Wayback: `https://web.archive.org/web/2024/…` and `http://archive.org/wayback/available?…` → both network-unreachable
- Search discovery: `https://www.mojeek.com/search?q=…` (HTTP 403 bot block), `https://lite.duckduckgo.com/lite/?q=…` (network failure), `https://searx.be/search?q=…` (network failure)
- Spanish open-data catalogue API `https://datos.gob.es/apidata/catalog/dataset?q=prado` → HTTP 400 (endpoint/shortname error)

**Fields:** Can images be freely downloaded — **未能核实**; License type — **未能核实**; Commercial use — **未能核实**; Attribution — **未能核实**; API/download URL — **未能核实**; Resolution limits — **未能核实**.

---

## 5. Städel Museum, Frankfurt am Main

- **Institution:** Städel Museum (Digital Collection: "Digitale Sammlung")
- **Can images be freely downloaded?** **Yes, for public-domain works** — direct download from the object page. Images of in-copyright works are not free (handled by the Artothek picture agency, extra fees).
- **License type:** **Public Domain Mark 1.0** for images of public-domain artworks (the page links to `https://creativecommons.org/publicdomain/mark/1.0/`); **CC0 1.0** for the metadata via the OAI interface.
- **Commercial use allowed?** **Yes** for public-domain images — "used for any purpose", and the page explicitly allows editing, remixing and any-format reproduction.
- **Attribution required?** Not legally required for PDM, but the museum requests the mention: **«Städel Museum, Frankfurt am Main»**.
- **API / download entry URL:**
  - Digital Collection: `https://sammlung.staedelmuseum.de/en`
  - Object pages carry a download icon for PD images
  - OAI metadata interface: `https://sammlung.staedelmuseum.de/en/oai` (page calls it "./oai"); metadata formats Dublin Core and LIDO
  - In-copyright image licensing: `https://www.artothek.de/`
- **Resolution limits:** 未能核实 as a numeric cap (images are described as "zoomable, hi-res"; the page says PD images are offered via the Digital Collection without stating a pixel limit on the fetched page).

**Key quotations (English) + source URL — all from `https://sammlung.staedelmuseum.de/en/concept`:**
> "The Städel Museum makes all images of artworks in the public-domain (i.e. artworks no longer under copyright protection) available for download free of charge via the Digital Collection. These images are in the public-domain and may be downloaded, edited, remixed, shared, reproduced in any format, and used for any purpose. Mention: 'Städel Museum, Frankfurt am Main'."

> "The public-domain images can be downloaded directly from the relevant object page, just click on the download icon below the image."

> "For images of copyrighted works or additional service and consulting, please contact the picture agency we partner with: Artothek … Please note: for copyrighted works additional fees apply."

> "Metadata on the Städel Museum's public-domain works is available to the public via an OAI interface. The metadata is available under the CC0 1.0 license and contains all relevant information and tags to the individual artworks. For licensing reasons, audio-guides and videos as well as curatorial texts on the artworks are not included."

Also stated: "All digital offerings from the Städel are available for free and provide unlimited, global access to a common cultural heritage."

---

## 6. SMK – Statens Museum for Kunst (National Gallery of Denmark)

- **Institution:** SMK – Statens Museum for Kunst / National Gallery of Denmark
- **Can images be freely downloaded?** **Yes** for public-domain objects — the API exposes a direct download endpoint and full-resolution IIIF images.
- **License type:** **Public Domain Mark 1.0** (`https://creativecommons.org/publicdomain/mark/1.0/`) — verified per object in the API and in the IIIF manifest `license` field.
- **Commercial use allowed?** **Yes** (Public Domain Mark places the work in the public domain; no restriction indicated in the metadata).
- **Attribution required?** Not legally (PDM), but the IIIF manifest carries the requested attribution string: **"Shared by SMK, National Gallery of Denmark"**.
- **API / download entry URL:**
  - Open-data front end: `https://open.smk.dk/`
  - API query used: `https://api.smk.dk/api/v1/art/search?keys=*&limit=1` (returned `"found":202537`)
  - Per-object record: `https://api.smk.dk/api/v1/art?object_number=KKS5261`
  - Image download: `https://api.smk.dk/api/v1/download/…` (per-object `image_native` field)
  - IIIF manifest: `https://api.smk.dk/api/v1/iiif/manifest?id=KKS5261`
  - IIIF image service: e.g. `https://iip.smk.dk/iiif/jp2/qz20sx771_kks5261.tif.jp2`
- **Resolution limits:** No stated cap found; images are **full-resolution** — the example object is 4992 × 6287 px, native TIFF ~32 MB (`"image_mime_type":"image/tiff","image_size":32476791`), with IIIF serving `full/full/0/native.jpg`.

**Key quotations / captured data + source URLs:**
> API JSON (one object of the 202,537 found): `"public_domain":true,"rights":"https://creativecommons.org/publicdomain/mark/1.0/"`
— `https://api.smk.dk/api/v1/art/search?keys=*&limit=1`

> IIIF manifest: `"license":"https://creativecommons.org/publicdomain/mark/1.0/","attribution":"Shared by SMK, National Gallery of Denmark"`
— `https://api.smk.dk/api/v1/iiif/manifest?id=KKS5261`

> `"frontend_url":"https://open.smk.dk/artwork/image/KKS5261"` and `"image_native":"https://api.smk.dk/api/v1/download/…/KKS5261.jpg"`
— same API response

**未能核实:** the *narrative* policy text on `https://open.smk.dk/` and `https://www.smk.dk/` — those pages are JavaScript-rendered and returned only the site title ("SMK Open" / "SMK – Statens Museum for Kunst") with no readable body. URLs tried: `https://open.smk.dk/en`, `https://open.smk.dk/en/about`, `https://open.smk.dk/en/api`, `https://open.smk.dk/en/faq`, `https://www.smk.dk/en/`, `https://docs.smk.dk/` (DNS not found), `https://github.com/NationalGalleryOfDenmark` (HTTP 404). **The per-object API/IIIF licence data above, however, was fetched directly and is authoritative for the licence actually applied.**

---

## 7. Nationalmuseum, Stockholm

- **Institution:** Nationalmuseum / National Museum of Sweden (art and design)
- **Can images be freely downloaded?** **Partial.** Public-domain (PD) images are free; some images are CC BY-SA; in-copyright artist works are marked "© konstnären / artist / Bildupphovsrätt i Sverige" and are **not** free.
- **License type:** **Public Domain (marked "PD")** and **CC BY-SA 4.0** (for a set of photographer-copyright images). A full policy page exists.
- **Commercial use allowed?** **Yes** for PD images ("free to use them however you like") and **yes** for CC BY-SA images ("Adapt — remix, transform, and build upon the material for any purpose, even commercially"). **No** for the artist-copyrighted images (permission from Bildupphovsrätt i Sverige required).
- **Attribution required?** **PD:** not legally required; the museum "kindly ask[s]" for credit. **CC BY-SA:** required, with this exact format: **"Photo: [photographer's name], [museum's name] ([license])"** — e.g. *Photo: Erik Cornelius, Nationalmuseum (CC BY-SA)*.
- **API / download entry URL:**
  - Collection search: `https://collection.nationalmuseum.se/en/`
  - Media Portal: `https://media.nationalmuseum.se/search/all`
  - Free images on Wikimedia Commons: `https://commons.wikimedia.org/wiki/Category:Images_from_the_Nationalmuseum_Stockholm`
  - Ultra high-resolution images: `https://www.nationalmuseum.se/en/explore-art-and-design/images/super-high-resolution-images`
  - Order images/rights: `https://www.nationalmuseum.se/en/explore-art-and-design/images/order-images-rights`
  - Rights page: `https://www.nationalmuseum.se/en/explore-art-and-design/images/rights-and-reproductions`
- **Resolution limits:** 未能核实 as a numeric cap (a separate "Ultra high-resolution images" page is offered).

**Key quotations (English) + source URL — all from `https://www.nationalmuseum.se/en/explore-art-and-design/images/rights-and-reproductions`:**
> "Some of the online images of Nationalmuseum's artworks are protected by copyright, but most are not."

> "In-copyright objects and images of them are marked '© konstnären / artist / Bildupphovsrätt i Sverige'. These images may not be used or published without permission from Bildupphovsrätt Sverige / the Visual Copyright Society."

> "Some images online are protected by the photographer's copyright. These images are marked as 'CC BY-SA' and may be used according to these license terms."

> "Basically, with a CC BY-SA image, you are free to: Share — copy and redistribute the material in any medium or format. Adapt — remix, transform, and build upon the material for any purpose, even commercially. … Credit the photographer as follows: 'Photo: [photographer's name], [museum's name] ([license])'. For example: Photo: Erik Cornelius, Nationalmuseum (CC BY-SA)."

> "Nationalmuseum has digitally reproduced many works of art that are no longer protected by copyright. These digital images are public domain (marked as 'PD'). That means they belong to our shared cultural heritage and you are free to use them however you like."

> "Please credit the artist, the photographer and Nationalmuseum. You can link to the object, or use this crediting format: [Artist]: [Title], [Date], Nationalmuseum (Photo: [photographer's name]), public domain. For example: Rembrandt: Kökspigan, 1651, Nationalmuseum (Photo: Erik Cornelius), public domain."

---

## 8. Finnish National Gallery (Kansallisgalleria)

- **Institution:** Finnish National Gallery / Kansallisgalleria (Ateneum, Kiasma, Sinebrychoff)
- **Can images be freely downloaded?** **Partial — yes for copyright-free images.** Over 36,000 images released into the public domain; copyrighted images are order-only, for a fee.
- **License type:** **CC0** for the 36,000+ public-domain images. Copyrighted images require a paid licence agreement.
- **Commercial use allowed?** **Yes for the CC0 images** ("used free of charge"). Copyrighted images are licensed for a fee with published commercial tariffs.
- **Attribution required?** **未能核实** — the CC0 release implies no attribution obligation; the "Using our images" section of the page was not captured, so no explicit requested credit string could be verified.
- **API / download entry URL:**
  - Collection search (images downloadable when labelled "Copyright Free"): `https://kokoelma.kansallisgalleria.fi/en`
  - Photographic service & price list: `https://kansallisgalleria.fi/en/photographic-service/`
  - Image order form: `https://link.webropolsurveys.com/S/CF3B461B76B0CDF4`
  - Press images: `https://kansallisgalleria.fi/en/press/`
  - Contact: `kuvakokoelmat@kansallisgalleria.fi`
- **Resolution limits:** 未能核实 as a stated cap. The site notes images on the website are "mainly in JPG format", and that the photographic service delivers high-resolution files for printing.

**Key quotations (English) + source URL — `https://kansallisgalleria.fi/en/photographic-service/`:**
> "The Finnish National Gallery has released over 36,000 images into the public domain under the CC0-license."

> "Copyrighted images are accompanied by a copyright notice 'In Copyright'. If you would like to use these images, you can order them using the image order form. Image orders are subject to a fee."

> "Copyright-free images are labelled with the 'Copyright Free' mark. These image files can be downloaded from the website and used free of charge."

> "The permitted uses of the images depend on whether the images are copyrighted or whether their copyright term has expired."

Fee examples for copyrighted images (same page, price list updated 1 Sept 2024): "Websites €100 (vat 0%)", "Merchandise — posters, postcards, calendars: €100", "Advertising €500–1 000", "Private use €50".

---

## 9. Belvedere Museum, Vienna (Österreichische Galerie Belvedere)

- **Institution:** Österreichische Galerie Belvedere / Austrian Gallery Belvedere
- **Can images be freely downloaded?** **Partial.** An "Open Content" programme offers free downloads of images of **copyright-free** works (5,916 items listed; "über 5.000"). Not free for in-copyright works.
- **License type:** **Unclear / no Creative Commons licence found.** The pages describe a free download for "private and scientific purposes" only, with a separate commercial channel; **no CC0/CC BY/PDM label was stated on the Open Content pages I fetched.** (The general Imprint reserves copyright on website content.)
- **Commercial use allowed?** **No, not freely** — "Für kommerzielle Zwecke wenden Sie sich bitte an die Reproduktionsabteilung" (for commercial purposes please contact the Reproduction Department, `repro@belvedere.at`).
- **Attribution required?** **未能核实** — no explicit attribution string stated on the Open Content pages fetched. The museum asks for a courtesy copy ("Belegexemplar") for its library if you wish.
- **API / download entry URL:**
  - Collection Online: `https://sammlung.belvedere.at/`
  - Open Content: `https://sammlung.belvedere.at/opencontent` and `https://sammlung.belvedere.at/opencontent/images`
  - Object page example with download options: `https://sammlung.belvedere.at/objects/55620/beweinung-christi`
  - IIIF viewer: `https://sammlung.belvedere.at/mirador/objects/55620`
  - Commercial/reproduction contact: `repro@belvedere.at`
- **Resolution limits:** Explicitly stated: **300 dpi on the 15 cm long side = 1772 pixels**.

**Key quotations (German + gloss) + source URLs:**
> « Das Belvedere bietet kostenfreien Zugang zu Abbildungen von über 5.000 urheberrechtsfreien Kunstwerken aus seiner Sammlung. Die Digitalisate stehen für private und wissenschaftliche Zwecke in einer Auflösung von 300 dpi auf 15 cm lange Seite (1772 Pixel) zum Download bereit und ermöglichen eine vielfältige Nutzung in Forschung, Lehre und persönlicher Beschäftigung mit Kunst. »
> (The Belvedere offers free access to images of over 5,000 copyright-free artworks… The digital copies are available for download for private and scientific purposes at a resolution of 300 dpi on the 15 cm long side (1772 pixels)…)
— `https://sammlung.belvedere.at/opencontent/images` (identical text at `/opencontent`)

> « Bilddaten urheberrechtsfreier Werke können für die private und wissenschaftliche Nutzung heruntergeladen werden. Für kommerzielle Zwecke wenden Sie sich bitte an die Reproduktionsabteilung. »
> (Image files of copyright-free works can be downloaded for private and scientific use. For commercial purposes please contact the Reproduction Department.)
— same URL

> Object page download buttons: « Private & wissenschaftliche Nutzung » and « Kommerzielle Nutzung ».
— `https://sammlung.belvedere.at/objects/55620/beweinung-christi`

> Imprint reservation: « Die auf dieser Webseite bereitgestellten Inhalte, Texte, Abbildungen, Graphiken, Ton- und Videodokumente und sonstigen Dokumente sind urheberrechtlich geschützt. … Jede Vervielfältigung, Veröffentlichung oder andere Verwertung ist ohne die ausdrückliche Zustimmung von Belvedere bzw dem jeweiligen Rechteinhaber nicht gestattet. »
> (…All reproduction, publication or other exploitation is not permitted without the express consent of the Belvedere or the respective rights holder.)
> And: « Vervielfältigungen eines Werkes dieser Webseite für Text- und Data-Mining und damit insbesondere für das Training einer Künstlichen Intelligenz bleibt ausdrücklich vorbehalten (§ 42h Abs 6 UrhG). »
> (Reproductions for text and data mining, in particular for AI training, are expressly reserved.)
— `https://www.belvedere.at/impressum`

---

## 10. Kunsthistorisches Museum Vienna (KHM)

- **Institution:** Kunsthistorisches Museum Wien / KHM-Museumsverband (KHM, Neue Burg, Hofburg treasury, etc.)
- **Can images be freely downloaded?** **No.** The museum states all pictures and text are copyright-protected and may not be used without express permission; there is a formal reproduction request channel.
- **License type:** **All rights reserved / view-only** (no CC licence found). Rights page is explicit.
- **Commercial use allowed?** **No** — any use requires express permission; reproduction requests go through a paid/formal channel.
- **Attribution required?** **未能核实** as a specific string; the museum requires permission, and requests are made through the "Reproduction Request" service.
- **API / download entry URL:**
  - Rights & Reproduction: `https://www.khm.at/en/museum/rights-reproduction`
  - Reproduction request: `https://shop.khm.at/en/repro`
  - Online collection (browse only, no download licence shown): `https://www.khm.at/en/artworks` and `https://www.khm.at/en/artworks/search`
  - Contact: `info.repro@khm.at`
- **Resolution limits:** 未能核实.

**Key quotations (English) + source URL — `https://www.khm.at/en/museum/rights-reproduction`:**
> "All pictures and text as well as photographic and audio material are protected by copyright. Kunsthistorisches Museum Vienna"

> "Pictures and photographic material of the KHM may not be reproduced, copied, altered or otherwise be used in any way without express permission."

> "Reproduction Request" (link to `https://shop.khm.at/en/repro`).

**Note:** `/en/artworks` (online collection) was fetched and shows object browsing but **no open-licence or download statement**; no CC marks appeared.

---

## 11. Web Gallery of Art (WGA)

- **Institution:** Web Gallery of Art — private, non-museum virtual museum/database of European fine arts (founders Emil Krén and Daniel Marx; site "wga.hu")
- **Can images be freely downloaded?** **Partial in practice, but reuse-restricted.** Images/documents may be downloaded from the database **only for educational and personal purposes**; distribution in any form is prohibited without the legal owner's authorisation.
- **License type:** **Unclear / proprietary — "educational and personal purposes" only, no open licence** (the database itself is asserted as copyrighted).
- **Commercial use allowed?** **No** ("educational and personal purposes" only; distribution prohibited without authorisation).
- **Attribution required?** **未能核实** as a specific requested string. The site carries a general copyright line and describes the database as copyrighted.
- **API / download entry URL:** **No API found.** Site: `https://www.wga.hu/` (title page: `https://www.wga.hu/index.html`); search: `https://www.wga.hu/index_search.html`; artists: `https://www.wga.hu/index_artists.html`. A downloadable **catalogue** of image data is offered at `https://www.wga.hu/support/mobile/catalog.html` (catalogue of "fundamental data of all images").
- **Resolution limits:** 未能核实. The site states "over 52,800 reproductions".

**Key quotation (English) + source URL — `https://www.wga.hu/support/mobile/legal.html`:**
> "The Web Gallery of Art is copyrighted as a database. Images and documents downloaded from this database can only be used for educational and personal purposes. Distribution of the images in any form is prohibited without the authorization of their legal owner."

> Homepage description: "The Web Gallery of Art is a virtual museum and searchable database of European fine arts, decorative arts and architecture (3rd-19th centuries), currently containing over 52,800 reproductions."
— `https://www.wga.hu/index.html`

> Footer credit: "© Web Gallery of Art, created by Emil Krén and Daniel Marx."
— `https://www.wga.hu/support/mobile/info.html`

**Navigation note:** the old copyright URLs (`/info/copyright.html`, `/info/terms.html`, `/copyright.html`) now return HTTP 200 with a generic "The address has changed!" page. The live terms live at `/support/mobile/legal.html` (reachable via the mobile nav "Info" page at `/support/mobile/info.html`, which is titled "legal questions").

---

## Summary table

| # | Institution | Free download? | License | Commercial use | Attribution |
|---|---|---|---|---|---|
| 1 | Paris Musées | Partial (CC0-tagged images) | CC0 for tagged images; "Tous droits réservés" for the rest | Yes for CC0 | Not legally, but requested (title/artist/Paris Musées/museum) |
| 2 | Musée du Louvre | Partial (medium-res, listed uses only) | No CC0 for images; Etalab 2.0 for text metadata; paid licence via GrandPalaisRmn | No (paid licence) | Yes (photo credit + permalink; Etalab attribution) |
| 3 | Uffizi Galleries | No | Permission/fee-based, no CC | No (authorisation + fee) | 未能核实 |
| 4 | Museo del Prado | **未能核实** | **未能核实** | **未能核实** | **未能核实** |
| 5 | Städel Museum | Yes (public-domain works) | Public Domain Mark 1.0; CC0 1.0 metadata | Yes | Requested: "Städel Museum, Frankfurt am Main" |
| 6 | SMK Copenhagen | Yes | Public Domain Mark 1.0 | Yes | Requested: "Shared by SMK, National Gallery of Denmark" |
| 7 | Nationalmuseum Stockholm | Partial | PD + CC BY-SA 4.0 | Yes for PD and CC BY-SA; no for artist-copyright | PD: requested; CC BY-SA: required, "Photo: [photographer], [museum] ([license])" |
| 8 | Finnish National Gallery | Partial (copyright-free images) | CC0 (36,000+ images) | Yes for CC0; fee for in-copyright | 未能核实 |
| 9 | Belvedere Vienna | Partial (private/scientific only) | No CC found; bespoke Open Content terms | No (contact Reproduction Dept.) | 未能核实 |
| 10 | KHM Vienna | No | All rights reserved | No (express permission required) | 未能核实 |
| 11 | Web Gallery of Art | Restricted (educational/personal only) | Proprietary; no open licence | No | 未能核实 |

**Institutions with the clearest true CC0 / public-domain open policies:** Paris Musées (CC0), Städel (PDM 1.0 + CC0 metadata), SMK (PDM 1.0 + API/IIIF), Finnish National Gallery (CC0). Nationalmuseum is PD + CC BY-SA with a thoroughly documented rights page. Louvre and Belvedere are free-but-restricted. Uffizi and KHM are permission/fee only. WGA is educational/personal only. Prado remains unverified.
