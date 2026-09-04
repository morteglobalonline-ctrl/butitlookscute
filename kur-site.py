#!/usr/bin/env python3
"""Siteyi tek kaynaktan uretir — ortak baslik/alt bilgi her sayfada ayni.

Site Builder Agent yalnizca bu dosyayi ve katalog.json'u degistirir.
"""
import json, os, html

DIZIN = os.path.dirname(os.path.abspath(__file__))
MAIL = 'info@butitlookscute.com'
IG = 'https://instagram.com/butitlookscute'
ALAN = 'butitlookscute.com'

LOGO = ('<a class="logo" href="/">BUT <span class="p">IT</span> LOOKS<br><span class="p">CUTE</span>'
        '<small>HOME &amp; LIVING STORE</small></a>')

MENU = [('/', 'Shop'), ('/about.html', 'About'), ('/faq.html', 'FAQ'),
        ('/shipping.html', 'Shipping'), ('/contact.html', 'Contact')]


def bas(baslik, aciklama, aktif='', yol='/', gorsel=None):
    nav = ''.join(
        f'<a href="{u}"{" aria-current=\"page\"" if u == aktif else ""}>{html.escape(a)}</a>'
        for u, a in MENU)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(baslik)}</title>
<meta name="description" content="{html.escape(aciklama)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="/style.css">
<link rel="canonical" href="https://{ALAN}{yol}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#8B6DC4">
<meta property="og:type" content="website">
<meta property="og:site_name" content="But It Looks Cute">
<meta property="og:title" content="{html.escape(baslik)}">
<meta property="og:description" content="{html.escape(aciklama)}">
<meta property="og:url" content="https://{ALAN}{yol}">
<meta property="og:image" content="https://{ALAN}/img/banner-1.jpg">
<meta property="og:image:width" content="1672">
<meta property="og:image:height" content="941">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(baslik)}">
<meta name="twitter:description" content="{html.escape(aciklama)}">
<meta name="twitter:image" content="https://{ALAN}/img/banner-1.jpg">
<script type="application/ld+json">{{
 "@context":"https://schema.org","@type":"OnlineStore",
 "name":"But It Looks Cute","alternateName":"butitlookscute",
 "url":"https://{ALAN}/","logo":"https://{ALAN}/img/banner-1.jpg",
 "image":"https://{ALAN}/img/banner-1.jpg",
 "description":"Cute things for your space. Playful home and living products — mugs, candles, journals, pillows and desk mats. Printed on demand, shipped from the US.",
 "email":"{MAIL}","sameAs":["{IG}"],
 "areaServed":{{"@type":"Country","name":"United States"}},
 "currenciesAccepted":"USD","paymentAccepted":"Credit Card"
}}</script>
<script>window.MAGAZA_API="https://api.butitlookscute.com";</script>
</head>
<body>
<div class="ribbon"><div class="wrap">
  <span>♡ Free shipping on orders over $75</span>
  <span>Cute things for your space ♥</span>
</div></div>
<header><div class="wrap">
  {LOGO}
  <nav>{nav}</nav>
  <a class="ig" href="{IG}" target="_blank" rel="noopener">◎ @butitlookscute</a>
  <button class="sepet-dugme" id="sepetAc" aria-label="Basket">▢<b id="sepetSayi">0</b></button>
</div></header>

<aside class="cekmece" id="cekmece" aria-label="Shopping basket">
  <header><h3>Your basket</h3><button class="kapat" id="sepetKapat" aria-label="Close" style="position:static">×</button></header>
  <div class="liste" id="sepetListe"></div>
  <div class="alt">
    <div class="toplam"><span>Subtotal</span><span id="sepetToplam">$0.00</span></div>
    <p class="kargo-not" id="kargoNot">Free shipping on orders over $75</p>
    <button class="btn btn-fill" id="odeme">CHECKOUT →</button>
  </div>
