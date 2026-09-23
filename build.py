# -*- coding: utf-8 -*-
"""Static site generator for Twin Cities Pawn & Gun (Stitch neo-brutalist design).
Generates all HTML pages with shared nav / ticker / footer. Run: python3 build.py"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://twin-cities-pawn-guns.pages.dev"
ARMSLIST = "https://www.armslist.com/store/227/twin-cities-pawn"
GUNBROKER = "https://www.gunbroker.com/All/search?Keywords=twin%20cities%20pawn&Sort=13"
GMAPS = "https://maps.app.goo.gl/QMvtTgS8PpCSxRGJ8"

TAILWIND_CONFIG = """tailwind.config = {
  darkMode: "class",
  theme: { extend: {
    colors: {
      "primary-container": "#facc15", "on-primary-container": "#6c5700",
      "surface": "#131316", "surface-dim": "#131316",
      "surface-container-lowest": "#0e0e11", "surface-container-low": "#1b1b1e",
      "surface-container": "#1f1f22", "surface-container-high": "#2a2a2d",
      "surface-container-highest": "#353438", "surface-bright": "#39393c",
      "surface-tint": "#eec200", "on-surface": "#e5e1e6", "on-surface-variant": "#d1c6ab",
      "primary": "#ffecb9", "on-primary": "#3c2f00", "primary-fixed": "#ffe083",
      "primary-fixed-dim": "#eec200", "inverse-primary": "#735c00",
      "secondary": "#c7c5d0", "secondary-container": "#46464f", "on-secondary-container": "#b6b4bf",
      "outline": "#9a9078", "outline-variant": "#4d4632",
      "inverse-surface": "#e5e1e6", "inverse-on-surface": "#303033",
      "background": "#131316", "on-background": "#e5e1e6", "surface-variant": "#353438"
    },
    borderRadius: { "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" },
    spacing: { "gutter": "1.5rem", "margin": "2rem", "space-xs": "0.25rem", "space-sm": "0.5rem",
      "space-md": "1rem", "space-lg": "1.5rem", "space-xl": "2.5rem" },
    fontFamily: { "headline": ["Space Grotesk"], "body": ["Hanken Grotesk"], "mono": ["JetBrains Mono"] },
    fontSize: {
      "display-hero": ["72px", { lineHeight: "80px", letterSpacing: "-0.03em", fontWeight: "700" }],
      "display-hero-mobile": ["40px", { lineHeight: "46px", letterSpacing: "-0.02em", fontWeight: "700" }],
      "headline-xl": ["48px", { lineHeight: "56px", letterSpacing: "-0.02em", fontWeight: "700" }],
      "headline-xl-mobile": ["32px", { lineHeight: "38px", letterSpacing: "-0.01em", fontWeight: "700" }],
      "headline-lg": ["36px", { lineHeight: "44px", letterSpacing: "-0.015em", fontWeight: "600" }],
      "headline-md": ["24px", { lineHeight: "32px", fontWeight: "600" }],
      "headline-sm": ["20px", { lineHeight: "28px", fontWeight: "600" }],
      "body-lg": ["18px", { lineHeight: "28px", fontWeight: "400" }],
      "body-md": ["15px", { lineHeight: "24px", fontWeight: "400" }],
      "body-sm": ["13px", { lineHeight: "20px", fontWeight: "400" }],
      "label-data": ["13px", { lineHeight: "18px", letterSpacing: "0.04em", fontWeight: "500" }],
      "label-caps": ["11px", { lineHeight: "14px", letterSpacing: "0.12em", fontWeight: "700" }]
    }
  } }
}"""


def head(title, desc, canonical, keywords, schema=""):
    schema_block = ""
    if schema:
        schema_block = '\n  <script type="application/ld+json">\n%s\n  </script>' % schema
    return """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{base}/{canon}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="images/og-image.jpg" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{base}/{canon}" />
  <meta property="og:site_name" content="Twin Cities Pawn &amp; Gun" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="images/og-image.jpg" />
  <link rel="icon" type="image/png" href="images/logo.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
{twcfg}
  </script>
  <link rel="stylesheet" href="css/styles.css" />{schema}
