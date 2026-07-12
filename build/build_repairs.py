# -*- coding: utf-8 -*-
"""Repairs hub + individual repair service pages."""
from partials import IC, WA, PHONE_DISPLAY, PHONE_LINK
from components import quote_assistant, cta_band, trust_strip_ink, faq_block
from build import (breadcrumb_ld, service_ld, faqpage_ld)
from build_services import page_shell, inline_quote_section, device_svg

REPAIRS = [
    ("battery-replacement","Battery replacement","phone battery replacement",
     "Phone battery replacement","battery",
     "Is your phone dying by lunchtime, shutting down at 30%, or getting hot on charge? A worn battery is one of the most common phone faults — and one of the most satisfying to fix. We come to you and replace it so your phone holds a proper charge again.",
     [("How do I know if my battery needs replacing?","Common signs are fast draining, sudden shutdowns even with charge left, swelling, overheating, or your phone only working while plugged in."),
      ("Do you come to me to replace the battery?","Yes — we're mobile and travel to your home or workplace across South Wales, by appointment."),
      ("How long does a battery replacement take?","Many battery replacements are completed on-site in under an hour, depending on the model. We confirm the expected time before we start."),
      ("How are parts and details decided?","The part options and details are discussed and agreed with you before any work begins.")]),
    ("charging-port-repair","Charging port repair","phone charging port repair",
     "Phone charging port repair","port",
     "Having to wiggle the cable to get it to charge? Charging only at a certain angle, or not at all? It's often the charging port — blocked, worn or damaged. We come to you, diagnose it, and repair it where possible.",
     [("Why won't my phone charge properly?","It can be a worn or damaged charging port, lint or debris packed into the port, a faulty cable, or sometimes the battery. We'll diagnose which it is."),
      ("Can a charging port be cleaned rather than replaced?","Sometimes, yes — a blocked port can just need careful cleaning. If it's damaged or worn, it may need replacing. We'll tell you honestly which it is."),
      ("Do you come to me?","Yes, we're a mobile call-out service across South Wales, by appointment."),
      ("How do I get a quote?","Message us on WhatsApp or send a quote request with your phone model and what's happening when you try to charge.")]),
    ("camera-replacement","Camera replacement","phone camera repair",
     "Phone camera repair & replacement","camera",
     "Cracked camera lens, blurry or foggy photos, black camera screen, or a lens that won't focus? We come to you and repair or replace the camera so you can capture things clearly again.",
     [("What camera problems can you fix?","Cracked lens glass, blurry or unfocused photos, a black camera screen, spots or haze, and front or rear camera faults."),
      ("Do you repair both front and rear cameras?","Yes — tell us which camera and what's happening and we'll confirm what's involved."),
      ("Do you come to me?","Yes, we travel to you across South Wales by appointment."),
      ("How are parts decided?","Part options and details are discussed and agreed with you before any work begins.")]),
    ("speaker-repair","Speaker repair","phone speaker repair",
     "Phone speaker & sound repair","speaker",
     "Can't hear callers, sound is muffled or crackly, or the phone's gone silent? Whether it's the earpiece, the loudspeaker or the microphone, we come to you to diagnose and repair the sound fault where possible.",
     [("What sound problems can you fix?","Muffled or crackly audio, no sound from the loudspeaker or earpiece, people not being able to hear you, and distorted volume."),
      ("Could it be something other than the speaker?","Sometimes — blocked speaker grilles, software, or a microphone fault can sound similar. We'll diagnose the real cause first."),
      ("Do you come to me?","Yes — mobile call-out across South Wales, by appointment."),
      ("How do I get a quote?","Send a quote request or WhatsApp us with your model and what you're hearing (or not hearing).")]),
    ("phone-diagnostics","Phone diagnostics","phone diagnostics",
     "Phone diagnostics — not sure what's wrong?","diagnostic",
     "Phone acting up and you can't work out why? You don't need to know the exact fault to get in touch. We come to you, take a proper look, tell you what's going on and explain your options — before anything goes ahead.",
     [("What if I don't know what's wrong with my phone?","That's completely fine. Describe what it's doing and we'll come and diagnose it. We explain what we find and your options before any work begins."),
      ("Do you charge to diagnose a phone?","Get in touch and we'll be upfront about how we handle diagnostics for your situation before we come out — no surprises."),
      ("Do you come to me?","Yes, we're mobile across South Wales, by appointment."),
      ("What happens after diagnosis?","We explain the fault and your options and agree everything with you before starting. Nothing goes ahead without your say-so.")]),
]

