"""Raster assets: hero poster, og image, favicon + touch icons."""
import os
from PIL import Image, ImageDraw, ImageFont

SP = os.path.dirname(os.path.abspath(__file__))
ROOT = r"E:\templates\landscaping website template"
IMG = os.path.join(ROOT, "assets", "img")
VID = os.path.join(ROOT, "assets", "video")
os.makedirs(IMG, exist_ok=True)
os.makedirs(VID, exist_ok=True)

PINE = (22, 31, 20)
SAND = (242, 236, 211)
CREAM = (248, 244, 226)
GOLD = (205, 186, 140)


def fit_logo(path, box):
    """The s&s mark, resized to fit within box x box (aspect preserved), centered on a transparent canvas."""
    src = Image.open(path).convert("RGBA")
    w, h = src.size
    scale = box / max(w, h)
    new = src.resize((max(1, round(w * scale)), max(1, round(h * scale))), Image.LANCZOS)
    canvas = Image.new("RGBA", (box, box), (0, 0, 0, 0))
    off = ((box - new.width) // 2, (box - new.height) // 2)
    canvas.alpha_composite(new, off)
    return canvas


LOGO = os.path.join(IMG, "s&s.png")
LOGO_WHITE = os.path.join(IMG, "s&s-white.png")

# favicons / touch icons
fit_logo(LOGO, 96).save(os.path.join(IMG, "favicon-96.png"))
pad_mark = fit_logo(LOGO, 148)
apple = Image.new("RGBA", (180, 180), SAND + (255,))
apple.alpha_composite(pad_mark, (16, 16))
apple.convert("RGB").save(os.path.join(IMG, "apple-touch-icon.png"))
for n in (192, 512):
    inner = fit_logo(LOGO, int(n * 0.82))
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
mark = fit_logo(LOGO_WHITE, 110)
og.alpha_composite(mark, (72, 428))
x = 210
d.text((x, 430), "Sage & Stone", font=f_big, fill=CREAM)
w = d.textlength("Sage & Stone", font=f_big)
sub = "L A N D S C A P E  C O .   ·   B E N D ,  O R E G O N"
d.text((x + 4, 548), sub, font=f_sub, fill=GOLD)
og.convert("RGB").save(os.path.join(IMG, "og-home.jpg"), "JPEG", quality=82, optimize=True, progressive=True)
print("og done", os.path.getsize(os.path.join(IMG, "og-home.jpg")))
