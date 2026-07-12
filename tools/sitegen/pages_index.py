# Homepage body content.
from parts import SITE, AREA_PAGES, ICON_PIN, ICON_PHONE, ICON_MAIL, ICON_CLOCK, ICON_CHECK, STAR, ARR, SQUIGGLE, CONTOURS, lazy_img

R = ""  # root prefix for index

SERVICES = [
    {
        "slug": "landscape-design-build",
        "name": "Landscape Design &amp; Build",
        "img": "svc-design.webp",
        "alt": "Landscape designer pointing at a color site plan on a laptop, concept drawings spread on the desk",
        "blurb": "From the first site walk to the final walkthrough - native planting plans, boulder placement, and outdoor rooms designed around how you actually live.",
    },
    {
        "slug": "hardscaping-outdoor-living",
        "name": "Hardscaping &amp; Outdoor Living",
        "img": "svc-hardscape.webp",
        "alt": "Paver patio with a stone fire pit, seat walls and Adirondack chairs behind a brick home",
        "blurb": "Paver patios, basalt fire pits, retaining walls, and pergolas - built on proper base so they hold their line through every freeze and thaw.",
    },
    {
        "slug": "water-wise-irrigation",
        "name": "Water-Wise Irrigation",
        "img": "svc-irrigation.webp",
        "alt": "Irrigation sprinkler watering a green lawn with backlit water droplets catching the sun",
        "blurb": "Drip zones, smart controllers, and hydrozoning that keep landscapes thriving on a high-desert water budget - not in spite of it.",
    },
    {
        "slug": "landscape-maintenance",
        "name": "Year-Round Maintenance",
        "img": "svc-maintenance.webp",
        "alt": "Gardener shaping a shrub with long-handled hedge shears",
        "blurb": "Seasonal pruning, fertility programs, fall blowouts, and spring start-ups - from crews who know bitterbrush from bindweed.",
    },
]

REVIEWS = [
    ("Marta &amp; Dan K.", "NorthWest Crossing, Bend", "3 weeks ago",
     "They tore out a thirsty lawn we fought for a decade and gave us a meadow of fescue and penstemon that looks better in August than the lawn ever did in June. Our water bill dropped by almost half."),
    ("Craig B.", "Tumalo", "1 month ago",
     "Three companies told us our slope couldn't hold a patio. Sage &amp; Stone built a basalt terrace with a fire court that hasn't moved a millimeter through two winters. Worth every dollar."),
    ("Alison R.", "Sisters", "6 weeks ago",
     "The crew was on time every single morning, tarped everything, and swept the street before they left. The design still stops neighbors on their evening walks."),
    ("Priya &amp; Tom S.", "Awbrey Butte, Bend", "2 months ago",
     "We wanted low-water without it looking like a gravel pit. What we got is layered, full of birds, and basically ignores the deer. The maintenance plan keeps it dialed."),
    ("Jeff M.", "Sunriver", "5 days ago",
     "Their irrigation rebuild found leaks two other outfits missed. The smart controller paid for itself the first season - and the lawn we kept is the healthiest it's ever been."),
]

FAQS = [
    ("What does a full landscape project cost in Bend?",
     "Most full design-build projects at Sage &amp; Stone land between $25,000 and $120,000 depending on size and scope. Paver patios typically start around $8,500, water-wise planting conversions around $12,000, and irrigation rebuilds around $4,500. After a site walk you get a fixed, line-item estimate - not an hourly guess."),
    ("How does the high desert change what you plant?",
     "Bend sits at 3,600&nbsp;ft with about 12 inches of rain a year, USDA zone 6b, and frost possible any month. We build plant palettes around natives and proven adapters - bunchgrasses, penstemon, rabbitbrush, serviceberry, ponderosa - and group them by water need so irrigation supports the landscape instead of fighting it."),
    ("Will my landscape survive the deer?",
     "Mostly, yes - by design. We lean on deer-resistant natives, protect vulnerable young plants through their first seasons, and place anything tasty inside fenced or courtyard zones. No honest landscaper promises deer-proof; we design deer-realistic."),
    ("When should I book to get on the schedule?",
     "Design work happens year-round, and winter is actually the best time to start - your project is drawn, permitted, and first in line when the ground thaws. Build season runs roughly April through November, and the calendar usually fills by early spring."),
    ("Do you handle irrigation blowouts and spring start-ups?",
     "Yes. Maintenance clients get fall blowouts before the first hard freeze and full spring start-ups with head-by-head checks, controller programming, and a written condition report."),
    ("Are you licensed and insured?",
     "Fully. Oregon Landscape Contractors Board {lcb} and {ccb}, bonded and insured, with a two-season craftsmanship warranty on everything we build.".format(lcb=SITE["lcb"], ccb=SITE["ccb"])),
]


