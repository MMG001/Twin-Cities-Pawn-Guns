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
      "background": "#131316", "on-background": "#e5e1e6", "surface-variant": "#353438",
      "white": "#ffffff", "gray-50": "#f8f9fa", "gray-100": "#f1f5f9", "gray-200": "#e2e8f0",
      "gray-600": "#4b5563", "gray-700": "#374151", "gray-900": "#111827"
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
  <meta property="og:image" content="{base}/images/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Twin Cities Pawn &amp; Gun storefront in Ramsey, Minnesota" />
  <meta property="og:type" content="business.business" />
  <meta property="og:url" content="{base}/{canon}" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:site_name" content="Twin Cities Pawn &amp; Gun" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{desc}" />
  <meta name="twitter:image" content="{base}/images/og-image.jpg" />
  <meta name="twitter:image:alt" content="Twin Cities Pawn &amp; Gun storefront in Ramsey, Minnesota" />
  <meta name="geo.region" content="US-MN" />
  <meta name="geo.placename" content="Ramsey, Minnesota" />
  <meta name="geo.position" content="45.2619;-93.4499" />
  <meta name="ICBM" content="45.2619, -93.4499" />
  <link rel="icon" type="image/png" href="images/logo.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <!-- Async font load: doesn't block render -->
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap" onload="this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap" /></noscript>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" onload="this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" /></noscript>
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
        <img src="images/logo.png" alt="Twin Cities Pawn &amp; Gun logo" class="h-12 w-auto" />
        <div class="hidden sm:flex flex-col">
          <span class="font-headline text-sm font-bold tracking-wider uppercase text-on-surface">Twin Cities Pawn &amp; Gun</span>
          <span class="font-mono text-[9px] text-outline tracking-widest uppercase">Home of the 0% Pawn &middot; Ramsey, MN</span>
        </div>
      </a>
      <nav class="hidden md:flex items-center space-x-6" aria-label="Main navigation">
        <a href="index.html" data-nav="index.html" class="nav-link">Home</a>
        <a href="about.html" data-nav="about.html" class="nav-link">About</a>
        <div class="dropdown relative" id="inv-dropdown">
          <button class="nav-link flex items-center gap-1" aria-haspopup="true" aria-expanded="false">
            Inventory <span class="material-symbols-outlined text-base leading-none">expand_more</span>
          </button>
          <div class="mega-menu" role="menu">
            <!-- Column Headers -->
            <div class="mega-headers">
              <a href="guns-rifles.html" class="mega-col-hd" role="menuitem">
                <span class="mega-col-icon material-symbols-outlined">local_police</span>
                <div class="mega-col-title">Guns &amp; Rifles</div>
              </a>
              <a href="accessories.html" class="mega-col-hd" role="menuitem">
                <span class="mega-col-icon material-symbols-outlined">target</span>
                <div class="mega-col-title">Accessories</div>
              </a>
              <a href="pawn-loans.html" class="mega-col-hd" role="menuitem">
                <span class="mega-col-icon material-symbols-outlined">payments</span>
                <div class="mega-col-title">Pawn &amp; Loans</div>
              </a>
            </div>
            <!-- Sub-items -->
            <div class="mega-items">
              <div class="mega-col" role="group">
                <a href="guns-rifles.html#handguns" class="mega-item">Handguns &amp; Pistols</a>
                <a href="guns-rifles.html#revolvers" class="mega-item">Revolvers</a>
                <a href="guns-rifles.html#rifles" class="mega-item">Semi-Automatic</a>
                <a href="guns-rifles.html#rifles" class="mega-item">Hunting &amp; Tactical Rifles</a>
                <a href="guns-rifles.html#shotguns" class="mega-item">Shotguns</a>
                <a href="guns-rifles.html#archery" class="mega-item">Archery</a>
              </div>
              <div class="mega-col" role="group">
                <a href="accessories.html#ammo" class="mega-item">Ammunition &amp; Ammo</a>
                <a href="accessories.html#optics" class="mega-item">Sights, Scopes &amp; Optics</a>
                <a href="accessories.html#holsters" class="mega-item">Holsters, Slings &amp; Cases</a>
                <a href="accessories.html#magazines" class="mega-item">Magazines &amp; Safes</a>
              </div>
              <div class="mega-col" role="group">
                <a href="pawn-loans.html#tools" class="mega-item">Power Tools</a>
                <a href="pawn-loans.html#electronics" class="mega-item">Electronics</a>
                <a href="pawn-loans.html#jewelry" class="mega-item">Jewelry &amp; Gold</a>
                <a href="pawn-loans.html#loans" class="mega-item">Pawn Loans (0%)</a>
              </div>
            </div>
            <!-- Footer Action Bar -->
            <div class="mega-footer">
              <a href="guns-rifles.html" class="mega-footer-all">Browse All Inventory <span class="material-symbols-outlined text-sm leading-none">arrow_forward</span></a>
              <div class="mega-footer-right">
                <a href="{armslist}" target="_blank" rel="noopener" class="mega-footer-link">Shop Armslist</a>
                <span class="mega-footer-sep">|</span>
                <a href="{gunbroker}" target="_blank" rel="noopener" class="mega-footer-link">Shop GunBroker</a>
                <a href="contact.html" class="mega-footer-cta">Get a Quote &rarr;</a>
              </div>
            </div>
          </div>
        </div>
        <div class="dropdown relative" id="res-dropdown">
          <button class="nav-link flex items-center gap-1" aria-haspopup="true" aria-expanded="false">
            Resources <span class="material-symbols-outlined text-base leading-none">expand_more</span>
          </button>
          <div class="mega-menu" role="menu">
            <!-- Column Headers -->
            <div class="mega-headers">
              <a href="resources.html" class="mega-col-hd" role="menuitem">
                <span class="mega-col-icon material-symbols-outlined">menu_book</span>
                <div class="mega-col-title">MN Gun Laws &amp; Guides</div>
              </a>
              <a href="faq.html" class="mega-col-hd" role="menuitem">
                <span class="mega-col-icon material-symbols-outlined">quiz</span>
                <div class="mega-col-title">FAQ</div>
              </a>
              <a href="contact.html" class="mega-col-hd" role="menuitem">
                <span class="mega-col-icon material-symbols-outlined">support_agent</span>
                <div class="mega-col-title">Contact &amp; Help</div>
              </a>
            </div>
            <!-- Sub-items -->
            <div class="mega-items">
              <div class="mega-col" role="group">
                <a href="gun-law-checklist.html" class="mega-item">2026 Gun Law Checklist</a>
                <a href="rules-for-pawning.html" class="mega-item">Rules for Pawning a Gun</a>
                <a href="gun-license-mn.html" class="mega-item">Gun License in Minnesota</a>
                <a href="unregistered-gun.html" class="mega-item">Unregistered Firearms</a>
              </div>
              <div class="mega-col" role="group">
                <a href="faq.html" class="mega-item">General FAQ</a>
                <a href="faq-gun-pawns.html" class="mega-item">Gun Pawn FAQ</a>
              </div>
              <div class="mega-col" role="group">
                <a href="contact.html" class="mega-item">Contact Us</a>
                <a href="employment.html" class="mega-item">Employment</a>
                <a href="about.html" class="mega-item">About Us</a>
              </div>
            </div>
            <!-- Footer Action Bar -->
            <div class="mega-footer">
              <a href="resources.html" class="mega-footer-all">Browse All Resources <span class="material-symbols-outlined text-sm leading-none">arrow_forward</span></a>
              <div class="mega-footer-right">
                <a href="{armslist}" target="_blank" rel="noopener" class="mega-footer-link">Shop Armslist</a>
                <span class="mega-footer-sep">|</span>
                <a href="{gunbroker}" target="_blank" rel="noopener" class="mega-footer-link">Shop GunBroker</a>
              </div>
            </div>
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
        <button data-accordion-toggle="m-res" class="flex justify-between items-center py-2 font-headline text-on-surface w-full">Resources <span class="material-symbols-outlined acc-chevron text-base">expand_more</span></button>
        <div id="m-res" class="hidden pl-3 border-l border-outline-variant/30 space-y-1 pb-2">
          <a href="gun-law-checklist.html" class="block py-1 text-on-surface-variant hover:text-primary-container">2026 Gun Law Checklist</a>
          <a href="rules-for-pawning.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Rules for Pawning a Gun</a>
          <a href="gun-license-mn.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Gun License in Minnesota</a>
          <a href="unregistered-gun.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Unregistered Firearms</a>
          <a href="faq.html" class="block py-1 text-on-surface-variant hover:text-primary-container">General FAQ</a>
          <a href="faq-gun-pawns.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Gun Pawn FAQ</a>
          <a href="employment.html" class="block py-1 text-on-surface-variant hover:text-primary-container">Employment</a>
        </div>
        <a href="contact.html" class="py-2 font-headline text-on-surface hover:text-primary-container">Contact</a>
        <a href="contact.html" class="mt-2 bg-primary-container text-surface-container-lowest font-headline text-xs uppercase px-5 py-3 font-bold tracking-wider text-center">Get a Quote</a>
        <a href="tel:7634274100" class="mt-1 font-mono text-sm text-primary-container text-center py-2">(763) 427-4100</a>
      </div>
    </div>
  </header>
  <main id="main-content">
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
  </main>
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
          <li><a href="pawn-loans.html" class="hover:text-primary-container transition-colors">Pawn &amp; Loans</a></li>
          <li><a href="pawn-loans.html" class="hover:text-primary-container transition-colors">FFL Transfers ($50)</a></li>
          <li><a href="about.html" class="hover:text-primary-container transition-colors">About Us</a></li>
          <li><a href="contact.html" class="hover:text-primary-container transition-colors">Contact</a></li>
        </ul>
        <div class="text-[10px] font-bold text-primary-container uppercase tracking-widest mt-6 mb-4">Resources</div>
        <ul class="space-y-2 text-sm text-on-surface-variant">
          <li><a href="gun-law-checklist.html" class="hover:text-primary-container transition-colors">2026 Gun Law Checklist</a></li>
          <li><a href="gun-license-mn.html" class="hover:text-primary-container transition-colors">MN Gun License Guide</a></li>
          <li><a href="rules-for-pawning.html" class="hover:text-primary-container transition-colors">Rules for Pawning a Gun</a></li>
          <li><a href="resources.html" class="hover:text-primary-container transition-colors">All Resources</a></li>
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
          <a href="resources.html" class="hover:text-primary-container">Resources</a><span class="text-outline-variant">|</span>
          <a href="sitemap.html" class="hover:text-primary-container">Sitemap</a>
        </div>
        <div class="text-center font-mono text-[11px] text-outline">&copy; <span id="year">2026</span> Twin Cities Pawn &amp; Gun &middot; 6650 US-10, Ramsey, MN 55303 | Designed by <a href="https://webcreativeseo.com" class="hover:text-primary-container" target="_blank" rel="noopener">Webcreativeseo.com</a></div>
      </div>
      <!-- Social validation signals -->
      <div class="flex justify-center gap-5 py-2">
        <a href="https://www.facebook.com/twincitiespawn" target="_blank" rel="noopener me" aria-label="Twin Cities Pawn &amp; Gun on Facebook" class="text-outline hover:text-primary-container transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        </a>
        <a href="https://www.instagram.com/twincities_pawn/" target="_blank" rel="noopener me" aria-label="Twin Cities Pawn &amp; Gun on Instagram" class="text-outline hover:text-primary-container transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        </a>
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


