# Service-area pages — one per town, each with genuinely local content.
from parts import SITE, AREA_PAGES, ICON_CHECK, ARR

NAME = dict(AREA_PAGES)

AREAS = {
    "bend": {
        "title": "Landscaping in Bend, OR | Sage & Stone Landscape Co.",
        "desc": "Bend's design-build landscaping crew: native planting, paver patios, and water-wise irrigation for west-side pumice lots and east-side juniper flats. Free site walks.",
        "h1": "Landscaping in Bend, Oregon — our home turf",
        "lede": "Our shop sits off Empire Avenue, and most of our 480+ projects are within fifteen minutes of it. We know Bend lot by lot — because we've probably built on your street.",
        "facts": [("3,623 ft", "elevation — high-desert rules apply"), ("Zone 6b", "USDA hardiness, frost any month"),
                  ("Home base", "crews dispatch from NE Bend daily"), ("Tiered rates", "city water pricing rewards low-water design")],
        "body": """
<h2>West side and east side are different jobs</h2>
<p>West of the parkway — NorthWest Crossing, Shevlin, Awbrey Butte — you're on deep pumice under ponderosa: fast-draining, acidic-leaning, and shady in exactly the wrong places. East side neighborhoods like Larkspur and Mountain View sit on thinner, more alkaline soil over hardpan with all-day sun and wind. We carry two different planting playbooks, two different irrigation strategies, and we'll tell you plainly which one your lot needs.</p>
<h2>Where Bend budgets go furthest</h2>
<p>Bend's tiered water rates mean turf is the most expensive thing you can own by August. The projects with the best payback in town: converting front lawns to layered native beds on drip, firewise thinning and stone mulch near Shevlin Park and the river canyon, and outdoor rooms — covered patios, fire courts — that stretch our short, brilliant summers by two months on each end. HOA design review in NWX or on Awbrey? We handle the submittal paperwork as part of design.</p>
""",
        "notes": ["Pumice soils drain in minutes — we build beds with compost amendment and drip, not spray",
                  "Deer corridors run Awbrey Butte and the river trail — planting plans assume visitors",
                  "Firewise zoning matters near Shevlin Park, Deschutes River Woods, and the canyon rim",
                  "HOA design submittals handled for NorthWest Crossing, Tetherow, and Awbrey Butte"],
        "near": ["tumalo", "redmond", "sunriver"],
    },
    "redmond": {
        "title": "Landscaping in Redmond, OR | Sage & Stone Landscape Co.",
        "desc": "Redmond landscaping built for caliche hardpan and wind: design-build yards, patios, windbreaks, and water-wise irrigation from a licensed Central Oregon crew.",
        "h1": "Landscaping in Redmond, Oregon",
        "lede": "Twenty minutes north of our shop, 500 feet lower, and a few degrees warmer — Redmond looks easier than Bend until your shovel hits caliche. Ours have hit a lot of it.",
        "facts": [("3,077 ft", "lower and warmer than Bend"), ("Caliche", "cemented hardpan under much of town"),
                  ("20 min", "from our Bend shop — daily routes"), ("Wind", "open flats need windbreaks and staking")],
        "body": """
<h2>The caliche layer changes how you build</h2>
<p>Much of Redmond sits on a cemented calcium-carbonate hardpan a foot or two down. Plant a tree in a caliche pocket the lazy way and you've built a bathtub that drowns it by year three. We bore through or trench proper drainage for every tree pit, and we design walls and patios with footings that respect what's actually under the surface — it's the single biggest difference between landscapes that last here and ones that don't.</p>
<h2>Wind is the second client</h2>
<p>From the Dry Canyon to Eagle Crest, Redmond properties take wind Bend neighborhoods never feel. We place windbreak plantings and screen structures first, then build the living spaces in their shelter — which is also what keeps your fire pit usable and your young trees from racking sideways. Warmer summers here also widen the plant palette: some of our favorite bloomers that sulk in Bend thrive in Redmond yards.</p>
""",
        "notes": ["Tree pits bored through hardpan with engineered drainage — no caliche bathtubs",
                  "Windbreaks and screening designed before patios, not after",
                  "Eagle Crest and Ridge at Eagle Crest HOA submittals handled",
                  "Slightly warmer zone opens planting options Bend can't grow"],
        "near": ["powell-butte", "tumalo", "sisters"],
    },
    "sisters": {
        "title": "Landscaping in Sisters, OR | Sage & Stone Landscape Co.",
        "desc": "Sisters landscaping in the ponderosa forest edge: firewise defensible space, deer-resistant native design, and hardscapes built for snow country.",
        "h1": "Landscaping in Sisters, Oregon",
        "lede": "Sisters yards live where the high desert meets ponderosa forest — which means fire, deer, and snow set the rules before design even starts. We design beautifully inside those rules.",
        "facts": [("3,186 ft", "forest-edge microclimate"), ("Firewise", "defensible space is design priority one"),
                  ("Heavy deer", "resistant palettes only — no candy"), ("25 min", "from our Bend shop")],
        "body": """
<h2>Defensible space that doesn't look like a moonscape</h2>
<p>The five- and thirty-foot zones around a Sisters home decide how it fares in a fire season — but defensible space done thoughtfully reads as design, not paranoia. Stone mulch and basalt near structures, limbed-up pines, low-fuel native beds with irrigated separation, and firewood stored where embers can't find it. We build to Firewise standards and it still looks like the mountain town charm you moved here for.</p>
<h2>Deer-realistic, snow-ready</h2>
<p>Sisters has the heaviest deer pressure in our service area, full stop. We plant what they genuinely ignore — rabbitbrush, penstemon, catmint, bunchgrasses — and cage anything vulnerable through establishment. Structures get real snow-load framing, patios get base prep for hard freeze, and irrigation gets blown out early on our route because winter shows up here first.</p>
""",
        "notes": ["Firewise defensible-space design in the 0–5 ft and 5–30 ft zones",
                  "Deer-resistant native palettes proven on Sisters properties",
                  "Pergolas and shade structures framed for real snow load",
                  "Western-gateway aesthetic guidelines respected for in-town lots"],
        "near": ["tumalo", "redmond", "bend"],
    },
    "tumalo": {
        "title": "Landscaping in Tumalo, OR | Sage & Stone Landscape Co.",
        "desc": "Tumalo acreage landscaping: irrigation-district water, windbreaks, horse-friendly design, and native planting with Cascade views. Licensed Central Oregon design-build crew.",
        "h1": "Landscaping in Tumalo, Oregon",
        "lede": "Acreage properties, canal water rights, horses, and the best Sisters views in the county — Tumalo projects are half landscape design, half small-ranch logistics. We enjoy both halves.",
        "facts": [("3,250 ft", "open rural benchland"), ("TID water", "canal delivery changes irrigation design"),
                  ("Acreage", "1–20 acre properties are the norm"), ("15 min", "from our Bend shop")],
        "body": """
<h2>Designing with irrigation-district water</h2>
<p>Many Tumalo properties hold Tumalo Irrigation District rights — seasonal canal water that's cheap and plentiful from April to October and completely gone the rest of the year. We design dual systems: district water feeding pasture and shelterbelts through filtered delivery, domestic well water on drip for the refined zones near the house. Getting that split right is most of the water bill, and most outfits from town get it wrong.</p>
<h2>The homestead zone strategy</h2>
<p>On acreage, landscaping every square foot is a money pit. Our Tumalo designs concentrate craft in a homestead zone around the house — outdoor rooms, native beds, lawn where kids and dogs actually play — then transition through windbreak plantings into managed pasture or left-natural juniper. It frames the Cascade views, cuts maintenance to a sane footprint, and reads like the property grew that way.</p>
""",
        "notes": ["Dual irrigation design: TID canal water + domestic well, each doing its job",
                  "Shelterbelt and windbreak planting for open benchland exposure",
                  "Horse-safe plant selection and fencing-aware layouts",
                  "View corridors to the Sisters preserved and framed, never blocked"],
        "near": ["bend", "sisters", "redmond"],
    },
    "sunriver": {
        "title": "Landscaping in Sunriver, OR | Sage & Stone Landscape Co.",
        "desc": "Sunriver landscaping that passes SROA design review: lodgepole-shade planting, durable hardscapes for rental homes, and firewise ladder-fuel management.",
        "h1": "Landscaping in Sunriver, Oregon",
        "lede": "A thousand feet closer to the frost, under lodgepole shade, with a design committee reviewing every change — Sunriver rewards contractors who've done the paperwork before. We have.",
        "facts": [("4,164 ft", "colder — frost in every month is real"), ("SROA", "design-review submittals handled"),
                  ("Rentals", "durability-first design for vacation homes"), ("25 min", "from our Bend shop")],
        "body": """
<h2>Built to pass review — and to survive renters</h2>
<p>Sunriver Owners Association design review has opinions about colors, materials, setbacks, and tree work, and the approval cycle can eat a season if you start it wrong. We prepare the submittal package as part of design and build to the letter of it. For rental homes we bias hard toward hardscape, boulder, and tough shrub structure: landscapes that look composed in listing photos and shrug off a different family every week.</p>
<h2>Cold-pocket planting under lodgepole</h2>
<p>Sunriver sits in a frost basin — snow lingers, cold air pools, and the growing season is measurably shorter than Bend's. Add dry lodgepole shade and sandy soil, and most nursery-catalog plants simply quit. Our Sunriver palette is built from what actually persists here: kinnikinnick, manzanita, currant, native sedges — plus ladder-fuel cleanup that keeps the lot firewise without clear-cutting the character.</p>
""",
        "notes": ["SROA design-review submittals prepared and managed for you",
                  "Frost-basin plant palette — proven at 4,100+ ft, not hoped-for",
                  "Durable hardscape-first design for vacation rental properties",
                  "Ladder-fuel reduction that keeps lodgepole character intact"],
        "near": ["la-pine", "bend"],
    },
    "la-pine": {
        "title": "Landscaping in La Pine, OR | Sage & Stone Landscape Co.",
        "desc": "La Pine landscaping for Oregon's coldest basin: zone 5 hardy natives, frost-proof hardscape construction, and well-and-septic-aware irrigation design.",
        "h1": "Landscaping in La Pine, Oregon",
        "lede": "La Pine's frost pockets are famously the coldest spots in Oregon — a zone colder than Bend, on sandier soil, with wells and septic in play. Plant lists that work in town die here, so ours don't come from town.",
        "facts": [("4,236 ft", "basin frost pockets — Oregon's coldest"), ("Zone 5", "a full zone hardier than Bend plans"),
                  ("Wells", "irrigation designed around pump capacity"), ("35 min", "from our Bend shop")],
        "body": """
<h2>A full zone colder changes everything</h2>
<p>Cold air drains off the Cascades and pools in the La Pine basin; growers here have recorded frost in July. We spec zone-4-and-5-proven plants — serviceberry, potentilla, native willows, tough conifers, bunchgrasses — and skip the borderline material entirely rather than warranty-replacing it every spring. Hardscape gets the same respect: deeper base sections and footings sized for real frost heave, because a patio that survives La Pine survives anywhere.</p>
<h2>Working with wells and septic</h2>
<p>Most La Pine properties run on a well and septic system, which puts hard limits on irrigation flow and where you can dig or plant. We design zones around your pump's actual capacity, keep thirsty planting near the house, and map the drainfield before the first line goes in — so the landscape never fights the infrastructure that makes the property work.</p>
""",
        "notes": ["Zone 5-proven plant palette — no optimistic borderline material",
                  "Frost-heave-rated base construction for patios and walls",
                  "Irrigation engineered to well pump capacity, zone by zone",
                  "Septic and drainfield mapped before any excavation"],
        "near": ["sunriver", "bend"],
    },
    "powell-butte": {
        "title": "Landscaping in Powell Butte, OR | Sage & Stone Landscape Co.",
        "desc": "Powell Butte landscaping for rimrock and juniper country: xeric-first design, wind-tough planting, ranch entries, and water-smart systems on well water.",
        "h1": "Landscaping in Powell Butte, Oregon",
        "lede": "Open rimrock views, juniper grassland, serious wind, and wells that meter every gallon — Powell Butte is the purest high-desert brief in our service area, and honestly one of our favorites.",
        "facts": [("3,200 ft", "open juniper-grassland bench"), ("Xeric-first", "designs assume limited well flow"),
                  ("Big wind", "structure and shelter planting lead"), ("30 min", "from our Bend shop")],
        "body": """
<h2>Xeric-first isn't a compromise here</h2>
<p>Many Powell Butte wells produce just enough for the house, which makes a thirsty landscape a genuine liability. Our designs start from near-zero irrigation: native bunchgrass matrices, rabbitbrush and sage structure, boulder and rimrock work that borrows the site's own geology, and drip only where it buys real beauty near the house. Done right, it looks like Brasada Ranch — because that's the same country.</p>
<h2>Entries, drives, and shelter</h2>
<p>On five-to-forty-acre parcels, the landscape people actually experience is the entry sequence: the gate, the drive, the approach to the house. We design ranch entries that read from a quarter mile — stone monuments, steel, allée planting where water allows — and place windbreaks so the outdoor living zones sit in calm air while the views stay wide open.</p>
""",
        "notes": ["Near-zero-irrigation native design matched to well capacity",
                  "Ranch entry and driveway design that anchors the whole parcel",
                  "Wind-sheltered outdoor rooms without blocking rimrock views",
                  "Juniper management that opens views and reduces fuel load"],
        "near": ["redmond", "prineville"],
    },
    "prineville": {
        "title": "Landscaping in Prineville, OR | Sage & Stone Landscape Co.",
        "desc": "Prineville landscaping: lawn renovations, irrigation rebuilds, and heat-tough planting for Crooked River valley soils. Licensed Central Oregon design-build crew.",
        "h1": "Landscaping in Prineville, Oregon",
        "lede": "The lowest, warmest corner of our service area grows differently: real soil in the river valley, hotter summers, and a lot of good older landscapes that mostly need honest renovation, not demolition.",
        "facts": [("2,868 ft", "lowest, warmest town we serve"), ("River soil", "clay-loam — a different playbook than pumice"),
                  ("Renovation", "many projects revive, not replace"), ("40 min", "from our Bend shop")],
        "body": """
<h2>Valley soil is an asset — treat it like one</h2>
<p>Unlike Bend's pumice, the Crooked River valley holds genuine clay-loam that stores water and grows almost anything — it just drains slowly and compacts hard. We amend for structure instead of fertility, size drainage for spring saturation, and take advantage of the warmth: Prineville summers ripen a planting palette that the rest of Central Oregon envies.</p>
<h2>Renovation is Prineville's best value</h2>
<p>Many Prineville properties have mature trees and established lawns worth keeping — what's failed is usually the forty-year-old irrigation underneath. Our most common projects here are system rebuilds with smart controllers, lawn renovations that keep the turf where it earns its water, and refreshed foundation beds that bring an older home's landscape back to proud. It's the least expensive transformation we do anywhere.</p>
""",
        "notes": ["Clay-loam soil strategy: structure amendment and real drainage",
                  "Irrigation system rebuilds with head-by-head efficiency audits",
                  "Lawn renovation and reduction — keep what earns its water",
                  "Heat-tolerant planting the warmer valley supports"],
        "near": ["powell-butte", "redmond"],
    },
}


