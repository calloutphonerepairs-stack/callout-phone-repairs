# -*- coding: utf-8 -*-
"""Shared partials for Call Out Phone Repairs static site.
Generates consistent <head>, header, footer, floating WhatsApp, mobile bar.
Run build.py to emit final HTML into the site root."""

SITE = "https://calloutphonerepairs.co.uk"
BRAND = "Call Out Phone Repairs"
TAG = "We Come To You"
PHONE_DISPLAY = "07347 715961"
PHONE_LINK = "tel:+447347715961"
WA = "https://wa.me/447347715961"
EMAIL = "calloutphonerepairs@gmail.com"

# ---- SVG icons (inline, tiny) ----
IC = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.77-1.66-2.07-.17-.3-.02-.46.13-.61.13-.13.3-.35.44-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47 0 1.46 1.06 2.87 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.62.71.23 1.36.2 1.87.12.57-.08 1.77-.72 2.02-1.42.25-.7.25-1.29.17-1.42-.07-.13-.27-.2-.57-.35zM12 2a10 10 0 0 0-8.6 15.06L2 22l5.06-1.33A10 10 0 1 0 12 2z"/></svg>',
    "quote": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="14" x2="15" y2="14"/><line x1="9" y1="17" x2="13" y2="17"/></svg>',
    "screen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M9 7l2.5 3L9 13m4 0l2-2"/></svg>',
    "battery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="16" height="10" rx="2"/><line x1="22" y1="11" x2="22" y2="13"/><path d="M9 9l-1.5 3H10l-1.5 3"/></svg>',
    "port": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3v4M15 3v4M7 7h10v4a5 5 0 0 1-10 0z"/><line x1="12" y1="16" x2="12" y2="21"/></svg>',
    "camera": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
    "speaker": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.5 8.5a5 5 0 0 1 0 7M19 5a9 9 0 0 1 0 14"/></svg>',
    "diagnostic": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l2 5 4-10 2 5h6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.5 8.5 8 11 4.5-2.5 8-6 8-11V5z"/><polyline points="9 12 11 14 15 10"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "back": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>',
    "sparkle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
    "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>',
    "x-circle": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>',
    "photo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>',
}

