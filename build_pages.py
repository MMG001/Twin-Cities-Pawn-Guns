# -*- coding: utf-8 -*-
"""Page-body functions + write-out logic. Imported/execfile'd after build.py helpers.
This file is concatenated onto build.py by the shell before running."""


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
    <section class="bg-surface-container-lowest border-y border-outline-variant/30 py-16">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        {label_center}
        <h2 class="font-headline font-bold text-headline-lg text-on-surface">Brands We Carry</h2>
        <p class="mt-2 text-on-surface-variant max-w-2xl mx-auto">A rotating selection from the most trusted names in the industry &mdash; inventory changes daily.</p>
        <div class="mt-8 flex flex-wrap justify-center gap-3">
{chips}
        </div>
      </div>
    </section>""".format(label_center=('<div class="flex justify-center">%s</div>' % label("Trusted Manufacturers")), chips=brand_chips())


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
    <section class="relative blueprint-grid overflow-hidden">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid lg:grid-cols-2 gap-10 items-center py-16 lg:py-24">
        <div>
          {label}
          <h1 class="font-headline font-bold text-display-hero-mobile md:text-display-hero text-on-surface">Home of the <span class="text-primary-container">0% Pawn</span></h1>
          <p class="mt-6 text-body-lg text-on-surface-variant max-w-xl">Ramsey's trusted firearms dealer and pawn shop since 2010. Hundreds of guns, rifles, and shotguns in stock &mdash; plus fair, honest pawn loans at zero percent interest.</p>
          <div class="mt-8 flex flex-wrap gap-4">
            <a href="guns-rifles.html" class="inline-flex items-center gap-2 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Browse Inventory <span class="material-symbols-outlined text-base">arrow_outward</span></a>
            <a href="pawn-loans.html" class="inline-flex items-center gap-2 border border-outline-variant/60 text-on-surface font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors">Get a Pawn Loan</a>
          </div>
        </div>
        <div class="relative crosshair-card border border-outline-variant/40 gold-glow">
          {xh}
          <img src="images/storefront.webp" alt="Twin Cities Pawn & Gun storefront in Ramsey, Minnesota" class="w-full h-[420px] object-cover" />
          <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-surface-container-lowest to-transparent p-6">
            <div class="font-mono text-xs text-primary-container uppercase tracking-widest">6650 US-10 &middot; Ramsey, MN</div>
          </div>
        </div>
      </div>
    </section>""".format(label=label("Firearms &middot; Pawn &middot; Loans"), xh=crosshairs())

    cat_cards = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <div class="mb-10">{label}<h2 class="font-headline font-bold text-headline-lg text-on-surface">Explore The Vault</h2></div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <a href="guns-rifles.html" class="crosshair-card group relative block border border-outline-variant/40 overflow-hidden gold-aura-hover">
          {xh}
          <img src="images/rifle-wall.webp" alt="Wall of rifles at Twin Cities Pawn & Gun" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="p-6"><h3 class="font-headline font-bold text-headline-sm text-on-surface">Guns &amp; Rifles</h3><p class="text-sm text-on-surface-variant mt-2">Handguns, rifles, shotguns, revolvers, collectibles &amp; NFA items.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Shop firearms <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
        </a>
        <a href="accessories.html" class="crosshair-card group relative block border border-outline-variant/40 overflow-hidden gold-aura-hover">
          {xh}
          <img src="images/firearms-handguns-rifles.webp" alt="Handguns and accessories display case" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="p-6"><h3 class="font-headline font-bold text-headline-sm text-on-surface">Accessories &amp; Ammo</h3><p class="text-sm text-on-surface-variant mt-2">Ammunition, optics, holsters, magazines, cases &amp; safes.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Shop gear <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
        </a>
        <a href="pawn-loans.html" class="crosshair-card group relative block border border-outline-variant/40 overflow-hidden gold-aura-hover">
          {xh}
          <img src="images/pawn-counter-guitars.webp" alt="Pawn counter with guitars and merchandise" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
          <div class="p-6"><h3 class="font-headline font-bold text-headline-sm text-on-surface">Pawn &amp; Loans</h3><p class="text-sm text-on-surface-variant mt-2">0% pawn loans, tools, electronics, jewelry &amp; gold.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs uppercase tracking-wider text-primary-container">Get a loan <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
        </a>
      </div>
    </section>""".format(label=label("Categories"), xh=crosshairs())

    showcase_cards = [
        inv_card("gun-room-rifles.webp", "Rifle room with tactical and hunting rifles", "In Stock", "Tactical &amp; Hunting Rifles", "New &amp; Used"),
        inv_card("1911-pistols.webp", "1911 pistols in display case", "In Stock", "1911 Pistols", "New &amp; Used"),
        inv_card("revolver-showcase.webp", "Revolver showcase display", "In Stock", "Revolvers", "New &amp; Used"),
        inv_card("shotgun-rack.webp", "Rack of shotguns", "In Stock", "Shotguns", "New &amp; Used"),
    ]
    showcase = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <div class="flex flex-wrap items-end justify-between gap-4 mb-10">
        <div>{label}<h2 class="font-headline font-bold text-headline-lg text-on-surface">Firearms Showcase</h2></div>
        <a href="guns-rifles.html" class="font-mono text-xs uppercase tracking-wider text-primary-container hover:text-primary-fixed inline-flex items-center gap-2">View all <span class="material-symbols-outlined text-sm">arrow_forward</span></a>
      </div>
      {grid}
    </section>""".format(label=label("Featured"), grid=grid(showcase_cards, cols="sm:grid-cols-2 lg:grid-cols-4"))

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

    body = (nav() + ticker() + hero + trust + cat_cards + showcase +
            brands_section() + online_cta() + hours_location() + footer())
    return head(
        "Twin Cities Pawn & Gun | Firearms, Pawn Loans & Guns in Ramsey, MN",
        "Twin Cities Pawn & Gun in Ramsey, MN \u2014 Home of the 0% Pawn. Hundreds of guns, rifles, shotguns & accessories in stock. Licensed FFL dealer, $50 transfers, 0% pawn loans since 2010.",
        "index.html",
        "pawn shop Ramsey MN, gun store Ramsey, firearms dealer Minnesota, 0% pawn loans, FFL transfer, buy guns Ramsey, Twin Cities Pawn",
        schema=schema) + body


