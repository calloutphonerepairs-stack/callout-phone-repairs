# -*- coding: utf-8 -*-
"""Reusable content components: quote assistant, CTA band, trust strip, FAQ."""
from partials import IC, WA, PHONE_LINK, PHONE_DISPLAY

def quote_assistant():
    """Progressive-enhancement quote assistant.
    Default HTML = usable plain form (works with NO JavaScript).
    When JS initialises, the stepped app-like flow is shown and the plain form
    is hidden and reused as the 'send my details' path. A <noscript> block also
    surfaces WhatsApp/Call immediately for no-JS users."""
    plain_form = f'''<form id="quote-form" class="q-detail-form" action="/quote" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="location_qualify" value="">
        <input type="hidden" name="source" value="quote-form">
        <!-- honeypot -->
        <div aria-hidden="true" style="position:absolute;left:-9999px"><label>Company<input type="text" name="company" tabindex="-1" autocomplete="off"></label></div>
        <div class="field">
          <label for="f-name">Your name <span class="req">*</span></label>
          <input class="input" id="f-name" name="name" type="text" autocomplete="name" required aria-required="true" aria-describedby="f-name-err">
          <p class="field-error" id="f-name-err" role="alert">Please enter your name.</p>
        </div>
        <div class="field">
          <label for="f-phone">Phone number <span class="req">*</span></label>
          <input class="input" id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" pattern="[0-9\\s+()-]{{6,}}" required aria-required="true" aria-describedby="f-phone-err">
          <p class="field-error" id="f-phone-err" role="alert">Please enter a valid phone number.</p>
        </div>
        <div class="field">
          <label for="f-repair">What needs fixing? <span class="req">*</span></label>
          <select class="select" id="f-repair" name="repair" required aria-required="true" aria-describedby="f-repair-err">
            <option value="" selected disabled>Choose a repair…</option>
            <option value="Screen replacement">Cracked / broken screen</option>
            <option value="Battery replacement">Battery</option>
            <option value="Charging port repair">Charging port</option>
            <option value="Camera repair">Camera</option>
            <option value="Speaker repair">Speaker / sound</option>
            <option value="Not sure — needs diagnosis">Not sure — needs diagnosis</option>
          </select>
          <p class="field-error" id="f-repair-err" role="alert">Please choose what needs fixing.</p>
        </div>
        <div class="field">
          <label for="f-brandmodel">Your phone (make &amp; model) <span class="text-muted" style="font-weight:400">(optional)</span></label>
          <input class="input" id="f-brandmodel" name="phone_model" type="text" placeholder="e.g. iPhone 13, Galaxy S22 — or 'not sure'">
        </div>
        <div class="field">
          <label for="f-town">Town or postcode <span class="req">*</span></label>
          <input class="input" id="f-town" name="town" type="text" autocomplete="postal-code" required aria-required="true" aria-describedby="f-town-err">
          <p class="field-error" id="f-town-err" role="alert">Please enter your town or postcode.</p>
        </div>
        <div class="field">
          <label for="f-email">Email <span class="text-muted" style="font-weight:400">(optional)</span></label>
          <input class="input" id="f-email" name="email" type="email" autocomplete="email">
        </div>
        <div class="field">
          <label>Preferred contact</label>
          <div class="segmented" role="radiogroup" aria-label="Preferred contact method">
            <label><input type="radio" name="contact_pref" value="WhatsApp" checked><span>{IC['whatsapp']} WhatsApp</span></label>
            <label><input type="radio" name="contact_pref" value="Call"><span>{IC['phone']} Call</span></label>
            <label><input type="radio" name="contact_pref" value="Email"><span>{IC['mail']} Email</span></label>
          </div>
        </div>
        <div class="field">
          <label for="f-desc">Anything else? <span class="text-muted" style="font-weight:400">(optional)</span></label>
          <textarea class="textarea" id="f-desc" name="description" placeholder="Tell us a bit about the fault…"></textarea>
        </div>
        <div class="field">
          <label class="consent">
            <input type="checkbox" name="consent" required aria-required="true" aria-describedby="f-consent-err">
            <span>I'm happy for Call Out Phone Repairs to contact me about my enquiry. See our <a href="/privacy-policy/">privacy policy</a>. <span class="req">*</span></span>
          </label>
          <p class="field-error" id="f-consent-err" role="alert">Please tick to continue.</p>
        </div>
        <button type="submit" class="btn btn-quote btn-lg btn-block">Send my enquiry {IC['arrow']}</button>
        <p class="hint center" style="margin-top:0.75rem">We reply during 08:00–20:00, Mon–Sun. No automatic prices — we'll quote you personally.</p>
      </form>'''

    return f'''<div id="quote-assistant" class="quote-assistant">
  <div class="quote-shell">
    <div class="quote-head">
      <h3>Get your quote</h3>
      <span class="pill js-only">{IC['sparkle']} 4 quick steps</span>
    </div>

    <!-- ============================================================
         NO-JS DEFAULT: a complete, usable enquiry form + WhatsApp/Call.
         This is what everyone gets before/without JavaScript.
         JS hides this wrapper and shows the stepped flow instead.
         ============================================================ -->
    <div id="q-plain" class="q-plain">
      <p class="q-steplabel">Send us your details</p>
      <h4 class="q-question">Tell us what's wrong and where you are</h4>
      <p class="text-muted" style="font-size:0.92rem;margin-bottom:1.25rem">Fill this in and we'll reply with a price and a time that suits you — or contact us directly below. We never book or charge anything without speaking to you first.</p>
      <div class="q-finish-paths" style="margin-bottom:1.5rem">
        <a class="btn btn-whatsapp btn-lg btn-block" href="{WA}" data-where="assistant-plain">{IC['whatsapp']} Message us on WhatsApp</a>
        <a class="btn btn-outline btn-block" href="{PHONE_LINK}" data-where="assistant-plain">{IC['phone']} Call {PHONE_DISPLAY}</a>
        <div class="q-finish-divider">or send your details</div>
      </div>
      {plain_form}
    </div>

    <!-- ============================================================
         JS-ONLY stepped experience. Hidden unless JS initialises.
         ============================================================ -->
    <div class="q-stepped js-only" hidden>
      <div class="q-progress" aria-hidden="true"></div>

      <!-- STEP 1: BRAND -->
      <div class="q-step active" data-step="0" role="group" aria-label="Step 1: choose your phone brand">
        <p class="q-steplabel">Step 1 of 4</p>
        <h4 class="q-question" tabindex="-1">What phone do you have?</h4>
        <div class="q-choices">
          <button type="button" class="q-choice" data-brand="iPhone"><span class="q-choice-ic">{IC['phone']}</span> iPhone</button>
          <button type="button" class="q-choice" data-brand="Samsung"><span class="q-choice-ic">{IC['phone']}</span> Samsung</button>
          <button type="button" class="q-choice" data-brand="Other"><span class="q-choice-ic">{IC['phone']}</span> Another brand</button>
          <button type="button" class="q-choice" data-brand="Other"><span class="q-choice-ic">{IC['diagnostic']}</span> Not sure</button>
        </div>
      </div>

      <!-- STEP 2: MODEL -->
      <div class="q-step" data-step="1" role="group" aria-label="Step 2: choose your model">
        <button type="button" class="q-back" data-back>{IC['back']} Back</button>
        <p class="q-steplabel">Step 2 of 4 &middot; <span id="q-model-brandlabel"></span></p>
        <h4 class="q-question" tabindex="-1">Which model?</h4>
        <div class="q-choices cols-1" id="q-models"></div>
      </div>

      <!-- STEP 3: REPAIR -->
      <div class="q-step" data-step="2" role="group" aria-label="Step 3: choose the repair">
        <button type="button" class="q-back" data-back>{IC['back']} Back</button>
        <p class="q-steplabel">Step 3 of 4</p>
        <h4 class="q-question" tabindex="-1">What needs fixing?</h4>
        <div class="q-choices">
          <button type="button" class="q-choice" data-repair="Screen replacement"><span class="q-choice-ic">{IC['screen']}</span> Cracked / broken screen</button>
          <button type="button" class="q-choice" data-repair="Battery replacement"><span class="q-choice-ic">{IC['battery']}</span> Battery</button>
          <button type="button" class="q-choice" data-repair="Charging port repair"><span class="q-choice-ic">{IC['port']}</span> Charging port</button>
          <button type="button" class="q-choice" data-repair="Camera repair"><span class="q-choice-ic">{IC['camera']}</span> Camera</button>
          <button type="button" class="q-choice" data-repair="Speaker repair"><span class="q-choice-ic">{IC['speaker']}</span> Speaker / sound</button>
          <button type="button" class="q-choice" data-repair="Not sure — needs diagnosis"><span class="q-choice-ic">{IC['diagnostic']}</span> Not sure</button>
        </div>
      </div>

      <!-- STEP 4: LOCATION -->
      <div class="q-step" data-step="3" role="group" aria-label="Step 4: your location">
        <button type="button" class="q-back" data-back>{IC['back']} Back</button>
        <p class="q-steplabel">Step 4 of 4</p>
        <h4 class="q-question" tabindex="-1">Where shall we come to?</h4>
        <div class="field">
          <label for="q-location">Town or postcode <span class="req" aria-hidden="true">*</span></label>
          <input class="input" type="text" id="q-location" name="location" autocomplete="postal-code" placeholder="e.g. Pontypridd or CF37" aria-describedby="q-location-error">
          <p class="field-error" id="q-location-error" role="alert"></p>
          <p class="hint">We come to you across South Wales. This helps us confirm we can reach you.</p>
        </div>
        <div class="q-nav">
          <button type="button" class="btn btn-quote btn-block" id="q-location-next">See my options {IC['arrow']}</button>
        </div>
      </div>

      <!-- STEP 5: FINISH (two paths) -->
      <div class="q-step" data-step="4" role="group" aria-label="Finish: contact us">
        <button type="button" class="q-back" data-back>{IC['back']} Back</button>
        <p class="q-steplabel">Almost done</p>
        <h4 class="q-question" tabindex="-1">Great — here's your enquiry</h4>
        <div class="q-summary" id="q-summary"></div>
        <p class="text-muted" style="font-size:0.9rem;margin-bottom:1.25rem">Send this to us and we'll reply with a price and a time that suits you. We'll never charge or book anything without speaking to you first.</p>

        <div class="q-finish-paths">
          <a class="btn btn-whatsapp btn-lg btn-block" id="q-wa" href="{WA}" data-where="assistant">{IC['whatsapp']} Send on WhatsApp</a>
          <a class="btn btn-outline btn-block" href="{PHONE_LINK}" data-where="assistant">{IC['phone']} Call {PHONE_DISPLAY}</a>
          <div class="q-finish-divider">or</div>
          <button type="button" class="btn btn-outline btn-block" id="q-show-form">{IC['mail']} Send my details instead</button>
        </div>
        <!-- The plain form (#quote-form) is MOVED here by JS as the 'send details' path. -->
        <div id="q-form-slot"></div>
      </div>

      <!-- SUCCESS -->
      <div class="q-step" data-step="success" id="q-success" role="status">
        <div class="q-result">
          <div class="q-result-icon ok">{IC['check']}</div>
          <h3 tabindex="-1">Thanks — we've got your enquiry</h3>
          <p>We'll be in touch during our hours (08:00–20:00, daily) with a price and a time that works for you. Nothing is booked until we've spoken.</p>
          <a class="btn btn-whatsapp btn-block" href="{WA}" data-where="success">{IC['whatsapp']} Message us now instead</a>
        </div>
      </div>

      <!-- ERROR -->
      <div class="q-step" data-step="error" id="q-error" role="alert">
        <div class="q-result">
          <div class="q-result-icon err">{IC['x-circle']}</div>
          <h3 tabindex="-1">That didn't send</h3>
          <p>Something went wrong on our side, and your details are still in the form below. Please message us on WhatsApp or give us a call — we'll sort it straight away.</p>
          <a class="btn btn-whatsapp btn-block" href="{WA}" data-where="error" style="margin-bottom:0.75rem">{IC['whatsapp']} Send on WhatsApp</a>
          <a class="btn btn-outline btn-block" href="{PHONE_LINK}" data-where="error">{IC['phone']} Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </div>
  </div>
</div>'''


