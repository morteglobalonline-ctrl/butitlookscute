/* SEPET — tarayicida durur.
   Fiyat SUNUCUDA katalogdan dogrulanir; istemciden gelen tutara guvenilmez.
   Bu dosya her sayfada yuklenir, boylece sepet sayaci her yerde gorunur. */
(function () {
  var API = window.MAGAZA_API || '';
  function oku() { try { return JSON.parse(localStorage.getItem('bilc_sepet') || '[]'); } catch (e) { return []; } }
  function yaz(s) { localStorage.setItem('bilc_sepet', JSON.stringify(s)); ciz(); }

  window.sepeteEkle = function (u) {
    var s = oku(), v = null, i;
    for (i = 0; i < s.length; i++) if (s[i].slug === u.slug) v = s[i];
    if (v) v.adet = Math.min(10, v.adet + 1);
    else s.push({ slug: u.slug, ad: u.ad, tip: u.tip, dz: u.dz,
                  fiyat: parseFloat(u.fiyat), gorsel: (u.gorseller || [])[0], adet: 1 });
    yaz(s); ac();
  };

  function cekmece() { return document.getElementById('cekmece'); }
  function ac() { var c = cekmece(); if (c) c.setAttribute('data-acik', '1'); }
  function kapat() { var c = cekmece(); if (c) c.removeAttribute('data-acik'); }

  function ciz() {
    var s = oku(), i, adet = 0, ara = 0;
    for (i = 0; i < s.length; i++) { adet += s[i].adet; ara += s[i].fiyat * s[i].adet; }
    var sayi = document.getElementById('sepetSayi');
    if (sayi) sayi.textContent = adet;
    var liste = document.getElementById('sepetListe');
    if (!liste) return;
    if (!s.length) {
      liste.innerHTML = '<div class="bos"><p>Your basket is empty.</p>' +
        '<p style="font-size:14px">Six products, three designs each — go find your favourite.</p></div>';
    } else {
      liste.innerHTML = s.map(function (x, j) {
        return '<div class="satir">' +
          '<img src="' + (x.gorsel || '') + '" alt="' + x.ad + '">' +
          '<div><div class="dz">' + x.dz + '</div><h4>' + x.tip + '</h4>' +
          '<div class="adet"><button data-a="eksi" data-i="' + j + '" aria-label="Less">−</button>' +
          '<span>' + x.adet + '</span>' +
          '<button data-a="arti" data-i="' + j + '" aria-label="More">+</button></div></div>' +
          '<div style="font-weight:800">$' + (x.fiyat * x.adet).toFixed(2) + '</div></div>';
      }).join('');
    }
    var t = document.getElementById('sepetToplam');
    if (t) t.textContent = '$' + ara.toFixed(2);
    var kn = document.getElementById('kargoNot');
    if (kn) kn.textContent = ara >= 75 ? '✓ Free shipping applied'
      : 'Add $' + (75 - ara).toFixed(2) + ' more for free shipping';
  }

  document.addEventListener('click', function (e) {
    if (e.target.closest('#sepetAc')) ac();
    if (e.target.closest('#sepetKapat')) kapat();
    var b = e.target.closest('.adet button');
    if (b) {
      var s = oku(), i = +b.dataset.i;
      if (b.dataset.a === 'arti') s[i].adet = Math.min(10, s[i].adet + 1);
      else if (--s[i].adet < 1) s.splice(i, 1);
      yaz(s);
    }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') kapat(); });

  document.addEventListener('DOMContentLoaded', function () {
    var odeme = document.getElementById('odeme');
    if (odeme) odeme.addEventListener('click', function () {
      var s = oku(); if (!s.length) return;
      odeme.disabled = true; odeme.textContent = 'ONE MOMENT…';
      fetch(API + '/api/checkout', {
        method: 'POST', headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ sepet: s.map(function (x) { return { slug: x.slug, adet: x.adet }; }) })
      }).then(function (r) { return r.json(); }).then(function (j) {
        if (j.url) { location.href = j.url; return; }
        alert(j.hata || 'Checkout is not available yet. Please email info@butitlookscute.com.');
        odeme.disabled = false; odeme.textContent = 'CHECKOUT →';
      }).catch(function () {
        alert('Could not reach checkout. Please email info@butitlookscute.com.');
        odeme.disabled = false; odeme.textContent = 'CHECKOUT →';
      });
    });
    ciz();
  });
  ciz();
})();
