# Test Results — QA Pass 2 (verified against the actual files)

All tests run against the rebuilt site served over local HTTP (real document root), headless Chromium for behaviour, Node for the Pages Function, Python for static checks. Anything only verifiable on the live URL is marked **NOT VERIFIED (live-only)**.

## Content & inventory
| Test | Result |
|------|--------|
| Total HTML files | **28** ✅ |
| Indexable pages | **27** ✅ |
| Sitemap `<loc>` count | **27** ✅ |
| Canonicals present in sitemap | 27/27, 0 mismatches ✅ |
| Sitemap URLs with a file | 27/27, 0 missing ✅ |
| Duplicate titles / descriptions | 0 / 0 ✅ |
| One `<h1>` per page | 28/28 ✅ |
| Broken internal links | 0 (27 links resolved) ✅ |
| Visible `[CONFIRM]` markers | 0 ✅ |
| `DEV:` markers outside comments | 0 ✅ |
| Warranty/guarantee wording | 0 ✅ |
| Unverified model-range claims | 0 ✅ |
| Unconfirmed place-names in copy | 0 ✅ |
| Hours 08:00–20:00 consistent | 28/28 ✅ |
| Timing "45–60" always qualified "standard" | pass ✅ |

## Rendering & assets
| Test | Result |
|------|--------|
| Console errors across 28 pages | **0** ✅ |
| Failed network requests across 28 pages | **0** ✅ |
| Broken `<img>` (naturalWidth 0) | 0 ✅ |
| Responsive overflow (18 pages × 7 viewports = 126 checks; 320–1440px) | 0 overflow ✅ |
| Mobile landscape (844×390) overflow | none ✅ |
| Self-hosted fonts load (document.fonts.check) | Space Grotesk ✅, Inter ✅ |
| Google Fonts / third-party requests | 0 ✅ |

## Forms & JavaScript
| Test | Result |
|------|--------|
| No-JS: plain form + repair select + WhatsApp + Call visible | ✅ (tested `java_script_enabled=false`) |
| No-JS: stepped flow hidden | ✅ |
| With-JS: plain hidden, stepped shown | ✅ |
| Assistant full flow → 4 summary chips | ✅ |
| WhatsApp finish link pre-filled | ✅ |
| Repair value pre-filled into form from stepped flow | ✅ |
| Empty submit blocked; no success shown | ✅ |
| Unconfigured email → error state, NO false success | ✅ |
| Entered data preserved after failure | ✅ |
| Real Pages Function (Node): valid→502, missing name/consent→400, bad phone→400, honeypot→200 silent | ✅ |
| Real JS errors during flow | 0 ✅ |

## Forms — launch-prep fix pass (re-verified)
| Test | Result |
|------|--------|
| Photo field removed from form (no-JS and JS) | OK — 0 `#f-photo` / `type=file` / `name="photo"` in built HTML |
| Photo handling removed from `functions/quote.js` | OK — 0 photo references; `node --check` passes |
| No-JS submit -> HTML page (not raw JSON): success | OK — `Sec-Fetch-Mode: navigate` -> `text/html` |
| No-JS submit -> HTML page: validation error (400) | OK — `text/html`, 400 |
| No-JS submit -> HTML page: config error (503) | OK — `text/html`, 503 |
| JS fetch still receives JSON (unchanged) | OK — `Sec-Fetch-Mode: cors` -> `application/json` |
| GET `/quote` returns 405 (Function live, POST-only) | OK — Allow: POST |
| No-JS form still usable (name, repair select, submit, WhatsApp) | OK |
| JS assistant still works (4 chips, no photo field) after removal | OK — 0 real JS errors |
| Real email delivery to `calloutphonerepairs@gmail.com` | NOT VERIFIED (live-only) — needs verified Resend domain + real key post-deploy |

## SEO & structured data
| Test | Result |
|------|--------|
| JSON-LD parses on all pages | ✅ |
| Homepage: single coherent `@graph` (Organization+WebSite+WebPage+LocalBusiness, stable @id) | ✅ (1 block) |
| Duplicate schema entities on homepage | 0 ✅ |
| `priceRange` present | 0 ✅ |
| `FAQPage` blocks (disabled decision) | 0 ✅ |
| Visible FAQ sections retained | 20 pages ✅ |
| `og:image` + width/height/alt + `twitter:image`/alt | all indexable pages ✅ |
| OG image real 1200×630 raster, no overlap (full + 438px + 260px) | ✅ |

## Security headers
| Test | Result |
|------|--------|
| CSP script hash matches inline bootstrap byte-for-byte | ✅ (`sha256-xMEne5xSNlgeOligOATNEvyFpyN5H3HG/E/qDyG8S5Y=`) |
| Page runs with CSP applied — violations | 0 ✅ |
| Inline script executes under CSP (no `unsafe-inline` scripts) | ✅ (`js` class applied) |
| Fonts + assistant.js load under CSP | ✅ |
| Asset caching revalidated for CSS/JS/img; immutable only for fonts | ✅ |

## Accessibility
| Test | Result |
|------|--------|
| Skip link is first focusable | ✅ |
| Desktop dropdowns reveal on keyboard focus | ✅ (`:focus-within` → visible) |
| Mobile menu `aria-expanded` false→true→false + Escape | ✅ |
| Form fields `aria-describedby` → error; `aria-invalid` on error; focus to first invalid; `role="alert"` | ✅ |
| Sticky-bar touch targets ≥44px | ✅ |
| Reflow at 320px and 400%-equivalent, no h-scroll | ✅ |
| Reduced-motion respected (reveal stays visible) | ✅ |
| Forced-colors (High Contrast) renders (h1/CTA visible, no overflow, no errors) | ✅ |

## Performance (local — indicative only)
| Metric | Result |
|--------|--------|
| Homepage FCP/LCP (local) | ~0.19s (text hero) |
| CLS (observed) | 0 |
| Homepage transfer | ~173 KB, ~11 requests |

## NOT VERIFIED (live-only — cannot be done in a sandbox)
- Full Lighthouse (mobile+desktop) on the deployed Cloudflare URL for real-network LCP/INP.
- `www`→apex, `*.pages.dev`→apex, HTTP→HTTPS single-hop redirects (applied by Cloudflare/`_redirects` post-DNS-cutover).
- Real email delivery to `calloutphonerepairs@gmail.com` (pending provider — see UNRESOLVED.md).
- Rich-result eligibility in Google's live testing tools (schema is valid; eligibility is Google's call).