</aside>
'''


def son():
    return f'''<footer><div class="wrap">
  <div class="fgrid">
    <div>
      {LOGO}
      <p style="color:var(--mute);margin-top:14px;max-width:34ch">
        Cute things for your space. Printed on demand, shipped from the United States.</p>
      <p style="margin-top:12px"><a class="ig" href="{IG}" target="_blank" rel="noopener">◎ @butitlookscute</a></p>
    </div>
    <div><h5>Shop</h5><ul>
      <li><a href="/#shop">All products</a></li><li><a href="/#shop">Candles</a></li>
      <li><a href="/#shop">Mugs</a></li><li><a href="/#shop">Journals</a></li>
      <li><a href="/#shop">Home decor</a></li></ul></div>
    <div><h5>Help</h5><ul>
      <li><a href="/faq.html">FAQ</a></li><li><a href="/shipping.html">Shipping &amp; Returns</a></li>
      <li><a href="/contact.html">Contact</a></li></ul></div>
    <div><h5>Company</h5><ul>
      <li><a href="/about.html">About us</a></li><li><a href="/privacy.html">Privacy Policy</a></li>
      <li><a href="/terms.html">Terms of Service</a></li></ul></div>
  </div>
  <div class="fbot">
    <span>© 2026 But It Looks Cute ™ — all rights reserved</span>
    <span>Printed on demand · Ships from the US · <a href="{MAIL and "mailto:" + MAIL}">{MAIL}</a></span>
  </div>
</div></footer>
<script src="/sepet.js" defer></script>
</body></html>'''


def belge(dosya, baslik, kicik, govde, aktif=''):
    icerik = bas(f'{baslik} — But It Looks Cute', kicik, aktif, '/' + dosya)
    icerik += f'<div class="doc"><h1>{html.escape(baslik)}</h1><p class="kicik">{html.escape(kicik)}</p>{govde}</div>'
    icerik += son()
    open(os.path.join(DIZIN, dosya), 'w', encoding='utf-8').write(icerik)
    return dosya, len(icerik)


# ─────────────────────────── ANA SAYFA ───────────────────────────
katalog = json.load(open(os.path.join(DIZIN, 'katalog.json'), encoding='utf-8'))

ana = bas('But It Looks Cute — Home & Living Store',
          'Cute things for your space. Playful designs, cozy vibes, made to brighten your everyday. '
          'Printed on demand, shipped from the US.', '/')
ana += f'''
<div class="serit" id="serit">
  <div class="kaydir" id="kaydir">
    <figure><img src="/img/banner-1.jpg" alt="Summer Cute for Every Space — poolside picks" fetchpriority="high" width="1672" height="941"></figure>
    <figure><img src="/img/banner-2.jpg" alt="Cute details for every corner" loading="lazy" width="1672" height="941"></figure>
  </div>
  <button class="ok sol" id="okSol" aria-label="Previous">‹</button>
  <button class="ok sag" id="okSag" aria-label="Next">›</button>
  <div class="noktalar" id="noktalar"></div>
</div>

<div class="hero" style="background:var(--cream);position:relative;overflow:hidden">
  <div class="wrap" style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;
       padding-top:76px;padding-bottom:76px">
    <div>
      <span style="display:inline-flex;align-items:center;gap:8px;background:var(--paper);
        border:1.5px solid var(--ink);border-radius:999px;padding:8px 18px;font-weight:800;
        font-size:12.5px;letter-spacing:.08em">CUTE THINGS FOR EVERY SPACE ♥</span>
      <h1 style="font-size:clamp(38px,5vw,60px);line-height:1.06;margin:22px 0 16px">
        Decorate your space with <span style="color:var(--lav)">cute</span> that makes you smile.</h1>
      <p style="font-size:17px;color:var(--mute);max-width:34ch;margin-bottom:30px">
        Playful designs. Cozy vibes. Made to brighten your everyday.</p>
      <a class="btn btn-fill" href="#shop">SHOP NOW →</a>
      <a class="btn btn-out" href="/about.html">OUR STORY</a>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
      {''.join(f'<div style="border-radius:16px;overflow:hidden;background:var(--paper);aspect-ratio:1">'
               f'<img src="{u["gorseller"][0]}" alt="{html.escape(u["ad"])}" loading="lazy" '
               f'style="width:100%;height:100%;object-fit:cover"></div>'
               for u in katalog[:4] if u["gorseller"])}
    </div>
  </div>
</div>

