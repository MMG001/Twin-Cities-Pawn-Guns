# Website Knowledge & Context Readiness Audit

### Twin Cities Gun & Pawn — OKF-inspired structure & agent-legibility grade

**Industry:** Firearms retail / pawnbroker (FFL dealer)\
**Compliance context:** Firearms law (federal/state/local — disclaimer present), ADA/WCAG (relevant, not formally certified)\
**Audit type:** Post-build re-score (after page build + schema v3.1 + canonical/sitemap/image-optimization work)\
**Note on OKF:** Principles borrowed to judge a live site; this is **not** a claim of OKF compliance. Readiness ≠ ranking ≠ indexing.

---

## Inspection scope

**Assessed (read directly from disk — the exact files deployed via the build pipeline):** all 18 production pages — `index, about, guns-rifles, accessories, pawn-loans, contact, faq, faq-gun-pawns, employment, resources, rules-for-pawning, gun-license-mn, unregistered-gun, gun-law-checklist, terms, privacy, sitemap, equal-opportunity` — plus `robots.txt`, `sitemap.xml`, and the generator sources (`build.py`, `build_pages.py`, `tools/schema_config.py`, `tools/build_schema.py`, `tools/check_schema.py`).

**NOT assessed (state honestly):**

* **Live production rendering** — the deployed host `twin-cities-pawn-guns.pages.dev` returned **HTTP 000** from the audit environment (sandbox IP cannot reach that Cloudflare host; `google.com` returned 200, confirming general connectivity). All scores below are from the **local built HTML**, which the build pipeline copies verbatim to deploy. Live-only signals — real HTTP response headers/`_headers` behavior, production cache TTLs, actual rendered CLS, server compression — are **not assessed**.

* **Lighthouse field metrics** (Perf 86 / A11y 96 / Best-Practices 100 / SEO 100; CLS 0.181) are referenced **only** from the screenshots you supplied, not independently re-run here. They are cited as your evidence, not the audit's own measurement.

* No prior **baseline** audit run was recorded, so a true per-category **delta cannot be computed**. Where build work clearly moved a category, it's noted qualitatively.

---

## Overall grade: **C+ — 75.5 / 100**

