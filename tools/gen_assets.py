"""Raster assets: hero poster, og image, favicon + touch icons."""
import os
from PIL import Image, ImageDraw, ImageFont

SP = os.path.dirname(os.path.abspath(__file__))
ROOT = r"E:\templates\landscaping website template"
IMG = os.path.join(ROOT, "assets", "img")
VID = os.path.join(ROOT, "assets", "video")
os.makedirs(IMG, exist_ok=True)
os.makedirs(VID, exist_ok=True)

PINE = (27, 46, 36)
CLAY = (196, 98, 45)
SAGE = (138, 155, 110)
SAND = (244, 238, 227)
CREAM = (251, 247, 239)
GOLD = (217, 164, 91)


def draw_mark(size, bg=None):
    """The cairn + sun + sage sprig mark, supersampled 4x. Mirrors logo.svg."""
    ss = 4
    s = size * ss
    u = s / 64  # logo.svg viewBox units
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0) if bg is None else bg + (255,))
    d = ImageDraw.Draw(img)
    # sun
    d.ellipse([(38 - 14) * u, (22 - 14) * u, (38 + 14) * u, (22 + 14) * u], fill=CLAY)
    # sprig stem (arc) + leaf blob
    d.arc([8 * u, 12 * u, 30 * u, 32 * u], start=180, end=300, fill=SAGE, width=int(2.6 * u))
    leaf = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    dl = ImageDraw.Draw(leaf)
    dl.ellipse([9 * u, 15 * u, 26 * u, 26 * u], fill=SAGE)
    leaf = leaf.rotate(18, center=(17 * u, 20 * u), resample=Image.BICUBIC)
    img.alpha_composite(leaf)
    # stones
    d.ellipse([(32 - 9.5) * u, (27 - 6.5) * u, (32 + 9.5) * u, (27 + 6.5) * u], fill=PINE)
    d.ellipse([(31 - 13.5) * u, (38 - 7.5) * u, (31 + 13.5) * u, (38 + 7.5) * u], fill=PINE)
    d.ellipse([(32 - 18) * u, (51 - 8.5) * u, (32 + 18) * u, (51 + 8.5) * u], fill=PINE)
    return img.resize((size, size), Image.LANCZOS)


# favicons / touch icons
draw_mark(96).save(os.path.join(IMG, "favicon-96.png"))
pad_mark = draw_mark(148)
apple = Image.new("RGBA", (180, 180), SAND + (255,))
apple.alpha_composite(pad_mark, (16, 16))
apple.convert("RGB").save(os.path.join(IMG, "apple-touch-icon.png"))
for n in (192, 512):
    inner = draw_mark(int(n * 0.82))
    icon = Image.new("RGBA", (n, n), SAND + (255,))
    off = (n - inner.width) // 2
    icon.alpha_composite(inner, (off, off))
    icon.save(os.path.join(IMG, f"icon-{n}.png"))
print("icons done")

# hero poster (first frame = what the video starts on)
frame0 = Image.open(os.path.join(SP, "frames", "f0000.png")).convert("RGB")
frame0.save(os.path.join(VID, "hero-poster.webp"), "WEBP", quality=72, method=6)
print("poster done", os.path.getsize(os.path.join(VID, "hero-poster.webp")))

# og image 1200x630: mid-loop frame, crop, brand overlay
fr = Image.open(os.path.join(SP, "frames", "f0140.png")).convert("RGB")
og = fr.resize((1200, 675), Image.LANCZOS).crop((0, 22, 1200, 652))
ov = Image.new("RGBA", og.size, (0, 0, 0, 0))
do = ImageDraw.Draw(ov)
for y in range(630):
    a = int(200 * max(0, (y - 250) / 380) ** 1.5)
    do.line([(0, y), (1200, y)], fill=(14, 24, 18, a))
og = Image.alpha_composite(og.convert("RGBA"), ov)

f_big = ImageFont.truetype(os.path.join(SP, "fraunces-static350.ttf"), 92)
f_amp = ImageFont.truetype(os.path.join(SP, "fraunces-static600.ttf"), 92)
f_sub = ImageFont.truetype("arialbd.ttf", 26)
d = ImageDraw.Draw(og)
mark = draw_mark(110)
og.alpha_composite(mark, (72, 428))
x = 210
d.text((x, 430), "Sage & Stone", font=f_big, fill=CREAM)
w = d.textlength("Sage & Stone", font=f_big)
sub = "L A N D S C A P E  C O .   ·   B E N D ,  O R E G O N"
d.text((x + 4, 548), sub, font=f_sub, fill=GOLD)
og.convert("RGB").save(os.path.join(IMG, "og-home.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
print("og done", os.path.getsize(os.path.join(IMG, "og-home.jpg")))
