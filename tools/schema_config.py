# -*- coding: utf-8 -*-
"""Schema.org JSON-LD configuration — single source of truth (v3.1 spec).

All business facts, service metadata, and per-page graph configuration for the
Twin Cities Gun & Pawn website live here. `build_schema.py` reads this module,
assembles a per-page {"@context": "https://schema.org", "@graph": [...]} document,
and injects it into each HTML file. `check_schema.py` validates the output.

Nothing in this file touches the filesystem — it is pure data + light helpers.
"""

DOMAIN = "https://twin-cities-pawn-guns.pages.dev"


def u(path=""):
    """Build an absolute URL / @id anchor on the canonical domain."""
    if path.startswith("#"):
        return DOMAIN + "/" + path
    if path.startswith("http"):
        return path
    return DOMAIN + "/" + path.lstrip("/")


# ---------------------------------------------------------------------------
# CONCEPT knowsAbout entries — general topics, legal concepts, geo entities
# ---------------------------------------------------------------------------
CONCEPT_KNOWS_ABOUT = [
    {"@type": "Thing", "name": "Firearms",
     "sameAs": "https://en.wikipedia.org/wiki/Firearm"},
    {"@type": "Thing", "name": "Pawnbroker",
     "sameAs": "https://en.wikipedia.org/wiki/Pawnbroker"},
    {"@type": "Thing", "name": "Federal Firearms License",
     "sameAs": "https://en.wikipedia.org/wiki/Federal_Firearms_License"},
    {"@type": "Thing", "name": "Ammunition",
     "sameAs": "https://en.wikipedia.org/wiki/Ammunition"},
    {"@type": "Thing", "name": "Gun Broker",
     "sameAs": "https://en.wikipedia.org/wiki/Arms_dealer"},
    {"@type": "Thing", "name": "Pawn Shop",
     "sameAs": "https://en.wikipedia.org/wiki/Pawnbroker"},
    {"@type": "Thing", "name": "Ramsey, Minnesota",
     "sameAs": "https://en.wikipedia.org/wiki/Ramsey,_Minnesota"},
    {"@type": "Thing", "name": "Minnesota",
     "sameAs": "https://en.wikipedia.org/wiki/Minnesota"},
    {"@type": "Thing", "name": "Minneapolis\u2013Saint Paul",
     "sameAs": "https://en.wikipedia.org/wiki/Minneapolis%E2%80%93Saint_Paul"},
]