<div style="background:var(--cream);padding-bottom:64px"><div class="wrap">
  <div style="background:var(--paper);border-radius:22px;box-shadow:var(--shadow);display:grid;
       grid-template-columns:repeat(4,1fr);gap:28px;padding:30px 34px">
    {''.join(f'<div style="display:flex;gap:13px;align-items:flex-start">'
             f'<div style="width:34px;height:34px;flex:none;border-radius:50%;background:var(--lav-4);'
             f'display:grid;place-items:center;font-size:16px">{i}</div>'
             f'<div><h4 style="font-family:var(--display);margin:0 0 3px;font-size:15px">{b}</h4>'
             f'<p style="margin:0;font-size:13px;color:var(--mute)">{a}</p></div></div>'
             for i, b, a in [('◕','Unique &amp; Playful Designs','Made to stand out'),
                             ('♥','Made with Love','Thoughtful in every detail'),
                             ('❦','Printed on Demand','Sustainable &amp; responsible'),
                             ('✦','Cute is Always a Good Idea','Bringing joy to your space')])}
  </div>
</div></div>

<section id="shop"><div class="wrap">
  <h2 class="sec-title">♥ THE CUTE COLLECTION ♥</h2>
  <p class="sec-sub">Six products, three designs each — Moo Patch, Moo Minimal and Moo Check.
    Tap any product to see every angle.</p>
  <div class="filtre" id="filtre"></div>
  <div class="prods" id="izgara"></div>
</div></section>

<div style="background:var(--lav);color:#fff;text-align:center;padding:56px 0">
  <div class="wrap">
    <h2 style="font-size:clamp(24px,3.4vw,36px);margin:0 0 10px">Make your space feel like you</h2>
    <p style="margin:0 0 26px;opacity:.92">New cute things every week — follow along on Instagram.</p>
    <a class="btn btn-out" style="background:#fff;border-color:#fff;color:var(--lav)"
       href="{IG}" target="_blank" rel="noopener">FOLLOW @BUTITLOOKSCUTE →</a>
  </div>
</div>

<div class="perde" id="perde">
  <div class="kutu" style="max-width:1020px;margin:24px auto;position:relative">
    <button class="kapat" id="kapat" aria-label="Close">×</button>
    <div class="pencere" id="pencere"></div>
  </div>
</div>

<script>
// --- giris seridi: otomatik dondurur, tiklaninca durur ---
(function(){{
  const kaydir = document.getElementById('kaydir');
  const say = kaydir.children.length;
  const noktalar = document.getElementById('noktalar');
  let i = 0, sayac = null;

  noktalar.innerHTML = Array.from({{length: say}}, (_, j) =>
    `<button data-j="${{j}}" aria-label="Slide ${{j+1}}"${{j===0?' aria-current="true"':''}}></button>`).join('');

  function goster(n) {{
    i = (n + say) % say;
    kaydir.style.transform = `translateX(-${{i * 100}}%)`;
    noktalar.querySelectorAll('button').forEach((b, j) =>
      j === i ? b.setAttribute('aria-current','true') : b.removeAttribute('aria-current'));
  }}
  function basla() {{ dur(); sayac = setInterval(() => goster(i + 1), 6000); }}
  function dur() {{ if (sayac) clearInterval(sayac); sayac = null; }}

  document.getElementById('okSag').addEventListener('click', () => {{ goster(i + 1); basla(); }});
  document.getElementById('okSol').addEventListener('click', () => {{ goster(i - 1); basla(); }});
  noktalar.addEventListener('click', e => {{
    const b = e.target.closest('button'); if (b) {{ goster(+b.dataset.j); basla(); }} }});
  const serit = document.getElementById('serit');
  serit.addEventListener('mouseenter', dur);
  serit.addEventListener('mouseleave', basla);
  // dokunmatik kaydirma
  let x0 = null;
  serit.addEventListener('touchstart', e => {{ x0 = e.touches[0].clientX; dur(); }}, {{passive:true}});
  serit.addEventListener('touchend', e => {{
    if (x0 === null) return;
    const d = e.changedTouches[0].clientX - x0;
    if (Math.abs(d) > 40) goster(i + (d < 0 ? 1 : -1));
    x0 = null; basla();
  }}, {{passive:true}});
  // hareketi azalt tercihi
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) basla();
}})();

