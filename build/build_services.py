# -*- coding: utf-8 -*-
"""Screen cluster + get-a-quote pages."""
from partials import head, header, footer, floating_and_bar, scripts, IC, SITE, WA, PHONE_DISPLAY, PHONE_LINK
from components import quote_assistant, cta_band, trust_strip_ink, faq_block
from build import (write, local_business_ld, breadcrumb_ld, service_ld, faqpage_ld,
                   breadcrumbs_html, ASSISTANT_CSS, ASSISTANT_JS)

def page_shell(title, desc, path, active, schema, body, crumbs, faq_plain=None):
    html = head(title, desc, path, extra_css=ASSISTANT_CSS, schema=schema)
    html += header(active=active)
    html += floating_and_bar()
    html += breadcrumbs_html(crumbs)
    html += f'<main id="main">{body}</main>'
    html += footer()
    html += scripts(ASSISTANT_JS)
    if faq_plain:
        html = html.replace("</head>", faqpage_ld(faq_plain) + "\n</head>")
    write(path.lstrip("/") + "index.html" if path.endswith("/") else path, html)

def inline_quote_section(head_kicker="Get your quote", head_title="Get a price for your repair",
                         lead="Four quick taps — then send it your way. No automatic prices — we reply personally."):
    return f'''<section class="section" style="background:var(--white)">
  <div class="container">
    <div class="section-head center reveal">
      <p class="eyebrow">{head_kicker}</p>
      <h2>{head_title}</h2>
      <p class="lead">{lead}</p>
    </div>
    <div class="reveal">{quote_assistant()}</div>
  </div>
</section>'''

# ---- device illustration for screen pages ----
def device_svg(label, cracked=True):
    crack = '''<path d="M70 40l14 26-20 16 22 30-16 40" stroke="#2563EB" stroke-width="2.5" fill="none" opacity="0.9"/>
    <path d="M84 66l24 6M64 82l-20 8M86 112l26 2" stroke="#2563EB" stroke-width="2" fill="none" opacity="0.7"/>''' if cracked else ''
    return f'''<svg viewBox="0 0 160 300" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}" class="device-illus">
      <rect x="20" y="10" width="120" height="280" rx="26" fill="#0F172A" stroke="#1E293B" stroke-width="2"/>
      <rect x="30" y="26" width="100" height="248" rx="16" fill="#1E293B"/>
      <rect x="64" y="18" width="32" height="7" rx="3.5" fill="#334155"/>
      {crack}
    </svg>'''

