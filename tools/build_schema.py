# -*- coding: utf-8 -*-
"""Build & inject Schema.org JSON-LD (v3.1) into every HTML page.

For each page defined in schema_config.PAGES this script:
  1. Assembles a per-page @graph (WebSite + PawnShop + WebPage + BreadcrumbList
     + Service nodes at the correct level + optional FAQPage / Action nodes).
  2. Removes any existing <script type="application/ld+json"> block (DOTALL).
  3. Inserts the freshly-built block immediately before </head>.

Run: python3 tools/build_schema.py
"""
import copy
import json
import os
import re
import sys

# Allow running from repo root or from tools/.
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import schema_config as cfg  # noqa: E402

ACTION_PLATFORMS = [
    "http://schema.org/DesktopWebPlatform",
    "http://schema.org/MobileWebPlatform",
]

LD_SCRIPT_RE = re.compile(
    r'[ \t]*<script type=["\']application/ld\+json["\']>.*?</script>\n?',
    re.DOTALL | re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Node builders
# ---------------------------------------------------------------------------
def build_website():
    return copy.deepcopy(cfg.WEBSITE)


def build_business():
    return copy.deepcopy(cfg.BUSINESS)


def build_webpage(slug, page):
    node = {
        "@type": page["webpage_type"],
        "@id": cfg.u(slug + "#webpage"),
        "url": cfg.u(slug),
        "name": page["name"],
        "isPartOf": {"@id": cfg.u("#website")},
        "about": {"@id": cfg.u("#business")},
        "inLanguage": "en-US",
        "breadcrumb": {"@id": cfg.u(slug + "#breadcrumb")},
    }
    if page.get("description"):
        node["description"] = page["description"]
    if page.get("primary_image"):
        node["primaryImageOfPage"] = {
            "@type": "ImageObject",
            "url": cfg.u(page["primary_image"]),
        }
    if page.get("main_entity"):
        node["mainEntity"] = {"@id": cfg.SERVICES[page["main_entity"]]["id"]}
    return node


def build_breadcrumb(slug, page):
    items = []
    for i, (name, target) in enumerate(page["breadcrumb"], start=1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": cfg.u(target),
        })
    return {
        "@type": "BreadcrumbList",
        "@id": cfg.u(slug + "#breadcrumb"),
        "itemListElement": items,
    }


def service_level(key, slug):
    """Return 'full', 'card' or 'stub' for a service on a given page."""
    svc = cfg.SERVICES[key]
    if slug == svc["own_page"]:
        return "full"
    if slug == "index.html" and key in cfg.INDEX_CARD_SERVICES:
        return "card"
    return "stub"


def build_service(key, slug):
    svc = cfg.SERVICES[key]
    level = service_level(key, slug)

    # Nav-stub: @id, name, url, provider only.
    if level == "stub":
        return {
            "@type": "Service",
            "@id": svc["id"],
            "name": svc["name"],
            "url": svc["url"],
            "provider": {"@id": cfg.u("#business")},
        }

    # Shared fields for card + full.
    node = {
        "@type": "Service",
        "@id": svc["id"],
        "name": svc["name"],
        "serviceType": svc["serviceType"],
        "description": svc["desc_card"] if level == "card" else svc["desc_full"],
        "provider": {"@id": cfg.u("#business")},
        "url": svc["url"],
        "areaServed": {"@id": cfg.u("#service-area")},
        "category": copy.deepcopy(svc["category"]),
    }

    if level == "full":
        node["mainEntityOfPage"] = {"@id": cfg.u(slug + "#webpage")}
        related = svc.get("related") or []
        if related:
            node["isRelatedTo"] = [{"@id": cfg.SERVICES[r]["id"]} for r in related]

    return node


def build_faqpage(slug, html):
    """Extract visible Q&A accordion items and build an FAQPage node."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    questions = []
    for item in soup.select(".faq-item"):
        head = item.select_one(".faq-head")
        body = item.select_one(".faq-body")
        if not head or not body:
            continue
        # Question = first span in the head that is not the material icon.
        q_text = None
        for span in head.find_all("span"):
            classes = span.get("class") or []
            if "material-symbols-outlined" in classes or "faq-icon" in classes:
                continue
            q_text = span.get_text(" ", strip=True)
            break
        if q_text is None:
            q_text = head.get_text(" ", strip=True)
        a_text = body.get_text(" ", strip=True)
        if not q_text or not a_text:
            continue
        questions.append({
            "@type": "Question",
            "name": q_text,
            "acceptedAnswer": {"@type": "Answer", "text": a_text},
        })

    return {
        "@type": "FAQPage",
        "@id": cfg.u(slug + "#faqpage"),
        "mainEntity": questions,
    }


def build_action(kind):
    if kind == "ask":
        return {
            "@type": "AskAction",
            "name": "Request a Quote",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": cfg.u("contact.html#contact-form"),
                "actionPlatform": list(ACTION_PLATFORMS),
            },
        }
    if kind == "apply":
        return {
            "@type": "ApplyAction",
            "name": "Apply for Employment",
            "target": {
                "@type": "EntryPoint",
                "urlTemplate": cfg.u("employment.html#application-form"),
                "actionPlatform": list(ACTION_PLATFORMS),
            },
        }
    raise ValueError("Unknown action kind: %s" % kind)


# ---------------------------------------------------------------------------
# Graph assembly
# ---------------------------------------------------------------------------
def build_graph(slug, page, html):
    graph = [build_website(), build_business(), build_webpage(slug, page),
             build_breadcrumb(slug, page)]

    if page.get("faq"):
        graph.append(build_faqpage(slug, html))

    for key in cfg.SERVICE_ORDER:
        graph.append(build_service(key, slug))

    for kind in page.get("actions", []):
        graph.append(build_action(kind))

    return {"@context": "https://schema.org", "@graph": graph}


def inject(slug, page):
    path = os.path.join(ROOT, slug)
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()

    graph = build_graph(slug, page, html)
    payload = json.dumps(graph, indent=2, ensure_ascii=False)
    block = '  <script type="application/ld+json">\n%s\n  </script>\n' % payload

    # Remove any existing JSON-LD block(s).
    html = LD_SCRIPT_RE.sub("", html)

    # Insert before </head>.
    if "</head>" not in html:
        raise RuntimeError("No </head> in %s" % slug)
    html = html.replace("</head>", block + "</head>", 1)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)


def main():
    for slug, page in cfg.PAGES.items():
        inject(slug, page)
        print("injected %-26s (%d nodes)" % (
            slug, len(build_graph(slug, page, open(os.path.join(ROOT, slug), encoding="utf-8").read())["@graph"])))
    print("Done: %d pages." % len(cfg.PAGES))


if __name__ == "__main__":
    main()