# ---------------------------------------------------------------------------
# BRAND knowsAbout entries — all 43 firearm brands carried in-store
# ---------------------------------------------------------------------------
BRAND_KNOWS_ABOUT = [
    {"@type": "Brand", "name": "A.P.F."},
    {"@type": "Brand", "name": "Benelli",
     "sameAs": "https://en.wikipedia.org/wiki/Benelli_Armi_SpA"},
    {"@type": "Brand", "name": "Beretta",
     "sameAs": "https://en.wikipedia.org/wiki/Beretta"},
    {"@type": "Brand", "name": "Browning Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Browning_Arms_Company"},
    {"@type": "Brand", "name": "Bushmaster",
     "sameAs": "https://en.wikipedia.org/wiki/Bushmaster_Firearms_International"},
    {"@type": "Brand", "name": "Canik",
     "sameAs": "https://en.wikipedia.org/wiki/Canik_(manufacturer)"},
    {"@type": "Brand", "name": "Charter Arms"},
    {"@type": "Brand", "name": "Citadel"},
    {"@type": "Brand", "name": "Colt",
     "sameAs": "https://en.wikipedia.org/wiki/Colt%27s_Manufacturing_Company"},
    {"@type": "Brand", "name": "Commando"},
    {"@type": "Brand", "name": "Daniel Defense",
     "sameAs": "https://en.wikipedia.org/wiki/Daniel_Defense"},
    {"@type": "Brand", "name": "Diamondback Firearms",
     "sameAs": "https://en.wikipedia.org/wiki/Diamondback_Firearms"},
    {"@type": "Brand", "name": "FN Herstal",
     "sameAs": "https://en.wikipedia.org/wiki/FN_Herstal"},
    {"@type": "Brand", "name": "Glock",
     "sameAs": "https://en.wikipedia.org/wiki/Glock"},
    {"@type": "Brand", "name": "Heckler \u0026 Koch",
     "sameAs": "https://en.wikipedia.org/wiki/Heckler_%26_Koch"},
    {"@type": "Brand", "name": "Henry Repeating Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Henry_Repeating_Arms"},
    {"@type": "Brand", "name": "Howa",
     "sameAs": "https://en.wikipedia.org/wiki/Howa"},
    {"@type": "Brand", "name": "Ithaca Gun Company",
     "sameAs": "https://en.wikipedia.org/wiki/Ithaca_Gun_Company"},
    {"@type": "Brand", "name": "Kahr Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Kahr_Arms"},
    {"@type": "Brand", "name": "Kel-Tec",
     "sameAs": "https://en.wikipedia.org/wiki/Kel-Tec"},
    {"@type": "Brand", "name": "Kimber Manufacturing",
     "sameAs": "https://en.wikipedia.org/wiki/Kimber_Manufacturing"},
    {"@type": "Brand", "name": "Kral"},
    {"@type": "Brand", "name": "Marlin Firearms",
     "sameAs": "https://en.wikipedia.org/wiki/Marlin_Firearms"},
    {"@type": "Brand", "name": "Mauser",
     "sameAs": "https://en.wikipedia.org/wiki/Mauser"},
    {"@type": "Brand", "name": "Merak"},
    {"@type": "Brand", "name": "O.F. Mossberg \u0026 Sons",
     "sameAs": "https://en.wikipedia.org/wiki/O.F._Mossberg_%26_Sons"},
    {"@type": "Brand", "name": "Norinco",
     "sameAs": "https://en.wikipedia.org/wiki/Norinco"},
    {"@type": "Brand", "name": "Perazzi",
     "sameAs": "https://en.wikipedia.org/wiki/Perazzi"},
    {"@type": "Brand", "name": "Remington Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Remington_Arms"},
    {"@type": "Brand", "name": "Rock Island Armory",
     "sameAs": "https://en.wikipedia.org/wiki/Armscor_(manufacturer)"},
    {"@type": "Brand", "name": "Rossi Firearms",
     "sameAs": "https://en.wikipedia.org/wiki/Amadeo_Rossi_S.A."},
    {"@type": "Brand", "name": "Ruger",
     "sameAs": "https://en.wikipedia.org/wiki/Sturm,_Ruger_%26_Co."},
    {"@type": "Brand", "name": "Savage Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Savage_Arms"},
    {"@type": "Brand", "name": "SIG Sauer",
     "sameAs": "https://en.wikipedia.org/wiki/SIG_Sauer"},
    {"@type": "Brand", "name": "Smith \u0026 Wesson",
     "sameAs": "https://en.wikipedia.org/wiki/Smith_%26_Wesson"},
    {"@type": "Brand", "name": "Springfield Armory",
     "sameAs": "https://en.wikipedia.org/wiki/Springfield_Armory,_Inc."},
    {"@type": "Brand", "name": "Stoeger Industries",
     "sameAs": "https://en.wikipedia.org/wiki/Stoeger_Industries"},
    {"@type": "Brand", "name": "Taurus Firearms",
     "sameAs": "https://en.wikipedia.org/wiki/Taurus_Firearms"},
    {"@type": "Brand", "name": "Thompson/Center Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Thompson/Center_Arms"},
    {"@type": "Brand", "name": "Carl Walther GmbH",
     "sameAs": "https://en.wikipedia.org/wiki/Carl_Walther_GmbH"},
    {"@type": "Brand", "name": "Weatherby",
     "sameAs": "https://en.wikipedia.org/wiki/Weatherby"},
    {"@type": "Brand", "name": "Winchester Repeating Arms",
     "sameAs": "https://en.wikipedia.org/wiki/Winchester_Repeating_Arms_Company"},
    {"@type": "Brand", "name": "Windham Weaponry",
     "sameAs": "https://en.wikipedia.org/wiki/Windham_Weaponry"},
]


# ---------------------------------------------------------------------------
# WEBSITE NODE — identical on every page
# ---------------------------------------------------------------------------
WEBSITE = {
    "@type": "WebSite",
    "@id": u("#website"),
    "name": "Twin Cities Gun & Pawn",
    "url": DOMAIN,
    "publisher": {"@id": u("#business")},
    "inLanguage": "en-US",
}


