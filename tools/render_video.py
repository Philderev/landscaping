"""Render the Sage & Stone hero background video frames.

Scene: golden hour over the Central Oregon high desert. Layered composition:
sky gradient, pulsing sun glow, drifting clouds, hazy Three Sisters range,
pine ridge, rolling meadow, sage bushes, swaying bunchgrass, floating motes.
Rendered at 2x supersampling for antialiasing, downscaled to 1920x1080.
All motion uses integer sine cycles over the duration so the video loops
seamlessly.
"""
import math
import os
import random
import time

from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 1080
SS = 2  # supersample factor
SW, SH = W * SS, H * SS
FPS = 30
DUR = 12.0
FRAMES = int(FPS * DUR)
TAU = math.tau

OUT = os.path.join(os.path.dirname(__file__), "frames")
os.makedirs(OUT, exist_ok=True)

rng = random.Random(41)


def hx(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def lerp(a, b, t):
    return a + (b - a) * t


def lerp_rgb(c1, c2, t):
    return tuple(int(round(lerp(a, b, t))) for a, b in zip(c1, c2))


# ---------------------------------------------------------------- static sky
def build_sky():
    img = Image.new("RGB", (SW, SH))
    d = ImageDraw.Draw(img)
    stops = [
        (0.00, hx("6F9484")),
        (0.34, hx("9FAE8F")),
        (0.55, hx("D8BC85")),
        (0.72, hx("F0C87E")),
        (1.00, hx("F6DCA4")),
    ]
    for y in range(SH):
        t = y / (SH - 1)
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i + 1]
            if t0 <= t <= t1:
                d.line([(0, y), (SW, y)], fill=lerp_rgb(c0, c1, (t - t0) / (t1 - t0)))
                break
    return img


SUN = (1380 * SS, 610 * SS)


def build_glow(radius, core, edge_alpha=0):
    """Radial glow sprite (RGBA)."""
    size = radius * 2
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    steps = 64
    for i in range(steps, 0, -1):
        t = i / steps
        a = int((1 - t) ** 2 * 255)
        r = int(radius * t)
        d.ellipse([radius - r, radius - r, radius + r, radius + r],
                  fill=core + (max(a, edge_alpha),))
    return img.filter(ImageFilter.GaussianBlur(radius * 0.08))


