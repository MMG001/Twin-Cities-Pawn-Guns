# Indexing Diagnostic & Fix Runbook — Twin Cities Gun & Pawn

**Site:** https://twin-cities-pawn-guns.pages.dev
**Repo:** MMG001/Twin-Cities-Pawn-Guns (branch `main`)
**Date:** September 30, 2026
**Symptom addressed:** pages sitting in Google Search Console as **"Crawled — currently not indexed."**

---

## TL;DR — the honest verdict

I ran your runbook as a **measured diagnostic** against the actual built HTML, step by step. The headline result:

> **This is NOT a duplicate-content problem.** The runbook is written mainly for sites with dozens of near-identical *city / location* landing pages. Your site is a **single-location business with topically distinct pages**, and the measurements confirm the pages are genuinely different once boilerplate is removed. **So the fix is NOT to rewrite your pages** — doing that would risk the content that is already good.

What the measurements *did* surface as legitimately worth fixing was **thin contextual internal linking** on the resource guides (Step 2). That has been fixed and pushed this session. The technical indexability checks (Step 3) all came back **clean**.

Two honesty caveats up front, because they bound everything below:

1. **I have no access to your Google Search Console.** I cannot see *which specific URLs* Google flagged, cannot read the Page Indexing report, and cannot submit URLs for indexing. Those steps (Step 4) are things **you** must do in GSC — I've written them out precisely.
2. **The live site was unreachable from this sandbox** (network returns HTTP 000). So every check below was run against the **built HTML in the repo** — which *is* the exact source that Cloudflare Pages deploys, but it is not a live fetch of the deployed page. Where that distinction matters, I say so.

---

## Step 0 — Measure duplication (is duplication even the cause?)

The runbook's first instruction is to *measure* before assuming. I did two passes.

**Pass 1 (naive):** full visible text of each page, 5-word shingles, Jaccard similarity. This produced high numbers — but they were **inflated by boilerplate** (the shared nav, ticker, footer, and hours/location block appear on every page). That is a measurement artifact, not real duplication.

**Pass 2 (correct):** isolate only the `<main>` content body, strip city/geo tokens, then compute 5-word-shingle Jaccard similarity between every pair of content pages. This is the number that actually matters.

**Result — pairwise content similarity (main body only):**

| Page | Similarity vs. rest of site |
|---|---|
| about.html | ~8.2% |
| rules-for-pawning.html | ~8.4% |
| gun-license-mn.html | ~6.9% |
| unregistered-gun.html | ~5.5% |
| gun-law-checklist.html | ~6.5% |
| faq-gun-pawns.html | ~10.5% |
| pawn-loans.html | ~19.1% |
| index.html | ~22.9% |

**Runbook threshold:** below ~40% overlap → duplication is *not* the cause. **Every page is far below that.** The two highest (index and pawn-loans) are elevated only because they legitimately restate the core service vocabulary ("pawn loan", "firearm", "Twin Cities") — which is expected and healthy, not duplication.

**Thin pages noted (by design, not a defect):** sitemap (164 words), equal-opportunity (187), employment (211), resources (253), privacy (265). These are utility/legal pages; being short is normal for their type and is not what triggers "crawled — not indexed" on content pages.

**Conclusion for Step 0:** Skip Step 1 (make pages unique) entirely — the pages are already unique. Proceed to Steps 2 and 3.

---

## Step 1 — Make pages unique

**Skipped, deliberately.** Step 0 proved the pages are already distinct. Rewriting them would be effort spent against a non-problem and would put good content at risk. No changes made here.

---

## Step 2 — Strengthen internal links from indexed pages ✅ FIXED

This is the one place the measurements found a real, fixable weakness.

**How I measured it:** for every page, count inbound links, separating (a) *boilerplate* inbound (nav + footer, which every page gets automatically) from (b) *contextual* inbound — links that sit inside another page's `<main>` content. Contextual links are the ones Google weighs most for discovering and valuing a page.

**Finding:** no orphan pages (every page had 17 boilerplate inbound links), **but** several resource guides had very thin *contextual* inbound linking — Google was reaching them only through the nav/footer, which is a weak signal.

**Fix applied:** added a contextual **"Related Pages"** module to the resource guides, generated from the source (`build_pages.py` → `info_page()`), so it survives regeneration. Mappings:

- **rules-for-pawning** → Pawn Loans, Gun License in MN, Gun Pawn FAQ
- **gun-license-mn** → Guns & Rifles, Rules for Pawning, Unregistered Firearms
- **unregistered-gun** → Gun License in MN, 2026 MN Gun Law Checklist, Guns & Rifles

**Measured before → after (contextual inbound links):**

| Page | Before | After |
|---|---|---|
| guns-rifles.html | 5 | **7** |
| gun-license-mn.html | 4 | **6** |
| pawn-loans.html | 5 | **6** |
| rules-for-pawning.html | 5 | **6** |
| unregistered-gun.html | 2 | **3** |
| faq-gun-pawns.html | 2 | **3** |
| gun-law-checklist.html | — | **4** |