(async function(){{
  const K = await (await fetch('/katalog.json')).json();
  const izgara = document.getElementById('izgara');
  const kart = (u, i) => `
    <div class="card" data-i="${{i}}" role="button" tabindex="0">
      <div class="ph"><img src="${{u.gorseller[0]||''}}" alt="${{u.ad}}" loading="lazy"></div>
      <div class="body">
        <div class="dz">${{u.dz}}</div>
        <h3>${{u.tip}}</h3>
        <div class="pr">$${{u.fiyat}}${{u.fiyatMax !== u.fiyat ? '–$' + u.fiyatMax : ''}}</div>
        <div class="say">${{u.gorseller.length}} photo${{u.gorseller.length > 1 ? 's' : ''}}</div>
      </div>
    </div>`;
  izgara.innerHTML = K.map((u, i) => kart(u, i)).join('');

  // --- KATEGORI VE TASARIM FILTRESI ---
  // 18 urun var ve artacak; kategori olmadan alt siralar hic gorulmuyor.
  const filtre = document.getElementById('filtre');
  let secKat = 'hepsi', secDz = 'hepsi';

  const katlar = [...new Set(K.map(u => u.kat))].sort();
  const dzler  = [...new Set(K.map(u => u.dz))].sort();
  const say = (alan, deger) => K.filter(u => u[alan] === deger).length;

  filtre.innerHTML =
    `<div class="filtre-baslik">Category</div><div class="filtre-grup">` +
    `<button data-t="kat" data-v="hepsi" aria-current="true">All<span class="sayi">${{K.length}}</span></button>` +
    katlar.map(c => `<button data-t="kat" data-v="${{c}}">${{c}}<span class="sayi">${{say('kat', c)}}</span></button>`).join('') +
    `</div><div class="filtre-baslik" style="margin-top:16px">Design</div><div class="filtre-grup">` +
    `<button data-t="dz" data-v="hepsi" aria-current="true">All</button>` +
    dzler.map(d => `<button data-t="dz" data-v="${{d}}">${{d}}<span class="sayi">${{say('dz', d)}}</span></button>`).join('') +
    `</div>`;

  function suz() {{
    const liste = K.map((u, i) => ({{u, i}}))
      .filter(({{u}}) => (secKat === 'hepsi' || u.kat === secKat) && (secDz === 'hepsi' || u.dz === secDz));
    izgara.innerHTML = liste.length ? liste.map(({{u, i}}) => kart(u, i)).join('')
      : '<div class="bos-sonuc"><p>Nothing here yet — try another combination.</p></div>';
  }}

  filtre.addEventListener('click', e => {{
    const b = e.target.closest('button'); if (!b) return;
    const tur = b.dataset.t;
    if (tur === 'kat') secKat = b.dataset.v; else secDz = b.dataset.v;
    filtre.querySelectorAll(`button[data-t="${{tur}}"]`).forEach(x => x.removeAttribute('aria-current'));
    b.setAttribute('aria-current', 'true');
    suz();
  }});

  const perde = document.getElementById('perde');
  const pencere = document.getElementById('pencere');

  function ac(i) {{
    const u = K[i];
    pencere.innerHTML = `
      <div class="galeri">
        <div class="buyuk"><img id="buyuk" src="${{u.gorseller[0]||''}}" alt="${{u.ad}}"></div>
        <div class="kucukler">${{u.gorseller.slice(0,15).map((g,j) =>
          `<button data-g="${{j}}"${{j===0?' aria-current="true"':''}}>
             <img src="${{g}}" alt="View ${{j+1}}" loading="lazy"></button>`).join('')}}</div>
      </div>
      <div class="detay">
        <div class="dz">${{u.dz}}</div>
        <h2>${{u.tip}}</h2>
        <p style="color:var(--mute);margin:0">${{u.aciklama}}</p>
        <div class="fiyat">$${{u.fiyat}}${{u.fiyatMax !== u.fiyat ? ' – $' + u.fiyatMax : ''}}</div>
        <ul>${{u.ozellik.map(o => `<li>${{o}}</li>`).join('')}}</ul>
        ${{u.varyantlar && u.varyantlar.length > 1 ? `
          <div class="secim">
            <label for="vr">${{/Candle/.test(u.tip) ? 'Scent' : 'Size'}}</label>
            <select id="vr">${{u.varyantlar.map(v =>
              `<option value="${{v.id}}" data-f="${{v.fiyat}}">${{v.ad}} — $${{v.fiyat}}</option>`).join('')}}</select>
          </div>` : ''}}
        <button class="btn btn-fill" id="ekle">ADD TO BASKET →</button>
        <p class="not">Printed on demand and shipped from the US. We do not accept returns —
          if your item arrives damaged we will send a replacement. See
          <a href="/shipping.html" style="color:var(--lav)">shipping &amp; returns</a>.</p>
      </div>`;
    pencere.querySelector('#ekle').addEventListener('click', () => {{
      const sec = pencere.querySelector('#vr');
      const v = sec ? u.varyantlar.find(x => String(x.id) === sec.value) : (u.varyantlar || [])[0];
      window.sepeteEkle(u, v); kapat();
    }});
    const buyuk = pencere.querySelector('#buyuk');
    pencere.querySelectorAll('.kucukler button').forEach(b => b.addEventListener('click', () => {{
      buyuk.src = u.gorseller[+b.dataset.g];
      pencere.querySelectorAll('.kucukler button').forEach(x => x.removeAttribute('aria-current'));
      b.setAttribute('aria-current', 'true');
    }}));
    perde.setAttribute('data-acik', '1');
    document.body.style.overflow = 'hidden';
  }}
  function kapat() {{ perde.removeAttribute('data-acik'); document.body.style.overflow = ''; }}

  izgara.addEventListener('click', e => {{
    const c = e.target.closest('.card'); if (c) ac(+c.dataset.i);
  }});
  izgara.addEventListener('keydown', e => {{
    if (e.key === 'Enter' || e.key === ' ') {{ const c = e.target.closest('.card');
      if (c) {{ e.preventDefault(); ac(+c.dataset.i); }} }}
  }});
  document.getElementById('kapat').addEventListener('click', kapat);
  perde.addEventListener('click', e => {{ if (e.target === perde) kapat(); }});
  document.addEventListener('keydown', e => {{ if (e.key === 'Escape') kapat(); }});
}})();
</script>
'''
ana += son()
open(os.path.join(DIZIN, 'index.html'), 'w', encoding='utf-8').write(ana)
print(f'  index.html          {len(ana)} bayt · {len(katalog)} ürün')


# ─────────────────────────── KURUMSAL SAYFALAR ───────────────────────────
sayfalar = []

sayfalar.append(belge('about.html', 'About Us',
  'Cute things for your space — and the small studio behind them.', f'''