# ---------------------------------------------------------------------------
# BUSINESS NODE — full PawnShop, injected on EVERY page.
# Defines #logo, #service-area (GeoCircle) and references the 4 service @ids.
# ---------------------------------------------------------------------------
BUSINESS = {
    "@type": "PawnShop",
    "@id": u("#business"),
    "name": "Twin Cities Gun & Pawn",
    "alternateName": "TC Gun & Pawn",
    "foundingDate": "2010",
    "url": DOMAIN,
    "telephone": "+1-763-427-4100",
    "priceRange": "$$",
    "publicAccess": True,
    "paymentAccepted": "Cash, Debit Card, Credit Card",
    "currenciesAccepted": "USD",
    "logo": {
        "@type": "ImageObject",
        "@id": u("#logo"),
        "url": u("images/logo.png"),
        "width": 680,
        "height": 280,
        "caption": "Twin Cities Gun & Pawn",
    },
    "image": {
        "@type": "ImageObject",
        "url": u("images/og-image.jpg"),
        "width": 1200,
        "height": 630,
    },
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "6650 US-10",
        "addressLocality": "Ramsey",
        "addressRegion": "MN",
        "postalCode": "55303",
        "addressCountry": "US",
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 45.2619,
        "longitude": -93.4499,
    },
    "hasMap": "https://maps.google.com/?q=Twin+Cities+Pawn+%26+Gun,+6650+US-10,+Ramsey,+MN+55303",
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "10:00",
            "closes": "19:00",
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": "Saturday",
            "opens": "10:00",
            "closes": "17:00",
        },
    ],
    # areaServed: exactly 3 nodes — GeoCircle (#service-area) + State + City
    "areaServed": [
        {
            "@type": "GeoCircle",
            "@id": u("#service-area"),
            "description": "30-mile service radius anchored on Ramsey, Minnesota",
            "geoMidpoint": {
                "@type": "GeoCoordinates",
                "latitude": 45.2619,
                "longitude": -93.4499,
            },
            "geoRadius": "48280",
        },
        {
            "@type": "State",
            "name": "Minnesota",
            "sameAs": "https://en.wikipedia.org/wiki/Minnesota",
        },
        {
            "@type": "City",
            "name": "Minneapolis\u2013Saint Paul",
            "sameAs": "https://en.wikipedia.org/wiki/Minneapolis%E2%80%93Saint_Paul",
        },
    ],
    "sameAs": [
        "https://www.armslist.com/store/227/twin-cities-pawn",
        "https://www.gunbroker.com/All/search?Keywords=twin%20cities%20pawn&Sort=13",
        "https://www.facebook.com/twincitiespawn",
        "https://www.instagram.com/twincities_pawn/",
    ],
    "amenityFeature": [
        {"@type": "LocationFeatureSpecification", "name": "Licensed FFL Dealer", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "On-Site FFL Transfer ($50)", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Fair Pawn Loans \u2014 No Credit Check", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "Government-Issued ID Required for Firearm Purchase", "value": True},
        {"@type": "LocationFeatureSpecification", "name": "300+ Firearms In Stock", "value": True},
    ],
    # knowsAbout: 9 concepts + 43 brands = 52 entries
    "knowsAbout": CONCEPT_KNOWS_ABOUT + BRAND_KNOWS_ABOUT,
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Twin Cities Gun & Pawn Services",
        "itemListElement": [
            {"@id": u("#service-firearms")},
            {"@id": u("#service-accessories")},
            {"@id": u("#service-pawn-loans")},
            {"@id": u("#service-ffl-transfer")},
        ],
    },
    "potentialAction": [
        {
            "@type": "CommunicateAction",
            "name": "Call Twin Cities Gun & Pawn",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": "tel:+17634274100",
                "actionPlatform": [
                    "http://schema.org/DesktopWebPlatform",
                    "http://schema.org/MobileWebPlatform",
                ],
            },
        },
        {
            "@type": "AskAction",
            "name": "Request a Quote",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": u("contact.html#contact-form"),
                "actionPlatform": [
                    "http://schema.org/DesktopWebPlatform",
                    "http://schema.org/MobileWebPlatform",
                ],
            },
        },
    ],
}


