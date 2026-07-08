# Shared fragments: site config, <head>, header, footer, inline SVG bits.
import json

SITE = {
    "base": "https://philderev.github.io/landscaping/",
    "name": "Sage & Stone Landscape Co.",
    "short": "Sage & Stone",
    "tagline": "High-desert landscape design & build in Bend, Oregon",
    "phone_display": "(541) 555-0148",
    "phone_tel": "+15415550148",
    "email": "hello@sageandstonebend.com",
    "street": "20310 Empire Ave, Suite E4",
    "city": "Bend",
    "region": "OR",
    "zip": "97703",
    "lat": 44.0582,
    "lng": -121.3153,
    "areas": ["Bend", "Redmond", "Sisters", "Tumalo", "Sunriver", "La Pine", "Powell Butte", "Prineville"],
    "lcb": "LCB #10482",
    "ccb": "CCB #231188",
}

# The logo mark: a trail cairn (three stacked stones) in front of a clay sun,
# with a sage sprig. Drawn once, reused inline everywhere via currentColor-ish
# fixed palette (works on light and dark backgrounds).
def logo_mark(stone="#1B2E24", size=44, title=False):
    t = "<title>Sage &amp; Stone Landscape Co. mark</title>" if title else ""
    return f'''<svg viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-hidden="{'false' if title else 'true'}" focusable="false">{t}
<circle cx="38" cy="22" r="14" fill="#C4622D"/>
<path d="M14 20c4-6 13-5 15 1 1 4-1 7-4 8l-11 .4c-3-2-3-6 0-9.4Z" fill="#8A9B6E" transform="rotate(-28 22 24) translate(-4 -6)"/>
<path d="M22 12c-6 1-9 6-8 10" fill="none" stroke="#8A9B6E" stroke-width="2.6" stroke-linecap="round"/>
<ellipse cx="32" cy="27" rx="9.5" ry="6.5" fill="{stone}"/>
<ellipse cx="31" cy="38" rx="13.5" ry="7.5" fill="{stone}"/>
<ellipse cx="32" cy="51" rx="18" ry="8.5" fill="{stone}"/>
</svg>'''


ICON_PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7.4 7.4 0 0 0-7.4 7.4c0 5.3 6.5 11.9 6.8 12.2a.9.9 0 0 0 1.2 0c.3-.3 6.8-6.9 6.8-12.2A7.4 7.4 0 0 0 12 2Zm0 10.2a2.9 2.9 0 1 1 0-5.8 2.9 2.9 0 0 1 0 5.8Z"/></svg>'
ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.4 15.6c-1.2-.1-2.4-.4-3.5-.9-.5-.2-1.1-.1-1.5.3l-1.5 1.5a15.3 15.3 0 0 1-6.4-6.4L9 8.6c.4-.4.5-1 .3-1.5-.5-1.1-.8-2.3-.9-3.5A1.5 1.5 0 0 0 6.9 2.3H4a1.6 1.6 0 0 0-1.6 1.8A18.6 18.6 0 0 0 19.9 21.6 1.6 1.6 0 0 0 21.7 20v-2.9a1.5 1.5 0 0 0-1.3-1.5Z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm-.4 4.25-6.54 4.09a2 2 0 0 1-2.12 0L4.4 8.25a.85.85 0 1 1 .9-1.44L12 10.9l6.7-4.09a.85.85 0 1 1 .9 1.44Z"/></svg>'
ICON_CLOCK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2Zm4.2 13.4a1 1 0 0 1-1.4.4L11.5 14a1 1 0 0 1-.5-.9V7a1 1 0 0 1 2 0v5.5l2.9 1.6a1 1 0 0 1 .3 1.3Z"/></svg>'
ICON_CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2Zm5 7.4-5.9 6a1 1 0 0 1-1.4 0L7 12.7a1 1 0 1 1 1.4-1.4l2 2 5.2-5.3A1 1 0 1 1 17 9.4Z"/></svg>'
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 2 2.9 6.2 6.6.8-4.9 4.6 1.3 6.6L12 17l-5.9 3.2 1.3-6.6L2.5 9l6.6-.8Z"/></svg>'
ARR = '<span class="arr" aria-hidden="true">→</span>'