<p>But It Looks Cute started with a simple, slightly stubborn idea: the things you
use every day should make you happy to look at. Your morning mug. The notebook on
your desk. The candle you light when the day is finally over. None of it has to be
beige.</p>

<p>So we made a home and living label built around one playful world — soft lavender,
inky black, warm cream, and a friendly cow who turns up everywhere. Three designs run
through the whole collection, and each one has its own mood.</p>

<div class="kutu">
  <p><strong>Moo Patch</strong> — playful · bold · iconic. Cow spots everywhere and the
  logo front and centre.</p>
  <p><strong>Moo Minimal</strong> — clean · minimal · modern. Lots of breathing room,
  one small cow, and a gentle reminder to stay a little longer.</p>
  <p><strong>Moo Check</strong> — trendy · cozy · aesthetic. A retro checkerboard with
  tiny hearts tucked into the squares.</p>
</div>

<h2>Made when you order it</h2>
<p>Nothing here sits in a warehouse. Every mug, candle, journal, pillow and desk mat is
printed and assembled after you place your order, by a print partner in the United
States, and shipped straight to you. It takes a few days longer than a giant warehouse
would — and it means we are not making thousands of things nobody asked for.</p>

<h2>Small on purpose</h2>
<p>We are a small operation. There is no call centre and no returns warehouse. What
there is: one email address that a real person reads, and a promise that if something
turns up damaged, we make it right without an argument.</p>

<h2>Say hello</h2>
<p>We are most active on Instagram — that is where new designs land first, and where
we share what customers do with theirs.</p>
<p><a class="btn btn-fill" href="{IG}" target="_blank" rel="noopener">FOLLOW @BUTITLOOKSCUTE</a></p>
''', '/about.html'))


sayfalar.append(belge('faq.html', 'Frequently Asked Questions',
  'Shipping times, sizing, care and everything else people ask us.', f'''
