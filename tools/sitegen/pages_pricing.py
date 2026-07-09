# Pricing page. Figures anchored to 2026 national cost data (Angi, HomeGuide,
# LawnLove, Techo-Bloc contractor survey, NerdWallet) with a Central Oregon
# labor/material adjustment — and kept consistent with numbers quoted
# elsewhere on the site.
from parts import SITE, ICON_CHECK, ARR

TIERS = [
    {
        "name": "The Refresh",
        "range": "$8k – $18k",
        "who": "For a yard that's basically right but tired.",
        "items": [
            "Planting-bed renovation with native and adapted plants",
            "Fresh mulch, edging, and soil amendment throughout",
            "Drip retrofit for the beds you're keeping",
            "Smart controller upgrade and full irrigation tune-up",
            "Two-season establishment warranty",
        ],
        "pop": False,
    },
    {
        "name": "The Full Yard",
        "range": "$25k – $60k",
        "who": "Our most-booked project: a blank or broken yard, done completely.",
        "items": [
            "Scaled design with plant palette and materials board",
            "Paver patio or gathering space (200–400 sq ft)",
            "Full native planting plan with boulders and rock work",
            "New hydrozoned irrigation — drip beds, efficient turf zones",
            "Low-voltage lighting on paths and key trees",
            "Two-season craftsmanship + establishment warranty",
        ],
        "pop": True,
    },
    {
        "name": "The Estate",
        "range": "$60k – $150k+",
        "who": "Acreage and outdoor-living builds with multiple zones.",
        "items": [
            "Everything in The Full Yard, scaled to the property",
            "Fire court, outdoor kitchen, or pergola structures",
            "Retaining walls, terracing, and grade work",
            "Windbreaks, meadow zones, and pasture transitions",
            "Phased build plans available across seasons",
        ],
        "pop": False,
    },
]

GROUPS = [
    ("Design", "landscape-design-build", [
        ("Site walk &amp; consultation", "Free", "60–90 minutes on your property, honest talk, no folder of upsells"),
        ("Landscape design package", "$1,500 – $4,500", "Scaled plan, plant palette, materials — credited back when we build"),
        ("Design-build projects", "$25k – $120k", "Typical range for complete design-and-build landscapes in Central Oregon"),
    ]),
    ("Hardscape &amp; outdoor living", "hardscaping-outdoor-living", [
        ("Paver patio, installed", "$22 – $28 / sq ft", "On engineered, freeze-thaw-rated base — most patios land $8,500–$30,000"),
        ("Fire pit or fire court", "$3,500 – $9,000", "Basalt or steel, wood-burning or plumbed gas, permits handled"),
        ("Retaining &amp; seat walls", "$45 – $75 / face sq ft", "Engineered for our freeze-thaw cycles, drainage included"),
        ("Pergola or shade structure", "from $6,500", "Cedar or steel, framed for Central Oregon snow load"),
        ("Landscape lighting", "from $2,400", "8-fixture low-voltage starter system, expandable by zone"),
    ]),
    ("Water-wise irrigation", "water-wise-irrigation", [
        ("New irrigation system", "$1.50 – $3.00 / sq ft", "Hydrozoned drip and high-efficiency rotators — most systems $4,500–$9,000"),
        ("Turf-to-drip conversion", "from $12,000", "Lawn out, native planting in, water bill down 40–60%"),
        ("Smart controller upgrade", "$650 – $1,200", "Weather-based controller, installed, programmed, and tuned"),
        ("Irrigation audit &amp; tune-up", "$225", "Head-by-head check with a written report and fix list"),
        ("Fall blowout", "$95", "Route-scheduled before the first hard freeze"),
        ("Spring start-up", "$135", "Pressure checks, programming, and a written condition report"),
    ]),
    ("Maintenance &amp; care", "landscape-maintenance", [
        ("Full-season program", "$220 – $480 / mo", "Weekly visits April–November: pruning, fertility, irrigation both ends"),
        ("Every-other-week program", "from $160 / mo", "Same crew, lighter cadence — best for low-water landscapes"),
        ("Spring or fall cleanup", "$350 – $950", "Cutbacks, bed refresh, pre-emergent, haul-away included"),
        ("One-time cleanup &amp; reset", "from $650", "For yards that got away — includes a condition report"),
        ("Mulch, delivered &amp; installed", "$95 – $120 / cu yd", "Includes edging and bed prep, not just a dumped pile"),
    ]),
]

FACTORS = [
    ("Access", "A yard a skid steer can reach costs less than one we wheelbarrow through a 36-inch gate."),
    ("What's underground", "Lava rock, caliche hardpan, and old construction debris slow excavation — we scout it on the site walk."),
    ("Materials", "Concrete pavers vs. natural basalt, cedar vs. steel — we price options side by side so you choose the trade-offs."),
    ("Slope &amp; drainage", "Grade work and retaining needs are the biggest hidden variable on Bend's west side lots."),
    ("Season", "Design in winter, build in spring — early-season slots book at standard rates while summer fills."),
]

