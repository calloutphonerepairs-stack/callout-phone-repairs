# Call Out Phone Repairs — Production Build (QA pass 2)

Hand-built static website — vanilla HTML, CSS, minimal JavaScript, ready for Cloudflare Pages. No frameworks, no page builder, no third-party runtime dependencies.

See `CHANGELOG.md` for every change, `TEST-RESULTS.md` for verification evidence, and `UNRESOLVED.md` for the only items needing your input.

---

## Exact counts (verified after final rebuild)

- **Indexable pages:** 27
- **System pages:** 1 (custom `/404.html`, `noindex`, excluded from sitemap)
- **Total HTML files:** 28
- **Sitemap URLs:** 27 — every canonical is in the sitemap (0 mismatches); every sitemap URL has a file (0 missing)

---

## Design system (light/blue)

Premium 2026 technology aesthetic — Linear/Vercel/Stripe/Apple-inspired. Light, spacious, professional.

- Background `#F8FAFC` · cards `#FFFFFF` · structure/borders `#E2E8F0` · text `#0F172A` / `#475569`
- **Single site accent `#2563EB`** for buttons, links, active states, icons.
- **Colour honesty:** blue is the single *site* accent. WhatsApp green is used only as the external WhatsApp brand/action colour (a recognised affordance), not a second decorative accent. The solid-blue **"Get a Quote"** button is the only solid-blue block on any screen, so it stays the dominant commercial action.
- Bento-style sections; one dark navy CTA band + footer for contrast.
- **Self-hosted fonts** (Inter + Space Grotesk, Latin woff2 subsets, ~124 KB) — no Google Fonts, no third-party requests.
- Bespoke inline SVG illustration only — no photography, no stock, no fabricated repair evidence.
- Branded **1200×630** social-share image (`/assets/img/og-cover.png`), redesigned with a safe two-column layout (text left, phone right, 96 px gap — no overlap at full size or thumbnail).
- **Forced-colors (Windows High Contrast) support** in CSS.

---

## Security headers

`_headers` ships a **Content-Security-Policy** with no `unsafe-inline` for scripts: the one tiny inline bootstrap script (adds the `js` class) is allowed via a **SHA-256 hash**. Verified: the page runs with the CSP applied, zero CSP violations, fonts and the external `assistant.js` all load. Also: `nosniff`, `SAMEORIGIN`, `Referrer-Policy`, `Permissions-Policy`. Asset caching is revalidated (`max-age` + `must-revalidate`) for CSS/JS/images so an unversioned file can't be served stale; only the content-stable font files are `immutable`.

---

## Progressive enhancement (verified with JS disabled)

The quote assistant is real progressive enhancement:

- **No JavaScript:** a complete, usable enquiry form is the default — name, phone, a visible **repair `<select>`**, phone make/model, town/postcode, email, preferred contact, description, photo, consent — plus immediate WhatsApp and Call. Native browser validation is active (no source-level `novalidate`). Submitting posts to the Pages Function like any normal form.
- **JavaScript on:** the plain form is hidden and relocated into a stepped app-like flow (brand → model → repair → location → finish), with a pre-filled WhatsApp path, Call, or the same form as "send my details". JS sets `noValidate` after init so only the custom inline validation shows.

Verified in a browser with `java_script_enabled=false`: plain form + repair select + WhatsApp + Call all visible/usable; stepped flow hidden. The backend requires only name/phone/town/consent (all visible in the no-JS form); `brand`/`model` are optional.

---

## Forms & email (Resend — production-ready)