def build_cloud(w, h, alpha):
    """Soft cumulus sprite from overlapping blurred ellipses.

    Ellipses are inset so the gaussian blur never clips at the sprite edge.
    """
    pad_x, pad_y = int(w * 0.30), int(h * 0.45)
    img = Image.new("RGBA", (w + pad_x * 2, h + pad_y * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    col = hx("FAEDCE")
    n = rng.randint(4, 6)
    for _ in range(n):
        ew = rng.uniform(0.35, 0.62) * w
        eh = rng.uniform(0.30, 0.5) * h
        x = pad_x + rng.uniform(0, w - ew)
        y = pad_y + rng.uniform(h * 0.15, h - eh)
        d.ellipse([x, y, x + ew, y + eh], fill=col + (alpha,))
    return img.filter(ImageFilter.GaussianBlur(h * 0.18))


def ridge_points(base_y, amp, peaks, seed, jag=0.0):
    """Rolling / jagged silhouette top edge across the width."""
    r = random.Random(seed)
    pts = []
    n = 160
    phases = [(r.uniform(0, TAU), r.uniform(0.5, 1.0)) for _ in range(3)]
    for i in range(n + 1):
        x = SW * i / n
        t = i / n
        y = base_y
        for k, (ph, mag) in enumerate(phases):
            y -= amp * mag / (k + 1) * (0.5 + 0.5 * math.sin(TAU * peaks * (k * 0.7 + 1) * t + ph))
        if jag:
            y -= r.uniform(0, amp * jag)
        pts.append((x, y))
    return pts


def poly_from_ridge(pts):
    return pts + [(SW, SH), (0, SH)]


def draw_sisters(d):
    """Hazy triple-peak range (the Three Sisters) on the horizon."""
    col = hx("9BAF9F")
    base = 700 * SS
    peaks = [(430, 175, 260), (760, 200, 300), (1105, 160, 250)]  # x, height, half-width
    for cx, ph, hw in peaks:
        cx, ph, hw = cx * SS, ph * SS, hw * SS
        d.polygon([(cx - hw, base), (cx - hw * 0.25, base - ph * 0.92),
                   (cx, base - ph), (cx + hw * 0.3, base - ph * 0.85),
                   (cx + hw, base)], fill=col)
        # snow cap
        d.polygon([(cx - hw * 0.16, base - ph * 0.80), (cx, base - ph),
                   (cx + hw * 0.2, base - ph * 0.78),
                   (cx + hw * 0.05, base - ph * 0.72),
                   (cx - hw * 0.06, base - ph * 0.76)], fill=hx("EFE9DC"))
    # low connecting range
    d.polygon(poly_from_ridge(ridge_points(705 * SS, 28 * SS, 5, 7)), fill=col)


def draw_pine(d, x, y, h, col):
    """Simple stacked-triangle pine silhouette."""
    w = h * 0.42
    tiers = 3
    for i in range(tiers):
        t0 = i / tiers
        t1 = (i + 1) / tiers
        yw0 = y - h + h * 0.25 + (h * 0.75) * t0
        yw1 = y - h + h * 0.25 + (h * 0.75) * t1
        half = w * (0.35 + 0.65 * t1) / 2
        tip_half = w * (0.35 + 0.65 * t0) / 2 * 0.25
        d.polygon([(x - half, yw1), (x + half, yw1), (x + tip_half, yw0), (x - tip_half, yw0)], fill=col)
    d.polygon([(x - w * 0.16, y - h), (x + w * 0.16, y - h), (x, y - h - h * 0.14)], fill=col)
    d.rectangle([x - w * 0.05, y - h * 0.06, x + w * 0.05, y], fill=col)


def build_midridge():
    layer = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    col = hx("39543F")
    pts = ridge_points(790 * SS, 45 * SS, 3, 11)
    d.polygon(poly_from_ridge(pts), fill=col + (255,))

    def ridge_y(x):
        i = min(int(x / SW * 160), 159)
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        return lerp(y0, y1, (x - x0) / max(x1 - x0, 1))

    r = random.Random(23)
    xs = []
    x = 30 * SS
    while x < SW - 30 * SS:
        xs.append(x)
        x += r.uniform(30, 120) * SS * (0.4 if r.random() < 0.3 else 1.0)
    for x in xs:
        h = r.uniform(38, 92) * SS
        draw_pine(d, x, ridge_y(x) + 6 * SS, h, col)
    return layer


def build_meadow():
    layer = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    top = hx("2C4733")
    bot = hx("152318")
    pts = ridge_points(872 * SS, 26 * SS, 2, 31)
    d.polygon(poly_from_ridge(pts), fill=top + (255,))
    y0 = 880 * SS
    for y in range(y0, SH):
        t = (y - y0) / (SH - y0)
        d.line([(0, y), (SW, y)], fill=lerp_rgb(top, bot, t))
    return layer


def build_sage_bushes():
    layer = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = random.Random(5)
    for cx, cy, s in [(290, 985, 1.15), (1495, 1005, 1.35), (930, 1030, 0.95), (1780, 1035, 1.0)]:
        cx, cy = cx * SS, cy * SS
        base = hx("24391F")
        hi = hx("4E6442")
        for _ in range(9):
            ew = r.uniform(48, 95) * s * SS
            eh = r.uniform(30, 55) * s * SS
            x = cx + r.uniform(-70, 70) * s * SS
            y = cy + r.uniform(-28, 14) * s * SS
            d.ellipse([x - ew / 2, y - eh / 2, x + ew / 2, y + eh / 2], fill=base + (255,))
        for _ in range(4):
            ew = r.uniform(22, 42) * s * SS
            eh = r.uniform(13, 22) * s * SS
            x = cx + r.uniform(-55, 55) * s * SS
            y = cy + r.uniform(-32, -6) * s * SS
            d.ellipse([x - ew / 2, y - eh / 2, x + ew / 2, y + eh / 2], fill=hi + (110,))
    return layer.filter(ImageFilter.GaussianBlur(1.2 * SS))


def build_vignette():
    v = Image.new("L", (SW // 4, SH // 4), 0)
    d = ImageDraw.Draw(v)
    w4, h4 = SW // 4, SH // 4
    for i in range(90):
        t = i / 89
        a = int(78 * t ** 2.2)
        pad_x = int(w4 * 0.55 * (1 - t))
        pad_y = int(h4 * 0.55 * (1 - t))
        d.ellipse([-pad_x - w4 * 0.25, -pad_y - h4 * 0.25,
                   w4 + pad_x + w4 * 0.25, h4 + pad_y + h4 * 0.25], outline=None, fill=None)
    # simpler: radial mask
    v = Image.new("L", (w4, h4), 0)
    px = v.load()
    cx, cy = w4 / 2, h4 / 2
    maxd = math.hypot(cx, cy)
    for yy in range(h4):
        for xx in range(w4):
            t = math.hypot(xx - cx, yy - cy) / maxd
            px[xx, yy] = int(88 * max(0.0, t - 0.55) / 0.45 ** 1.0)
    v = v.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(40))
    black = Image.new("RGBA", (W, H), (8, 14, 10, 255))
    black.putalpha(v)
    return black


# ------------------------------------------------------------------ dynamics
class Blade:
    __slots__ = ("x", "y", "h", "w", "amp", "phase", "col")

    def __init__(self, x, y, h, w, amp, phase, col):
        self.x, self.y, self.h, self.w = x, y, h, w
        self.amp, self.phase, self.col = amp, phase, col


def build_blades():
    blades = []
    cols_back = [hx("2E4A33"), hx("335239"), hx("3C5A3B")]
    cols_front = [hx("14241B"), hx("18291D"), hx("1E3123"), hx("223826")]
    # back row (shorter, lighter, sits on meadow crest)
    x = -40.0
    while x < W + 40:
        h = rng.uniform(50, 110)
        blades.append(Blade(x * SS, rng.uniform(900, 950) * SS, h * SS,
                            rng.uniform(2.2, 3.4) * SS, rng.uniform(6, 12) * SS,
                            rng.uniform(0, TAU), rng.choice(cols_back)))
        x += rng.uniform(8, 18)
    # front row (tall, dark)
    x = -40.0
    while x < W + 40:
        h = rng.uniform(90, 215)
        blades.append(Blade(x * SS, rng.uniform(1020, 1105) * SS, h * SS,
                            rng.uniform(2.8, 4.6) * SS, rng.uniform(10, 24) * SS,
                            rng.uniform(0, TAU), rng.choice(cols_front)))
        x += rng.uniform(6, 14)
    return blades


BLADES = build_blades()

MOTES = [(rng.uniform(0, W), rng.uniform(380, 1000), rng.uniform(1.2, 3.2),
          rng.uniform(0, TAU), rng.uniform(0, TAU), rng.choice([1, 1, 2]))
         for _ in range(46)]

CLOUDS = []
for (cx, cy, cw, ch, al, cyc) in [
    (260, 165, 620, 150, 92, 1), (900, 90, 780, 175, 70, 1),
    (1460, 250, 560, 130, 96, 2), (620, 330, 420, 100, 60, 1),
    (1740, 130, 500, 120, 78, 1),
]:
    CLOUDS.append({"img": build_cloud(int(cw * SS), int(ch * SS), al),
                   "x": cx * SS, "y": cy * SS,
                   "ax": rng.uniform(38, 70) * SS, "ay": rng.uniform(5, 10) * SS,
                   "cyc": cyc, "ph": rng.uniform(0, TAU)})


def main():
    t0 = time.time()
    print("building static layers...")
    sky = build_sky()
    glow_big = build_glow(520 * SS, hx("F5CE84"))
    glow_core = build_glow(120 * SS, hx("FBE7B4"))
    sun_disc_r = 62 * SS

    static_bg = sky.copy()
    # far range + connecting ridge sit over the big glow's lower half
    far = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
    draw_sisters(ImageDraw.Draw(far))
    midridge = build_midridge()
    meadow = build_meadow()
    sage = build_sage_bushes()
    vignette = build_vignette()

    for f in range(FRAMES):
        t = f / FRAMES  # 0..1, loops
        frame = static_bg.copy()

        # sun glow, gentle 2-cycle pulse
        pulse = 0.86 + 0.14 * (0.5 + 0.5 * math.sin(TAU * 2 * t))
        g = glow_big if pulse > 0.99 else Image.eval(glow_big, lambda v: v)
        gb = glow_big.copy()
        if pulse < 1.0:
            a = gb.getchannel("A").point(lambda v: int(v * pulse))
            gb.putalpha(a)
        frame.paste(gb, (SUN[0] - gb.width // 2, SUN[1] - gb.height // 2), gb)

        # clouds drift (integer-cycle sine -> perfect loop)
        for c in CLOUDS:
            dx = c["ax"] * math.sin(TAU * c["cyc"] * t + c["ph"])
            dy = c["ay"] * math.sin(TAU * c["cyc"] * t + c["ph"] * 1.7 + 1.1)
            frame.paste(c["img"], (int(c["x"] + dx - c["img"].width / 2),
                                   int(c["y"] + dy - c["img"].height / 2)), c["img"])

        # mountains, sun core above ridge line, mid ridge, glow bloom
        frame.paste(far, (0, 0), far)
        d = ImageDraw.Draw(frame, "RGBA")
        frame.paste(glow_core, (SUN[0] - glow_core.width // 2, SUN[1] - glow_core.height // 2), glow_core)
        d.ellipse([SUN[0] - sun_disc_r, SUN[1] - sun_disc_r,
                   SUN[0] + sun_disc_r, SUN[1] + sun_disc_r], fill=hx("FCEBC0") + (235,))
        frame.paste(midridge, (0, 0), midridge)
        frame.paste(meadow, (0, 0), meadow)
        frame.paste(sage, (0, 0), sage)

        # grass sway: spatial gust wave + per-blade phase, 2 cycles/loop
        for b in BLADES:
            gust = math.sin(TAU * 2 * t + b.x / (420 * SS))
            sway = b.amp * (0.35 * math.sin(TAU * 3 * t + b.phase) + 0.65 * gust)
            tipx, tipy = b.x + sway, b.y - b.h
            midx = b.x + sway * 0.45
            midy = b.y - b.h * 0.55
            d.polygon([(b.x - b.w, b.y), (b.x + b.w, b.y),
                       (midx + b.w * 0.45, midy), (tipx, tipy),
                       (midx - b.w * 0.45, midy)], fill=b.col)

        # floating motes
        for (mx, my, mr, p1, p2, cyc) in MOTES:
            a = int(28 + 105 * (0.5 + 0.5 * math.sin(TAU * 2 * t + p2)))
            dx = 26 * math.sin(TAU * cyc * t + p1)
            dy = 16 * math.cos(TAU * cyc * t + p1 * 0.6)
            x, y, r_ = (mx + dx) * SS, (my + dy) * SS, mr * SS
            d.ellipse([x - r_, y - r_, x + r_, y + r_], fill=(255, 233, 184, a))

        out = frame.resize((W, H), Image.LANCZOS)
        out.paste(vignette, (0, 0), vignette)
        out.convert("RGB").save(os.path.join(OUT, f"f{f:04d}.png"))
        if f % 30 == 0:
            print(f"frame {f}/{FRAMES}  {time.time() - t0:.0f}s")

    print(f"done {FRAMES} frames in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