def build_repairs_hub():
    title = "Phone Repairs — We Come To You | Call Out Phone Repairs, South Wales"
    desc = "Mobile phone repairs across Pontypridd & South Wales: screens, batteries, charging ports, cameras, speakers and diagnostics. We come to you. Get a quote."
    path = "/repairs/"
    crumbs = [("Home","/"),("Repairs","/repairs/")]
    schema = breadcrumb_ld(crumbs)
    cards = ""
    icon_map = {"battery-replacement":"battery","charging-port-repair":"port","camera-replacement":"camera","speaker-repair":"speaker","phone-diagnostics":"diagnostic"}
    # Screen first (featured), then the rest
    cards += f'''<a class="card card-link card-featured reveal" href="/screen-repair/"><div class="card-icon">{IC['screen']}</div><h3>Screen repair</h3><p class="text-muted">Our main service — cracked and broken screens replaced at your home or workplace. Most standard screen replacements take around 45–60 minutes.</p><span class="card-arrow">Screen repair {IC['arrow']}</span></a>'''
    for slug,name,_,_,icon,_,_ in REPAIRS:
        cards += f'''<a class="card card-link reveal" href="/repairs/{slug}/"><div class="card-icon">{IC[icon]}</div><h3>{name}</h3><p class="text-muted">{ {
            "battery-replacement":"Fast draining or sudden shutdowns? A replacement battery can restore normal running.",
            "charging-port-repair":"Loose connection or won't charge? Often the port.",
            "camera-replacement":"Cracked lens or blurry photos sorted.",
            "speaker-repair":"Muffled, crackly or silent sound put right.",
            "phone-diagnostics":"Not sure what's wrong? We'll find out and explain."}[slug] }</p><span class="card-arrow">Learn more {IC['arrow']}</span></a>'''
    body = f'''
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <p class="eyebrow">Phone repairs</p>
        <h1>Phone repairs — we come to you</h1>
        <p class="lead">Whatever's wrong with your phone, we travel to your home or workplace across South Wales to fix it. Screens are what we do most, but we handle plenty more.</p>
      </div>
      <div class="grid grid-3">{cards}</div>
    </div>
  </section>
  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>
  {inline_quote_section(head_title="Tell us what's wrong — get a quote")}
  {cta_band()}
'''
    page_shell(title, desc, path, "", schema, body, crumbs)

def build_repair_page(slug, name, kw, h1, icon, intro, faqs):
    title = f"{h1.split('—')[0].strip()} — We Come To You | South Wales"
    desc = f"{intro[:150]}"
    path = f"/repairs/{slug}/"
    crumbs = [("Home","/"),("Repairs","/repairs/"),(name,path)]
    schema = breadcrumb_ld(crumbs) + service_ld(name, intro, path)
    body = f'''
  <section class="section">
    <div class="container">
      <div class="hero-grid" style="align-items:center">
        <div class="reveal">
          <p class="eyebrow">{name}</p>
          <h1>{h1}</h1>
          <p class="lead" style="margin:1rem 0 1.5rem">{intro}</p>
          <div class="hero-actions">
            <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
            <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="{slug}">{IC['whatsapp']} WhatsApp us</a>
          </div>
        </div>
        <div class="hero-visual reveal"><div class="card-icon" style="width:120px;height:120px;border-radius:30px">{IC[icon]}</div></div>
      </div>
    </div>
  </section>
  <section class="section-tight on-ink" style="padding-block:1.5rem"><div class="container">{trust_strip_ink()}</div></section>
  <section class="section">
    <div class="container container-narrow stack-lg">
      <div class="reveal">
        <h2>How it works</h2>
        <p class="mt-4">You don't visit a shop. We agree a time, come to your home or workplace, and carry out the repair there where possible. We always explain what's involved and agree it with you before starting.</p>
        <p class="mt-4"><a href="/how-it-works/">See how our mobile service works {IC['arrow']}</a></p>
      </div>
      <div class="reveal">
        <h2>Parts &amp; repair information</h2>
        <p class="mt-4">The exact part options, availability and details for your repair are discussed and agreed with you before any work begins. <a href="/parts-and-repair-information/">Read more {IC['arrow']}</a></p>
      </div>
      <div class="reveal">
        <h2>Areas we cover</h2>
        <p class="mt-4">Based in Pontypridd, we cover Treforest, Pontyclun, Tonypandy, Treherbert, Aberdare, Merthyr Tydfil, Caerphilly and Cardiff. <a href="/areas/">All areas {IC['arrow']}</a></p>
      </div>
    </div>
  </section>
  {inline_quote_section(head_title=f"Get a quote for {name.lower()}")}
  <section class="section">
    <div class="container container-narrow">
      <div class="section-head center reveal"><p class="eyebrow">Common questions</p><h2>{name} FAQs</h2></div>
      <div class="reveal">{faq_block(faqs)}</div>
    </div>
  </section>
  {cta_band()}
'''
    page_shell(title, desc, path, "", schema, body, crumbs, faq_plain=faqs)

def build_all():
    build_repairs_hub()
    for r in REPAIRS:
        build_repair_page(*r)

if __name__ == "__main__":
    build_all()