</head>
<body class="font-body bg-surface text-on-surface antialiased">
""".format(title=title, desc=desc, keywords=keywords, base=BASE_URL, canon=canonical,
           twcfg=TAILWIND_CONFIG, schema=schema_block)



def nav():
    return """
  <!-- ===== NAV ===== -->
  <header class="sticky top-0 z-50 bg-surface-container-lowest/80 backdrop-blur-xl border-b border-outline-variant/30">
    <div class="max-w-[1360px] mx-auto px-6 lg:px-margin flex justify-between items-center py-4">
      <a href="index.html" class="flex items-center gap-3 group">
        <img src="images/logo.png" alt="Twin Cities Pawn &amp; Gun logo" class="h-10 w-auto" />
        <div class="hidden sm:flex flex-col">
          <span class="font-headline text-sm font-bold tracking-wider uppercase text-on-surface">Twin Cities Pawn &amp; Gun</span>
          <span class="font-mono text-[9px] text-outline tracking-widest uppercase">Home of the 0% Pawn &middot; Ramsey, MN</span>
        </div>
      </a>
      <nav class="hidden md:flex items-center space-x-6" aria-label="Main navigation">
        <a href="index.html" data-nav="index.html" class="nav-link">Home</a>
        <a href="about.html" data-nav="about.html" class="nav-link">About</a>
        <div class="dropdown relative">
          <button class="nav-link flex items-center gap-1">Inventory <span class="material-symbols-outlined text-base">expand_more</span></button>
          <div class="dropdown-menu bg-surface-container-lowest border border-outline-variant/40 shadow-2xl">
            <div class="border-b border-outline-variant/30 px-4 py-3">
              <div class="text-[10px] font-mono text-primary-container uppercase tracking-widest mb-2">Firearms</div>
              <a href="guns-rifles.html" class="block px-2 py-1.5 text-sm font-headline text-on-surface hover:text-primary-container">&#128299; Guns &amp; Rifles</a>
              <div class="pl-4 space-y-0.5 text-xs text-on-surface-variant mt-1">
                <a href="guns-rifles.html#handguns" class="block hover:text-primary-container py-0.5">&rsaquo; Handguns &amp; Pistols</a>
                <a href="guns-rifles.html#revolvers" class="block hover:text-primary-container py-0.5">&rsaquo; Revolvers</a>
                <a href="guns-rifles.html#rifles" class="block hover:text-primary-container py-0.5">&rsaquo; Hunting &amp; Tactical Rifles</a>
                <a href="guns-rifles.html#shotguns" class="block hover:text-primary-container py-0.5">&rsaquo; Shotguns</a>
                <a href="guns-rifles.html#collectible" class="block hover:text-primary-container py-0.5">&rsaquo; Collectible Firearms</a>
                <a href="guns-rifles.html#nfa" class="block hover:text-primary-container py-0.5">&rsaquo; NFA Items</a>
                <a href="guns-rifles.html#archery" class="block hover:text-primary-container py-0.5">&rsaquo; Archery</a>
              </div>
            </div>
            <div class="border-b border-outline-variant/30 px-4 py-3">
              <div class="text-[10px] font-mono text-primary-container uppercase tracking-widest mb-2">Accessories</div>
              <a href="accessories.html" class="block px-2 py-1.5 text-sm font-headline text-on-surface hover:text-primary-container">&#127919; All Accessories</a>
              <div class="pl-4 space-y-0.5 text-xs text-on-surface-variant mt-1">
                <a href="accessories.html#ammo" class="block hover:text-primary-container py-0.5">&rsaquo; Ammunition &amp; Ammo</a>
                <a href="accessories.html#optics" class="block hover:text-primary-container py-0.5">&rsaquo; Sights, Scopes &amp; Optics</a>
                <a href="accessories.html#holsters" class="block hover:text-primary-container py-0.5">&rsaquo; Holsters, Slings &amp; Cases</a>
                <a href="accessories.html#magazines" class="block hover:text-primary-container py-0.5">&rsaquo; Magazines &amp; Safes</a>
              </div>
            </div>
            <div class="px-4 py-3">
              <div class="text-[10px] font-mono text-primary-container uppercase tracking-widest mb-2">Pawn &amp; Loans</div>
              <a href="pawn-loans.html" class="block px-2 py-1.5 text-sm font-headline text-on-surface hover:text-primary-container">&#128176; Pawn &amp; Loans</a>
              <div class="pl-4 space-y-0.5 text-xs text-on-surface-variant mt-1">
                <a href="pawn-loans.html#tools" class="block hover:text-primary-container py-0.5">&rsaquo; Power Tools</a>
                <a href="pawn-loans.html#electronics" class="block hover:text-primary-container py-0.5">&rsaquo; Electronics</a>
                <a href="pawn-loans.html#jewelry" class="block hover:text-primary-container py-0.5">&rsaquo; Jewelry &amp; Gold</a>
                <a href="pawn-loans.html#loans" class="block hover:text-primary-container py-0.5">&rsaquo; Pawn Loans (0%)</a>
              </div>
            </div>
          </div>
        </div>
        <div class="dropdown relative">
          <button class="nav-link flex items-center gap-1">Online Store <span class="material-symbols-outlined text-base">expand_more</span></button>
          <div class="dropdown-menu bg-surface-container-lowest border border-outline-variant/40 shadow-2xl">
            <a href="{armslist}" target="_blank" rel="noopener" class="block px-4 py-3 text-sm text-on-surface hover:text-primary-container border-b border-outline-variant/20">
              <div class="font-bold font-headline">Armslist</div>
              <div class="text-xs text-on-surface-variant">Browse our Armslist listings</div>
            </a>
            <a href="{gunbroker}" target="_blank" rel="noopener" class="block px-4 py-3 text-sm text-on-surface hover:text-primary-container">
              <div class="font-bold font-headline">GunBroker</div>
              <div class="text-xs text-on-surface-variant">Shop our GunBroker inventory</div>
            </a>
          </div>
        </div>
        <a href="contact.html" data-nav="contact.html" class="nav-link">Contact</a>
      </nav>
      <div class="hidden md:flex items-center gap-3">
        <a href="tel:7634274100" class="font-mono text-sm text-primary-container hover:text-primary-fixed">(763) 427-4100</a>
        <a href="contact.html" class="bg-primary-container text-surface-container-lowest font-headline text-xs uppercase px-5 py-2.5 font-bold tracking-wider gold-hover">Get a Quote</a>
      </div>
      <button id="hamburger" class="md:hidden p-2 text-on-surface" aria-label="Toggle menu"><span class="material-symbols-outlined">menu</span></button>
    </div>
    <!-- Mobile menu -->
    <div id="mobile-menu" class="md:hidden bg-surface-container-lowest border-t border-outline-variant/30">
      <div class="px-6 py-4 flex flex-col gap-1 text-sm">
        <a href="index.html" class="py-2 font-headline text-on-surface hover:text-primary-container">Home</a>
        <a href="about.html" class="py-2 font-headline text-on-surface hover:text-primary-container">About</a>
        <button data-accordion-toggle="m-inv" class="flex justify-between items-center py-2 font-headline text-on-surface w-full">Inventory <span class="material-symbols-outlined acc-chevron text-base">expand_more</span></button>
        <div id="m-inv" class="hidden pl-3 border-l border-outline-variant/30 space-y-1 pb-2">
          <a href="guns-rifles.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Guns &amp; Rifles</a>
          <a href="guns-rifles.html#handguns" class="block py-1 text-xs text-on-surface-variant hover:text-primary-container">&rsaquo; Handguns &amp; Pistols</a>
          <a href="guns-rifles.html#rifles" class="block py-1 text-xs text-on-surface-variant hover:text-primary-container">&rsaquo; Rifles</a>
          <a href="guns-rifles.html#shotguns" class="block py-1 text-xs text-on-surface-variant hover:text-primary-container">&rsaquo; Shotguns</a>
          <a href="accessories.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Accessories &amp; Ammo</a>
          <a href="pawn-loans.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Pawn &amp; Loans</a>
        </div>
        <button data-accordion-toggle="m-online" class="flex justify-between items-center py-2 font-headline text-on-surface w-full">Online Store <span class="material-symbols-outlined acc-chevron text-base">expand_more</span></button>
        <div id="m-online" class="hidden pl-3 border-l border-outline-variant/30 space-y-1 pb-2">
          <a href="{armslist}" target="_blank" rel="noopener" class="block py-1 text-on-surface-variant hover:text-primary-container">Armslist Store</a>
          <a href="{gunbroker}" target="_blank" rel="noopener" class="block py-1 text-on-surface-variant hover:text-primary-container">GunBroker Listings</a>
        </div>
        <a href="contact.html" class="py-2 font-headline text-on-surface hover:text-primary-container">Contact</a>
        <a href="contact.html" class="mt-2 bg-primary-container text-surface-container-lowest font-headline text-xs uppercase px-5 py-3 font-bold tracking-wider text-center">Get a Quote</a>
        <a href="tel:7634274100" class="mt-1 font-mono text-sm text-primary-container text-center py-2">(763) 427-4100</a>
      </div>
    </div>
  </header>
