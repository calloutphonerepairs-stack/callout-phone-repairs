# -*- coding: utf-8 -*-
"""Trust & utility pages."""
from partials import (head, header, footer, floating_and_bar, scripts,
                      IC, SITE, BRAND, TAG, PHONE_DISPLAY, PHONE_LINK, WA, EMAIL)
from components import quote_assistant, cta_band, trust_strip_ink, faq_block
from build import (write, breadcrumb_ld, faqpage_ld, ld, local_business_ld,
                   ASSISTANT_CSS, ASSISTANT_JS)
from build_services import page_shell, inline_quote_section

def build_how_it_works():
    title = "How It Works — Mobile Phone Repair That Comes To You | Call Out Phone Repairs"
    desc = "How our mobile phone repair works: get a quote, we arrange a time, we come to you across South Wales, and most standard screens are fixed on-site in ~45–60 minutes."
    path = "/how-it-works/"
    crumbs = [("Home","/"),("How It Works","/how-it-works/")]
    faqs = [
        ("Do I need to go to a shop?","No. We're a mobile call-out service — we come to your home or workplace by appointment. There's no shop to visit."),
        ("Will my phone be taken away?","For most standard screen replacements, no — we do them on-site while you're there, normally in around 45–60 minutes. If a repair is more involved, we'll explain that and agree it with you first."),
        ("When are you available?","We handle calls, messages and appointments between 08:00 and 20:00, seven days a week. You can send a quote request at any time."),
        ("Is anything booked automatically?","No. We never confirm a booking or charge anything until we've spoken with you and agreed the details."),
    ]
    schema = breadcrumb_ld(crumbs)
    body = f'''
  <section class="section">
    <div class="container container-narrow center">
      <p class="eyebrow" style="justify-content:center">How it works</p>
      <h1>Getting your phone fixed couldn't be simpler</h1>
      <p class="lead mt-4">No shop, no queue, no leaving your phone behind for days. Here's exactly how it works, from first message to fixed phone.</p>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="steps">
        <div class="step reveal"><div class="step-num">1</div><h3>Get a quote</h3><p>Message us on WhatsApp or send a quote request with your phone model and the fault. We reply with a personalised price — no automatic prices online.</p></div>
        <div class="step reveal"><div class="step-num">2</div><h3>We arrange a time</h3><p>We agree a time and place that suits you — your home or workplace — within our hours of 08:00–20:00, daily.</p></div>
        <div class="step reveal"><div class="step-num">3</div><h3>We come to you</h3><p>We travel to you across South Wales. You don't go anywhere, and you don't lose your phone for the day.</p></div>
        <div class="step reveal"><div class="step-num">4</div><h3>We repair it</h3><p>We confirm the expected time, agree everything, then carry out the repair. Most standard screen replacements are done in around 45–60 minutes.</p></div>
      </div>
    </div>
  </section>
  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>
  <section class="section">
    <div class="container container-narrow stack-lg">
      <div class="reveal"><h2>What to expect on the day</h2><p class="mt-4">Before we start, we confirm the fault, talk through the part options and details, and tell you the expected repair time. Nothing goes ahead until you're happy. Most standard screen replacements take around 45–60 minutes, depending on the device, fault and parts required. Some repairs are more involved — if yours is, we'll explain that clearly and agree it with you before beginning.</p></div>
      <div class="reveal"><h2>Parts &amp; repair information</h2><p class="mt-4">The exact part options, availability and details for your repair are discussed and agreed with you before any work begins, so you always know what's involved. <a href="/parts-and-repair-information/">Read our parts &amp; repair information {IC['arrow']}</a></p></div>
      <div class="reveal"><h2>Payment &amp; booking</h2><p class="mt-4">We never confirm a booking or take payment automatically online. We speak with you first, agree the details, and only then arrange everything. It's a personal service, start to finish.</p></div>
    </div>
  </section>
  {inline_quote_section(head_title="Ready? Get your quote")}
  <section class="section"><div class="container container-narrow"><div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>How it works — FAQs</h2></div><div class="reveal">{faq_block(faqs)}</div></div></section>
  {cta_band()}
'''
    page_shell(title, desc, path, "how", schema, body, crumbs, faq_plain=faqs)