def _svc_cards():
    out = []
    for s in SERVICES:
        out.append(f'''<a class="svc-card rv" href="services/{s['slug']}.html">
  <div class="svc-art">{lazy_img(f"assets/img/{s['img']}", s['alt'], 960, 570)}</div>
  <div class="svc-body">
    <h3>{s['name']}</h3>
    <p>{s['blurb']}</p>
    <span class="svc-more">Explore the service {ARR}</span>
  </div>
</a>''')
    return "\n".join(out)


def _reviews():
    out = []
    stars = f'<div class="stars" role="img" aria-label="5 out of 5 stars">{STAR * 5}</div>'
    google_url = "https://www.google.com/maps?q=" + SITE["street"].replace(" ", "+") + f",+{SITE['city']},+{SITE['region']}+{SITE['zip']}"
    for name, place, when, text in REVIEWS:
        initial = name[0]
        out.append(f'''<article class="review">
  <div class="review-top">
    <div class="review-avatar" aria-hidden="true">{initial}</div>
    <div>
      <b>{name}</b>
      <span class="review-when">{when} &middot; {place}</span>
    </div>
  </div>
  {stars}
  <p>{text}</p>
  <footer>
    <span>Posted on Google</span>
    <a href="{google_url}" target="_blank" rel="noopener">Read on Google</a>
  </footer>
</article>''')
    return "\n".join(out)


def _faq():
    out = []
    for q, a in FAQS:
        out.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    return "\n".join(out)


def _marquee():
    towns = SITE["areas"] + ["Central Oregon since 2012"]
    items = "".join(f"<li>{t}</li>" for t in towns)
    return f'''<div class="marquee">
  <div class="wrap">
    <div class="marq-clip">
      <div class="marq-track">
        <ul>{items}</ul>
        <ul aria-hidden="true">{items}</ul>
      </div>
    </div>
  </div>
</div>'''


