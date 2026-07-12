# -*- coding: utf-8 -*-
"""Areas hub + location pages. Pontypridd = flagship (full). Others = unique-but-concise."""
from partials import IC, WA, PHONE_DISPLAY, PHONE_LINK, SITE, BRAND
from components import quote_assistant, cta_band, trust_strip_ink, faq_block
from build import breadcrumb_ld, faqpage_ld, ld, AREAS_SERVED
from build_services import page_shell, inline_quote_section

# slug, name, angle-intro, nearby, unique-body-sections, organic_only(bool)
LOCATIONS = [
    ("pontypridd","Pontypridd", None, None, None, False),  # flagship, handled separately
    ("treforest","Treforest",
     "Right next to our Pontypridd base, Treforest is home to the University of South Wales campus and the industrial estate — so we're often nearby fixing student phones and sorting screens for people at work.",
     None,
     [("Students &amp; USW","A cracked screen shouldn't get between you and your deadlines. We come to your accommodation or campus area, and most standard screen replacements are normally completed in around 45–60 minutes."),
      ("Treforest Industrial Estate","Working on the estate? We can come to your workplace and repair your phone with minimal disruption to your day.")], False),
    ("pontyclun","Pontyclun",
     "Pontyclun sits on the M4 commuter belt, so we cover it regularly for people who'd rather have their phone repaired at home or work than lose time to a shop.",
     None,
     [("Commuter-friendly","We come to you around your schedule — mornings, evenings or the weekend, within our 08:00–20:00 hours."),
      ("At home or at work","We repair screens, batteries and more at your home or workplace in Pontyclun.")], False),
    ("tonypandy","Tonypandy",
     "Tonypandy is a busy commercial centre in the Rhondda, and we cover it so you don't have to travel out for a phone repair.",
     None,
     [("Rhondda coverage","We travel into the Rhondda to reach you — tell us where you are and we'll confirm we can come to you."),
      ("Local &amp; convenient","No trek to a city shop; we come to your home or workplace in Tonypandy.")], False),
    ("treherbert","Treherbert",
     "Treherbert sits at the head of the Rhondda Fawr valley. It's further out, and we're always honest about that — but we do cover it, so get in touch and we'll confirm a time that works.",
     None,
     [("Valley-head honesty","Because Treherbert is further from our Pontypridd base, we'll be upfront about timing when you enquire — but distance doesn't mean we can't help."),
      ("Message us to confirm","Send us your postcode and we'll confirm a time that works.")], False),
    ("aberdare","Aberdare",
     "Aberdare is the main town of the Cynon Valley, and we cover it for screen repairs, batteries and more, carried out at your home or workplace.",
     None,
     [("Cynon Valley coverage","We come to you in Aberdare rather than the other way around."),
      ("Everyday repairs, locally","Cracked screens, tired batteries and charging problems, repaired at your home or work.")], False),
    ("merthyr-tydfil","Merthyr Tydfil",
     "Merthyr Tydfil is a large town at the top of our coverage area. It's a bit further from our Pontypridd base, so we'll always be clear about timing — but we regularly help people here.",
     None,
     [("Honest about distance","Merthyr is towards the edge of our patch. We'll confirm realistic timing when you get in touch — no vague promises."),
      ("Worth the trip","We come to you in Merthyr for screens and other repairs. Send your postcode and we'll confirm we can reach you.")], True),
    ("caerphilly","Caerphilly",
     "Caerphilly is a busy commuter town in a slightly different direction from our usual valleys run, and we cover it for people who'd rather not head into Cardiff or wait on a shop.",
     None,
     [("Commuter town coverage","We come to your home or workplace in Caerphilly so a repair fits into your day."),
      ("Message us to confirm","Send us your postcode and we'll confirm whether we can reach you.")], True),
    ("cardiff","Cardiff",
     "Cardiff is a big city and the most competitive area we cover, so we're realistic: we're strongest in the northern parts of the city closest to us, and we're building our presence here over time. If you're in Cardiff, get in touch and we'll confirm we can reach you.",
     None,
     [("North Cardiff first","We're closest to and strongest in north Cardiff. Send us your postcode and we'll confirm whether we can reach you."),
      ("Honest about the city","Cardiff has a lot of repair options. We focus on coming to you and being straight with you — not on empty promises. Tell us where you are and we'll confirm.")], True),
]