# ---------------------------------------------------------------------------
# SERVICES — metadata keyed by short id. Rendered at three levels:
#   full  -> on the service's own page (all fields, isRelatedTo, mainEntityOfPage)
#   card  -> on index.html (name, serviceType, card description, provider, url,
#            areaServed, category)
#   stub  -> everywhere else (@id, name, url, provider only)
# ---------------------------------------------------------------------------
SERVICES = {
    "firearms": {
        "id": u("#service-firearms"),
        "name": "Firearms Sales — Guns & Rifles",
        "serviceType": "Retail Firearms Sales",
        "url": u("guns-rifles.html"),
        "category": {"@type": "Thing", "name": "Firearms",
                     "sameAs": "https://en.wikipedia.org/wiki/Firearm"},
        "desc_full": ("Twin Cities Gun & Pawn carries 300+ handguns, pistols, revolvers, rifles, "
                      "shotguns, semi-automatic firearms, and collectible guns in the Twin Cities, MN. "
                      "Licensed FFL dealer serving the Twin Cities metro within a 30-mile radius."),
        "desc_card": ("300+ handguns, rifles, shotguns, and collectible firearms in stock. "
                      "Licensed FFL dealer serving the Twin Cities metro area."),
        "own_page": "guns-rifles.html",
        "related": ["accessories", "pawn-loans"],
    },
    "accessories": {
        "id": u("#service-accessories"),
        "name": "Firearms Accessories",
        "serviceType": "Retail Firearms Accessories",
        "url": u("accessories.html"),
        "category": {"@type": "Thing", "name": "Firearm Accessories",
                     "sameAs": "https://en.wikipedia.org/wiki/Firearm_accessories"},
        "desc_full": ("Twin Cities Gun & Pawn stocks ammunition, scopes and optics, holsters, slings, "
                      "cases, magazines, and gun safes in the Twin Cities, MN. Serving the Twin Cities metro within 30 miles."),
        "desc_card": ("Ammunition, optics, holsters, slings, magazines, and gun safes. "
                      "Everything you need to keep your firearm ready."),
        "own_page": "accessories.html",
        "related": ["firearms", "pawn-loans"],
    },
    "pawn-loans": {
        "id": u("#service-pawn-loans"),
        "name": "Pawn Loans",
        "serviceType": "Pawn Lending",
        "url": u("pawn-loans.html"),
        "category": {"@type": "Thing", "name": "Pawnbroker",
                     "sameAs": "https://en.wikipedia.org/wiki/Pawnbroker"},
        "desc_full": ("Twin Cities Gun & Pawn offers fair pawn loans in the Twin Cities, MN. We buy and loan "
                      "against guns, power tools, electronics, jewelry, and gold. Fair appraisals, fast cash. "
                      "No credit check required. Serving the Twin Cities metro within 30 miles."),
        "desc_card": ("Get cash fast with our fair pawn loans. No credit check required. "
                      "We accept guns, tools, electronics, jewelry, and gold."),
        "own_page": "pawn-loans.html",
        "related": ["ffl-transfer", "firearms"],
    },
    "ffl-transfer": {
        "id": u("#service-ffl-transfer"),
        "name": "FFL Firearms Transfer",
        "serviceType": "Federal Firearms License Transfer",
        "url": u("pawn-loans.html"),
        "category": {"@type": "Thing", "name": "Federal Firearms License",
                     "sameAs": "https://en.wikipedia.org/wiki/Federal_Firearms_License"},
        "desc_full": ("Licensed FFL dealer offering $50 firearms transfers in the Twin Cities, MN. Transfer any legally "
                      "purchased firearm through Twin Cities Gun & Pawn."),
        "desc_card": ("Licensed FFL dealer offering $50 firearms transfers serving the Twin Cities metro. "
                      "Transfer any legally purchased firearm through Twin Cities Gun & Pawn."),
        "own_page": "pawn-loans.html",
        "related": [],
    },
}

# Order in which service nodes are emitted on a page.
SERVICE_ORDER = ["firearms", "accessories", "pawn-loans", "ffl-transfer"]

# Services that appear at CARD level on the homepage.
INDEX_CARD_SERVICES = ["firearms", "accessories", "pawn-loans"]