**Verification:** regenerated all 18 pages, `check_schema.py` → **ALL PASS (18/18)**; confirmed the "Related pages" section renders on all three guides; re-ran the link-count script to produce the "after" column above. Committed and pushed (`0e79a22`).

---

## Step 3 — Technical indexability check ✅ ALL CLEAN

Every technical blocker the runbook lists was checked against the built HTML:

| Check | Result |
|---|---|
| `noindex` meta tag anywhere | **None** — no page contains `noindex` |
| `X-Robots-Tag: noindex` in `_headers` | **None** — headers file is clean |
| robots.txt disallow rules | **None blocking** — robots.txt allows all crawlers; points to sitemap |
| `<meta name="robots">` per page | **Present** = `index, follow` on all 19 built pages |
| Self-referencing canonical | **Present & correct** on every page |
| Content in raw HTML (not JS-injected) | **Confirmed** — full text is in server HTML (e.g. index `<main>` ≈ 5,060 chars). JavaScript only *defers the Google Maps iframe* (main.js) — no content depends on JS |
| sitemap.xml accuracy | **18 URLs = 18 production pages**; `font-mockup.html` correctly excluded |

**Conclusion:** there is no technical reason Google *can't* index these pages. "Crawled — currently not indexed" here is a **quality/priority judgment by Google**, not a crawl block — which is consistent with the Step 0 finding (unique but modest-authority pages on a young site).

### One structural nuance for you to decide (not forced)

The homepage is reachable at **both** `https://…/` and `https://…/index.html`:

- Schema `WebSite.url` uses the bare `/`
- The homepage canonical, schema `@id`, and sitemap entry use `/index.html`
- 58 internal links point to `href="index.html"`

Google can crawl the home content at two URLs. This is **not** currently causing an indexing failure, but canonicalizing the homepage to one form (bare `/` is the conventional choice) is a tidy long-term improvement. Because it's a structural URL change touching ~58 links, the sitemap, and schema `@id`s, **I did not make it unilaterally** — tell me if you want it and I'll do it cleanly in one pass.

---

## Step 4 — Submit for indexing (YOUR steps — I cannot do these)

I have **no GSC access**, so these are for you to run in Google Search Console for the `twin-cities-pawn-guns.pages.dev` property:

1. **Confirm the flagged URLs.** Open **Indexing → Pages → "Crawled — currently not indexed"** and note exactly which URLs are listed. (I've been diagnosing the whole site; this tells us if it's the resource guides specifically.)
2. **Re-submit the sitemap.** Indexing → Sitemaps → submit `https://twin-cities-pawn-guns.pages.dev/sitemap.xml` (it now reflects the current 18 pages).
3. **URL Inspection + Request Indexing** for each flagged URL, *after* the new deploy is live (verify the "Related Pages" section is visible on the deployed guide first). Do a handful per day; don't mass-spam requests.
4. **Prioritize** the pages that now have stronger internal links (gun-license-mn, unregistered-gun, rules-for-pawning) — the improved contextual linking is a fresh signal for Google to re-evaluate them.

---

## Step 5 — Monitor (YOUR ongoing steps)

- Give Google **2–4 weeks**; "Crawled — not indexed" reversals happen on Google's crawl schedule, not on demand.
- Watch the GSC Pages report for URLs moving from "Crawled — not indexed" → "Indexed."
- If specific pages are *still* stuck after a month **and** GSC shows them under a "Duplicate" bucket (not the generic "crawled" one), come back and we'll do a targeted content-differentiation pass on just those URLs — but only with GSC evidence pointing there.

---

## What was changed this session (for your records)

| Commit | What |
|---|---|
| `5c2f20e` | Canonical name → "Twin Cities Gun & Pawn" across schema, titles, OG, page copy (prior turn) |
| `0e79a22` | **Contextual "Related Pages" internal-linking module added to resource guides** (this runbook, Step 2) |

**All edits were made to the source generators** (`build_pages.py`), then regenerated — so they survive future rebuilds. No generated `.html` was hand-edited.

---

## Honest limits of this report

- **No Google Search Console access** → I cannot confirm *which* URLs Google flagged, cannot read the Page Indexing report, and **cannot submit or "request indexing."** Steps 4–5 are yours.
- **Live site unreachable from this environment** (HTTP 000) → all checks ran against the **built HTML in the repo**, which is the exact deploy source, but is not a live fetch of the deployed page. Re-verify the deployed pages in a browser after Cloudflare finishes building commit `0e79a22`.
- **I am not claiming the indexing issue is "fixed."** Reversing "Crawled — currently not indexed" is Google's decision and takes crawl cycles. What I *can* verifiably claim: duplication was measured and ruled out, internal linking was measurably strengthened, and no technical indexability blocker exists in the source.
