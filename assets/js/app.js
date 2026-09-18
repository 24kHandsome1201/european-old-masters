/* 古画 · European Old Masters
 * 单一运行时脚本。数据来自 assets/js/works-data.js（普通 <script>，不是 fetch），
 * 这样 file:// 直接双击打开也能用。
 */
(function () {
  'use strict';

  /* ---------------------------------------------------------------- eras */

  var ERAS = [
    {
      id: '1',
      name: '晚期哥特与早期文艺复兴',
      en: 'Late Gothic & Early Renaissance',
      span: '约 1300 — 1500',
      start: 1280, end: 1500,
      lede: '绘画开始认真对待"看得见的世界"。乔托把圣徒画成有体重、有情绪的人；'
          + '北方画家则用油彩把羊毛、金属和皮肤的光泽一层层堆出来。'
          + '此时板面与湿壁画仍是主流。',
      pigment: 'var(--pigment-1)'
    },
    {
      id: '2',
      name: '文艺复兴盛期与北方文艺复兴',
      en: 'High Renaissance & Northern Renaissance',
      span: '约 1500 — 1600',
      start: 1500, end: 1600,
      lede: '透视、解剖与古典比例被系统化，画家从工匠变成"设计者"。'
          + '同一时期，阿尔卑斯山以北的画家把细节推向极致，也用画作参与宗教与政治的争论。',
      pigment: 'var(--pigment-2)'
    },
    {
      id: '3',
      name: '巴洛克',
      en: 'Baroque',
      span: '约 1600 — 1700',
      start: 1600, end: 1700,
      lede: '光成了主角。画家用强烈的明暗对比把瞬间凝固下来，'
          + '也让观众站进了画面里。风景、静物、肖像各自独立成科，市场从教堂转向了客厅与画廊。',
      pigment: 'var(--pigment-3)'
    },
    {
      id: '4',
      name: '洛可可与启蒙',
      en: 'Rococo & Enlightenment',
      span: '约 1700 — 1780',
      start: 1700, end: 1780,
      lede: '轻盈、愉悦、装饰性。贵族趣味偏爱柔和的粉色调和私密题材，'
          + '与此同时，城市景观画和日常生活的静物画记录着正在长大的市民社会。',
      pigment: 'var(--pigment-4)'
    },
    {
      id: '5',
      name: '新古典与浪漫主义',
      en: 'Neoclassicism & Romanticism',
      span: '约 1780 — 1850',
      start: 1780, end: 1850,
      lede: '一边回望古希腊罗马的理性与德性，一边转向自然、废墟与个人情感。'
          + '画廊与公共展览改变了画家谋生的方式，历史画与风景画的地位此消彼长。',
      pigment: 'var(--pigment-5)'
    },
    {
      id: '6',
      name: '写实、印象与后印象',
      en: 'Realism, Impressionism & Post-Impressionism',
      span: '约 1850 — 1900',
      start: 1850, end: 1900,
      lede: '画什么和怎么画同时被改写。有人坚持把穷人、工人和农民画成主角，'
          + '有人走出画室去捕捉空气与光，也有人干脆把绘画推向结构与色彩本身。',
      pigment: 'var(--pigment-6)'
    }
  ];

  var ERA_BY_ID = {};
  ERAS.forEach(function (e) { ERA_BY_ID[e.id] = e; });

  var SOURCE_KEY = 'guhua:image-source';

  /* ------------------------------------------------------------- helpers */

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function works() { return (window.WORKS || []); }

  function byId(id) {
    id = String(id);
    for (var i = 0; i < works().length; i++) {
      if (String(works()[i].id) === id) return works()[i];
    }
    return null;
  }

  function getSourceMode() {
    try {
      var v = localStorage.getItem(SOURCE_KEY);
      return v === 'remote' ? 'remote' : 'local';
    } catch (e) { return 'local'; }
  }

  function setSourceMode(mode) {
    try { localStorage.setItem(SOURCE_KEY, mode); } catch (e) { /* 隐私模式下忽略 */ }
  }

  /* kind: 'thumb' 用于目录页，'full' 用于详情页与主视觉 */
  function imgSrc(w, kind) {
    if (getSourceMode() === 'remote') {
      return kind === 'thumb' ? (w.remoteSmall || w.remote) : w.remote;
    }
    return kind === 'thumb' ? (w.thumb || w.local) : w.local;
  }

  /* 本地图缺失时静默回落到馆方在线图，而不是留一个破图 */
  function onImgError(img, w) {
    img.addEventListener('error', function () {
      if (img.dataset.fallback === '1') {
        img.dataset.loading = 'false';
        var p = img.parentNode;
        if (p && !$('.img-error', p)) {
          img.remove();
          p.appendChild(el('p', 'img-error', '图片未能载入'));
        }
        return;
      }
      img.dataset.fallback = '1';
      img.src = w.remoteSmall || w.remote;
    });
  }

  function artistLine(w) {
    var dates = w.artistDates ? ' <span class="num">' + esc(w.artistDates) + '</span>' : '';
    return esc(w.artist) + dates;
  }

  function yearText(w) { return w.yearLabel || String(w.year || ''); }

  /* ------------------------------------------------------- header + toggle */

  function initHeader() {
    var host = $('[data-source-toggle]');
    if (!host) return;

    function paint() {
      var mode = getSourceMode();
      $$('button', host).forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.mode === mode));
      });
    }

    host.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-mode]');
      if (!b) return;
      setSourceMode(b.dataset.mode);
      paint();
      refreshImages();
    });

    paint();
  }

  function refreshImages() {
    $$('img[data-work-id]').forEach(function (img) {
      var w = byId(img.dataset.workId);
      if (!w) return;
      img.dataset.fallback = '';
      var next = imgSrc(w, img.dataset.kind || 'full');
      if (img.getAttribute('src') !== next) img.src = next;
    });
  }

  /* ------------------------------------------------------------ timeline */

  function renderTimeline(host) {
    var data = works().slice().sort(function (a, b) { return a.year - b.year; });
    if (!data.length) return;

    var min = 1280, max = 1910;
    var inner = el('div', 'timeline__inner');

    var bands = el('div', 'timeline__bands');
    ERAS.forEach(function (era) {
      var seg = el('div', 'timeline__band');
      var from = Math.max(era.start, min), to = Math.min(era.end, max);
      seg.style.width = ((to - from) / (max - min) * 100) + '%';
      seg.style.background = era.pigment;
      seg.title = era.name + '（' + era.span + '）';
      bands.appendChild(seg);
    });
    inner.appendChild(bands);

    var axis = el('div', 'timeline__axis');
    inner.appendChild(axis);

    for (var y = 1300; y <= 1900; y += 50) {
      var tick = el('span', 'timeline__tick');
      tick.textContent = y;
      tick.style.left = ((y - min) / (max - min) * 100) + '%';
      inner.appendChild(tick);
    }

    data.forEach(function (w) {
      var dot = el('button', 'timeline__dot');
      dot.type = 'button';
      dot.dataset.era = w.era;
      dot.style.left = ((w.year - min) / (max - min) * 100) + '%';
      dot.setAttribute('aria-label',
        w.titleZh + '（' + w.artistZh + '，' + yearText(w) + '）');
      dot.title = w.titleZh + ' · ' + w.artistZh + ' · ' + yearText(w);
      dot.addEventListener('click', function () {
        location.href = 'work.html?id=' + encodeURIComponent(w.id);
      });
      inner.appendChild(dot);
    });

    host.appendChild(inner);

    var legend = el('div', 'timeline__legend');
    ERAS.forEach(function (era) {
      var b = el('button');
      b.type = 'button';
      var sw = el('span', 'timeline__swatch');
      sw.style.background = era.pigment;
      b.appendChild(sw);
      b.appendChild(document.createTextNode(era.name));
      b.addEventListener('click', function () {
        var target = $('#era-' + era.id);
        if (target) target.scrollIntoView({ block: 'start' });
      });
      legend.appendChild(b);
    });
    host.parentNode.appendChild(legend);
  }

  /* ------------------------------------------------------------- gallery */

  function renderGallery(host) {
    var data = works().slice().sort(function (a, b) { return a.year - b.year; });
    var state = { era: 'all', q: '' };

    var filters = el('div', 'filters');
    var chips = el('div', 'filters__chips');
    chips.style.display = 'flex';
    chips.style.flexWrap = 'wrap';
    chips.style.gap = 'var(--s2)';

    function chip(label, value) {
      var b = el('button', 'chip', label);
      b.type = 'button';
      b.dataset.value = value;
      b.addEventListener('click', function () {
        state.era = value;
        paintChips();
        apply();
      });
      chips.appendChild(b);
    }

    chip('全部', 'all');
    ERAS.forEach(function (e) { chip(e.name, e.id); });
    filters.appendChild(chips);

    var count = el('span', 'result-count');
    filters.appendChild(count);

    var search = el('div', 'search');
    search.innerHTML =
      '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
      + '<circle cx="7" cy="7" r="4.6" stroke="currentColor" stroke-width="1.3"/>'
      + '<path d="M10.4 10.4L14 14" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>'
      + '</svg>';
    var input = document.createElement('input');
    input.type = 'search';
    input.placeholder = '搜索画家或画名';
    input.setAttribute('aria-label', '搜索画家或画名');
    input.addEventListener('input', function () {
      state.q = input.value.trim().toLowerCase();
      apply();
    });
    search.appendChild(input);
    filters.appendChild(search);

    host.appendChild(filters);

    var list = el('div');
    host.appendChild(list);

    function paintChips() {
      $$('.chip', chips).forEach(function (b) {
        b.setAttribute('aria-pressed', String(b.dataset.value === state.era));
      });
    }

    function matches(w) {
      if (state.era !== 'all' && w.era !== state.era) return false;
      if (!state.q) return true;
      var hay = [w.title, w.titleZh, w.artist, w.artistZh]
        .join(' ').toLowerCase();
      return hay.indexOf(state.q) !== -1;
    }

    function plate(w) {
      var a = el('a', 'plate');
      a.href = 'work.html?id=' + encodeURIComponent(w.id);

      var frame = el('div', 'plate__frame');
      var img = document.createElement('img');
      img.dataset.workId = w.id;
      img.dataset.kind = 'thumb';
      img.dataset.loading = 'true';
      img.src = imgSrc(w, 'thumb');
      img.alt = w.titleZh + '，' + w.artistZh + '，' + yearText(w);
      img.loading = 'lazy';
      img.decoding = 'async';
      if (w.w && w.h) { img.width = w.w; img.height = w.h; }
      img.addEventListener('load', function () { img.dataset.loading = 'false'; });
      onImgError(img, w);
      frame.appendChild(img);

      var body = el('div', 'plate__body');
      body.appendChild(el('span', 'plate__artist', w.artistZh + ' ' + (w.artistDates || '')));
      var t = el('span', 'plate__title');
      t.innerHTML = '<em>' + esc(w.titleZh) + '</em>';
      body.appendChild(t);
      body.appendChild(el('span', 'plate__meta', yearText(w) + ' · ' + (w.mediumZh || '')));

      a.appendChild(frame);
      a.appendChild(body);
      return a;
    }

    function eraHead(era, n) {
      var head = el('div', 'era__head');
      var title = el('div', 'era__title');
      var mark = el('div', 'era__mark');
      mark.style.background = era.pigment;
      title.appendChild(mark);
      title.appendChild(el('h2', null, era.name));
      title.appendChild(el('span', 'era__span', era.span + ' · 本页 ' + n + ' 幅'));
      head.appendChild(title);
      var lede = el('p', 'era__lede', era.lede);
      head.appendChild(lede);
      return head;
    }

    function apply() {
      var shown = data.filter(matches);
      count.textContent = '共 ' + shown.length + ' 幅';
      list.innerHTML = '';

      if (!shown.length) {
        list.appendChild(el('p', 'empty', '没有符合条件的画作。换个关键词，或点「全部」看完整目录。'));
        return;
      }

      ERAS.forEach(function (era) {
        var group = shown.filter(function (w) { return w.era === era.id; });
        if (!group.length) return;
        var sec = el('section', 'era');
        sec.id = 'era-' + era.id;
        sec.appendChild(eraHead(era, group.length));
        var grid = el('div', 'grid');
        group.forEach(function (w) { grid.appendChild(plate(w)); });
        sec.appendChild(grid);
        list.appendChild(sec);
      });
    }

    paintChips();
    apply();
  }

  /* ------------------------------------------------------- detail (work) */

  function renderWork(root) {
    var params = new URLSearchParams(location.search);
    var w = byId(params.get('id')) || works()[0];

    if (!w) {
      root.innerHTML = '<div class="wrap"><p class="empty">找不到这幅画。</p></div>';
      return;
    }

    document.title = w.titleZh + ' · ' + w.artistZh + ' | 古画';

    var fig = el('figure', 'work__figure');
    var frame = el('div', 'work__frame');
    var img = document.createElement('img');
    img.dataset.workId = w.id;
    img.dataset.kind = 'full';
    img.dataset.loading = 'true';
    img.src = imgSrc(w, 'full');
    img.alt = w.titleZh + '，' + w.artistZh + '，' + yearText(w);
    img.width = w.w || 1200; img.height = w.h || 1000;
    img.addEventListener('load', function () { img.dataset.loading = 'false'; });
    onImgError(img, w);
    frame.appendChild(img);
    fig.appendChild(frame);

    var cap = el('figcaption', 'work__figcaption');
    cap.appendChild(el('span', null, yearText(w) + ' · ' + (w.mediumZh || w.medium || '')));
    var orig = el('a', null, '查看馆方原图');
    orig.href = w.remote; orig.target = '_blank'; orig.rel = 'noopener noreferrer';
    cap.appendChild(orig);
    var rec = el('a', null, '馆藏记录');
    rec.href = w.source; rec.target = '_blank'; rec.rel = 'noopener noreferrer';
    cap.appendChild(rec);
    fig.appendChild(cap);

    var side = el('div');

    var head = el('header', 'work__header');
    head.appendChild(el('span', 'eyebrow', (ERA_BY_ID[w.era] || {}).name || ''));
    var h1 = el('h1');
    h1.innerHTML = '<em>' + esc(w.titleZh) + '</em>';
    head.appendChild(h1);
    var ar = el('p', 'work__artist');
    ar.innerHTML = artistLine(w);
    head.appendChild(ar);
    side.appendChild(head);

    var prose = el('div', 'work__prose');
    prose.appendChild(el('h2', null, '看点'));
    prose.appendChild(el('p', null, w.look));
    prose.appendChild(el('h2', null, '导览'));
    prose.appendChild(el('p', null, w.note));
    if (w.tags && w.tags.length) {
      var tags = el('div', 'tags');
      w.tags.forEach(function (t) { tags.appendChild(el('span', 'tag', t)); });
      prose.appendChild(tags);
    }
    side.appendChild(prose);

    var facts = el('dl', 'facts');
    [
      ['原名', w.title],
      ['画家', w.artist + (w.artistDates ? '（' + w.artistDates + '）' : '')],
      ['年代', yearText(w)],
      ['材质', w.mediumZh ? w.mediumZh + '（' + w.medium + '）' : w.medium],
      ['尺寸', w.dimensions],
      ['收藏', w.repository],
      ['入藏', w.credit]
    ].forEach(function (row) {
      if (!row[1]) return;
      var d = el('div');
      d.appendChild(el('dt', null, row[0]));
      d.appendChild(el('dd', null, row[1]));
      facts.appendChild(d);
    });
    side.appendChild(facts);

    var credit = el('div', 'credit-box');
    credit.innerHTML =
      '<strong>图片来源</strong><br>'
      + esc(w.repository) + '，<span class="lic">' + esc(w.license) + '</span><br>'
      + '原作已进入公有领域（画家卒于 ' + esc(w.deathYear || '') + ' 年，'
      + '远超中国著作权法"终生加死后 50 年"的保护期）。'
      + '数字图片由馆方以 CC0 公有领域贡献方式发布，本站不再主张任何权利。<br>'
      + '许可：<a href="' + esc(w.licenseUrl) + '" target="_blank" rel="noopener noreferrer">'
      + esc(w.licenseUrl) + '</a><br>'
      + '来源：<a href="' + esc(w.source) + '" target="_blank" rel="noopener noreferrer">'
      + esc(w.source) + '</a><br>'
      + '本站为非营利学习项目，不投放广告、不销售任何商品或服务。';
    side.appendChild(credit);

    var layout = el('div', 'work__layout');
    layout.appendChild(fig);
    layout.appendChild(side);
    root.appendChild(layout);

    /* 上一幅 / 下一幅：按年代顺序 */
    var ordered = works().slice().sort(function (a, b) { return a.year - b.year; });
    var i = ordered.findIndex(function (x) { return String(x.id) === String(w.id); });
    var prev = i > 0 ? ordered[i - 1] : null;
    var next = i > -1 && i < ordered.length - 1 ? ordered[i + 1] : null;
    var pager = el('nav', 'pager');
    pager.setAttribute('aria-label', '按年代浏览');
    if (prev) {
      var pa = el('a');
      pa.href = 'work.html?id=' + prev.id;
      pa.innerHTML = '<span>上一幅 · ' + yearText(prev) + '</span>' + esc(prev.titleZh);
      pager.appendChild(pa);
    }
    if (next) {
      var na = el('a', 'next');
      na.href = 'work.html?id=' + next.id;
      na.innerHTML = '<span>下一幅 · ' + yearText(next) + '</span>' + esc(next.titleZh);
      pager.appendChild(na);
    }
    root.appendChild(pager);
  }

  /* ----------------------------------------------------------------- hero */

  function renderHero() {
    var host = $('[data-hero]');
    if (!host) return;
    var feature = byId(host.dataset.hero) || works()[0];
    if (!feature) return;

    var media = el('div', 'hero__media');
    var img = document.createElement('img');
    img.dataset.workId = feature.id;
    img.dataset.kind = 'full';
    img.src = imgSrc(feature, 'full');
    img.alt = feature.titleZh + '，' + feature.artistZh;
    img.width = feature.w || 1600; img.height = feature.h || 1000;
    img.fetchPriority = 'high';
    onImgError(img, feature);
    media.appendChild(img);

    var cap = el('div', 'hero__caption wrap');
    cap.appendChild(el('span', 'eyebrow', '本站最先看的一幅'));
    var h1 = el('h1', null, feature.titleZh);
    cap.appendChild(h1);
    var line = el('p', 'byline');
    line.innerHTML = esc(feature.artistZh) + '，' + yearText(feature)
      + ' · ' + esc(feature.repository);
    cap.appendChild(line);
    var link = el('p', 'byline');
    link.style.marginTop = 'var(--s2)';
    link.innerHTML = '<a href="work.html?id=' + feature.id + '">看这幅画的导览 →</a>';
    cap.appendChild(link);

    media.appendChild(cap);
    host.appendChild(media);
  }

  /* ----------------------------------------------------------------- boot */

  function boot() {
    initHeader();
    var t = $('[data-timeline]');
    if (t) renderTimeline(t);
    var g = $('[data-gallery]');
    if (g) renderGallery(g);
    var w = $('[data-work]');
    if (w) renderWork(w);
    renderHero();

    var n = $('[data-work-count]');
    if (n) n.textContent = String(works().length);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