def brand_chips_light():
    chips = "\n".join('        <span class="brand-chip-light">%s</span>' % b for b in BRANDS)
    return chips


def label(text):
    return ('<div class="inline-flex items-center gap-2 font-mono text-[11px] tracking-widest '
            'text-primary-container uppercase mb-4"><span class="w-6 h-px bg-primary-container"></span>%s</div>' % text)


def crosshairs():
    return ('<span class="xh tl">+</span><span class="xh tr">+</span>'
            '<span class="xh bl">+</span><span class="xh br">+</span>')


def inv_card(img, alt, badge, title, cond, cdn=False, lazy=True, light=False):
    src = img if cdn else ("images/" + img)
    loading = ' loading="lazy"' if lazy else ''
    card_class = "inv-card-light" if light else "inv-card"
    title_style = "color:#111827" if light else ""
    cond_style = "color:#6b7280" if light else "color:#9a9078"
    return """
        <article class="{card_class} group">
          <div class="relative overflow-hidden h-56">
            <img src="{src}" alt="{alt}" class="w-full h-56 object-cover"{loading} />
          </div>
          <div class="p-5">
            <h3 class="font-headline font-semibold text-lg" style="{title_style}">{title}</h3>
            <div class="mt-2 flex items-center justify-between">
              <span class="font-mono text-[11px] uppercase tracking-wider" style="{cond_style}">{cond}</span>
              <span class="material-symbols-outlined text-primary-container text-lg">arrow_outward</span>
            </div>
          </div>
        </article>""".format(card_class=card_class, src=src, alt=alt, badge=badge, title=title,
                             cond=cond, loading=loading, title_style=title_style, cond_style=cond_style)


