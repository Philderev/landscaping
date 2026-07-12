# Privacy policy, terms of service, and thank-you page bodies.
from parts import SITE, ARR

EFFECTIVE = "July 9, 2026"

PRIVACY = f'''
<main id="main">
<section class="sec">
  <div class="wrap legal">
    <p class="eyebrow">Legal</p>
    <h1>Privacy Policy</h1>
    <p class="updated">Effective {EFFECTIVE} · {SITE['name']}, {SITE['street']}, {SITE['city']}, {SITE['region']} {SITE['zip']}</p>

    <h2>The short version</h2>
    <p>We collect the information you send us so we can call you back about your project, and basic analytics (only if you allow them) so we can tell which pages are useful. We don't sell data, we don't run ad tracking, and declining cookies doesn't break anything.</p>

    <h2>Information you give us</h2>
    <p>When you submit our quote form, call, text, or email, we receive what you share: your name, phone number, email address, and details about your property and project. We use it to respond to your inquiry, schedule site walks, prepare estimates, and manage your project. We keep project records for as long as we're required to for warranty, tax, and licensing purposes.</p>

    <h2>Cookies and analytics</h2>
    <p>With your consent (the banner you saw when you arrived), we use basic analytics cookies - such as Google Analytics - to understand things like which pages get visited and how people find us. These tools receive technical data such as pages viewed, approximate region, browser, and device type. If you decline, no analytics cookies are set and the site works exactly the same. You can change your mind anytime by clearing this site's data in your browser, which resets the banner.</p>

    <h2>Third-party services</h2>
    <p>Our lead form, scheduling, and messaging are handled through our customer-management platform, which processes your contact details on our behalf. If we run advertising campaigns, ad platforms may set their own cookies only where you've consented. We choose vendors that contractually limit use of your data to providing services to us.</p>

    <h2>What we don't do</h2>
    <ul>
      <li>We don't sell or rent your personal information - to anyone, ever.</li>
      <li>We don't send marketing email unless you asked for it.</li>
      <li>We don't collect more than we need to run a landscaping business well.</li>
    </ul>

    <h2>Your choices and rights</h2>
    <p>You can ask us what information we hold about you, ask us to correct it, or ask us to delete it (we may need to keep records the law requires, like invoices). Email <a href="mailto:{SITE['email']}">{SITE['email']}</a> or call <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a> and a real person will handle it.</p>

    <h2>Children</h2>
    <p>Our site and services are for adults; we don't knowingly collect information from children under 13.</p>

    <h2>Changes</h2>
    <p>If we change this policy, we'll update the date at the top. Meaningful changes get a plain-language note here, not buried legalese.</p>

    <h2>Contact</h2>
    <p>{SITE['name']}<br>{SITE['street']}, {SITE['city']}, {SITE['region']} {SITE['zip']}<br><a href="mailto:{SITE['email']}">{SITE['email']}</a> · <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></p>
  </div>
</section>
</main>
'''

TERMS = f'''
<main id="main">
<section class="sec">
  <div class="wrap legal">
    <p class="eyebrow">Legal</p>
    <h1>Terms of Service</h1>
    <p class="updated">Effective {EFFECTIVE} · {SITE['name']}, Oregon {SITE['lcb']} · {SITE['ccb']}</p>

    <h2>Using this website</h2>
    <p>This site describes our landscaping services in Central Oregon. You're welcome to browse, share, and print pages for personal use. The content, photography, illustrations, and branding are ours - please don't reuse them commercially without written permission.</p>

    <h2>Estimates and proposals</h2>
    <p>Prices and "starting at" figures on this site are honest ballparks, not offers. Binding pricing comes only from a written, line-item estimate after a site walk. Written estimates are valid for 30 days; if hidden conditions surface during work (buried concrete, undocumented utilities, caliche where the soil report said loam), we'll pause, show you, and agree on any change in writing before proceeding.</p>

    <h2>Scheduling and weather</h2>
    <p>Build dates are scheduled in good faith around Central Oregon weather. Frozen ground, smoke days, and safety-related delays can shift schedules; we communicate early and reschedule promptly. Neither party is liable for delays caused by events beyond reasonable control.</p>

    <h2>Warranty</h2>
    <p>We warrant our hardscape workmanship through two full seasons (one complete freeze-thaw cycle) and plantings through their establishment terms as described in your project agreement. The warranty covers our workmanship and materials; it doesn't cover damage from third parties, unmaintained irrigation, animals, or acts of nature. Warranty claims: call or email us - we respond within two business days.</p>

    <h2>Payments</h2>
    <p>Projects follow the payment schedule in your agreement - typically a deposit to secure scheduling and materials, progress payments at defined milestones, and final payment at walkthrough. We never ask for full payment up front.</p>

    <h2>Licensing and insurance</h2>
    <p>{SITE['name']} is licensed with the Oregon Landscape Contractors Board ({SITE['lcb']}) and Construction Contractors Board ({SITE['ccb']}), bonded, and insured. Verification is available on request or through the state's license lookup tools.</p>

    <h2>Liability</h2>
    <p>To the extent permitted by Oregon law, our total liability related to this website is limited to the amount you paid to use it (the site is free, so: zero), and liability related to services is governed by your project agreement. Nothing in these terms limits rights that Oregon consumer law grants you.</p>

    <h2>Governing law</h2>
    <p>These terms are governed by the laws of the State of Oregon. Any dispute will be resolved in the courts of Deschutes County, Oregon.</p>

    <h2>Questions</h2>
    <p>Email <a href="mailto:{SITE['email']}">{SITE['email']}</a> - we'd rather clarify up front than argue later.</p>
  </div>
</section>
</main>
'''

THANKS = f'''
<main id="main">
<section class="wrap thanks">
  <div>
    <div class="thanks-ic">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9.55 17.05-5.3-5.3 1.4-1.4 3.9 3.9 8.8-8.8 1.4 1.4Z"/></svg>
    </div>
    <p class="eyebrow" style="justify-content:center">Request received</p>
    <h1 style="max-width:18ch;margin-inline:auto">Got it - your site walk request is in.</h1>
    <p class="lede" style="margin-inline:auto">Here's exactly what happens next:</p>
    <ol>
      <li>A real person at Sage &amp; Stone reads your note - today if it's a weekday.</li>
      <li>We call you within one business day for a quick chat about scope and timing.</li>
      <li>We schedule your free site walk - most happen within the week.</li>
    </ol>
    <p style="margin-bottom:2rem">Need us sooner? Call <a href="tel:{SITE['phone_tel']}"><strong>{SITE['phone_display']}</strong></a> - Mon-Fri 7am-5pm, Sat 8am-1pm.</p>
    <p>
      <a class="btn btn-primary" href="index.html">Back to the homepage {ARR}</a>
    </p>
  </div>
</section>
</main>
'''
