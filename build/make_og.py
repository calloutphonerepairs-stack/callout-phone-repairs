# -*- coding: utf-8 -*-
"""Generate the 1200x630 social-sharing image.
Safe two-column layout: text confined to left ~62%, phone to right ~26%, no overlap.
Light/blue brand system. Run to regenerate assets/img/og-cover.png (+ .webp)."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ---- Layout guides ----
PAD = 72                      # generous safe padding
TEXT_LEFT = PAD               # text column starts
TEXT_RIGHT = int(W * 0.62)    # text confined to left ~62%
PHONE_ZONE_L = int(W * 0.70)  # phone lives in right ~26% (0.70 -> 0.96)
PHONE_ZONE_R = W - PAD

BG = "#F8FAFC"; INK = "#0F172A"; SUB = "#475569"; BLUE = "#2563EB"
CARD_TINT = "#E7EEFB"; STRUCT = "#E2E8F0"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def font(sz, bold=True):
    p = ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
         else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    try: return ImageFont.truetype(p, sz)
    except Exception: return ImageFont.load_default()

# top accent bar
d.rectangle([0, 0, W, 8], fill=BLUE)

# soft decorative blob confined to the phone zone (never under text)
d.ellipse([PHONE_ZONE_L-40, 40, PHONE_ZONE_R+90, 40+380], fill=CARD_TINT)

# ---- Left column: text (all within TEXT_LEFT..TEXT_RIGHT) ----
y = 150
d.text((TEXT_LEFT, y), "MOBILE PHONE REPAIR", font=font(26, True), fill=BLUE)
y += 54
d.text((TEXT_LEFT, y), "Broken phone", font=font(66, True), fill=INK)
y += 74
d.text((TEXT_LEFT, y), "screen?", font=font(66, True), fill=INK)
y += 78
d.text((TEXT_LEFT, y), "We come to you.", font=font(66, True), fill=BLUE)
y += 96
d.text((TEXT_LEFT, y), "Mobile phone repair across", font=font(30, False), fill=SUB)
y += 40
d.text((TEXT_LEFT, y), "Pontypridd and South Wales.", font=font(30, False), fill=SUB)
y += 72
d.text((TEXT_LEFT, y), "Call Out Phone Repairs", font=font(34, True), fill=INK)

# ---- Right column: phone illustration (within PHONE_ZONE) ----
cx = (PHONE_ZONE_L + PHONE_ZONE_R) // 2
pw, ph = 150, 300
px = cx - pw // 2
py = (H - ph) // 2 + 6
# shadow
d.ellipse([px-6, py+ph-6, px+pw+6, py+ph+26], fill=STRUCT)
# body
d.rounded_rectangle([px, py, px+pw, py+ph], radius=30, fill=INK)
# screen
d.rounded_rectangle([px+13, py+20, px+pw-13, py+ph-20], radius=18, fill=BLUE)
# restored check (white)
cxp = px + pw//2
cyp = py + ph//2
d.line([(cxp-30, cyp), (cxp-6, cyp+26)], fill="#FFFFFF", width=13, joint="curve")
d.line([(cxp-6, cyp+26), (cxp+34, cyp-22)], fill="#FFFFFF", width=13, joint="curve")

out_png = os.path.join(ROOT, "assets/img/og-cover.png")
out_webp = os.path.join(ROOT, "assets/img/og-cover.webp")
img.save(out_png, "PNG", optimize=True)
img.save(out_webp, "WEBP", quality=90, method=6)
print("wrote", out_png, os.path.getsize(out_png), "bytes")
print("wrote", out_webp, os.path.getsize(out_webp), "bytes")
print("text column right edge:", TEXT_RIGHT, "| phone zone left:", PHONE_ZONE_L, "| gap:", PHONE_ZONE_L - TEXT_RIGHT, "px")