def coverage_svg(place):
    return f'''<svg viewBox="0 0 300 300" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stylised illustration of our coverage around {place}" class="device-illus">
      <circle cx="150" cy="150" r="120" fill="#EFF5FF"/>
      <circle cx="150" cy="150" r="120" stroke="#BFD3F5" stroke-width="2" stroke-dasharray="6 8"/>
      <circle cx="150" cy="150" r="78" fill="#DBE7FE"/>
      <circle cx="150" cy="150" r="40" fill="#2563EB" opacity="0.18"/>
      <g transform="translate(150 140)">
        <path d="M0 -30a24 24 0 0 1 24 24c0 18-24 40-24 40S-24 12-24 -6A24 24 0 0 1 0 -30z" fill="#2563EB"/>
        <circle cx="0" cy="-6" r="9" fill="#fff"/>
      </g>
      <circle cx="80" cy="90" r="4" fill="#2563EB"/><circle cx="220" cy="110" r="4" fill="#2563EB"/>
      <circle cx="95" cy="215" r="4" fill="#2563EB"/><circle cx="215" cy="205" r="4" fill="#2563EB"/>
    </svg>'''

def loc_faqs(place, organic_only):
    base = [
        (f"Do you come to me in {place}?", f"Yes — we're a mobile call-out service and we travel to your home or workplace in {place}, by appointment. If you're just outside {place}, send your postcode and we'll confirm."),
        ("How long does a screen repair take?","Most standard screen replacements are completed on-site in around 45–60 minutes, depending on the device, fault and parts required."),
        (f"What repairs can you do in {place}?","Screen replacement is our main service, plus batteries, charging ports, cameras, speakers and diagnostics."),
        ("How do I get a quote?","Send a quote request or message us on WhatsApp with your phone model, the fault and your area, and we'll reply with a price."),
    ]
    return base

def build_area_hub():
    title = "Areas We Cover — Phone Repair Across South Wales | Call Out Phone Repairs"
    desc = "We come to you across South Wales: Pontypridd, Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly and Cardiff. Get a quote."
    path = "/areas/"
    crumbs = [("Home","/"),("Areas We Cover","/areas/")]
    schema = breadcrumb_ld(crumbs)
    cards = ""
    for slug,name,intro,nearby,_,_ in LOCATIONS:
        blurb = {"pontypridd":"Our home base — full coverage across the town and valleys.",
                 "treforest":"Next to base — USW campus and the industrial estate.",
                 "pontyclun":"On the M4 commuter belt.",
                 "tonypandy":"Rhondda commercial centre.",
                 "treherbert":"Upper Rhondda Fawr — further out, but covered.",
                 "aberdare":"Main town of the Cynon Valley.",
                 "merthyr-tydfil":"Large northern town — honest on timing.",
                 "caerphilly":"Commuter town in a different direction from the valleys.",
                 "cardiff":"North Cardiff first; building across the city."}[slug]
        cards += f'''<a class="card card-link reveal" href="/areas/{slug}/"><div class="card-icon">{IC['pin']}</div><h3>{name}</h3><p class="text-muted">{blurb}</p><span class="card-arrow">{name} {IC['arrow']}</span></a>'''
    body = f'''
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">Areas we cover</p>
        <h1>Phone repair across South Wales — we come to you</h1>
        <p class="lead">We're based in Pontypridd and travel to your home or workplace across the valleys and into Cardiff. Pick your area for local details, or just <a href="/get-a-quote/">get a quote</a>.</p>
      </div>
      <div class="grid grid-3">{cards}</div>
      <p class="text-muted center mt-6" style="max-width:60ch;margin-inline:auto">Not sure if you're in range? Message us your postcode and we'll confirm straight away. We're honest about how far we travel — if somewhere is a stretch, we'll tell you.</p>
    </div>
  </section>
  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>
  {inline_quote_section(head_title="Get a quote — wherever you are in South Wales")}
  {cta_band()}
'''
    page_shell(title, desc, path, "areas", schema, body, crumbs)