FAQ = [
    ("Why ranges instead of exact prices?",
     "Because your lot hasn't been walked yet. These ranges are what real projects cost across Central Oregon; after a free site walk you get a fixed, line-item estimate — and that number holds unless hidden conditions surface, in which case we pause and agree on changes in writing first."),
    ("How do payments work?",
     "A deposit secures your build slot and materials, progress payments follow defined milestones, and the final payment comes at walkthrough. We never ask for full payment up front."),
    ("Are these prices high or low for Bend?",
     "Middle of the licensed, insured market. Central Oregon runs a bit above national averages on labor and materials — our numbers track 2026 national cost guides with that adjustment. Unlicensed cash crews will quote less; they also disappear when the patio heaves in February."),
    ("Does the design fee really come back?",
     "Yes — the $1,500–$4,500 design fee is credited in full against the build when we construct the project within twelve months."),
]


def body():
    tiers = ""
    for t in TIERS:
        items = "\n".join(f"<li>{ICON_CHECK}<span>{i}</span></li>" for i in t["items"])
        badge = '<span class="tier-badge">Most booked</span>' if t["pop"] else ""
        tiers += f'''<div class="tier{' pop' if t['pop'] else ''} rv">
  {badge}
  <h3>{t['name']}</h3>
  <b class="amount">{t['range']}</b>
  <p>{t['who']}</p>
  <ul class="checks">{items}</ul>
</div>'''

    groups = ""
    for name, slug, rows in GROUPS:
        rws = "\n".join(
            f'''<li class="price-row"><div><b>{item}</b><span>{note}</span></div><span class="dots" aria-hidden="true"></span><strong>{price}</strong></li>'''
            for item, price, note in rows
        )
        groups += f'''<section class="price-group rv" aria-label="{name} pricing">
  <div class="pg-head">
    <h3>{name}</h3>
    <a href="services/{slug}.html">About this service {ARR}</a>
  </div>
  <ul class="price-list">{rws}</ul>
</section>'''

    factors = "\n".join(
        f'<div class="factor rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in FACTORS
    )
    faqs = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)

    return f'''
<main id="main">
<div class="wrap crumbs">
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="index.html">Home</a></li>
      <li aria-current="page">Pricing</li>
    </ol>
  </nav>
</div>
<section class="wrap page-hero">
  <p class="eyebrow">Transparent pricing — Central Oregon, 2026</p>
  <h1>Honest numbers, before we ever walk your lot</h1>
  <p class="lede">Most landscapers make you book a sales visit to hear a price. Here's what real projects cost across Bend and Central Oregon — anchored to 2026 national cost data, adjusted for our market. Your exact number comes from a free site walk and a fixed, line-item estimate.</p>
</section>

<section class="sec" aria-labelledby="tiers-h" style="padding-top:clamp(2rem,4vw,3rem)">
  <div class="wrap">
    <div class="sec-head rv">
      <p class="eyebrow">Complete projects</p>
      <h2 id="tiers-h">Three ways people invest in a landscape</h2>
    </div>
    <div class="tiers">{tiers}</div>
    <p class="form-note rv" style="margin-top:1.6rem">Ranges reflect completed Sage &amp; Stone projects and 2026 cost guides. Every project gets a fixed line-item price before work begins — the price you approve is the price you pay.</p>
  </div>
</section>

<section class="sec" aria-labelledby="rates-h" style="background:var(--sand-2)">
  <div class="wrap">
    <div class="sec-head rv">
      <p class="eyebrow">By the line item</p>
      <h2 id="rates-h">Service rates &amp; starting figures</h2>
    </div>
    <div class="price-groups">{groups}</div>
  </div>
</section>

<section class="sec" aria-labelledby="factors-h">
  <div class="wrap">
    <div class="sec-head rv">
      <p class="eyebrow">Why quotes differ</p>
      <h2 id="factors-h">What actually moves the number</h2>
    </div>
    <div class="factors">{factors}</div>
  </div>
</section>

<section class="sec" id="pricing-faq" aria-labelledby="pfaq-h" style="background:var(--sand-2)">
  <div class="wrap">
    <div class="sec-head center rv">
      <p class="eyebrow">Money questions</p>
      <h2 id="pfaq-h">Fair questions about pricing</h2>
    </div>
    <div class="faq rv">{faqs}</div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap cta-in">
    <h2 class="rv">Want your number? It starts with a free walk.</h2>
    <a class="btn btn-ghost on-dark rv" href="index.html#quote">Book a free site walk {ARR}</a>
  </div>
</section>
</main>
'''
