# -*- coding: utf-8 -*-
"""Page-body functions + write-out logic. Imported/execfile'd after build.py helpers.
This file is concatenated onto build.py by the shell before running."""

import os
from build import *

# ---------- small structural helpers ----------
def grid(cards, cols="sm:grid-cols-2 lg:grid-cols-3"):
    return '<div class="grid grid-cols-1 %s gap-6">%s\n        </div>' % (cols, "".join(cards))


def inv_section(sec_id, label_text, h2, sub, cards_html, bg="dark"):
    if bg == "white":
        outer = '<div style="background:#ffffff;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">'
        outer_end = '</div>'
        h2_extra = ' style="color:#111827"'
        sub_extra = ' style="color:#4b5563"'
        h2_cls = 'font-headline font-bold text-headline-lg'
        sub_cls = 'mt-2 max-w-2xl'
    elif bg == "gray":
        outer = '<div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">'
        outer_end = '</div>'
        h2_extra = ' style="color:#111827"'
        sub_extra = ' style="color:#4b5563"'
        h2_cls = 'font-headline font-bold text-headline-lg'
        sub_cls = 'mt-2 max-w-2xl'
    else:
        outer = ''
        outer_end = ''
        h2_extra = ''
        sub_extra = ''
        h2_cls = 'font-headline font-bold text-headline-lg text-on-surface'
        sub_cls = 'mt-2 text-on-surface-variant max-w-2xl'
    return """{outer}
    <section id="{sid}" data-section="{sid}" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14 scroll-mt-24">
      <div class="mb-8">
        {label}
        <h2 class="{h2_cls}"{h2_extra}>{h2}</h2>
        <p class="{sub_cls}"{sub_extra}>{sub}</p>
      </div>
      {cards}
    </section>{outer_end}""".format(outer=outer, outer_end=outer_end, sid=sec_id, label=label(label_text),
        h2=h2, sub=sub, cards=cards_html, h2_cls=h2_cls, sub_cls=sub_cls, h2_extra=h2_extra, sub_extra=sub_extra)


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