def body(slug):
    a = AREAS[slug]
    facts = "\n".join(f'<div class="fact-lt"><b>{v}</b><span>{s}</span></div>' for v, s in a["facts"])
    notes = "\n".join(f"<li>{ICON_CHECK}<span>{n}</span></li>" for n in a["notes"])
    near = "\n".join(
        f'<li><a href="{s}.html">Landscaping in {NAME[s]} {ARR}</a></li>' for s in a["near"]
    )
    return f'''
<main id="main">
<div class="wrap crumbs">
  <nav aria-label="Breadcrumb">
    <ol>
      <li><a href="../index.html">Home</a></li>
      <li><a href="../index.html#areas">Service Areas</a></li>
      <li aria-current="page">{NAME[slug]}</li>
    </ol>
  </nav>
</div>
<section class="wrap page-hero">
  <p class="eyebrow">Serving {NAME[slug]}, Oregon</p>
  <h1>{a['h1']}</h1>
  <p class="lede">{a['lede']}</p>
  <div class="facts rv">
    {facts}
  </div>
</section>
<section class="sec">
  <div class="wrap split">
    <div class="prose rv">
      {a['body']}
      <h2>How we work in {NAME[slug]}</h2>
      <ul class="checks">{notes}</ul>
      <p style="margin-top:1.6rem">Every project starts the same way: a free site walk, straight talk about budget, and a fixed line-item estimate. See our full services — <a href="../services/landscape-design-build.html">design &amp; build</a>, <a href="../services/hardscaping-outdoor-living.html">hardscaping</a>, <a href="../services/water-wise-irrigation.html">irrigation</a>, and <a href="../services/landscape-maintenance.html">maintenance</a> — all available in {NAME[slug]}.</p>
    </div>
    <aside>
      <div class="side-card rv">
        <h3 class="serif">Book a free {NAME[slug]} site walk</h3>
        <p style="color:var(--ink-soft);font-size:.97rem">We're in the area on regular routes — scheduling a walk is easy.</p>
        <a class="btn btn-primary" href="../index.html#quote">Request my site walk {ARR}</a>
        <a class="btn btn-ghost" href="tel:{SITE['phone_tel']}">Call {SITE['phone_display']}</a>
        <hr>
        <img src="../assets/img/map-central-oregon.webp" alt="Map of the Sage &amp; Stone service area across Central Oregon" width="1120" height="940" loading="lazy" style="border-radius:12px">
        <hr>
        <h4 style="margin:0 0 .8rem;font-family:var(--serif);font-weight:500">Nearby areas</h4>
        <ul class="side-links">{near}</ul>
      </div>
    </aside>
  </div>
</section>
<section class="cta-band">
  <div class="wrap cta-in">
    <h2 class="rv">Let's walk your {NAME[slug]} property together.</h2>
    <a class="btn btn-ghost on-dark rv" href="../index.html#quote">Book a free site walk {ARR}</a>
  </div>
</section>
</main>
'''