# ================= ABOUT =================
def page_about():
    story = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 grid lg:grid-cols-2 gap-12 items-center">
      <div class="relative crosshair-card border border-outline-variant/40 gold-glow">
        {xh}
        <img src="images/pawn-counter-guitars.webp" alt="Inside Twin Cities Pawn & Gun store" class="w-full h-[420px] object-cover" />
      </div>
      <div>
        {label}
        <h2 class="font-headline font-bold text-headline-lg text-on-surface">Ramsey's Trusted Pawn &amp; Gun Shop</h2>
        <div class="mt-5 space-y-4 text-on-surface-variant">
          <p>Twin Cities Pawn &amp; Gun has proudly served the Minneapolis&ndash;St. Paul metro area since 2010. What started as a local pawn shop has grown into one of the region's most trusted destinations for firearms, ammunition, and fair pawn loans.</p>
          <p>We're a fully licensed FFL dealer with hundreds of handguns, rifles, and shotguns in stock at any given time. Whether you're a first-time buyer, a seasoned collector, or you simply need a short-term loan, our knowledgeable staff treats every customer with honesty and respect.</p>
          <p>We're best known as the <span class="text-primary-container font-semibold">Home of the 0% Pawn</span> &mdash; because we believe in giving our neighbors a fair deal. Stop by our Ramsey location on US-10 and see the difference for yourself.</p>
        </div>
        <a href="contact.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Visit Us <span class="material-symbols-outlined text-base">arrow_outward</span></a>
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
        <div class="crosshair-card relative border border-outline-variant/40 bg-surface-container-low p-7 gold-aura-hover">
          {xh}
          <span class="material-symbols-outlined text-primary-container text-3xl">{icon}</span>
          <h3 class="font-headline font-bold text-headline-sm mt-4 text-on-surface">{t}</h3>
          <p class="text-sm text-on-surface-variant mt-2">{d}</p>
        </div>""".format(xh=crosshairs(), icon=icon, t=t, d=d))
    why = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <div class="mb-10">{label}<h2 class="font-headline font-bold text-headline-lg text-on-surface">Why Choose Us</h2></div>
      {grid}
    </section>""".format(label=label("The Difference"), grid=grid(reason_cards))

    body = (nav() + ticker() +
            page_hero("gun-room-rifles.webp", "Firearms display at Twin Cities Pawn & Gun", "About Us", "About Twin Cities Pawn &amp; Gun", "Serving Ramsey and the Twin Cities with honest firearms sales and fair pawn loans since 2010.") +
            story + stats + why + brands_section() + hours_location() + footer())
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
            page_hero("rifle-wall.webp", "Wall of rifles at Twin Cities Pawn & Gun", "Firearms Inventory", "Guns &amp; Rifles", "Hundreds of handguns, rifles, shotguns, revolvers and more in stock. Inventory changes daily &mdash; shop online or visit us in Ramsey.") +
            chips + handguns + revolvers + rifles + shotguns + archery + collectible + nfa +
            online_cta() + cta_band("Can't Find What You're Looking For?", "Our inventory turns over fast and much of it never makes it online. Call us or stop by &mdash; we'll help you find the right firearm.", "Contact Us", "contact.html") +
            brands_section() + footer())
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
            page_hero("firearms-handguns-rifles.webp", "Firearms accessories display", "Gear &amp; Accessories", "Accessories &amp; Ammo", "Ammunition, optics, holsters, magazines, safes and more &mdash; everything you need to run and maintain your firearms.") +
            chips + ammo + optics + holsters + magazines +
            cta_band("Need Something Specific?", "We stock far more than we can list online. Give us a call and we'll let you know what's in stock or help you order it.", "Contact Us", "contact.html") +
            online_cta() + brands_section() + footer())
    return head(
        "Ammunition & Firearm Accessories | Twin Cities Pawn & Gun \u2014 Ramsey, MN",
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
            hours_location() + footer())
    return head(
        "0% Pawn Loans & FFL Transfers | Twin Cities Pawn & Gun \u2014 Ramsey, MN",
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
        <div class="crosshair-card border border-outline-variant/40 overflow-hidden gold-glow h-[300px]">
          <iframe src="https://maps.google.com/maps?q=6650+US-10,+Ramsey,+MN+55303&output=embed" width="100%" height="100%" style="border:0" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map to Twin Cities Pawn & Gun"></iframe>
        </div>
      </div>
    </section>""".format(label=label("Get In Touch"), xh=crosshairs(), gmaps=GMAPS)

    body = (nav() + ticker() +
            page_hero("storefront.webp", "Twin Cities Pawn & Gun storefront", "Contact", "Contact Us", "Stop by, call, or send us a message. We're here to help with firearms, pawn loans, and FFL transfers.") +
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
    "sitemap.html": page_sitemap,
}

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
    print("DONE")