def cta_band(heading="Cracked screen? Let's get it sorted.",
             text="Tell us your phone and the fault. We'll come to you across South Wales and most standard screen replacements are done in around 45–60 minutes."):
    return f'''<section class="section">
  <div class="container">
    <div class="cta-band reveal">
      <h2>{heading}</h2>
      <p>{text}</p>
      <div class="hero-actions">
        <a class="btn btn-quote btn-lg" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
        <a class="btn btn-whatsapp btn-lg" href="{WA}" data-where="ctaband">{IC['whatsapp']} WhatsApp us</a>
      </div>
    </div>
  </div>
</section>'''


def trust_strip_ink():
    items = [
        ("home", "We come to you"),
        ("clock", "Most standard screens ~45–60 min"),
        ("pin", "Across South Wales"),
        ("check", "Everything agreed before we start"),
    ]
    lis = "".join(f'<span class="trust-item">{IC[i]} {t}</span>' for i, t in items)
    return f'<div class="trust-strip">{lis}</div>'


def faq_block(items):
    """items: list of (question, answer_html)"""
    out = ['<div class="faq-list">']
    for q, a in items:
        out.append(f'''<details class="faq-item">
  <summary>{q}</summary>
  <div class="faq-body">{a}</div>
</details>''')
    out.append('</div>')
    return "\n".join(out)