def build_pontypridd():
    """Flagship location page — full unique content."""
    place = "Pontypridd"
    path = "/areas/pontypridd/"
    title = "Phone Repair Pontypridd — We Come To You | Call Out Phone Repairs"
    desc = "Mobile phone repair in Pontypridd. Based right here, we come to your home or work to fix cracked screens, batteries and more. Most standard screen replacements take around 45–60 minutes. Get a quote."
    crumbs = [("Home","/"),("Areas We Cover","/areas/"),("Pontypridd","/areas/pontypridd/")]
    faqs = loc_faqs(place, False)
    schema = (breadcrumb_ld(crumbs) +
              ld({"@context":"https://schema.org","@type":"Service",
                  "serviceType":"Mobile phone repair","name":f"Phone repair in {place}",
                  "url":SITE+path,"provider":{"@id":SITE+"/#business"},
                  "areaServed":{"@type":"Place","name":place}}))
    body = f'''
  <section class="section">
    <div class="container">
      <div class="hero-grid" style="align-items:center">
        <div class="reveal">
          <p class="eyebrow">Phone repair · Pontypridd</p>
          <h1>Phone repair in Pontypridd — we come to you</h1>
          <p class="lead" style="margin:1rem 0 1.5rem">Pontypridd is our home base, so this is where we're fastest and most flexible. We come to your home or workplace anywhere in and around Ponty to replace screens at your home or work. Most standard screen replacements are normally completed in around 45–60 minutes, depending on the device, fault and parts required.</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="pontypridd">{IC['whatsapp']} WhatsApp us</a>
          </div>
        </div>
        <div class="hero-visual reveal">{coverage_svg("Pontypridd")}</div>
      </div>
    </div>
  </section>
  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>
  <section class="section">
    <div class="container container-narrow stack-lg">
      <div class="reveal">
        <h2>Your local phone repair service in Pontypridd</h2>
        <p class="mt-4">Being based in Pontypridd means we can usually reach you quickly and fit around your day. Whether you're near the town centre or a little further out in Pontypridd, just send your postcode when you get in touch and we'll confirm a time — no shop visit, no queue, no leaving your phone behind for days.</p>
      </div>
      <div class="reveal">
        <h2>What we repair in Pontypridd</h2>
        <div class="grid grid-2 mt-4">
          <a class="card card-link" href="/screen-repair/"><div class="card-icon">{IC['screen']}</div><h3 style="font-size:1.05rem">Screen repair</h3><p class="text-muted">Our main service. Most standard screen replacements take around 45–60 minutes.</p></a>
          <a class="card card-link" href="/repairs/battery-replacement/"><div class="card-icon">{IC['battery']}</div><h3 style="font-size:1.05rem">Battery replacement</h3><p class="text-muted">For phones that drain fast or shut down early.</p></a>
          <a class="card card-link" href="/repairs/charging-port-repair/"><div class="card-icon">{IC['port']}</div><h3 style="font-size:1.05rem">Charging port repair</h3><p class="text-muted">When charging gets loose or stops working.</p></a>
          <a class="card card-link" href="/repairs/phone-diagnostics/"><div class="card-icon">{IC['diagnostic']}</div><h3 style="font-size:1.05rem">Diagnostics</h3><p class="text-muted">Not sure what's wrong? We'll find out and explain.</p></a>
        </div>
      </div>
      <div class="reveal">
        <h2>How it works</h2>
        <p class="mt-4">Message us with your phone and the fault, we agree a time, and we come to you in Pontypridd. We confirm the expected repair time and agree everything before we start — nothing goes ahead without your say-so.</p>
        <p class="mt-4"><a href="/how-it-works/">See how our service works {IC['arrow']}</a> · <a href="/parts-and-repair-information/">Parts &amp; repair information {IC['arrow']}</a></p>
      </div>
      <div class="reveal">
        <h2>Nearby areas we also cover</h2>
        <p class="mt-4">From our Pontypridd base we also cover <a href="/areas/treforest/">Treforest</a>, <a href="/areas/pontyclun/">Pontyclun</a>, <a href="/areas/tonypandy/">Tonypandy</a> and <a href="/areas/aberdare/">Aberdare</a>, among our named areas. <a href="/areas/">See all areas {IC['arrow']}</a></p>
      </div>
    </div>
  </section>
  {inline_quote_section(head_title="Get a quote in Pontypridd")}
  <section class="section">
    <div class="container container-narrow">
      <div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>Pontypridd phone repair FAQs</h2></div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>
  {cta_band(heading="Cracked screen in Pontypridd? We'll come to you.")}
'''
    page_shell(title, desc, path, "areas", schema, body, crumbs, faq_plain=faqs)

