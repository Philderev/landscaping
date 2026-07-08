"""Regenerate hero poster + og image from the real hero video frames."""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

SP = os.path.dirname(os.path.abspath(__file__))
ROOT = r"E:\templates\landscaping website template"
PINE = (27, 46, 36)
CLAY = (196, 98, 45)
SAGE = (138, 155, 110)
CREAM = (251, 247, 239)
GOLD = (217, 164, 91)

FRAME = sys.argv[1] if len(sys.argv) > 1 else "poster-4s.png"


def draw_mark(size):
    ss = 4
    s = size * ss
    u = s / 64
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([(38 - 14) * u, (22 - 14) * u, (38 + 14) * u, (22 + 14) * u], fill=CLAY)
    d.arc([8 * u, 12 * u, 30 * u, 32 * u], start=180, end=300, fill=SAGE, width=int(2.6 * u))
    leaf = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    dl = ImageDraw.Draw(leaf)
    dl.ellipse([9 * u, 15 * u, 26 * u, 26 * u], fill=SAGE)
    leaf = leaf.rotate(18, center=(17 * u, 20 * u), resample=Image.BICUBIC)
    img.alpha_composite(leaf)
    d.ellipse([(32 - 9.5) * u, (27 - 6.5) * u, (32 + 9.5) * u, (27 + 6.5) * u], fill=PINE)
    d.ellipse([(31 - 13.5) * u, (38 - 7.5) * u, (31 + 13.5) * u, (38 + 7.5) * u], fill=PINE)
    d.ellipse([(32 - 18) * u, (51 - 8.5) * u, (32 + 18) * u, (51 + 8.5) * u], fill=PINE)
    return img.resize((size, size), Image.LANCZOS)


frame = Image.open(os.path.join(SP, FRAME)).convert("RGB")

# poster: 1600x900, modest quality — it's behind a dark overlay anyway
poster = frame.resize((1600, 900), Image.LANCZOS)
poster.save(os.path.join(ROOT, "assets", "video", "hero-poster.webp"), "WEBP", quality=68, method=6)
print("poster", os.path.getsize(os.path.join(ROOT, "assets", "video", "hero-poster.webp")))

# og image 1200x630 with green gradient + brand
og = frame.resize((1200, 675), Image.LANCZOS).crop((0, 22, 1200, 652)).convert("RGBA")
ov = Image.new("RGBA", og.size, (0, 0, 0, 0))
do = ImageDraw.Draw(ov)
for y in range(630):
    a = int(215 * max(0, (y - 230) / 400) ** 1.4)
    do.line([(0, y), (1200, y)], fill=(10, 30, 20, a))
for y in range(630):
    a = int(120 * (1 - y / 630) ** 2)
    do.line([(0, y), (1200, y)], fill=(10, 30, 20, a // 3))
og = Image.alpha_composite(og, ov)

f_big = ImageFont.truetype(os.path.join(SP, "fraunces-static350.ttf"), 92)
f_sub = ImageFont.truetype("arialbd.ttf", 26)
d = ImageDraw.Draw(og)
og.alpha_composite(draw_mark(110), (72, 428))
d.text((210, 430), "Sage & Stone", font=f_big, fill=CREAM)
d.text((214, 548), "L A N D S C A P E  C O .   ·   B E N D ,  O R E G O N", font=f_sub, fill=GOLD)
og.convert("RGB").save(os.path.join(ROOT, "assets", "img", "og-home.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
print("og", os.path.getsize(os.path.join(ROOT, "assets", "img", "og-home.jpg")))
