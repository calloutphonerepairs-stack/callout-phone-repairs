# Change Log — QA Correction Pass 2

Every change was made in the shared sources / generators and the whole site was rebuilt, so the fixes survive a rebuild. Items map to the 14-point review.

## 1. No-JavaScript form — completed and proven
- Removed source-level `novalidate` so native validation works with JS off; JS sets `noValidate` after init so only custom inline errors show.
- The no-JS default form now has a **visible repair `<select>`** and a visible phone make/model field (replacing hidden brand/model inputs).
- Proven against the **real Pages Function** (Node harness): valid no-JS submit passes validation and returns 502 (email unconfigured, not a false success); missing name/consent and bad phone return 400; honeypot returns 200 silently. Backend requires only name/phone/town/consent — all visible in the no-JS form.

## 2. Social-share (OG) image — redesigned, no overlap
- New saved generator `build/make_og.py` produces a safe two-column layout: text confined to the left ~62% (right edge 744px), phone in the right zone (left edge 840px) — a 96px gap, so no overlap is possible.
- Verified visually at full 1200×630 **and** at social-card thumbnail sizes (438px, 260px): headline fully readable, phone clearly separated.

## 3. Service-area claims — reconciled with confirmed facts
- Removed all "nearby communities" / "surrounding communities/villages" wording and every specific unconfirmed place-name (Rhydyfelin, Upper Boat, Talbot Green, Llanharan, Miskin, Llwynypia, Penygraig, Clydach Vale, Treorchy, Ynyswen, Tynewydd, Aberaman, Cwmbach, Mountain Ash, Aberfan, Troedyrhiw, Dowlais, Ystrad Mynach, Bedwas, Llanbradach, Whitchurch, Llandaff, Radyr, Taffs Well, Hopkinstown, Graigwen, Cilfynydd, Glyncoch).
- Visible content now names **only the nine confirmed service areas**, matching the schema `areaServed` exactly. "Just outside?" copy says "send us your postcode and we'll confirm" instead of claiming coverage.

