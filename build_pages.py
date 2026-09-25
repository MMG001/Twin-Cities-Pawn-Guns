# -*- coding: utf-8 -*-
"""Page-body functions + write-out logic. Imported/execfile'd after build.py helpers.
This file is concatenated onto build.py by the shell before running."""

import os
from build import *

# ---------- small structural helpers ----------
def grid(cards, cols="sm:grid-cols-2 lg:grid-cols-3"):
    return '<div class="grid grid-cols-1 %s gap-6">%s\n        </div>' % (cols, "".join(cards))


def inv_section(sec_id, label_text, h2, sub, cards_html):
    return """
    <section id="{sid}" data-section="{sid}" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14 scroll-mt-24">
      <div class="mb-8">
        {label}
        <h2 class="font-headline font-bold text-headline-lg text-on-surface">{h2}</h2>
        <p class="mt-2 text-on-surface-variant max-w-2xl">{sub}</p>
      </div>
      {cards}
    </section>""".format(sid=sec_id, label=label(label_text), h2=h2, sub=sub, cards=cards_html)


def filter_bar(chips):
    # chips: list of (filter_value, text)
    btns = ['<button class="filter-chip active" data-filter="all">All</button>']
    for val, txt in chips:
        btns.append('<button class="filter-chip" data-filter="%s">%s</button>' % (val, txt))
    return """
    <div class="sticky top-[68px] z-40 bg-surface-container-lowest/90 backdrop-blur-xl border-b border-outline-variant/30">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-4 flex flex-wrap gap-2">
        %s
      </div>
    </div>""" % "\n        ".join(btns)