def build_screen_pillar():
    title = "Phone Screen Repair & Replacement | We Come To You — South Wales"
    desc = "Cracked or smashed phone screen? We come to you across Pontypridd & South Wales to replace it. Most standard screen replacements take around 45–60 minutes. Get a quote."
    path = "/screen-repair/"
    crumbs = [("Home","/"),("Screen Repair","/screen-repair/")]
    schema = (breadcrumb_ld(crumbs) +
              service_ld("Phone screen repair",
                         "Mobile phone screen replacement for cracked, smashed and unresponsive screens, carried out at the customer's home or workplace across South Wales.",
                         path))
    faqs = [
        ("Can you replace a smashed screen?","Yes. Cracked glass, a black or flickering display, unresponsive touch and lines across the screen are all things we replace — we come to you to do it."),
        ("Do you fix screens at my home?","Yes. We're a mobile call-out service and most standard screen replacements are completed on-site during the appointment."),
        ("How long does a screen repair take?","Most standard screen replacements take around 45–60 minutes, depending on the device, fault and parts required. We confirm the expected time before we start."),
        ("Do you repair both iPhone and Samsung screens?","Yes — see our dedicated iPhone and Samsung screen pages. We also repair a range of other phone models — send us yours and we'll confirm."),
        ("How are parts and details decided?","The exact part options and details for your repair are discussed and agreed with you before any work begins, so you always know what's involved first."),
        ("How do I get a quote?","Send a quote request or message us on WhatsApp with your phone model and the fault. We'll reply with a personalised price."),
    ]
    body = f'''
  <section class="section">
    <div class="container">
      <div class="hero-grid" style="align-items:center">
        <div class="reveal">
          <p class="eyebrow">Screen repair · our main service</p>
          <h1>Phone screen repair &amp; replacement</h1>
          <p class="lead" style="margin:1rem 0 1.5rem">Cracked or smashed your screen? We come to you across Pontypridd and South Wales to replace it on-site. Most standard screen replacements are normally completed in around 45–60 minutes, depending on the device, fault and parts required — and we confirm the expected time before we start.</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="screenhero">{IC['whatsapp']} WhatsApp us</a>
          </div>
        </div>
        <div class="hero-visual reveal">{device_svg("Illustration of a phone with a cracked screen", cracked=True)}</div>
      </div>
    </div>
  </section>

  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>

  <section class="section">
    <div class="container container-narrow stack-lg">
      <div class="reveal">
        <h2>Cracked, smashed or faulty screens we repair</h2>
        <p class="mt-4">If your screen is damaged or misbehaving, we can almost certainly help. Common problems we replace screens for include:</p>
        <div class="grid grid-2 mt-4">
          <div class="card"><h3 style="font-size:1.05rem">Cracked or smashed glass</h3><p class="text-muted">From a hairline crack to a completely shattered front.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Black or blank display</h3><p class="text-muted">The phone works but the screen shows nothing.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Unresponsive touch</h3><p class="text-muted">Taps and swipes don't register, or register in the wrong place.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Lines or discolouration</h3><p class="text-muted">Coloured lines, blotches or flickering across the display.</p></div>
        </div>
      </div>

      <div class="reveal">
        <h2>iPhone and Samsung screen repairs</h2>
        <p class="mt-4">Most of what we do is iPhone and Samsung. We've got dedicated pages explaining each, including honest notes on the trickier models.</p>
        <div class="grid grid-2 mt-4">
          <a class="card card-link" href="/screen-repair/iphone/"><div class="card-icon">{IC['phone']}</div><h3>iPhone screen repair</h3><p class="text-muted">Cracked glass, black or unresponsive iPhone displays.</p><span class="card-arrow">iPhone screens {IC['arrow']}</span></a>
          <a class="card card-link" href="/screen-repair/samsung/"><div class="card-icon">{IC['phone']}</div><h3>Samsung screen repair</h3><p class="text-muted">Galaxy screen replacement, with clear advice on curved and foldable models.</p><span class="card-arrow">Samsung screens {IC['arrow']}</span></a>
        </div>
      </div>

      <div class="reveal">
        <h2>How screen repairs work — we come to you</h2>
        <p class="mt-4">You don't visit a shop and you don't lose your phone for the day. We agree a time, travel to your home or workplace, and replace the screen while you're there. Most standard screen replacements take around 45–60 minutes. If a particular repair is more involved, we'll explain that and agree it with you before starting.</p>
        <p class="mt-4"><a href="/how-it-works/">See how our mobile service works {IC['arrow']}</a></p>
      </div>

      <div class="reveal">
        <h2>Parts &amp; repair information</h2>
        <p class="mt-4">We keep it simple and clear: the exact part options, availability and details for your repair are discussed and agreed with you before any work begins — so you always know what's involved first.</p>
        <p class="mt-4"><a href="/parts-and-repair-information/">Read our parts &amp; repair information {IC['arrow']}</a></p>
      </div>

      <div class="reveal">
        <h2>Areas we cover</h2>
        <p class="mt-4">We're based in Pontypridd and travel across South Wales — including Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly and Cardiff.</p>
        <p class="mt-4"><a href="/areas/">See all areas we cover {IC['arrow']}</a></p>
      </div>
    </div>
  </section>

  {inline_quote_section(head_title="Get a quote for your screen repair")}

  <section class="section">
    <div class="container container-narrow">
      <div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>Screen repair FAQs</h2></div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>

  {cta_band()}
'''
    page_shell(title, desc, path, "screen", schema, body, crumbs, faq_plain=faqs)