def page_hero(img, alt, label_text, h1, sub=""):
    sub_html = ('<p class="mt-4 text-on-surface-variant text-body-lg max-w-2xl">%s</p>' % sub) if sub else ""
    return """
    <section class="relative min-h-[46vh] flex items-end blueprint-grid" aria-label="Page header">
      <img src="images/{img}" alt="{alt}" class="absolute inset-0 w-full h-full object-cover" />
      <div class="absolute inset-0" style="background:rgba(0,0,0,0.60)"></div>
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
    <section class="bg-surface-container-lowest border-y border-outline-variant/30 py-16">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <!-- Section header -->
        <div class="text-center mb-10">
          <div class="inline-flex items-center gap-3 font-mono text-[11px] tracking-widest text-primary-container uppercase mb-4">
            <span class="w-8 h-px bg-primary-container inline-block"></span>Shop Our Inventory Online<span class="w-8 h-px bg-primary-container inline-block"></span>
          </div>
          <h2 class="font-headline font-bold text-headline-lg text-on-surface">Buy Firearms Online &mdash; Ramsey, MN</h2>
          <p class="mt-4 text-on-surface-variant max-w-2xl mx-auto">
            Twin Cities Pawn &amp; Gun lists handguns, pistols, rifles, shotguns, and collectible firearms on Armslist and GunBroker. Browse current in-stock inventory, place bids, or call us to verify availability. New guns added regularly &mdash; inventory moves fast.
          </p>
        </div>
        <!-- Marketplace cards -->
        <div class="grid md:grid-cols-2 gap-6">
          <a href="{armslist}" target="_blank" rel="noopener"
             class="crosshair-card group relative block border border-primary-container/30 overflow-hidden gold-aura-hover"
             style="min-height:360px">
            {xh}
            <div class="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105"
                 style="background-image:url('images/armslist-card-bg.webp')"></div>
            <div class="absolute inset-0" style="background:rgba(0,0,0,0.60)"></div>
            <div class="relative flex flex-col justify-end h-full p-8 md:p-10"
                 style="min-height:360px;z-index:10">
              <img src="images/logo-armslist.webp" alt="ArmsLIST Firearms Marketplace"
                   style="height:64px;width:auto;max-width:260px;object-fit:contain;object-position:left;align-self:flex-start;filter:brightness(0) invert(1)" class="mb-5" />
              <h3 class="font-headline font-bold text-white text-xl">Armslist Store</h3>
              <p class="text-white/75 mt-2 text-sm leading-relaxed max-w-sm">
                Browse our current handgun, rifle, and shotgun listings on Armslist &mdash; new firearms added regularly.
              </p>
              <span class="inline-flex items-center gap-2 mt-5 font-mono text-xs uppercase tracking-wider text-primary-container font-bold">
                View Listings <span class="material-symbols-outlined text-sm">arrow_outward</span>
              </span>
            </div>
          </a>
          <a href="{gunbroker}" target="_blank" rel="noopener"
             class="crosshair-card group relative block border border-primary-container/30 overflow-hidden gold-aura-hover"
             style="min-height:360px">
            {xh}
            <div class="absolute inset-0 bg-cover bg-center transition-transform duration-700 group-hover:scale-105"
                 style="background-image:url('images/gunbroker-card-bg.webp')"></div>
            <div class="absolute inset-0" style="background:rgba(0,0,0,0.60)"></div>
            <div class="relative flex flex-col justify-end h-full p-8 md:p-10"
                 style="min-height:360px;z-index:10">
              <img src="images/logo-gunbroker.webp" alt="GunBroker.com"
                   style="height:72px;width:auto;max-width:220px;object-fit:contain;object-position:left;align-self:flex-start" class="mb-5" />
              <h3 class="font-headline font-bold text-white text-xl">GunBroker</h3>
              <p class="text-white/75 mt-2 text-sm leading-relaxed max-w-sm">
                Online firearm auctions and buy-it-now listings. Pistols, revolvers, rifles, and collectible guns shipped to your local FFL.
              </p>
              <span class="inline-flex items-center gap-2 mt-5 font-mono text-xs uppercase tracking-wider text-primary-container font-bold">
                Shop Online <span class="material-symbols-outlined text-sm">arrow_outward</span>
              </span>
            </div>
          </a>
        </div>
      </div>
    </section>""".format(armslist=ARMSLIST, gunbroker=GUNBROKER, xh=crosshairs())