SQUIGGLE = '<svg viewBox="0 0 220 14" preserveAspectRatio="none" aria-hidden="true"><path d="M3 10 C 40 2, 75 12, 110 7 S 185 3, 217 8" fill="none" stroke="#C4622D" stroke-width="5" stroke-linecap="round"/></svg>'

CONTOURS = '''<svg class="contours" viewBox="0 0 1200 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
<g fill="none" stroke="#C9D2B1" stroke-width="1.4">
<path d="M-40 520 C 180 430, 300 560, 520 480 S 900 420, 1240 500"/>
<path d="M-40 470 C 190 380, 320 510, 540 430 S 910 370, 1240 450"/>
<path d="M-40 420 C 200 330, 340 460, 560 380 S 920 320, 1240 400"/>
<path d="M-40 370 C 210 285, 360 410, 580 335 S 930 275, 1240 350"/>
<path d="M-40 320 C 220 240, 380 360, 600 290 S 940 230, 1240 300"/>
<path d="M240 180 C 320 120, 470 130, 520 200 S 430 330, 330 290 240 240 240 180Z"/>
<path d="M280 200 C 340 155, 440 165, 475 215 S 415 300, 345 270 280 235 280 200Z"/>
<path d="M320 220 C 360 190, 420 195, 440 225 S 400 272, 360 255 320 240 320 220Z"/>
<path d="M760 120 C 850 60, 1000 80, 1050 160 S 950 300, 840 250 760 180 760 120Z"/>
<path d="M800 140 C 870 95, 975 110, 1012 170 S 935 270, 855 232 800 185 800 140Z"/>
</g></svg>'''


def head(*, title, desc, canonical_path, root, og_type="website", extra_schema=None, preload_poster=False):
    """Build the full <head> — inline CSS is appended by build.py."""
    canon = SITE["base"] + canonical_path
    og_img = SITE["base"] + "assets/img/og-home.jpg"
    schemas = extra_schema or []
    blocks = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, separators=(",", ":"))}</script>'
        for s in schemas
    )
    poster = (
        f'<link rel="preload" as="image" href="{root}assets/video/hero-poster.webp" fetchpriority="high">'
        if preload_poster else ""
    )
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#12211A">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}assets/img/favicon-96.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="preload" href="{root}assets/fonts/fraunces-latin.woff2" as="font" type="font/woff2" crossorigin>
{poster}
{blocks}
<script>document.documentElement.classList.replace('no-js','js')</script>'''


def header(root, active=""):
    def cur(k):
        return ' aria-current="page"' if k == active else ""
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-head" id="top">
  <div class="wrap head-in">
    <a class="brand" href="{root}index.html">
      {logo_mark()}
      <span class="brand-name">Sage &amp; Stone<span class="brand-sub">Landscape Co. · Bend, OR</span></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="{root}index.html#services"{cur('services')}>Services</a>
      <a href="{root}index.html#work">Our Work</a>
      <a href="{root}index.html#about">Why High Desert</a>
      <a href="{root}index.html#areas">Service Area</a>
      <a class="nav-phone" href="tel:{SITE['phone_tel']}" aria-label="Call {SITE['phone_display']}">{SITE['phone_display']}</a>
      <a class="btn btn-primary" href="{root}index.html#quote">Get a quote</a>
    </nav>
  </div>
</header>'''


