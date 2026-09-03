# But It Looks Cute

Home & living store — cute things for your space.
Static storefront for **butitlookscute.com**.

## Ne var

| Dosya | Ne |
|---|---|
| `index.html` | Ana sayfa: kahraman bölümü, koleksiyon ızgarası, ürün penceresi (galeri) |
| `about.html` | Hakkımızda — marka hikâyesi ve üç tasarım sistemi |
| `faq.html` | Sık sorulanlar — kargo süresi, bakım, iade |
| `shipping.html` | Kargo ve iade politikası |
| `privacy.html` | Gizlilik politikası |
| `terms.html` | Kullanım koşulları |
| `contact.html` | İletişim — info@butitlookscute.com |
| `style.css` | Ortak stil; marka renkleri CSS değişkenlerinde |
| `katalog.json` | Ürün kataloğu — Printify'dan üretilir |
| `kur-site.py` | Sayfaları tek kaynaktan üretir |

## Marka

| | |
|---|---|
| Lila | `#8B6DC4` |
| Açık lila | `#A78BD0` |
| Siyah | `#111111` |
| Krem | `#F5F2EE` |

Tipografi: **Baloo 2** (başlık, logo) + **Nunito** (metin), Google Fonts.

Üç tasarım sistemi tüm ürünlerde geçerli: **Moo Patch** · **Moo Minimal** · **Moo Check**.

## Yayın

GitHub Pages ile yayınlanır. `CNAME` dosyası `butitlookscute.com` alan adını
işaret eder — alan adının DNS'inde şu kayıtlar bulunmalı:

```
A     185.199.108.153
A     185.199.109.153
A     185.199.110.153
A     185.199.111.153
CNAME www  →  morteglobalonline-ctrl.github.io
```

## Sayfaları yeniden üretmek

```bash
python3 kur-site.py
```

Ortak başlık, menü ve alt bilgi tek yerde durur; her sayfa oradan üretilir.
Ürün kataloğu ayrı bir dosyadır (`katalog.json`) — ürün eklemek sayfa
şablonuna dokunmadan yapılır.

## Not

Sipariş akışı henüz bağlı değil. Ürünler Printify'da kurulu ve fiyatlı;
ödeme ve otomatik sipariş için bir arka uç gerekiyor (Stripe + Printify
Orders API). Şu an sayfalar ürünü tanıtıyor ve iletişime yönlendiriyor.