def keyword_entity_table():
    """Semantic keyword/entity table for topical authority + contextual interlinking."""
    rows = [
        ("Firearms",
         'Handguns, <a href="guns-rifles.html#handguns">pistols</a>, revolvers, semi-automatic pistols, '
         '<a href="guns-rifles.html">rifles</a>, bolt-action rifles, AR-15 platform rifles, '
         '<a href="guns-rifles.html#shotguns">shotguns</a>, collectible &amp; used guns',
         "guns-rifles.html"),
        ("Firearm Brands",
         'Glock, Smith &amp; Wesson, SIG Sauer, Ruger, Colt, Kimber, Taurus, Springfield Armory, '
         'Remington, Mossberg, Henry Repeating Arms, Browning, Daniel Defense, Walther, Kel-Tec',
         "guns-rifles.html"),
        ("Ammunition &amp; Accessories",
         'Ammunition (ammo), scopes &amp; optics, red dot sights, holsters, slings, magazines, '
         'gun cases, cleaning kits, <a href="accessories.html">gun safes</a>',
         "accessories.html"),
        ("Pawn &amp; Loans",
         '<a href="pawn-loans.html">0% interest pawn loans</a>, collateral loans, buy &amp; sell, '
         'power tools, electronics, jewelry &amp; gold, fair appraisals, fast cash',
         "pawn-loans.html"),
        ("Licensed Services",
         'Licensed <a href="pawn-loans.html">FFL dealer</a>, $50 FFL transfers, background checks, '
         'firearm consignment, ATF Form 4 &amp; tax stamp guidance',
         "pawn-loans.html"),
        ("Location &amp; Service Area",
         'Ramsey, Minnesota (MN) &middot; Twin Cities &middot; Minneapolis&ndash;St. Paul metro &middot; '
         'Anoka County &middot; serving a 30-mile radius &middot; 6650 US-10, Ramsey, MN 55303',
         "contact.html"),
        ("Compliance &amp; Resources",
         'Minnesota gun laws, <a href="gun-law-checklist.html">2026 gun law checklist</a>, '
         '<a href="gun-license-mn.html">MN gun license</a>, '
         '<a href="rules-for-pawning.html">rules for pawning a gun</a>, '
         '<a href="resources.html">firearm resources</a>',
         "resources.html"),
    ]
    trs = ""
    for cat, terms, href in rows:
        trs += (
            '<tr>'
            '<th scope="row"><a href="%s" class="hover:text-primary-container">%s</a></th>'
            '<td>%s</td>'
            '</tr>' % (href, cat, terms)
        )
    return """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16" aria-labelledby="semantic-heading">
      <div class="text-center mb-8">
        <div class="inline-flex items-center gap-3 font-mono text-[11px] tracking-widest text-primary-container uppercase mb-4">
          <span class="w-8 h-px bg-primary-container inline-block"></span>What We Offer<span class="w-8 h-px bg-primary-container inline-block"></span>
        </div>
        <h2 id="semantic-heading" class="font-headline font-bold text-headline-lg text-on-surface">Guns, Pawn Loans &amp; Firearm Services in Minnesota</h2>
        <p class="mt-4 text-on-surface-variant max-w-3xl mx-auto">A complete look at the firearms, brands, ammunition, and pawn services Twin Cities Pawn &amp; Gun offers throughout Ramsey and the greater Twin Cities metro.</p>
      </div>
      <div class="seo-table-wrap crosshair-card border border-outline-variant/40">
        {xh}
        <table class="seo-table">
          <thead>
            <tr><th scope="col">Category</th><th scope="col">Keywords &amp; Entities</th></tr>
          </thead>
          <tbody>{trs}</tbody>
        </table>
      </div>
    </section>""".format(trs=trs, xh=crosshairs())