# ---------------------------------------------------------------------------
# PER-PAGE CONFIG
# breadcrumb: list of (name, slug) — position auto-assigned in order.
# webpage_type: schema subtype of WebPage.
# faq: True -> extract visible Q&A from the HTML and add an FAQPage node.
# actions: list of "ask" | "apply" -> standalone action nodes for that page.
# main_entity: service short-id referenced by the WebPage.mainEntity.
# primary_image: relative image path -> WebPage.primaryImageOfPage.
# ---------------------------------------------------------------------------
PAGES = {
    "index.html": {
        "webpage_type": "WebPage",
        "name": "Twin Cities Gun & Pawn | Firearms, Pawn Loans & Guns in the Twin Cities, MN",
        "description": ("Twin Cities trusted firearms dealer and pawn shop since 2010. 300+ guns, rifles, "
                        "shotguns. Licensed FFL dealer serving the Twin Cities metro."),
        "breadcrumb": [("Home", "index.html")],
        "primary_image": "images/storefront.webp",
    },
    "about.html": {
        "webpage_type": "AboutPage",
        "name": "About Twin Cities Gun & Pawn | Twin Cities, MN Firearms & Pawn Shop Since 2010",
        "breadcrumb": [("Home", "index.html"), ("About", "about.html")],
    },
    "guns-rifles.html": {
        "webpage_type": "CollectionPage",
        "name": "Guns & Rifles | 300+ Firearms In Stock | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Inventory", "guns-rifles.html"), ("Guns & Rifles", "guns-rifles.html")],
        "main_entity": "firearms",
    },
    "accessories.html": {
        "webpage_type": "CollectionPage",
        "name": "Firearms Accessories | Ammo, Optics, Holsters & Safes | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Inventory", "guns-rifles.html"), ("Accessories", "accessories.html")],
        "main_entity": "accessories",
    },
    "pawn-loans.html": {
        "webpage_type": "WebPage",
        "name": "Pawn Loans & $50 FFL Transfers | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Inventory", "guns-rifles.html"), ("Pawn & Loans", "pawn-loans.html")],
        "main_entity": "pawn-loans",
    },
    "contact.html": {
        "webpage_type": "ContactPage",
        "name": "Contact Twin Cities Gun & Pawn | Twin Cities, MN | (763) 427-4100",
        "breadcrumb": [("Home", "index.html"), ("Contact", "contact.html")],
        "actions": ["ask", "apply"],
    },
    "faq.html": {
        "webpage_type": "WebPage",
        "name": "FAQ | Twin Cities Gun & Pawn | Twin Cities, MN",
        "breadcrumb": [("Home", "index.html"), ("FAQ", "faq.html")],
        "faq": True,
    },
    "faq-gun-pawns.html": {
        "webpage_type": "WebPage",
        "name": "FAQ: Pawning Guns | Twin Cities Gun & Pawn | Twin Cities, MN",
        "breadcrumb": [("Home", "index.html"), ("Contact", "contact.html"), ("FAQ \u2013 Gun Pawns", "faq-gun-pawns.html")],
        "faq": True,
    },
    "employment.html": {
        "webpage_type": "WebPage",
        "name": "Employment Application | Join Our Team | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Contact", "contact.html"), ("Employment", "employment.html")],
        "actions": ["apply"],
    },
    "resources.html": {
        "webpage_type": "CollectionPage",
        "name": "Firearms & Pawn Resources | Twin Cities Gun & Pawn | Twin Cities, MN",
        "breadcrumb": [("Home", "index.html"), ("Resources", "resources.html")],
    },
    "rules-for-pawning.html": {
        "webpage_type": "WebPage",
        "name": "Rules for Pawning a Gun in Minnesota | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Resources", "resources.html"), ("Rules for Pawning a Gun", "rules-for-pawning.html")],
    },
    "gun-license-mn.html": {
        "webpage_type": "WebPage",
        "name": "Gun License & Permit Requirements in Minnesota | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Resources", "resources.html"), ("Gun License in Minnesota", "gun-license-mn.html")],
    },
    "unregistered-gun.html": {
        "webpage_type": "WebPage",
        "name": "Unregistered Firearms in Minnesota: Legal Consequences | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Resources", "resources.html"), ("Unregistered Firearms", "unregistered-gun.html")],
    },
    "gun-law-checklist.html": {
        "webpage_type": "WebPage",
        "name": "2026 Gun Law Checklist | Minnesota | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Resources", "resources.html"), ("2026 Gun Law Checklist", "gun-law-checklist.html")],
    },
    "terms.html": {
        "webpage_type": "WebPage",
        "name": "Terms & Conditions | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Terms & Conditions", "terms.html")],
    },
    "privacy.html": {
        "webpage_type": "WebPage",
        "name": "Privacy Policy | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Privacy Policy", "privacy.html")],
    },
    "sitemap.html": {
        "webpage_type": "WebPage",
        "name": "Sitemap | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Sitemap", "sitemap.html")],
    },
    "equal-opportunity.html": {
        "webpage_type": "WebPage",
        "name": "Equal Opportunity Employer | Twin Cities Gun & Pawn",
        "breadcrumb": [("Home", "index.html"), ("Equal Opportunity Employer", "equal-opportunity.html")],
    },
}