`functions/quote.js` performs full server-side validation, blocks spam (honeypot + server checks), and never fails silently. Email delivery uses **Resend**, with the API key read from the `RESEND_API_KEY` environment variable — never hardcoded, never sent to the browser (the function runs only on Cloudflare's edge). Photo upload has been removed for launch — customers are directed to send photos via WhatsApp instead.

Behaviour (verified against the real function via a Node harness):
- **Valid submit + working key** → sends via Resend to `calloutphonerepairs@gmail.com`, `Reply-To` set to the customer's email (when supplied) → `200 {ok:true}` → success screen.
- **RESEND_API_KEY missing** → `503 {error:"not_configured"}` with a friendly message → the UI shows the WhatsApp/Call fallback (no crash, no false success).
- **Provider/delivery error** (e.g. bad key, Resend down) → `502 {error:"delivery"}` → WhatsApp/Call fallback, entered data preserved.
- **Missing name / consent / bad phone** → `400` validation.
- **Honeypot filled** → `200` silent (bot handling), no delivery.

The client treats every non-2xx the same way — show the error state, keep the data — so all of the above degrade gracefully.

**No-JavaScript submitters** never land on raw JSON: the Function detects a normal browser form navigation (via `Sec-Fetch-Mode: navigate` / `Accept: text/html`) and returns a proper styled **HTML success or error page** with WhatsApp/Call fallback links. JavaScript submitters get JSON exactly as before (the JS experience is unchanged).

**Sender:** `Website Enquiries <quotes@send.calloutphonerepairs.co.uk>` (must be on a domain verified in Resend). See **Post-deploy configuration** below for the exact Cloudflare + Resend + DNS steps.

> **Not yet tested live:** real email delivery has **not** been tested end-to-end, because that requires a verified Resend domain and a real `RESEND_API_KEY` that only exist after deployment. The function's logic (validation, honeypot, missing-key handling, JSON vs HTML responses, and a real HTTP call to Resend that correctly reports failure rather than false success) has been verified with a local test harness. Do the live delivery test after completing "Post-deploy configuration".

---

## Deploying to Cloudflare Pages (GoDaddy domain)

This site uses a **Cloudflare Pages Function** (`functions/quote.js`) for the form. Pages Functions are activated automatically when a **`functions/` directory exists at the root of what you deploy** — there is no separate "enable functions" switch and no build step. The two things that matter: deploy the folder so that `functions/` and `index.html` sit at the **deploy root**, and never exclude `functions/`.

1. **Cloudflare** → add site `calloutphonerepairs.co.uk`.
2. Set the two Cloudflare **nameservers** at **GoDaddy** (Domain → DNS → Nameservers → Custom). Up to 24h to propagate.
3. **Workers & Pages → Create → Pages.** Choose one method:
   - **Direct upload (simplest):** upload the contents of this site folder (the folder that contains `index.html`, `functions/`, `assets/`, `_headers`, `_redirects`). No build command, no framework preset. Cloudflare detects `functions/` and deploys the `/quote` route automatically.
   - **Git:** connect a repo whose root contains `index.html` and `functions/`. Framework preset = **None**, Build command = **(empty)**, Build output directory = **`/`** (the repo root). Functions deploy automatically from `functions/`.
4. Set the **custom domain** to the apex `calloutphonerepairs.co.uk`. Cloudflare issues HTTPS automatically.
5. Set the **`RESEND_API_KEY`** environment variable (see "Post-deploy configuration" below), then redeploy so the Function picks it up.
6. `_redirects` (included): reliably redirects `www` → apex (path-based, single-hop, preserves path/query). It also contains a `*.pages.dev` rule, but that host-based rule is **not reliably supported** by `_redirects` — use a **Bulk Redirect** for the preview host instead (see "Post-deploy configuration → E").
7. `_headers` (included): CSP + security headers, revalidated asset caching, immutable fonts with CORS.
8. Live: run Lighthouse on the real URL, submit `sitemap.xml` to Google Search Console + Bing, and send one real test enquiry (see below).

### About the `/build/` folder
`/build/` contains the Python generators used to produce the HTML — it is **not** runtime code and is never served as a page or a function (Pages only turns `functions/` into routes). You can either upload the folder as-is (harmless; nothing links to it) or omit `/build/` when uploading. **Do not omit `functions/`** — that is the form's server code. If you prefer a clean production upload, deploy everything **except** `/build/` and the `*.md` docs.

### Verifying the Function deployed
After the first deploy, visit `https://<your-domain>/quote` directly with a browser (a GET). You should get **405 Method Not Allowed** (the Function is live and only accepts POST). A **404** there means `functions/` was not at the deploy root — re-check step 3.

---

## Project structure & rebuilding

- Deployable site: everything except `/build/`.
- `/build/`: Python generators. Tokens in `assets/css/main.css`; shared header/footer/nav in `partials.py`; components in `components.py`; page generators in `build*.py`; OG image in `make_og.py`; audits in `audit.py` + `audit_qa.py`.
- Rebuild: `cd build && python3 build.py && python3 build_services.py && python3 build_repairs.py && python3 build_areas.py && python3 build_pages.py && python3 build_tech.py` (and `python3 make_og.py` to regenerate the social image).

---

## Verification headline (full detail in TEST-RESULTS.md)

28 pages, 0 broken links, 0 console errors, 0 failed requests. One `<h1>` per page; unique titles/descriptions; canonical↔sitemap parity. Schema valid (single coherent homepage `@graph`; no `priceRange`; no `FAQPage`). No-JS form + JS assistant both verified; false-success impossible. 126 responsive checks (7 viewports) with no overflow. Accessibility: skip link, keyboard dropdowns, mobile-menu ARIA + Escape, form `aria-describedby`/`aria-invalid`, 44px touch targets, 400%/320px reflow, reduced-motion, forced-colors. Self-hosted fonts load under CSP; local LCP ~0.19s, CLS 0.

---

## Post-deploy configuration — Cloudflare, Resend & DNS

Do these **after** the site is deployed to Cloudflare Pages and the domain is on Cloudflare. The code is already production-ready; these steps activate email delivery.

### A. Resend — verify the sending domain
1. Create a Resend account and add the domain **`send.calloutphonerepairs.co.uk`** (a dedicated subdomain for transactional mail — keeps it isolated from any mail on the root domain).
2. Resend will show a set of **DNS records to add**. Add all of them in Cloudflare DNS (Cloudflare dashboard → your domain → DNS → Records). They are typically:
   - **MX** record for `send` (Resend's mail host).
   - **TXT (SPF)** for `send` — e.g. `v=spf1 include:amazonses.com ~all` (use the exact value Resend gives).
   - **TXT (DKIM)** — usually a `resend._domainkey.send` CNAME/TXT (use Resend's exact record).
   - Recommended: a **DMARC** TXT at `_dmarc.send` — e.g. `v=DMARC1; p=none; rua=mailto:calloutphonerepairs@gmail.com`.
   - Set these DNS records to **DNS only** (grey cloud) in Cloudflare, not proxied.
3. Wait for Resend to show the domain as **Verified** (DNS can take a few minutes to a few hours).
4. Create a Resend **API key** (Resend dashboard → API Keys). Copy it — you'll paste it into Cloudflare next. Treat it like a password.

### B. Cloudflare Pages — set the environment variable
1. Cloudflare dashboard → **Workers & Pages** → your Pages project → **Settings** → **Environment variables**.
2. Add a variable:
   - **Name:** `RESEND_API_KEY`
   - **Value:** the Resend API key from step A4
   - Add it to **both Production and Preview** environments (so preview deploys work too).
   - Use the **Encrypt** option so it's stored as a secret.
3. **Redeploy** the Pages project (env vars only take effect on a new deployment) — either push a commit or use "Retry deployment" / "Create deployment".

### C. Confirm the sender address matches
The function sends **from** `Website Enquiries <quotes@send.calloutphonerepairs.co.uk>`. The mailbox part (`quotes@`) doesn't need to exist as a real inbox — Resend only requires the **domain** (`send.calloutphonerepairs.co.uk`) to be verified. If you'd prefer a different verified sender, change the `FROM` constant at the top of `functions/quote.js` and redeploy. Replies go to the **customer** (Reply-To), and the enquiry itself is delivered to `calloutphonerepairs@gmail.com`.

### D. Final deployment steps (recap)
1. Deploy the site folder to Cloudflare Pages so `index.html` and **`functions/`** sit at the deploy root (static; framework preset None; no build command; build output directory `/`). `/build/` and the `*.md` docs can be omitted, but **never omit `functions/`**.
2. Point the apex domain `calloutphonerepairs.co.uk` at the Pages project; Cloudflare issues HTTPS.
3. Add the Resend DNS records (A) and set `RESEND_API_KEY` (B), then redeploy.
4. Verify the Function: GET `https://calloutphonerepairs.co.uk/quote` should return **405** (live, POST-only). A 404 means `functions/` wasn't at the root.
5. Submit a real test enquiry:
   - With a working key → you should receive the email at `calloutphonerepairs@gmail.com`; hit **Reply** and confirm it addresses the customer's email.
   - Before the key is set → the form shows the WhatsApp/Call fallback, never a false success.
6. Submit `sitemap.xml` to Google Search Console and Bing.

### E. Preventing duplicate indexing of the `*.pages.dev` preview host — read this
Cloudflare Pages gives every project a `your-project.pages.dev` hostname. The included `_redirects` file has a rule aimed at it, **but `_redirects` matches on path, not hostname, so a host-based `*.pages.dev` rule is not officially supported and may not fire.** Don't rely on it alone. Use one (ideally both) of these:
- **Bulk Redirects (recommended, reliable):** Cloudflare dashboard → your account → **Bulk Redirects** → create a list and a rule: **Source** `https://your-project.pages.dev/*` → **Target** `https://calloutphonerepairs.co.uk/$1`, status **301**, with **Subpath matching** on, and **Preserve path suffix** and **Preserve query string** both enabled. Enable the rule. This runs at the zone level and reliably redirects the preview host.
- **Access policy / disable the preview alias:** in Pages project → Settings, you can restrict preview deployments so the `*.pages.dev` host isn't publicly indexable.
Your page canonical tags already point to the apex domain, which further discourages indexing of the preview host, but the Bulk Redirect is the dependable fix.

### Quick reference
| What | Value |
|------|-------|
| Env var name | `RESEND_API_KEY` (Cloudflare Pages, Production + Preview, encrypted) |
| Sender (`FROM`) | `Website Enquiries <quotes@send.calloutphonerepairs.co.uk>` |
| Verified domain (Resend) | `send.calloutphonerepairs.co.uk` |
| Delivered to | `calloutphonerepairs@gmail.com` |
| Reply-To | the customer's submitted email (when provided) |
| DNS records | MX + SPF (TXT) + DKIM + DMARC (recommended) on `send.` — from Resend, added in Cloudflare, DNS-only |