<h2>How long will my order take?</h2>
<p>Each item is made after you order it. Production usually takes <strong>2–5 business
days</strong>, and shipping inside the United States takes a further <strong>3–7
business days</strong>. Candles and desk mats sometimes sit at the longer end of that
range.</p>

<h2>Where do you ship?</h2>
<p>We currently ship within the <strong>United States only</strong>. If you are
somewhere else and want one of these, email us — we would like to know there is demand.</p>

<h2>Do you accept returns?</h2>
<p>No, and we would rather say that plainly than bury it. Because every item is made
for you specifically, we cannot resell it. <strong>If your order arrives damaged,
faulty, or is not what you ordered, we replace it free of charge</strong> — just email
us within 30 days with a photo. Full details on the
<a href="/shipping.html">shipping &amp; returns</a> page.</p>

<h2>Are the mugs dishwasher safe?</h2>
<p>Yes. Our 11oz ceramic mugs are both dishwasher and microwave safe. As with any
printed mug, hand washing will keep the colours vivid for longer.</p>

<h2>How do I care for the pillow cover?</h2>
<p>Machine wash cold on a gentle cycle, tumble dry low. Remove the insert first.
Do not bleach.</p>

<h2>What about the candles?</h2>
<p>Trim the wick to about 6mm before each burn, never leave a burning candle
unattended, and stop burning when about 12mm of wax is left. First burn: let the wax
pool reach the edge of the jar so it burns evenly afterwards.</p>

<h2>Can I wipe the desk mat clean?</h2>
<p>Yes — a damp cloth and mild soap. Let it air dry flat. Do not machine wash it.</p>

<h2>Do the three designs come on every product?</h2>
<p>Yes. Moo Patch, Moo Minimal and Moo Check each run across the whole collection, so
you can build a matching set — or deliberately mismatch, which we also support.</p>

<h2>Can I change or cancel my order?</h2>
<p>Email us as fast as you can. Once an item has gone into production we cannot stop
it, but if you catch us early we will do what we can.</p>

<h2>Something else?</h2>
<p>Write to <a href="mailto:{MAIL}" style="color:var(--lav)">{MAIL}</a> — a real person
answers, usually within one business day.</p>
''', '/faq.html'))


sayfalar.append(belge('shipping.html', 'Shipping & Returns',
  'How long orders take, what we do when something goes wrong, and why we do not accept returns.', f'''
<h2>Where we ship</h2>
<p>We ship within the <strong>United States</strong>. Orders are produced and dispatched
by our print partner in the US.</p>

<h2>How long it takes</h2>
<ul>
  <li><strong>Production:</strong> 2–5 business days — every item is made for your order</li>
  <li><strong>Delivery:</strong> 3–7 business days after dispatch</li>
  <li><strong>Total:</strong> usually 5–12 business days from order to doorstep</li>
</ul>
<p>You will get a tracking link by email as soon as your parcel leaves the facility.</p>

<h2>Shipping cost</h2>
<p>Shipping is calculated at checkout based on your address and what is in your basket.
<strong>Orders over $75 ship free.</strong></p>

<h2>Returns — please read before ordering</h2>
<div class="kutu">
  <p><strong>We do not accept returns or exchanges for change of mind.</strong> Every
  item is printed and assembled specifically for your order, so there is no shelf for it
  to go back to. Please check the product photos and details carefully before ordering.</p>
</div>

<h2>If something is wrong, we fix it</h2>
<p>This part matters more than the sentence above. If your order arrives:</p>
<ul>
  <li>damaged or broken in transit</li>
  <li>with a printing fault</li>
  <li>as the wrong item or wrong design</li>
</ul>
<p>…then email <a href="mailto:{MAIL}" style="color:var(--lav)">{MAIL}</a> within
<strong>30 days</strong> of delivery with your order number and a photo of the problem.
We will send a replacement at no cost to you. You do not need to ship the faulty item
back.</p>

<h2>Lost or delayed parcels</h2>
<p>If tracking has not moved for more than seven days, get in touch and we will open a
case with the carrier and, where needed, reprint your order.</p>

