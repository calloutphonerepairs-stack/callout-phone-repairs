# -*- coding: utf-8 -*-
"""Technical audit: links, canonicals, H1 count, schema JSON validity, leaked markers, warranty check."""
import os, re, json, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BUILD = os.path.join(ROOT, "build")

html_files = []
for dirpath, dirs, files in os.walk(ROOT):
    if "/build" in dirpath or dirpath.endswith("build"): continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(dirpath, f))

def url_to_file(u):
    """Map a site path like /screen-repair/ to its index.html on disk."""
    u = u.split("#")[0].split("?")[0]
    if u.endswith("/"):
        return os.path.join(ROOT, u.strip("/"), "index.html")
    if u.endswith(".html"):
        return os.path.join(ROOT, u.strip("/"))
    # extension-less file? treat as dir
    return os.path.join(ROOT, u.strip("/"), "index.html")

issues = []
warnings = []
pages_checked = 0
all_internal_links = set()

for hf in html_files:
    rel = hf.replace(ROOT, "")
    with open(hf, encoding="utf-8") as f:
        html = f.read()
    pages_checked += 1

    # 1) single H1
    h1s = re.findall(r"<h1[ >]", html)
    if len(h1s) != 1:
        issues.append(f"{rel}: found {len(h1s)} <h1> (expected 1)")

    # 2) canonical present (except 404)
    if "404" not in rel:
        if 'rel="canonical"' not in html:
            issues.append(f"{rel}: missing canonical")
    else:
        if "noindex" not in html:
            issues.append(f"{rel}: 404 should be noindex")

    # 3) title + meta description
    if "<title>" not in html:
        issues.append(f"{rel}: missing <title>")
    if 'name="description"' not in html:
        issues.append(f"{rel}: missing meta description")

    # 4) JSON-LD validity
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(m)
        except Exception as e:
            issues.append(f"{rel}: invalid JSON-LD ({e})")

    # 5) leaked markers in VISIBLE text (DEV markers must be in HTML comments only)
    # find [CONFIRM] anywhere (should be zero)
    if "[CONFIRM]" in html:
        issues.append(f"{rel}: visible [CONFIRM] marker present")
    # DEV: markers must only appear inside comments
    for dm in re.finditer(r"DEV:", html):
        # find nearest comment bounds
        start = html.rfind("<!--", 0, dm.start())
        end = html.find("-->", dm.start())
        cstart = html.rfind("<!--", 0, dm.start())
        cend = html.find("-->", cstart) if cstart != -1 else -1
        inside = cstart != -1 and cend != -1 and cstart < dm.start() < cend
        if not inside:
            issues.append(f"{rel}: DEV marker outside HTML comment")

    # 6) warranty/guarantee leak (must not advertise)
    low = html.lower()
    for bad in ["warranty", "guarantee", "guaranteed"]:
        if bad in low:
            # allow only within privacy? no—flag all for manual review
            warnings.append(f"{rel}: contains '{bad}' — verify it is not an advertised claim")

    # 7) collect internal links
    for href in re.findall(r'href="(/[^"]*)"', html):
        if href.startswith("/assets/") or href.startswith("/#") or href.startswith("//"):
            continue
        all_internal_links.add(href)

# 8) resolve internal links to files
broken = []
for link in sorted(all_internal_links):
    if link in ("/robots.txt","/sitemap.xml"):
        continue
    target = url_to_file(link)
    if not os.path.exists(target):
        broken.append(link)

print("="*60)
print(f"AUDIT — {pages_checked} HTML pages checked")
print("="*60)
print(f"\nUnique internal links: {len(all_internal_links)}")
if broken:
    print(f"\n❌ BROKEN INTERNAL LINKS ({len(broken)}):")
    for b in broken: print("   ", b)
else:
    print("\n✅ No broken internal links")

if issues:
    print(f"\n❌ ISSUES ({len(issues)}):")
    for i in issues: print("   ", i)
else:
    print("\n✅ No structural issues (H1/canonical/title/meta/JSON-LD/markers)")

if warnings:
    print(f"\n⚠️  WARNINGS to eyeball ({len(warnings)}):")
    for w in warnings: print("   ", w)
else:
    print("\n✅ No warranty/guarantee wording found")

print("\nDone.")
