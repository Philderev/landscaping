# Service page definitions + body template.
from parts import SITE, ICON_CHECK, ARR, compact_lead_form

R = "../"

PAGES = {
    "landscape-design-build": {
        "title": "Landscape Design & Build in Bend, OR | Sage & Stone Landscape Co.",
        "desc": "Full-service landscape design and construction in Bend and Central Oregon. Native planting plans, outdoor rooms, and fixed line-item estimates from one dedicated crew.",
        "h1": "Landscape design &amp; build, drawn for the high desert",
        "lede": "One team takes your landscape from first sketch to final walkthrough — a scaled design, a fixed line-item price, and a build crew that treats your lot like the last one they'll ever sign.",
        "banner": "ill-design.svg",
        "banner_alt": "Landscape designer pointing at a color site plan on a laptop, concept drawings spread on the desk",
        "included_h": "What a design-build project includes",
        "included": [
            "Free on-site walk and consultation — sun, wind, soil, drainage, views, deer pressure",
            "Scaled 2D landscape plan with plant palette, materials board, and lighting layout",
            "Fixed, line-item estimate — the price you approve is the price you pay",
            "Grading, soil amendment, and drainage designed for pumice and volcanic ash soils",
            "Native and adapted planting installed with two-season establishment warranty",
            "Boulder and rock placement using local basalt and Deschutes river rock",
            "Low-voltage landscape lighting and irrigation roughed in during the build, not after",
            "Final walkthrough with a plant-by-plant care guide",
        ],
        "body": """
<h2>Designed around your lot, not a catalog</h2>
<p>Every Bend lot has its own logic — where the snow drifts, where the afternoon sun hammers, where the mule deer cut through at dusk. Our designs start with a long walk and a lot of questions, because a landscape that ignores its site becomes a maintenance bill with plants in it.</p>
<p>You'll get a scaled plan you can hold: planting zones grouped by water need, hardscape drawn to the inch, and materials chosen from what already belongs here — basalt, juniper timbers, decomposed granite, river rock. We design outdoor rooms for the way Central Oregonians actually live: fire courts for cold clear evenings, shade structures for July, and windbreaks that make shoulder seasons usable.</p>
<h2>Built by the people who drew it</h2>
<p>Design-build means no hand-off, no finger-pointing, and no "the designer didn't mean that." The foreman who pours your footings sat in the design reviews. Changes get answered in hours, not weeks, and the schedule is posted where you can see it.</p>
<p>Most full projects run four to nine weeks on site. We keep a tidy site, tarp and sweep daily, and never leave a weekend mess.</p>
""",
        "faq": [
            ("How much does landscape design cost?",
             "The site walk is free. Full design packages run $1,500–$4,500 depending on lot size and scope, and the design fee is credited back when we build the project."),
            ("Can you work from my architect's or my own sketch?",
             "Absolutely — we're happy to price and build from existing plans, or refine your sketch into a buildable design."),
        ],
    },
    "hardscaping-outdoor-living": {
        "title": "Paver Patios, Fire Pits & Hardscaping in Bend, OR | Sage & Stone",
        "desc": "Paver patios, basalt fire pits, retaining walls and pergolas built for Central Oregon freeze-thaw. Proper base prep and a two-season warranty from Bend's hardscape crew.",
        "h1": "Hardscapes that hold their line through freeze and thaw",
        "lede": "Patios, fire courts, walls, and pergolas built on honest base prep — because in a town that freezes 180 nights a year, what's under the pavers matters more than the pavers.",
        "banner": "ill-hardscape.svg",
        "banner_alt": "Paver patio with a stone fire pit, seat walls and Adirondack chairs behind a brick home",
        "included_h": "What we build",
        "included": [
            "Paver and natural-stone patios on compacted, geotextile-reinforced base",
            "Basalt and steel fire pits and fire courts — wood or plumbed gas",
            "Retaining and seat walls engineered for our freeze-thaw cycles",
            "Pergolas, shade structures, and privacy screens in cedar and steel",
            "Outdoor kitchens, counters, and built-in seating",
            "Paths and driveways in pavers, flagstone, and decomposed granite",
            "Low-voltage lighting integrated into steps, walls, and trees",
            "Permeable options that return snowmelt to your soil, not the street",
        ],
        "body": """
<h2>Freeze-thaw is the whole game</h2>
<p>Central Oregon swings through more freeze-thaw cycles than almost anywhere in the Northwest — and every winter it quietly destroys patios that were built on two inches of sand and optimism. Our hardscapes start with excavation to mineral soil, engineered base compacted in lifts, geotextile separation, and drainage that gives meltwater somewhere to go. It's invisible work, and it's why our patios stay flat.</p>
<h2>Local stone, honest details</h2>
<p>We build with what the high desert gives us: basalt columns and boulders, Deschutes river rock, lava rock accents, and porcelain or concrete pavers rated for hard frost. Edges get restrained, steps get lit, and fire features get plumbed and permitted properly.</p>
<p>Every hardscape carries our two-season warranty across a full freeze-thaw cycle — if anything settles or heaves, we make it right.</p>
""",
        "faq": [
            ("What does a paver patio cost in Bend?",
             "Most of our patios land between $8,500 and $30,000 depending on size, stone, and access. Fire features typically add $3,500–$9,000. You'll get a fixed line-item price before we break ground."),
            ("Do I need a permit for a fire pit or wall?",
             "Walls over four feet and plumbed gas features typically do. We handle permitting and inspections as part of the project."),
        ],
    },
    "water-wise-irrigation": {
        "title": "Water-Wise Irrigation & Smart Sprinklers in Bend, OR | Sage & Stone",
        "desc": "Drip irrigation, smart controllers, hydrozoning, blowouts and spring start-ups in Bend and Central Oregon. Healthier landscapes on roughly half the water.",
        "h1": "Irrigation built for a 12-inch-of-rain climate",
        "lede": "Drip zones, smart controllers, and hydrozoning that deliver water where roots actually are — most conversions cut outdoor water use 40–60% while the landscape looks better, not worse.",
        "banner": "ill-irrigation.svg",
        "banner_alt": "Irrigation sprinkler watering a green lawn with backlit water droplets catching the sun",
        "included_h": "Irrigation services",
        "included": [
            "New system design and installation — drip, rotary, and MP rotator zones",
            "Hydrozoning: plants grouped by water need so no zone overwaters half its plants",
            "Smart weather-based controllers (Hydrawise, Rachio) set up and tuned for Bend's climate",
            "System audits, leak detection, and head-by-head efficiency tuning",
            "Turf-to-drip conversions when you replace lawn with native planting",
            "Fall blowouts before the first hard freeze — booked on a route, done right",
            "Spring start-ups with pressure checks, controller programming, and a written report",
            "Backflow testing coordination and repair",
        ],
        "body": """
<h2>The cheapest water is the water you don't spray</h2>
<p>Bend gets about twelve inches of precipitation a year, and city water rates climb every season. Overhead spray on a windy 90° afternoon can lose half its water before it touches soil. Our systems put water at the root zone — drip for beds, high-efficiency rotators where turf earns its keep — on schedules that follow the actual weather instead of a clock.</p>
<h2>Set up for our seasons</h2>
<p>High-desert irrigation lives and dies by the calendar: charged after the last hard freeze, tapered through fall, blown out before the first deep cold. Maintenance clients get both ends of that calendar handled automatically, with a written condition report each visit. One less thing to remember, and no burst manifolds in November.</p>
""",
        "faq": [
            ("How much water will I actually save?",
             "Typical turf-to-drip conversions in our service area cut outdoor use 40–60%. A smart controller alone usually saves 20–30% by skipping unnecessary cycles."),
            ("When should I schedule my blowout?",
             "Mid-October through mid-November, before the first sustained hard freeze. Maintenance clients are routed automatically each fall."),
        ],
    },
    "landscape-maintenance": {
        "title": "Landscape Maintenance in Bend, OR | Sage & Stone Landscape Co.",
        "desc": "Year-round landscape maintenance in Bend: seasonal pruning, fertility, irrigation start-ups and blowouts, and native planting care from a licensed Central Oregon crew.",
        "h1": "Care that keeps a landscape getting better",
        "lede": "A high-desert landscape isn't finished at install — it's established over seasons. Our maintenance calendar keeps plantings thriving, systems tuned, and weekends yours.",
        "banner": "ill-maintenance.svg",
        "banner_alt": "Gardener shaping a shrub with long-handled hedge shears",
        "included_h": "What's on the calendar",
        "included": [
            "Spring clean-ups: cutbacks, bed refresh, pre-emergent, mulch top-up",
            "Structural and seasonal pruning — trees, shrubs, and ornamental grasses",
            "Fertility programs matched to volcanic soils, not generic 4-step bags",
            "Irrigation spring start-ups and fall blowouts, bundled in",
            "Native and low-water planting care (they're low-water, not no-care)",
            "Weed management that protects your plantings and the watershed",
            "Fall clean-ups and winter preparation for plants and hardscape",
            "Written visit reports with photos, so you always know what was done",
        ],
        "body": """
<h2>Maintenance that understands what's planted</h2>
<p>Most maintenance crews mow, blow, and go. Ours are trained on the plant palettes we design with — they know a young penstemon from a weed, when bunchgrasses want cutting (late winter, not fall), and how to prune a serviceberry so it flowers instead of sulking. That knowledge is the difference between a landscape that matures and one that slowly unravels.</p>
<h2>Plans that match your landscape, not a template</h2>
<p>Choose a full-season program or an every-other-week visit; either way you get the same two-person crew, a season calendar written for your specific plantings, and a photo report after every visit. Maintenance clients also get first call on irrigation service and priority scheduling for the fall blowout route.</p>
""",
        "faq": [
            ("What does maintenance cost?",
             "Most Bend properties run $220–$480 per month on a full-season program, depending on size and planting complexity. One-time clean-ups start around $650."),
            ("Do you maintain landscapes you didn't build?",
             "Yes — we'll start with a walkthrough and a condition report, then propose a calendar to get it back on track."),
        ],
    },
}