def footer(root):
    year = 2026
    svc = [
        ("landscape-design-build", "Landscape Design &amp; Build"),
        ("hardscaping-outdoor-living", "Hardscaping &amp; Outdoor Living"),
        ("water-wise-irrigation", "Water-Wise Irrigation"),
        ("landscape-maintenance", "Year-Round Maintenance"),
    ]
    svc_links = "\n".join(f'<li><a href="{root}services/{s}.html">{n}</a></li>' for s, n in svc)
    areas = "\n".join(f"<li>{a}, Oregon</li>" for a in SITE["areas"][:6])
    return f'''<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      {logo_mark(stone="#F4EEE3", size=52)}
      <p>Design-build landscaping rooted in Central Oregon — native planting, basalt hardscapes, and water-wise systems made for the high desert.</p>
      <div class="socials">
        <a href="https://www.facebook.com/sageandstonebend" aria-label="Sage &amp; Stone on Facebook"><svg viewBox="0 0 24 24"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.3-1.5 1.6-1.5h1.6V3.6c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.4-4 4.1v2.3H7.6V13h2.7v8Z"/></svg></a>
        <a href="https://www.instagram.com/sageandstonebend" aria-label="Sage &amp; Stone on Instagram"><svg viewBox="0 0 24 24"><path d="M12 8.1A3.9 3.9 0 1 0 15.9 12 3.9 3.9 0 0 0 12 8.1Zm0 6.4a2.5 2.5 0 1 1 2.5-2.5 2.5 2.5 0 0 1-2.5 2.5ZM17.4 3H6.6A3.6 3.6 0 0 0 3 6.6v10.8A3.6 3.6 0 0 0 6.6 21h10.8a3.6 3.6 0 0 0 3.6-3.6V6.6A3.6 3.6 0 0 0 17.4 3Zm2.2 14.4a2.2 2.2 0 0 1-2.2 2.2H6.6a2.2 2.2 0 0 1-2.2-2.2V6.6a2.2 2.2 0 0 1 2.2-2.2h10.8a2.2 2.2 0 0 1 2.2 2.2ZM17 6.1a1 1 0 1 0 1 1 1 1 0 0 0-1-1Z"/></svg></a>
        <a href="https://www.youtube.com/@sageandstonebend" aria-label="Sage &amp; Stone on YouTube"><svg viewBox="0 0 24 24"><path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2 26.6 26.6 0 0 0 2 12a26.6 26.6 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.8 1.8c1.6.4 7.8.4 7.8.4s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8A26.6 26.6 0 0 0 22 12a26.6 26.6 0 0 0-.4-4.8ZM10 15V9l5.2 3Z"/></svg></a>
      </div>
    </div>
    <nav aria-label="Services">
      <h3>Services</h3>
      <ul>{svc_links}</ul>
    </nav>
    <div>
      <h3>Serving</h3>
      <ul>{areas}</ul>
    </div>
    <div>
      <h3>Visit or call</h3>
      <ul>
        <li>{SITE['street']}<br>{SITE['city']}, {SITE['region']} {SITE['zip']}</li>
        <li><a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></li>
        <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
        <li>Mon–Fri 7am–5pm · Sat 8am–1pm</li>
      </ul>
    </div>
  </div>
  <div class="wrap foot-legal">
    <span>© {year} {SITE['name']} · Bend, Oregon</span>
    <span>Oregon {SITE['lcb']} · {SITE['ccb']} · Licensed, bonded &amp; insured</span>
  </div>
</footer>
<script src="{root}assets/js/main.js" defer></script>'''


def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "LandscapingBusiness",
        "@id": SITE["base"] + "#business",
        "name": SITE["name"],
        "description": "Design-build landscaping company in Bend, Oregon. Native landscape design, paver patios and hardscapes, water-wise irrigation, and year-round maintenance across Central Oregon.",
        "url": SITE["base"],
        "telephone": SITE["phone_tel"],
        "email": SITE["email"],
        "image": SITE["base"] + "assets/img/og-home.jpg",
        "logo": SITE["base"] + "assets/img/logo.svg",
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE["street"],
            "addressLocality": SITE["city"],
            "addressRegion": SITE["region"],
            "postalCode": SITE["zip"],
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "areaServed": [{"@type": "City", "name": f"{a}, Oregon"} for a in SITE["areas"]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "07:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": "Saturday", "opens": "08:00", "closes": "13:00"},
        ],
        "sameAs": [
            "https://www.facebook.com/sageandstonebend",
            "https://www.instagram.com/sageandstonebend",
            "https://www.youtube.com/@sageandstonebend",
        ],
    }


def breadcrumb_schema(items):
    """items: list of (name, path-or-None-for-current)."""
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                **({"item": SITE["base"] + path} if path is not None else {}),
            }
            for i, (name, path) in enumerate(items)
        ],
    }