<h2>Wrong address</h2>
<p>Please double-check your shipping address at checkout. If you spot a mistake, email us
immediately — we can often correct it before the order enters production. Once it has
shipped to an address you provided, we cannot recover it.</p>
''', '/shipping.html'))


sayfalar.append(belge('privacy.html', 'Privacy Policy',
  'What we collect, why we collect it, and what we never do with it. Last updated 3 September 2026.', f'''
<p>This policy explains how But It Looks Cute ("we", "us") handles personal information
when you visit {ALAN} or place an order.</p>

<h2>What we collect</h2>
<ul>
  <li><strong>Order information</strong> — your name, shipping address, email address and
    what you ordered. We need this to make and deliver your order.</li>
  <li><strong>Payment information</strong> — handled entirely by our payment processor.
    We never see or store your full card number.</li>
  <li><strong>Basic usage data</strong> — pages visited and rough location, so we can see
    which products people are interested in.</li>
</ul>

<h2>Why we collect it</h2>
<p>To produce and ship your order, to answer your emails, to handle a damaged item, and
to understand which designs are worth making more of. That is the whole list.</p>

<h2>Who we share it with</h2>
<ul>
  <li><strong>Our print partner</strong> — receives your name and shipping address so the
    parcel can reach you. Nothing more.</li>
  <li><strong>Our payment processor</strong> — handles the transaction.</li>
  <li><strong>Delivery carriers</strong> — receive the address on the label.</li>
</ul>
<div class="kutu">
  <p><strong>We do not sell your personal information. We do not rent it, trade it, or
  hand it to advertisers.</strong> If that ever changed, this page would say so before it
  happened.</p>
</div>

<h2>Email</h2>
<p>We only email you about your order unless you have asked to hear about new products.
Every marketing email has an unsubscribe link that works immediately.</p>

<h2>Cookies</h2>
<p>We use the minimum needed to keep your basket working and to count visits. You can
block cookies in your browser; the shop will still work, though your basket may not
survive a refresh.</p>

<h2>How long we keep things</h2>
<p>Order records are kept as long as tax and accounting rules require. Support emails are
kept for two years so we have context if you write again.</p>

<h2>Your rights</h2>
<p>You can ask us what we hold about you, ask for it to be corrected, or ask us to delete
it — except where we are legally required to keep order records. Write to
<a href="mailto:{MAIL}" style="color:var(--lav)">{MAIL}</a> and we will respond within
30 days.</p>

<h2>Children</h2>
<p>This shop is not directed at children under 13 and we do not knowingly collect their
information.</p>

<h2>Changes</h2>
<p>If this policy changes we will update the date at the top of this page.</p>
''', ''))


sayfalar.append(belge('terms.html', 'Terms of Service',
  'The rules of buying from us. Last updated 3 September 2026.', f'''
<p>By placing an order at {ALAN} you agree to these terms.</p>

<h2>Products</h2>
<p>Every item is printed on demand. Because printing and fabric vary slightly between
batches, small differences in colour and placement are normal and are not considered
faults. Product photographs are digital mockups; the physical item may differ slightly
in tone.</p>

<h2>Prices and payment</h2>
<p>All prices are in US dollars and exclude shipping, which is calculated at checkout.
We may change prices at any time, but never after you have placed an order. Payment is
taken at checkout by our payment processor.</p>

<h2>Orders</h2>
<p>Placing an order is an offer to buy. We may decline an order — for example if an item
cannot be produced or an address is undeliverable — and if we do, you are refunded in
full. Once an item enters production it cannot be cancelled.</p>

<h2>Delivery</h2>
<p>We ship within the United States. Delivery estimates are estimates, not guarantees.
Risk passes to you on delivery.</p>

<h2>Returns</h2>
<p>We do not accept returns for change of mind. Faulty, damaged or incorrect items are
replaced free of charge — see <a href="/shipping.html">shipping &amp; returns</a>.</p>

<h2>Intellectual property</h2>
<p>All designs, artwork, the But It Looks Cute name and the site itself belong to us. You
are buying a product, not a licence to reproduce the artwork. Reselling our designs, or
using them commercially, is not permitted.</p>

<h2>Liability</h2>
<p>Our liability is limited to the amount you paid for the order. Nothing here limits
liability that cannot be limited by law.</p>

