# Master Website Blueprint v1.3 — Call Out Phone Repairs

**Tagline:** We Come To You
**Canonical URL:** `https://calloutphonerepairs.co.uk/`
**Platform:** Static HTML / CSS / vanilla JavaScript, hosted on Cloudflare Pages
**Document status:** Master Website Blueprint v1.3 — Built & QA-corrected (second pass). Light/blue design system; illustration-led (no photography); no warranty claims; no unverified model-range or service-area claims; standard-screen timing wording enforced; self-hosted fonts; **FAQPage schema disabled** (visible FAQs retained); single coherent homepage @graph; CSP with script hash; forced-colors support.
**Last updated:** 11 July 2026

---

## Service-area honesty (v1.3)

Visible content names **only the nine confirmed service areas** (Pontypridd, Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly, Cardiff) — matching the schema `areaServed` exactly. Unverified "nearby communities" wording and specific unconfirmed place-names (e.g. individual villages/suburbs) were removed. Where someone may be just outside a named area, the copy says "send us your postcode and we'll confirm" rather than claiming coverage. This keeps visible claims == structured data == confirmed facts.

## Design system (v1.3 — approved, light/blue)

- **Palette:** page background `#F8FAFC`; white cards `#FFFFFF`; structural borders/dividers `#E2E8F0`; primary text `#0F172A`; secondary text `#475569`.
- **Single site accent:** `#2563EB` (blue), hover/active `#1D4ED8` — used for buttons, links, active states and icons. **Honest note (#9):** blue is the single *site* accent. **WhatsApp green (`#25D366`) is used only as the external brand/action colour on WhatsApp buttons** — a widely-recognised affordance — and is not a second decorative accent. The primary **"Get a Quote"** button is the only solid-blue block on any screen, so it stays the dominant commercial action; WhatsApp is the recognised secondary contact affordance.
- **Aesthetic:** Linear/Vercel/Stripe/Apple-inspired — spacious, subtle shadows, rounded corners, Bento-style sections (varied cell sizes, one feature cell, one deliberate dark anchor cell), one dark navy CTA band + footer for contrast rhythm.
- **Fonts:** self-hosted Inter + Space Grotesk (see 12).
- **Social sharing (#8):** a branded **1200×630** `og-cover.png` (light/blue, phone + restored-screen motif) is referenced via `og:image` (+ width/height/alt) and `twitter:image` (+ alt) on all indexable pages; `og:type` per page (website/article as appropriate).
- **Visuals:** bespoke inline SVG illustration only — no photography, no stock, no fabricated repair evidence. Alt text always names illustrations *as illustrations*.

---

## How to use this document

This is the single source of truth for the Call Out Phone Repairs website. Any experienced developer, SEO specialist, or designer should be able to build the site from this document alone. It defines every page, URL, heading, internal link, schema block, form, call to action, image slot, and technical requirement.

Two conventions used throughout:

- **(✎ provisional)** — a keyword target or metadata value that must be validated with live keyword research (Google Keyword Planner or equivalent) before it is locked. No search volumes have been invented anywhere in this document.
- **[CONFIRM] / [DEV MARKER]** — a factual detail (owner name, models covered, communities served, part descriptions, etc.) not yet verified. These appear only as internal HTML comments in code (e.g. `<!-- DEV: confirm owner name -->`), never as visible text to customers. Copy is written to be true and non-specific where a fact is unconfirmed, rather than inventing it. The register is in Section 15.

A short table of contents:

1. Primary objective and strategy
2. Confirmed business facts
3. Site architecture and page inventory
4. URL structure
5. Navigation
6. Internal linking strategy
7. Keyword map
8. Conversion strategy (CTAs, guided quote assistant, forms)
9. Form architecture and email delivery
10. Page-by-page briefs
11. Schema strategy
12. Technical SEO specification
13. AI-search optimisation
14. Performance and Core Web Vitals
15. The [CONFIRM] register
16. Cloudflare + GoDaddy deployment checklist
17. Pre-launch technical audit checklist
18. Post-launch and long-term growth

---

## 1. Primary objective and strategy

### 1.1 The single objective

**Generate the maximum number of genuine phone screen replacement enquiries across the coverage areas.**

Every decision in this document — architecture, layout, internal link, CTA, copy, schema, performance target — serves that one goal. Where a decision does not serve it, the decision is wrong.

Screen replacement is the primary commercial service because it is the highest-demand, highest-intent repair. The site is therefore built as a **topic cluster with screen repair as the core**, not as a flat list of equally weighted service pages.

### 1.2 The honest strategic position

The business is a **solo, mobile, call-out phone repair service based in Pontypridd**. This shapes what is realistic:

- **Organic search (blue links)** is the primary lever. Strong, genuinely useful, interlinked content can rank across all nine areas over time — including towns where the business has weak map-pack proximity.
- **The Google Business Profile map pack** is won mainly by proximity, reviews, relevance, and prominence. From a Pontypridd base, the business can compete strongly in the map pack for **Pontypridd and immediate RCT**, less so further out, and **not** in distant, competitive markets like Cardiff or Merthyr at launch. This is a physical reality that no schema, service-area entry, or on-page tactic overrides. The location pages for distant towns are an **organic** play, framed honestly.
- **Reviews are the compounding asset.** The site launches with zero reviews. A steady, genuine, ethically generated review stream — not an artificial burst — is the strongest long-term ranking and trust asset the business has. See Section 18.

### 1.3 What makes this site hard to outperform

Three things, in priority order:

1. **Topical authority on screen repair** — a genuine, deep, interlinked cluster (pillar + sub-pillars + model-level depth over time) that most local competitors do not build.
2. **Genuine local proof per area** — real reviews accumulating on each location page over time (and, later, genuine repair photos once the business has them), which no template or national competitor can fake. At launch, proof is illustration-led design plus honest copy; real proof is added as it is earned.
3. **Honesty as strategy** — plain, non-over-promising information (part options and repair details discussed with each customer before work begins), a real named person on the About page, realistic timings, and advice content. No warranty or guarantee is advertised at launch. This aligns with where both Google's helpful-content systems and AI answer engines are heading, and is the opposite of competitor overpromising.

### 1.4 The three roles this document is written from

Every brief has been written as a senior technical SEO consultant, senior UX/CRO specialist, and senior front-end developer would write it: no keyword stuffing, no thin pages, no unnecessary code, every section with a purpose, and current best practice throughout. Where the owner's brief could be improved, the improvement has been made and explained rather than followed blindly.

---

## 2. Confirmed business facts

These are confirmed and used consistently throughout the site. **NAP (Name, Address/Area, Phone) consistency is a local SEO factor** — these exact forms must appear identically on the website, the Google Business Profile, and every directory citation.

| Field | Value |
|---|---|
| Business name | **Call Out Phone Repairs** (exact spacing — never "Callout" or "Call-Out") |
| Tagline | **We Come To You** |
| Website (canonical) | `https://calloutphonerepairs.co.uk/` |
| Phone | **07347 715961** (display) · `tel:+447347715961` (link) |
| WhatsApp | **+44 7347 715961** · `https://wa.me/447347715961` |
| Email | **calloutphonerepairs@gmail.com** |
| Business type | Mobile call-out phone repair service (no public premises, no walk-ins) |
| Address | **Not published anywhere.** Service-area business; base address hidden on Google Business Profile and absent from the website. |
| Opening hours | **Monday–Sunday, 08:00–20:00.** Calls, WhatsApp responses, and repair appointments are handled daily 08:00–20:00. The website and quote form accept online submissions at any time. **No 24-hour / 24-7 claims anywhere.** |
| Coverage | Pontypridd (base) + Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly, Cardiff |

### 2.1 The availability framing rule (important)

Confirmed customer-facing hours are **Monday–Sunday, 08:00–20:00.** The business is a mobile call-out service by appointment, **not a walk-in shop.** Every reference to availability follows this pattern:

> Submit a quote request at any time. Calls, messages and repair appointments are handled daily between 08:00 and 20:00.

Rules for a future developer:

- **Never** state or imply that the business is open, contactable, or available 24 hours / 24-7.
- The **website and quote form accept online submissions at any time** — this is the only "any time" claim permitted, and it refers to form submission, not to calls, replies, or appointments.
- **Calls, WhatsApp responses, and repair appointments** are always framed as operating **08:00–20:00 daily**.
- Never imply a walk-in shop.
- Use **08:00–20:00** consistently in: visible copy, footer, the Contact page, `LocalBusiness` `openingHours` schema, and the Google Business Profile guidance.

### 2.2 The repair-experience framing rule (important)

The business is a **come-to-you** service. Most **standard** screen replacements are **completed on-site, with the customer present.** This is a core trust differentiator versus high-street shops that keep a phone for hours or days.

**Approved timing wording** (use as an honest expectation, not a guaranteed completion promise; adapt naturally — do not repeat verbatim on every page):

> Most standard screen replacements are normally completed on-site in around 45–60 minutes, depending on the device, fault and parts required. We confirm the expected repair time before starting.

**Do NOT apply the 45–60-minute statement** to any of the following unless separately confirmed:

- Foldable phones
- Complex Samsung screens (curved / AMOLED / foldable)
- Non-screen repairs (battery, charging port, camera, speaker)
- Diagnostic work
- Repairs where parts are unavailable

For these, describe the process honestly **without** a specific timing, or use a confirmed timing once provided.

**Repair-model rules:**

- We travel to the customer **by appointment**.
- Most **standard** screen repairs are completed **on-site**.
- We do **not** operate a public walk-in shop.
- **Do not** describe collection and return as the normal service.
- Unusual or complex repairs are **discussed case by case before the customer agrees**.
- **No absolute promises** ("always", "guaranteed in an hour"). Use "normally", "typically", "most standard repairs".
---

## 3. Site architecture and page inventory

The site is a **screen-repair topic cluster**. Screen repair is the pillar; iPhone and Samsung screen repair are sub-pillars; other repairs are secondary service pages; location pages carry local intent and funnel to the screen cluster; trust pages remove objections at the point of conversion.

### 3.1 Full page inventory (27 indexable pages + 1 system 404 = 28 HTML files)

| # | Page | Type | Primary role |
|---|---|---|---|
| 1 | Homepage | Core | Brand, "we come to you", screen-led hero, funnel to quote |
| 2 | Screen Repair | **Pillar** | Owns generic screen terms; cluster spine |
| 3 | iPhone Screen Repair | Sub-pillar | Owns iPhone screen terms |
| 4 | Samsung Screen Repair | Sub-pillar | Owns Samsung screen terms |
| 5 | Repairs (hub) | Service hub | Lists all non-screen repairs; prevents orphans; links the five service pages |
| 6 | Battery Replacement | Service | Secondary cluster |
| 7 | Charging Port Repair | Service | Secondary cluster |
| 8 | Camera Replacement | Service | Secondary cluster |
| 9 | Speaker Repair | Service | Secondary cluster |
| 10 | Phone Diagnostics | Service | Secondary cluster; entry point for "not sure what's wrong" |
| 11 | Areas We Cover | Location hub | Links all nine areas; coverage map; prevents orphans |
| 12 | Pontypridd | Location (flagship) | Owns "phone repair Pontypridd"; strongest proximity |
| 13 | Treforest | Location | Students + industrial estate angle |
| 14 | Pontyclun | Location | M4 commuter belt; Talbot Green |
| 15 | Tonypandy | Location | Rhondda Fawr commercial centre |
| 16 | Treherbert | Location | Rhondda valley-head; scarce local options |
| 17 | Aberdare | Location | Cynon Valley town |
| 18 | Merthyr Tydfil | Location | Large northern town; organic play |
| 19 | Caerphilly | Location | Commuter town; own centre |
| 20 | Cardiff | Location | City; hardest; long-game organic |
| 21 | How It Works | Trust/process | Honest process; on-site, ~45–60 min framing |
| 22 | Parts & Repair Information | Trust | Neutral: part options & details discussed with customer before work begins. NO warranty/guarantee claims. |
| 23 | About | Trust/E-E-A-T | Real, named, honest — solo technician |
| 24 | Reviews | Trust/social proof | Genuine reviews; grows over time |
| 25 | Contact | Trust/contact | Call, WhatsApp, email, hours, areas, form, no address |
| 26 | Get a Quote | Conversion | Guided assistant + form + WhatsApp/Call |
| 27 | Privacy Policy | Legal/GDPR | Consent, data handling; legal review required |

**System pages:** Custom 404 (`/404.html`, `noindex`, excluded from sitemap, returns true 404 status).

**Reserved but unpublished** (built into the architecture now so future expansion needs no redesign):

- `/for-business/` parent + `/for-business/business-repair/`, `/schools/`, `/insurance/`, `/fleet/`
- `/advice/` content layer (model-level screen guides and honest advice articles)

### 3.2 Architecture diagram

```
HOMEPAGE — Call Out Phone Repairs · We Come To You
│
├── SCREEN REPAIR ★ (pillar)
│   ├── iPhone Screen Repair (sub-pillar)
│   └── Samsung Screen Repair (sub-pillar)
│
├── REPAIRS
│   ├── Battery Replacement
│   ├── Charging Port Repair
│   ├── Camera Replacement
│   ├── Speaker Repair
│   └── Phone Diagnostics
│
├── AREAS WE COVER (hub)
│   ├── Pontypridd ★ (flagship)
│   ├── Treforest
│   ├── Pontyclun
│   ├── Tonypandy
│   ├── Treherbert
│   ├── Aberdare
│   ├── Merthyr Tydfil
│   ├── Caerphilly
│   └── Cardiff
│
├── HOW IT WORKS
├── PARTS & REPAIR INFORMATION
├── ABOUT
├── REVIEWS
├── CONTACT
├── GET A QUOTE
├── PRIVACY POLICY
└── 404 (noindex)

Reserved (unpublished): /for-business/*, /advice/*
```

---

## 4. URL structure

**Conventions (enforced site-wide):**

- Protocol + host: `https://calloutphonerepairs.co.uk` (non-www, HTTPS — the permanent canonical)
- **Trailing slash ON** for all directory URLs (matches Cloudflare Pages `index.html` serving, avoids an extra redirect hop). Homepage is the bare root `/`.
- Lowercase, hyphen-separated, no parameters in canonical URLs, no dates, no IDs.

```
https://calloutphonerepairs.co.uk/                          Homepage
https://calloutphonerepairs.co.uk/screen-repair/            Screen Repair (pillar)
https://calloutphonerepairs.co.uk/screen-repair/iphone/     iPhone Screen Repair
https://calloutphonerepairs.co.uk/screen-repair/samsung/    Samsung Screen Repair
https://calloutphonerepairs.co.uk/repairs/                   Repairs (hub)
https://calloutphonerepairs.co.uk/repairs/battery-replacement/
https://calloutphonerepairs.co.uk/repairs/charging-port-repair/
https://calloutphonerepairs.co.uk/repairs/camera-replacement/
https://calloutphonerepairs.co.uk/repairs/speaker-repair/
https://calloutphonerepairs.co.uk/repairs/phone-diagnostics/
https://calloutphonerepairs.co.uk/areas/                    Areas We Cover (hub)
https://calloutphonerepairs.co.uk/areas/pontypridd/
https://calloutphonerepairs.co.uk/areas/treforest/
https://calloutphonerepairs.co.uk/areas/pontyclun/
https://calloutphonerepairs.co.uk/areas/tonypandy/
https://calloutphonerepairs.co.uk/areas/treherbert/
https://calloutphonerepairs.co.uk/areas/aberdare/
https://calloutphonerepairs.co.uk/areas/merthyr-tydfil/
https://calloutphonerepairs.co.uk/areas/caerphilly/
https://calloutphonerepairs.co.uk/areas/cardiff/
https://calloutphonerepairs.co.uk/how-it-works/
https://calloutphonerepairs.co.uk/parts-and-repair-information/
https://calloutphonerepairs.co.uk/about/
https://calloutphonerepairs.co.uk/reviews/
https://calloutphonerepairs.co.uk/contact/
https://calloutphonerepairs.co.uk/get-a-quote/
https://calloutphonerepairs.co.uk/privacy-policy/
https://calloutphonerepairs.co.uk/404.html                 Custom 404 (noindex)

Reserved (unpublished):
https://calloutphonerepairs.co.uk/for-business/
https://calloutphonerepairs.co.uk/for-business/business-repair/
https://calloutphonerepairs.co.uk/for-business/schools/
https://calloutphonerepairs.co.uk/for-business/insurance/
https://calloutphonerepairs.co.uk/for-business/fleet/
https://calloutphonerepairs.co.uk/advice/
```

**Why `/screen-repair/` nests iPhone and Samsung:** the URL path physically encodes the pillar → sub-pillar hierarchy, reinforcing the topic cluster to crawlers. Services sit under `/repairs/` (kept separate so screen retains prominence rather than being buried among equals). Locations under `/areas/`.

---

## 5. Navigation

### 5.1 Primary navigation (desktop and mobile)

Screen repair is deliberately the **first** item and its own top-level entry — every navigation impression reinforces the commercial spine.

```
[Logo: Call Out Phone Repairs · We Come To You]

Screen Repair ▾          ← FIRST, commercial priority
  ├ iPhone Screen Repair
  └ Samsung Screen Repair
Repairs ▾
  ├ Battery Replacement
  ├ Charging Port Repair
  ├ Camera Replacement
  ├ Speaker Repair
  └ Phone Diagnostics
Areas We Cover ▾
  └ [nine areas]
How It Works
About
Reviews
[Get a Quote]            ← button-styled, high-contrast primary CTA
```

### 5.2 Persistent conversion elements (every page)

- **Floating WhatsApp button** — always visible on desktop and mobile. Pure HTML/CSS styled link to `https://wa.me/447347715961`. `aria-label="Contact us on WhatsApp"`. One of the primary CTAs. No animation that harms performance; near-zero cost.
- **Sticky mobile contact bar** — persistent at the bottom of the mobile viewport: **[Call] [WhatsApp] [Get a Quote]**. Three large tap targets. The primary mobile conversion mechanism.
- **Footer** — full crawlable link list (all services, all areas, all trust pages) plus the site-wide contact block (phone, WhatsApp, email, areas served, availability framing, Privacy link). Ensures no orphan pages and keeps contact one glance away.

### 5.3 Navigation accessibility

- Dropdowns are tap- and keyboard-accessible (not hover-only).
- `aria-current="page"` on the active page; `aria-expanded` on dropdown toggles.
- Visible focus states; skip-to-content link; semantic `<nav>` landmarks.
- Sticky bar and floating button must not trap focus or obscure content; they reserve their own space and never cause layout shift.

---

## 6. Internal linking strategy

Internal linking is one of the highest-leverage, fully controllable ranking systems, and it is built to concentrate relevance on screen repair. Rules are enforced site-wide.

### 6.1 The rules

**A. Screen cluster (concentrates screen relevance):**
- Screen pillar ↔ iPhone sub-pillar (two-way)
- Screen pillar ↔ Samsung sub-pillar (two-way)
- iPhone ↔ Samsung (sibling cross-link)
- Homepage hero → Screen pillar; all three link back to homepage

**B. Location → screen cluster (captures "[screen term] [town]" long-tails):**
- Every location page has a prominent screen-replacement section linking to the Screen pillar, iPhone page, and Samsung page, using descriptive keyword anchors ("iPhone screen replacement", "Samsung screen repair", "cracked screen repair"). This is how the site ranks for hundreds of "[screen term] [town]" combinations **without building a single doorway page for those combinations**.

**C. Location ↔ neighbouring location (local relevance web):**
- Pontypridd ↔ Treforest (adjacent)
- Tonypandy ↔ Treherbert (Rhondda corridor)
- Aberdare ↔ Merthyr Tydfil (Cynon/Taf corridor)
- Pontyclun ↔ Cardiff ↔ Caerphilly (commuter belt)
- All ↔ Areas hub

**D. Service → location:** service pages reference "across [areas]" linking to the Areas hub — not stuffed with nine town links.

**E. Trust pages support conversion:** How It Works, Parts & Repair Information, and Reviews are linked from every service and location page's decision section, answering objections at the point of conversion.

**F. Anti-cannibalisation (absolute):** one primary keyword per page; no two pages target the same term; anchor text matches the *target* page's primary keyword, never a term the *linking* page is trying to own.

**G. No orphans:** every page is reachable from navigation + footer + at least one contextual in-body link. Verified in the pre-launch audit.

**H. Anchor-text discipline:** varied, natural, descriptive. Never "click here". Avoid exact-match repetition (an over-optimisation and AI-spam signal). Mix "iPhone screen repair", "get your iPhone screen replaced", "iPhone screen replacement service".

### 6.2 Inbound link priority

The **Screen Repair pillar** should receive the most internal links of any page (from homepage, all nine location pages, both sub-pillars, and relevant service pages). The **Get a Quote** page and the flagship **Pontypridd** page are the next most-linked. Link equity is deliberately weighted toward screen.

---

## 7. Keyword map

**Every target below is (✎ provisional) until validated with live keyword research.** No search volumes are invented. One primary keyword per page; secondaries are covered naturally, never stuffed. Validate at minimum: `mobile phone repair South Wales`, `phone repair Pontypridd`, `mobile phone repair Pontypridd`, all screen-repair terms, and all nine location terms, before locking title tags and H1s.

| Page | Primary keyword (✎) | Key secondaries — natural coverage only (✎) |
|---|---|---|
| Homepage | mobile phone repair South Wales *(final choice pending validation — must reflect Pontypridd base + wider South Wales mobile service + strongest realistic commercial intent)* | we come to you phone repair, phone screen repair South Wales, mobile phone screen replacement, phone repair Pontypridd |
| Screen Repair | phone screen repair | phone screen replacement, cracked phone screen, smashed phone screen, mobile phone screen repair, broken screen repair |
| iPhone Screen Repair | iPhone screen repair | iPhone screen replacement, cracked iPhone screen, broken iPhone screen, iPhone [model] screen |
| Samsung Screen Repair | Samsung screen repair | Samsung screen replacement, Galaxy screen repair, cracked Samsung screen, Samsung [model] screen |
| Battery Replacement | phone battery replacement | iPhone battery replacement, Samsung battery replacement, phone won't hold charge |
| Charging Port Repair | phone charging port repair | charging port replacement, phone won't charge |
| Camera Replacement | phone camera repair | phone camera replacement, cracked camera lens |
| Speaker Repair | phone speaker repair | earpiece repair, phone sound not working |
| Phone Diagnostics | phone diagnostics | phone fault diagnosis, what's wrong with my phone |
| Areas We Cover | phone repair South Wales | mobile phone repair South Wales, areas we cover |
| Pontypridd | phone repair Pontypridd | mobile phone repair Pontypridd, phone screen repair Pontypridd, screen replacement Pontypridd, iPhone/Samsung screen repair Pontypridd, cracked screen repair Pontypridd |
| Treforest | phone repair Treforest | phone screen repair Treforest, screen replacement Treforest |
| Pontyclun | phone repair Pontyclun | screen repair Talbot Green, screen replacement Pontyclun |
| Tonypandy | phone repair Tonypandy | screen repair Rhondda, cracked screen Tonypandy |
| Treherbert | phone repair Treherbert | screen repair Rhondda, screen replacement Treherbert |
| Aberdare | phone repair Aberdare | screen repair Cynon Valley, screen replacement Aberdare |
| Merthyr Tydfil | phone repair Merthyr Tydfil | screen replacement Merthyr, iPhone screen repair Merthyr |
| Caerphilly | phone repair Caerphilly | screen replacement Caerphilly, iPhone/Samsung screen repair Caerphilly |
| Cardiff | phone repair Cardiff | mobile phone screen repair Cardiff, iPhone/Samsung screen replacement Cardiff, we come to you Cardiff |
| How It Works | mobile phone repair process | how mobile phone repair works, do you come to me |
| Parts & Repair Information | phone repair parts *(low priority, informational)* | (no warranty keywords; no genuine/OEM/aftermarket claims unless verified per repair) |
| About | *(brand/E-E-A-T — no keyword target)* | — |
| Reviews | phone repair reviews [area] | — |
| Contact | *(low priority, trust-focused)* | contact phone repair South Wales |
| Get a Quote | phone repair quote | phone screen repair quote, get a quote |

**The intersection principle:** "iPhone screen repair Pontypridd" is not a page. It is captured by the Pontypridd page and the iPhone page ranking together for the long-tail, connected by the internal link between them. This delivers breadth of rankings through depth of content, not through manufactured combination pages.
---

## 8. Conversion strategy

The site is engineered for one conversion: a genuine enquiry (WhatsApp, call, or quote submission), weighted toward screen repair. Design principles:

### 8.1 The two-speed contact model

Two customer types, two paths, both always available:

1. **The express lane — the panicked customer** (smashed screen, wants to talk now). Served by the persistent **floating WhatsApp button** and the **sticky mobile bar (Call / WhatsApp / Get a Quote)**. One tap, no form. This path must never be more than a glance away on any page or scroll position.
2. **The considered lane — the researcher** who wants to understand the service first. Served by the **guided quote assistant** and page content, ending in an enquiry.

The two paths never compete. The assistant *feeds* the express lane (see 8.3).

### 8.2 CTA hierarchy

- **Primary CTA:** Get a Quote (button-styled, high contrast) + WhatsApp.
- **Secondary CTA:** Call.
- Every service and location page repeats a screen-led CTA near the top (after the direct answer) and at the bottom (after the content/FAQ). The sticky bar covers everything in between.
- CTA copy is action- and reassurance-led: "Get my quote", "Message us on WhatsApp", "Call now" — not vague ("Submit", "Contact").
- **Quote wording rule (do not deviate):** the word "Free" must **not** appear before "Quote" anywhere — no "Free Quote" — until the owner explicitly confirms that policy. Use **"Get a Quote"**, **"Request a Quote"**, or **"Get Your Personalised Quote"** in all headings, buttons, title tags, and metadata.

### 8.3 The guided quote assistant

A progressive-enhancement, vanilla-JS assistant. It qualifies the lead in four quick steps, then offers two parallel finishes so the highest-intent customer converts in one tap while useful data is still captured.

**Steps:**

1. **Brand** — iPhone / Samsung / Other
2. **Model** — a list appropriate to the brand, plus "Not sure / help me identify"
3. **Repair needed** — Screen / Battery / Charging port / Camera / Speaker / Not sure (screen listed first)
4. **Location** — postcode or town (also silently checks whether the area is covered)

**Two parallel finishes (Step 5):**

- **"Message us on WhatsApp"** — opens WhatsApp with a pre-filled message summarising what they entered (e.g. *"Hi, I have an iPhone 13 with a cracked screen, in Pontypridd — can I get a quote?"*). One tap, highest conversion.
- **"Send my details"** — a short form (name, preferred contact method, phone number, optional email) that submits the enquiry. (No photo upload at launch — customers are directed to send photos via WhatsApp.)
- **"Or just call us"** — `tel:` link always shown.

**Hard rules:**

- The assistant **never displays a price** and **never promises a time or confirms a booking**. It qualifies and routes only. "Quote" always means "we will give you one", never "here is one".
- It **works without JavaScript** (progressive enhancement): the underlying content is a normal form/links that function if JS fails. JS enhances it into the stepped experience.
- Every completed flow is an analytics event (which brand/model/repair/area, and which step users drop at) — this becomes demand intelligence over time.

**Why this design (improvement on a linear "form at the end" assistant):** ending an assistant on a form reintroduces the exact friction the assistant removes. Offering a pre-filled WhatsApp finish converts the highest-intent customer instantly and still captures the qualifying data. This is a deliberate CRO improvement.

### 8.4 Trust elements at the point of conversion

Near every quote CTA, a short reassurance line drawn from confirmed facts:

- "We come to you — most standard screen replacements are done at your home or work in around 45–60 minutes."
- "No need to lose your phone for the day."
- Links to How It Works, Parts & Repair Information, and Reviews for anyone who wants more detail before enquiring.

All such lines use only confirmed facts and the "normally/typically" framing — no absolute promises.

---

## 9. Form architecture and email delivery

### 9.1 Fields

**Quote form (full):**

- Name (required)
- Phone number (required)
- Email (optional)
- Preferred contact method (required — WhatsApp / Call / Email)
- Town or postcode (required)
- Phone brand (required)
- Phone model (required)
- Repair required (required — screen listed first)
- Description of the fault (optional)
- (Photo upload removed for launch — customers send photos via WhatsApp)
- GDPR consent checkbox (required) with a link to the Privacy Policy

**Contact form (shorter):** Name, phone/email, message, preferred contact method, GDPR consent.

The guided assistant's "Send my details" finish is the quote form pre-populated from the assistant steps, so the customer only completes what is left.

### 9.2 Delivery architecture

**Static sites cannot send email directly.** The confirmed architecture:

```
Browser (form, progressively enhanced)
   │  submits via fetch (or native POST fallback if JS fails)
   ▼
Cloudflare Pages Function  (serverless, in-project — no third-party front-end dependency)
   │  • server-side validation
   │  • spam protection (honeypot field + basic rate limiting; optional Turnstile)
   │  • logs submission (so nothing fails silently)
   ▼
Email-sending mechanism  [PROVIDER: TO BE CONFIRMED]
   │  options: Cloudflare Email Routing/Workers, or a reputable
   │  transactional email API (e.g. MailChannels-type, Resend, Postmark)
   ▼
Destination inbox: calloutphonerepairs@gmail.com
   (future option: quotes@calloutphonerepairs.co.uk forwarding to Gmail)
```

**The email-sending provider is marked TO BE CONFIRMED.** The architecture is provider-agnostic: the Pages Function is the stable integration point, and the provider can be chosen or swapped without changing the front-end.

### 9.3 Requirements (all mandatory)

- **Server-side validation** (never trust client-side alone).
- **Spam protection:** honeypot field + rate limiting at the Function; optional Cloudflare Turnstile if spam becomes a problem (privacy-friendly, low friction).
- **Photo upload:** removed for launch. Customers are directed to send photos via WhatsApp instead, avoiding image storage/PII handling at launch.
- **GDPR:** explicit consent checkbox, clear purpose statement, data handling covered in the Privacy Policy, minimal retention.
- **Customer confirmation:** a clear on-screen success message after submission, and (where email is provided) an optional confirmation email.
- **Reliable error handling:** if submission fails, the customer sees a clear error and an alternative (WhatsApp/Call), and the failure is logged. **The form must never fail silently.**
- **Accessibility:** every field labelled, errors announced to assistive technology, keyboard-operable, adequate contrast, large tap targets.
- **Performance:** the form and assistant add minimal, deferred, non-render-blocking JS; they never block the main thread or cause layout shift.

### 9.4 Tracking

- WhatsApp button clicks, `tel:` clicks, and quote submissions are tracked as analytics events so the business can see which channels and pages convert.
- Recommended analytics: **Cloudflare Web Analytics** (privacy-first, cookieless, no consent-banner burden, no performance cost) plus lightweight custom event tracking. If GA4 is preferred later, it requires consent management and adds weight — a deliberate trade-off, not a default.
---

## 10. Page-by-page briefs

**Standing rules for every page:** single `<h1>`; logical heading order (no skipped levels); self-referencing canonical; unique title and meta description; sticky mobile bar + floating WhatsApp present; a screen-led quote CTA near top and bottom; descriptive internal-link anchors; WCAG AA; all imagery is bespoke illustration / vector / device-render (NO photography, NO fabricated repair 'evidence', NO stock); direct-answer opener written for humans and AI extraction; unverified facts handled via internal HTML-comment dev markers (never visible [CONFIRM] text); availability and repair-timing framing per Sections 2.1–2.2. Schema recommendations are conservative and must be validated against current Schema.org and Google documentation at build (Section 11).

---

### 10.1 Homepage — `/`

**Search intent:** mixed commercial + orientation. Must answer *what, where, how, trust, act* immediately and funnel to a screen-repair quote.

**Primary keyword (✎):** to be set post-validation (candidate: *mobile phone repair South Wales*, or a Pontypridd-led commercial phrase — chosen for strongest realistic commercial intent while reflecting the genuine Pontypridd base + wider South Wales service).
**Secondary (✎):** we come to you phone repair, phone screen repair South Wales, mobile phone screen replacement, phone repair Pontypridd.

**Direct-answer opener (honest):**
> Call Out Phone Repairs is a mobile phone repair service based in Pontypridd. We come to you — at home or at work — to repair cracked and broken phone screens and other faults across Pontypridd and South Wales. Most standard screen replacements are completed on-site in around 45–60 minutes, depending on the device and parts required. Tell us your phone and the problem for a quote by WhatsApp or phone.

**H1:** Mobile Phone Repair That Comes To You *(exact wording finalised post keyword validation; contains the validated primary intent naturally)*
**Near-H1 line:** We Come To You · Pontypridd & South Wales

**Section order:**

1. **Hero** — H1 + tagline + one-line value prop + primary CTA (Get a Quote) + WhatsApp/Call. Hero visual: bespoke illustrated device / screen-repair vector composition (no photo). LCP element is text + inline SVG, not a raster photo.
2. **H2: Cracked or Broken Screen? We'll Come and Fix It** — screen-replacement lead, front-loaded. Links Screen pillar, iPhone, Samsung. Includes the ~45–60 min, we-come-to-you reassurance.
3. **H2: How It Works** — honest steps: Get a quote → We come to you → We repair on the spot → Done, phone back in your hands. Links How It Works.
4. **H2: Phones and Repairs We Cover** — screen (lead, visually dominant) + battery, charging port, camera, speaker, diagnostics, each card linking to its page.
5. **H2: Areas We Cover Across South Wales** — honest coverage (Pontypridd core + wider areas by appointment). Links Areas hub + priority location pages.
6. **H2: Why People Choose Call Out Phone Repairs** — trust built on clarity, not claims: a real named person (links About), the honest come-to-you process (links How It Works), genuine reviews as they arrive (links Reviews), plain parts/repair information (links Parts & Repair Information). No invented credentials, no warranty claim. Review slot populated as genuine reviews arrive; honest empty-state at launch.
7. **H2: Get Your Personalised Quote** — guided assistant entry + short form; WhatsApp/Call reinforced.
8. **FAQ (visible).** Questions: Do you come to me? · Which areas do you cover? · What phones do you repair? · How long does a screen repair take? *(normally ~45–60 min)* · Do you fix the screen at my home? · How do I get a price? · Do you repair iPhones and Samsungs?
9. **Footer** — full nav, contact block (phone, WhatsApp, email, areas, availability framing), Privacy link.

**Internal links out:** Screen pillar, iPhone, Samsung, each service, Areas hub, Pontypridd, Treforest, Cardiff, How It Works, Parts & Repair Information, Reviews, Get a Quote.

**Visuals (illustration-led, no photography):** bespoke hero device/screen-repair SVG; abstract technology/geometric accents; clean line icons for services; illustrated coverage map (stylised, not a real photo). Inline SVG where practical (crisp, tiny, no layout shift); any raster illustration is WebP/AVIF, sized (`width`/`height`), `loading="lazy"` below the fold. No `fetchpriority` raster hero needed — hero is text + SVG.

**Alt text examples (illustration-led — never imply a real job):** "Illustration of an iPhone with a cracked screen"; "Stylised graphic of a restored phone screen."

**Accessibility:** single H1; real hero `alt`; CTAs are real `<a>`/`<button>` with discernible text; WhatsApp icon `aria-label`; AA contrast; keyboard-navigable assistant; sticky bar does not obscure content or shift layout.

**Metadata (✎):**
- Title (≤ ~60 chars): *Mobile Phone Repair — We Come To You | Call Out Phone Repairs*
- Meta description (≤ ~155 chars): honest, screen-led, mentions Pontypridd/South Wales + we-come-to-you + ~45–60 min + quote CTA.

**Schema (validate at build):** `Organization`; `LocalBusiness` (service-area, hidden address, `areaServed` = genuine areas, `openingHours` = **Mo–Su 08:00–20:00**, no 24/7); `WebSite`; `WebPage`; `BreadcrumbList`; `Service`. No self-serving review stars. **No `priceRange`** (unverified — removed). **No `FAQPage`** (disabled, 11.2). Homepage uses one coherent `@graph` (Organization + WebSite + WebPage + LocalBusiness, linked by stable `@id`).

**[DEV MARKERS]:** owner name for About/Person schema; on-site framing wording; any timing beyond the standard-screen 45–60 min. No warranty wording anywhere.

---

### 10.2 Screen Repair (pillar) — `/screen-repair/`

**Search intent:** high commercial — cracked/broken screen, comparing options, wants process, brands covered, price route. Owns generic screen terms; anchors the cluster.

**Primary (✎):** phone screen repair
**Secondary (✎):** phone screen replacement, cracked phone screen repair, smashed phone screen, mobile phone screen repair, broken screen repair. *(iPhone/Samsung terms reserved for the sub-pillars — anti-cannibalisation.)*

**Direct-answer opener:**
> Cracked or smashed your phone screen? We come to you across Pontypridd and South Wales to replace it — usually at your home or workplace. Most standard screen replacements are completed on-site in around 45–60 minutes, depending on the device, fault and parts required, and we confirm the expected time before we start. Tell us your phone model for a quote by WhatsApp or phone.

**H1:** Phone Screen Repair & Replacement — We Come To You

**Section order:**
1. Direct answer — what this is, we-come-to-you, screen-led, ~45–60 min.
2. **H2: Cracked, Smashed or Faulty Screens We Repair** — symptoms: cracked glass, black screen, unresponsive touch, lines/discolouration, ghost touch (semantic completeness).
3. **H2: iPhone and Samsung Screen Repairs** — brief, links the two sub-pillars (passes relevance down; does not try to own their terms).
4. **H2: How Screen Repairs Work — We Come To You** — honest on-site process, ~45–60 min, no "lose your phone for the day". Links How It Works. [CONFIRM rare exceptions handled case by case.]
5. **H2: Parts & Repair Information** — plain language: the exact part options, availability and details are discussed with the customer before work begins. Links Parts & Repair Information. **No** genuine/OEM/premium/high-quality claims unless verified per repair. **No warranty section.**
7. **H2: Areas We Cover** — links Areas hub + priority locations; honest coverage.
8. **H2: Get a Quote for Your Screen Repair** — assistant + form + WhatsApp/Call.
9. **FAQ (visible):** Can you replace a smashed screen? · Do you fix screens at my home? · How long does a screen repair take? *(most standard screen replacements ~45–60 min)* · Do you repair both iPhone and Samsung screens? · How are parts and details decided? *(discussed with you before work begins)* · How do I get a quote? **(No warranty FAQ.)**
10. Footer.

**Internal links out:** iPhone, Samsung (core cluster), How It Works, Parts & Repair Information, Areas hub, priority locations, Get a Quote, homepage.
**Inbound (should receive the most internal links on the site):** homepage, all nine location pages, both sub-pillars, relevant service pages.

**Visuals (illustration-led):** stylised cracked-screen vs restored-screen illustration (clearly a graphic, not a photo of a real job); line icons for fault types; abstract tech accents. **Alt examples:** "Illustration of a cracked phone screen beside a restored screen"; "Line icon representing screen replacement."

**Metadata (✎):**
- Title: *Phone Screen Repair & Replacement | We Come To You — South Wales*
- Meta: cracked/smashed screen, we-come-to-you, Pontypridd/South Wales, ~45–60 min, quote CTA.

**Schema (validate):** `Service` (screen repair) linked to `LocalBusiness`/`Organization`; `BreadcrumbList`; `WebPage`. No review stars. No `FAQPage` (disabled, 11.2).

**[DEV MARKERS]:** on-site framing + rare exceptions wording. No part-quality claims unless verified; no warranty.

---

### 10.3 iPhone Screen Repair (sub-pillar) — `/screen-repair/iphone/`

**Search intent:** commercial, brand-specific — cracked iPhone screen, model-aware.
**Primary (✎):** iPhone screen repair · **Secondary (✎):** iPhone screen replacement, cracked iPhone screen repair, broken iPhone screen, iPhone [model] screen replacement.

**Direct-answer opener:**
> Cracked your iPhone screen? We come to you across Pontypridd and South Wales to replace iPhone screens — usually on the spot. Most standard iPhone screen replacements are completed in around 45–60 minutes, depending on the model and parts required. Tell us your iPhone model for a quote by WhatsApp or phone.

**H1:** iPhone Screen Repair & Replacement — We Come To You

**Section order:**
1. Direct answer.
2. **H2: iPhone Models We Repair** — [CONFIRM range/models]; honest about any not covered; anchor for future per-model depth.
3. **H2: Common iPhone Screen Problems** — cracked glass, black display, unresponsive touch, lines, True Tone/related notes handled honestly [CONFIRM technical scope].
4. **H2: iPhone Screen Parts & Repair Details** — plain language: part options and details discussed with the customer before work begins; links Parts & Repair Information. **No** genuine/OEM/aftermarket labelling unless verified per repair.
5. **H2: How We Repair Your iPhone Screen** — on-site, ~45–60 min [CONFIRM].
6. **H2: Areas We Cover.**
7. **H2: Get an iPhone Screen Repair Quote** — assistant pre-set to iPhone + WhatsApp/Call.
8. **FAQ:** Which iPhone models do you repair? *(dev-marker: confirm range)* · Do you come to me? · How long does an iPhone screen repair take? *(standard ~45–60 min)* · How are parts and details decided? *(discussed before work begins)* · How do I get a quote? **(No warranty FAQ.)**
10. Footer.

**Internal links out:** Screen pillar (up), Samsung (sibling), Parts & Repair Information, How It Works, Areas hub, priority locations, Get a Quote.
**Inbound:** pillar, homepage, all location pages, service cross-links.

**Visuals (illustration-led):** premium iPhone device illustration / render (generic, not brand-passing-off), stylised screen-repair graphic. **Alt:** "Illustration of an iPhone with a cracked screen."

**Metadata (✎):** Title *iPhone Screen Repair & Replacement | We Come To You — South Wales*; meta iPhone-led + ~45–60 min + quote CTA.

**Schema (validate):** `Service` (iPhone screen repair) → LocalBusiness/Organization; `BreadcrumbList`; `WebPage`.

**Future:** reserved child slugs for high-demand models (`/screen-repair/iphone/iphone-15/`, etc.), added post-launch per validated demand — not at launch.

**[DEV MARKERS]:** models covered; technical scope. No parts claims unless verified; no warranty.

---

### 10.4 Samsung Screen Repair (sub-pillar) — `/screen-repair/samsung/`

**Search intent:** commercial, brand-specific — Samsung/Galaxy screen.
**Primary (✎):** Samsung screen repair · **Secondary (✎):** Samsung screen replacement, Galaxy screen repair, cracked Samsung screen, Samsung [model] screen.

**Direct-answer opener:**
> Cracked or broken your Samsung Galaxy screen? We come to you across Pontypridd and South Wales to replace it, usually on the spot. Tell us your Samsung model for a quote by WhatsApp or phone.

**H1:** Samsung Screen Repair & Replacement — We Come To You

**Section order:** mirrors the iPhone sub-pillar — Samsung models covered *(dev-marker: confirm)*; common Galaxy screen faults; **honest note that Samsung AMOLED / curved-edge / foldable screens differ in complexity** (do NOT apply the standard 45–60 min timing to these); parts & repair details discussed before work begins (no genuine/OEM claims unless verified); areas; quote (assistant pre-set to Samsung); FAQ; footer. **No warranty section.**

**Internal links out:** Screen pillar (up), iPhone (sibling), Parts & Repair Information, How It Works, Areas, locations, Get a Quote.
**Inbound:** pillar, homepage, all locations.

**Visuals (illustration-led):** premium generic Samsung/Galaxy device illustration, stylised screen graphic. **Alt:** "Illustration of a Samsung Galaxy phone with a damaged screen."

**Metadata (✎):** Title *Samsung Screen Repair & Replacement | We Come To You — South Wales*.

**Schema (validate):** `Service` (Samsung screen repair) → LocalBusiness/Organization; `BreadcrumbList`; `WebPage`.

**[DEV MARKERS]:** models/scope incl. curved/foldable. No parts claims unless verified; no warranty; no standard-timing claim for complex/foldable screens.

---

### 10.5 Service pages (shared template ×5)

**URLs:** `/repairs/battery-replacement/`, `/repairs/charging-port-repair/`, `/repairs/camera-replacement/`, `/repairs/speaker-repair/`, `/repairs/phone-diagnostics/`

**Shared section order:**
1. Direct-answer opener (symptom → we come to you → quote).
2. **H2: Signs You Need [This Repair]** — honest symptom list (semantic completeness).
3. **H2: Phones We Cover.**
4. **H2: How We Repair It — We Come To You** — on-site framing [CONFIRM per service].
5. **H2: Parts & Repair Information** — part options and details discussed before work begins; links Parts & Repair Information. No warranty claim.
6. **H2: Areas We Cover.**
7. **H2: Get a Quote** — assistant pre-set to this repair + WhatsApp/Call.
8. **FAQ (visible).**
9. Footer.

**Cross-links:** each service ↔ Screen pillar (priority sibling), ↔ Diagnostics (hub for "not sure"), ↔ Areas, ↔ Get a Quote.
**Inbound:** homepage, location pages' "Repairs We Offer" sections, footer.

**Per-page specifics:**

| Page | Primary (✎) | Honest notes / [CONFIRM] |
|---|---|---|
| Battery Replacement | phone battery replacement | Symptoms: drains fast, won't hold charge, unexpected shutdowns, swelling (safety note). iPhone/Samsung scope [CONFIRM]. Genuine vs aftermarket battery [CONFIRM]. |
| Charging Port Repair | phone charging port repair | Symptoms: won't charge, loose cable, intermittent. Distinguish port vs cable vs battery (links Diagnostics). Clean-vs-replace honesty [CONFIRM]. |
| Camera Replacement | phone camera repair | Cracked lens vs module fault; front/rear [CONFIRM scope]. |
| Speaker Repair | phone speaker repair | Earpiece vs loudspeaker vs mic; muffled/no sound. **Do not imply water-damage recovery unless [CONFIRM].** |
| Phone Diagnostics | phone diagnostics | "Not sure what's wrong?" — honest entry point; links to all services; genuine fault-finding, no false promises. |

**Metadata (✎ each):** Title *[Repair] | We Come To You — South Wales | Call Out Phone Repairs*; meta symptom-led + quote CTA.
**Schema each (validate):** `Service` → LocalBusiness/Organization; `BreadcrumbList`; `WebPage`.

**Note:** these pages are deliberately lighter than the screen cluster — present for topical completeness and genuine demand, but link equity and prominence stay weighted to screen.

---

### 10.6 Areas We Cover (hub) — `/areas/`

**Search intent:** navigational + commercial — "do you cover my area", "phone repair South Wales", browsing coverage.
**Primary (✎):** phone repair South Wales · **Secondary (✎):** mobile phone repair South Wales, areas we cover.

**Direct-answer opener:**
> We're a mobile phone repair service based in Pontypridd, covering towns across South Wales. Find your area below — we come to you at home or work, by appointment.

**H1:** Areas We Cover Across South Wales

**Section order:**
1. Direct answer + honest coverage framing (Pontypridd core; wider areas by appointment/travel).
2. **H2: Coverage Map** — real service-area visual (no home address).
3. **H2: Areas We Cover** — grouped honestly: *Around Pontypridd* (Pontypridd, Treforest, Pontyclun); *Rhondda* (Tonypandy, Treherbert); *Cynon Valley* (Aberdare); *Merthyr Tydfil*; *Caerphilly*; *Cardiff* — each links to its page; grouping signals the honest strength gradient.
4. **H2: Don't See Your Area?** — invite contact; honest that coverage is growing.
5. **H2: Get a Quote.**
6. **FAQ.**
7. Footer.

**Internal links out:** all nine location pages (primary hub inbound link for each — prevents orphans), Get a Quote, homepage.
**Inbound:** homepage, nav, footer, every location page.

**Images (real):** coverage-area visual; on-location repair shots [CONFIRM].
**Metadata (✎):** Title *Areas We Cover — Mobile Phone Repair Across South Wales*; meta lists key towns + we-come-to-you.
**Schema (validate):** `LocalBusiness` with `areaServed` = the nine genuine areas (clarity/entity understanding only — not a ranking lever, and will not override proximity); `BreadcrumbList`; `WebPage`.
---

### 10.7 Location pages — the model

The Pontypridd flagship (10.7.1) is the master template. The other eight inherit its structure but carry their **own** primary keyword, scenario, communities, landmarks, and FAQs. Cardiff, Merthyr Tydfil, and Treherbert carry explicit honest framing that the business travels from Pontypridd, that coverage is expanding, and that these are organic (not map-pack) targets. All nearby-community lists and coverage claims are **[CONFIRM]**.

**Shared location-page section order:**
1. Direct-answer opener (local, we-come-to-you, screen-led, ~45–60 min).
2. **H2: Phone Screen Repair in [Town]** — commercial priority; links Screen pillar, iPhone, Samsung with descriptive anchors. This is where "[screen term] [town]" long-tails are earned.
3. **H2: Areas We Cover Around [Town]** — genuine nearby communities [CONFIRM]; real coverage detail (the unique content that prevents doorway-page status).
4. **H2: Repairs We Offer in [Town]** — screen (lead) + battery, charging port, camera, speaker, diagnostics; links to service pages.
5. **H2: How We Reach You in [Town]** — local travel context, landmarks, honest on-site framing.
6. **H2: Local Reviews** — area-specific review slot (populated as genuine reviews arrive; honest empty-state; no fabrication).
7. **H2: Get a Quote in [Town]** — assistant + form + WhatsApp/Call.
8. **FAQ (visible, town-specific).**
9. Footer.

**Shared per-page metadata (✎):** Title *Phone Repair in [Town] — We Come To You | Call Out Phone Repairs*; local, screen-led meta.
**Shared per-page schema (validate):** `LocalBusiness` (`areaServed` = town + genuine nearby [CONFIRM]) — clarity only, not a ranking shortcut, will not override proximity; `BreadcrumbList`; `WebPage`; `Service` references.
**Shared inbound links:** homepage (priority towns), Areas hub, footer, neighbouring location pages.
**Shared [CONFIRM]:** nearby communities served; on-site framing; timings; imagery genuine.

---

#### 10.7.1 Pontypridd (flagship) — `/areas/pontypridd/`

**Primary (✎):** phone repair Pontypridd
**Secondary (✎):** mobile phone repair Pontypridd, phone screen repair Pontypridd, screen replacement Pontypridd, iPhone screen repair Pontypridd, Samsung screen repair Pontypridd, cracked screen repair Pontypridd.

**Direct-answer opener:**
> Based in Pontypridd, Call Out Phone Repairs comes to you across the town and surrounding areas to repair cracked screens, batteries, charging ports and more — at your home or workplace. Most standard screen replacements are completed on-site in around 45–60 minutes. Tell us your phone and the fault for a quote by WhatsApp or phone.

**H1:** Phone Repair in Pontypridd — We Come To You

**Unique local layer:**
- Lead with the genuine Pontypridd base (real proximity strength — this is the page most likely to win the map pack).
- Nearby communities [CONFIRM]: Rhydyfelin, Hawthorn, Glyncoch, Cilfynydd, Graigwen, Ynysybwl.
- Landmarks/travel: Taff Street, town centre, Ynysangharad War Memorial Park, near the University of South Wales Treforest campus.
- FAQ: Do you cover [Rhydyfelin/Glyncoch]? [CONFIRM] · Can you come to my workplace in Pontypridd town centre? · How long does a screen repair take? · Do you repair iPhone and Samsung screens in Pontypridd? · How do I book?

**Links out (beyond shared):** Treforest (adjacent).
**Visuals (illustration-led):** stylised illustrated coverage map of Pontypridd & nearby areas; abstract tech accents; line icons. No photos. Real local photos may be added later as earned.
**Alt:** "Stylised illustrated coverage map of Pontypridd and nearby areas"; "Illustration of a phone with a cracked screen." (No photographs; alt text must not imply a real customer repair.)

---

#### 10.7.2 Treforest — `/areas/treforest/`

**Primary (✎):** phone repair Treforest · **Secondary (✎):** phone screen repair Treforest, screen replacement Treforest.
**Unique angle:** University of South Wales students (high screen-breakage, often no car → come-to-you is ideal) + Treforest Industrial Estate businesses (on-site during the working day).
**Communities [CONFIRM]:** Rhydyfelin, Upper Boat.
**Landmarks:** USW Treforest campus, Treforest Industrial Estate, railway station, Forest Road.
**FAQ:** Do you repair phones for USW students? · Can you come to the Treforest Industrial Estate? · Do you offer student pricing? [CONFIRM] · How long does a screen repair take?
**Links out:** Pontypridd (adjacent), screen cluster.

---

#### 10.7.3 Pontyclun — `/areas/pontyclun/`

**Primary (✎):** phone repair Pontyclun · **Secondary (✎):** screen repair Talbot Green, screen replacement Pontyclun.
**Unique angle:** M4 commuter belt; convenience-led professionals; Talbot Green retail area draws the district.
**Communities [CONFIRM]:** Talbot Green, Llantrisant, Miskin, Brynsadler, Groes-faen.
**Landmarks:** Talbot Green Retail Park, Royal Mint (nearby), M4 J34, Llantrisant Leisure Centre.
**FAQ:** Do you cover Talbot Green and Llantrisant? · Can you repair my phone while I work from home in Pontyclun? · How long does it take?
**Links out:** Cardiff (commuter corridor), screen cluster.

---

#### 10.7.4 Tonypandy — `/areas/tonypandy/`

**Primary (✎):** phone repair Tonypandy · **Secondary (✎):** screen repair Rhondda, cracked screen Tonypandy.
**Unique angle:** Rhondda Fawr commercial centre; removes the drive down to Pontypridd or into Cardiff. **Honest coverage framing** (travelling up the Rhondda).
**Communities [CONFIRM]:** Llwynypia, Penygraig, Clydach Vale.
**Landmarks:** Tonypandy town centre, A4058, Judges' Hall, De Winton Field.
**FAQ:** Do you travel up the Rhondda to Tonypandy? · How long does it take you to reach Tonypandy? *(honest)* · Do you repair screens on the spot?
**Links out:** Treherbert (valley neighbour), screen cluster. *(Keep genuinely distinct from Treherbert — different landmarks, different community references.)*

---

#### 10.7.5 Treherbert — `/areas/treherbert/`

**Primary (✎):** phone repair Treherbert · **Secondary (✎):** screen repair Rhondda, screen replacement Treherbert.
**Unique angle (distinct from Tonypandy):** valley-head; repair options are genuinely scarce this far up the valley, so a reliable come-to-you service is rare and valued. Emphasise scarcity/convenience, not commercial-centre bustle. **Strongest honest travel framing.**
**Communities [CONFIRM]:** Treorchy, Ynyswen, Blaenrhondda, Tynewydd.
**Landmarks:** Treherbert town, Rhondda Tunnel history, A4061 toward the Bwlch.
**FAQ:** Do you really travel as far as Treherbert? · Do you cover Treorchy and Ynyswen? · How long does it take to reach me?
**Links out:** Tonypandy (valley neighbour), screen cluster.

---

#### 10.7.6 Aberdare — `/areas/aberdare/`

**Primary (✎):** phone repair Aberdare · **Secondary (✎):** screen repair Cynon Valley, screen replacement Aberdare.
**Unique angle:** substantial Cynon Valley town with its own identity and centre; competing on the mobile come-to-you model, not on being the only option.
**Communities [CONFIRM]:** Aberaman, Cwmbach, Trecynon, Hirwaun.
**Landmarks:** Aberdare town centre, Aberdare Park, A4059/A470 corridor, Robertstown.
**FAQ:** Do you cover Aberdare and the Cynon Valley? · Can you come to Aberaman or Cwmbach? · How long does a repair take?
**Links out:** Merthyr Tydfil (neighbouring valley town), screen cluster.

---

#### 10.7.7 Merthyr Tydfil — `/areas/merthyr-tydfil/`

**Primary (✎):** phone repair Merthyr Tydfil · **Secondary (✎):** screen replacement Merthyr, iPhone screen repair Merthyr.
**Unique angle:** large town, own centre; pitch is the convenience/time-saving of come-to-you for busy households and retail-park workers. **Honest framing: furthest north, organic (not map-pack) target, travelling from Pontypridd.**
**Communities [CONFIRM]:** Dowlais, Troedyrhiw, Merthyr Vale, Pentrebach.
**Landmarks:** Merthyr town centre, Cyfarthfa Castle & Park, Cyfarthfa Retail Park, A470 north, Bike Park Wales.
**FAQ:** Do you travel to Merthyr Tydfil? · How soon can you reach Merthyr? *(honest)* · Do you repair screens on the spot?
**Links out:** Aberdare, screen cluster.

---

#### 10.7.8 Caerphilly — `/areas/caerphilly/`

**Primary (✎):** phone repair Caerphilly · **Secondary (✎):** screen replacement Caerphilly, iPhone/Samsung screen repair Caerphilly.
**Unique angle:** large commuter town with its own centre and strong Cardiff pull; convenience-led. **Honest framing: a different direction from the Pontypridd base, so real travel.**
**Communities [CONFIRM]:** Ystrad Mynach, Bedwas, Trethomas, Llanbradach, Senghenydd.
**Landmarks:** Caerphilly Castle (strong local anchor), town centre, Caerphilly Mountain road, Morgan Jones Park.
**FAQ:** Do you cover Caerphilly and Ystrad Mynach? · Do you travel over Caerphilly Mountain? · How long does it take?
**Links out:** Cardiff, screen cluster.

---

#### 10.7.9 Cardiff — `/areas/cardiff/`

**Primary (✎):** phone repair Cardiff · **Secondary (✎):** mobile phone screen repair Cardiff, iPhone/Samsung screen replacement Cardiff, we come to you phone repair Cardiff.
**Unique angle:** city convenience — a technician coming to home or office beats navigating city-centre parking to reach a shop. **Most honest framing of all: highest competition, weakest proximity from a Pontypridd base, a long-game organic play. Realistically nearest/most serviceable in north Cardiff first (e.g. Whitchurch, Llandaff, Radyr).**
**Coverage:** rather than list villages, target come-to-you city-wide plus the realistic nearest districts; be honest that whole-city same-day coverage is not promised.
**Landmarks/travel:** the A470 corridor from Pontypridd into north Cardiff (credible and genuine — avoid castle/stadium clichés).
**FAQ:** Which parts of Cardiff do you cover? *(honest — north/nearest first)* · Do you come to offices in Cardiff? · How do I get a quote?
**Links out:** Caerphilly, Pontyclun (commuter corridor), screen cluster.

---

### 10.8 How It Works — `/how-it-works/`

**Search intent:** process/reassurance; objection-handling.
**Primary (✎):** mobile phone repair process · **Secondary (✎):** how mobile phone repair works, do you come to me.

**Direct-answer opener:**
> Getting your phone fixed is simple: request a quote, we arrange a time, and we come to you — at home or work. Most standard screen replacements are completed on the spot in around 45–60 minutes, and we confirm the expected time before starting. You don't lose your phone for the day.

**H1:** How Our Mobile Phone Repair Service Works

**Section order:**
1. Direct answer.
2. **H2: 1. Get a Quote** — WhatsApp / call / quote form; links Get a Quote.
3. **H2: 2. We Come To You** — by appointment, at home or work, across the coverage areas.
4. **H2: 3. We Repair Your Phone** — on the spot for most screen repairs, normally ~45–60 min; honest that a rare repair may need a different arrangement, handled case by case [CONFIRM]. **No "collect and return" framing implying a phone is kept for hours/days.**
5. **H2: 4. Parts & Repair Information** — part options and details are discussed and agreed with the customer before work begins; links Parts & Repair Information. **No warranty/aftercare guarantee claim.**
6. **H2: What We Repair** — links the screen cluster and services.
7. **H2: Areas We Cover** — links Areas hub.
8. **H2: Get a Quote.**
9. **FAQ.**
10. Footer.

**Metadata (✎):** Title *How Our Mobile Phone Repair Works — We Come To You*; meta process + ~45–60 min + we-come-to-you.
**Schema (validate):** `WebPage`, `BreadcrumbList`. Consider `HowTo` **only if** genuinely valid and appropriate at build — do not force it.
**[DEV MARKERS]:** rare-exception handling wording; any timing beyond the standard-screen 45–60 min. No warranty.

---

### 10.9 Parts & Repair Information — `/parts-and-repair-information/`

**Search intent:** transparency/reassurance for someone deciding whether to enquire. **Not** a warranty page. Low keyword priority — exists for clarity and trust, not to rank.
**Primary (✎):** phone repair parts *(low priority, informational)* · **Secondary:** none targeted. **No warranty keywords.**

**Direct-answer opener (neutral, honest, no promises):**
> We keep it simple and clear. The exact part options, availability and details for your repair are discussed and agreed with you before any work begins — so you always know what's involved before we start.

**H1:** Parts & Repair Information

**Section order:**
1. Direct answer.
2. **H2: How We Handle Parts** — plain language: options and availability depend on the device and fault, and are discussed with the customer before work begins. **No** genuine/OEM/premium/high-quality labelling unless that exact description has been verified for the specific repair.
3. **H2: What to Expect** — we confirm the details and the expected repair time before starting; nothing goes ahead until the customer agrees.
4. **H2: Get a Quote.**
5. **FAQ** (neutral): How do you decide which parts to use? *(discussed with you first)* · Will I know the details before you start? *(yes — confirmed before any work)* · How do I get a quote?
6. Footer.

**Explicitly NOT on this page:** no warranty period, no parts guarantee, no workmanship guarantee, no "free repairs if something goes wrong", no protection claims of any kind, no genuine/OEM/aftermarket/premium/high-quality descriptions unless separately verified per repair.

**Design note:** other pages link here for "parts & repair information" (never "warranty").
**Metadata (✎):** Title *Parts & Repair Information — Call Out Phone Repairs*; meta neutral (details discussed before work begins), no warranty wording.
**Schema (validate):** `WebPage`, `BreadcrumbList`. **No warranty-related schema.**
**[DEV MARKERS]:** none required — the neutral copy is true as written and needs no unverified facts.

---

### 10.10 About — `/about/`

**Search intent:** trust/E-E-A-T; the human proof.
**Keyword target:** none (brand/trust). The page's SEO value is E-E-A-T, not keywords.

**H1:** About Call Out Phone Repairs

**Section order:**
1. **Who we are** — a real, named person; honest that this is a solo mobile technician. Customers trust a real person over a faceless company. [CONFIRM you're happy to be named — confirmed yes; provide the name and any details you can stand behind.]
2. **Why we come to you** — the genuine reason the mobile model exists and how it helps customers.
3. **How we work** — genuine approach: quality of workmanship, honesty, clear communication, fair advice. **No invented experience, qualifications, awards, or years in business.** Only truthful statements the owner can stand behind.
4. **Illustrated / design-led visual** representing the person and the come-to-you service (no fabricated repair photos). A genuine photo of the owner may be added later if the owner chooses to provide one.
5. **H2: Areas We Cover** — links Areas hub.
6. **H2: Get a Quote.**

**Design note:** this page carries disproportionate E-E-A-T weight for both Google and AI search. Its power comes entirely from being genuine and specific.
**Metadata (✎):** Title *About Call Out Phone Repairs — We Come To You*.
**Schema (validate):** `AboutPage`/`WebPage`, `Organization`, `BreadcrumbList`; `Person` (recommended, given the owner is happy to be named — strengthens trust) [CONFIRM name].
**[CONFIRM]:** owner name and any biographical detail (must be truthful); imagery genuine. **No fabricated credentials of any kind.**

---

### 10.11 Reviews — `/reviews/`

**Search intent:** social proof.
**Primary (✎):** phone repair reviews [area].

**H1:** Customer Reviews

**Section order:**
1. Intro.
2. Genuine reviews (populated as they arrive; **honest empty-state at launch — no fabricated reviews**).
3. Per-area review signposting (feeds location pages as area reviews accumulate).
4. **H2: Get a Quote.**

**Policy note:** **no self-serving `AggregateRating`/`Review` rich-star markup.** Reviews are displayed as visible content. Any review structured data is added only if it complies with Google's current review-snippet policy at build time, and no rich-result eligibility is claimed. This page grows genuinely real over time via the review engine (Section 18).
**Metadata (✎):** Title *Customer Reviews — Call Out Phone Repairs*.
**Schema (validate):** `WebPage`, `BreadcrumbList`.

---

### 10.12 Contact — `/contact/`

**Search intent:** direct contact + trust.
**Primary (✎):** low priority, trust-focused (e.g. contact phone repair South Wales).

**Direct-answer opener:**
> Call Out Phone Repairs is a mobile call-out repair service — we come to you, by appointment. Contact us by WhatsApp, phone, or the form below and we'll arrange a time. We don't operate a walk-in shop.

**H1:** Contact Call Out Phone Repairs

**Section order:**
1. Direct answer (mobile, by appointment, we come to you — not a walk-in shop).
2. **H2: Call or WhatsApp** — buttons: `tel:+447347715961`, `https://wa.me/447347715961`.
3. **H2: Email** — calloutphonerepairs@gmail.com.
4. **H2: When We're Available** — "Submit a quote request at any time. Calls, messages and repair appointments are handled daily between 08:00 and 20:00." Per Section 2.1. **No 24-hour claim.**
5. **H2: Areas We Cover** — links Areas hub.
6. **H2: Send Us a Message** — contact form → Pages Function → Gmail (Section 9); GDPR consent + Privacy link.

**No home address anywhere.** Use a coverage-area visual, not a home pin.
**Metadata (✎):** Title *Contact — Call Out Phone Repairs | We Come To You*.
**Schema (validate):** `LocalBusiness` (service-area, hidden address, `areaServed`, `openingHours` = **Mo–Su 08:00–20:00**, no 24/7), `ContactPage`/`WebPage`, `BreadcrumbList`.
**[CONFIRM]:** none beyond the standard, provided availability framing is followed.

---

### 10.13 Get a Quote — `/get-a-quote/`

**Search intent:** conversion.
**Primary (✎):** phone repair quote · **Secondary (✎):** phone screen repair quote, get a quote.

**Direct-answer opener:**
> Tell us your phone and the fault and we'll give you a quote. Most standard screen replacements are done at your home or work in around 45–60 minutes. Prefer to talk? Message us on WhatsApp or call.

**H1:** Get Your Personalised Phone Repair Quote

**Section order:**
1. Direct answer.
2. **Guided quote assistant** (Brand → Model → Repair → Location → two parallel finishes: pre-filled WhatsApp / short form / call — per Section 8.3).
3. **H2: Prefer to Call or WhatsApp?** — the quick escape, also offered up front.
4. Honest note: "We'll reply by WhatsApp or phone. We don't show automatic prices online because an accurate quote depends on your exact model and repair."
5. GDPR consent; confirmation on submit.

**Progressive enhancement:** functions as a plain form + links without JavaScript.
**Metadata (✎):** Title *Get a Phone Repair Quote — We Come To You*.
**Schema (validate):** `WebPage`, `BreadcrumbList`.
**Hard rule:** no auto-generated prices, ever.

---

### 10.14 Privacy Policy — `/privacy-policy/`

**Purpose:** GDPR compliance. Covers: data collected (form data, analytics), lawful basis, retention, how to make a data request, cookies/analytics disclosure. Linked from every form and the footer.
**[CONFIRM]:** **legal review required.** A solid starting draft can be written, but it must be checked by someone qualified; it is not legal advice.
**Schema (validate):** `WebPage`, `BreadcrumbList`.

---

### 10.15 Custom 404 — `/404.html`

On-brand, friendly, `noindex`, excluded from sitemap, returns a true 404 status. Routes back to Home / Screen Repair / Areas / Get a Quote so a dead end becomes a recovered journey.
---

## 11. Schema strategy

All structured data is **JSON-LD in clearly separated blocks**, never inline in body copy. **Every type and property must be validated against current Schema.org definitions and current Google Search Central documentation at build time.** Nothing is shipped unvalidated. Conservative by design.

### 11.1 Types used

| Type | Applied to | Notes |
|---|---|---|
| `Organization` | Site-wide | Brand: name, logo, `sameAs` (socials, Google Business Profile). |
| `LocalBusiness` | Site-wide (homepage primary; location/contact pages) | **Confirmed valid type.** Service-area business: **no `address` exposed**; use `areaServed`. `openingHours` = **Monday–Sunday 08:00–20:00** (`Mo-Su 08:00-20:00`). **No 24/7 schema.** If a more specific *valid* subtype is confirmed at build, it may be used; otherwise `LocalBusiness` stands. **`MobilePhoneRepair` is NOT a valid Schema.org type and must not be used.** |
| `Service` | Each service + screen page | Separate `Service` entities for screen repair, iPhone screen repair, Samsung screen repair, battery, charging port, camera, speaker, diagnostics — each linked to the provider. |
| `WebSite` / `WebPage` | Site-wide / per page | `url` = canonical. |
| `BreadcrumbList` | All pages in the hierarchy | Mirrors the URL structure. |
| `FAQPage` | **Disabled site-wide** (no-op helper); visible FAQs retained for users | See 11.2. |
| `AboutPage` / `ContactPage` | About / Contact | Optional, valid. |
| `Person` | About | Only if the owner is named (confirmed yes) — strengthens E-E-A-T. |
| `ImageObject` | Key images | Optional; supports image understanding. |
| `AggregateRating` / `Review` | **Not used for self-serving stars** | See 11.3. |

### 11.2 FAQ schema — final decision (DISABLED)

Visible FAQ sections are kept where they help users and answer search intent. **`FAQPage` structured data is DISABLED site-wide.** Rationale: Google discontinued general FAQ rich results, and there is no proven AI-search ranking benefit, so emitting `FAQPage` markup adds page weight for no gain and introduces a maintenance/consistency risk (markup vs visible text). The generator's `faqpage_ld()` helper is a no-op that emits nothing, so no page carries `FAQPage` JSON-LD. Verified: 0 `FAQPage` blocks across all 28 pages; 20 pages retain visible FAQ sections for users.

If FAQ rich results return to general eligibility in future, re-enabling is a one-line change in `faqpage_ld()` (the visible FAQ source lists already exist and would generate matching markup).

### 11.3 Review schema — honest position

The strategy does **not** rely on `AggregateRating`/`Review` rich stars for the business's own reviews. Google's policy prohibits self-serving review markup (a business marking up reviews of itself) from generating review rich results, and misuse can incur penalties. Genuine reviews are **displayed on-page** as visible social proof. Review structured data is used **only** where it complies with Google's current review-snippet policy at build time, and **no rich-result eligibility is claimed or implied.**

### 11.4 areaServed — honest position

`areaServed` enumerates **genuine coverage only**, to support entity clarity and machine understanding. It is **not** a ranking shortcut, and it does **not** imply the business is locally based in every town it serves — the business is based in Pontypridd and travels. **Local and map-pack rankings depend heavily on proximity, relevance, reviews, and prominence.** Neither `areaServed` nor any other schema will make the business rank in distant, competitive towns (e.g. Cardiff, Merthyr Tydfil) from a Pontypridd base. Schema aids understanding; it does not manufacture local prominence.

**Structured data must only reflect facts genuinely offered by the business and visible on the page.** Every schema type and property is validated against current Schema.org definitions and current Google documentation before production.

### 11.5 Integrity rules

- One coherent schema graph per page; no conflicting or duplicate types.
- No markup for content that isn't genuinely present and visible on the page.
- Full control of JSON-LD on this static stack means no platform auto-injection to conflict with (unlike Wix) — but every block is still validated (Rich Results Test + Schema Markup Validator) in the pre-launch audit.

---

## 12. Technical SEO specification

Built to the highest defensible standard for static HTML on Cloudflare Pages.

### 12.1 Canonicalisation and duplicate-content control

- Self-referencing `<link rel="canonical">` on every page — absolute, non-www, HTTPS, trailing-slash-correct.
- **One canonical, enforced at three layers:** edge redirects (12.2), canonical tags, and consistent absolute internal links (all non-www HTTPS).
- Single trailing-slash convention (slash ON for directories; bare root for homepage) — prevents the trailing-slash duplicate-content trap.
- No parameters in canonical URLs; any inbound tracking parameters resolve to the clean canonical via the canonical tag.

### 12.2 Redirects (single-hop, no chains)

All configured at the Cloudflare edge, preserving full path and query string:

- `https://www.calloutphonerepairs.co.uk/*` → `https://calloutphonerepairs.co.uk/*` (301)
- `http://calloutphonerepairs.co.uk/*` → `https://calloutphonerepairs.co.uk/*` (301)
- `http://www.calloutphonerepairs.co.uk/*` → `https://calloutphonerepairs.co.uk/*` (301)
- `https://<project>.pages.dev/*` → `https://calloutphonerepairs.co.uk/*` (301) — prevents the Pages preview subdomain being indexed as duplicate content.

Verified: no redirect chains, no loops, no duplicate publicly accessible version.

### 12.3 Crawl and indexation

- `robots.txt` at root — allows crawling of all public pages, blocks nothing critical, references the sitemap. (A mistaken disallow here is a common fatal error — verify.)
- `sitemap.xml` — all 26 canonical indexable URLs, accurate `lastmod`, non-www/HTTPS/trailing-slash consistent. Excludes the 404. Submitted to Google Search Console and Bing Webmaster Tools.
- Custom `404.html` returns a true 404 status and is `noindex`.
- Flat, shallow structure — every page within 2–3 clicks of the homepage; no crawl traps, no infinite parameter space.
- **Static HTML is fully server-rendered** — perfectly crawlable by search and AI crawlers with no JavaScript-rendering dependency for content.

### 12.4 HTML quality

- Semantic HTML5: `<header> <nav> <main> <article> <section> <aside> <footer>`, appropriate landmarks.
- Exactly one `<h1>` per page; logical heading order with no skipped levels.
- Valid W3C markup (0 errors target).
- `<html lang="en-GB">`.
- Unique `<title>` and meta description per page; no duplicates.
- Descriptive `alt` on every meaningful image; `aria-label` on icon links.

### 12.5 Security

- Cloudflare automatic HTTPS + HSTS.
- No mixed content — all assets and internal links HTTPS.
- Security headers via Cloudflare: Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, and appropriate Permissions-Policy.
- SSL/TLS mode Full (Strict).

### 12.6 Links hygiene

- No broken internal links (zero tolerance).
- No redirect chains in internal links (always link to the final canonical URL directly).
- No orphan pages (every page linked from nav/footer/in-body).
- External links use appropriate `rel` attributes.

---

## 13. AI-search optimisation

AI answer engines (Google AI Overviews, and assistant-style search in ChatGPT/Perplexity/Gemini) reward: direct answers, clear structure, genuine expertise and trust (E-E-A-T), and crawlable, server-rendered content. The site's honest, structured, static build is well suited to this. The same site wins classic and AI search — there is no separate "AI version".

Concrete measures, built into every brief:

1. **Direct-answer-first structure** — each page opens by directly and honestly answering its core question before elaborating. These openers are written to be extractable.
2. **Question-shaped FAQ blocks** — concise, factual, self-contained answers (the most AI-extractable format), with `FAQPage` schema only where appropriate (11.2).
3. **Server-rendered static HTML** — content is not hidden behind JavaScript rendering, a decisive advantage over JS-heavy competitor sites that AI crawlers struggle to parse.
4. **Genuine E-E-A-T without fabrication** — a real, named person (About) if confirmed, honest process, plain parts/repair information (no warranty claims), genuine reviews as they arrive, realistic timings. No invented credentials or fabricated evidence. Trust signals are thin at launch and strengthen with real reviews over time — the design conveys credibility; reviews earn it.
5. **Semantic completeness** — covering the genuine sub-questions of each topic (symptoms, process, parts/details, coverage) signals authority far more than keyword density. (No warranty topic at launch.)
6. **Unambiguous factual statements** — clear service, areas, process, and timings so AI can represent the business accurately without hedging.

---

## 14. Performance and Core Web Vitals

**Targets (real-world mobile):** LCP < 2.5s, INP < 200ms, CLS < 0.1 — comfortably "Good".

**How the static + Cloudflare stack delivers this:**

- **Edge-served static HTML** — near-instant TTFB globally from Cloudflare's CDN.
- **Images:** next-gen formats (WebP/AVIF); correctly sized; explicit `width`/`height` on every image (prevents CLS); `loading="lazy"` below the fold; `fetchpriority="high"` on the LCP hero; responsive `srcset`/`sizes`.
- **CSS:** minimal, hand-written, no heavy framework; critical above-the-fold CSS inlined; the rest loaded without blocking render.
- **JavaScript:** vanilla only; deferred; non-render-blocking; tiny. The guided assistant and forms progressively enhance pre-existing HTML and never block the main thread.
- **Fonts (final):** self-hosted, Latin-subset **woff2** static weights (Inter 400/500/600; Space Grotesk 500/600/700), each `font-display: swap`, with the two above-the-fold weights preloaded. **No Google Fonts / no third-party font requests** — faster, privacy-conscious, resilient. Total font payload ~124 KB across six files. System-font fallback stack in place so a font failure never breaks layout.
- **Zero layout shift:** all media dimensioned; sticky bar and floating WhatsApp button reserve their own space / use transforms and never reflow content.
- **No unnecessary dependencies:** no jQuery, no framework, no heavy analytics. Privacy-friendly analytics only (Cloudflare Web Analytics).
- **Caching:** aggressive Cloudflare edge caching for static assets; sensible cache headers; immutable hashed asset filenames for cache-busting on deploy.
- **Persistent CTAs are cheap:** the floating button and sticky bar are HTML/CSS with negligible cost and no janky animation.
---

## 15. The [CONFIRM] register

Nothing in this register may be published until the owner confirms it. Grouped by type. Resolve before or during the content-writing stage; the build can begin in parallel using placeholders clearly marked in code.

### 15.1 Service capability and process

- [ ] **On-site vs exceptions per repair type** — confirmed default: most screen repairs completed on-site in ~45–60 min. Confirm which (if any) repairs cannot be completed on-site and how those are handled (honestly, case by case — not "collect and return" framing).
- [ ] **iPhone models covered** (range / oldest supported / any excluded).
- [ ] **Samsung models covered**, including whether curved-edge / AMOLED / foldable screens are taken on (and honest note that complexity/cost differ).
- [ ] **Battery** scope (brands/models); **charging port** clean-vs-replace; **camera** front/rear + lens-vs-module; **speaker** earpiece/loudspeaker/mic.
- [ ] **Water-damage recovery / microsoldering** — **do not publish** unless explicitly confirmed as offered.
- [ ] Any **timing statements** beyond the confirmed "normally ~45–60 minutes for most screen repairs".

### 15.2 Parts and repair information

- [x] **Warranty/guarantee:** NOT advertised at launch (confirmed). No warranty period, parts/workmanship guarantee, or protection claims anywhere. Removed from site.
- [ ] **Parts descriptions:** do NOT describe any part as genuine / OEM / premium / high-quality unless that exact description is verified for the specific repair. Until verified, use only the neutral "options discussed with you before work begins" wording.
- [ ] *(Future, optional)* If a formal warranty is ever introduced, it can be added as a new section/page — not present at launch.

### 15.3 Trust and identity

- [ ] **Owner's name** for the About page and `Person` schema (confirmed: happy to be named — provide the name).
- [ ] Any **genuine** background the owner can stand behind (no invented experience, qualifications, awards, or years in business).
- [x] **Imagery:** launch uses bespoke illustration / vector / device-render only — NO photography, NO fabricated repair evidence, NO stock (confirmed). Real repair/technician photos may be added later as earned. Alt text describes illustrations as illustrations, never implying real jobs.

### 15.4 Coverage detail (per location page)

- [ ] Genuine **nearby communities served** for each of the nine areas (lists in Section 10.7 are proposed and must be verified).
- [ ] Honest current **coverage reach** for the wider/expanding areas (Tonypandy, Treherbert, Aberdare, Merthyr, Caerphilly, Cardiff).

### 15.5 Opening hours

- [x] **Opening hours:** Monday–Sunday 08:00–20:00 (confirmed). Online quote submissions accepted any time; calls, messages, and appointments 08:00–20:00. No 24-hour claim. Visible copy always frames this as mobile/appointment, never walk-in.

### 15.6 Technical / operational

- [ ] **Email-sending provider** for the form (Cloudflare Email Routing/Workers, or a transactional API) — architecture confirmed (Pages Function → provider → Gmail); provider TO BE CONFIRMED.
- [ ] Optional future **branded email** (`quotes@calloutphonerepairs.co.uk`) forwarding to Gmail.
- [ ] **Privacy Policy** legal review.
- [ ] **Keyword validation** for all (✎) targets before locking titles/H1s.
- [ ] **Analytics choice** confirmed (recommended: Cloudflare Web Analytics + event tracking).

---

## 16. Cloudflare + GoDaddy deployment checklist

The domain is registered at **GoDaddy**; the site deploys on **Cloudflare Pages**. For edge redirects and rules to work, Cloudflare must manage DNS (the domain must be a Cloudflare **zone**).

- [ ] Add `calloutphonerepairs.co.uk` as a **zone** in the Cloudflare account used for Pages.
- [ ] In GoDaddy, change the **nameservers** to the Cloudflare-assigned nameservers (when ready to cut over).
- [ ] Wait for zone activation / DNS propagation; verify Cloudflare is authoritative.
- [ ] Create the Cloudflare Pages project and connect the **apex** `calloutphonerepairs.co.uk` as a custom domain.
- [ ] Add `www` as a custom domain or redirect target.
- [ ] 301 **www → non-www** (single hop; preserve path + query).
- [ ] 301 **HTTP → HTTPS** (single hop).
- [ ] 301 **`<project>.pages.dev` → canonical custom domain** (prevents duplicate indexing of the preview subdomain).
- [ ] Confirm all redirects **preserve full path + query string**.
- [ ] Verify **no redirect chains**, no loops, and **no duplicate publicly accessible version** (test www, http, and pages.dev all reach the canonical in one hop).
- [ ] Set **SSL/TLS mode to Full (Strict)**; confirm no mixed-content or certificate warnings.
- [ ] Deploy the Pages Function for form handling; configure the email provider (Section 9); test end-to-end delivery to Gmail.
- [ ] Submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools.
- [ ] Set up Cloudflare Web Analytics.

---

## 17. Pre-launch technical audit checklist

Run in full before go-live. Covers every stated quality requirement.

**Crawl & indexation**
- [ ] All canonical tags present, self-referencing, non-www / HTTPS / trailing-slash correct
- [ ] `robots.txt` correct; blocks nothing critical; references sitemap
- [x] `sitemap.xml` complete (27 URLs), valid, ready to submit (GSC + Bing)
- [ ] No orphan pages (every page linked from nav/footer/in-body)
- [ ] No `noindex` on pages meant to be indexed; 404 is `noindex` and excluded from sitemap

**Redirects & links**
- [ ] www/http/pages.dev → canonical, single-hop, path + query preserved
- [ ] No redirect chains or loops
- [ ] No broken internal links (zero tolerance)
- [ ] No accidental 404s; custom 404 works and returns 404 status
- [ ] External links valid; `rel` attributes correct

**HTML & schema**
- [ ] W3C HTML validation: 0 errors
- [ ] Exactly one `<h1>` per page; logical heading order
- [ ] No duplicate title tags or meta descriptions
- [ ] All JSON-LD validates (Rich Results Test + Schema Markup Validator); no conflicts; every type/property confirmed valid
- [ ] No schema for content not genuinely present (esp. reviews)

**Performance / CWV**
- [ ] LCP < 2.5s, INP < 200ms, CLS < 0.1 (mobile)
- [ ] Images next-gen, sized, lazy/eager correct, LCP prioritised
- [ ] No render-blocking resources; JS deferred
- [ ] No layout shift (sticky bar / floating button verified)

**Security & correctness**
- [ ] HTTPS everywhere; HSTS; no mixed content
- [ ] Security headers present
- [ ] No JavaScript console errors on any page
- [ ] Forms: submit, validate server-side, spam-protected, show confirmation, never fail silently, log submissions
- [ ] WhatsApp / Call / Quote links correct and tracked

**Accessibility (WCAG AA)**
- [ ] Colour contrast, visible focus states, full keyboard navigation, skip link
- [ ] All meaningful images have descriptive `alt`; icons have `aria-label`
- [ ] Form fields labelled; errors announced to assistive technology
- [ ] Landmarks correct; `aria-current` / `aria-expanded` set

**SEO / content**
- [ ] Every page: unique title, meta, H1, canonical
- [ ] Internal linking rules applied; anchors descriptive, not over-optimised
- [ ] NAP consistent site-wide and matches the Google Business Profile exactly
- [ ] Keyword map validated; no cannibalisation
- [ ] No thin pages — every location page carries genuinely unique local content
- [ ] Availability framed as mobile/appointment everywhere (no walk-in implication)
- [ ] Repair timing framed as "normally ~45–60 min"; no "collect and return" implication; no absolute promises
- [ ] No [CONFIRM] item published unverified

---

## 18. Post-launch and long-term growth

### 18.1 The review engine (the compounding asset)

The site launches with zero reviews. The goal is a **steady, genuine, ethically generated review stream** — not an artificial burst, which risks Google's spam filters and can suppress or remove reviews. Reframed realistically: build a machine that turns the highest possible share of real jobs into real reviews, reaching scale over months. A steady, recent, consistent curve ranks better than a spike.

- Ask in person at the moment the repair is finished and the customer is happy; follow up with a WhatsApp containing the direct Google review link (one tap).
- Reply to every review, briefly and personally.
- Encourage customers to mention, in their own words, what was fixed and where — legitimate local relevance; never scripted, never incentivised, never faked, never gated. Ask everyone, not only the happy ones (gating is against Google policy).
- Surface area-specific reviews on the matching location page as they arrive — this is the unique local content that makes each location page permanently non-doorway, and it is the moat a national competitor cannot replicate.

### 18.2 Google Business Profile

- **Primary category:** "Mobile phone repair shop" (the single most important relevance field).
- **Secondary categories:** genuinely relevant only (e.g. phone repair service, electronics repair) — never padded.
- **Service-area business with the address hidden**; areas set to genuine coverage, expanded only as coverage genuinely grows.
- Populate services (screen first), a natural 750-char description (mobile/appointment framing), and genuine photos/video.
- **Set opening hours to Monday–Sunday 08:00–20:00** — matching the website and schema exactly. Do not set the profile to "Open 24 hours".
- Google Posts regularly (freshness/engagement — a supporting signal, not a ranking driver on its own).
- **Honest expectation:** the profile can compete in the map pack for Pontypridd and near-RCT; it will not rank in distant, competitive towns from a Pontypridd base regardless of profile optimisation. Photos, Posts, and service-area entries support conversion and clarity; reviews and proximity drive local rank.

### 18.3 Citations

- Consistent NAP across UK directories (Yell, Thomson Local, Bing Places, Apple Business Connect, Facebook, relevant local South Wales directories).
- Character-for-character NAP consistency is the rule that matters.

### 18.4 Content growth roadmap

- **Model-level screen depth** under the iPhone and Samsung sub-pillars (highest-demand models first, validated by demand) — the biggest differentiator most local competitors ignore.
- **Advice layer** (`/advice/`) — honest, genuinely useful articles ("what to do the moment you crack your screen", "genuine vs aftermarket screens", "repair or replace?") that capture top-of-funnel and informational/AI-search traffic and link down to commercial screen pages.
- **B2B expansion** (`/for-business/`) — published when ready; structure already reserved, no redesign needed.
- Strengthen location pages continuously with real reviews per area (and genuine repair photos later, once the business has them). Never fabricate proof.

### 18.5 Measurement

- Track WhatsApp clicks, calls, and quote submissions per page/channel (Section 9.4) to see what converts and invest accordingly.
- Review Search Console (queries, pages, coverage) monthly; refine titles/content from real query data.
- **Launch strong, then improve from real evidence** — which pages get enquiries, what customers actually ask, which areas convert — rather than trying to perfect everything pre-launch.

---

## 19. Honest expectations

- **No ranking guarantees.** No one can promise position one. This document builds the strongest defensible foundation; rankings depend on competition, reviews, proximity, and time.
- **Screen cluster + reviews + honest content** are the engine. The technical foundation is necessary but not sufficient — its absence would lose, but on its own it does not win.
- **Distant towns are a slow organic game.** Cardiff especially is a multi-month challenger effort, not a launch win, and an organic (not map-pack) target from a Pontypridd base.
- **The site's durable advantage** is genuine local proof (real reviews and photos per area) plus screen-repair topical depth — things competitors find genuinely hard to replicate.

---

## 20. Next step

On approval of this blueprint, proceed to the production build: complete, organised, documented, deployment-ready static HTML / CSS / vanilla JavaScript for Cloudflare Pages, implementing every specification above. Outstanding [CONFIRM] items are handled with clearly marked placeholders in code and must be resolved before the corresponding content goes live.

*End of Master Website Blueprint.*
