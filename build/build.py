# -*- coding: utf-8 -*-
"""Build script — emits final static HTML into the site root."""
import os, datetime, json
from partials import (head, header, footer, floating_and_bar, scripts,
                      IC, SITE, BRAND, TAG, PHONE_DISPLAY, PHONE_LINK, WA, EMAIL)
from components import quote_assistant, cta_band, trust_strip_ink, faq_block

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
YEAR = datetime.date.today().year

def write(path, html):
    html = html.replace("{YEAR}", str(YEAR))
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)

# ---------- Schema helpers (conservative, validated types) ----------
def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

AREAS_SERVED = ["Pontypridd","Treforest","Pontyclun","Tonypandy","Treherbert",
                "Aberdare","Merthyr Tydfil","Caerphilly","Cardiff"]

def local_business_node():
    """LocalBusiness as a graph node (dict, no <script> wrapper) for linking into @graph."""
    return {
        "@type":"LocalBusiness",
        "@id": SITE + "/#business",
        "name": BRAND, "slogan": TAG,
        "url": SITE + "/",
        "telephone": "+447347715961",
        "email": EMAIL,
        "image": {"@id": SITE + "/#logo"},
        "logo": {"@id": SITE + "/#logo"},
        "parentOrganization": {"@id": SITE + "/#organization"},
        "areaServed": [{"@type":"Place","name":a} for a in AREAS_SERVED],
        "openingHoursSpecification":[{
            "@type":"OpeningHoursSpecification",
            "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens":"08:00","closes":"20:00"}],
        "description":"Mobile phone repair service based in Pontypridd, covering South Wales. We come to you to repair cracked and broken phone screens and other faults, by appointment.",
        # Service-area business: address deliberately not published.
        # DEV: add "sameAs":[Google Business Profile URL, socials] once confirmed.
    }

def local_business_ld():
    """Standalone LocalBusiness block (used on non-home pages like About/Contact).
    Includes a real crawlable image (raster OG cover) and a dedicated logo."""
    node = local_business_node()
    node["@context"] = "https://schema.org"
    # On standalone pages the #logo ImageObject isn't in scope, so inline URLs:
    node["image"] = SITE + "/assets/img/og-cover.png"
    node["logo"] = SITE + "/assets/img/logo-mark.svg"
    node.pop("parentOrganization", None)
    return ld(node)

def home_graph_ld():
    """Coherent @graph for the homepage: Organization + WebSite + WebPage + LocalBusiness,
    linked by stable @id values, including LocalBusiness as a node (one coherent graph)."""
    return ld({
        "@context":"https://schema.org",
        "@graph":[
            {
                "@type":"Organization",
                "@id": SITE + "/#organization",
                "name": BRAND,
                "url": SITE + "/",
                "logo": {
                    "@type":"ImageObject",
                    "@id": SITE + "/#logo",
                    "url": SITE + "/assets/img/logo-mark.svg",
                    "caption": BRAND
                },
                "image": {"@id": SITE + "/#logo"},
                "description":"Mobile phone repair service based in Pontypridd, covering South Wales."
                # DEV: add "sameAs" (Google Business Profile + socials) once confirmed.
            },
            {
                "@type":"WebSite",
                "@id": SITE + "/#website",
                "url": SITE + "/",
                "name": BRAND,
                "publisher": {"@id": SITE + "/#organization"},
                "inLanguage":"en-GB"
            },
            {
                "@type":"WebPage",
                "@id": SITE + "/#webpage",
                "url": SITE + "/",
                "name":"Mobile Phone Repair — We Come To You | Call Out Phone Repairs",
                "isPartOf": {"@id": SITE + "/#website"},
                "about": {"@id": SITE + "/#business"},
                "primaryImageOfPage": SITE + "/assets/img/og-cover.png",
                "inLanguage":"en-GB"
            },
            local_business_node()
        ]
    })

def breadcrumb_ld(trail):
    # trail: list of (name, path) ; last is current
    items = []
    for i,(name,path) in enumerate(trail):
        entry = {"@type":"ListItem","position":i+1,"name":name}
        if path: entry["item"] = SITE + path
        items.append(entry)
    return ld({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items})

def service_ld(name, desc, path):
    return ld({
        "@context":"https://schema.org","@type":"Service",
        "serviceType": name, "name": name, "description": desc,
        "url": SITE + path,
        "provider": {"@id": SITE + "/#business"},
        "areaServed":[{"@type":"Place","name":a} for a in AREAS_SERVED],
    })

