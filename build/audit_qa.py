# -*- coding: utf-8 -*-
"""Extended QA audit for the correction pass (issues #3,#4,#6,#7,#8,#10,#14)."""
import os, re, glob, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
html_files = []
for dp, dirs, files in os.walk(ROOT):
    if "/build" in dp or dp.endswith("build"): continue
    for f in files:
        if f.endswith(".html"): html_files.append(os.path.join(dp,f))

def body_text(html):
    # crude visible-text extraction: strip scripts/styles/comments/tags
    h = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", h)

problems = {}
def flag(cat, msg):
    problems.setdefault(cat, []).append(msg)

# Phrases that must NOT appear as unqualified claims (#3, #4, #14)
BANNED = [
    "most iphone models", "most samsung", "most android", "most phones",
    "popular android phones", "most cracked screens", "most screens in",
    "genuine part", "oem", "premium parts", "high-quality parts",
    "certified", "years of experience", "same-day", "24/7", "24 hour", "24-hour",
    "free quote", "warranty", "guarantee", "guaranteed",
]
# timing must always be qualified — flag "45" mentions lacking 'standard'
for hf in html_files:
    rel = hf.replace(ROOT,"")
    html = open(hf, encoding="utf-8").read()
    txt = body_text(html).lower()

    for b in BANNED:
        if b in txt:
            # allow 'guarantee' nowhere; report context
            idx = txt.find(b)
            flag("banned_phrase", f"{rel}: '{b}' → …{txt[max(0,idx-30):idx+40]}…")

    # timing qualification: every '45–60' should sit near 'standard screen'
    for m in re.finditer(r"45[–-]60", txt):
        window = txt[max(0,m.start()-140):m.end()+40]
        if "standard" not in window:
            flag("timing_unqualified", f"{rel}: 45–60 without 'standard' nearby → …{window}…")

    # OG image present (#8)
    if "404" not in rel:
        if 'property="og:image"' not in html:
            flag("og_image", f"{rel}: missing og:image")
        if 'name="twitter:image"' not in html:
            flag("og_image", f"{rel}: missing twitter:image")

    # No Google Fonts (#10)
    if "fonts.googleapis.com" in html or "fonts.gstatic.com" in html:
        flag("google_fonts", f"{rel}: still references Google Fonts")

    # priceRange removed (#6)
    if '"priceRange"' in html:
        flag("pricerange", f"{rel}: priceRange still in schema")

    # FAQ schema vs visible parity (#7): every FAQPage question name must appear in visible text
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(m.group(1))
        except: continue
        blocks = data if isinstance(data, list) else [data]
        for blk in blocks:
            if isinstance(blk, dict) and blk.get("@type") == "FAQPage":
                for qa in blk.get("mainEntity", []):
                    q = qa.get("name","")
                    a = qa.get("acceptedAnswer",{}).get("text","")
                    # normalise apostrophes
                    vt = body_text(html)
                    if q and q.replace("&amp;","&") not in vt.replace("&amp;","&"):
                        flag("faq_parity", f"{rel}: FAQ question not in visible text: {q[:50]}")
                    # answer parity (first 40 chars)
                    if a and a[:40] not in vt:
                        flag("faq_parity", f"{rel}: FAQ answer not matching visible: {a[:45]}")

print("="*60); print("EXTENDED QA AUDIT"); print("="*60)
if not problems:
    print("\n✅ All extended checks passed")
else:
    for cat, items in problems.items():
        print(f"\n❌ {cat} ({len(items)}):")
        for it in items[:12]:
            print("   ", it)
        if len(items) > 12: print(f"    …and {len(items)-12} more")