def cta_band(title, sub, btn_text, btn_href, external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ""
    return """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 p-10 md:p-14 text-center gold-glow">
        {xh}
        <h2 class="font-headline font-bold text-headline-lg text-on-surface">{title}</h2>
        <p class="mt-3 text-on-surface-variant max-w-2xl mx-auto">{sub}</p>
        <a href="{href}"{tgt} class="inline-flex items-center gap-2 mt-7 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider gold-hover">{btn} <span class="material-symbols-outlined text-base">arrow_outward</span></a>
      </div>
    </section>""".format(xh=crosshairs(), title=title, sub=sub, href=btn_href, tgt=tgt, btn=btn_text)


def brands_section():
    return """
    <section class="py-16" style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        {label_center}
        <h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Brands We Carry</h2>
        <p class="mt-2 max-w-2xl mx-auto" style="color:#4b5563">A rotating selection from the most trusted names in the industry &mdash; inventory changes daily.</p>
        <div class="mt-8 flex flex-wrap justify-center gap-3">
{chips}
        </div>
      </div>
    </section>""".format(label_center=('<div class="flex justify-center">%s</div>' % label("Trusted Manufacturers")), chips=brand_chips_light())


# ================= INDEX =================
def page_index():
    trust = """
    <section class="bg-surface-container-lowest border-b border-outline-variant/30">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid grid-cols-2 md:grid-cols-4 divide-x divide-outline-variant/20">
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">300+</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Firearms In Stock</div></div>
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">0%</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Pawn Loan Rate</div></div>
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">$50</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">FFL Transfers</div></div>
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">2010</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Serving Since</div></div>
      </div>
    </section>"""

    hero = """
    <section class="relative min-h-[70vh] flex items-center blueprint-grid overflow-hidden" aria-label="Homepage hero">
      <img src="images/hero-interior.webp" alt="Interior of Twin Cities Pawn & Gun — hundreds of firearms in stock in Ramsey, MN" class="absolute inset-0 w-full h-full object-cover" fetchpriority="high" />
      <div class="absolute inset-0" style="background:rgba(0,0,0,0.60)"></div>
      <div class="relative max-w-[1360px] mx-auto px-6 lg:px-margin py-24 w-full">
        {label}
        <h1 class="font-headline font-bold text-display-hero-mobile md:text-display-hero text-on-surface">Home of the <span class="text-primary-container">0% Pawn</span></h1>
        <p class="mt-6 text-body-lg text-on-surface-variant max-w-2xl">Ramsey's trusted firearms dealer and pawn shop since 2010. Hundreds of guns, rifles, and shotguns in stock &mdash; plus fair, honest pawn loans at zero percent interest.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <a href="guns-rifles.html" class="inline-flex items-center gap-2 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Browse Inventory <span class="material-symbols-outlined text-base">arrow_outward</span></a>
          <a href="pawn-loans.html" class="inline-flex items-center gap-2 border border-outline-variant/60 text-on-surface font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors">Get a Pawn Loan</a>
        </div>
      </div>
    </section>""".format(label=label("Firearms &middot; Pawn &middot; Loans"))

    cat_cards = """
    <section class="py-16" style="background:#ffffff">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="mb-10">{label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Explore The Vault</h2></div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <a href="guns-rifles.html" class="crosshair-card group relative block overflow-hidden gold-aura-hover" style="border:1px solid #e2e8f0">
            {xh}
            <img src="images/cat-guns-rifles.webp" alt="Guns and rifles for sale at Twin Cities Pawn &amp; Gun in Ramsey, MN" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="p-6" style="background:#ffffff"><h3 class="font-headline font-bold text-headline-sm" style="color:#111827">Guns &amp; Rifles</h3><p class="text-sm mt-2" style="color:#4b5563">Handguns, rifles, shotguns, revolvers, collectibles &amp; NFA items.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Shop firearms <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
          </a>
          <a href="accessories.html" class="crosshair-card group relative block overflow-hidden gold-aura-hover" style="border:1px solid #e2e8f0">
            {xh}
            <img src="images/cat-accessories-ammo.webp" alt="Ammunition and firearm accessories at Twin Cities Pawn &amp; Gun" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="p-6" style="background:#ffffff"><h3 class="font-headline font-bold text-headline-sm" style="color:#111827">Accessories &amp; Ammo</h3><p class="text-sm mt-2" style="color:#4b5563">Ammunition, optics, holsters, magazines, cases &amp; safes.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Shop gear <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
          </a>
          <a href="pawn-loans.html" class="crosshair-card group relative block overflow-hidden gold-aura-hover" style="border:1px solid #e2e8f0">
            {xh}
            <img src="images/cat-pawn-loans.webp" alt="Pawn loans at Twin Cities Pawn &amp; Gun — gun and cash" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="p-6" style="background:#ffffff"><h3 class="font-headline font-bold text-headline-sm" style="color:#111827">Pawn &amp; Loans</h3><p class="text-sm mt-2" style="color:#4b5563">0% pawn loans, tools, electronics, jewelry &amp; gold.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Get a loan <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
          </a>
        </div>
      </div>
    </section>""".format(label=label("Categories"), xh=crosshairs())

    showcase_cards = [
        inv_card("gun-room-rifles.webp", "Rifle room with tactical and hunting rifles", "In Stock", "Tactical &amp; Hunting Rifles", "New &amp; Used", light=True),
        inv_card("1911-pistols.webp", "1911 pistols in display case", "In Stock", "1911 Pistols", "New &amp; Used", light=True),
        inv_card("revolver-showcase.webp", "Revolver showcase display", "In Stock", "Revolvers", "New &amp; Used", light=True),
        inv_card("shotgun-rack.webp", "Rack of shotguns", "In Stock", "Shotguns", "New &amp; Used", light=True),
    ]
    showcase = """
    <section class="py-16" style="background:#f8f9fa;border-top:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="flex flex-wrap items-end justify-between gap-4 mb-10">
          <div>{label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Firearms Showcase</h2></div>
          <a href="guns-rifles.html" class="font-mono text-xs uppercase tracking-wider text-primary-container hover:text-primary-fixed inline-flex items-center gap-2">View all <span class="material-symbols-outlined text-sm">arrow_forward</span></a>
        </div>
        {grid}
      </div>
    </section>""".format(label=label("Featured"), grid=grid(showcase_cards, cols="sm:grid-cols-2 lg:grid-cols-4"))

    gold_cta = """
    <section class="py-14" style="background:#facc15">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        <div class="font-mono text-[11px] tracking-widest uppercase mb-4" style="color:#6c5700">&#9733; Home of the 0% Pawn &#9733;</div>
        <h2 class="font-headline font-bold text-headline-lg" style="color:#131316;line-height:1.1">Ready to Buy, Sell, or Get a Loan?</h2>
        <p class="mt-4 max-w-xl mx-auto" style="color:#3c2f00">Visit our Ramsey store on US-10. Open Monday&ndash;Friday 10AM&ndash;7PM, Saturday 10AM&ndash;5PM. Walk-ins always welcome.</p>
        <div class="mt-8 flex flex-wrap gap-4 justify-center">
          <a href="contact.html" class="inline-flex items-center gap-2 font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider" style="background:#131316;color:#facc15">Visit Our Store <span class="material-symbols-outlined text-base" style="color:#facc15">arrow_outward</span></a>
          <a href="tel:7634274100" class="inline-flex items-center gap-2 font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider" style="border:2px solid #131316;color:#131316">(763) 427-4100</a>
        </div>
      </div>
    </section>"""

    schema = ('{\n'
              '  "@context": "https://schema.org",\n'
              '  "@type": "PawnShop",\n'
              '  "name": "Twin Cities Pawn & Gun",\n'
              '  "image": "%s/images/og-image.jpg",\n'
              '  "@id": "%s",\n'
              '  "url": "%s",\n'
              '  "telephone": "+1-763-427-4100",\n'
              '  "priceRange": "$$",\n'
              '  "address": {\n'
              '    "@type": "PostalAddress",\n'
              '    "streetAddress": "6650 US-10",\n'
              '    "addressLocality": "Ramsey",\n'
              '    "addressRegion": "MN",\n'
              '    "postalCode": "55303",\n'
              '    "addressCountry": "US"\n'
              '  },\n'
              '  "geo": {"@type": "GeoCoordinates", "latitude": 45.2619, "longitude": -93.4499},\n'
              '  "openingHoursSpecification": [\n'
              '    {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "10:00", "closes": "19:00"},\n'
              '    {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "17:00"}\n'
              '  ],\n'
              '  "sameAs": ["%s", "%s"]\n'
              '}') % (BASE_URL, BASE_URL, BASE_URL, ARMSLIST, GUNBROKER)

    body = (nav() + ticker() + hero + trust + cat_cards + showcase + gold_cta +
            online_cta() + hours_location() + footer())
    return head(
        "Twin Cities Pawn & Gun | Firearms & Pawn Loans, Ramsey MN",
        "Home of the 0% Pawn in Ramsey, MN. Hundreds of guns, rifles & accessories in stock. Licensed FFL dealer \u2014 $50 transfers & 0% pawn loans since 2010.",
        "index.html",
        "pawn shop Ramsey MN, gun store Ramsey, firearms dealer Minnesota, 0% pawn loans, FFL transfer, buy guns Ramsey, Twin Cities Pawn",
        schema=schema) + body


# ================= ABOUT =================
def page_about():
    story = """
    <section class="py-16" style="background:#ffffff">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid lg:grid-cols-2 gap-12 items-center">
        <div class="relative crosshair-card gold-glow" style="border:1px solid #e2e8f0">
          {xh}
          <img src="images/storefront-exterior.webp" alt="Twin Cities Pawn &amp; Gun storefront exterior in Ramsey, MN" class="w-full h-[420px] object-cover" />
        </div>
        <div>
          {label}
          <h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Ramsey's Trusted Pawn &amp; Gun Shop</h2>
          <div class="mt-5 space-y-4" style="color:#4b5563">
            <p>Twin Cities Pawn &amp; Gun has proudly served the Minneapolis&ndash;St. Paul metro area since 2010. What started as a local pawn shop has grown into one of the region's most trusted destinations for firearms, ammunition, and fair pawn loans.</p>
            <p>We're a fully licensed FFL dealer with hundreds of handguns, rifles, and shotguns in stock at any given time. Whether you're a first-time buyer, a seasoned collector, or you simply need a short-term loan, our knowledgeable staff treats every customer with honesty and respect.</p>
            <p>We're best known as the <span class="text-primary-container font-semibold">Home of the 0% Pawn</span> &mdash; because we believe in giving our neighbors a fair deal. Stop by our Ramsey location on US-10 and see the difference for yourself.</p>
          </div>
          <a href="contact.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Visit Us <span class="material-symbols-outlined text-base">arrow_outward</span></a>
        </div>
      </div>
    </section>""".format(xh=crosshairs(), label=label("Our Story"))

    stats = """
    <section class="bg-surface-container-lowest border-y border-outline-variant/30">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid grid-cols-2 md:grid-cols-4 divide-x divide-outline-variant/20">
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">15+</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Years In Business</div></div>
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">300+</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Firearms In Stock</div></div>
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">0%</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Pawn Loan Interest</div></div>
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">100%</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Licensed &amp; Legal</div></div>
      </div>
    </section>"""

    reasons = [
        ("verified", "Licensed FFL Dealer", "Fully licensed and compliant with all federal, state, and local firearms laws. Every transaction is handled by the book."),
        ("payments", "Home of the 0% Pawn", "We offer pawn loans at zero percent interest &mdash; a genuinely fair deal you won't find anywhere else."),
        ("diversity_3", "Huge Selection", "Hundreds of firearms plus tools, electronics, jewelry, and more. Our inventory changes daily."),
        ("handshake", "Honest &amp; Fair", "Straightforward pricing and respectful service for buyers, sellers, and borrowers alike."),
        ("swap_horiz", "$50 FFL Transfers", "Buying online? We handle incoming FFL transfers for a flat $50 fee."),
        ("storefront", "Local &amp; Trusted", "A Ramsey fixture since 2010, proudly serving the Twin Cities community."),
    ]
    reason_cards = []
    for icon, t, d in reasons:
        reason_cards.append("""
        <div class="crosshair-card relative p-7 gold-aura-hover" style="border:1px solid #e2e8f0;background:#ffffff">
          {xh}
          <span class="material-symbols-outlined text-primary-container text-3xl">{icon}</span>
          <h3 class="font-headline font-bold text-headline-sm mt-4" style="color:#111827">{t}</h3>
          <p class="text-sm mt-2" style="color:#4b5563">{d}</p>
        </div>""".format(xh=crosshairs(), icon=icon, t=t, d=d))
    why = """
    <section class="py-16" style="background:#f8f9fa;border-top:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="mb-10">{label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Why Choose Us</h2></div>
        {grid}
      </div>
    </section>""".format(label=label("The Difference"), grid=grid(reason_cards))

    body = (nav() + ticker() +
            page_hero("about-hero-rifles.webp", "Rifles with price tags on display at Twin Cities Pawn & Gun", "About Us", "About Twin Cities Pawn &amp; Gun", "Serving Ramsey and the Twin Cities with honest firearms sales and fair pawn loans since 2010.") +
            story + stats + why + brands_section() + keyword_entity_table() + footer())
    return head(
        "About Us | Twin Cities Pawn & Gun \u2014 Ramsey, MN Since 2010",
        "Learn about Twin Cities Pawn & Gun, Ramsey Minnesota's trusted licensed FFL firearms dealer and pawn shop since 2010. Home of the 0% Pawn.",
        "about.html",
        "about Twin Cities Pawn, gun store history Ramsey MN, licensed FFL dealer Minnesota, trusted pawn shop",
        ) + body


# ================= GUNS & RIFLES =================
def page_guns():
    chips = filter_bar([
        ("handguns", "Handguns"), ("revolvers", "Revolvers"), ("rifles", "Rifles"),
        ("shotguns", "Shotguns"), ("archery", "Archery"), ("collectible", "Collectible"), ("nfa", "NFA"),
    ])

    handguns = inv_section("handguns", "Pistols &amp; Semi-Autos", "Handguns &amp; Pistols",
        "From everyday carry to full-size duty pistols &mdash; Glock, Sig Sauer, Smith &amp; Wesson, Springfield and more.",
        grid([
            inv_card("firearms-handguns-rifles.webp", "Handguns and pistols in glass display case", "In Stock", "Semi-Auto Pistols", "New &amp; Used"),
            inv_card("1911-pistols.webp", "1911 pistols on display", "In Stock", "1911 Pistols", "New &amp; Used"),
            inv_card("handgun-case-display.webp", "Handgun case display", "In Stock", "Concealed Carry Pistols", "New &amp; Used"),
            inv_card("pistol-glass-case.webp", "Pistols in glass case", "In Stock", "Duty &amp; Range Pistols", "New &amp; Used"),
        ]))

    revolvers = inv_section("revolvers", "Wheelguns", "Revolvers",
        "Classic and modern revolvers from Smith &amp; Wesson, Ruger, Colt, Taurus and more.",
        grid([
            inv_card("revolver-showcase.webp", "Revolver showcase display case", "In Stock", "Double-Action Revolvers", "New &amp; Used"),
            inv_card("handgun-case-display.webp", "Handgun and revolver display", "In Stock", "Concealed Carry Revolvers", "New &amp; Used"),
            inv_card("pistol-glass-case.webp", "Revolvers in glass case", "In Stock", "Magnum Revolvers", "New &amp; Used"),
        ]))

    rifles = inv_section("rifles", "Hunting &amp; Tactical", "Hunting &amp; Tactical Rifles",
        "AR-platform rifles, bolt-action hunting rifles, and everything in between from Ruger, Daniel Defense, Remington and more.",
        grid([
            inv_card("gun-room-rifles.webp", "Rifle room with hunting and tactical rifles", "In Stock", "AR-Platform Rifles", "New &amp; Used"),
            inv_card("rifle-wall.webp", "Wall of rifles", "In Stock", "Bolt-Action Hunting Rifles", "New &amp; Used"),
            inv_card("glock-wall-rifles.webp", "Rifles and pistols wall display", "In Stock", "Modern Sporting Rifles", "New &amp; Used"),
        ]))

    shotguns = inv_section("shotguns", "Field &amp; Home Defense", "Shotguns",
        "Pump-action, semi-auto, and over/under shotguns from Mossberg, Remington, Browning and more.",
        grid([
            inv_card("shotgun-rack.webp", "Rack of shotguns", "In Stock", "Pump-Action Shotguns", "New &amp; Used"),
            inv_card("glock-shotgun-wall.webp", "Shotgun wall display", "In Stock", "Semi-Auto &amp; Home Defense", "New &amp; Used"),
        ]))

    archery = """
    <section id="archery" data-section="archery" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14 scroll-mt-24">
      <div class="mb-8">{label}<h2 class="font-headline font-bold text-headline-lg text-on-surface">Archery</h2>
        <p class="mt-2 text-on-surface-variant max-w-2xl">Compound bows and archery gear for hunters and target shooters. Selection varies &mdash; call to check current stock.</p></div>
      <div class="grid md:grid-cols-2 gap-6 items-center">
        <div class="crosshair-card relative border border-outline-variant/40 gold-glow archery-frame">
          {xh}
          <img src="images/archery-compound-bows.webp" alt="Compound bows available at Twin Cities Pawn & Gun" />
        </div>
        <div>
          <h3 class="font-headline font-bold text-headline-sm text-on-surface">Compound Bows &amp; Gear</h3>
          <p class="mt-3 text-on-surface-variant">We regularly stock compound bows and archery accessories. Whether you're gearing up for bow season or just getting started, stop in to see what's available.</p>
          <a href="contact.html" class="inline-flex items-center gap-2 mt-6 border border-outline-variant/60 text-on-surface font-headline text-xs uppercase px-6 py-3 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors">Check Availability <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
        </div>
      </div>
    </section>""".format(label=label("Bows &amp; Gear"), xh=crosshairs())

    collectible = inv_section("collectible", "Curios &amp; Relics", "Collectible Firearms",
        "Vintage, surplus, and collectible firearms for the discerning enthusiast. Ask our staff about current C&amp;R inventory.",
        grid([
            inv_card("1911-pistols.webp", "Collectible 1911 pistols", "Consignment", "Vintage Pistols", "Collectible"),
            inv_card("rifle-wall.webp", "Collectible rifles on wall", "Consignment", "Surplus &amp; Milsurp Rifles", "Collectible"),
            inv_card("revolver-showcase.webp", "Collectible revolvers", "Consignment", "Classic Revolvers", "Collectible"),
        ]))

    nfa = """
    <section id="nfa" data-section="nfa" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14 scroll-mt-24">
      <div class="mb-8">{label}<h2 class="font-headline font-bold text-headline-lg text-on-surface">NFA Items</h2>
        <p class="mt-2 text-on-surface-variant max-w-2xl">Suppressors, SBRs, and other NFA-regulated items. All NFA transactions require ATF approval and applicable tax stamps &mdash; our staff will walk you through the process.</p></div>
      <div class="crosshair-card relative border border-outline-variant/40 bg-surface-container-low p-8 md:p-10 gold-glow">
        {xh}
        <div class="grid md:grid-cols-3 gap-6">
          <div><span class="material-symbols-outlined text-primary-container text-3xl">graphic_eq</span><h3 class="font-headline font-bold text-headline-sm mt-3 text-on-surface">Suppressors</h3><p class="text-sm text-on-surface-variant mt-2">A growing selection of suppressors for rifle and pistol calibers.</p></div>
          <div><span class="material-symbols-outlined text-primary-container text-3xl">straighten</span><h3 class="font-headline font-bold text-headline-sm mt-3 text-on-surface">SBRs &amp; SBS</h3><p class="text-sm text-on-surface-variant mt-2">Short-barreled rifles and shotguns available with proper paperwork.</p></div>
          <div><span class="material-symbols-outlined text-primary-container text-3xl">description</span><h3 class="font-headline font-bold text-headline-sm mt-3 text-on-surface">Tax Stamp Help</h3><p class="text-sm text-on-surface-variant mt-2">We guide you through Form 4, trusts, and the ATF approval process.</p></div>
        </div>
        <a href="contact.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-xs uppercase px-6 py-3 font-bold tracking-wider gold-hover">Ask About NFA <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
      </div>
    </section>""".format(label=label("Class III"), xh=crosshairs())

    body = (nav() + ticker() +
            page_hero("guns-rifles-hero.webp", "Winchester ammunition box with classic shotgun and rifle", "Firearms Inventory", "Guns &amp; Rifles", "Hundreds of handguns, rifles, shotguns, revolvers and more in stock. Inventory changes daily &mdash; shop online or visit us in Ramsey.") +
            chips + handguns + revolvers + rifles + shotguns + archery + collectible + nfa +
            online_cta() + cta_band("Can't Find What You're Looking For?", "Our inventory turns over fast and much of it never makes it online. Call us or stop by &mdash; we'll help you find the right firearm.", "Contact Us", "contact.html") +
            related_links([
                ("accessories.html", "Ammo &amp; Accessories", "Ammunition, optics, holsters, magazines and gun safes."),
                ("pawn-loans.html", "FFL Transfers ($50)", "Buy online? Ship it to us for a fast, licensed FFL transfer."),
                ("gun-license-mn.html", "MN Gun License", "What you need to legally buy a firearm in Minnesota."),
            ]) + footer())
    return head(
        "Guns & Rifles for Sale | Twin Cities Pawn & Gun \u2014 Ramsey, MN",
        "Shop handguns, rifles, shotguns, revolvers, collectible & NFA firearms at Twin Cities Pawn & Gun in Ramsey, MN. Licensed FFL dealer with 300+ guns in stock.",
        "guns-rifles.html",
        "guns for sale Ramsey MN, rifles for sale Minnesota, handguns Ramsey, shotguns, buy firearms, FFL dealer, NFA items, suppressors Minnesota",
        ) + body


# ================= ACCESSORIES =================
def page_accessories():
    chips = filter_bar([
        ("ammo", "Ammunition"), ("optics", "Optics"), ("holsters", "Holsters"), ("magazines", "Magazines &amp; Safes"),
    ])

    ammo = inv_section("ammo", "Rounds &amp; Calibers", "Ammunition &amp; Ammo",
        "Handgun, rifle, and shotgun ammunition in popular calibers. Stock and pricing change frequently &mdash; call for current availability.",
        grid([
            inv_card("https://www.berrysmfg.com/wp-content/uploads/2026/02/Safari-Trio-scaled.jpg", "Boxes of ammunition", "In Stock", "Handgun &amp; Rifle Ammo", "New", cdn=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    optics = inv_section("optics", "Glass &amp; Electronics", "Sights, Scopes &amp; Optics",
        "Red dots, rifle scopes, thermal and night vision optics to complete your build.",
        grid([
            inv_card("https://infitacusa.com/cdn/shop/articles/IOP13_ImagesDSC05691.jpg?v=1776079529&width=1500", "Thermal optic scope", "In Stock", "Thermal &amp; Night Vision", "New &amp; Used", cdn=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    holsters = inv_section("holsters", "Carry &amp; Storage", "Holsters, Slings &amp; Cases",
        "Concealed carry holsters, rifle slings, and protective cases for transport and storage.",
        grid([
            inv_card("https://formsv2.soundestlink.com/images/1400/6a85cba1c5aa8a2a0175784a", "Concealed carry holster", "In Stock", "Holsters &amp; Slings", "New", cdn=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    magazines = inv_section("magazines", "Feed &amp; Secure", "Magazines &amp; Safes",
        "Factory and aftermarket magazines, plus gun safes and lockboxes to keep your firearms secure.",
        grid([
            inv_card("firearms-handguns-rifles.webp", "Magazines and firearm accessories", "In Stock", "Pistol &amp; Rifle Magazines", "New &amp; Used"),
            inv_card("handgun-case-display.webp", "Gun cases and storage", "In Stock", "Safes &amp; Lockboxes", "New &amp; Used"),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    body = (nav() + ticker() +
            page_hero("accessories-hero.webp", "Leupold rifle scope mounted on precision firearm", "Gear &amp; Accessories", "Accessories &amp; Ammo", "Ammunition, optics, holsters, magazines, safes and more &mdash; everything you need to run and maintain your firearms.") +
            chips + ammo + optics + holsters + magazines +
            cta_band("Need Something Specific?", "We stock far more than we can list online. Give us a call and we'll let you know what's in stock or help you order it.", "Contact Us", "contact.html") +
            online_cta() +
            related_links([
                ("guns-rifles.html", "Guns &amp; Rifles", "300+ handguns, rifles and shotguns in stock in Ramsey, MN."),
                ("pawn-loans.html", "Pawn &amp; Loans", "0% interest pawn loans on firearms, tools and more."),
                ("contact.html", "Visit The Store", "6650 US-10, Ramsey, MN &mdash; hours, map and directions."),
            ]) + footer())
    return head(
        "Ammo & Firearm Accessories | Twin Cities Pawn, Ramsey MN",
        "Ammunition, optics, holsters, magazines, and gun safes at Twin Cities Pawn & Gun in Ramsey, MN. Everything you need for your firearms in one place.",
        "accessories.html",
        "ammunition Ramsey MN, ammo for sale Minnesota, rifle scopes, holsters, magazines, gun safes, firearm accessories Ramsey",
        ) + body


# ================= PAWN & LOANS =================
def page_pawn():
    featured = """
    <section id="loans" data-section="loans" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 scroll-mt-24">
      <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 overflow-hidden gold-glow grid lg:grid-cols-2">
        {xh}
        <div class="p-10 md:p-14">
          {label}
          <h2 class="font-headline font-bold text-headline-xl-mobile md:text-headline-xl text-on-surface">0% Pawn Loans</h2>
          <p class="mt-4 text-on-surface-variant">We're the <span class="text-primary-container font-semibold">Home of the 0% Pawn</span> &mdash; get a fair, short-term loan against items of value with zero percent interest. No credit checks, no hassle, and your items are held securely.</p>
          <ul class="mt-6 space-y-3 text-on-surface-variant">
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Loans on firearms, tools, electronics, jewelry &amp; more</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>No credit check &mdash; your item is the collateral</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Fair valuations and flexible terms</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Reclaim your item when you repay</li>
          </ul>
          <a href="contact.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Get a Loan Quote <span class="material-symbols-outlined text-base">arrow_outward</span></a>
        </div>
        <div class="relative min-h-[320px]">
          <img src="images/pawn-counter-guitars.webp" alt="Pawn counter at Twin Cities Pawn & Gun" class="absolute inset-0 w-full h-full object-cover" />
        </div>
      </div>
    </section>""".format(xh=crosshairs(), label=label("Home of the 0% Pawn"))

    ffl = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin pb-4">
      <div class="crosshair-card relative border border-outline-variant/40 bg-surface-container-low p-8 md:p-10 gold-aura-hover grid md:grid-cols-[auto_1fr_auto] gap-6 items-center">
        {xh}
        <span class="material-symbols-outlined text-primary-container text-5xl">swap_horiz</span>
        <div>
          <h3 class="font-headline font-bold text-headline-sm text-on-surface">$50 FFL Transfers</h3>
          <p class="text-sm text-on-surface-variant mt-2 max-w-2xl">Bought a firearm online? We handle incoming FFL transfers for a flat <span class="font-mono text-primary-container">$50</span> fee. Have it shipped to us and we'll take care of the paperwork and background check.</p>
        </div>
        <a href="contact.html" class="inline-flex items-center gap-2 border border-outline-variant/60 text-on-surface font-headline text-xs uppercase px-6 py-3 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors whitespace-nowrap">Start a Transfer <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
      </div>
    </section>""".format(xh=crosshairs())

    tools = inv_section("tools", "Buy &amp; Pawn", "Power Tools",
        "We buy, sell, and loan on quality power tools &mdash; drills, saws, and more from trusted brands.",
        grid([
            inv_card("tools-power-tools.webp", "Power tools available at pawn shop", "In Stock", "Power Tools", "Used"),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    electronics = inv_section("electronics", "Buy &amp; Pawn", "Electronics",
        "Laptops, game consoles, audio gear and more. Selection rotates constantly &mdash; stop in to see what's available.",
        grid([
            inv_card("tools-electronics.webp", "Electronics for sale at pawn shop", "In Stock", "Electronics", "Used"),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    jewelry = inv_section("jewelry", "Buy &amp; Pawn", "Jewelry &amp; Gold",
        "Gold, diamonds, and fine jewelry. We offer fair valuations for buying, selling, and pawn loans.",
        grid([
            inv_card("https://parkerpawn.com/wp-content/uploads/2023/04/gold-jewelry-diamond-shop-with-rings-necklaces-luxury-retail-store-window-display-showcase-1024x768.jpg", "Gold and diamond jewelry display", "In Stock", "Fine Jewelry", "New &amp; Used", cdn=True),
            inv_card("https://www.pauldingpawnshop.com/wp-content/uploads/2022/05/gold-jewelry-rings-2022-02-28-20-56-06-utc-scaled.jpg", "Gold rings", "In Stock", "Gold &amp; Rings", "New &amp; Used", cdn=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    body = (nav() + ticker() +
            page_hero("tools-power-tools.webp", "Pawn shop merchandise at Twin Cities Pawn & Gun", "Pawn &amp; Loans", "Pawn &amp; Loans", "Home of the 0% Pawn. Fair loans, honest valuations, and a rotating selection of tools, electronics, jewelry and more.") +
            featured + ffl + tools + electronics + jewelry +
            cta_band("Have Something to Pawn or Sell?", "Bring it in for a free, no-obligation valuation. We loan on and buy firearms, tools, electronics, jewelry, and more.", "Get a Quote", "contact.html") +
            related_links([
                ("rules-for-pawning.html", "Rules for Pawning a Gun", "Minnesota pawn laws, ID requirements and hold periods."),
                ("guns-rifles.html", "Shop Firearms", "Browse 300+ guns, rifles and shotguns in stock."),
                ("faq-gun-pawns.html", "Gun Pawn FAQ", "Answers to common questions about pawning firearms."),
            ]) +
            hours_location() + footer())
    return head(
        "0% Pawn Loans & FFL Transfers | Twin Cities Pawn & Gun, MN",
        "Home of the 0% Pawn. Get fair pawn loans with zero interest at Twin Cities Pawn & Gun in Ramsey, MN. $50 FFL transfers, plus tools, electronics & jewelry.",
        "pawn-loans.html",
        "0% pawn loans Ramsey MN, pawn shop loans Minnesota, FFL transfer $50, sell jewelry Ramsey, pawn tools electronics, gold buyer Ramsey",
        ) + body


# ================= CONTACT =================
def page_contact():
    form = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 grid lg:grid-cols-2 gap-12">
      <div>
        {label}
        <h2 class="font-headline font-bold text-headline-lg text-on-surface">Send Us a Message</h2>
        <p class="mt-2 text-on-surface-variant">Questions about inventory, pawn loans, or FFL transfers? Fill out the form and we'll get back to you. For fastest service, give us a call.</p>
        <!-- Replace REPLACE_WITH_YOUR_ID with your Formspree form ID (https://formspree.io) -->
        <form action="https://formspree.io/f/REPLACE_WITH_YOUR_ID" method="POST" class="mt-8 space-y-5">
          <div class="grid sm:grid-cols-2 gap-5">
            <div>
              <label for="name" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Name</label>
              <input type="text" id="name" name="name" required class="w-full bg-surface-container-low border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors" />
            </div>
            <div>
              <label for="phone" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Phone</label>
              <input type="tel" id="phone" name="phone" class="w-full bg-surface-container-low border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors" />
            </div>
          </div>
          <div>
            <label for="email" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Email</label>
            <input type="email" id="email" name="email" required class="w-full bg-surface-container-low border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors" />
          </div>
          <div>
            <label for="subject" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Subject</label>
            <select id="subject" name="subject" class="w-full bg-surface-container-low border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors">
              <option>General Inquiry</option>
              <option>Firearm Availability</option>
              <option>Pawn Loan</option>
              <option>FFL Transfer</option>
              <option>Sell an Item</option>
            </select>
          </div>
          <div>
            <label for="message" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Message</label>
            <textarea id="message" name="message" rows="5" required class="w-full bg-surface-container-low border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors"></textarea>
          </div>
          <button type="submit" class="inline-flex items-center gap-2 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider gold-hover">Send Message <span class="material-symbols-outlined text-base">send</span></button>
        </form>
      </div>
      <div class="space-y-6">
        <div class="crosshair-card relative border border-outline-variant/40 bg-surface-container-low p-7 gold-aura-hover">
          {xh}
          <h3 class="font-headline font-bold text-headline-sm text-on-surface">Visit Our Store</h3>
          <address class="not-italic mt-4 space-y-3 text-on-surface-variant text-sm">
            <p class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">location_on</span>6650 US-10, Ramsey, MN 55303</p>
            <p class="flex items-center gap-3"><span class="material-symbols-outlined text-primary-container text-lg">call</span><a href="tel:7634274100" class="font-mono text-primary-container hover:underline">(763) 427-4100</a></p>
            <p class="flex items-center gap-3"><span class="material-symbols-outlined text-primary-container text-lg">directions</span><a href="{gmaps}" target="_blank" rel="noopener" class="text-primary-container hover:underline">Get directions &rarr;</a></p>
          </address>
          <div class="mt-5 border-t border-outline-variant/20 pt-4 font-mono text-sm text-on-surface-variant space-y-1">
            <div class="flex justify-between"><span>Mon &ndash; Fri</span><span class="text-on-surface">10 AM &ndash; 7 PM</span></div>
            <div class="flex justify-between"><span>Saturday</span><span class="text-on-surface">10 AM &ndash; 5 PM</span></div>
            <div class="flex justify-between"><span>Sunday</span><span class="text-outline">Closed</span></div>
          </div>
        </div>
        <div class="crosshair-card border border-outline-variant/40 overflow-hidden gold-glow h-[300px]" id="map-holder-contact">
          <div class="map-placeholder flex flex-col items-center justify-center h-full min-h-[300px] bg-surface-container-lowest cursor-pointer select-none" onclick="loadMap('map-holder-contact','https://maps.google.com/maps?q=6650+US-10,+Ramsey,+MN+55303&amp;output=embed')">
            <span class="material-symbols-outlined text-5xl text-primary-container mb-3">location_on</span>
            <p class="font-mono text-sm text-on-surface mb-1">6650 US-10, Ramsey, MN 55303</p>
            <p class="text-xs text-on-surface-variant mb-4">Interactive map loads on click</p>
            <button class="bg-primary-container text-surface-container-lowest font-headline text-xs uppercase px-5 py-2.5 font-bold tracking-wider">Load Map</button>
          </div>
        </div>
      </div>
    </section>""".format(label=label("Get In Touch"), xh=crosshairs(), gmaps=GMAPS)

    body = (nav() + ticker() +
            page_hero("contact-hero.webp", "Handguns with yellow price tags on display counter", "Contact", "Contact Us", "Stop by, call, or send us a message. We're here to help with firearms, pawn loans, and FFL transfers.") +
            form + online_cta() + footer())
    return head(
        "Contact Us | Twin Cities Pawn & Gun \u2014 Ramsey, MN | (763) 427-4100",
        "Contact Twin Cities Pawn & Gun in Ramsey, MN. Visit us at 6650 US-10, call (763) 427-4100, or send a message. Open Mon\u2013Fri 10\u20137, Sat 10\u20135.",
        "contact.html",
        "contact Twin Cities Pawn, gun store Ramsey MN phone, pawn shop directions Ramsey, 6650 US-10, firearms dealer contact Minnesota",
        ) + body


# ================= LEGAL / MINIMAL PAGES =================
def legal_page(canon, title, meta_desc, keywords, label_text, h1, sub, content_html):
    body = (nav() + ticker() +
            text_hero(label_text, h1, sub) +
            """
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="prose-legal space-y-6 text-on-surface-variant">
        {content}
      </div>
    </section>""".format(content=content_html) +
            footer())
    return head(title, meta_desc, canon, keywords) + body


def info_page(canon, title, meta_desc, keywords, hero_img, hero_alt, label_text, h1, sub, content_html):
    """Info page with image hero (for guides with photos)"""
    body = (nav() + ticker() +
            page_hero(hero_img, hero_alt, label_text, h1, sub) +
            """
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="prose-legal space-y-6 text-on-surface-variant">
        {content}
      </div>
    </section>""".format(content=content_html) +
            footer())
    return head(title, meta_desc, canon, keywords) + body


def h3(t):
    return '<h2 class="font-headline font-bold text-headline-sm text-on-surface mt-8 mb-2">%s</h2>' % t


def p(t):
    return '<p>%s</p>' % t


def page_terms():
    c = "".join([
        p("Welcome to Twin Cities Pawn &amp; Gun. By accessing or using our website and services, you agree to the following terms and conditions. Please read them carefully."),
        h3("1. Firearms Sales &amp; Compliance"),
        p("All firearm sales and transfers comply with federal, state, and local laws. A valid government-issued photo ID and a successful background check are required for all firearm purchases and transfers. We reserve the right to refuse any sale or transfer at our discretion, as permitted by law."),
        h3("2. FFL Transfers"),
        p("Incoming FFL transfers are handled for a flat $50 fee per firearm. The buyer is responsible for ensuring the firearm is legal to own in their jurisdiction. All standard background check and identification requirements apply."),
        h3("3. Pawn Loans"),
        p("Pawn loans are subject to a written pawn agreement provided at the time of the transaction. Items are held as collateral and may be reclaimed upon repayment within the agreed term. Failure to repay within the term may result in forfeiture of the pledged item."),
        h3("4. Inventory &amp; Pricing"),
        p("Inventory and pricing are subject to change without notice. Items shown online or in-store may sell quickly and availability is not guaranteed. Photographs are for illustration and may not depict the exact item in stock."),
        h3("5. Limitation of Liability"),
        p("Twin Cities Pawn &amp; Gun is not liable for any indirect, incidental, or consequential damages arising from the use of our website or services, to the fullest extent permitted by law."),
        h3("6. Changes to These Terms"),
        p("We may update these terms from time to time. Continued use of our website constitutes acceptance of any changes."),
        h3("Contact"),
        p('Questions about these terms? Contact us at <a href="tel:7634274100" class="text-primary-container hover:underline">(763) 427-4100</a> or visit us at 6650 US-10, Ramsey, MN 55303.'),
    ])
    return legal_page("terms.html", "Terms & Conditions | Twin Cities Pawn & Gun",
        "Terms and conditions for Twin Cities Pawn & Gun in Ramsey, MN, including firearms sales compliance, FFL transfers, and pawn loan policies.",
        "terms and conditions, Twin Cities Pawn policies, firearms sale terms, pawn loan terms",
        "Legal", "Terms &amp; Conditions", "Last updated 2026. Please review these terms governing the use of our website and services.", c)


def page_privacy():
    c = "".join([
        p("Twin Cities Pawn &amp; Gun respects your privacy. This policy explains what information we collect and how we use it."),
        h3("Information We Collect"),
        p("We collect information you provide directly, such as your name, phone number, email, and message when you use our contact form. In-store transactions require identification as mandated by law for firearms and pawn transactions."),
        h3("How We Use Your Information"),
        p("We use your information to respond to inquiries, process transactions, comply with legal requirements, and improve our services. We do not sell your personal information to third parties."),
        h3("Legal Compliance"),
        p("As a licensed FFL dealer and pawn shop, we are required to collect and retain certain records for firearm and pawn transactions in accordance with federal, state, and local law. These records are handled in compliance with applicable regulations."),
        h3("Website &amp; Cookies"),
        p("Our website may use standard analytics and cookies to understand traffic and improve the user experience. You can disable cookies in your browser settings."),
        h3("Data Security"),
        p("We take reasonable measures to protect your information. However, no method of transmission over the internet is completely secure."),
        h3("Contact"),
        p('For privacy questions, contact us at <a href="tel:7634274100" class="text-primary-container hover:underline">(763) 427-4100</a> or 6650 US-10, Ramsey, MN 55303.'),
    ])
    return legal_page("privacy.html", "Privacy Policy | Twin Cities Pawn & Gun",
        "Privacy policy for Twin Cities Pawn & Gun in Ramsey, MN. Learn what information we collect and how we protect it.",
        "privacy policy, Twin Cities Pawn privacy, data protection pawn shop",
        "Legal", "Privacy Policy", "How we collect, use, and protect your information.", c)


def page_equal():
    c = "".join([
        p("Twin Cities Pawn &amp; Gun is an Equal Opportunity Employer. We are committed to providing a workplace free of discrimination and harassment."),
        p("We do not discriminate on the basis of race, color, religion, sex, sexual orientation, gender identity, national origin, age, disability, veteran status, genetic information, or any other characteristic protected by federal, state, or local law."),
        h3("Our Commitment"),
        p("All employment decisions &mdash; including hiring, promotion, compensation, and termination &mdash; are based on merit, qualifications, and business needs. We are committed to fostering an inclusive environment where every team member is treated with dignity and respect."),
        h3("Employment Inquiries"),
        p('Interested in joining our team? Stop by 6650 US-10, Ramsey, MN 55303, or call <a href="tel:7634274100" class="text-primary-container hover:underline">(763) 427-4100</a>.'),
    ])
    return legal_page("equal-opportunity.html", "Equal Opportunity Employer | Twin Cities Pawn & Gun",
        "Twin Cities Pawn & Gun is an Equal Opportunity Employer committed to a workplace free of discrimination.",
        "equal opportunity employer, Twin Cities Pawn careers, non-discrimination policy",
        "Careers", "Equal Opportunity Employer", "Our commitment to a fair and inclusive workplace.", c)


def page_faq():
    faqs = [
        ("Do you offer 0% pawn loans?", "Yes! We're proudly known as the Home of the 0% Pawn. We offer fair, short-term loans at zero percent interest against items of value including firearms, tools, electronics, and jewelry."),
        ("How much do FFL transfers cost?", "We handle incoming FFL transfers for a flat $50 fee per firearm. Have your online purchase shipped to us and we'll take care of the paperwork and background check."),
        ("What do I need to buy a firearm?", "You'll need a valid government-issued photo ID and must pass a background check. All sales comply with federal, state, and local laws. Certain items may have additional requirements."),
        ("What are your hours?", "We're open Monday through Friday from 10 AM to 7 PM, Saturday from 10 AM to 5 PM, and closed on Sunday."),
        ("Where are you located?", "We're at 6650 US-10, Ramsey, MN 55303, conveniently serving the Minneapolis\u2013St. Paul metro area."),
        ("Can I see your inventory online?", "Yes &mdash; browse our listings on Armslist and GunBroker via the links on our site. Note that much of our inventory is in-store only and turns over quickly, so call us to check availability."),
        ("Do you buy items?", "Absolutely. We buy firearms, tools, electronics, jewelry, and more. Bring your item in for a free, no-obligation valuation."),
        ("Do you handle NFA items like suppressors?", "Yes. We carry suppressors, SBRs, and other NFA items. Our staff will guide you through the ATF Form 4, trust, and tax stamp process."),
    ]
    items = []
    for q, a in faqs:
        items.append("""
        <div class="faq-item border border-outline-variant/40 bg-surface-container-low">
          <button class="faq-head w-full flex justify-between items-center gap-4 text-left px-6 py-5">
            <span class="font-headline font-semibold text-on-surface">{q}</span>
            <span class="material-symbols-outlined text-primary-container faq-icon">add</span>
          </button>
          <div class="faq-body px-6 text-on-surface-variant"><p class="pb-5">{a}</p></div>
        </div>""".format(q=q, a=a))
    content = """
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="space-y-4">{items}</div>
    </section>""".format(items="".join(items))
    body = (nav() + ticker() +
            text_hero("Help Center", "Frequently Asked Questions", "Answers to common questions about our firearms, pawn loans, transfers, and store.") +
            content +
            cta_band("Still Have Questions?", "We're happy to help. Give us a call or stop by the store and our team will get you sorted.", "Contact Us", "contact.html") +
            footer())
    return head("FAQ | Twin Cities Pawn & Gun \u2014 Ramsey, MN",
        "Frequently asked questions about Twin Cities Pawn & Gun: 0% pawn loans, FFL transfers, buying firearms, hours, location, and more.",
        "faq.html",
        "pawn shop FAQ, FFL transfer questions, buy gun requirements Minnesota, 0% pawn loan questions, Twin Cities Pawn hours",
        ) + body


def page_sitemap():
    links = [
        ("index.html", "Home"), ("about.html", "About Us"),
        ("guns-rifles.html", "Guns &amp; Rifles"), ("guns-rifles.html#handguns", "&rsaquo; Handguns &amp; Pistols"),
        ("guns-rifles.html#revolvers", "&rsaquo; Revolvers"), ("guns-rifles.html#rifles", "&rsaquo; Rifles"),
        ("guns-rifles.html#shotguns", "&rsaquo; Shotguns"), ("guns-rifles.html#archery", "&rsaquo; Archery"),
        ("guns-rifles.html#collectible", "&rsaquo; Collectible Firearms"), ("guns-rifles.html#nfa", "&rsaquo; NFA Items"),
        ("accessories.html", "Accessories &amp; Ammo"), ("accessories.html#ammo", "&rsaquo; Ammunition"),
        ("accessories.html#optics", "&rsaquo; Optics"), ("accessories.html#holsters", "&rsaquo; Holsters"),
        ("accessories.html#magazines", "&rsaquo; Magazines &amp; Safes"),
        ("pawn-loans.html", "Pawn &amp; Loans"), ("pawn-loans.html#loans", "&rsaquo; 0% Pawn Loans"),
        ("pawn-loans.html#tools", "&rsaquo; Power Tools"), ("pawn-loans.html#electronics", "&rsaquo; Electronics"),
        ("pawn-loans.html#jewelry", "&rsaquo; Jewelry &amp; Gold"),
        ("contact.html", "Contact"), ("faq.html", "FAQ"),
        ("faq-gun-pawns.html", "FAQ &ndash; Gun Pawns"), ("employment.html", "Employment"),
        ("resources.html", "Resources"), ("gun-law-checklist.html", "&rsaquo; 2026 Gun Law Checklist"),
        ("rules-for-pawning.html", "&rsaquo; Rules for Pawning a Gun"),
        ("gun-license-mn.html", "&rsaquo; Gun License in Minnesota"), ("unregistered-gun.html", "&rsaquo; Unregistered Firearms"),
        ("terms.html", "Terms &amp; Conditions"), ("privacy.html", "Privacy Policy"),
        ("equal-opportunity.html", "Equal Opportunity Employer"),
    ]
    lis = "".join('<li><a href="%s" class="text-on-surface-variant hover:text-primary-container transition-colors">%s</a></li>' % (h, t) for h, t in links)
    content = """
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <ul class="space-y-3 text-lg">%s</ul>
      <div class="mt-10 border-t border-outline-variant/20 pt-6">
        <div class="text-[10px] font-mono text-primary-container uppercase tracking-widest mb-3">Shop Online</div>
        <ul class="space-y-3 text-lg">
          <li><a href="%s" target="_blank" rel="noopener" class="text-on-surface-variant hover:text-primary-container">Armslist Store &nearr;</a></li>
          <li><a href="%s" target="_blank" rel="noopener" class="text-on-surface-variant hover:text-primary-container">GunBroker Listings &nearr;</a></li>
        </ul>
      </div>
    </section>""" % (lis, ARMSLIST, GUNBROKER)
    body = (nav() + ticker() +
            text_hero("Navigation", "Sitemap", "Every page on the Twin Cities Pawn &amp; Gun website, all in one place.") +
            content + footer())
    return head("Sitemap | Twin Cities Pawn & Gun \u2014 Ramsey, MN",
        "Full sitemap of the Twin Cities Pawn & Gun website \u2014 firearms, accessories, pawn loans, and more.",
        "sitemap.html",
        "Twin Cities Pawn sitemap, site navigation, pawn shop pages",
        ) + body


# ---------- NEW PAGES (mega-menu / resources update) ----------
def faq_accordion(faqs):
    items = []
    for q, a in faqs:
        items.append("""
        <div class="faq-item border border-outline-variant/40 bg-surface-container-low">
          <button class="faq-head w-full flex justify-between items-center gap-4 text-left px-6 py-5">
            <span class="font-headline font-semibold text-on-surface">{q}</span>
            <span class="material-symbols-outlined text-primary-container faq-icon">add</span>
          </button>
          <div class="faq-body px-6 text-on-surface-variant"><p class="pb-5">{a}</p></div>
        </div>""".format(q=q, a=a))
    return "".join(items)


def page_faq_gun_pawns():
    faqs = [
        ("Can I pawn a firearm in Minnesota?", "Yes. Twin Cities Pawn &amp; Gun is a licensed FFL dealer and we regularly accept firearms as collateral for pawn loans. You must be the legal owner, at least 18 (21 for handguns), and pass identity verification. Prohibited persons under federal or Minnesota law cannot pawn a firearm."),
        ("What ID do I need to pawn a gun?", "You'll need a valid, unexpired government-issued photo ID such as a Minnesota driver's license or state ID. We record the transaction as required by state pawn regulations and federal firearms law."),
        ("How do you determine how much my gun is worth?", "Our firearms specialists evaluate make, model, caliber, condition, age, included accessories, and current market demand. We aim to offer a fair loan value and will explain how we arrived at the figure."),
        ("What are the loan terms?", "Pawn loans are short-term and outlined in a written pawn ticket you receive at the time of the transaction. Twin Cities Pawn is Home of the 0% Pawn &mdash; ask our team about current terms, the redemption period, and how to extend a loan."),
        ("How do I get my firearm back?", "Repay the loan amount according to the terms on your pawn ticket within the redemption period. Because a firearm is being returned to you, you must again pass a background check and complete the required federal paperwork before we can release it."),
        ("Do I need a background check to reclaim my gun?", "Yes. Under federal law, returning a pawned firearm to its owner is treated as a transfer, so a NICS background check and ATF Form 4473 are required before the firearm can be handed back."),
        ("What happens if I don't repay the loan?", "If the loan isn't repaid or extended within the agreed period, the firearm is forfeited and becomes store inventory, which we may sell in compliance with all applicable laws. You are never obligated to repay &mdash; the item is the collateral."),
        ("Can I pawn a firearm that isn't registered to me?", "Minnesota does not maintain a general firearm registry, but you must be the lawful owner of any item you pawn. We cannot accept stolen property, and knowingly pawning a firearm you don't own is a crime."),
        ("Are there firearms you won't accept?", "We cannot accept firearms that are stolen, illegally modified, have obliterated serial numbers, or that we're prohibited from handling under federal or state law. NFA items have additional requirements &mdash; ask our staff."),
        ("Is my information kept private?", "We collect only what's required by law for firearms and pawn transactions and handle it in accordance with applicable regulations and our privacy policy. We do not sell your personal information."),
    ]
    content = """
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="space-y-4">{items}</div>
    </section>""".format(items=faq_accordion(faqs))
    body = (nav() + ticker() +
            text_hero("Help Center", "FAQ &ndash; Gun Pawns", "Everything you need to know about pawning a firearm at Twin Cities Pawn &amp; Gun in Ramsey, Minnesota.") +
            content +
            cta_band("Ready to Pawn Your Firearm?", "Stop by with a valid photo ID for a free, no-obligation valuation, or call us with any questions.", "Contact Us", "contact.html") +
            footer())
    return head("Gun Pawn FAQ | Twin Cities Pawn & Gun | Ramsey, MN",
        "Answers to common questions about pawning firearms in Minnesota: required ID, valuations, loan terms, background checks, and reclaiming your gun.",
        "faq-gun-pawns.html",
        "pawn a gun Minnesota, gun pawn FAQ, firearm pawn loan Ramsey MN, how to pawn a firearm, get pawned gun back",
        ) + body


def page_employment():
    positions = ["Sales Associate", "Firearms Specialist", "Pawn Specialist", "Manager", "Other"]
    opts = "".join("<option>%s</option>" % pos for pos in positions)
    form = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 grid lg:grid-cols-2 gap-12">
      <div>
        {label}
        <h2 class="font-headline font-bold text-headline-lg text-on-surface">Why Work With Us</h2>
        <div class="mt-5 space-y-4 text-on-surface-variant">
          <p>Twin Cities Pawn &amp; Gun has been a Ramsey fixture since 2010, and our team is the reason customers keep coming back. We're looking for friendly, honest, hard-working people who enjoy helping others.</p>
          <p>Firearms enthusiasts are especially welcome &mdash; but a great attitude and a willingness to learn matter most. We offer a supportive environment, competitive pay, and the chance to work with an amazing selection of firearms, tools, electronics, and collectibles every day.</p>
          <ul class="space-y-3 mt-6">
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Friendly, team-oriented workplace</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>On-the-job training &amp; growth</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Equal opportunity employer</li>
          </ul>
        </div>
      </div>
      <div class="crosshair-card relative border border-outline-variant/40 bg-surface-container-low p-7 gold-glow">
        {xh}
        <h3 class="font-headline font-bold text-headline-sm text-on-surface mb-5">Employment Application</h3>
        <form action="#" method="POST" class="space-y-5">
          <div>
            <label for="name" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Full Name</label>
            <input type="text" id="name" name="name" required class="w-full bg-surface-container border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors" />
          </div>
          <div class="grid sm:grid-cols-2 gap-5">
            <div>
              <label for="email" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Email</label>
              <input type="email" id="email" name="email" required class="w-full bg-surface-container border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors" />
            </div>
            <div>
              <label for="phone" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Phone</label>
              <input type="tel" id="phone" name="phone" class="w-full bg-surface-container border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors" />
            </div>
          </div>
          <div>
            <label for="position" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Position Applying For</label>
            <select id="position" name="position" class="w-full bg-surface-container border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors">{opts}</select>
          </div>
          <div>
            <label for="experience" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Relevant Experience</label>
            <textarea id="experience" name="experience" rows="4" class="w-full bg-surface-container border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors"></textarea>
          </div>
          <div>
            <label for="why" class="block font-mono text-[11px] uppercase tracking-widest text-on-surface-variant mb-2">Why do you want to work here?</label>
            <textarea id="why" name="why" rows="4" class="w-full bg-surface-container border border-outline-variant/40 px-4 py-3 text-on-surface focus:border-primary-container focus:outline-none transition-colors"></textarea>
          </div>
          <button type="submit" class="inline-flex items-center gap-2 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider gold-hover">Submit Application <span class="material-symbols-outlined text-base">send</span></button>
        </form>
      </div>
    </section>""".format(label=label("Careers"), xh=crosshairs(), opts=opts)
    body = (nav() + ticker() +
            page_hero("pawn-counter-guitars.webp", "Inside Twin Cities Pawn & Gun store", "Careers", "Join Our Team", "Twin Cities Pawn &amp; Gun is always looking for great people. Apply below to become part of our Ramsey crew.") +
            form + footer())
    return head("Employment Application | Twin Cities Pawn & Gun | Ramsey, MN",
        "Apply to join the team at Twin Cities Pawn & Gun in Ramsey, MN. We're hiring sales associates, firearms specialists, pawn specialists, and more.",
        "employment.html",
        "Twin Cities Pawn jobs, gun store jobs Ramsey MN, pawn shop employment Minnesota, firearms specialist job, apply now",
        ) + body


def page_resources():
    cards = [
        ("checklist", "2026 Gun Law Checklist", "How Minnesota stacks up on gun safety laws, background checks, and concealed carry.", "gun-law-checklist.html"),
        ("gavel", "Rules for Pawning a Gun", "Minnesota pawn laws, required ID, hold periods, and how to reclaim your firearm.", "rules-for-pawning.html"),
        ("badge", "Gun License in Minnesota", "Permit to Purchase, Permit to Carry, background checks, and how to apply.", "gun-license-mn.html"),
        ("warning", "Unregistered Firearms", "What \u201cregistered\u201d really means under federal NFA rules and how to stay legal.", "unregistered-gun.html"),
    ]
    card_html = []
    for icon, t, d, href in cards:
        card_html.append("""
        <a href="{href}" class="crosshair-card group relative block border border-outline-variant/40 bg-surface-container-low p-8 gold-aura-hover">
          {xh}
          <span class="material-symbols-outlined text-primary-container text-4xl">{icon}</span>
          <h3 class="font-headline font-bold text-headline-sm mt-4 text-on-surface">{t}</h3>
          <p class="text-sm text-on-surface-variant mt-2">{d}</p>
          <span class="inline-flex items-center gap-2 mt-5 font-mono text-xs uppercase tracking-wider text-primary-container">Learn More <span class="material-symbols-outlined text-sm">arrow_outward</span></span>
        </a>""".format(href=href, xh=crosshairs(), icon=icon, t=t, d=d))
    
    external_links = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin pb-16">
      <div class="border-t border-outline-variant/30 pt-10">
        <div class="text-[10px] font-mono text-primary-container uppercase tracking-widest mb-5">External Resources</div>
        <div class="space-y-3">
          <a href="https://www.house.mn.gov/hrd/pubs/firearms.pdf" target="_blank" rel="noopener" class="flex items-center gap-3 text-on-surface-variant hover:text-primary-container transition-colors">
            <span class="material-symbols-outlined text-lg">description</span>
            <span>Minnesota House Research: Firearms Laws (PDF) &nearr;</span>
          </a>
          <a href="https://www.revisor.mn.gov/statutes/cite/624.714" target="_blank" rel="noopener" class="flex items-center gap-3 text-on-surface-variant hover:text-primary-container transition-colors">
            <span class="material-symbols-outlined text-lg">gavel</span>
            <span>MN Statute 624.714: Carry Permit &nearr;</span>
          </a>
        </div>
      </div>
    </section>"""
    
    content = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <p class="text-on-surface-variant max-w-2xl mb-10">Firearms and pawn transactions come with important rules and responsibilities. We've put together plain-English guides to help you understand Minnesota law and shop with confidence. Explore the resources below.</p>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
    </section>""".format(cards="".join(card_html))
    body = (nav() + ticker() +
            text_hero("Know Before You Go", "Resources", "Helpful guides on pawning firearms, Minnesota gun licensing, firearm registration law, and current gun safety laws.") +
            content + external_links +
            cta_band("Still Have Questions?", "Our knowledgeable staff is happy to walk you through the details. Give us a call or stop in.", "Contact Us", "contact.html") +
            footer())
    return head("Resources | Twin Cities Pawn & Gun | Ramsey, MN",
        "Gun law resources from Twin Cities Pawn & Gun: 2026 checklist, MN gun licensing, rules for pawning a firearm, and firearm registration law explained.",
        "resources.html",
        "gun pawn resources, Minnesota firearm law, gun license guide, pawn a gun rules, Twin Cities Pawn resources, 2026 gun laws",
        ) + body


def page_rules_for_pawning():
    c = "".join([
        p("Pawning a firearm can be a fast, discreet way to get a short-term loan using something you already own. But because firearms are involved, the process is governed by both federal and Minnesota law. Here's what you need to know before you visit Twin Cities Pawn &amp; Gun."),
        h3("Who Can Pawn a Firearm"),
        p("You must be the lawful owner of the firearm and legally allowed to possess it. You must be at least 18 years old for long guns and 21 for handguns. Individuals prohibited from possessing firearms under federal or Minnesota law &mdash; including certain felony convictions, domestic-violence orders, or adjudications &mdash; cannot pawn a firearm."),
        h3("What to Bring"),
        p("Bring a valid, unexpired government-issued photo ID (such as a Minnesota driver's license or state ID) and the firearm itself, unloaded and cased if possible. Any accessories, cases, or original boxes can increase the loan value. We'll record the transaction as required by state pawn regulations."),
        h3("How Valuation Works"),
        p("Our firearms specialists assess the make, model, caliber, condition, age, market demand, and any included accessories. We'll explain how we arrived at your offer. As the Home of the 0% Pawn, our goal is a fair deal &mdash; ask about current loan terms and redemption periods."),
        h3("The Hold &amp; Redemption Period"),
        p("When you pawn an item you receive a written pawn ticket that spells out the loan amount, fees, and the redemption period during which you can repay and reclaim your firearm. Your firearm is stored securely for the duration of the loan. Minnesota pawn shops are also required to report transactions to help law enforcement identify stolen property, which typically involves a short investigatory hold on incoming items."),
        h3("Reclaiming Your Firearm"),
        p("To get your firearm back, repay the loan according to your pawn ticket within the redemption period. Because handing a firearm back to its owner is legally a transfer, federal law requires you to complete an ATF Form 4473 and pass a NICS background check before the firearm can be released &mdash; even though it's your own gun."),
        h3("What Happens If You Don't Redeem"),
        p("A pawn loan is non-recourse: if you choose not to repay, you simply forfeit the firearm, which becomes store inventory that we may sell in full compliance with the law. There's no impact on your credit and no further obligation."),
        h3("Firearms We Cannot Accept"),
        p("We cannot accept stolen firearms, guns with obliterated or altered serial numbers, illegally modified firearms, or any item we're prohibited from handling. NFA-regulated items such as suppressors and short-barreled rifles carry additional federal requirements &mdash; talk to our staff about the specifics."),
        h3("FFL Considerations"),
        p("Twin Cities Pawn &amp; Gun is a fully licensed FFL dealer, so every firearm transaction &mdash; including pawns and redemptions &mdash; is handled by the book with the proper paperwork and background checks. This protects both you and the shop."),
        p('<span class="text-outline text-sm">This page is provided for general informational purposes and reflects our understanding of applicable rules; it is not legal advice. Laws change &mdash; contact us or a qualified attorney for guidance on your situation.</span>'),
    ])
    return info_page("rules-for-pawning.html", "Rules for Pawning a Gun in Minnesota | Twin Cities Pawn & Gun",
        "A plain-English guide to pawning a firearm in Minnesota: who qualifies, what ID to bring, how valuation works, hold periods, and reclaiming your gun.",
        "rules for pawning a gun, pawn a firearm Minnesota, gun pawn requirements Ramsey MN, how to pawn a gun, reclaim pawned firearm",
        "rules-pawning-hero.webp", "Vintage revolver with wood grips on wooden surface", 
        "Guide", "Rules for Pawning a Gun", "What you need to know before pawning a firearm in Minnesota.", c)


def page_gun_license_mn():
    c = "".join([
        p("Minnesota has specific requirements for purchasing and carrying firearms. Whether you're buying your first handgun or planning to carry, here's an overview of the permits and processes involved."),
        h3("Permit to Purchase (PTP)"),
        p("To buy a handgun or a semiautomatic military-style assault weapon from a dealer in Minnesota, you generally need either a Permit to Purchase or a valid Permit to Carry. The Permit to Purchase is issued free of charge by your local police chief or county sheriff, is valid for one year, and lets you buy eligible firearms during that time."),
        h3("Permit to Carry (PTC)"),
        p("A Minnesota Permit to Carry allows you to carry a handgun in public and also serves as a purchase permit. To qualify you must be at least 21, complete an approved firearms-training course from a certified instructor, and apply through your county sheriff. The permit is valid for five years statewide."),
        h3("Background Checks"),
        p("All firearm purchases from a licensed FFL dealer &mdash; including Twin Cities Pawn &amp; Gun &mdash; require a federal NICS background check via ATF Form 4473. Holding a valid PTP or PTC may streamline the process, but the dealer still verifies eligibility at the point of sale."),
        h3("How to Apply"),
        p("Applications for both the Permit to Purchase and Permit to Carry are submitted to your local sheriff or police department. You'll provide identification, complete the application, and (for the PTC) show proof of completed training. Authorities have a set number of days under state law to approve or deny the application."),
        h3("Long Guns"),
        p("Rifles and shotguns that are not classified as semiautomatic military-style assault weapons generally do not require a Permit to Purchase in Minnesota, though you still must be a legal buyer and pass the dealer's background check."),
        h3("Who Cannot Obtain a Permit"),
        p("Prohibited persons &mdash; including those with certain felony or domestic-violence convictions, active restraining orders, or specific mental-health adjudications &mdash; are not eligible. Federal and state law both apply."),
        h3("The Role of Your FFL Dealer"),
        p("As a licensed dealer, we help ensure your purchase is legal and properly documented. Our staff can answer general questions about permits, transfers, and the paperwork involved, and we handle incoming FFL transfers for a flat $50 fee."),
        h3("Common Questions"),
        p("Do I need a permit to buy a rifle? Usually no, for standard long guns. Does a Permit to Carry let me buy handguns? Yes. How long does a Permit to Purchase last? One year. Where do I apply? Your local sheriff or police department."),
        p('<span class="text-outline text-sm">This overview is for general information only and is not legal advice. Permit rules and timelines can change &mdash; confirm current requirements with your local sheriff\'s office or the Minnesota Bureau of Criminal Apprehension.</span>'),
    ])
    return info_page("gun-license-mn.html", "Minnesota Gun License & Permit | Twin Cities Pawn & Gun",
        "Understand Minnesota gun licensing: Permit to Purchase, Permit to Carry, background checks, how to apply, and the role of your FFL dealer.",
        "Minnesota gun license, permit to purchase MN, permit to carry Minnesota, MN firearms permit, how to apply gun permit Minnesota",
        "gun-license-mn-hero.webp", "Handgun with scattered ammunition on dark blue surface",
        "Guide", "Gun License in Minnesota", "Permits, background checks, and how to buy or carry legally in Minnesota.", c)


def page_unregistered_gun():
    c = "".join([
        p("There's a lot of confusion about \u201cregistered\u201d and \u201cunregistered\u201d firearms. In most cases, everyday rifles, shotguns, and handguns are not registered with any government database in Minnesota &mdash; there is no general state firearm registry. The term \u201cregistration\u201d most often applies to specific federally regulated items under the National Firearms Act (NFA)."),
        h3("What \u201cRegistered\u201d Actually Means"),
        p("Under the federal NFA, certain items must be registered in the National Firearms Registration and Transfer Record: suppressors (silencers), short-barreled rifles (SBRs), short-barreled shotguns (SBS), machine guns, and destructive devices. Owning one of these items legally requires ATF approval, the proper paperwork, and an associated tax stamp."),
        h3("Unregistered NFA Items Are Illegal"),
        p("Possessing an NFA item that has not been properly registered &mdash; for example, an unregistered suppressor or an illegally shortened rifle &mdash; is a serious federal felony. Penalties can include years in prison and substantial fines. This is very different from simply owning a standard firearm that isn't in any registry."),
        h3("Standard Firearms vs. NFA Items"),
        p("An ordinary pistol, rifle, or shotgun that you legally purchased does not need to be \u201cregistered\u201d in Minnesota, and not having it in a database does not make it illegal. The legal concern arises specifically with NFA-regulated items, stolen firearms, or guns with obliterated serial numbers."),
        h3("Minnesota State Law"),
        p("Minnesota does not require registration of ordinary firearms, but it does regulate who may possess firearms and how certain purchases are permitted. Possessing a firearm as a prohibited person, or possessing an illegal NFA item, carries severe state and federal consequences."),
        h3("Consequences of Getting Caught"),
        p("Illegally possessing an unregistered NFA item or an otherwise prohibited firearm can lead to felony charges, forfeiture of the firearm, loss of firearm rights, heavy fines, and imprisonment. Serial-number tampering and possession of stolen firearms are also criminal offenses."),
        h3("How to Stay Legal"),
        p("Buy from a licensed FFL dealer, keep your purchase records, and never alter a firearm in a way that would make it an unregistered NFA item. If you want a suppressor or SBR, work with a dealer like Twin Cities Pawn &amp; Gun to complete the proper ATF Form 4, trust or individual registration, and tax stamp before you take possession."),
        h3("We Can Help"),
        p("Our staff can walk you through the legal path to owning NFA items and make sure every transaction is fully compliant. When in doubt, ask us before you buy, modify, or sell."),
        p('<span class="text-outline text-sm">This information is for educational purposes only and does not constitute legal advice. Firearms laws are complex and change over time &mdash; consult the ATF or a qualified attorney regarding your specific circumstances.</span>'),
    ])
    return info_page("unregistered-gun.html", "Unregistered Guns in Minnesota | Twin Cities Pawn & Gun",
        "What \u201cregistered\u201d really means under federal NFA law, the difference between standard firearms and NFA items, and the consequences of unregistered guns.",
        "unregistered firearms Minnesota, NFA registration, unregistered suppressor, SBR laws, illegal firearm consequences MN, stay legal firearms",
        "unregistered-gun-hero.webp", "Firearms laid out on a table — unregistered firearms Minnesota guide",
        "Guide", "Unregistered Firearms in Minnesota", "Understanding firearm registration, NFA items, and how to stay on the right side of the law.", c)


def page_gun_law_checklist():
    """2026 Minnesota Gun Law Checklist — based on Everytown Research rankings"""
    intro = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <div class="flex items-start gap-6 mb-10 p-8 bg-surface-container-low border border-outline-variant/40">
        <div class="flex-shrink-0 w-20 h-20 rounded-full bg-primary-container/10 flex items-center justify-center">
          <span class="font-headline text-3xl font-bold text-primary-container">#14</span>
        </div>
        <div>
          <h2 class="font-headline font-bold text-headline-md text-on-surface">Minnesota Gun Law Strength</h2>
          <p class="text-on-surface-variant mt-2"><strong>Ranked #14 in the nation</strong> for gun law strength. Minnesota has passed strong gun safety policies including universal background checks, Extreme Risk laws, and domestic abuser prohibitions.</p>
          <div class="grid grid-cols-2 gap-6 mt-5 text-sm">
            <div><div class="font-mono text-xs text-primary-container uppercase tracking-widest">Composite Score</div><div class="text-on-surface font-bold text-2xl">55/100</div></div>
            <div><div class="font-mono text-xs text-primary-container uppercase tracking-widest">Gun Death Rate</div><div class="text-on-surface font-bold text-2xl">9.8</div><div class="text-on-surface-variant text-xs">per 100k residents (national avg: 12.8)</div></div>
          </div>
        </div>
      </div>
      <p class="text-on-surface-variant text-sm italic">Data sourced from <a href="https://everytownresearch.org/rankings/state/minnesota/" target="_blank" rel="noopener" class="text-primary-container hover:underline">Everytown Research &nearr;</a> (Last updated January 14, 2026)</p>
    </section>"""
    
    def law_cat(title, laws):
        laws_html = "".join('<li class="flex items-start gap-3 text-on-surface-variant"><span class="material-symbols-outlined text-primary-container text-lg flex-shrink-0">check_circle</span><span>%s</span></li>' % law for law in laws)
        return """
        <div class="mb-12">
          <h3 class="font-headline font-bold text-headline-sm text-on-surface mb-5 pb-3 border-b border-outline-variant/30">%s</h3>
          <ul class="space-y-3">%s</ul>
        </div>""" % (title, laws_html)
    
    content = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin pb-16">
      {foundational}
      {industry}
      {public}
      {wrong_hands}
      {policing}
      {sales}
    </section>""".format(
        foundational=law_cat("Foundational Laws", [
            "<strong>Background checks required</strong> for handgun and semiautomatic assault weapon purchases (permit to purchase or point-of-sale)",
            "<strong>Concealed carry permit required</strong> with training (including live-fire requirement)",
            "<strong>Extreme Risk law</strong> allows temporary gun removal for individuals in crisis",
            "<strong>No Shoot First law</strong> in place",
            "<strong>Secure storage required</strong> when a child (under 18) may access the firearm"
        ]),
        industry=law_cat("Gun Industry & Product Safety", [
            "<strong>Assault weapons prohibited</strong> (military-style weapons banned)",
            "<strong>Auto sears / Glock switches prohibited</strong>",
            "<strong>Bump stocks prohibited</strong>",
            "<strong>Consumer safety:</strong> new handgun models must have childproofing features",
            "<strong>Dealer license required</strong> at state level",
            "<strong>Ghost guns regulated</strong> (serial numbers required, background checks enforced)",
            "<strong>High-capacity magazines prohibited</strong>",
            "<strong>Legal accountability for gun industry</strong> allowed",
            "<strong>Microstamping for new handguns</strong> required"
        ]),
        public=law_cat("Guns in Public", [
            "<strong>No carry after violent offense</strong> (3-year ban for assault/violent misdemeanor)",
            "<strong>No guns mandate on college campuses</strong>",
            "<strong>No guns at state capitol or demonstrations</strong>",
            "<strong>No guns in bars</strong>",
            "<strong>No guns in K-12 schools</strong> by staff or permit holders",
            "<strong>Open carry regulated</strong> (permit required for all firearms)",
            "<strong>Strong concealed carry authority</strong> (officials can deny for public safety)"
        ]),
        wrong_hands=law_cat("Keeping Guns Out of the Wrong Hands", [
            "<strong>Emergency restraining order prohibitor</strong> (domestic abusers barred)",
            "<strong>Felony prohibitor</strong> (indefinite)",
            "<strong>Fugitive from justice prohibitor</strong>",
            "<strong>Gun removal program</strong> (officials seek illegal guns)",
            "<strong>Hate crime prohibitor</strong>",
            "<strong>Mental health prohibitor</strong> (indefinite for involuntary commitments)",
            "<strong>Minimum age:</strong> 21+ for handguns, 18+ for long guns",
            "<strong>Assault/violent misdemeanor prohibitor</strong> (3-year ban)",
            "<strong>Domestic abuser prohibition</strong> (misdemeanor conviction + restraining orders, covers dating partners)",
            "<strong>Relinquishment required</strong> for convicted abusers and those under restraining orders",
            "<strong>School threat assessment teams</strong> required",
            "<strong>Stalker prohibitor</strong> (3-year ban)"
        ]),
        policing=law_cat("Policing & Civil Rights", [
            "<strong>Funding for victims of gun violence</strong> via VOCA funds",
            "<strong>Local gun laws allowed</strong> (no state preemption)",
            "<strong>No Law Enforcement Officers Bill of Rights</strong>",
            "<strong>Office of Violence Intervention</strong> exists",
            "<strong>Police deadly force standard:</strong> only when necessary to prevent serious injury",
            "<strong>Qualified immunity limited</strong>",
            "<strong>Tools to address crime guns:</strong> tracing + trafficking/straw purchase crimes",
            "<strong>Violence intervention program funding</strong> in state budget"
        ]),
        sales=law_cat("Sales & Permitting", [
            "<strong>Authority to deny gun purchase</strong> if buyer poses danger",
            "<strong>Charleston Loophole closed</strong> (30-day waiting period for handguns/assault weapons)",
            "<strong>Lost and stolen reporting</strong> required",
            "<strong>Mental health record reporting</strong> into background check system",
            "<strong>Sales records sent to law enforcement</strong> (handguns)",
            "<strong>Training required to purchase guns</strong>",
            "<strong>Waiting periods</strong> enforced"
        ])
    )
    
    body = (nav() + ticker() +
            page_hero("gun-law-checklist-hero.webp", "Classic hunting shotguns displayed in wooden rack", "2026 Checklist", "Gun Law Checklist", "How Minnesota ranks on gun safety laws, background checks, concealed carry, and more.") +
            intro + content +
            cta_band("Questions About Minnesota Gun Laws?", "Our knowledgeable team can help you navigate firearms regulations in Minnesota. Give us a call or stop in.", "Contact Us", "contact.html") +
            footer())
    return head("2026 Gun Law Checklist | Minnesota | Twin Cities Pawn & Gun",
        "Minnesota's 2026 gun law rankings: #14 in the nation for gun law strength. See how the state stacks up on background checks, permits, and gun safety policies.",
        "gun-law-checklist.html",
        "Minnesota gun laws 2026, gun law rankings Minnesota, background check laws MN, concealed carry permit Minnesota, gun safety laws",
        ) + body


# ---------- WRITE-OUT ----------
PAGES = {
    "index.html": page_index,
    "about.html": page_about,
    "guns-rifles.html": page_guns,
    "accessories.html": page_accessories,
    "pawn-loans.html": page_pawn,
    "contact.html": page_contact,
    "terms.html": page_terms,
    "privacy.html": page_privacy,
    "equal-opportunity.html": page_equal,
    "faq.html": page_faq,
    "faq-gun-pawns.html": page_faq_gun_pawns,
    "employment.html": page_employment,
    "resources.html": page_resources,
    "rules-for-pawning.html": page_rules_for_pawning,
    "gun-license-mn.html": page_gun_license_mn,
    "unregistered-gun.html": page_unregistered_gun,
    "gun-law-checklist.html": page_gun_law_checklist,
    "sitemap.html": page_sitemap,
}

# Priority hints for sitemap.xml (Cheirank / canonical consistency)
SITEMAP_PRIORITY = {
    "index.html": "1.0",
    "guns-rifles.html": "0.9", "pawn-loans.html": "0.9", "accessories.html": "0.9",
    "contact.html": "0.8", "about.html": "0.8",
    "resources.html": "0.7", "gun-law-checklist.html": "0.7", "gun-license-mn.html": "0.7",
    "rules-for-pawning.html": "0.7", "unregistered-gun.html": "0.6",
    "faq.html": "0.6", "faq-gun-pawns.html": "0.6", "employment.html": "0.5",
    "terms.html": "0.3", "privacy.html": "0.3", "equal-opportunity.html": "0.3",
    "sitemap.html": "0.3",
}


def write_sitemap_xml():
    import datetime
    today = datetime.date.today().isoformat()
    urls = ""
    for fname in PAGES:
        loc = "%s/%s" % (BASE_URL, fname)
        prio = SITEMAP_PRIORITY.get(fname, "0.5")
        urls += ('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
                 '    <changefreq>weekly</changefreq>\n    <priority>%s</priority>\n  </url>\n'
                 % (loc, today, prio))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           '%s</urlset>\n' % urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml (%d urls)" % len(PAGES))


def write_robots_txt():
    txt = ("User-agent: *\n"
           "Allow: /\n\n"
           "Sitemap: %s/sitemap.xml\n" % BASE_URL)
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(txt)
    print("wrote robots.txt")


if __name__ == "__main__":
    for fname, fn in PAGES.items():
        html = fn()
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", fname, len(html), "bytes")
    # remove old services.html (replaced by pawn-loans.html)
    old = os.path.join(OUT, "services.html")
    if os.path.exists(old):
        os.remove(old)
        print("removed services.html")
    write_sitemap_xml()
    write_robots_txt()
    print("DONE")