""".format(armslist=ARMSLIST, gunbroker=GUNBROKER)


def ticker():
    items = ("&#128299; 300+ FIREARMS IN STOCK &nbsp;&middot;&nbsp; &#9989; LICENSED FFL DEALER &nbsp;&middot;&nbsp; "
             "&#128176; HOME OF THE 0% PAWN &nbsp;&middot;&nbsp; &#127942; SERVING RAMSEY MN SINCE 2010 &nbsp;&middot;&nbsp; "
             "&#128230; SHOP ONLINE: ARMSLIST &amp; GUNBROKER &nbsp;&middot;&nbsp; &#9742; (763) 427-4100 &nbsp;&middot;&nbsp; ")
    span = '<span class="font-mono text-[11px] tracking-widest text-on-surface-variant uppercase px-4">%s</span>' % items
    return """
  <!-- ===== TICKER ===== -->
  <div class="ticker-wrap bg-surface-container-lowest border-b border-outline-variant/30 py-2 overflow-hidden">
    <div class="ticker-inner">{span}{span}</div>
  </div>
""".format(span=span)


def footer():
    return """
  <!-- ===== FOOTER ===== -->
  <footer class="bg-surface-container-lowest border-t border-outline-variant/30">
    <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 grid grid-cols-1 md:grid-cols-4 gap-8">
      <div>
        <img src="images/logo.png" alt="Twin Cities Pawn &amp; Gun" class="h-12 mb-4" />
        <p class="text-on-surface-variant text-sm mb-4">Home of the 0% Pawn. Serving the Minneapolis&ndash;St. Paul area with honesty and integrity since 2010.</p>
        <div class="font-mono text-xs text-primary-container">(763) 427-4100</div>
        <div class="text-xs text-on-surface-variant mt-1">6650 US-10, Ramsey, MN 55303</div>
      </div>
      <div>
        <div class="text-[10px] font-bold text-primary-container uppercase tracking-widest mb-4">Inventory</div>
        <ul class="space-y-2 text-sm text-on-surface-variant">
          <li><a href="guns-rifles.html" class="hover:text-primary-container transition-colors">Guns &amp; Rifles</a></li>
          <li><a href="guns-rifles.html#handguns" class="hover:text-primary-container transition-colors">Handguns &amp; Pistols</a></li>
          <li><a href="guns-rifles.html#shotguns" class="hover:text-primary-container transition-colors">Shotguns</a></li>
          <li><a href="accessories.html" class="hover:text-primary-container transition-colors">Accessories</a></li>
          <li><a href="accessories.html#ammo" class="hover:text-primary-container transition-colors">Ammunition</a></li>
        </ul>
      </div>
      <div>
        <div class="text-[10px] font-bold text-primary-container uppercase tracking-widest mb-4">Services</div>
        <ul class="space-y-2 text-sm text-on-surface-variant">
          <li><a href="pawn-loans.html" class="hover:text-primary-container transition-colors">Pawn Loans (0%)</a></li>
          <li><a href="pawn-loans.html#tools" class="hover:text-primary-container transition-colors">Power Tools</a></li>
          <li><a href="pawn-loans.html#jewelry" class="hover:text-primary-container transition-colors">Jewelry &amp; Gold</a></li>
          <li><a href="about.html" class="hover:text-primary-container transition-colors">About Us</a></li>
          <li><a href="contact.html" class="hover:text-primary-container transition-colors">Contact</a></li>
        </ul>
      </div>
      <div>
        <div class="text-[10px] font-bold text-primary-container uppercase tracking-widest mb-4">Online &amp; Hours</div>
        <div class="space-y-2 text-sm text-on-surface-variant">
          <a href="{armslist}" target="_blank" rel="noopener" class="flex items-center gap-2 hover:text-primary-container"><span class="material-symbols-outlined text-sm">open_in_new</span>Armslist Store</a>
          <a href="{gunbroker}" target="_blank" rel="noopener" class="flex items-center gap-2 hover:text-primary-container"><span class="material-symbols-outlined text-sm">open_in_new</span>GunBroker Listings</a>
          <a href="{gmaps}" target="_blank" rel="noopener" class="flex items-center gap-2 hover:text-primary-container"><span class="material-symbols-outlined text-sm">location_on</span>Google Maps</a>
        </div>
        <div class="mt-4 border-t border-outline-variant/20 pt-4 font-mono text-xs text-on-surface-variant space-y-1">
          <div>Mon&ndash;Fri: 10AM &ndash; 7PM</div>
          <div>Saturday: 10AM &ndash; 5PM</div>
          <div>Sunday: <span class="text-outline">Closed</span></div>
        </div>
      </div>
    </div>
    <div class="border-t border-outline-variant/30 bg-surface-container-lowest/60">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-4 flex flex-col md:flex-row justify-between items-center gap-3 text-xs text-on-surface-variant">
        <div class="flex flex-wrap gap-3 justify-center">
          <a href="terms.html" class="hover:text-primary-container">Terms &amp; Conditions</a><span class="text-outline-variant">|</span>
          <a href="equal-opportunity.html" class="hover:text-primary-container">Equal Opportunity Employer</a><span class="text-outline-variant">|</span>
          <a href="privacy.html" class="hover:text-primary-container">Privacy Policy</a><span class="text-outline-variant">|</span>
          <a href="faq.html" class="hover:text-primary-container">FAQ</a><span class="text-outline-variant">|</span>
          <a href="sitemap.html" class="hover:text-primary-container">Sitemap</a>
        </div>
        <div class="text-center font-mono text-[11px] text-outline">&copy; <span id="year">2026</span> Twin Cities Pawn &amp; Gun &middot; 6650 US-10, Ramsey, MN 55303 | Designed by <a href="https://webcreativeseo.com" class="hover:text-primary-container" target="_blank" rel="noopener">Webcreativeseo.com</a></div>
      </div>
      <div class="text-center pb-3 text-[10px] text-outline font-mono px-4">All firearm sales comply with federal, state &amp; local laws. FFL licensed. Valid ID required for all transactions.</div>
    </div>
  </footer>
  <script src="js/main.js"></script>