def build_location(slug, name, intro, nearby, sections, organic_only):
    path = f"/areas/{slug}/"
    title = f"Phone Repair {name} — We Come To You | Call Out Phone Repairs"
    desc = f"Mobile phone repair in {name}. We come to you to fix cracked screens, batteries and more — most standard screens in around 45–60 minutes. Get a quote."
    crumbs = [("Home","/"),("Areas We Cover","/areas/"),(name,path)]
    faqs = loc_faqs(name, organic_only)
    schema = (breadcrumb_ld(crumbs) +
              ld({"@context":"https://schema.org","@type":"Service",
                  "serviceType":"Mobile phone repair","name":f"Phone repair in {name}",
                  "url":SITE+path,"provider":{"@id":SITE+"/#business"},
                  "areaServed":{"@type":"Place","name":name}}))
    extra = ""
    for h,p in sections:
        extra += f'<div class="reveal"><h2>{h}</h2><p class="mt-4">{p}</p></div>'
    body = f'''
  <section class="section">
    <div class="container">
      <div class="hero-grid" style="align-items:center">
        <div class="reveal">
          <p class="eyebrow">Phone repair · {name}</p>
          <h1>Phone repair in {name} — we come to you</h1>
          <p class="lead" style="margin:1rem 0 1.5rem">{intro}</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="{slug}">{IC['whatsapp']} WhatsApp us</a>
          </div>
        </div>
        <div class="hero-visual reveal">{coverage_svg(name)}</div>
      </div>
    </div>
  </section>
  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>
  <section class="section">
    <div class="container container-narrow stack-lg">
      {extra}
      <div class="reveal">
        <h2>What we repair in {name}</h2>
        <p class="mt-4">Screen replacement is our main service, plus <a href="/repairs/battery-replacement/">batteries</a>, <a href="/repairs/charging-port-repair/">charging ports</a>, <a href="/repairs/camera-replacement/">cameras</a>, <a href="/repairs/speaker-repair/">speakers</a> and <a href="/repairs/phone-diagnostics/">diagnostics</a>. We repair a range of <a href="/screen-repair/iphone/">iPhone</a> and <a href="/screen-repair/samsung/">Samsung</a> models.</p>
      </div>
      <div class="reveal">
        <h2>Not sure if we cover your exact spot?</h2>
        <p class="mt-4">We're based in Pontypridd and cover {name} as one of our named service areas. If you're nearby and not certain we can reach you, send us your postcode and we'll confirm. <a href="/areas/">See all the areas we cover {IC['arrow']}</a></p>
      </div>
    </div>
  </section>
  {inline_quote_section(head_title=f"Get a quote in {name}")}
  <section class="section">
    <div class="container container-narrow">
      <div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>{name} phone repair FAQs</h2></div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>
  {cta_band()}
'''
    page_shell(title, desc, path, "areas", schema, body, crumbs, faq_plain=faqs)

def build_all():
    build_area_hub()
    build_pontypridd()
    for slug,name,intro,nearby,sections,org in LOCATIONS:
        if slug == "pontypridd": continue
        build_location(slug,name,intro,nearby,sections,org)

if __name__ == "__main__":
    build_all()