BODY = f'''
<main id="main">
<section class="hero">
  <div class="hero-media">
    <video muted loop playsinline preload="none" width="1920" height="1080"
      poster="assets/video/hero-poster.webp" aria-hidden="true" tabindex="-1"
      disablepictureinpicture>
      <source data-src="assets/video/hero.webm" type="video/webm">
      <source data-src="assets/video/hero.mp4" type="video/mp4">
    </video>
  </div>
  <div class="wrap hero-in">
    <div class="hero-grid">
      <div class="hero-copy">
        <p class="eyebrow on-dark">Bend · Sisters · Redmond - Central Oregon</p>
        <h1>Landscapes that belong to the <em>high desert{SQUIGGLE}</em></h1>
        <p class="lede">Design-build landscaping made for 3,600&nbsp;ft: native planting, basalt hardscapes, and water-wise irrigation that thrive on volcanic soil, cold nights, and 300 days of sun.</p>
        <div class="hero-cta"><a class="btn btn-ghost on-dark" href="#services">See our services</a></div>
      </div>
      <form class="hero-form" action="#" method="post" aria-labelledby="hero-form-title">
        <p class="eyebrow on-dark">Free site walk</p>
        <h2 id="hero-form-title">Start your landscape plan</h2>
        <div class="field"><label for="hero-name">Name</label><input id="hero-name" name="name" type="text" autocomplete="name" required></div>
        <div class="field"><label for="hero-phone">Phone</label><input id="hero-phone" name="phone" type="tel" autocomplete="tel" required></div>
        <div class="field"><label for="hero-email">Email</label><input id="hero-email" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="hero-service">What do you need?</label><select id="hero-service" name="service" required><option value="" selected disabled>Select a service</option><option value="design-build">Design &amp; build</option><option value="hardscape">Patio or hardscape</option><option value="irrigation">Irrigation</option><option value="maintenance">Maintenance</option><option value="not-sure">Not sure yet</option></select></div>
        <label class="sms-consent" for="hero-sms-consent">
          <input id="hero-sms-consent" name="sms_consent" type="checkbox" value="yes">
          <span>I consent to receive SMS notifications, alerts, and occasional marketing communications from {SITE['short']}. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe at any time.</span>
        </label>
        <button class="btn btn-primary" type="submit">Request my site walk {ARR}</button>
        <p class="hero-form-note">No pressure. We reply within one business day.</p>
        <p class="form-legal"><a href="privacy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="terms.html">Terms of Service</a></p>
      </form>
    </div>
    <div class="hero-foot">
      <div class="hero-stats">
        <div class="stat"><b>14&nbsp;yrs</b><span>rooted in Bend</span></div>
        <div class="stat"><b>480+</b><span>projects built</span></div>
        <div class="stat"><b>2-season</b><span>craftsmanship warranty</span></div>
        <a class="scroll-cue" href="#services">Scroll
          <svg width="14" height="18" viewBox="0 0 14 18" aria-hidden="true"><path d="M7 1v14m0 0 5-5M7 15l-5-5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
      </div>
    </div>
  </div>
</section>

{_marquee()}

<section class="sec" id="services" aria-labelledby="services-h">
  <div class="wrap">
    <div class="sec-head rv">
      <p class="eyebrow">What we do</p>
      <h2 id="services-h">Four crafts, one crew, zero hand-offs</h2>
      <p class="lede">Design, stone, water, and care under one roof - so the person who drew your landscape is the same company standing behind it ten years on.</p>
    </div>
    <div class="svc-grid">
      {_svc_cards()}
    </div>
  </div>
</section>

<section class="sec dark" id="about" aria-labelledby="about-h">
  {CONTOURS}
  <div class="wrap manif">
    <div class="manif-copy rv">
      <p class="eyebrow on-dark">Why the high desert is different</p>
      <h2 id="about-h">The high desert doesn't forgive a copy-paste landscape</h2>
      <p>Plans drawn for Portland rot here. Twelve inches of rain, pumice soil that drains like a sieve, weeks of 90° sun, and a frost that can land in any month - Central Oregon breaks landscapes that weren't designed for it.</p>
      <p>We've spent fourteen years learning what holds: basalt and Deschutes river rock that shrug off frost heave, bunchgrass and penstemon that glow in August without a sprinkler line, ponderosa shade placed where winter sun still reaches the windows.</p>
      <p>That's the whole philosophy - <strong>build with the desert, not against it</strong> - and it's why our landscapes look better in year five than they did on day one.</p>
    </div>
    <div class="fact-grid rv">
      <div class="fact"><b>3,623&nbsp;ft</b><span>Bend's elevation - cold nights, intense UV, short growing season</span></div>
      <div class="fact"><b>~12&nbsp;in</b><span>annual precipitation - half of it snow. Every drop is budgeted</span></div>
      <div class="fact"><b>Zone&nbsp;6b</b><span>USDA hardiness - with frost possible in every calendar month</span></div>
      <div class="fact"><b>300</b><span>days of sun a year working for you - if the plant palette is right</span></div>
    </div>
  </div>
</section>

<section class="sec" id="process" aria-labelledby="process-h">
  <div class="wrap">
    <div class="sec-head rv">
      <p class="eyebrow">How it works</p>
      <h2 id="process-h">A straight line from idea to landscape</h2>
    </div>
    <div class="steps">
      <div class="step rv">
        <h3>The site walk</h3>
        <p>We walk your property together - sun, wind, soil, drainage, deer paths - and listen to how you want to live outside. Free, no folder of upsells.</p>
      </div>
      <div class="step rv">
        <h3>Design &amp; fixed estimate</h3>
        <p>Scaled plan, plant palette, materials, and a line-item price that holds. You'll know exactly what's being built and what it costs.</p>
      </div>
      <div class="step rv">
        <h3>The build</h3>
        <p>One dedicated crew, a posted schedule, a tidy site every evening, and a foreman who calls you before questions become surprises.</p>
      </div>
      <div class="step rv">
        <h3>Seasons of care</h3>
        <p>Walkthrough, plant-by-plant care guide, two-season warranty - and a maintenance calendar if you'd rather we keep it dialed.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="work" aria-labelledby="work-h" style="background:var(--sand-2)">
  <div class="wrap">
    <div class="sec-head rv">
      <p class="eyebrow">Signature work</p>
      <h2 id="work-h">Built here, for here</h2>
      <p class="lede">A few recent projects across Central Oregon - each one drawn from the lot's own rock, light, and horizon.</p>
    </div>
    <div class="proj-grid">
      <article class="proj rv">
        {lazy_img("assets/img/proj-firecourt.webp", "Evening patio with a round stone fire pit, curved outdoor seating and Adirondack chairs under pines", 960, 720)}
        <div class="proj-body">
          <h3>Shevlin Ridge Fire Court</h3>
          <p>A sloped, unusable back lot became a two-level basalt terrace with a gas fire bowl and unbroken Cascade views.</p>
          <ul class="tags"><li>Hardscape</li><li>Design-build</li><li>Bend</li></ul>
        </div>
      </article>
      <article class="proj rv">
        {lazy_img("assets/img/proj-meadow.webp", "Meadow planting in bloom with pink cosmos, cornflowers and coreopsis among fine grasses", 960, 720)}
        <div class="proj-body">
          <h3>Sisters Meadow Revival</h3>
          <p>Half an acre of thirsty turf replaced with fescue meadow, penstemon drifts, and a decomposed-granite path - water use down 60%.</p>
          <ul class="tags"><li>Native planting</li><li>Irrigation</li><li>Sisters</li></ul>
        </div>
      </article>
      <article class="proj rv">
        {lazy_img("assets/img/proj-courtyard.webp", "Modern courtyard with a steel pergola, wood deck and concrete dining table beside clipped hedges", 960, 720)}
        <div class="proj-body">
          <h3>Old Mill Courtyard</h3>
          <p>A narrow townhome yard turned into a private courtyard: porcelain pavers, a basalt-column bubbler, and evening lighting.</p>
          <ul class="tags"><li>Courtyard</li><li>Lighting</li><li>Bend</li></ul>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="sec" id="reviews" aria-labelledby="reviews-h">
  <div class="sec-head center wrap rv">
    <p class="eyebrow">Word of mouth</p>
    <h2 id="reviews-h">What neighbors say</h2>
  </div>
  <div class="reviews">
    {_reviews()}
  </div>
</section>

<section class="sec" id="areas" aria-labelledby="areas-h" style="background:var(--sand-2)">
  <div class="wrap areas">
    <div class="rv">
      <p class="eyebrow">Where we work</p>
      <h2 id="areas-h">Serving Central Oregon's high desert</h2>
      <p class="lede">Based on Bend's west side, our crews run daily routes from La Pine to Prineville. If you can see the Sisters from your driveway, you're probably in our service area.</p>
      <ul class="area-list">
        {"".join(f'<li>{ICON_PIN}<a href="areas/{s}.html">{n}</a></li>' for s, n in AREA_PAGES)}
      </ul>
    </div>
    <div class="map-card rv">
      <iframe class="live-map" title="Map showing Sage &amp; Stone Landscape Co. in Bend, Oregon" src="https://www.google.com/maps?q=20310+Empire+Ave,+Suite+E4,+Bend,+OR+97703&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
    </div>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-h">
  <div class="wrap">
    <div class="sec-head center rv">
      <p class="eyebrow">Good to know</p>
      <h2 id="faq-h">Questions we hear on every site walk</h2>
    </div>
    <div class="faq rv">
      {_faq()}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap cta-in">
    <h2 class="rv">Your lot already knows what it wants to be.</h2>
    <a class="btn btn-ghost on-dark rv" href="#quote">Book a free site walk {ARR}</a>
  </div>
</section>

<section class="sec" id="quote" aria-labelledby="quote-h">
  <div class="wrap contact-grid">
    <div class="rv">
      <p class="eyebrow">Free site walk &amp; estimate</p>
      <h2 id="quote-h">Tell us about your yard</h2>
      <p class="lede">A few details and we'll call you within one business day to set up a site walk. No pressure, no boilerplate bids.</p>
      <!-- Lead capture: swap this form for the client's GHL form embed at launch.
           Keep the same field names so tracking stays consistent. -->
      <form id="lead-form" action="#" method="post" novalidate>
        <div class="field-row">
          <div class="field">
            <label for="f-name">Name</label>
            <input id="f-name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="f-phone">Phone</label>
            <input id="f-phone" name="phone" type="tel" autocomplete="tel" required>
          </div>
        </div>
        <div class="field">
          <label for="f-email">Email</label>
          <input id="f-email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="f-service">What do you need?</label>
          <select id="f-service" name="service" required>
            <option value="" selected disabled>Select a service</option>
            <option value="design-build">Design &amp; build</option>
            <option value="hardscape">Patio or hardscape</option>
            <option value="irrigation">Irrigation</option>
            <option value="maintenance">Maintenance</option>
            <option value="not-sure">Not sure yet</option>
          </select>
        </div>
        <div class="field">
          <label for="f-msg">Tell us about the project</label>
          <textarea id="f-msg" name="message" placeholder="Lot size, what's there now, what you're dreaming about…"></textarea>
        </div>
        <label class="sms-consent" for="f-sms-consent">
          <input id="f-sms-consent" name="sms_consent" type="checkbox" value="yes">
          <span>I consent to receive SMS notifications, alerts, and occasional marketing communications from {SITE['short']}. Message frequency varies. Message and data rates may apply. Reply STOP to unsubscribe at any time.</span>
        </label>
        <div class="form-actions">
          <button class="btn btn-primary" type="submit">Request my site walk {ARR}</button>
          <p class="form-legal"><a href="privacy.html">Privacy Policy</a><span aria-hidden="true"> | </span><a href="terms.html">Terms of Service</a></p>
        </div>
      </form>
    </div>
    <aside class="info-card rv" aria-label="Contact details">
      <h3>Sage &amp; Stone Landscape Co.</h3>
      <div class="info-line">{ICON_PIN}<span>{SITE['street']}<br>{SITE['city']}, {SITE['region']} {SITE['zip']}</span></div>
      <div class="info-line">{ICON_PHONE}<a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></div>
      <div class="info-line">{ICON_MAIL}<a href="mailto:{SITE['email']}">{SITE['email']}</a></div>
      <div class="info-line">{ICON_CLOCK}
        <table class="hours">
          <caption class="skip">Business hours</caption>
          <tr><td>Monday-Friday</td><td>7:00am - 5:00pm</td></tr>
          <tr><td>Saturday</td><td>8:00am - 1:00pm</td></tr>
          <tr><td>Sunday</td><td>Closed</td></tr>
        </table>
      </div>
      <div class="info-line">{ICON_CHECK}<span>Oregon {SITE['lcb']} · {SITE['ccb']}<br>Licensed, bonded &amp; insured</span></div>
    </aside>
  </div>
</section>
</main>
'''