Structurally excellent and highly machine-legible; held back by two concrete, fixable gaps — a **broken contact-form destination** and **zero agent/maintainer documentation** (no README / [AGENTS.md](http://AGENTS.md) / llms.txt) — plus one **entity-name inconsistency** between the visible metadata and the schema.

---

## Score table

| \# | Category | Weight | Score | Element-specific reason |
| --- | --- | --- | --- | --- |
| 1 | Metadata quality | 15% | **9/10** | Every page has `<title>`, `<meta description>`, self-referencing `<link rel=canonical>`, full Open Graph (`og:title/description/image/type=business.business/url/locale/site_name`), Twitter card, and geo meta (`geo.region=US-MN`, `geo.position=45.2619;-93.4499`). JSON-LD v3.1 on all 18 pages with a 52-entry `knowsAbout`. **–1:** `og:title`/`<title>` say "Twin Cities **Gun & Pawn**" while schema `name` = "Twin Cities **Pawn & Gun**" — an agent reading both gets two entity names. |
| 2 | Content structure & machine-readability | 20% | **9/10** | Clean semantic HTML: exactly one `<h1>` per page, ordered `<h2>`/`<h3>`, and real landmarks (`<header> <nav> <main> <section>×10 <article>×4 <footer>` on index). Meaning is in markup, not styling. An agent can parse without guessing. |
| 3 | Knowledge portability | 15% | **7/10** | Fully static HTML — no proprietary/JS-locked surface; JSON-LD, `sitemap.xml` (18 URLs), `robots.txt` all present and exportable. **–3:** no `llms.txt` or small OKF-style services bundle; agent-facing knowledge lives only inside per-page JSON-LD, nothing portable at a single well-known path. |
| 4 | Cross-linking & navigation | 15% | **9/10** | `BreadcrumbList` on all 18 pages; dense internal graph (index links to every page — contact ×8, guns-rifles ×7, pawn-loans ×6, resources cluster interlinked); `<nav aria-label="Main navigation">` with dropdowns. Clear hierarchy Home → Inventory/Resources → leaf. |
| 5 | Human readability & UX | 15% | **8/10** | 99 of 102 `<img>` have descriptive `alt`; the 3 empty-alt images are correctly decorative (`alt="" aria-hidden="true"` full-bleed CTA bg). All form controls use `<label for>`; `<meta viewport>` present; images `loading="lazy"`. **–2:** CLS 0.181 (your screenshot) from web-font swap on the hero — a real layout-shift/UX cost; and `pawn-loans` meta description is 183 chars (truncates in SERP). |
| 6 | Documentation & maintainability | 10% | **3/10** | **Genuinely absent:** no `README`, `AGENTS.md`/`CLAUDE.md`, or `llms.txt` anywhere in the repo (verified by find). A strong "edit generators, never generated HTML" convention exists in the code but is **undocumented** — a new coding agent would have to reverse-engineer it and risks editing generated files. `check_schema.py` is the one self-documenting guardrail. |
| 7 | Forms & interactive elements | 10% | **5/10** | Contact form is well-built structurally — `<label for>`+`id` on every field, `required`, correct `type=email/tel`, a `<select>` for subject. **–5:** `action="https://formspree.io/f/REPLACE_WITH_YOUR_ID"` is an **unconfigured placeholder — the form submits nowhere**; no data destination is documented, and there's no visible client-side validation/confirmation beyond native `required`. |

**Weighted total:** (9×1.5)+(9×2.0)+(7×1.5)+(9×1.5)+(8×1.5)+(3×1.0)+(5×1.0) = **75.5 / 100**

---

## Top 3 strengths

1. **Schema-on-every-page, integrity-checked.** All 18 pages carry a JSON-LD `@graph` (`WebSite → PawnShop → WebPage → BreadcrumbList` + Service/FAQ nodes), and `tools/check_schema.py` enforces `@id` integrity and "Rule 11" traps on each build. That's the single biggest agent-legibility asset — structured, validated, machine-queryable entity data.

2. **Textbook semantic + navigation structure.** One `<h1>`, ordered headings, real HTML5 landmarks, `BreadcrumbList` everywhere, and a dense internal link graph where every page is reachable and related pages cross-reference. An agent can build an accurate site relationship graph from the markup alone.

3. **Complete, consistent metadata surface.** Canonical + full Open Graph + Twitter + geo meta on every page, with matching OG image dimensions (1200×630) and alt text — clean social/agent preview data with no missing core fields.

---

## Top 5 prioritized fixes

1. **Wire up (or remove) the contact form destination.** _Problem:_ `contact.html` action is `formspree.io/f/REPLACE_WITH_YOUR_ID` — submissions go nowhere. _Why it matters (humans + agents):_ the primary conversion path is silently broken, and an agent inspecting the form cannot determine a real data destination. _Action:_ replace with the real Formspree (or other) endpoint in the generator, or swap to a documented `mailto:`/backend; then note the destination in a form comment.

2. **Reconcile the business name across metadata and schema.** _Problem:_ visible title/OG = "Twin Cities Gun & Pawn"; schema `name` = "Twin Cities Pawn & Gun". _Why it matters (agents):_ two names for one entity weakens entity resolution and citation confidence. _Action:_ pick one canonical name (with the other as schema `alternateName`) and make `schema_config.py` + page titles agree.

3. **Add an `llms.txt` (and a tiny services bundle).** _Problem:_ no single well-known machine-readable summary of who/what/where. _Why it matters (agents):_ `llms.txt` is the emerging front door for AI agents to cite services, hours, address, and page map without scraping 18 pages. _Action:_ generate `/llms.txt` from `schema_config.py` (name, address, phone, hours, services, key page URLs) as a build step.

4. **Add `README.md` + `AGENTS.md` documenting the build pipeline.** _Problem:_ the "edit generators, not generated HTML; run build_pages → build_schema → check_schema" workflow is undocumented. _Why it matters (agents + maintainers):_ a coding agent will otherwise edit generated `.html` and have changes silently overwritten on rebuild. _Action:_ a short `AGENTS.md` stating the golden rule, the build commands, and the source-of-truth files.

5. **Cut CLS and tidy two metadata edges.** _Problem:_ CLS 0.181 (hero font swap) exceeds the 0.1 "good" threshold; `pawn-loans` description is 183 chars; homepage canonical targets `/index.html` rather than `/`. _Why it matters (humans + ranking-adjacent):_ layout shift hurts UX and Core Web Vitals; over-length descriptions truncate. _Action:_ preload the hero font / reserve space with `font-display:optional` or sized containers; trim the description to ≤160 chars; canonicalize the homepage to the bare domain.

---

## Verdict

**The site is genuinely agent-ready at the content layer** — validated JSON-LD on every page, clean semantic structure, breadcrumbs, and a dense internal link graph mean an AI agent can parse the entity, its services, and its geography without guessing. What keeps it from an A is not structure but two operational gaps and one consistency slip: a **contact form that submits to an unconfigured placeholder**, **no agent/maintainer documentation** (README/AGENTS.md/llms.txt), and a **name mismatch between the visible metadata and the schema**. The single highest-impact next change is **fixing the contact-form destination** — it's the site's main conversion path and currently silently fails — immediately followed by **adding an `llms.txt` + `AGENTS.md`**, which together would lift Documentation and Portability and push the overall grade into the mid-B range on the next re-score.

_Re-run this audit against the live URL once the sandbox (or your machine) can reach `twin-cities-pawn-guns.pages.dev` to capture the live-only signals marked "not assessed."_