## 4. Asset caching — no stale unversioned files
- `_headers`: CSS/JS use `max-age=3600, must-revalidate`; images `max-age=86400, must-revalidate`. Only the content-stable font files remain `immutable` (a given weight's bytes never change; a new weight would be a new filename). No unversioned file is served long-immutable.

## 5. (Covered by 1/12) Form success/failure integrity retained
- Success requires HTTP 2xx **and** body `{"ok":true}`; unconfigured email → error state, data preserved. Re-verified this pass.

## 6. FAQ schema — one consistent decision (DISABLED)
- `faqpage_ld()` is a no-op; **0 `FAQPage` blocks** across all 28 pages. **20 pages keep visible FAQ sections** for users. Removed the earlier duplicate-injection path entirely (see below). Docs/blueprint updated to state "disabled", ending the retained-vs-disabled inconsistency.
- **Bug found & fixed this pass:** 11 pages previously emitted **two** `FAQPage` blocks (schema string + `page_shell` both injected). Root cause removed in `build_areas.py` (2 sites) and `build_pages.py` (2 sites).

## 7. Page-count reconciliation — consistent everywhere
- 27 indexable + 1 custom 404 = 28 HTML files; 27 sitemap URLs. Blueprint v1.3 inventory, URL list, and sitemap-count line all agree. (Stale "26" references remain only in the superseded v1.1/v1.2 blueprints, which are not shipped in the package.)

## 8. Inline script / CSP — hashed, no unsafe-inline for scripts
- `_headers` CSP: `script-src 'self' 'sha256-xMEne5xSNlgeOligOATNEvyFpyN5H3HG/E/qDyG8S5Y='`. Verified the hash matches the inline bootstrap byte-for-byte, and that with the CSP applied the page runs with **zero CSP violations**, inline script executes (`js` class applied), fonts load under `font-src 'self'`, and `assistant.js` runs under `script-src 'self'`.

## 9. Homepage schema — one coherent linked graph
- Homepage now emits a **single** JSON-LD block: an `@graph` containing Organization + WebSite + WebPage + LocalBusiness, linked by stable `@id`s (`#organization`, `#website`, `#webpage`, `#business`, `#logo`). Removed the duplicate standalone LocalBusiness block. Non-home pages (About/Contact) still use a standalone LocalBusiness with inline image/logo URLs.

## 10. (Fonts) Self-hosted — retained from pass 1
- Inter (400/500/600) + Space Grotesk (500/600/700), Latin woff2 subsets, `font-display: swap`, two above-the-fold weights preloaded. No Google Fonts. Verified loading under CSP.

## 11. Marketing copy — unsupported/informal phrasing tightened
- "on the spot" → "on-site"; "fixed/replaced at your door" → "at your home or workplace"; "a fresh battery brings it back to life/back" → "a replacement battery can restore normal running"; "get your sound working again" / "capture things clearly again" / "sort it/the camera out" → qualified "diagnose and repair where possible"; "while you wait" / "while you get on with your day" → "during the appointment".

## 12. Accessibility — verified and improved
- Skip link is the first focusable element; desktop dropdowns reveal on keyboard focus (`:focus-within`); mobile menu `aria-expanded` true/false + Escape closes and resets; form fields wired `aria-describedby` → error, invalid fields `aria-invalid="true"`, focus to first invalid, errors `role="alert"`; sticky-bar touch targets ≥44px; 320px and 400%-equivalent reflow with no horizontal scroll; reduced-motion respected.
- **Added:** `@media (forced-colors: active)` block (Windows High Contrast) keeping borders, a distinguishable primary CTA, and visible focus outlines. Verified the site renders with forced-colors emulated (h1/CTA visible, no overflow, no errors).

## 13. (Structural) — re-verified
- 28 pages, 0 broken internal links, one `<h1>` each, self-referencing canonicals, unique titles/descriptions, valid JSON-LD, 0 warranty wording, DEV markers comment-only.

## 14. Copy claim sweep — re-run
- 0 occurrences of warranty/guarantee/OEM/genuine-parts/premium/certified/expert/years-of-experience/same-day/24-7/free-quote/most-models. Only "genuine" appears on `/reviews/` in the honest sense ("genuine customer feedback") — correct, retained.

---

# Addendum — Form system completed (Resend)

Scope-limited change: **only `functions/quote.js` was modified.** No HTML, CSS, client JS, design, copy, URLs, or SEO changed (verified by diff — quote.js is the sole differing source file).

- Integrated **Resend** as the email provider in `sendEmail()` (replacing the placeholder that returned "not configured").
- API key read from **`env.RESEND_API_KEY`** — never hardcoded, never exposed to client JS or HTML (verified: 0 occurrences outside the server function).
- Sends enquiries to **`calloutphonerepairs@gmail.com`** from **`Website Enquiries <quotes@send.calloutphonerepairs.co.uk>`**.
- **Reply-To** set to the customer's submitted email when a valid-looking address is provided.
- Sends both **plain-text and HTML** bodies; all user values **HTML-escaped** to prevent injection.
- **Missing `RESEND_API_KEY`** → friendly **503 `not_configured`** (no crash); client shows WhatsApp/Call fallback.
- **Provider/delivery error** → **502 `delivery`**; **valid + working key** → **200 `{ok:true}`**. No false success possible.
- Kept existing honeypot, server-side validation (name/phone/town/consent), and clear JSON responses — unchanged.
- Client JS unchanged: it already treats every non-2xx as "show error + preserve data", so 503/502 degrade gracefully, with or without JavaScript.

**Verified (Node harness against the real function):** missing key→503; missing name/consent & bad phone→400; honeypot→200 silent; valid+fake key→ real Resend call → 502 delivery (not false success). `node --check` passes. Site audits still pass (28 pages, 0 broken links, schema valid).

Post-deploy configuration (Cloudflare env var + Resend domain/DNS) is documented in the README.


---

# Addendum — Launch-prep fix pass (targeted)

Scope-limited. Changed only: `functions/quote.js`, `build/components.py` (form), `assets/js/assistant.js` (removed file handler), `build/build_pages.py` (privacy copy), and documentation. No design, layout, colours, typography, URLs, page count, SEO, schema, internal linking or performance work touched.

1. **Cloudflare deployment docs corrected.** Rewrote the deploy section to be accurate for Pages Functions: `functions/` must sit at the deploy root (auto-detected; no build step); direct-upload and Git both documented with correct settings; added a "verify the Function" step (GET `/quote` -> 405). Clarified `/build/` may be omitted but `functions/` must not.
2. **`*.pages.dev` guidance corrected (real issue).** `_redirects` cannot reliably match the preview hostname; documented the proper **Bulk Redirect** workflow (subpath matching, preserve path suffix, preserve query string) as the dependable fix, with canonicals as backup.
3. **Contact form docs made accurate.** Kept the Resend implementation as-is (not rewritten). Added an explicit "**not yet tested live**" note — real delivery needs a verified Resend domain + real key that exist only post-deploy. Removed the stale "guards photo type/size" claim.
4. **Photo upload removed for launch.** Deleted the photo field from the form (`components.py`), the file-name handler (`assistant.js`), and all photo handling from `functions/quote.js` (0 photo references remain). Privacy Policy now directs customers to send photos via WhatsApp. Blueprint updated (quote-form fields, function architecture, privacy scope).
5. **No-JavaScript form no longer ends on raw JSON.** The Function now detects a normal browser navigation (`Sec-Fetch-Mode: navigate` / `Accept: text/html`) and returns a **styled HTML success/error page** with WhatsApp/Call fallback; JS submitters still receive JSON (JS experience unchanged). Verified via harness: cors->JSON, navigate->HTML for success, validation (400) and config (503).
6. **Docs reconciled.** README, CHANGELOG, TEST-RESULTS, UNRESOLVED and Blueprint updated to match the final state (photo removed; email built but not live-tested; deployment method correct).