def build_iphone():
    title = "iPhone Screen Repair & Replacement | We Come To You — South Wales"
    desc = "Cracked iPhone screen? We come to you across Pontypridd & South Wales to replace it — most standard iPhone screens in around 45–60 minutes. Get a quote."
    path = "/screen-repair/iphone/"
    crumbs = [("Home","/"),("Screen Repair","/screen-repair/"),("iPhone","/screen-repair/iphone/")]
    schema = (breadcrumb_ld(crumbs) +
              service_ld("iPhone screen repair",
                         "Mobile iPhone screen replacement carried out at the customer's home or workplace across South Wales.", path))
    faqs = [
        ("Which iPhone models do you repair?","We repair a range of iPhone models. Tell us your exact model when you enquire and we'll confirm whether we can help."),
        ("Do you come to me for an iPhone screen repair?","Yes — we're mobile. We travel to your home or workplace across South Wales, by appointment."),
        ("How long does an iPhone screen repair take?","Most standard iPhone screen replacements take around 45–60 minutes, depending on the model and parts required. We confirm the expected time first."),
        ("How are parts and details decided?","The part options and details for your iPhone are discussed and agreed with you before any work begins."),
        ("How do I get a quote?","Message us on WhatsApp or send a quote request with your iPhone model and the fault, and we'll reply with a price."),
    ]
    body = f'''
  <section class="section">
    <div class="container">
      <div class="hero-grid" style="align-items:center">
        <div class="reveal">
          <p class="eyebrow">iPhone screen repair</p>
          <h1>iPhone screen repair &amp; replacement</h1>
          <p class="lead" style="margin:1rem 0 1.5rem">Cracked your iPhone screen? We come to you across Pontypridd and South Wales to replace it at your home or work. Most standard iPhone screen replacements are normally completed in around 45–60 minutes, depending on the model, fault and parts required.</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="iphonehero">{IC['whatsapp']} WhatsApp us</a>
          </div>
        </div>
        <div class="hero-visual reveal">{device_svg("Illustration of an iPhone with a cracked screen", cracked=True)}</div>
      </div>
    </div>
  </section>

  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>

  <section class="section">
    <div class="container container-narrow stack-lg">
      <div class="reveal">
        <h2>iPhone models we repair</h2>
        <p class="mt-4">We repair screens on a range of iPhone models, recent and older. When you get in touch, just tell us your exact model and we'll confirm whether we can help and what's involved. <!-- DEV: confirm exact supported iPhone range with owner --></p>
      </div>
      <div class="reveal">
        <h2>Common iPhone screen problems</h2>
        <div class="grid grid-2 mt-4">
          <div class="card"><h3 style="font-size:1.05rem">Cracked or shattered glass</h3><p class="text-muted">The most common one — from a small crack to a fully smashed front.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Black or unresponsive display</h3><p class="text-muted">The phone is on but the screen won't show or respond.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Touch not working</h3><p class="text-muted">Ghost touches, dead zones, or taps landing in the wrong place.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Lines or flickering</h3><p class="text-muted">Coloured lines or a flickering image after a drop.</p></div>
        </div>
      </div>
      <div class="reveal">
        <h2>iPhone screen parts &amp; repair details</h2>
        <p class="mt-4">The exact part options and details for your iPhone repair are discussed and agreed with you before any work begins. <a href="/parts-and-repair-information/">More on parts &amp; repair information {IC['arrow']}</a></p>
      </div>
      <div class="reveal">
        <h2>Areas we cover</h2>
        <p class="mt-4">Based in Pontypridd, we travel across South Wales. <a href="/areas/">See all areas {IC['arrow']}</a> · Also see <a href="/screen-repair/samsung/">Samsung screen repair</a>.</p>
      </div>
    </div>
  </section>

  {inline_quote_section(head_title="Get an iPhone screen repair quote")}

  <section class="section">
    <div class="container container-narrow">
      <div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>iPhone screen repair FAQs</h2></div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>
  {cta_band(heading="Cracked iPhone screen? We'll come to you.")}
'''
    page_shell(title, desc, path, "screen", schema, body, crumbs, faq_plain=faqs)