def head(title, description, canonical_path, extra_css="", schema="", og_type="website",
         og_image="/assets/img/og-cover.png", og_image_alt=None):
    canonical = SITE + canonical_path
    if og_image_alt is None:
        og_image_alt = "Call Out Phone Repairs — mobile phone repair across South Wales. We come to you."
    og_image_url = SITE + og_image
    css_links = '<link rel="stylesheet" href="/assets/css/main.css">'
    if extra_css:
        css_links += extra_css
    return f'''<!DOCTYPE html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<script>document.documentElement.className=document.documentElement.className.replace('no-js','js');</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{og_image_url}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_image_alt}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og_image_url}">
<meta name="twitter:image:alt" content="{og_image_alt}">
<meta name="theme-color" content="#F8FAFC">
<link rel="icon" href="/assets/img/logo-mark.svg" type="image/svg+xml">
<link rel="preload" href="/assets/fonts/spacegrotesk-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>
{css_links}
{schema}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''

def header(active=""):
    def cur(name):
        return ' aria-current="page"' if active == name else ''
    return f'''<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/">
      <img class="brand-mark" src="/assets/img/logo-mark.svg" alt="" width="38" height="38">
      <span class="brand-text">
        <span class="brand-name">{BRAND}</span>
        <span class="brand-tag">{TAG}</span>
      </span>
    </a>
    <nav class="nav-desktop" aria-label="Primary">
      <ul>
        <li class="nav-item has-submenu">
          <a class="nav-link" href="/screen-repair/"{cur('screen')}>Screen Repair</a>
          <ul class="submenu">
            <li><a class="sub-featured" href="/screen-repair/">All screen repairs</a></li>
            <li><a href="/screen-repair/iphone/">iPhone screen repair</a></li>
            <li><a href="/screen-repair/samsung/">Samsung screen repair</a></li>
          </ul>
        </li>
        <li class="nav-item has-submenu">
          <a class="nav-link" href="/repairs/">Repairs</a>
          <ul class="submenu">
            <li><a href="/repairs/battery-replacement/">Battery replacement</a></li>
            <li><a href="/repairs/charging-port-repair/">Charging port repair</a></li>
            <li><a href="/repairs/camera-replacement/">Camera replacement</a></li>
            <li><a href="/repairs/speaker-repair/">Speaker repair</a></li>
            <li><a href="/repairs/phone-diagnostics/">Phone diagnostics</a></li>
          </ul>
        </li>
        <li class="nav-item has-submenu">
          <a class="nav-link" href="/areas/"{cur('areas')}>Areas We Cover</a>
          <ul class="submenu">
            <li><a class="sub-featured" href="/areas/">All areas</a></li>
            <li><a href="/areas/pontypridd/">Pontypridd</a></li>
            <li><a href="/areas/treforest/">Treforest</a></li>
            <li><a href="/areas/pontyclun/">Pontyclun</a></li>
            <li><a href="/areas/tonypandy/">Tonypandy</a></li>
            <li><a href="/areas/treherbert/">Treherbert</a></li>
            <li><a href="/areas/aberdare/">Aberdare</a></li>
            <li><a href="/areas/merthyr-tydfil/">Merthyr Tydfil</a></li>
            <li><a href="/areas/caerphilly/">Caerphilly</a></li>
            <li><a href="/areas/cardiff/">Cardiff</a></li>
          </ul>
        </li>
        <li class="nav-item"><a class="nav-link" href="/how-it-works/"{cur('how')}>How It Works</a></li>
        <li class="nav-item"><a class="nav-link" href="/about/"{cur('about')}>About</a></li>
        <li class="nav-item"><a class="nav-link" href="/reviews/"{cur('reviews')}>Reviews</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn-quote header-quote" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
        <span class="icon-open">{IC['menu']}</span>
        <span class="icon-close">{IC['close']}</span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu">
  <ul>
    <li>
      <span class="mobile-group-label">Screen Repair</span>
      <ul class="mobile-sublist">
        <li><a href="/screen-repair/">All screen repairs</a></li>
        <li><a href="/screen-repair/iphone/">iPhone screen repair</a></li>
        <li><a href="/screen-repair/samsung/">Samsung screen repair</a></li>
      </ul>
    </li>
    <li>
      <span class="mobile-group-label">Repairs</span>
      <ul class="mobile-sublist">
        <li><a href="/repairs/battery-replacement/">Battery replacement</a></li>
        <li><a href="/repairs/charging-port-repair/">Charging port repair</a></li>
        <li><a href="/repairs/camera-replacement/">Camera replacement</a></li>
        <li><a href="/repairs/speaker-repair/">Speaker repair</a></li>
        <li><a href="/repairs/phone-diagnostics/">Phone diagnostics</a></li>
      </ul>
    </li>
    <li>
      <span class="mobile-group-label">Areas We Cover</span>
      <ul class="mobile-sublist">
        <li><a href="/areas/">All areas</a></li>
        <li><a href="/areas/pontypridd/">Pontypridd</a></li>
        <li><a href="/areas/treforest/">Treforest</a></li>
        <li><a href="/areas/pontyclun/">Pontyclun</a></li>
        <li><a href="/areas/tonypandy/">Tonypandy</a></li>
        <li><a href="/areas/treherbert/">Treherbert</a></li>
        <li><a href="/areas/aberdare/">Aberdare</a></li>
        <li><a href="/areas/merthyr-tydfil/">Merthyr Tydfil</a></li>
        <li><a href="/areas/caerphilly/">Caerphilly</a></li>
        <li><a href="/areas/cardiff/">Cardiff</a></li>
      </ul>
    </li>
    <li><a href="/how-it-works/">How It Works</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="/reviews/">Reviews</a></li>
    <li><a href="/contact/">Contact</a></li>
  </ul>
  <div class="mobile-cta">
    <a class="btn btn-quote btn-block" href="/get-a-quote/">{IC['quote']} Get a Quote</a>
    <a class="btn btn-whatsapp btn-block" href="{WA}" data-where="mobilemenu">{IC['whatsapp']} WhatsApp us</a>
    <a class="btn btn-outline btn-block" href="{PHONE_LINK}" data-where="mobilemenu">{IC['phone']} Call {PHONE_DISPLAY}</a>
  </div>