<h2>Contact</h2>
<p><a href="mailto:{MAIL}" style="color:var(--lav)">{MAIL}</a></p>
''', ''))


sayfalar.append(belge('contact.html', 'Contact',
  'One email address, read by a real person, usually answered within one business day.', f'''
<p>We keep this simple. There is one address, and a person reads it.</p>

<div class="kutu">
  <p style="font-size:20px;font-family:var(--display);margin-bottom:6px">
    <a href="mailto:{MAIL}" style="color:var(--lav)">{MAIL}</a></p>
  <p style="color:var(--mute);margin:0">We reply within one business day, Monday to Friday.</p>
</div>

<h2>Before you write</h2>
<p>These come up most often and are answered already:</p>
<ul>
  <li><a href="/faq.html" style="color:var(--lav)">How long will my order take?</a></li>
  <li><a href="/shipping.html" style="color:var(--lav)">My item arrived damaged</a></li>
  <li><a href="/shipping.html" style="color:var(--lav)">Can I return something?</a></li>
</ul>

<h2>To help us help you faster</h2>
<p>If you are writing about an order, include your <strong>order number</strong> and,
for anything damaged, a <strong>photo</strong>. That is usually all we need to send a
replacement the same day.</p>

<h2>Find us</h2>
<p>New designs land on Instagram first.</p>
<p><a class="btn btn-fill" href="{IG}" target="_blank" rel="noopener">FOLLOW @BUTITLOOKSCUTE</a></p>
''', '/contact.html'))

for ad, n in sayfalar:
    print(f'  {ad:20} {n} bayt')


# ─────────────────── ARAMA MOTORLARI ───────────────────
# Site yeni; Google onu kendiliginden bulmaz. Sitemap + robots ile
# haritayi veriyoruz, urun sayfalari da yapisal veriyle isaretleniyor.
from datetime import date
bugun = date.today().isoformat()

sayfa_listesi = [('/', '1.0', 'weekly'), ('/about.html', '0.7', 'monthly'),
                 ('/faq.html', '0.7', 'monthly'), ('/shipping.html', '0.6', 'monthly'),
                 ('/contact.html', '0.6', 'monthly'), ('/privacy.html', '0.3', 'yearly'),
                 ('/terms.html', '0.3', 'yearly')]

sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for yol, oncelik, sik in sayfa_listesi:
    sm.append(f'  <url><loc>https://{ALAN}{yol}</loc><lastmod>{bugun}</lastmod>'
              f'<changefreq>{sik}</changefreq><priority>{oncelik}</priority></url>')
sm.append('</urlset>')
open(os.path.join(DIZIN, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))

open(os.path.join(DIZIN, 'robots.txt'), 'w', encoding='utf-8').write(
    f'User-agent: *\nAllow: /\n\nSitemap: https://{ALAN}/sitemap.xml\n')

# Urun kataloguna yapisal veri — Google urunleri fiyatiyla gosterebilsin
urun_ld = {
    "@context": "https://schema.org", "@type": "ItemList",
    "name": "But It Looks Cute collection",
    "numberOfItems": len(katalog),
    "itemListElement": [{
        "@type": "ListItem", "position": i + 1,
        "item": {
            "@type": "Product",
            "name": u["ad"], "category": u["kat"],
            "description": u["aciklama"][:300],
            "image": u["gorseller"][:3],
            "brand": {"@type": "Brand", "name": "But It Looks Cute"},
            "offers": {"@type": "Offer", "priceCurrency": "USD", "price": u["fiyat"],
                       "availability": "https://schema.org/InStock",
                       "url": f"https://{ALAN}/#shop",
                       "shippingDetails": {"@type": "OfferShippingDetails",
                           "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "US"}}}
        }} for i, u in enumerate(katalog)]
}
ana_yol = os.path.join(DIZIN, 'index.html')
h = open(ana_yol, encoding='utf-8').read()
h = h.replace('</head>', '<script type="application/ld+json">'
              + json.dumps(urun_ld, ensure_ascii=False) + '</script>\n</head>')
open(ana_yol, 'w', encoding='utf-8').write(h)

print(f'  sitemap.xml          {len(sayfa_listesi)} sayfa')
print(f'  robots.txt           yazıldı')
print(f'  ürün yapısal verisi  {len(katalog)} ürün')