def related_links(links):
    """Contextual 'Related pages' interlinking module. links = list of (href, label, desc)."""
    cards = ""
    for href, lbl, desc in links:
        cards += (
            '<a href="%s" class="related-card crosshair-card border border-outline-variant/40 bg-surface-container-low p-5 gold-aura-hover block">'
            '%s'
            '<div class="flex items-center gap-2 font-headline font-bold text-on-surface">%s '
            '<span class="material-symbols-outlined text-primary-container text-base">arrow_outward</span></div>'
            '<p class="text-sm text-on-surface-variant mt-1">%s</p>'
            '</a>' % (href, crosshairs(), lbl, desc)
        )
    return """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14 border-t border-outline-variant/20" aria-label="Related pages">
      <div class="font-mono text-[11px] tracking-widest text-primary-container uppercase mb-6">Related Pages</div>
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">{cards}</div>
    </section>""".format(cards=cards)


def hours_location():
    return """
    <section class="py-16" style="background:#ffffff;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid lg:grid-cols-2 gap-10 items-stretch">
        <div class="crosshair-card overflow-hidden min-h-[340px] gold-glow" style="border:1px solid #e2e8f0" id="map-holder-hours">
          <div class="map-placeholder flex flex-col items-center justify-center h-full min-h-[340px] cursor-pointer select-none" style="background:#f1f5f9" onclick="loadMap('map-holder-hours','https://maps.google.com/maps?q=6650+US-10,+Ramsey,+MN+55303&amp;output=embed')">
            <span class="material-symbols-outlined text-5xl text-primary-container mb-3">location_on</span>
            <p class="font-mono text-sm mb-1" style="color:#111827">6650 US-10, Ramsey, MN 55303</p>
            <p class="text-xs mb-4" style="color:#4b5563">Interactive map loads on click</p>
            <button class="bg-primary-container text-surface-container-lowest font-headline text-xs uppercase px-5 py-2.5 font-bold tracking-wider">Load Map</button>
          </div>
        </div>
        <div>
          {label}
          <h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Hours &amp; Location</h2>
          <address class="not-italic mt-5" style="color:#4b5563">
            <p class="text-lg font-semibold" style="color:#111827">6650 US-10, Ramsey, MN 55303</p>
            <p class="mt-1"><a href="tel:7634274100" class="font-mono text-primary-container hover:underline">(763) 427-4100</a></p>
            <p class="mt-1"><a href="{gmaps}" target="_blank" rel="noopener" class="text-primary-container hover:underline">Get directions &rarr;</a></p>
          </address>
          <table class="mt-6 w-full font-mono text-sm" style="border:1px solid #e2e8f0">
            <tbody>
              <tr style="border-bottom:1px solid #e2e8f0"><td class="py-3 px-4" style="color:#4b5563">Monday &ndash; Friday</td><td class="py-3 px-4 text-right" style="color:#111827">10 AM &ndash; 7 PM</td></tr>
              <tr style="border-bottom:1px solid #e2e8f0"><td class="py-3 px-4" style="color:#4b5563">Saturday</td><td class="py-3 px-4 text-right" style="color:#111827">10 AM &ndash; 5 PM</td></tr>
              <tr><td class="py-3 px-4" style="color:#4b5563">Sunday</td><td class="py-3 px-4 text-right" style="color:#9ca3af">Closed</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>""".format(label=label("Visit The Vault"), gmaps=GMAPS)