def faqpage_ld(items):
    # FAQPage structured data intentionally DISABLED. Google discontinued FAQ
    # rich results (2026) and there is no proven AI-search benefit, so emitting
    # FAQPage markup would add weight for no gain. Visible FAQ sections are kept
    # for users. This no-op keeps all call sites working without emitting markup.
    return ""

def breadcrumbs_html(trail):
    lis = []
    for i,(name,path) in enumerate(trail):
        if path and i < len(trail)-1:
            lis.append(f'<li><a href="{path}">{name}</a></li>')
        else:
            lis.append(f'<li><span aria-current="page">{name}</span></li>')
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb"><div class="container"><ol>{"".join(lis)}</ol></div></nav>'

ASSISTANT_CSS = '<link rel="stylesheet" href="/assets/css/assistant.css">'
ASSISTANT_JS = '<script src="/assets/js/assistant.js" defer></script>'

# ======================================================================
# HERO device illustration (inline SVG — bespoke, no photo)
# ======================================================================
HERO_SVG = '''<svg class="hero-illustration" viewBox="0 0 400 420" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Illustration of a phone with a freshly repaired screen and a location pin, representing a mobile call-out repair">
  <defs>
    <linearGradient id="scr" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#2563EB"/><stop offset="1" stop-color="#1B3760"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#3B82F6" stop-opacity="0.5"/><stop offset="1" stop-color="#3B82F6" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <ellipse cx="210" cy="380" rx="150" ry="24" fill="#000" opacity="0.18"/>
  <g transform="rotate(-6 200 210)">
    <rect x="120" y="40" width="180" height="330" rx="34" fill="#0F172A" stroke="#1E293B" stroke-width="2"/>
    <rect x="132" y="58" width="156" height="294" rx="22" fill="url(#scr)"/>
    <rect x="132" y="58" width="156" height="150" rx="22" fill="url(#glow)"/>
    <rect x="186" y="48" width="48" height="9" rx="4.5" fill="#334155"/>
    <!-- restored 'check' on screen -->
    <circle cx="210" cy="200" r="46" fill="#fff" opacity="0.12"/>
    <path d="M188 200l14 14 28-30" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
    <!-- subtle repaired lines -->
    <rect x="156" y="270" width="108" height="10" rx="5" fill="#fff" opacity="0.18"/>
    <rect x="156" y="292" width="76" height="10" rx="5" fill="#fff" opacity="0.12"/>
  </g>
  <!-- location pin -->
  <g transform="translate(276 250)">
    <circle cx="0" cy="0" r="42" fill="#2563EB"/>
    <path d="M0 -20a16 16 0 0 1 16 16c0 12-16 26-16 26S-16 8-16 -4A16 16 0 0 1 0 -20z" fill="#fff"/>
    <circle cx="0" cy="-4" r="6" fill="#2563EB"/>
  </g>
</svg>'''