def cta_band(title, sub, btn_text, btn_href, external=False, bg_img=None):
    tgt = ' target="_blank" rel="noopener"' if external else ""
    if bg_img:
        return """
    <section class="relative py-24 overflow-hidden" style="background:#111">
      <img src="images/{bg_img}" alt="" aria-hidden="true" class="absolute inset-0 w-full h-full object-cover pointer-events-none select-none" style="opacity:0.35" loading="lazy" />
      <div class="relative z-10 max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        <h2 class="font-headline font-bold text-headline-lg" style="color:#ffffff">{title}</h2>
        <p class="mt-3 max-w-2xl mx-auto" style="color:#d1d5db">{sub}</p>
        <a href="{href}"{tgt} class="inline-flex items-center gap-2 mt-7 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider gold-hover">{btn} <span class="material-symbols-outlined text-base">arrow_outward</span></a>
      </div>
    </section>""".format(bg_img=bg_img, title=title, sub=sub, href=btn_href, tgt=tgt, btn=btn_text)
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
    <section class="py-16" style="background:#1b1b1e;border-top:1px solid #2e2c28;border-bottom:1px solid #2e2c28">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        {label_center}
        <h2 class="font-headline font-bold text-headline-lg" style="color:#ffffff">Brands We Carry</h2>
        <p class="mt-2 max-w-2xl mx-auto" style="color:#a0a0a8">A rotating selection from the most trusted names in the industry &mdash; inventory changes daily.</p>
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
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">Fair</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Pawn Valuations</div></div>
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">$50</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">FFL Transfers</div></div>
        <div class="py-8 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">2010</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Serving Since</div></div>
      </div>
    </section>"""

    hero = """
    <section class="relative min-h-[70vh] flex items-center blueprint-grid overflow-hidden" aria-label="Homepage hero">
      <img src="images/home-page-hero.jpg" alt="Interior of Twin Cities Gun & Pawn — hundreds of firearms in stock in the Twin Cities" class="absolute inset-0 w-full h-full object-cover" fetchpriority="high" />
      <div class="absolute inset-0" style="background:rgba(0,0,0,0.70)"></div>
      <div class="relative max-w-[1360px] mx-auto px-6 lg:px-margin py-24 w-full">
        {label}
        <h1 class="font-headline font-bold text-display-hero-mobile md:text-display-hero text-on-surface">Gun &amp; Firearms Pawn Shop &mdash; Buy &amp; Sell Guns, Rifles &amp; Shotguns in Minnesota</h1>
        <p class="mt-6 text-body-lg text-on-surface-variant max-w-2xl">Twin Cities Gun &amp; Pawn is a Minnesota gun broker specializing in handguns, pistols, revolvers, shotguns and AR-15 semi-automatic rifles. Buy new and used firearms, sell your gun for cash, or pawn your valuables at a licensed FFL dealer trusted across the Twin Cities and greater Minnesota since 2010.</p>
        <div class="mt-8 flex flex-wrap gap-4">
          <a href="guns-rifles.html" class="inline-flex items-center gap-2 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Browse Inventory <span class="material-symbols-outlined text-base">arrow_outward</span></a>
          <a href="pawn-loans.html" class="inline-flex items-center gap-2 border border-outline-variant/60 text-on-surface font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors">Get a Pawn Loan</a>
        </div>
        <!-- Trust badge strip — immediate credibility -->
        <div class="mt-10 flex flex-wrap gap-3" aria-label="Trust signals">
          <span class="inline-flex items-center gap-2 bg-black/60 border border-primary-container/60 text-primary-container font-mono text-[11px] font-bold uppercase tracking-wider px-3.5 py-2 backdrop-blur-sm"><span class="material-symbols-outlined text-sm" aria-hidden="true">verified</span>Licensed FFL Dealer</span>
          <span class="inline-flex items-center gap-2 bg-black/60 border border-white/20 text-white font-mono text-[11px] font-bold uppercase tracking-wider px-3.5 py-2 backdrop-blur-sm"><span class="material-symbols-outlined text-sm" aria-hidden="true">history</span>Serving MN Since 2010</span>
          <span class="inline-flex items-center gap-2 bg-black/60 border border-white/20 text-white font-mono text-[11px] font-bold uppercase tracking-wider px-3.5 py-2 backdrop-blur-sm"><span class="material-symbols-outlined text-sm" aria-hidden="true">storefront</span>300+ Firearms In Stock</span>
          <span class="inline-flex items-center gap-2 bg-black/60 border border-white/20 text-white font-mono text-[11px] font-bold uppercase tracking-wider px-3.5 py-2 backdrop-blur-sm"><span class="material-symbols-outlined text-sm" aria-hidden="true">swap_horiz</span>$50 FFL Transfers</span>
          <span class="inline-flex items-center gap-2 bg-black/60 border border-white/20 text-white font-mono text-[11px] font-bold uppercase tracking-wider px-3.5 py-2 backdrop-blur-sm"><span class="material-symbols-outlined text-sm" aria-hidden="true">lock</span>Secure Background Checks</span>
        </div>
      </div>
    </section>""".format(label=label("Twin Cities Gun &amp; Pawns"))

    broker_section = """
    <section class="py-16" style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        {label}
        <h2 class="font-headline font-bold text-headline-lg mt-2" style="color:#111827">Minnesota Firearms &amp; Gun Broker</h2>
        <p class="mt-4 text-body-lg max-w-3xl mx-auto" style="color:#374151">We&rsquo;re a leading Minnesota source for gently used, brand-name firearms &mdash; from concealed carry pistols and revolvers to hunting rifles and home-defense shotguns. Our inventory changes daily, so browse a category below or stop in for even more in-store deals on pre-owned guns.</p>
      </div>
    </section>""".format(label=label("Minnesota Gun Broker"))

    cat_cards = """
    <section class="py-16" style="background:#ffffff">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="mb-10 text-center">{label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Explore The Vault</h2><p class="mt-4 max-w-3xl mx-auto" style="color:#374151">We offer competitive prices on all our firearms so you can be sure you&rsquo;re getting a great deal. Stop into Twin Cities Gun &amp; Pawn and see our selection of high-quality handguns, rifles, shotguns, and accessories &mdash; we&rsquo;re confident you&rsquo;ll find exactly what you&rsquo;re looking for.</p></div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <a href="guns-rifles.html" class="crosshair-card group relative block overflow-hidden gold-aura-hover" style="border:1px solid #e2e8f0">
            {xh}
            <img src="images/gun-shop-showroom.webp" alt="Guns and rifles for sale at Twin Cities Gun &amp; Pawn in the Twin Cities" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="p-6" style="background:#ffffff"><h3 class="font-headline font-bold text-headline-sm" style="color:#111827">Guns &amp; Rifles</h3><p class="text-sm mt-2" style="color:#4b5563">Handguns, rifles, shotguns, revolvers &amp; more.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs font-bold uppercase tracking-wider px-3 py-1.5" style="background:#facc15;color:#000000">Shop firearms <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
          </a>
          <a href="accessories.html" class="crosshair-card group relative block overflow-hidden gold-aura-hover" style="border:1px solid #e2e8f0">
            {xh}
            <img src="images/rifle-scope-display.webp" alt="Ammunition and firearm accessories at Twin Cities Gun &amp; Pawn" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="p-6" style="background:#ffffff"><h3 class="font-headline font-bold text-headline-sm" style="color:#111827">Accessories &amp; Ammo</h3><p class="text-sm mt-2" style="color:#4b5563">Ammunition, optics, holsters, magazines, cases &amp; safes.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs font-bold uppercase tracking-wider px-3 py-1.5" style="background:#facc15;color:#000000">Shop gear <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
          </a>
          <a href="pawn-loans.html" class="crosshair-card group relative block overflow-hidden gold-aura-hover" style="border:1px solid #e2e8f0">
            {xh}
            <img src="images/cat-pawn-loans-real.webp" alt="Pawn loans at Twin Cities Gun &amp; Pawn — gun and cash" class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-500" />
            <div class="p-6" style="background:#ffffff"><h3 class="font-headline font-bold text-headline-sm" style="color:#111827">Pawn &amp; Loans</h3><p class="text-sm mt-2" style="color:#4b5563">Pawn your items or shop our store — tools, electronics, jewelry &amp; more.</p><span class="inline-flex items-center gap-2 mt-4 font-mono text-xs font-bold uppercase tracking-wider px-3 py-1.5" style="background:#facc15;color:#000000">See inventory <span class="material-symbols-outlined text-sm">arrow_outward</span></span></div>
          </a>
        </div>
      </div>
    </section>""".format(label=label("Categories"), xh=crosshairs())

    pawn_loan_split = """
    <section class="py-0" style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="flex flex-col md:flex-row gap-0 items-stretch">
          <!-- Image left -->
          <div class="md:w-1/2 relative overflow-hidden" style="min-height:420px">
            <img src="images/gun-pawn-transaction.webp" alt="Twin Cities Gun & Pawn staff and customer completing a firearm transaction in the Twin Cities" class="absolute inset-0 w-full h-full object-cover" />
          </div>
          <!-- Content right -->
          <div class="md:w-1/2 flex flex-col justify-center px-8 py-14" style="background:#f8f9fa">
            {label}
            <h2 class="font-headline font-bold text-headline-lg mt-2" style="color:#111827">Gun Pawn Loans &mdash; Get Cash Without Selling Your Firearm</h2>
            <p class="mt-4 text-body-md" style="color:#374151">Need cash fast? Pawn your handgun, rifle or shotgun and keep ownership. A firearm pawn loan puts money in your pocket today, and your gun is stored securely until you pay it back.</p>
            <ol class="mt-6 space-y-3">
              <li class="flex items-start gap-3"><span class="flex-shrink-0 w-7 h-7 rounded-full bg-primary-container flex items-center justify-center font-mono text-xs font-bold" style="color:#131316">1</span><span style="color:#374151">Bring in your firearm and a valid photo ID.</span></li>
              <li class="flex items-start gap-3"><span class="flex-shrink-0 w-7 h-7 rounded-full bg-primary-container flex items-center justify-center font-mono text-xs font-bold" style="color:#131316">2</span><span style="color:#374151">Get a cash offer on the spot.</span></li>
              <li class="flex items-start gap-3"><span class="flex-shrink-0 w-7 h-7 rounded-full bg-primary-container flex items-center justify-center font-mono text-xs font-bold" style="color:#131316">3</span><span style="color:#374151">Repay the loan and pick up your gun.</span></li>
            </ol>
            <div class="mt-8 flex flex-wrap gap-4">
              <a href="contact.html" class="inline-flex items-center gap-2 bg-primary-container font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover" style="color:#131316">Get a Gun Pawn Quote <span class="material-symbols-outlined text-base">arrow_outward</span></a>
              <a href="rules-for-pawning.html" class="inline-flex items-center gap-2 font-mono text-xs uppercase tracking-wider pt-3.5" style="color:#374151">Rules for pawning a gun in Minnesota <span class="material-symbols-outlined text-sm text-primary-container">arrow_forward</span></a>
            </div>
          </div>
        </div>
      </div>
    </section>""".format(label=label("Gun Pawn Loans"))

    showcase_cards = [
        inv_card("ar-rifles-display.webp", "Rifle room with tactical and hunting rifles", "In Stock", "Tactical &amp; Hunting Rifles", "New &amp; Used", light=True),
        inv_card("1911-handgun-display-case.webp", "1911 pistols in display case", "In Stock", "1911 Pistols", "New &amp; Used", light=True),
        inv_card("handgun-revolver-display-case.webp", "Revolver showcase display", "In Stock", "Revolvers", "New &amp; Used", light=True),
        inv_card("shotgun-rack-display.webp", "Rack of shotguns", "In Stock", "Shotguns", "New &amp; Used", light=True),
    ]
    showcase = """
    <section class="py-16" style="background:#f8f9fa;border-top:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="mb-10">
          {label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Twin Cities Largest Used Gun Selection</h2>
        </div>
        {grid}
        <div class="mt-10 flex justify-center">
          <a href="guns-rifles.html" class="inline-flex items-center gap-3 font-headline font-bold text-sm uppercase tracking-wider px-10 py-4" style="background:#131316;color:#facc15">Browse All Guns &amp; Rifles <span class="material-symbols-outlined text-base">arrow_outward</span></a>
        </div>
      </div>
    </section>""".format(label=label("Featured"), grid=grid(showcase_cards, cols="sm:grid-cols-2 lg:grid-cols-4"))

    gold_cta = """
    <section class="py-14" style="background:#facc15">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin text-center">
        <div class="font-mono text-[11px] tracking-widest uppercase mb-4" style="color:#6c5700">&#9733; Twin Cities, MN &middot; Since 2010 &#9733;</div>
        <h2 class="font-headline font-bold text-headline-lg" style="color:#131316;line-height:1.1">Ready to Buy, Sell, or Get a Loan?</h2>
        <p class="mt-4 max-w-xl mx-auto" style="color:#3c2f00">Visit us on US-10 in the Twin Cities. Open Monday&ndash;Friday 10AM&ndash;7PM, Saturday 10AM&ndash;5PM. Walk-ins always welcome.</p>
        <div class="mt-8 flex flex-wrap gap-4 justify-center">
          <a href="contact.html" class="inline-flex items-center gap-2 font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider" style="background:#131316;color:#facc15">Visit Our Store <span class="material-symbols-outlined text-base" style="color:#facc15">arrow_outward</span></a>
          <a href="tel:7634274100" class="inline-flex items-center gap-2 font-headline text-sm uppercase px-8 py-3.5 font-bold tracking-wider" style="border:2px solid #131316;color:#131316">(763) 427-4100</a>
        </div>
      </div>
    </section>"""

    schema = ('{\n'
              '  "@context": "https://schema.org",\n'
              '  "@type": "PawnShop",\n'
              '  "name": "Twin Cities Gun & Pawn",\n'
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

    store_split = """
    <section style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
        <div class="flex flex-col md:flex-row items-stretch" style="min-height:460px">
          <!-- Store interior photo left -->
          <div class="md:w-1/2 relative overflow-hidden" style="min-height:420px">
            <img src="images/store-interior.webp" alt="Twin Cities Gun &amp; Pawn store interior — pawn counter, guitars, tools, and jewelry in the Twin Cities" class="absolute inset-0 w-full h-full object-cover" />
          </div>
          <!-- Broker content right -->
          <div class="md:w-1/2 flex flex-col justify-center px-10 py-16 lg:px-16" style="background:#f8f9fa">
            {label}
            <h2 class="font-headline font-bold text-headline-lg mt-2" style="color:#111827">Minnesota Firearms &amp; Gun Broker</h2>
            <p class="mt-4 text-body-lg" style="color:#374151;max-width:520px">We&rsquo;re a leading Minnesota source for gently used, brand-name firearms &mdash; from concealed carry pistols and revolvers to hunting rifles and home-defense shotguns. Our inventory changes daily, so browse a category below or stop in for even more in-store deals on pre-owned guns.</p>
            <div class="mt-8">
              <a href="guns-rifles.html" class="inline-flex items-center gap-2 bg-primary-container font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover" style="color:#131316">Browse Inventory <span class="material-symbols-outlined text-base">arrow_outward</span></a>
            </div>
          </div>
        </div>
      </div>
    </section>""".format(label=label("Minnesota Gun Broker"))

    reviews = """
    <section class="relative border-y border-outline-variant/20 py-16 overflow-hidden">
      <div class="absolute inset-0 bg-cover bg-center" style="background-image:url('images/reviews-bg.webp')"></div>
      <div class="absolute inset-0" style="background:rgba(0,0,0,0.82)"></div>
      <div class="relative max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="text-center mb-10">
          <div class="inline-flex items-center font-mono text-[11px] font-bold tracking-widest uppercase mb-4 px-3 py-1.5" style="background:#facc15;color:#000000">Google Reviews</div>
          <h2 class="font-headline font-bold text-headline-lg text-on-surface">What Our Customers Say</h2>
          <div class="flex items-center justify-center gap-2 mt-3">
            <span class="text-primary-container text-xl">&#9733;&#9733;&#9733;&#9733;&#9733;</span>
            <span class="font-mono text-sm text-on-surface-variant">5.0 &middot; Verified Google Reviews</span>
          </div>
        </div>
        <div class="grid md:grid-cols-3 gap-6">
          <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 p-7 gold-aura-hover">
            {xh0}
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-full bg-primary-container flex items-center justify-center font-headline font-bold text-surface-container-lowest text-base flex-shrink-0">F</div>
              <div>
                <div class="font-headline font-bold text-on-surface text-sm">Freeman P.</div>
                <div class="text-primary-container text-sm">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              </div>
            </div>
            <p class="text-on-surface-variant text-sm leading-relaxed">&ldquo;Best priced firearms I&rsquo;ve found. Tyler is an awesome salesman &mdash; I&rsquo;ve never had any issues. They have new and used so you don&rsquo;t have to worry about getting someone&rsquo;s poorly maintained sloppy seconds.&rdquo;</p>
          </div>
          <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 p-7 gold-aura-hover">
            {xh1}
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-full bg-primary-container flex items-center justify-center font-headline font-bold text-surface-container-lowest text-base flex-shrink-0">R</div>
              <div>
                <div class="font-headline font-bold text-on-surface text-sm">Ryan R.</div>
                <div class="text-primary-container text-sm">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              </div>
            </div>
            <p class="text-on-surface-variant text-sm leading-relaxed">&ldquo;The staff here is amazing. Friendly and willing to answer any questions and assist however they can. I purchased a SCCy 9mm and was in and out in less than 30 minutes. I will continue coming back to this store.&rdquo;</p>
          </div>
          <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 p-7 gold-aura-hover">
            {xh2}
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-full bg-primary-container flex items-center justify-center font-headline font-bold text-surface-container-lowest text-base flex-shrink-0">D</div>
              <div>
                <div class="font-headline font-bold text-on-surface text-sm">Dan</div>
                <div class="text-primary-container text-sm">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              </div>
            </div>
            <p class="text-on-surface-variant text-sm leading-relaxed">&ldquo;Found the shop searching for a specific gun. Called up the shop and talked to the guys &mdash; they made it a great experience. Very helpful and the gun was exactly as described. Very pleased with the purchase. A+ from me.&rdquo;</p>
          </div>
        </div>
      </div>
    </section>""".format(xh0=crosshairs(), xh1=crosshairs(), xh2=crosshairs())

    hours_compact = """
    <section class="py-14" style="background:#ffffff;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid sm:grid-cols-2 lg:grid-cols-4 gap-8 items-start">
        <div class="lg:col-span-2">
          {label}
          <h2 class="font-headline font-bold text-headline-lg mt-1" style="color:#111827">Hours &amp; Location</h2>
          <address class="not-italic mt-4" style="color:#4b5563">
            <p class="text-base font-semibold" style="color:#111827">6650 US-10, Ramsey, MN 55303</p>
            <p class="mt-1"><a href="tel:7634274100" class="font-mono text-primary-container hover:underline">(763) 427-4100</a></p>
            <p class="mt-1"><a href="{gmaps}" target="_blank" rel="noopener" class="text-primary-container text-sm hover:underline">Get directions &rarr;</a></p>
          </address>
        </div>
        <div>
          <div class="inline-flex items-center font-mono text-[11px] font-bold tracking-widest uppercase mb-3 px-3 py-1.5" style="background:#facc15;color:#000000">Store Hours</div>
          <table class="w-full font-mono text-sm" style="border:1px solid #e2e8f0">
            <tbody>
              <tr style="border-bottom:1px solid #e2e8f0"><td class="py-2.5 px-4" style="color:#4b5563">Mon &ndash; Fri</td><td class="py-2.5 px-4 text-right" style="color:#111827">10 AM &ndash; 7 PM</td></tr>
              <tr style="border-bottom:1px solid #e2e8f0"><td class="py-2.5 px-4" style="color:#4b5563">Saturday</td><td class="py-2.5 px-4 text-right" style="color:#111827">10 AM &ndash; 5 PM</td></tr>
              <tr><td class="py-2.5 px-4" style="color:#4b5563">Sunday</td><td class="py-2.5 px-4 text-right" style="color:#9ca3af">Closed</td></tr>
            </tbody>
          </table>
        </div>
        <div class="flex flex-col gap-3">
          <div class="inline-flex items-center font-mono text-[11px] font-bold tracking-widest uppercase mb-3 px-3 py-1.5" style="background:#facc15;color:#000000">Find Us</div>
          <a href="{gmaps}" target="_blank" rel="noopener" class="inline-flex items-center gap-2 bg-primary-container font-headline text-xs uppercase px-5 py-3 font-bold tracking-wider gold-hover" style="color:#131316"><span class="material-symbols-outlined text-base">location_on</span>Open in Maps</a>
          <a href="contact.html" class="inline-flex items-center gap-2 font-headline text-xs uppercase px-5 py-3 font-bold tracking-wider" style="border:1px solid #e2e8f0;color:#374151;">Contact &amp; Directions <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
        </div>
      </div>
    </section>""".format(label=label("Visit The Vault"), gmaps=GMAPS)

    body = (nav() + ticker() + hero + trust + store_split + cat_cards + pawn_loan_split + showcase + gold_cta +
            online_cta() + reviews + hours_compact + footer())
    return head(
        "Twin Cities Gun & Pawn | Firearms & Pawn Loans, Twin Cities MN",
        "Hundreds of guns, rifles & accessories in stock in the Twin Cities. Licensed FFL dealer \u2014 $50 transfers & pawn loans since 2010.",
        "",
        "pawn shop Twin Cities MN, gun store Twin Cities, firearms dealer Minnesota, pawn loans Twin Cities, FFL transfer, buy guns Twin Cities, Twin Cities Pawn",
        schema=schema) + body


# ================= ABOUT =================
def page_about():
    story = """
    <section class="py-16" style="background:#ffffff">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid lg:grid-cols-2 gap-12 items-center">
        <div class="relative crosshair-card gold-glow" style="border:1px solid #e2e8f0">
          {xh}
          <img src="images/storefront-exterior.webp" alt="Twin Cities Gun &amp; Pawn storefront exterior in the Twin Cities" class="w-full h-[420px] object-cover" />
        </div>
        <div>
          {label}
          <h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Twin Cities' Trusted Gun &amp; Pawn Shop</h2>
          <div class="mt-5 space-y-4" style="color:#4b5563">
            <p>Twin Cities Gun &amp; Pawn has proudly served the Minneapolis&ndash;St. Paul metro area since 2010. What started as a local pawn shop has grown into one of the region's most trusted destinations for firearms, ammunition, and fair pawn loans.</p>
            <p>We're a fully licensed FFL dealer with hundreds of handguns, rifles, and shotguns in stock at any given time. Whether you're a first-time buyer, a seasoned collector, or you simply need a short-term loan, our knowledgeable staff treats every customer with honesty and respect.</p>
            <p>We believe in giving our neighbors a fair deal. Stop by our Twin Cities location on US-10 and see the difference for yourself.</p>
          </div>
          <a href="contact.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Visit Us <span class="material-symbols-outlined text-base">arrow_outward</span></a>
        </div>
      </div>
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin mt-10 grid grid-cols-1 md:grid-cols-3 gap-6" aria-label="See our store">
          <div class="overflow-hidden" style="border:1px solid #e2e8f0;border-radius:6px"><img src="images/showroom-displays-01b.webp" alt="Shotgun racks and showroom displays inside Twin Cities Gun &amp; Pawn" class="w-full object-cover" style="height:230px" loading="lazy" decoding="async" /></div>
          <div class="overflow-hidden" style="border:1px solid #e2e8f0;border-radius:6px"><img src="images/firearms-showroom-display.webp" alt="Rifle wall and handgun display cases at Twin Cities Gun &amp; Pawn" class="w-full object-cover" style="height:230px" loading="lazy" decoding="async" /></div>
          <div class="overflow-hidden" style="border:1px solid #e2e8f0;border-radius:6px"><img src="images/vibrant-hunting-store-display.webp" alt="Hunting rifles on the wall rack at Twin Cities Gun &amp; Pawn" class="w-full object-cover" style="height:230px" loading="lazy" decoding="async" /></div>
      </div>
    </section>""".format(xh=crosshairs(), label=label("Our Story"))

    stats = """
    <section class="bg-surface-container-lowest border-y border-outline-variant/30">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin grid grid-cols-2 md:grid-cols-4 divide-x divide-outline-variant/20">
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">15+</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Years In Business</div></div>
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">300+</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Firearms In Stock</div></div>
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">Fair</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Pawn Valuations</div></div>
        <div class="py-10 px-4 text-center"><div class="font-mono text-headline-md text-primary-container">100%</div><div class="text-xs uppercase tracking-widest text-on-surface-variant mt-1">Licensed &amp; Legal</div></div>
      </div>
    </section>"""

    reasons = [
        ("verified", "Licensed FFL Dealer", "Fully licensed and compliant with all federal, state, and local firearms laws. Every transaction is handled by the book."),
        ("payments", "Fair Pawn Loans", "Bring in your items and get a fair, honest valuation. We offer short-term loans with no credit check required."),
        ("diversity_3", "Huge Selection", "Hundreds of firearms plus tools, electronics, jewelry, and more. Our inventory changes daily."),
        ("handshake", "Honest &amp; Fair", "Straightforward pricing and respectful service for buyers, sellers, and borrowers alike."),
        ("swap_horiz", "$50 FFL Transfers", "Buying online? We handle incoming FFL transfers for a flat $50 fee."),
        ("storefront", "Local &amp; Trusted", "A Twin Cities fixture since 2010, proudly serving the metro community."),
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
        <div class="mb-10">{label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Twin Cities Largest Used Gun Broker</h2></div>
        {grid}
      </div>
    </section>""".format(label=label("Buy &amp; Sell Guns, Rifles &amp; Shotguns in Minnesota"), grid=grid(reason_cards))

    body = (nav() + ticker() +
            page_hero("about-page-bg.webp", "Inside the Twin Cities Gun &amp; Pawn firearms showroom", "About Us", "About Twin Cities Gun &amp; Pawn", "Licensed FFL dealer &mdash; buying, selling &amp; pawn loans since 2010.") +
            stats + story + why + brands_section() + keyword_entity_table() +
            related_links([
                ("guns-rifles.html", "Guns &amp; Rifles", "Browse hundreds of firearms in stock with $50 FFL transfers."),
                ("pawn-loans.html", "Pawn Loans", "Turn firearms, tools, and valuables into fast collateral loans."),
                ("contact.html", "Visit or Contact Us", "Store hours, directions, and how to reach our Twin Cities, MN shop."),
            ]) + footer())
    return head(
        "About Us | Twin Cities Gun & Pawn \u2014 Twin Cities, MN Since 2010",
        "Learn about Twin Cities Gun & Pawn, the Twin Cities' trusted licensed FFL firearms dealer and pawn shop since 2010. Licensed FFL dealer.",
        "about.html",
        "about Twin Cities Gun and Pawn, gun store history Twin Cities MN, licensed FFL dealer Minnesota, trusted pawn shop",
        ) + body


# ================= GUNS & RIFLES =================
def page_guns():
    chips = filter_bar([
        ("handguns", "Handguns"), ("revolvers", "Revolvers"), ("rifles", "Rifles"),
        ("shotguns", "Shotguns"), ("archery", "Archery"),
    ])

    handguns = inv_section("handguns", "Pistols &amp; Semi-Autos", "Handguns &amp; Pistols",
        "From everyday carry to full-size duty pistols &mdash; Glock, Sig Sauer, Smith &amp; Wesson, Springfield and more.",
        grid([
            inv_card("handgun-display-behind-glass.webp", "Semi-automatic pistols with price tags on glass shelves at Twin Cities Gun &amp; Pawn", "In Stock", "Semi-Auto Pistols", "New &amp; Used"),
            inv_card("handgun-ammo-display.webp", "1911 pistols and ammunition in a display case at Twin Cities Gun &amp; Pawn", "In Stock", "1911 Pistols", "New &amp; Used"),
            inv_card("handgun-display-case-02.webp", "Compact and concealed carry pistols in a lighted counter case at Twin Cities Gun &amp; Pawn", "In Stock", "Concealed Carry Pistols", "New &amp; Used"),
            inv_card("handgun-display-case-01.webp", "Full-size and compact handguns in a lighted counter display case at Twin Cities Gun &amp; Pawn", "In Stock", "Full-Size &amp; Compact Pistols", "New &amp; Used"),
            inv_card("handgun-display-case.webp", "Glass tower showcase of handguns inside Twin Cities Gun &amp; Pawn", "In Stock", "Handgun Showcase", "New &amp; Used"),
        ]))

    revolvers = inv_section("revolvers", "Wheelguns", "Revolvers",
        "Classic and modern revolvers from Smith &amp; Wesson, Ruger, Colt, Taurus and more.",
        grid([
            inv_card("revolvers-store.webp", "Revolver selection at Twin Cities Gun &amp; Pawn, Twin Cities MN", "In Stock", "Double-Action Revolvers", "New &amp; Used", light=True),
            inv_card("revolver-01.webp", "Multiple revolvers on display including single-action and double-action wheelguns", "In Stock", "Concealed Carry Revolvers", "New &amp; Used", light=True),
            inv_card("revolver-single.webp", "Smith &amp; Wesson stainless steel revolver with wood grips", "In Stock", "Magnum Revolvers", "New &amp; Used", light=True),
        ]), bg="white")

    rifles = inv_section("rifles", "Hunting &amp; Tactical", "Hunting &amp; Tactical Rifles",
        "AR-platform rifles, bolt-action hunting rifles, and everything in between from Ruger, Daniel Defense, Remington and more.",
        grid([
            inv_card("rifle-rack-ammo-display.webp", "Rack of hunting rifles above boxes of ammunition at Twin Cities Gun &amp; Pawn", "In Stock", "Hunting Rifles &amp; Ammo", "New &amp; Used", light=True),
            inv_card("vibrant-hunting-store-display.webp", "Bolt-action and lever-action hunting rifles on a wall rack at Twin Cities Gun &amp; Pawn", "In Stock", "Bolt-Action Hunting Rifles", "New &amp; Used", light=True),
            inv_card("hunting-rifle-display-wall.webp", "Wall of wood-stock hunting long guns with price tags at Twin Cities Gun &amp; Pawn", "In Stock", "Hunting Rifle Wall", "New &amp; Used", light=True),
            inv_card("ar-rifles-display.webp", "AR-15 rifles and pistol-caliber carbines on a slatwall display at Twin Cities Gun &amp; Pawn", "In Stock", "AR-Platform &amp; Semi-Auto Rifles", "New &amp; Used", light=True),
            inv_card("tactical-firearms-carousel.webp", "Rotating carousel of AR rifles and tactical shotguns in the Twin Cities Gun &amp; Pawn showroom", "In Stock", "Tactical Rifles &amp; Shotguns", "New &amp; Used", light=True),
        ]), bg="gray")

    shotguns = inv_section("shotguns", "Field &amp; Home Defense", "Shotguns",
        "Pump-action, semi-auto, and over/under shotguns from Mossberg, Remington, Browning and more.",
        grid([
            inv_card("shotguns-02.webp", "Pump-action shotguns with wood stocks laid out with Winchester and Remington ammunition", "In Stock", "We Carry a Variety of Shotguns", "New &amp; Used", light=True),
            inv_card("shotgun-rack-display-01.webp", "Pump-action shotguns with wood, synthetic and camo stocks in a rolling rack at Twin Cities Gun &amp; Pawn", "In Stock", "Pump-Action Shotguns", "New &amp; Used", light=True),
            inv_card("shotgun-rack-camo.webp", "Semi-auto and over/under shotguns with camo and wood stocks in a store rack at Twin Cities Gun &amp; Pawn", "In Stock", "Semi-Auto &amp; Over/Under Shotguns", "New &amp; Used", light=True),
            inv_card("shotgun-rack-display.webp", "Rack of priced shotguns on the sales floor at Twin Cities Gun &amp; Pawn", "In Stock", "Waterfowl &amp; Field Shotguns", "New &amp; Used", light=True),
            inv_card("showroom-displays-01.webp", "Rolling shotgun racks and long-gun wall in the Twin Cities Gun &amp; Pawn showroom", "In Stock", "Shop Our Shotgun Racks In Store", "New &amp; Used", light=True),
        ]), bg="white")

    archery = """
    <section id="archery" data-section="archery" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14 scroll-mt-24">
      <div class="mb-8">{label}<h2 class="font-headline font-bold text-headline-lg text-on-surface">Archery</h2>
        <p class="mt-2 text-on-surface-variant max-w-2xl">Compound bows and archery gear for hunters and target shooters. Selection varies &mdash; call to check current stock.</p></div>
      <div class="grid md:grid-cols-2 gap-6 items-center">
        <div class="grid grid-cols-2 gap-4">
          <div class="crosshair-card relative border border-outline-variant/40 gold-glow archery-frame overflow-hidden">
            {xh}
            <img src="images/archery-bows-01.webp" alt="Compound bows wall display at Twin Cities Gun &amp; Pawn Twin Cities, MN" class="w-full h-full object-cover" />
          </div>
          <div class="crosshair-card relative border border-outline-variant/40 gold-glow archery-frame overflow-hidden">
            {xh}
            <img src="images/archery-bows-02.webp" alt="Compound bows and arrows at Twin Cities Gun &amp; Pawn Twin Cities, MN" class="w-full h-full object-cover" />
          </div>
          <div class="crosshair-card relative border border-outline-variant/40 gold-glow archery-frame overflow-hidden" style="grid-column:span 2 / span 2">
            {xh}
            <img src="images/compound-bow-display-rack.webp" alt="Rotating tree-style rack of compound bows with price tags at Twin Cities Gun &amp; Pawn" class="w-full h-full object-cover" style="object-position:center 35%" loading="lazy" />
          </div>
        </div>
        <div>
          <h3 class="font-headline font-bold text-headline-sm text-on-surface">Compound Bows &amp; Gear</h3>
          <p class="mt-3 text-on-surface-variant">We regularly stock compound bows and archery accessories. Whether you're gearing up for bow season or just getting started, stop in to see what's available.</p>
          <a href="contact.html" class="inline-flex items-center gap-2 mt-6 border border-outline-variant/60 text-on-surface font-headline text-xs uppercase px-6 py-3 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors">Check Availability <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
        </div>
      </div>
    </section>""".format(label=label("Bows &amp; Gear"), xh=crosshairs())





    body = (nav() + ticker() +
            page_hero("guns-rifles-hero.webp", "Winchester ammunition box with classic shotgun and rifle", "Firearms Inventory", "Guns &amp; Rifles", "Hundreds of handguns, rifles, shotguns, revolvers and more in stock. Inventory changes daily &mdash; shop online or visit us in the Twin Cities.") +
            chips + handguns + revolvers + rifles + shotguns + archery +
            online_cta() + cta_band("Can't Find What You're Looking For?", "Our inventory turns over fast and much of it never makes it online. Call us or stop by &mdash; we'll help you find the right firearm.", "Contact Us", "contact.html", bg_img="cta-rifles-bg.webp") +
            related_links([
                ("accessories.html", "Ammo &amp; Accessories", "Ammunition, optics, holsters, magazines and gun safes."),
                ("pawn-loans.html", "FFL Transfers ($50)", "Buy online? Ship it to us for a fast, licensed FFL transfer."),
                ("gun-license-mn.html", "MN Gun License", "What you need to legally buy a firearm in Minnesota."),
            ]) + footer())
    return head(
        "Guns & Rifles for Sale | Twin Cities Gun & Pawn \u2014 Twin Cities, MN",
        "Shop handguns, rifles, shotguns, and revolvers at Twin Cities Gun & Pawn in the Twin Cities. Licensed FFL dealer with hundreds of guns in stock.",
        "guns-rifles.html",
        "guns for sale Twin Cities MN, rifles for sale Minnesota, handguns Twin Cities MN, shotguns, buy firearms, FFL dealer, revolvers Minnesota",
        ) + body


# ================= ACCESSORIES =================
def page_accessories():
    chips = filter_bar([
        ("ammo", "Ammunition"), ("optics", "Optics"), ("holsters", "Holsters"), ("magazines", "Magazines"),
    ])

    ammo = inv_section("ammo", "Rounds &amp; Calibers", "Ammunition &amp; Ammo",
        "Handgun, rifle, and shotgun ammunition in popular calibers. Stock and pricing change frequently &mdash; call for current availability.",
        grid([
            inv_card("bullets-boxes.jpg", "Ammunition boxes in stock at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Handgun &amp; Rifle Ammo", "New &amp; Used"),
            inv_card("bullets-handgun.jpg", "Handgun ammunition at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Pistol Ammo", "New &amp; Used"),
            inv_card("ammo-retail-shelf-display.webp", "Shelves of Winchester, Federal, Sig Sauer and Sellier &amp; Bellot rifle and pistol ammunition at Twin Cities Gun &amp; Pawn", "In Stock", "Hunting &amp; Pistol Ammo Wall", "New"),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"))

    optics = inv_section("optics", "Glass &amp; Electronics", "Sights, Scopes &amp; Optics",
        "Red dots, rifle scopes, thermal and night vision optics to complete your build.",
        grid([
            inv_card("optics-scope.jpg", "Rifle scope at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Rifle Scopes", "New &amp; Used", light=True),
            inv_card("optics-sights.jpg", "Red dot and rifle sights at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Sights &amp; Red Dots", "New &amp; Used", light=True),
            inv_card("optics-scope-kit.jpg", "Scope kit with mounts at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Scope Kits &amp; Mounts", "New &amp; Used", light=True),
            inv_card("retail-optics-accessories-display.webp", "Glass case of rifle scopes, rangefinders and binoculars at Twin Cities Gun &amp; Pawn", "In Stock", "Scopes, Rangefinders &amp; Binoculars", "New &amp; Used", light=True),
            inv_card("bright-hunting-gear-display.webp", "Display case of rifle scopes, binoculars, fishing reels and gun cleaning kits at Twin Cities Gun &amp; Pawn", "In Stock", "Hunting Gear &amp; Cleaning Kits", "New &amp; Used", light=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"), bg="white")

    holsters = inv_section("holsters", "Carry &amp; Storage", "Holsters &amp; Slings",
        "Concealed carry holsters and rifle slings to keep your firearm secure and accessible.",
        grid([
            inv_card("holsters-owb.jpg", "OWB holsters for pistols at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "OWB Holsters", "New", light=True),
            inv_card("holsters-iwb.jpg", "IWB concealed carry holsters at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "IWB Holsters", "New", light=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"), bg="gray")

    magazines = inv_section("magazines", "Feed &amp; Secure", "Magazines",
        "Factory and aftermarket pistol and rifle magazines.",
        grid([
            inv_card("magazines-pistol.jpg", "Pistol magazines at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Pistol Magazines", "New &amp; Used", light=True),
            inv_card("magazines-rifle.jpg", "Rifle magazines at Twin Cities Gun &amp; Pawn Twin Cities, MN", "In Stock", "Rifle Magazines", "New &amp; Used", light=True),
        ], cols="sm:grid-cols-2 lg:grid-cols-3"), bg="white")

    body = (nav() + ticker() +
            page_hero("accessories-hero.webp", "Leupold rifle scope mounted on precision firearm", "Gear &amp; Accessories", "Accessories &amp; Ammo", "Ammunition, optics, holsters, magazines, safes and more &mdash; everything you need to run and maintain your firearms.") +
            chips + ammo + optics + holsters + magazines +
            cta_band("Need Something Specific?", "We stock far more than we can list online. Give us a call and we'll let you know what's in stock or help you order it.", "Contact Us", "contact.html", bg_img="cta-rifles-bg.webp") +
            online_cta() +
            related_links([
                ("guns-rifles.html", "Guns &amp; Rifles", "300+ handguns, rifles and shotguns in stock in the Twin Cities."),
                ("pawn-loans.html", "Pawn &amp; Loans", "Pawn your items or shop our store &mdash; firearms, tools, electronics &amp; more."),
                ("contact.html", "Visit The Store", "6650 US-10, Ramsey, MN &mdash; hours, map and directions."),
            ]) + footer())
    return head(
        "Ammo & Firearm Accessories | Twin Cities Gun & Pawn, Twin Cities MN",
        "Ammunition, optics, holsters, magazines, and gun safes at Twin Cities Gun & Pawn in the Twin Cities. Everything you need for your firearms in one place.",
        "accessories.html",
        "ammunition Twin Cities MN, ammo for sale Minnesota, rifle scopes, holsters, magazines, gun safes, firearm accessories Twin Cities",
        ) + body


# ================= PAWN & LOANS =================
def page_pawn():
    featured = """
    <section id="pawn" data-section="pawn" class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 scroll-mt-24">
      <div class="grid lg:grid-cols-2 gap-6">
        <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 overflow-hidden gold-glow p-10 md:p-14">
          {xh}
          {label}
          <h2 class="font-headline font-bold text-headline-xl-mobile md:text-headline-xl text-on-surface">Pawn Your Items</h2>
          <p class="mt-4 text-on-surface-variant">Bring in your firearms, tools, electronics or jewelry. Get a fast, fair valuation and walk out with cash. No credit check needed &mdash; your item is the collateral.</p>
          <ul class="mt-6 space-y-3 text-on-surface-variant">
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Firearms, tools, electronics, jewelry &amp; more</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>No credit check required</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Fair, honest valuations every time</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Reclaim your item when you repay</li>
          </ul>
          <a href="contact.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">Get a Loan Quote <span class="material-symbols-outlined text-base">arrow_outward</span></a>
        </div>
        <div class="crosshair-card relative bg-surface-container-low border border-outline-variant/40 overflow-hidden gold-glow p-10 md:p-14">
          {xh2}
          <h2 class="font-headline font-bold text-headline-xl-mobile md:text-headline-xl text-on-surface">Shop Our Store</h2>
          <p class="mt-4 text-on-surface-variant">Looking to buy? Browse hundreds of firearms, tools, electronics, jewelry and more. Stop in to see our rotating inventory or call to check current availability.</p>
          <ul class="mt-6 space-y-3 text-on-surface-variant">
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>300+ firearms in stock</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Tools, electronics, jewelry &amp; collectibles</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Rotating inventory &mdash; new items daily</li>
            <li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary-container text-lg">check_circle</span>Competitive prices, honest deals</li>
          </ul>
          <a href="guns-rifles.html" class="inline-flex items-center gap-2 mt-8 bg-primary-container text-surface-container-lowest font-headline text-sm uppercase px-7 py-3.5 font-bold tracking-wider gold-hover">See Our Inventory <span class="material-symbols-outlined text-base">arrow_outward</span></a>
        </div>
      </div>
    </section>""".format(xh=crosshairs(), label=label("Pawn Your Items"), xh2=crosshairs())

    ffl = """
    <div style="background:#ffffff;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0;">
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-10">
      <div class="crosshair-card relative border border-slate-200 bg-white p-8 md:p-10 gold-aura-hover grid md:grid-cols-[auto_1fr_auto] gap-6 items-center">
        {xh}
        <span class="material-symbols-outlined text-primary-container text-5xl">swap_horiz</span>
        <div>
          <h3 class="font-headline font-bold text-headline-sm" style="color:#131316;">$50 FFL Transfers</h3>
          <p class="text-sm mt-2 max-w-2xl" style="color:#4b5563;">Bought a firearm online? We handle incoming FFL transfers for a flat <span class="font-mono text-primary-container">$50</span> fee. Have it shipped to us and we'll take care of the paperwork and background check.</p>
        </div>
        <a href="contact.html" class="inline-flex items-center gap-2 border border-slate-300 font-headline text-xs uppercase px-6 py-3 font-bold tracking-wider hover:border-primary-container hover:text-primary-container transition-colors whitespace-nowrap" style="color:#131316;">Start a Transfer <span class="material-symbols-outlined text-sm">arrow_outward</span></a>
      </div>
    </section>
    </div>""".format(xh=crosshairs())

    photo_grid = """
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-12">
      <h2 class="font-headline font-bold text-headline-md text-on-surface mb-2">What We Buy &amp; Sell</h2>
      <p class="text-on-surface-variant text-sm mb-8">Rotating inventory &mdash; stop in or call to check current stock.</p>
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-3">
        <div class="relative overflow-hidden group">
          <img src="images/pawn-tools.jpg" alt="Power tools at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Power Tools</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-tvs.jpg" alt="TVs and electronics at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">TVs &amp; Electronics</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-speakers.jpg" alt="Speakers and audio at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Audio &amp; Speakers</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-instruments.jpg" alt="Musical instruments at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Instruments</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-jewelry.jpg" alt="Jewelry and watches at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Jewelry &amp; Watches</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-jewelry-01.jpg" alt="Gold and diamond jewelry at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Gold &amp; Diamonds</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-knives.jpg" alt="Knives and collectibles at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Knives &amp; Collectibles</span></div>
        </div>
        <div class="relative overflow-hidden group">
          <img src="images/pawn-bikes.jpg" alt="Bikes and sporting goods at Twin Cities Gun &amp; Pawn" class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy" />
          <div class="absolute bottom-0 inset-x-0 bg-black/60 px-3 py-2"><span class="font-headline font-bold text-sm text-white">Bikes &amp; Sporting Goods</span></div>
        </div>
      </div>
    </section>"""

    body = (nav() + ticker() +
            page_hero("pawn-tools.jpg", "Pawn shop merchandise at Twin Cities Gun & Pawn", "Pawn &amp; Loans", "Pawn &amp; Loans", "Licensed FFL dealer. Fair loans, honest valuations, and a rotating selection of tools, electronics, jewelry and more.") +
            featured + ffl + photo_grid +
            cta_band("Have Something to Pawn or Sell?", "Bring it in for a free, no-obligation valuation. We loan on and buy firearms, tools, electronics, jewelry, and more.", "Get a Quote", "contact.html", bg_img="cta-rifles-bg.webp") +
            related_links([
                ("rules-for-pawning.html", "Rules for Pawning a Gun", "Minnesota pawn laws, ID requirements and hold periods."),
                ("guns-rifles.html", "Shop Firearms", "Browse 300+ guns, rifles and shotguns in stock."),
                ("faq-gun-pawns.html", "Gun Pawn FAQ", "Answers to common questions about pawning firearms."),
            ]) +
            footer())
    return head(
        "Pawn Your Items or Shop Our Store | Twin Cities Gun & Pawn, MN",
        "Pawn your firearms, tools, electronics or jewelry at Twin Cities Gun & Pawn in the Twin Cities. Fair valuations, no credit check. Plus $50 FFL transfers and a huge rotating inventory.",
        "pawn-loans.html",
        "pawn shop Twin Cities MN, pawn items Minnesota, FFL transfer $50, sell jewelry Twin Cities, pawn tools electronics, gold buyer Twin Cities, shop inventory Twin Cities",
        ) + body


# ================= CONTACT =================
def page_contact():
    form = """
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 grid lg:grid-cols-2 gap-12">
      <div>
        {label}
        <h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Send Us a Message</h2>
        <p class="mt-2" style="color:#4b5563">Questions about inventory, pawn loans, or FFL transfers? Fill out the form and we'll get back to you. For fastest service, give us a call.</p>
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
    </section>
    </div>""".format(label=label("Get In Touch"), xh=crosshairs(), gmaps=GMAPS)

    body = (nav() + ticker() +
            page_hero("contact-hero.webp", "Glock pistol and AR-15 rifle laid out on dark surface — Twin Cities Gun &amp; Pawn contact", "Contact", "Contact Us", "Stop by, call, or send us a message. We're here to help with firearms, pawn loans, and FFL transfers.") +
            form + online_cta() +
            related_links([
                ("guns-rifles.html", "Guns &amp; Rifles", "See what's in stock before you stop by the shop."),
                ("pawn-loans.html", "Pawn Loans", "How collateral loans work and what we accept."),
                ("faq.html", "FAQ", "Quick answers about hours, transfers, and buying."),
            ]) + footer())
    return head(
        "Contact Us | Twin Cities Gun & Pawn \u2014 Twin Cities, MN | (763) 427-4100",
        "Contact Twin Cities Gun & Pawn in the Twin Cities. Visit us at 6650 US-10, call (763) 427-4100, or send a message. Open Mon\u2013Fri 10\u20137, Sat 10\u20135.",
        "contact.html",
        "contact Twin Cities Pawn, gun store Twin Cities MN phone, pawn shop directions Twin Cities, 6650 US-10, firearms dealer contact Twin Cities",
        ) + body


# ================= LEGAL / MINIMAL PAGES =================
def legal_page(canon, title, meta_desc, keywords, label_text, h1, sub, content_html):
    body = (nav() + ticker() +
            text_hero(label_text, h1, sub) +
            """
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="prose-legal space-y-6" style="color:#374151">
        {content}
      </div>
    </section>
    </div>""".format(content=content_html) +
            footer())
    return head(title, meta_desc, canon, keywords) + body


def info_page(canon, title, meta_desc, keywords, hero_img, hero_alt, label_text, h1, sub, content_html, quick_facts=None, related=None, author_topic=None):
    """Info page: hero + quick-facts bar + full-width dark numbered content. No sidebar.

    `related` = optional list of (href, label, desc) tuples rendered as a contextual
    'Related Pages' interlinking module before the footer (internal-linking / indexing).
    """
    import re

    counter_val = [0]
    def replace_h2(m):
        counter_val[0] += 1
        n = counter_val[0]
        return (
            '<div class="guide-section" id="s%d">'
            '<span class="guide-num">%02d</span>'
            '<h2 class="guide-h2 font-headline font-bold">%s</h2>'
            '</div>' % (n, n, m.group(2))
        )
    anchored = re.sub(r'<h2([^>]*)>(.*?)</h2>', replace_h2, content_html, flags=re.DOTALL)

    qf = ""
    if quick_facts:
        facts_html = "".join(
            '<div class="flex items-center gap-2">'
            '<span class="material-symbols-outlined text-primary-container text-base flex-shrink-0">check_circle</span>'
            '<span class="text-sm" style="color:#e5e7eb">%s</span></div>' % f
            for f in quick_facts
        )
        qf = """
    <div style="background:#1b1b1e;border-bottom:1px solid #2e2c28">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-5 flex flex-wrap gap-x-8 gap-y-3">%s</div>
    </div>""" % facts_html

    author_block = guide_author(author_topic) if author_topic else ""
    body = (nav() + ticker() +
            page_hero(hero_img, hero_alt, label_text, h1, sub) +
            qf +
            author_block +
            """
    <div style="background:#131316">
      <div class="max-w-[860px] mx-auto px-6 lg:px-margin py-16">
        <div class="guide-article-dark">%s</div>
      </div>
    </div>""" % anchored +
            (related_links(related) if related else "") +
            footer())
    return head(title, meta_desc, canon, keywords) + body


def h3(t):
    return '<h2 class="font-headline font-bold text-headline-sm mt-8 mb-2" style="color:#111827">%s</h2>' % t


def p(t):
    return '<p>%s</p>' % t


def guide_author(topic_label="Firearms &amp; MN Law"):
    """E-E-A-T author byline displayed above guide body content to establish expertise &amp; trust."""
    return """
    <div style="background:#f0f4f8;border-top:3px solid #facc15;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[880px] mx-auto px-6 lg:px-margin py-5 flex flex-col sm:flex-row sm:items-center gap-4">
        <div class="flex items-center gap-4 flex-1">
          <div class="w-12 h-12 flex-shrink-0 flex items-center justify-center" style="background:#111827;border:2px solid #facc15">
            <span class="material-symbols-outlined text-2xl" style="color:#facc15">badge</span>
          </div>
          <div>
            <div class="font-mono text-[10px] uppercase tracking-widest mb-0.5" style="color:#6c5700">Expert Guide</div>
            <div class="font-headline font-bold text-sm" style="color:#111827">Twin Cities Gun &amp; Pawn Staff</div>
            <div class="text-xs" style="color:#4b5563">Licensed FFL Dealer &bull; Serving the Twin Cities, MN since 2010 &bull; {topic}</div>
          </div>
        </div>
        <div class="flex flex-wrap gap-2 flex-shrink-0">
          <span class="inline-flex items-center gap-1 font-mono text-[10px] font-bold uppercase tracking-wider px-2.5 py-1.5" style="background:#facc15;color:#000000"><span class="material-symbols-outlined text-xs">verified</span>&nbsp;FFL Licensed</span>
          <span class="inline-flex items-center gap-1 font-mono text-[10px] font-bold uppercase tracking-wider px-2.5 py-1.5" style="border:1px solid #d1d5db;color:#374151"><span class="material-symbols-outlined text-xs">history_edu</span>&nbsp;Est. 2010</span>
        </div>
      </div>
    </div>""".format(topic=topic_label)


def page_terms():
    c = "".join([
        p("Welcome to Twin Cities Gun &amp; Pawn. By accessing or using our website and services, you agree to the following terms and conditions. Please read them carefully."),
        h3("1. Firearms Sales &amp; Compliance"),
        p("All firearm sales and transfers comply with federal, state, and local laws. A valid government-issued photo ID and a successful background check are required for all firearm purchases and transfers. We reserve the right to refuse any sale or transfer at our discretion, as permitted by law."),
        h3("2. FFL Transfers"),
        p("Incoming FFL transfers are handled for a flat $50 fee per firearm. The buyer is responsible for ensuring the firearm is legal to own in their jurisdiction. All standard background check and identification requirements apply."),
        h3("3. Pawn Loans"),
        p("Pawn loans are subject to a written pawn agreement provided at the time of the transaction. Items are held as collateral and may be reclaimed upon repayment within the agreed term. Failure to repay within the term may result in forfeiture of the pledged item."),
        h3("4. Inventory &amp; Pricing"),
        p("Inventory and pricing are subject to change without notice. Items shown online or in-store may sell quickly and availability is not guaranteed. Photographs are for illustration and may not depict the exact item in stock."),
        h3("5. Limitation of Liability"),
        p("Twin Cities Gun &amp; Pawn is not liable for any indirect, incidental, or consequential damages arising from the use of our website or services, to the fullest extent permitted by law."),
        h3("6. Changes to These Terms"),
        p("We may update these terms from time to time. Continued use of our website constitutes acceptance of any changes."),
        h3("Contact"),
        p('Questions about these terms? Contact us at <a href="tel:7634274100" class="text-primary-container hover:underline">(763) 427-4100</a> or visit us at 6650 US-10, Ramsey, MN 55303.'),
    ])
    return legal_page("terms.html", "Terms & Conditions | Twin Cities Gun & Pawn",
        "Terms and conditions for Twin Cities Gun & Pawn in the Twin Cities, including firearms sales compliance, FFL transfers, and pawn loan policies.",
        "terms and conditions, Twin Cities Pawn policies, firearms sale terms, pawn loan terms",
        "Legal", "Terms &amp; Conditions", "Last updated 2026. Please review these terms governing the use of our website and services.", c)


def page_privacy():
    c = "".join([
        p("Twin Cities Gun &amp; Pawn respects your privacy. This policy explains what information we collect and how we use it."),
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
    return legal_page("privacy.html", "Privacy Policy | Twin Cities Gun & Pawn",
        "Privacy policy for Twin Cities Gun & Pawn in the Twin Cities. Learn what information we collect and how we protect it.",
        "privacy policy, Twin Cities Pawn privacy, data protection pawn shop",
        "Legal", "Privacy Policy", "How we collect, use, and protect your information.", c)


def page_equal():
    c = "".join([
        p("Twin Cities Gun &amp; Pawn is an Equal Opportunity Employer. We are committed to providing a workplace free of discrimination and harassment."),
        p("We do not discriminate on the basis of race, color, religion, sex, sexual orientation, gender identity, national origin, age, disability, veteran status, genetic information, or any other characteristic protected by federal, state, or local law."),
        h3("Our Commitment"),
        p("All employment decisions &mdash; including hiring, promotion, compensation, and termination &mdash; are based on merit, qualifications, and business needs. We are committed to fostering an inclusive environment where every team member is treated with dignity and respect."),
        h3("Employment Inquiries"),
        p('Interested in joining our team? Stop by 6650 US-10, Ramsey, MN 55303, or call <a href="tel:7634274100" class="text-primary-container hover:underline">(763) 427-4100</a>.'),
    ])
    return legal_page("equal-opportunity.html", "Equal Opportunity Employer | Twin Cities Gun & Pawn",
        "Twin Cities Gun & Pawn is an Equal Opportunity Employer committed to a workplace free of discrimination.",
        "equal opportunity employer, Twin Cities Pawn careers, non-discrimination policy",
        "Careers", "Equal Opportunity Employer", "Our commitment to a fair and inclusive workplace.", c)


def page_faq():
    faqs = [
        ("Do you offer pawn loans?", "Yes! We offer fair, short-term pawn loans against items of value including firearms, tools, electronics, and jewelry. No credit check required &mdash; your item serves as collateral. Stop in or call for current terms and a free valuation."),
        ("How much do FFL transfers cost?", "We handle incoming FFL transfers for a flat $50 fee per firearm. Have your online purchase shipped to us and we'll take care of the paperwork and background check."),
        ("What do I need to buy a firearm?", "You'll need a valid government-issued photo ID and must pass a background check. All sales comply with federal, state, and local laws. Certain items may have additional requirements."),
        ("What are your hours?", "We're open Monday through Friday from 10 AM to 7 PM, Saturday from 10 AM to 5 PM, and closed on Sunday."),
        ("Where are you located?", "We're at 6650 US-10, Ramsey, MN 55303, conveniently serving the Minneapolis\u2013St. Paul metro area."),
        ("Can I see your inventory online?", "Yes &mdash; browse our listings on Armslist and GunBroker via the links on our site. Note that much of our inventory is in-store only and turns over quickly, so call us to check availability."),
        ("Do you buy items?", "Absolutely. We buy firearms, tools, electronics, jewelry, and more. Bring your item in for a free, no-obligation valuation."),

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
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="space-y-4">{items}</div>
    </section>
    </div>""".format(items="".join(items))
    body = (nav() + ticker() +
            text_hero("Help Center", "Frequently Asked Questions", "Answers to common questions about our firearms, pawn loans, transfers, and store.") +
            content +
            cta_band("Still Have Questions?", "We're happy to help. Give us a call or stop by the store and our team will get you sorted.", "Contact Us", "contact.html") +
            related_links([
                ("faq-gun-pawns.html", "Gun Pawn FAQ", "In-depth answers about pawning firearms in Minnesota."),
                ("pawn-loans.html", "Pawn Loans", "How collateral loans work and what we accept."),
                ("guns-rifles.html", "Guns &amp; Rifles", "Browse our firearm inventory and FFL transfer service."),
            ]) + footer())
    return head("FAQ | Twin Cities Gun & Pawn \u2014 Twin Cities, MN",
        "Frequently asked questions about Twin Cities Gun & Pawn: pawn loans, FFL transfers, buying firearms, hours, location, and more.",
        "faq.html",
        "pawn shop FAQ, FFL transfer questions, buy gun requirements Minnesota, pawn loan questions, Twin Cities Pawn hours",
        ) + body


def page_sitemap():
    links = [
        ("/", "Home"), ("about.html", "About Us"),
        ("guns-rifles.html", "Guns &amp; Rifles"), ("guns-rifles.html#handguns", "&rsaquo; Handguns &amp; Pistols"),
        ("guns-rifles.html#revolvers", "&rsaquo; Revolvers"), ("guns-rifles.html#rifles", "&rsaquo; Rifles"),
        ("guns-rifles.html#shotguns", "&rsaquo; Shotguns"), ("guns-rifles.html#archery", "&rsaquo; Archery"),
        ("accessories.html", "Accessories &amp; Ammo"), ("accessories.html#ammo", "&rsaquo; Ammunition"),
        ("accessories.html#optics", "&rsaquo; Optics"), ("accessories.html#holsters", "&rsaquo; Holsters"),
        ("accessories.html#magazines", "&rsaquo; Magazines"),
        ("pawn-loans.html", "Pawn &amp; Loans"), ("pawn-loans.html#pawn", "&rsaquo; Pawn Your Items"),
        ("pawn-loans.html#tools", "&rsaquo; Power Tools"), ("pawn-loans.html#electronics", "&rsaquo; Electronics"),
        ("pawn-loans.html#jewelry", "&rsaquo; Jewelry &amp; Gold"),
        ("/gallery", "Store Gallery"),
        ("contact.html", "Contact"), ("faq.html", "FAQ"),
        ("faq-gun-pawns.html", "FAQ &ndash; Gun Pawns"), ("employment.html", "Employment"),
        ("resources.html", "Resources"), ("gun-law-checklist.html", "&rsaquo; 2026 Gun Law Checklist"),
        ("rules-for-pawning.html", "&rsaquo; Rules for Pawning a Gun"),
        ("gun-license-mn.html", "&rsaquo; Gun License in Minnesota"), ("unregistered-gun.html", "&rsaquo; Unregistered Firearms"),
        ("terms.html", "Terms &amp; Conditions"), ("privacy.html", "Privacy Policy"),
        ("equal-opportunity.html", "Equal Opportunity Employer"),
    ]
    lis = "".join('<li><a href="%s" class="hover:text-primary-container transition-colors" style="color:#374151">%s</a></li>' % (h, t) for h, t in links)
    content = """
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <ul class="space-y-3 text-lg">%s</ul>
      <div class="mt-10 border-t border-outline-variant/20 pt-6">
        <div class="inline-flex items-center font-mono text-[10px] font-bold uppercase tracking-widest mb-3 px-3 py-1.5" style="background:#facc15;color:#000000">Shop Online</div>
        <ul class="space-y-3 text-lg">
          <li><a href="%s" target="_blank" rel="noopener" class="hover:text-primary-container" style="color:#374151">Armslist Store &nearr;</a></li>
          <li><a href="%s" target="_blank" rel="noopener" class="hover:text-primary-container" style="color:#374151">GunBroker Listings &nearr;</a></li>
        </ul>
      </div>
    </section>
    </div>""" % (lis, ARMSLIST, GUNBROKER)
    body = (nav() + ticker() +
            text_hero("Navigation", "Sitemap", "Every page on the Twin Cities Gun &amp; Pawn website, all in one place.") +
            content + footer())
    return head("Sitemap | Twin Cities Gun & Pawn \u2014 Twin Cities, MN",
        "Full sitemap of the Twin Cities Gun & Pawn website \u2014 firearms, accessories, pawn loans, and more.",
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
        ("Can I pawn a firearm in Minnesota?", "Yes. Twin Cities Gun &amp; Pawn is a licensed FFL dealer and we regularly accept firearms as collateral for pawn loans. You must be the legal owner, at least 18 (21 for handguns), and pass identity verification. Prohibited persons under federal or Minnesota law cannot pawn a firearm."),
        ("What ID do I need to pawn a gun?", "You'll need a valid, unexpired government-issued photo ID such as a Minnesota driver's license or state ID. We record the transaction as required by state pawn regulations and federal firearms law."),
        ("How do you determine how much my gun is worth?", "Our firearms specialists evaluate make, model, caliber, condition, age, included accessories, and current market demand. We aim to offer a fair loan value and will explain how we arrived at the figure."),
        ("What are the loan terms?", "Pawn loans are short-term and outlined in a written pawn ticket you receive at the time of the transaction. Ask our team about current terms, the redemption period, and how to extend a loan."),
        ("How do I get my firearm back?", "Repay the loan amount according to the terms on your pawn ticket within the redemption period. Because a firearm is being returned to you, you must again pass a background check and complete the required federal paperwork before we can release it."),
        ("Do I need a background check to reclaim my gun?", "Yes. Under federal law, returning a pawned firearm to its owner is treated as a transfer, so a NICS background check and ATF Form 4473 are required before the firearm can be handed back."),
        ("What happens if I don't repay the loan?", "If the loan isn't repaid or extended within the agreed period, the firearm is forfeited and becomes store inventory, which we may sell in compliance with all applicable laws. You are never obligated to repay &mdash; the item is the collateral."),
        ("Can I pawn a firearm that isn't registered to me?", "Minnesota does not maintain a general firearm registry, but you must be the lawful owner of any item you pawn. We cannot accept stolen property, and knowingly pawning a firearm you don't own is a crime."),
        ("Are there firearms you won't accept?", "We cannot accept firearms that are stolen, illegally modified, have obliterated serial numbers, or that we're prohibited from handling under federal or state law. NFA items have additional requirements &mdash; ask our staff."),
        ("Is my information kept private?", "We collect only what's required by law for firearms and pawn transactions and handle it in accordance with applicable regulations and our privacy policy. We do not sell your personal information."),
    ]
    content = """
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[880px] mx-auto px-6 lg:px-margin py-16">
      <div class="space-y-4">{items}</div>
    </section>
    </div>""".format(items=faq_accordion(faqs))
    body = (nav() + ticker() +
            text_hero("Help Center", "FAQ &ndash; Gun Pawns", "Everything you need to know about pawning a firearm at Twin Cities Gun &amp; Pawn in the Twin Cities.") +
            content +
            cta_band("Ready to Pawn Your Firearm?", "Stop by with a valid photo ID for a free, no-obligation valuation, or call us with any questions.", "Contact Us", "contact.html") +
            related_links([
                ("rules-for-pawning.html", "Rules for Pawning a Gun", "ID, valuation, hold periods, and reclaiming a pawned firearm."),
                ("pawn-loans.html", "Pawn Loans", "How collateral loans work at our Twin Cities, MN shop."),
                ("gun-license-mn.html", "Gun License in Minnesota", "Permits and background checks for buying or carrying."),
            ]) + footer())
    return head("Gun Pawn FAQ | Twin Cities Gun & Pawn | Twin Cities, MN",
        "Answers to common questions about pawning firearms in Minnesota: required ID, valuations, loan terms, background checks, and reclaiming your gun.",
        "faq-gun-pawns.html",
        "pawn a gun Minnesota, gun pawn FAQ, firearm pawn loan Twin Cities MN, how to pawn a firearm, get pawned gun back",
        ) + body


def page_employment():
    positions = ["Sales Associate", "Firearms Specialist", "Pawn Specialist", "Manager", "Other"]
    opts = "".join("<option>%s</option>" % pos for pos in positions)
    form = """
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16 grid lg:grid-cols-2 gap-12">
      <div>
        {label}
        <h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Why Work With Us</h2>
        <div class="mt-5 space-y-4" style="color:#374151">
          <p>Twin Cities Gun &amp; Pawn has been a Twin Cities fixture since 2010, and our team is the reason customers keep coming back. We're looking for friendly, honest, hard-working people who enjoy helping others.</p>
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
    </section>
    </div>""".format(label=label("Careers"), xh=crosshairs(), opts=opts)
    body = (nav() + ticker() +
            page_hero("pawn-counter-guitars.webp", "Inside Twin Cities Gun & Pawn store", "Careers", "Join Our Team", "Twin Cities Gun &amp; Pawn is always looking for great people. Apply below to become part of our Twin Cities crew.") +
            form +
            related_links([
                ("about.html", "About Us", "Our story as the Twin Cities' trusted FFL dealer since 2010."),
                ("equal-opportunity.html", "Equal Opportunity Employer", "Our commitment to a fair and inclusive workplace."),
                ("contact.html", "Contact Us", "Store hours, directions, and how to reach our team."),
            ]) + footer())
    return head("Employment Application | Twin Cities Gun & Pawn | Twin Cities, MN",
        "Apply to join the team at Twin Cities Gun & Pawn in the Twin Cities. We're hiring sales associates, firearms specialists, pawn specialists, and more.",
        "employment.html",
        "Twin Cities Pawn jobs, gun store jobs Twin Cities MN, pawn shop employment Minnesota, firearms specialist job, apply now",
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
          <a href="https://www.house.mn.gov/hrd/pubs/firearms.pdf" target="_blank" rel="noopener" class="flex items-center gap-3 hover:text-primary-container transition-colors" style="color:#4b5563">
            <span class="material-symbols-outlined text-lg">description</span>
            <span>Minnesota House Research: Firearms Laws (PDF) &nearr;</span>
          </a>
          <a href="https://www.revisor.mn.gov/statutes/cite/624.714" target="_blank" rel="noopener" class="flex items-center gap-3 hover:text-primary-container transition-colors" style="color:#4b5563">
            <span class="material-symbols-outlined text-lg">gavel</span>
            <span>MN Statute 624.714: Carry Permit &nearr;</span>
          </a>
        </div>
      </div>
    </section>"""
    
    content = """
    <div style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
    <section class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">
      <p class="max-w-2xl mb-10" style="color:#4b5563">Firearms and pawn transactions come with important rules and responsibilities. We've put together plain-English guides to help you understand Minnesota law and shop with confidence. Explore the resources below.</p>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">{cards}</div>
    </section>
    {ext}
    </div>""".format(cards="".join(card_html), ext=external_links)
    body = (nav() + ticker() +
            text_hero("Know Before You Go", "Resources", "Helpful guides on pawning firearms, Minnesota gun licensing, firearm registration law, and current gun safety laws.") +
            content +
            cta_band("Still Have Questions?", "Our knowledgeable staff is happy to walk you through the details. Give us a call or stop in.", "Contact Us", "contact.html") +
            footer())
    return head("Resources | Twin Cities Gun & Pawn | Twin Cities, MN",
        "Gun law resources from Twin Cities Gun & Pawn: 2026 checklist, MN gun licensing, rules for pawning a firearm, and firearm registration law explained.",
        "resources.html",
        "gun pawn resources, Minnesota firearm law, gun license guide, pawn a gun rules, Twin Cities Pawn resources, 2026 gun laws",
        ) + body


def page_rules_for_pawning():
    c = "".join([
        p('Pawning a firearm can be a fast, discreet way to get a short-term <a href="pawn-loans.html" class="text-primary-container hover:underline font-semibold">pawn loan</a> using something you already own. But because firearms are involved, the process is governed by both federal and Minnesota law. Here\'s what you need to know before you visit Twin Cities Gun &amp; Pawn.'),
        h3("Who Can Pawn a Firearm"),
        p("You must be the lawful owner of the firearm and legally allowed to possess it. You must be at least 18 years old for long guns and 21 for handguns. Individuals prohibited from possessing firearms under federal or Minnesota law &mdash; including certain felony convictions, domestic-violence orders, or adjudications &mdash; cannot pawn a firearm."),
        h3("What to Bring"),
        p("Bring a valid, unexpired government-issued photo ID (such as a Minnesota driver's license or state ID) and the firearm itself, unloaded and cased if possible. Any accessories, cases, or original boxes can increase the loan value. We'll record the transaction as required by state pawn regulations."),
        h3("How Valuation Works"),
        p("Our firearms specialists assess the make, model, caliber, condition, age, market demand, and any included accessories. We'll explain how we arrived at your offer. Our goal is a fair deal &mdash; ask about current loan terms and redemption periods."),
        h3("The Hold &amp; Redemption Period"),
        p("When you pawn an item you receive a written pawn ticket that spells out the loan amount, fees, and the redemption period during which you can repay and reclaim your firearm. Your firearm is stored securely for the duration of the loan. Minnesota pawn shops are also required to report transactions to help law enforcement identify stolen property, which typically involves a short investigatory hold on incoming items."),
        h3("Reclaiming Your Firearm"),
        p("To get your firearm back, repay the loan according to your pawn ticket within the redemption period. Because handing a firearm back to its owner is legally a transfer, federal law requires you to complete an ATF Form 4473 and pass a NICS background check before the firearm can be released &mdash; even though it's your own gun."),
        h3("What Happens If You Don't Redeem"),
        p("A pawn loan is non-recourse: if you choose not to repay, you simply forfeit the firearm, which becomes store inventory that we may sell in full compliance with the law. There's no impact on your credit and no further obligation."),
        h3("Firearms We Cannot Accept"),
        p("We cannot accept stolen firearms, guns with obliterated or altered serial numbers, illegally modified firearms, or any item we're prohibited from handling. NFA-regulated items such as suppressors and short-barreled rifles carry additional federal requirements &mdash; talk to our staff about the specifics."),
        h3("FFL Considerations"),
        p("Twin Cities Gun &amp; Pawn is a fully licensed FFL dealer, so every firearm transaction &mdash; including pawns and redemptions &mdash; is handled by the book with the proper paperwork and background checks. This protects both you and the shop."),
        p('<span class="text-outline text-sm">This page is provided for general informational purposes and reflects our understanding of applicable rules; it is not legal advice. Laws change &mdash; contact us or a qualified attorney for guidance on your situation.</span>'),
    ])
    return info_page("rules-for-pawning.html", "Rules for Pawning a Gun in Minnesota | Twin Cities Gun & Pawn",
        "A plain-English guide to pawning a firearm in Minnesota: who qualifies, what ID to bring, how valuation works, hold periods, and reclaiming your gun.",
        "rules for pawning a gun, pawn a firearm Minnesota, gun pawn requirements Twin Cities MN, how to pawn a gun, reclaim pawned firearm",
        "rules-pawning-hero.webp", "Vintage revolver with wood grips on wooden surface", 
        "Guide", "Rules for Pawning a Gun", "What you need to know before pawning a firearm in Minnesota.", c,
        quick_facts=["Valid government photo ID required", "18+ for long guns &mdash; 21+ for handguns", "ATF Form 4473 required on redemption", "Non-recourse loan &mdash; no credit impact if you forfeit"],
        related=[
            ("pawn-loans.html", "Pawn Loans", "How collateral loans work at our Twin Cities, MN shop."),
            ("gun-license-mn.html", "Gun License in Minnesota", "Permits, background checks, and buying or carrying legally."),
            ("faq-gun-pawns.html", "Gun Pawn FAQ", "Answers to the most common questions about pawning firearms."),
        ],
        author_topic="Pawn Regulations &amp; Firearm Law")


def page_gun_license_mn():
    c = "".join([
        p("Minnesota has specific requirements for purchasing and carrying firearms. Whether you're buying your first handgun or planning to carry, here's an overview of the permits and processes involved."),
        h3("Permit to Purchase (PTP)"),
        p("To buy a handgun or a semiautomatic military-style assault weapon from a dealer in Minnesota, you generally need either a Permit to Purchase or a valid Permit to Carry. The Permit to Purchase is issued free of charge by your local police chief or county sheriff, is valid for one year, and lets you buy eligible firearms during that time."),
        h3("Permit to Carry (PTC)"),
        p("A Minnesota Permit to Carry allows you to carry a handgun in public and also serves as a purchase permit. To qualify you must be at least 21, complete an approved firearms-training course from a certified instructor, and apply through your county sheriff. The permit is valid for five years statewide."),
        h3("Background Checks"),
        p("All firearm purchases from a licensed FFL dealer &mdash; including Twin Cities Gun &amp; Pawn &mdash; require a federal NICS background check via ATF Form 4473. Holding a valid PTP or PTC may streamline the process, but the dealer still verifies eligibility at the point of sale."),
        h3("How to Apply"),
        p("Applications for both the Permit to Purchase and Permit to Carry are submitted to your local sheriff or police department. You'll provide identification, complete the application, and (for the PTC) show proof of completed training. Authorities have a set number of days under state law to approve or deny the application."),
        h3("Long Guns"),
        p("Rifles and shotguns that are not classified as semiautomatic military-style assault weapons generally do not require a Permit to Purchase in Minnesota, though you still must be a legal buyer and pass the dealer's background check."),
        h3("Who Cannot Obtain a Permit"),
        p("Prohibited persons &mdash; including those with certain felony or domestic-violence convictions, active restraining orders, or specific mental-health adjudications &mdash; are not eligible. Federal and state law both apply."),
        h3("The Role of Your FFL Dealer"),
        p('As a licensed dealer, we help ensure your purchase is legal and properly documented. Our staff can answer general questions about permits, transfers, and the paperwork involved, and we handle incoming <a href="guns-rifles.html" class="text-primary-container hover:underline font-semibold">FFL transfers</a> for a flat $50 fee.'),
        h3("Common Questions"),
        p("Do I need a permit to buy a rifle? Usually no, for standard long guns. Does a Permit to Carry let me buy handguns? Yes. How long does a Permit to Purchase last? One year. Where do I apply? Your local sheriff or police department."),
        p('<span class="text-outline text-sm">This overview is for general information only and is not legal advice. Permit rules and timelines can change &mdash; confirm current requirements with your local sheriff\'s office or the Minnesota Bureau of Criminal Apprehension.</span>'),
    ])
    return info_page("gun-license-mn.html", "Minnesota Gun License & Permit | Twin Cities Gun & Pawn",
        "Understand Minnesota gun licensing: Permit to Purchase, Permit to Carry, background checks, how to apply, and the role of your FFL dealer.",
        "Minnesota gun license, permit to purchase MN, permit to carry Minnesota, MN firearms permit, how to apply gun permit Minnesota",
        "gun-license-mn-hero.webp", "Handgun with scattered ammunition on dark blue surface",
        "Guide", "Gun License in Minnesota", "Permits, background checks, and how to buy or carry legally in Minnesota.", c,
        quick_facts=["Permit to Purchase (PTP) is free &mdash; valid 1 year", "Permit to Carry (PTC) valid 5 years statewide", "Must be 21+ to carry", "NICS background check required at every purchase"],
        related=[
            ("guns-rifles.html", "Guns &amp; Rifles", "Browse our firearm selection and FFL transfer services."),
            ("rules-for-pawning.html", "Rules for Pawning a Gun", "ID, valuation, hold periods, and redeeming a pawned firearm."),
            ("unregistered-gun.html", "Unregistered Firearms", "What registration means under federal NFA law in Minnesota."),
        ],
        author_topic="MN Firearm Permits &amp; Licensing")


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
        p('Buy from a licensed <a href="guns-rifles.html" class="text-primary-container hover:underline font-semibold">FFL dealer</a>, keep your purchase records, and never alter a firearm in a way that would make it an unregistered NFA item. If you want a suppressor or SBR, work with a dealer like Twin Cities Gun &amp; Pawn to complete the proper ATF Form 4, trust or individual registration, and tax stamp before you take possession.'),
        h3("We Can Help"),
        p("Our staff can walk you through the legal path to owning NFA items and make sure every transaction is fully compliant. When in doubt, ask us before you buy, modify, or sell."),
        p('<span class="text-outline text-sm">This information is for educational purposes only and does not constitute legal advice. Firearms laws are complex and change over time &mdash; consult the ATF or a qualified attorney regarding your specific circumstances.</span>'),
    ])
    return info_page("unregistered-gun.html", "Unregistered Guns in Minnesota | Twin Cities Gun & Pawn",
        "What \u201cregistered\u201d really means under federal NFA law, the difference between standard firearms and NFA items, and the consequences of unregistered guns.",
        "unregistered firearms Minnesota, NFA registration, unregistered suppressor, SBR laws, illegal firearm consequences MN, stay legal firearms",
        "unregistered-gun-hero.webp", "Firearms laid out on a table — unregistered firearms Minnesota guide",
        "Guide", "Unregistered Firearms in Minnesota", "Understanding firearm registration, NFA items, and how to stay on the right side of the law.", c,
        quick_facts=["No general firearm registry in Minnesota", "NFA items must be federally registered", "Unregistered NFA item = serious federal felony", "Work with a licensed FFL for legal NFA ownership"],
        related=[
            ("gun-license-mn.html", "Gun License in Minnesota", "Permits, background checks, and how to buy or carry legally."),
            ("gun-law-checklist.html", "2026 MN Gun Law Checklist", "A quick-reference checklist for staying compliant in Minnesota."),
            ("guns-rifles.html", "Guns &amp; Rifles", "Browse our firearm selection and FFL transfer services."),
        ],
        author_topic="Federal NFA &amp; MN Firearm Law")


def page_gun_law_checklist():
    """2026 Minnesota Gun Law Checklist — dark card grid layout inspired by numbered template"""

    # Dark stats banner
    stats = """
    <div style="background:#0d0d10;border-bottom:1px solid #2e2c28">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-14">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          <div style="background:#1b1b1e;border:1px solid #2e2c28;border-top:3px solid #facc15" class="p-8">
            <div class="font-mono text-xs tracking-widest uppercase mb-3" style="color:#facc15">National Ranking</div>
            <div class="font-headline font-bold" style="font-size:clamp(2.5rem,5vw,4rem);color:#e5e1e6;line-height:1">#14</div>
            <div class="text-sm mt-3" style="color:#9ca3af">out of 50 states for gun law strength</div>
          </div>
          <div style="background:#1b1b1e;border:1px solid #2e2c28;border-top:3px solid #facc15" class="p-8">
            <div class="font-mono text-xs tracking-widest uppercase mb-3" style="color:#facc15">Composite Score</div>
            <div class="font-headline font-bold" style="font-size:clamp(2.5rem,5vw,4rem);color:#e5e1e6;line-height:1">55<span class="text-2xl" style="color:#6b7280">/100</span></div>
            <div class="text-sm mt-3" style="color:#9ca3af">Everytown Research composite index</div>
          </div>
          <div style="background:#1b1b1e;border:1px solid #2e2c28;border-top:3px solid #facc15" class="p-8">
            <div class="font-mono text-xs tracking-widest uppercase mb-3" style="color:#facc15">Gun Death Rate</div>
            <div class="font-headline font-bold" style="font-size:clamp(2.5rem,5vw,4rem);color:#e5e1e6;line-height:1">9.8<span class="text-xl" style="color:#6b7280">/100k</span></div>
            <div class="text-sm mt-3" style="color:#9ca3af">vs. national avg of 12.8 per 100k residents</div>
          </div>
        </div>
        <p class="text-xs italic" style="color:#4b5563">Data sourced from <a href="https://everytownresearch.org/rankings/state/minnesota/" target="_blank" rel="noopener" style="color:#facc15">Everytown Research &nearr;</a> &nbsp;&middot;&nbsp; Last updated January 14, 2026</p>
      </div>
    </div>"""

    _cat_counter = [0]
    def law_cat(title, laws, icon="gavel"):
        _cat_counter[0] += 1
        n = _cat_counter[0]
        cards = "".join(
            '<div style="background:#1b1b1e;border:1px solid #2e2c28" class="p-4 flex items-start gap-3">'
            '<span class="material-symbols-outlined text-base flex-shrink-0 mt-0.5" style="color:#facc15">check_circle</span>'
            '<span class="text-sm leading-relaxed" style="color:#d1d5db">%s</span>'
            '</div>' % law
            for law in laws
        )
        return """
        <div class="mb-14">
          <div class="flex items-center gap-4 mb-6 pb-4 border-b" style="border-color:#2e2c28">
            <span class="font-mono font-bold text-2xl flex-shrink-0" style="color:#facc15">%02d</span>
            <span class="material-symbols-outlined flex-shrink-0" style="color:#facc15;font-size:1.35rem">%s</span>
            <h2 class="font-headline font-bold text-headline-sm" style="color:#facc15">%s</h2>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">%s</div>
        </div>""" % (n, icon, title, cards)

    cats = "".join([
        law_cat("Foundational Laws", [
            "<strong style='color:#e5e1e6'>Background checks required</strong> for handgun and semiautomatic assault weapon purchases",
            "<strong style='color:#e5e1e6'>Concealed carry permit required</strong> with training including live-fire requirement",
            "<strong style='color:#e5e1e6'>Extreme Risk law</strong> allows temporary gun removal for individuals in crisis",
            "<strong style='color:#e5e1e6'>No Shoot First law</strong> in place",
            "<strong style='color:#e5e1e6'>Secure storage required</strong> when a child under 18 may access the firearm"
        ], icon="gavel"),
        law_cat("Gun Industry &amp; Product Safety", [
            "<strong style='color:#e5e1e6'>Assault weapons prohibited</strong> — military-style weapons banned",
            "<strong style='color:#e5e1e6'>Auto sears / Glock switches prohibited</strong>",
            "<strong style='color:#e5e1e6'>Bump stocks prohibited</strong>",
            "<strong style='color:#e5e1e6'>Consumer safety:</strong> new handguns must have childproofing features",
            "<strong style='color:#e5e1e6'>Dealer license required</strong> at state level",
            "<strong style='color:#e5e1e6'>Ghost guns regulated</strong> — serial numbers required, background checks enforced",
            "<strong style='color:#e5e1e6'>High-capacity magazines prohibited</strong>",
            "<strong style='color:#e5e1e6'>Legal accountability for gun industry</strong> allowed",
            "<strong style='color:#e5e1e6'>Microstamping for new handguns</strong> required"
        ], icon="factory"),
        law_cat("Guns in Public", [
            "<strong style='color:#e5e1e6'>No carry after violent offense</strong> — 3-year ban for assault/violent misdemeanor",
            "<strong style='color:#e5e1e6'>No guns mandate on college campuses</strong>",
            "<strong style='color:#e5e1e6'>No guns at state capitol or demonstrations</strong>",
            "<strong style='color:#e5e1e6'>No guns in bars</strong>",
            "<strong style='color:#e5e1e6'>No guns in K-12 schools</strong> by staff or permit holders",
            "<strong style='color:#e5e1e6'>Open carry regulated</strong> — permit required for all firearms",
            "<strong style='color:#e5e1e6'>Strong concealed carry authority</strong> — officials can deny for public safety"
        ], icon="location_city"),
        law_cat("Keeping Guns Out of the Wrong Hands", [
            "<strong style='color:#e5e1e6'>Emergency restraining order prohibitor</strong> — domestic abusers barred",
            "<strong style='color:#e5e1e6'>Felony prohibitor</strong> indefinite",
            "<strong style='color:#e5e1e6'>Fugitive from justice prohibitor</strong>",
            "<strong style='color:#e5e1e6'>Gun removal program</strong> — officials actively seek illegal guns",
            "<strong style='color:#e5e1e6'>Hate crime prohibitor</strong>",
            "<strong style='color:#e5e1e6'>Mental health prohibitor</strong> — indefinite for involuntary commitments",
            "<strong style='color:#e5e1e6'>Minimum age:</strong> 21+ for handguns, 18+ for long guns",
            "<strong style='color:#e5e1e6'>Assault/violent misdemeanor prohibitor</strong> — 3-year ban",
            "<strong style='color:#e5e1e6'>Domestic abuser prohibition</strong> covers misdemeanor convictions &amp; dating partners",
            "<strong style='color:#e5e1e6'>Relinquishment required</strong> for convicted abusers and those under restraining orders",
            "<strong style='color:#e5e1e6'>School threat assessment teams</strong> required by law",
            "<strong style='color:#e5e1e6'>Stalker prohibitor</strong> — 3-year ban"
        ], icon="shield"),
        law_cat("Policing &amp; Civil Rights", [
            "<strong style='color:#e5e1e6'>Funding for victims of gun violence</strong> via VOCA funds",
            "<strong style='color:#e5e1e6'>Local gun laws allowed</strong> — no state preemption",
            "<strong style='color:#e5e1e6'>Office of Violence Intervention</strong> exists",
            "<strong style='color:#e5e1e6'>Police deadly force standard:</strong> only when necessary to prevent serious injury",
            "<strong style='color:#e5e1e6'>Qualified immunity limited</strong>",
            "<strong style='color:#e5e1e6'>Tools to address crime guns:</strong> tracing + trafficking/straw purchase crimes",
            "<strong style='color:#e5e1e6'>Violence intervention program funding</strong> in state budget"
        ], icon="balance"),
        law_cat("Sales &amp; Permitting", [
            "<strong style='color:#e5e1e6'>Authority to deny gun purchase</strong> if buyer poses danger",
            "<strong style='color:#e5e1e6'>Charleston Loophole closed</strong> — 30-day waiting period for handguns/assault weapons",
            "<strong style='color:#e5e1e6'>Lost and stolen reporting</strong> required",
            "<strong style='color:#e5e1e6'>Mental health record reporting</strong> into background check system",
            "<strong style='color:#e5e1e6'>Sales records sent to law enforcement</strong> for handguns",
            "<strong style='color:#e5e1e6'>Training required to purchase guns</strong>",
            "<strong style='color:#e5e1e6'>Waiting periods</strong> enforced"
        ], icon="sell")
    ])

    dark_content = """
    <div style="background:#131316">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin py-16">%s</div>
    </div>""" % cats

    body = (nav() + ticker() +
            page_hero("gun-law-checklist-hero.webp", "Classic hunting shotguns displayed in wooden rack", "2026 Checklist", "Gun Law Checklist", "How Minnesota ranks on gun safety laws, background checks, concealed carry, and more.") +
            stats +
            guide_author("2026 Minnesota Gun Law &amp; Compliance") +
            dark_content +
            cta_band("Questions About Minnesota Gun Laws?", "Our knowledgeable team can help you navigate firearms regulations in Minnesota. Give us a call or stop in.", "Contact Us", "contact.html") +
            related_links([
                ("gun-license-mn.html", "Gun License in Minnesota", "Permit to Purchase, Permit to Carry, and how to apply."),
                ("unregistered-gun.html", "Unregistered Firearms", "What registration means under federal NFA law in Minnesota."),
                ("rules-for-pawning.html", "Rules for Pawning a Gun", "ID, valuation, hold periods, and reclaiming a firearm."),
            ]) + footer())
    return head("2026 Gun Law Checklist | Minnesota | Twin Cities Gun & Pawn",
        "Minnesota's 2026 gun law rankings: #14 in the nation for gun law strength. See how the state stacks up on background checks, permits, and gun safety policies.",
        "gun-law-checklist.html",
        "Minnesota gun laws 2026, gun law rankings Minnesota, background check laws MN, concealed carry permit Minnesota, gun safety laws",
        ) + body


# ---------- GALLERY ----------
GALLERY_PHOTOS = [
    # (filename in images/, caption)
    ("home-page-hero.jpg", "Store Panorama"),
    ("firearms-store-interior.webp", "Showroom Overview"),
    ("store-showroom.webp", "Long-Gun Wall &amp; Pistol Counters"),
    ("showroom-display-01.webp", "Tactical Carousel &amp; Rifle Walls"),
    ("firearms-showroom-display.webp", "Corner Rifle Wall &amp; Handgun Tower"),
    ("gun-shop-showroom.webp", "Gun Shop Showroom"),
    ("showroom-displays-01.webp", "Shotgun Racks &amp; Showroom Displays"),
    ("handgun-display-behind-glass.webp", "Semi-Auto Pistols Behind Glass"),
    ("1911-handgun-display-case.webp", "1911 Pistols &amp; Ammunition"),
    ("handgun-revolver-display-case.webp", "Handgun &amp; Revolver Display Case"),
    ("handgun-display-case.webp", "Handgun Tower Showcase"),
    ("handgun-display-case-01.webp", "Full-Size &amp; Compact Pistols"),
    ("handgun-display-case-02.webp", "Concealed Carry Pistols"),
    ("ar-rifles-display.webp", "AR-Platform Rifles"),
    ("tactical-firearms-carousel.webp", "Tactical Firearms Carousel"),
    ("rifle-rack-ammo-display.webp", "Hunting Rifles &amp; Ammo"),
    ("vibrant-hunting-store-display.webp", "Bolt-Action Hunting Rifles"),
    ("hunting-rifle-display-wall.webp", "Hunting Rifle Wall"),
    ("organized-gun-shop-display.webp", "Classic Wood-Stock Long Guns"),
    ("shotgun-rack-display.webp", "Shotgun Rack"),
    ("shotgun-rack-display-01.webp", "Pump-Action Shotguns"),
    ("shotgun-rack-camo.webp", "Semi-Auto &amp; Over/Under Shotguns"),
    ("compound-bow-display-rack.webp", "Compound Bows"),
    ("rifle-scope-display.webp", "Rifle Scope Display Case"),
    ("retail-optics-accessories-display.webp", "Optics &amp; Accessories"),
    ("ammo-retail-shelf-display.webp", "Ammunition Wall"),
    ("bright-hunting-gear-display.webp", "Hunting Gear Display"),
]

GALLERY_CSS = """
  <style>
    .tc-gallery{display:grid;grid-template-columns:1fr;gap:1rem}
    @media(min-width:480px){.tc-gallery{grid-template-columns:repeat(2,1fr)}}
    @media(min-width:900px){.tc-gallery{grid-template-columns:repeat(3,1fr)}}
    @media(min-width:1200px){.tc-gallery{grid-template-columns:repeat(4,1fr)}}
    .tc-gal-item{display:block;width:100%;padding:0;border:1px solid #e2e8f0;background:#fff;cursor:zoom-in;text-align:left;overflow:hidden}
    .tc-gal-item:focus-visible{outline:3px solid #facc15;outline-offset:2px}
    .tc-gal-img{position:relative;aspect-ratio:4/3;overflow:hidden;background:#111}
    .tc-gal-img img{width:100%;height:100%;object-fit:cover;transition:transform .4s ease}
    .tc-gal-item:hover .tc-gal-img img{transform:scale(1.05)}
    .tc-gal-cap{padding:.75rem 1rem;font-weight:700;font-size:.9rem;color:#111827;border-top:3px solid #facc15}
    .tc-lb{position:fixed;inset:0;z-index:9999;background:rgba(0,0,0,.92);display:none;align-items:center;justify-content:center;flex-direction:column;padding:4rem 4.5rem}
    .tc-lb.open{display:flex}
    .tc-lb img{max-width:100%;max-height:calc(100vh - 9rem);object-fit:contain;box-shadow:0 10px 40px rgba(0,0,0,.6)}
    .tc-lb-cap{margin-top:1rem;color:#fff;font-weight:700;text-align:center}
    .tc-lb-cap span{color:#facc15;font-family:monospace;font-size:.8rem;margin-left:.6rem}
    .tc-lb button{position:absolute;background:rgba(0,0,0,.55);color:#fff;border:2px solid rgba(255,255,255,.35);cursor:pointer;line-height:1;display:flex;align-items:center;justify-content:center}
    .tc-lb button:hover,.tc-lb button:focus-visible{background:#facc15;color:#000;border-color:#facc15;outline:none}
    .tc-lb-close{top:1rem;right:1rem;width:48px;height:48px;font-size:2rem}
    .tc-lb-prev,.tc-lb-next{top:50%;transform:translateY(-50%);width:52px;height:72px;font-size:3rem}
    .tc-lb-prev{left:.75rem}.tc-lb-next{right:.75rem}
    @media(max-width:640px){.tc-lb{padding:4rem .5rem}.tc-lb-prev,.tc-lb-next{width:40px;height:56px;font-size:2.2rem;top:auto;bottom:1rem;transform:none}}
  </style>"""

GALLERY_JS = """
  <script>
  (function () {
    var items = Array.prototype.slice.call(document.querySelectorAll('.tc-gal-item'));
    var lb = document.getElementById('tc-lightbox');
    if (!lb || !items.length) return;
    var img = lb.querySelector('img'), cap = lb.querySelector('.tc-lb-cap');
    var idx = 0, lastFocus = null;
    function show(i) {
      idx = (i + items.length) % items.length;
      var it = items[idx];
      img.src = it.getAttribute('data-full');
      img.alt = it.querySelector('img').alt;
      cap.innerHTML = it.getAttribute('data-caption') + '<span>' + (idx + 1) + ' / ' + items.length + '</span>';
    }
    function open(i) {
      lastFocus = document.activeElement;
      show(i);
      lb.classList.add('open');
      lb.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lb.querySelector('.tc-lb-close').focus();
    }
    function close() {
      lb.classList.remove('open');
      lb.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      img.src = '';
      if (lastFocus) lastFocus.focus();
    }
    items.forEach(function (it, i) { it.addEventListener('click', function () { open(i); }); });
    lb.querySelector('.tc-lb-close').addEventListener('click', close);
    lb.querySelector('.tc-lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(idx - 1); });
    lb.querySelector('.tc-lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') show(idx - 1);
      else if (e.key === 'ArrowRight') show(idx + 1);
    });
    var sx = null;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, {passive: true});
    lb.addEventListener('touchend', function (e) {
      if (sx === null) return;
      var dx = e.changedTouches[0].clientX - sx; sx = null;
      if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    });
  })();
  </script>"""


def page_gallery():
    tiles = "".join("""
          <button type="button" class="tc-gal-item" data-full="images/{f}" data-caption="{c}" aria-label="View larger: {c}">
            <div class="tc-gal-img"><img src="images/{f}" alt="{c} at Twin Cities Gun &amp; Pawn" loading="lazy" decoding="async" /></div>
            <div class="tc-gal-cap">{c}</div>
          </button>""".format(f=f, c=c) for f, c in GALLERY_PHOTOS)
    content = """
    <section class="py-16" style="background:#f8f9fa;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0">
      <div class="max-w-[1360px] mx-auto px-6 lg:px-margin">
        <div class="mb-10 text-center">{label}<h2 class="font-headline font-bold text-headline-lg" style="color:#111827">Inside Our Showroom</h2><p class="mt-4 max-w-3xl mx-auto" style="color:#374151">Take a look around Twin Cities Gun &amp; Pawn &mdash; handgun counters, rifle and shotgun walls, optics, ammunition and more. Click any photo to view it full size.</p></div>
        <div class="tc-gallery">{tiles}
        </div>
      </div>
    </section>
    <div id="tc-lightbox" class="tc-lb" role="dialog" aria-modal="true" aria-label="Photo viewer" aria-hidden="true">
      <button type="button" class="tc-lb-close" aria-label="Close">&times;</button>
      <button type="button" class="tc-lb-prev" aria-label="Previous photo">&lsaquo;</button>
      <img src="" alt="" />
      <div class="tc-lb-cap"></div>
      <button type="button" class="tc-lb-next" aria-label="Next photo">&rsaquo;</button>
    </div>""".format(label=label("Gallery"), tiles=tiles)
    body = (nav() + ticker() + GALLERY_CSS +
            text_hero("Gallery", "Our Store Gallery", "Step inside Twin Cities Gun &amp; Pawn &mdash; real photos of our firearms, displays and showroom.") +
            content +
            cta_band("See It In Person", "Our inventory changes daily. Stop by the store or give us a call to check what&rsquo;s in stock.", "Visit Our Store", "contact.html") +
            footer().replace("</body>", GALLERY_JS + "\n</body>", 1))
    return head("Store Gallery | Photos of Our Showroom | Twin Cities Gun & Pawn",
        "Photo gallery of Twin Cities Gun & Pawn \u2014 handgun counters, rifle and shotgun walls, optics, ammunition and our full firearms showroom in the Twin Cities.",
        "gallery.html",
        "Twin Cities Gun & Pawn photos, gun store gallery, firearms showroom Minnesota, pawn shop pictures",
        ) + body


# ---------- WRITE-OUT ----------
PAGES = {
    "": page_index,
    "about.html": page_about,
    "guns-rifles.html": page_guns,
    "accessories.html": page_accessories,
    "pawn-loans.html": page_pawn,
    "gallery.html": page_gallery,
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
    "": "1.0",
    "guns-rifles.html": "0.9", "pawn-loans.html": "0.9", "accessories.html": "0.9",
    "contact.html": "0.8", "about.html": "0.8", "gallery.html": "0.6",
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
        loc = BASE_URL + "/" + fname if fname else BASE_URL + "/"
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
        out_fname = "index.html" if fname == "" else fname
        with open(os.path.join(OUT, out_fname), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", out_fname, len(html), "bytes")
    # remove old services.html (replaced by pawn-loans.html)
    old = os.path.join(OUT, "services.html")
    if os.path.exists(old):
        os.remove(old)
        print("removed services.html")
    write_sitemap_xml()
    write_robots_txt()
    print("DONE")