def build_parts_info():
    title = "Parts & Repair Information | Call Out Phone Repairs"
    desc = "How we handle parts and repairs: the exact part options, availability and details are discussed and agreed with you before any work begins. Clear and upfront."
    path = "/parts-and-repair-information/"
    crumbs = [("Home","/"),("Parts & Repair Information","/parts-and-repair-information/")]
    faqs = [
        ("How do you decide which parts to use?","It depends on your device and the fault. We discuss the part options, availability and details with you and agree them before any work begins."),
        ("Will I know the details before you start?","Yes — we confirm the fault, the options and the expected repair time with you first. Nothing goes ahead until you're happy."),
        ("How do I get a quote?","Message us on WhatsApp or send a quote request with your phone model and the fault, and we'll reply with a personalised price."),
    ]
    schema = breadcrumb_ld(crumbs)
    body = f'''
  <section class="section">
    <div class="container container-narrow">
      <p class="eyebrow">Parts &amp; repair information</p>
      <h1>Parts &amp; repair information</h1>
      <p class="lead mt-4">We keep it simple and clear. The exact part options, availability and details for your repair are discussed and agreed with you before any work begins — so you always know what's involved before we start.</p>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container container-narrow stack-lg">
      <div class="reveal"><h2>How we handle parts</h2><p class="mt-4">Every phone and every fault is a little different, so the right approach depends on your specific device and repair. Rather than make blanket claims, we talk you through the options and availability for your situation and agree the details with you first. That way there are no surprises.</p></div>
      <div class="reveal"><h2>What to expect</h2><p class="mt-4">Before any work starts, we confirm the fault, explain the options and details, and tell you the expected repair time. Nothing goes ahead until you've agreed. Most standard screen replacements take around 45–60 minutes, depending on the device, fault and parts required.</p></div>
      <div class="reveal"><h2>Straightforward and upfront</h2><p class="mt-4">Our aim is simple: you always know what's involved before we begin. If you have any questions about parts or a repair, just ask when you get in touch and we'll be happy to talk it through.</p></div>
    </div>
  </section>
  {inline_quote_section(head_title="Get your quote")}
  <section class="section"><div class="container container-narrow"><div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>Parts &amp; repair FAQs</h2></div><div class="reveal">{faq_block(faqs)}</div></div></section>
  {cta_band()}
'''
    page_shell(title, desc, path, "", schema, body, crumbs, faq_plain=faqs)

def build_about():
    title = "About Call Out Phone Repairs — Mobile Repairs in South Wales"
    desc = "Call Out Phone Repairs is a local mobile phone repair service based in Pontypridd. We come to you across South Wales with honest, straightforward repairs."
    path = "/about/"
    crumbs = [("Home","/"),("About","/about/")]
    schema = breadcrumb_ld(crumbs) + local_business_ld()
    body = f'''
  <section class="section">
    <div class="container container-narrow">
      <p class="eyebrow">About us</p>
      <h1>Local, mobile and straightforward</h1>
      <p class="lead mt-4">Call Out Phone Repairs is a mobile phone repair service based in Pontypridd, covering South Wales. The idea is simple: instead of you traipsing to a shop and leaving your phone for days, we come to you and, for many standard repairs, fix it while we're there.</p>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container container-narrow stack-lg">
      <!-- DEV: confirm owner name + any experience details before publishing a personal bio. Keep copy true and non-specific until confirmed. -->
      <div class="reveal"><h2>Why we come to you</h2><p class="mt-4">A broken phone is stressful enough without losing it for days or driving across town. As a come-to-you service, we fit around your life — your home, your workplace, a time that suits you. Most standard screen replacements are completed in around 45–60 minutes during the appointment.</p></div>
      <div class="reveal"><h2>How we work</h2><p class="mt-4">You deal directly with the person doing the repair. That means clear communication and honest advice — we tell you what's realistic, agree everything before we start, and never book or charge anything without speaking to you first. If a repair is more complex, we'll say so.</p></div>
      <div class="reveal"><h2>Built on real work, over time</h2><p class="mt-4">We're building this business the right way — on genuine repairs and honest reviews from real customers across South Wales. As those reviews come in, you'll find them on our <a href="/reviews/">reviews page</a>.</p></div>
      <div class="reveal"><h2>Where we work</h2><p class="mt-4">Based in Pontypridd, we cover Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly and Cardiff. If you're just outside one of these, send your postcode and we'll confirm. <a href="/areas/">See all areas {IC['arrow']}</a></p></div>
    </div>
  </section>
  {cta_band()}
'''
    page_shell(title, desc, path, "about", schema, body, crumbs)