ORDER = ["landscape-design-build", "hardscaping-outdoor-living", "water-wise-irrigation", "landscape-maintenance"]
NAMES = {
    "landscape-design-build": "Landscape Design &amp; Build",
    "hardscaping-outdoor-living": "Hardscaping &amp; Outdoor Living",
    "water-wise-irrigation": "Water-Wise Irrigation",
    "landscape-maintenance": "Year-Round Maintenance",
}


def body(slug):
    p = PAGES[slug]
    checks = "\n".join(f"<li>{ICON_CHECK}<span>{item}</span></li>" for item in p["included"])
    faqs = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in p["faq"])
    others = "\n".join(
        f'<li><a href="{s}.html">{NAMES[s]} {ARR}</a></li>' for s in ORDER if s != slug
    )
    return f'''
<main id="main">
<div class="wrap crumbs">
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="../index.html">Home</a></li>
      <li><a href="../index.html#services">Services</a></li>
      <li aria-current="page">{NAMES[slug]}</li>
    </ol>
  </nav>
</div>
<section class="wrap page-hero">
  <div class="page-hero-grid">
    <div><p class="eyebrow">{NAMES[slug]} — Bend &amp; Central Oregon</p><h1>{p['h1']}</h1><p class="lede">{p['lede']}</p></div>
    {compact_lead_form('../')}
  </div>
  <div class="banner-art rv">
    <img src="../assets/img/{p['banner'].replace('ill-', 'banner-').replace('.svg', '.webp')}" alt="{p['banner_alt']}" width="2520" height="960" fetchpriority="high">
  </div>
</section>
<section class="sec">
  <div class="wrap split">
    <div class="prose rv">
      <h2 style="margin-top:0">{p['included_h']}</h2>
      <ul class="checks">{checks}</ul>
      {p['body']}
      <h2>Questions about this service</h2>
      <div class="faq" style="max-width:none">{faqs}</div>
    </div>
    <aside>
      <div class="side-card rv">
        <h3 class="serif">Start with a free site walk</h3>
        <p style="color:var(--ink-soft);font-size:.97rem">We'll walk the property, talk options and honest budgets, and follow up with a fixed line-item estimate.</p>
        <a class="btn btn-primary" href="../index.html#quote">Request my site walk {ARR}</a>
        <a class="btn btn-ghost" href="tel:{SITE['phone_tel']}">Call {SITE['phone_display']}</a>
        <hr>
        <h4 style="margin:0 0 .8rem;font-family:var(--serif);font-weight:500">Other services</h4>
        <ul class="side-links">{others}</ul>
      </div>
    </aside>
  </div>
</section>
<section class="cta-band">
  <div class="wrap cta-in">
    <h2 class="rv">Let's walk your lot together.</h2>
    <a class="btn btn-ghost on-dark rv" href="../index.html#quote">Book a free site walk {ARR}</a>
  </div>
</section>
</main>
'''