</body>
</html>
""".format(armslist=ARMSLIST, gunbroker=GUNBROKER, gmaps=GMAPS)



# ---------- Reusable helpers ----------
BRANDS = ["Glock", "Smith &amp; Wesson", "Sig Sauer", "Ruger", "Colt", "Kimber", "Taurus",
          "Springfield Armory", "Remington", "Mossberg", "Henry", "Browning",
          "Daniel Defense", "Walther", "KelTec"]


def brand_chips():
    chips = "\n".join('        <span class="brand-chip">%s</span>' % b for b in BRANDS)
    return chips


def label(text):
    return ('<div class="inline-flex items-center gap-2 font-mono text-[11px] tracking-widest '
            'text-primary-container uppercase mb-4"><span class="w-6 h-px bg-primary-container"></span>%s</div>' % text)


def crosshairs():
    return ('<span class="xh tl">+</span><span class="xh tr">+</span>'
            '<span class="xh bl">+</span><span class="xh br">+</span>')


def inv_card(img, alt, badge, title, cond, cdn=False, lazy=True):
    src = img if cdn else ("images/" + img)
    loading = ' loading="lazy"' if lazy else ''
    return """
        <article class="inv-card group">
          <div class="relative overflow-hidden h-56">
            <img src="{src}" alt="{alt}" class="w-full h-56 object-cover"{loading} />
            <span class="absolute top-3 left-3 bg-primary-container text-surface-container-lowest font-mono text-[10px] font-bold uppercase tracking-wider px-2 py-1">{badge}</span>
          </div>
          <div class="p-5">
            <h3 class="font-headline font-semibold text-lg text-on-surface">{title}</h3>
            <div class="mt-2 flex items-center justify-between">
              <span class="font-mono text-[11px] text-outline uppercase tracking-wider">{cond}</span>
              <span class="material-symbols-outlined text-primary-container text-lg">arrow_outward</span>
            </div>
          </div>
        </article>""".format(src=src, alt=alt, badge=badge, title=title, cond=cond, loading=loading)


def page_hero(img, alt, label_text, h1, sub=""):
    sub_html = ('<p class="mt-4 text-on-surface-variant text-body-lg max-w-2xl">%s</p>' % sub) if sub else ""
    return """
    <section class="relative min-h-[46vh] flex items-end blueprint-grid" aria-label="Page header">
      <img src="images/{img}" alt="{alt}" class="absolute inset-0 w-full h-full object-cover opacity-40" />
      <div class="absolute inset-0" style="background:linear-gradient(180deg,rgba(19,19,22,0.55),rgba(19,19,22,0.95))"></div>
      <div class="relative max-w-[1360px] mx-auto px-6 lg:px-margin pb-12 pt-20 w-full">
        {label}
        <h1 class="font-headline font-bold text-headline-xl-mobile md:text-headline-xl text-on-surface">{h1}</h1>
        {sub}
      </div>
    </section>""".format(img=img, alt=alt, label=label(label_text), h1=h1, sub=sub_html)


def text_hero(label_text, h1, sub=""):
    sub_html = ('<p class="mt-4 text-on-surface-variant text-body-lg max-w-2xl">%s</p>' % sub) if sub else ""
    return """
    <section class="relative blueprint-grid bg-surface-container-lowest border-b border-outline-variant/30" aria-label="Page header">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-20">
        {label}
        <h1 class="font-headline font-bold text-headline-xl-mobile md:text-headline-xl text-on-surface">{h1}</h1>
        {sub}
      </div>
    </section>""".format(label=label(label_text), h1=h1, sub=sub_html)


def online_cta():
    return """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <div class="grid md:grid-cols-2 gap-6">
        <a href="{armslist}" target="_blank" rel="noopener" class="crosshair-card block bg-surface-container-low border border-outline-variant/40 p-8 gold-aura-hover">
          {xh}
          <span class="material-symbols-outlined text-primary-container text-3xl">storefront</span>
          <h3 class="font-headline font-bold text-headline-sm mt-3 text-on-surface">Armslist Store</h3>
          <p class="text-sm text-on-surface-variant mt-2">Browse our current firearm listings on Armslist &mdash; new items added regularly.</p>
          <span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">View listings <span class="material-symbols-outlined text-sm">arrow_outward</span></span>
        </a>
        <a href="{gunbroker}" target="_blank" rel="noopener" class="crosshair-card block bg-surface-container-low border border-outline-variant/40 p-8 gold-aura-hover">
          {xh}
          <span class="material-symbols-outlined text-primary-container text-3xl">gavel</span>
          <h3 class="font-headline font-bold text-headline-sm mt-3 text-on-surface">GunBroker</h3>
          <p class="text-sm text-on-surface-variant mt-2">Shop our online auctions and inventory on GunBroker.</p>
          <span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Shop online <span class="material-symbols-outlined text-sm">arrow_outward</span></span>
        </a>
      </div>
    </section>""".format(armslist=ARMSLIST, gunbroker=GUNBROKER, xh=crosshairs())


def hours_location():
    return """
    <section class="bg-surface-container-lowest border-y border-outline-variant/30 py-16">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid lg:grid-cols-2 gap-10 items-stretch">
        <div class="crosshair-card border border-outline-variant/40 overflow-hidden min-h-[340px] gold-glow">
          <iframe src="https://maps.google.com/maps?q=6650+US-10,+Ramsey,+MN+55303&output=embed" width="100%" height="100%" style="border:0;min-height:340px" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map to Twin Cities Pawn & Gun"></iframe>
        </div>
        <div>
          {label}
          <h2 class="font-headline font-bold text-headline-lg text-on-surface">Hours &amp; Location</h2>
          <address class="not-italic mt-5 text-on-surface-variant">
            <p class="text-lg font-semibold text-on-surface">6650 US-10, Ramsey, MN 55303</p>
            <p class="mt-1"><a href="tel:7634274100" class="font-mono text-primary-container hover:underline">(763) 427-4100</a></p>
            <p class="mt-1"><a href="{gmaps}" target="_blank" rel="noopener" class="text-primary-container hover:underline">Get directions &rarr;</a></p>
          </address>
          <table class="mt-6 w-full font-mono text-sm border border-outline-variant/40">
            <tbody>
              <tr class="border-b border-outline-variant/30"><td class="py-3 px-4 text-on-surface-variant">Monday &ndash; Friday</td><td class="py-3 px-4 text-right text-on-surface">10 AM &ndash; 7 PM</td></tr>
              <tr class="border-b border-outline-variant/30"><td class="py-3 px-4 text-on-surface-variant">Saturday</td><td class="py-3 px-4 text-right text-on-surface">10 AM &ndash; 5 PM</td></tr>
              <tr><td class="py-3 px-4 text-on-surface-variant">Sunday</td><td class="py-3 px-4 text-right text-outline">Closed</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>""".format(label=label("Visit The Vault"), gmaps=GMAPS)