def build_reviews():
    title = "Reviews — Call Out Phone Repairs | South Wales"
    desc = "Reviews for Call Out Phone Repairs, a mobile phone repair service in South Wales. Genuine customer feedback, added as it comes in."
    path = "/reviews/"
    crumbs = [("Home","/"),("Reviews","/reviews/")]
    schema = breadcrumb_ld(crumbs)
    # Honest empty-state at launch — NO fabricated reviews or star ratings.
    body = f'''
  <section class="section">
    <div class="container container-narrow center">
      <p class="eyebrow" style="justify-content:center">Reviews</p>
      <h1>What our customers say</h1>
      <p class="lead mt-4">We're a new, growing local service, and we believe reviews should be genuine — so we only publish real feedback from real customers. As we complete repairs across South Wales, verified reviews will appear here.</p>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container container-narrow">
      <div class="card reveal center" style="padding:3rem 2rem">
        <div class="card-icon" style="margin-inline:auto">{IC['sparkle']}</div>
        <h2 style="font-size:1.4rem">Been fixed by us? We'd love your feedback</h2>
        <p class="text-muted mt-4" style="max-width:46ch;margin-inline:auto">If we've repaired your phone, a quick honest review helps other people in South Wales find us — and helps us keep improving.</p>
        <div class="hero-actions" style="justify-content:center;margin-top:1.5rem">
          <a class="btn btn-whatsapp" href="{WA}" data-where="reviews">{IC['whatsapp']} Message us</a>
        </div>
        <!-- DEV: when a Google Business Profile review link is available, add a "Leave a Google review" button here. Do NOT display a star rating until a verified rating is provided. -->
      </div>
    </div>
  </section>
  {inline_quote_section(head_title="Need a repair? Get a quote")}
  {cta_band()}
'''
    page_shell(title, desc, path, "reviews", schema, body, crumbs)

def build_contact():
    title = "Contact Call Out Phone Repairs — WhatsApp, Call or Email"
    desc = "Contact Call Out Phone Repairs for mobile phone repair across South Wales. WhatsApp, call 07347 715961, or send your details. Hours 08:00–20:00 daily."
    path = "/contact/"
    crumbs = [("Home","/"),("Contact","/contact/")]
    schema = breadcrumb_ld(crumbs) + local_business_ld()
    body = f'''
  <section class="section">
    <div class="container container-narrow">
      <p class="eyebrow">Contact</p>
      <h1>Get in touch</h1>
      <p class="lead mt-4">The quickest way to reach us is WhatsApp or a call. Tell us your phone and the fault and we'll come back with a price and a time that suits you.</p>
      <div class="grid grid-3 mt-6">
        <a class="card card-link reveal" href="{WA}" data-where="contactpage"><div class="card-icon">{IC['whatsapp']}</div><h3 style="font-size:1.1rem">WhatsApp</h3><p class="text-muted">Fastest way to reach us. Message us your model and fault.</p></a>
        <a class="card card-link reveal" href="{PHONE_LINK}" data-where="contactpage"><div class="card-icon">{IC['phone']}</div><h3 style="font-size:1.1rem">Call</h3><p class="text-muted">{PHONE_DISPLAY}</p></a>
        <a class="card card-link reveal" href="mailto:{EMAIL}"><div class="card-icon">{IC['mail']}</div><h3 style="font-size:1.1rem">Email</h3><p class="text-muted">Prefer to write? Email us your details.</p></a>
      </div>
      <div class="card reveal mt-6" style="display:flex;gap:1rem;align-items:flex-start">
        <div class="card-icon" style="margin-bottom:0;flex:none">{IC['clock']}</div>
        <div>
          <h3 style="font-size:1.1rem">Hours</h3>
          <p class="text-muted">We handle calls, messages and appointments <strong>Monday–Sunday, 08:00–20:00</strong>. You can send a quote request through the website at any time and we'll reply within our hours.</p>
        </div>
      </div>
      <p class="text-muted mt-6"><strong>Please note:</strong> we're a mobile call-out service by appointment and don't operate a walk-in shop, so there's no public address to visit — we come to you.</p>
    </div>
  </section>
  {inline_quote_section(head_title="Send us your enquiry")}
  {cta_band()}
'''
    page_shell(title, desc, path, "", schema, body, crumbs)