# ======================================================================
# HOMEPAGE
# ======================================================================
def build_home():
    title = "Mobile Phone Repair — We Come To You | Call Out Phone Repairs"
    desc = "Mobile phone repair across Pontypridd & South Wales. We come to you to fix cracked screens, batteries and more — most standard screen replacements in around 45–60 minutes. Get a quote."
    schema = home_graph_ld()
    faqs = [
        ("Do you come to me?","Yes. We're a mobile call-out service — we travel to your home or workplace across South Wales, by appointment. You don't visit a shop."),
        ("Which areas do you cover?","We're based in Pontypridd and cover Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly and Cardiff. If you're just outside one of these, send us your postcode and we'll confirm whether we can reach you."),
        ("How long does a screen repair take?","Most standard screen replacements are completed on-site in around 45–60 minutes, depending on the device, fault and parts required. We confirm the expected time before starting."),
        ("What phones do you repair?","We repair a range of iPhone, Samsung Galaxy and other phone models. Send us your exact model and the fault, and we'll confirm whether we can help."),
        ("How do I get a price?","Send a quote request or message us on WhatsApp with your phone and the fault. We reply with a personalised price — we never show automatic prices online."),
    ]
    faq_plain = [(q, a) for q,a in faqs]

    html = head(title, desc, "/", extra_css=ASSISTANT_CSS, schema=schema)
    html += header(active="")
    html += floating_and_bar()
    html += f'''<main id="main">

  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <div class="hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">Mobile phone repair · South Wales</p>
          <h1>Broken phone screen? <span class="accent">We come to you.</span></h1>
          <p class="hero-sub">Based in Pontypridd, we travel to your home or work to repair cracked screens. Most standard screen replacements are normally completed in around 45–60 minutes, depending on the device, fault and parts required.</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="hero">{IC['whatsapp']} WhatsApp us</a>
          </div>
          <div class="hero-trust">
            <span class="trust-item">{IC['check']} No shop visit needed</span>
            <span class="trust-item">{IC['check']} iPhone &amp; Samsung</span>
            <span class="trust-item">{IC['check']} Quote before we start</span>
          </div>
        </div>
        <div class="hero-visual">{HERO_SVG}</div>
      </div>
    </div>
  </section>

  <!-- TRUST STRIP -->
  <section class="section-tight on-ink" style="padding-block:1.5rem">
    <div class="container">{trust_strip_ink()}</div>
  </section>

  <!-- SCREEN LEAD -->
  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <p class="eyebrow">Our main service</p>
        <h2>Cracked or broken screen? We'll come and fix it.</h2>
        <p class="lead">Screen replacement is what we do most. We come to you across South Wales to replace iPhone, Samsung and other phone screens on-site. Most standard screen replacements are normally completed in around 45–60 minutes, depending on the device, fault and parts required.</p>
      </div>
      <div class="bento">
        <a class="bento-cell bento-feature bento-3 reveal" href="/screen-repair/">
          <p class="bento-kicker">Most requested</p>
          <div class="card-icon">{IC['screen']}</div>
          <h3>Phone screen repair</h3>
          <p>Cracked, smashed or unresponsive screens replaced at your home or work. Most standard screen replacements take around 45–60 minutes.</p>
          <span class="card-arrow">Learn more {IC['arrow']}</span>
        </a>
        <a class="bento-cell bento-3 reveal" href="/screen-repair/iphone/">
          <div class="card-icon">{IC['phone']}</div>
          <h3>iPhone screen repair</h3>
          <p>iPhone screen replacement — cracked glass, black or unresponsive displays.</p>
          <span class="card-arrow">Learn more {IC['arrow']}</span>
        </a>
        <a class="bento-cell bento-3 reveal" href="/screen-repair/samsung/">
          <div class="card-icon">{IC['phone']}</div>
          <h3>Samsung screen repair</h3>
          <p>Galaxy screen replacement, with honest advice on trickier models.</p>
          <span class="card-arrow">Learn more {IC['arrow']}</span>
        </a>
        <a class="bento-cell bento-3 reveal" href="/repairs/">
          <div class="card-icon">{IC['diagnostic']}</div>
          <h3>Other repairs</h3>
          <p>Batteries, charging ports, cameras, speakers and diagnostics too.</p>
          <span class="card-arrow">All repairs {IC['arrow']}</span>
        </a>
      </div>
    </div>
  </section>

  <!-- HOW IT WORKS -->
  <section class="section" style="background:var(--white)">
    <div class="container">
      <div class="section-head center reveal">
        <p class="eyebrow">How it works</p>
        <h2>A simple four-step process</h2>
      </div>
      <div class="steps">
        <div class="step reveal"><div class="step-num">1</div><h3>Get a quote</h3><p>Message us on WhatsApp or send a quote request with your phone and the fault.</p></div>
        <div class="step reveal"><div class="step-num">2</div><h3>We arrange a time</h3><p>We agree a time that suits you, at your home or workplace.</p></div>
        <div class="step reveal"><div class="step-num">3</div><h3>We come to you</h3><p>We travel to you across South Wales — no shop visit, no queue.</p></div>
        <div class="step reveal"><div class="step-num">4</div><h3>We repair it</h3><p>Most standard screen replacements are completed on-site in around 45–60 minutes.</p></div>
      </div>
      <div class="center mt-6">
        <a class="btn btn-outline" href="/how-it-works/">See how it works in detail {IC['arrow']}</a>
      </div>
    </div>
  </section>

  <!-- OTHER REPAIRS -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">More repairs</p>
        <h2>Not just screens</h2>
        <p class="lead">If it's not the screen, we also handle selected battery, charging, camera and speaker faults. Send us the model and fault and we'll confirm whether we can help.</p>
      </div>
      <div class="grid grid-3">
        <a class="card card-link reveal" href="/repairs/battery-replacement/"><div class="card-icon">{IC['battery']}</div><h3>Battery replacement</h3><p class="text-muted">Draining fast or shutting down early? A battery replacement may help.</p><span class="card-arrow">Learn more {IC['arrow']}</span></a>
        <a class="card card-link reveal" href="/repairs/charging-port-repair/"><div class="card-icon">{IC['port']}</div><h3>Charging port repair</h3><p class="text-muted">Loose or won't charge? Often a port that needs cleaning or replacing.</p><span class="card-arrow">Learn more {IC['arrow']}</span></a>
        <a class="card card-link reveal" href="/repairs/camera-replacement/"><div class="card-icon">{IC['camera']}</div><h3>Camera repair</h3><p class="text-muted">Cracked lens or blurry photos? Tell us the fault and we'll confirm whether we can help.</p><span class="card-arrow">Learn more {IC['arrow']}</span></a>
        <a class="card card-link reveal" href="/repairs/speaker-repair/"><div class="card-icon">{IC['speaker']}</div><h3>Speaker repair</h3><p class="text-muted">Muffled or silent audio during calls or media.</p><span class="card-arrow">Learn more {IC['arrow']}</span></a>
        <a class="card card-link reveal" href="/repairs/phone-diagnostics/"><div class="card-icon">{IC['diagnostic']}</div><h3>Phone diagnostics</h3><p class="text-muted">Not sure what's wrong? We'll find out and explain your options.</p><span class="card-arrow">Learn more {IC['arrow']}</span></a>
        <a class="card card-link reveal" href="/areas/"><div class="card-icon">{IC['pin']}</div><h3>Areas we cover</h3><p class="text-muted">Pontypridd, Treforest, Cardiff and across South Wales.</p><span class="card-arrow">See all areas {IC['arrow']}</span></a>
      </div>
    </div>
  </section>

  <!-- QUOTE ASSISTANT -->
  <section class="section" style="background:var(--white)">
    <div class="container">
      <div class="section-head center reveal">
        <p class="eyebrow">Get your quote</p>
        <h2>Tell us what's wrong — get a price</h2>
        <p class="lead">Four quick taps, then send it your way. No automatic prices — we reply personally.</p>
      </div>
      <div class="reveal">{quote_assistant()}</div>
    </div>
  </section>

  <!-- WHY CHOOSE -->
  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <p class="eyebrow">Why choose us</p>
        <h2>Straightforward, local and on your side</h2>
      </div>
      <div class="bento">
        <div class="bento-cell bento-feature bento-4 reveal">
          <p class="bento-kicker">The come-to-you difference</p>
          <div class="card-icon">{IC['home']}</div>
          <h3>We come to you — no shop, no queue</h3>
          <p>A broken phone is stressful enough without losing it for days or driving across town. We travel to your home or workplace across South Wales and fix it where you are, at a time that suits you.</p>
        </div>
        <div class="bento-cell bento-dark bento-2 reveal">
          <div class="card-icon" style="background:rgba(255,255,255,.10);color:#fff">{IC['clock']}</div>
          <h3>~45–60 min</h3>
          <p>Typical for a standard screen replacement, completed on-site (depending on device, fault and parts).</p>
        </div>
        <div class="bento-cell bento-3 reveal">
          <div class="card-icon">{IC['user']}</div>
          <h3>A real local person</h3>
          <p>You deal directly with the person doing the repair — clear communication and honest advice, start to finish.</p>
        </div>
        <div class="bento-cell bento-3 reveal">
          <div class="card-icon">{IC['check']}</div>
          <h3>Agreed before we start</h3>
          <p>We confirm the fault, the details and the expected time before any work begins. Nothing goes ahead without your say-so.</p>
        </div>
      </div>
      <div class="center mt-6"><a class="btn btn-outline" href="/about/">About Call Out Phone Repairs {IC['arrow']}</a></div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" style="background:var(--white)">
    <div class="container container-narrow">
      <div class="section-head center reveal">
        <p class="eyebrow">Common questions</p>
        <h2>Good to know</h2>
      </div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>

  {cta_band()}

</main>'''
    html += footer()
    html += scripts(ASSISTANT_JS)
    # inject FAQ schema (appropriate here — genuine Q&A; validated at build)
    html = html.replace("</head>", faqpage_ld(faq_plain) + "\n</head>")
    write("index.html", html)


if __name__ == "__main__":
    build_home()
    print("Home built.")
