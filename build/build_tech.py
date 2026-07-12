# -*- coding: utf-8 -*-
"""Technical files: robots.txt, sitemap.xml, _redirects, _headers."""
import os, datetime
from build import write, SITE

TODAY = datetime.date.today().isoformat()

# All indexable canonical URLs (with trailing slashes for directories)
PAGES = [
    ("/", "1.0"),
    ("/screen-repair/", "0.9"),
    ("/screen-repair/iphone/", "0.9"),
    ("/screen-repair/samsung/", "0.9"),
    ("/repairs/", "0.7"),
    ("/repairs/battery-replacement/", "0.7"),
    ("/repairs/charging-port-repair/", "0.7"),
    ("/repairs/camera-replacement/", "0.7"),
    ("/repairs/speaker-repair/", "0.7"),
    ("/repairs/phone-diagnostics/", "0.7"),
    ("/areas/", "0.8"),
    ("/areas/pontypridd/", "0.9"),
    ("/areas/treforest/", "0.8"),
    ("/areas/pontyclun/", "0.8"),
    ("/areas/tonypandy/", "0.8"),
    ("/areas/treherbert/", "0.8"),
    ("/areas/aberdare/", "0.8"),
    ("/areas/merthyr-tydfil/", "0.8"),
    ("/areas/caerphilly/", "0.8"),
    ("/areas/cardiff/", "0.8"),
    ("/how-it-works/", "0.6"),
    ("/parts-and-repair-information/", "0.5"),
    ("/about/", "0.6"),
    ("/reviews/", "0.6"),
    ("/contact/", "0.7"),
    ("/get-a-quote/", "0.9"),
    ("/privacy-policy/", "0.2"),
]

def build_robots():
    txt = f"""User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
"""
    write("robots.txt", txt)

def build_sitemap():
    urls = ""
    for path, pri in PAGES:
        urls += f"""  <url>
    <loc>{SITE}{path}</loc>
    <lastmod>{TODAY}</lastmod>
    <priority>{pri}</priority>
  </url>
"""
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>
"""
    write("sitemap.xml", xml)

def build_redirects():
    # Cloudflare Pages _redirects — canonical host enforcement + trailing-slash safety.
    # Note: HTTPS is enforced by Cloudflare automatically. www->apex handled here.
    txt = """# Canonical host: non-www apex. Single-hop redirects, preserve path + query.
https://www.calloutphonerepairs.co.uk/* https://calloutphonerepairs.co.uk/:splat 301!

# Cloudflare Pages preview domain -> canonical (avoid duplicate indexing)
https://:project.pages.dev/* https://calloutphonerepairs.co.uk/:splat 301!
"""
    write("_redirects", txt)

def build_headers():
    # Compute the CSP hash for the single inline bootstrap script (the no-js→js
    # class switch in <head>) so we can use a strict CSP WITHOUT 'unsafe-inline'.
    import hashlib, base64
    inline_js = "document.documentElement.className=document.documentElement.className.replace('no-js','js');"
    inline_hash = "sha256-" + base64.b64encode(hashlib.sha256(inline_js.encode()).digest()).decode()

    # Content-Security-Policy notes:
    #   - default-src 'self'         : first-party only
    #   - script-src 'self' + hash   : our external JS + the one inline bootstrap (no 'unsafe-inline')
    #   - style-src 'self' 'unsafe-inline' : a few small inline style="" attributes are used in markup;
    #       inline styles are far lower-risk than inline scripts. (Could be hashed later if desired.)
    #   - img/font 'self' data:      : all first-party; data: allows the tiny inline SVG favicon if needed
    #   - connect-src 'self'         : the quote form posts to our own /quote function
    #   - frame-ancestors 'none'     : clickjacking protection
    csp = ("default-src 'self'; "
           "base-uri 'self'; "
           f"script-src 'self' '{inline_hash}'; "
           "style-src 'self' 'unsafe-inline'; "
           "img-src 'self' data:; "
           "font-src 'self'; "
           "connect-src 'self'; "
           "form-action 'self'; "
           "frame-ancestors 'none'; "
           "object-src 'none'")

    txt = f"""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
  Content-Security-Policy: {csp}

/assets/css/*
  Cache-Control: public, max-age=3600, must-revalidate

/assets/js/*
  Cache-Control: public, max-age=3600, must-revalidate

/assets/img/*
  Cache-Control: public, max-age=86400, must-revalidate

/assets/fonts/*
  Cache-Control: public, max-age=31536000, immutable
  Access-Control-Allow-Origin: *

/*.html
  Cache-Control: public, max-age=0, must-revalidate
"""
    write("_headers", txt)

if __name__ == "__main__":
    build_robots()
    build_sitemap()
    build_redirects()
    build_headers()
    print("Technical files built.")