def build_privacy():
    title = "Privacy Policy | Call Out Phone Repairs"
    desc = "How Call Out Phone Repairs handles the information you share when you enquire about a phone repair."
    path = "/privacy-policy/"
    crumbs = [("Home","/"),("Privacy Policy","/privacy-policy/")]
    schema = breadcrumb_ld(crumbs)
    # DEV: this is a plain-English starting point and must be reviewed for legal completeness before launch.
    body = f'''
  <section class="section">
    <div class="container container-narrow stack-lg">
      <div>
        <p class="eyebrow">Privacy</p>
        <h1>Privacy policy</h1>
        <p class="lead mt-4">This policy explains, in plain English, what happens to the information you share when you contact Call Out Phone Repairs.</p>
        <!-- DEV: have this reviewed for legal completeness (UK GDPR / ICO guidance) before launch. Confirm data controller name & registration details. -->
      </div>
      <div><h2>What we collect</h2><p class="mt-4">When you send a quote request or contact us, we collect the details you choose to give us — such as your name, phone number, email, location, and information about your phone and the fault. If you choose to send us a photo of the damage, please do so via WhatsApp rather than the website form.</p></div>
      <div><h2>How we use it</h2><p class="mt-4">We use your information solely to respond to your enquiry, provide a quote, and arrange and carry out any repair you ask us to. We don't sell your information, and we don't use it for anything you haven't asked us to.</p></div>
      <div><h2>How we contact you</h2><p class="mt-4">We'll get back to you using the method you've chosen or provided — WhatsApp, phone or email — about your enquiry.</p></div>
      <div><h2>Keeping your information</h2><p class="mt-4">We keep enquiry details only as long as needed to help you and to keep sensible records of work carried out, then remove them.</p></div>
      <div><h2>Your choices</h2><p class="mt-4">You can ask us what information we hold about you, ask us to correct it, or ask us to delete it. Just get in touch and we'll sort it.</p></div>
      <div><h2>Contact</h2><p class="mt-4">Questions about this policy? Contact us on WhatsApp, call {PHONE_DISPLAY}, or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div>
    </div>
  </section>
'''
    page_shell(title, desc, path, "", schema, body, crumbs)

def build_404():
    title = "Page not found | Call Out Phone Repairs"
    html = head(title, "The page you were looking for couldn't be found.", "/404.html", extra_css=ASSISTANT_CSS)
    # 404 must be noindex
    html = html.replace('<meta name="robots" content="index, follow, max-image-preview:large">',
                        '<meta name="robots" content="noindex, follow">')
    html += header(active="")
    html += floating_and_bar()
    html += f'''<main id="main">
  <section class="section" style="min-height:50vh;display:flex;align-items:center">
    <div class="container container-narrow center">
      <p class="eyebrow" style="justify-content:center">404</p>
      <h1>We couldn't find that page</h1>
      <p class="lead mt-4">The page may have moved or never existed. Let's get you back on track.</p>
      <div class="hero-actions" style="justify-content:center;margin-top:1.5rem">
        <a class="btn btn-quote btn-lg" href="/">{IC['home']} Back to home</a>
        <a class="btn btn-outline btn-lg" href="/get-a-quote/">{IC['quote']} Get a quote</a>
      </div>
      <p class="text-muted mt-6">Or jump to <a href="/screen-repair/">screen repair</a>, <a href="/areas/">areas we cover</a>, or <a href="/contact/">contact us</a>.</p>
    </div>
  </section>
</main>'''
    html += footer()
    html += scripts()
    write("404.html", html)

def build_all():
    build_how_it_works()
    build_parts_info()
    build_about()
    build_reviews()
    build_contact()
    build_privacy()
    build_404()

if __name__ == "__main__":
    build_all()