</div>
'''

def floating_and_bar():
    return f'''<a class="wa-float" href="{WA}" data-where="float" aria-label="Contact us on WhatsApp">{IC['whatsapp']}</a>
<nav class="mobile-bar" aria-label="Quick contact">
  <a class="mb-call" href="{PHONE_LINK}" data-where="mobilebar">{IC['phone']}<span>Call</span></a>
  <a class="mb-wa" href="{WA}" data-where="mobilebar">{IC['whatsapp']}<span>WhatsApp</span></a>
  <a class="mb-quote" href="/get-a-quote/">{IC['quote']}<span>Get a Quote</span></a>
</nav>
'''

def footer():
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="/" style="margin-bottom:1rem">
          <img class="brand-mark" src="/assets/img/logo-mark.svg" alt="" width="38" height="38">
          <span class="brand-text"><span class="brand-name">{BRAND}</span><span class="brand-tag">{TAG}</span></span>
        </a>
        <p style="max-width:34ch;color:#A9BAD4;font-size:0.94rem">Mobile phone repair across South Wales. We travel to you at home or work — most standard screen replacements are done on-site in around 45–60 minutes.</p>
        <p class="footer-note">Mobile call-out service by appointment. We do not operate a walk-in shop.</p>
      </div>
      <div class="footer-col">
        <h4>Screen Repair</h4>
        <ul>
          <li><a href="/screen-repair/">Phone screen repair</a></li>
          <li><a href="/screen-repair/iphone/">iPhone screen repair</a></li>
          <li><a href="/screen-repair/samsung/">Samsung screen repair</a></li>
          <li><a href="/repairs/battery-replacement/">Battery replacement</a></li>
          <li><a href="/repairs/charging-port-repair/">Charging port repair</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Areas We Cover</h4>
        <ul>
          <li><a href="/areas/pontypridd/">Pontypridd</a></li>
          <li><a href="/areas/treforest/">Treforest</a></li>
          <li><a href="/areas/pontyclun/">Pontyclun</a></li>
          <li><a href="/areas/aberdare/">Aberdare</a></li>
          <li><a href="/areas/caerphilly/">Caerphilly</a></li>
          <li><a href="/areas/cardiff/">Cardiff</a></li>
          <li><a href="/areas/">All areas &rarr;</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <div class="footer-contact-item">{IC['phone']}<span><a href="{PHONE_LINK}">{PHONE_DISPLAY}</a></span></div>
        <div class="footer-contact-item">{IC['whatsapp']}<span><a href="{WA}" data-where="footer">WhatsApp us</a></span></div>
        <div class="footer-contact-item">{IC['mail']}<span><a href="mailto:{EMAIL}">Email us</a></span></div>
        <div class="footer-contact-item">{IC['clock']}<span>Mon–Sun, 08:00–20:00<br><span style="color:#7C8CA8;font-size:0.85rem">Submit a quote request any time</span></span></div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; {{YEAR}} {BRAND}. All rights reserved.</span>
      <span><a href="/how-it-works/">How it works</a> &middot; <a href="/parts-and-repair-information/">Parts &amp; repair info</a> &middot; <a href="/contact/">Contact</a> &middot; <a href="/privacy-policy/">Privacy</a></span>
    </div>
  </div>
</footer>
'''

def scripts(extra=""):
    return f'''<script src="/assets/js/main.js" defer></script>{extra}
</body>
</html>'''