def build_samsung():
    title = "Samsung Screen Repair & Replacement | We Come To You — South Wales"
    desc = "Cracked Samsung Galaxy screen? We come to you across Pontypridd & South Wales to replace it. Honest advice on curved and foldable models. Get a quote."
    path = "/screen-repair/samsung/"
    crumbs = [("Home","/"),("Screen Repair","/screen-repair/"),("Samsung","/screen-repair/samsung/")]
    schema = (breadcrumb_ld(crumbs) +
              service_ld("Samsung screen repair",
                         "Mobile Samsung Galaxy screen replacement carried out at the customer's home or workplace across South Wales.", path))
    faqs = [
        ("Which Samsung models do you repair?","We repair screens on a range of Samsung Galaxy models. Tell us your exact model and we'll confirm whether we can help."),
        ("Do you repair curved or foldable Samsung screens?","Some Galaxy models — including curved-edge, AMOLED and foldable screens — are more involved than a standard flat screen. Tell us your exact model and we'll give you honest advice on what's possible and what's involved before anything goes ahead."),
        ("Do you come to me?","Yes — we're mobile and travel to your home or workplace across South Wales, by appointment."),
        ("How are parts and details decided?","The part options and details for your Samsung repair are discussed and agreed with you before any work begins."),
        ("How do I get a quote?","Send a quote request or WhatsApp us your Galaxy model and the fault, and we'll reply with a price."),
    ]
    body = f'''
  <section class="section">
    <div class="container">
      <div class="hero-grid" style="align-items:center">
        <div class="reveal">
          <p class="eyebrow">Samsung screen repair</p>
          <h1>Samsung screen repair &amp; replacement</h1>
          <p class="lead" style="margin:1rem 0 1.5rem">Cracked or broken your Samsung Galaxy screen? We come to you across Pontypridd and South Wales, with honest advice on the trickier curved and foldable models.</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="samsunghero">{IC['whatsapp']} WhatsApp us</a>
          </div>
        </div>
        <div class="hero-visual reveal">{device_svg("Illustration of a Samsung Galaxy phone with a damaged screen", cracked=True)}</div>
      </div>
    </div>
  </section>

  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>

  <section class="section">
    <div class="container container-narrow stack-lg">
      <div class="reveal">
        <h2>Samsung models we repair</h2>
        <p class="mt-4">We repair screens across a range of Galaxy models. Some are more straightforward than others, so just tell us your exact model when you enquire and we'll confirm whether we can help and what's involved.</p>
      </div>
      <div class="reveal">
        <h2>A quick honest note on curved &amp; foldable screens</h2>
        <p class="mt-4">Not all Samsung screens are the same. Curved-edge, AMOLED and foldable displays (like the Z Fold and Z Flip) are more complex than a standard flat screen. We'll always be straight with you about what's realistic for your specific model, and agree everything before any work begins — no surprises.</p>
      </div>
      <div class="reveal">
        <h2>Common Galaxy screen problems</h2>
        <div class="grid grid-2 mt-4">
          <div class="card"><h3 style="font-size:1.05rem">Cracked glass</h3><p class="text-muted">Chips and cracks from an accidental drop.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Black or dead display</h3><p class="text-muted">Screen won't light up although the phone is on.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Touch issues</h3><p class="text-muted">Unresponsive areas or erratic touch.</p></div>
          <div class="card"><h3 style="font-size:1.05rem">Lines &amp; discolouration</h3><p class="text-muted">Green or coloured lines, or spreading blotches.</p></div>
        </div>
      </div>
      <div class="reveal">
        <h2>Parts &amp; repair details</h2>
        <p class="mt-4">Part options and details are discussed and agreed with you before work begins. <a href="/parts-and-repair-information/">Parts &amp; repair information {IC['arrow']}</a> · Also see <a href="/screen-repair/iphone/">iPhone screen repair</a>.</p>
      </div>
    </div>
  </section>

  {inline_quote_section(head_title="Get a Samsung screen repair quote")}

  <section class="section">
    <div class="container container-narrow">
      <div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>Samsung screen repair FAQs</h2></div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>
  {cta_band(heading="Broken Galaxy screen? Let's take a look.")}
'''
    page_shell(title, desc, path, "screen", schema, body, crumbs, faq_plain=faqs)


def build_get_a_quote():
    title = "Get a Phone Repair Quote — We Come To You | Call Out Phone Repairs"
    desc = "Get a personalised phone repair quote. Tell us your phone and the fault — we come to you across South Wales. WhatsApp, call, or send your details."
    path = "/get-a-quote/"
    crumbs = [("Home","/"),("Get a Quote","/get-a-quote/")]
    schema = breadcrumb_ld(crumbs)
    body = f'''
  <section class="section">
    <div class="container container-narrow center">
      <p class="eyebrow" style="justify-content:center">Get your quote</p>
      <h1>Get your personalised phone repair quote</h1>
      <p class="lead mt-4">Tell us your phone and the fault and we'll come back with a price and a time that suits you. Most standard screen replacements are done at your home or work in around 45–60 minutes. Prefer to talk? Message us on WhatsApp or call.</p>
    </div>
  </section>
  <section class="section" style="padding-top:0">
    <div class="container">{quote_assistant()}</div>
  </section>
  <section class="section-tight" style="padding-top:0">
    <div class="container container-narrow center">
      <p class="text-muted">We reply during 08:00–20:00, daily. We never show automatic prices online because an accurate quote depends on your exact model and repair — and we never book or charge anything until we've spoken with you.</p>
      <div class="hero-actions" style="justify-content:center;margin-top:1.5rem">
        <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="quotepage">{IC['whatsapp']} WhatsApp us</a>
        <a class="btn btn-outline btn-lg" href="{PHONE_LINK}" data-where="quotepage">{IC['phone']} Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </section>
'''
    page_shell(title, desc, path, "", schema, body, crumbs)


def build_all():
    build_screen_pillar()
    build_iphone()
    build_samsung()
    build_get_a_quote()

if __name__ == "__main__":
    build_all()
