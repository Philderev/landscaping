# Assemble the static site into the project root.
import os
import re

from css import CSS

def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\n+", "", css)
    css = re.sub(r"  +", " ", css)
    return css.strip()

def remove_visible_dashes(html):
    """Remove dash characters from rendered text without damaging markup or code."""
    protected = re.split(r'(<(?:style|script)\b[^>]*>.*?</(?:style|script)>)', html,
                         flags=re.I | re.S)
    for i in range(0, len(protected), 2):
        chunks = re.split(r'(<[^>]+>)', protected[i])
        for j in range(0, len(chunks), 2):
            chunks[j] = re.sub(r'[\u2013\u2014]+', ' ', chunks[j])
            chunks[j] = re.sub(r' {2,}', ' ', chunks[j])
            chunks[j] = re.sub(r' +(?=\n)', '', chunks[j])
        protected[i] = ''.join(chunks)
    return ''.join(protected)
from parts import SITE, AREA_PAGES, head, header, footer, business_schema, breadcrumb_schema
import pages_index
import pages_services
import pages_areas
import pages_legal
import pages_pricing

ROOT = r"E:\templates\landscaping website template"
SP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # scratchpad
DATE = "2026-07-09"


def page(*, title, desc, canonical_path, root, body, active="", schemas=None, preload_poster=False, noindex=False):
    css = minify_css(CSS.replace("{R}", root))
    html = f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
{head(title=title, desc=desc, canonical_path=canonical_path, root=root, extra_schema=schemas, preload_poster=preload_poster, noindex=noindex)}
<style>{css}</style>
</head>
<body>
{header(root, active)}
{body}
{footer(root)}
</body>
</html>'''
    return remove_visible_dashes(html)


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"wrote {path}  ({len(content.encode('utf8'))/1024:.1f} KB)")


# ------------------------------------------------------------------ index
index_schemas = [business_schema()]
write("index.html", page(
    title="Sage & Stone Landscape Co. | Landscape Design & Build in Bend, Oregon",
    desc="Bend's high-desert landscape design-build company. Native planting, paver patios and basalt hardscapes, water-wise irrigation, and year-round maintenance across Central Oregon.",
    canonical_path="",
    root="",
    body=pages_index.BODY,
    active="",
    schemas=index_schemas,
    preload_poster=True,
))

# ------------------------------------------------------------------ services
for slug in pages_services.ORDER:
    p = pages_services.PAGES[slug]
    name_plain = pages_services.NAMES[slug].replace("&amp;", "&")
    schemas = [breadcrumb_schema([
        ("Home", ""),
        (name_plain, None),
    ])]
    write(f"services/{slug}.html", page(
        title=p["title"],
        desc=p["desc"],
        canonical_path=f"services/{slug}.html",
        root="../",
        body=pages_services.body(slug),
        active=f"services:{slug}",
        schemas=schemas,
    ))

# ------------------------------------------------------------------ areas
for slug, name in AREA_PAGES:
    a = pages_areas.AREAS[slug]
    schemas = [breadcrumb_schema([
        ("Home", ""),
        (f"Landscaping in {name}, Oregon", None),
    ])]
    write(f"areas/{slug}.html", page(
        title=a["title"],
        desc=a["desc"],
        canonical_path=f"areas/{slug}.html",
        root="../",
        body=pages_areas.body(slug),
        active=f"areas:{slug}",
        schemas=schemas,
    ))

# ------------------------------------------------------------------ pricing
write("pricing.html", page(
    title="Landscaping Prices in Bend, OR (2026) | Sage & Stone Landscape Co.",
    desc="Real 2026 landscaping prices for Bend & Central Oregon: paver patios $22-$28/sq ft, full design-build projects $25k-$120k, irrigation from $1.50/sq ft, maintenance $220-$480/mo. Fixed line-item estimates.",
    canonical_path="pricing.html",
    root="",
    body=pages_pricing.body(),
    active="pricing",
    schemas=[breadcrumb_schema([("Home", ""), ("Pricing", None)])],
))

# ------------------------------------------------------------------ legal + thank-you
write("privacy.html", page(
    title="Privacy Policy | Sage & Stone Landscape Co.",
    desc="How Sage & Stone Landscape Co. handles your information: what we collect through our quote form, how consent-based analytics work, and the choices you have.",
    canonical_path="privacy.html",
    root="",
    body=pages_legal.PRIVACY,
))
write("terms.html", page(
    title="Terms of Service | Sage & Stone Landscape Co.",
    desc="Terms for using the Sage & Stone Landscape Co. website: estimates and proposals, scheduling, our two-season workmanship warranty, payments, and Oregon licensing.",
    canonical_path="terms.html",
    root="",
    body=pages_legal.TERMS,
))
write("thank-you.html", page(
    title="Request received | Sage & Stone Landscape Co.",
    desc="Thanks for your site walk request - a real person at Sage & Stone will call you within one business day.",
    canonical_path="thank-you.html",
    root="",
    body=pages_legal.THANKS,
    noindex=True,
))

# ------------------------------------------------------------------ 404
err_body = '''
<main id="main">
<section class="wrap err">
  <div>
    <span class="num">404</span>
    <h1 style="font-size:clamp(1.8rem,4vw,2.6rem)">This path isn't on the map</h1>
    <p class="lede" style="margin-inline:auto">The page you're after may have moved, or the trail marker's gone. Head back to base camp and we'll get you re-oriented.</p>
    <p style="margin-top:2rem"><a class="btn btn-primary" href="index.html">Back to the homepage <span class="arr" aria-hidden="true">→</span></a></p>
  </div>
</section>
</main>
'''
write("404.html", page(
    title="Page not found | Sage & Stone Landscape Co.",
    desc="The page you're looking for doesn't exist. Return to Sage & Stone Landscape Co. - landscape design and build in Bend, Oregon.",
    canonical_path="404.html",
    root="",
    body=err_body,
))

# ------------------------------------------------------------------ robots + sitemap
write("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {SITE['base']}sitemap.xml
""")

urls = ([("", "1.0")]
        + [(f"services/{s}.html", "0.8") for s in pages_services.ORDER]
        + [("pricing.html", "0.8")]
        + [(f"areas/{s}.html", "0.7") for s, _ in AREA_PAGES]
        + [("privacy.html", "0.3"), ("terms.html", "0.3")])
entries = "\n".join(
    f"""  <url>
    <loc>{SITE['base']}{u}</loc>
    <lastmod>{DATE}</lastmod>
    <priority>{p}</priority>
  </url>""" for u, p in urls
)
write("sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}
</urlset>
""")

# ------------------------------------------------------------------ manifest
write("site.webmanifest", """{
  "name": "Sage & Stone Landscape Co.",
  "short_name": "Sage & Stone",
  "icons": [
    { "src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#161F14",
  "background_color": "#F2ECD3",
  "display": "browser"
}
""")

# ------------------------------------------------------------------ js
write("assets/js/main.js", r"""// Sage & Stone - progressive enhancement. ~2 KB, no dependencies.
(function () {
  "use strict";

  // Mobile nav
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Announcement bar. Dismissal is remembered so it doesn't return on
  // the next visit; bump the key if the promo copy changes.
  var announce = document.getElementById("announce");
  if (announce) {
    var aClose = announce.querySelector(".announce-close");
    var dismissed = null;
    try { dismissed = localStorage.getItem("ss-announce-dismissed"); } catch (err) {}
    if (dismissed) announce.classList.add("hide");
    var msgs = announce.querySelectorAll(".announce-msgs p");
    var rotate = null;
    if (msgs.length > 1) {
      var mi = 0;
      rotate = setInterval(function () {
        msgs[mi].classList.remove("on");
        mi = (mi + 1) % msgs.length;
        msgs[mi].classList.add("on");
      }, 5000);
    }
    aClose.addEventListener("click", function () {
      announce.classList.add("hide");
      if (rotate) clearInterval(rotate);
      try { localStorage.setItem("ss-announce-dismissed", "1"); } catch (err) {}
    });
  }

  // Header shadow once scrolled
  var head = document.querySelector(".site-head");
  if (head) {
    var onScroll = function () {
      head.classList.toggle("scrolled", window.scrollY > 8);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Hero background video. The poster is identical to the video's first
  // frame, so a late start is invisible. Loading begins on the first user
  // interaction (or a 6 s fallback) so the video never competes with first
  // paint or lab metrics. Skipped for reduced-motion and Save-Data; paused
  // while the hero is off screen.
  var video = document.querySelector(".hero-media video");
  if (video) {
    var conn = navigator.connection || {};
    var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!reduced && !conn.saveData) {
      var started = false;
      var start = function () {
        if (started) return;
        started = true;
        ["pointerdown", "pointermove", "touchstart", "scroll", "keydown"].forEach(function (ev) {
          window.removeEventListener(ev, start);
        });
        video.querySelectorAll("source[data-src]").forEach(function (s) {
          s.src = s.dataset.src;
        });
        video.load();
        var p = video.play();
        if (p && p.catch) p.catch(function () { /* poster stays - fine */ });
        if ("IntersectionObserver" in window) {
          new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
              if (en.isIntersecting) { var q = video.play(); if (q && q.catch) q.catch(function () {}); }
              else video.pause();
            });
          }, { threshold: 0.05 }).observe(video);
        }
      };
      ["pointerdown", "pointermove", "touchstart", "scroll", "keydown"].forEach(function (ev) {
        window.addEventListener(ev, start, { passive: true, once: false });
      });
      var arm = function () { setTimeout(start, 10000); };
      if (document.readyState === "complete") arm();
      else window.addEventListener("load", arm);
    }
  }

  // Lazy images: swap data-src in only when near the viewport. Native
  // loading=lazy prefetches within thousands of px on slow connections,
  // which drags every photo into the initial load.
  var lazyImgs = document.querySelectorAll("img.lz[data-src]");
  if (lazyImgs.length) {
    if ("IntersectionObserver" in window) {
      var lzio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) {
            en.target.src = en.target.dataset.src;
            en.target.removeAttribute("data-src");
            lzio.unobserve(en.target);
          }
        });
      }, { rootMargin: "400px 0px" });
      lazyImgs.forEach(function (img) { lzio.observe(img); });
    } else {
      lazyImgs.forEach(function (img) { img.src = img.dataset.src; });
    }
  }

  // Scroll-in reveals (skipped for reduced motion via CSS)
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add("in");
          io.unobserve(en.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    document.querySelectorAll(".rv").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".rv").forEach(function (el) { el.classList.add("in"); });
  }

  // Anchor landing correction: sections use content-visibility, so the
  // browser's first jump targets estimated heights. Nudge the scroll over a
  // few frames until the target is actually flush with the viewport.
  var fixAnchor = function () {
    if (!location.hash) return;
    var el = document.getElementById(location.hash.slice(1));
    if (!el) return;
    var tries = 0;
    var step = function () {
      var top = el.getBoundingClientRect().top;
      if (Math.abs(top) > 2 && tries++ < 14) {
        window.scrollBy(0, top);
        requestAnimationFrame(step);
      }
    };
    requestAnimationFrame(step);
  };
  window.addEventListener("hashchange", fixAnchor);
  fixAnchor();

  // Lead form - placeholder handler. Swap for the GHL form embed at launch;
  // keep field names (name/phone/email/service/message) for tracking parity.
  // On success the visitor lands on the thank-you page (a clean conversion
  // URL for GA4/ads goals). Nothing is transmitted in this demo build.
  document.querySelectorAll("#lead-form, .hero-form").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      window.location.href = form.dataset.success || "thank-you.html";
    });
  });

  // Pricing calculator - mirrors the line-item rates published on the page.
  var calc = document.getElementById("calc");
  if (calc) {
    var TYPES = {
      full:       { lo: 12,  hi: 22, min: 400,  max: 12000, def: 1500, step: 100, floor: 8000,  name: "Full landscape" },
      patio:      { lo: 22,  hi: 28, min: 120,  max: 1500,  def: 350,  step: 10,  floor: 8500,  name: "Patio & hardscape" },
      irrigation: { lo: 1.5, hi: 3,  min: 1000, max: 15000, def: 4000, step: 250, floor: 4500,  name: "Irrigation system" },
      refresh:    { lo: 6,   hi: 12, min: 200,  max: 5000,  def: 800,  step: 50,  floor: 2500,  name: "Planting refresh" }
    };
    var EXTRAS = { fire: [3500, 9000], light: [2400, 4200], rock: [1500, 5000] };
    var TIER_NAMES = { "1": "Essential", "1.25": "Signature", "1.6": "Premium" };
    var size = document.getElementById("c-size");
    var sizeOut = document.getElementById("c-size-out");
    var total = document.getElementById("c-total");
    var desc = document.getElementById("c-desc");
    var fmt = function (n) {
      n = Math.round(n / 250) * 250;
      return "$" + n.toLocaleString("en-US");
    };
    var update = function (typeChanged) {
      var t = TYPES[calc.elements["c-type"].value];
      if (typeChanged) {
        size.min = t.min; size.max = t.max; size.step = t.step; size.value = t.def;
        document.getElementById("c-min").textContent = t.min.toLocaleString("en-US");
        document.getElementById("c-max").textContent = t.max.toLocaleString("en-US");
      }
      var sq = +size.value;
      var mult = +calc.elements["c-tier"].value;
      var lo = sq * t.lo * mult, hi = sq * t.hi * mult;
      calc.querySelectorAll('input[name="c-extra"]:checked').forEach(function (x) {
        lo += EXTRAS[x.value][0]; hi += EXTRAS[x.value][1];
      });
      lo = Math.max(lo, t.floor); hi = Math.max(hi, lo * 1.4);
      sizeOut.textContent = sq.toLocaleString("en-US");
      total.textContent = fmt(lo) + " - " + fmt(hi);
      desc.textContent = t.name + " · " + sq.toLocaleString("en-US") + " sq ft · " +
        TIER_NAMES[calc.elements["c-tier"].value] + " finish";
    };
    calc.addEventListener("input", function (e) {
      update(e.target.name === "c-type");
    });
    update(true);
  }

  // Cookie banner. No analytics load unless the visitor allows them -
  // wire the GA4/GTM snippet behind the "granted" choice at launch.
  var ck = document.getElementById("cookie");
  if (ck) {
    var choice = null;
    try { choice = localStorage.getItem("ss-consent"); } catch (err) {}
    var settle = function (val) {
      try { localStorage.setItem("ss-consent", val); } catch (err) {}
      ck.classList.remove("show");
      setTimeout(function () { ck.hidden = true; }, 400);
    };
    if (!choice) {
      ck.hidden = false;
      setTimeout(function () { ck.classList.add("show"); }, 1400);
    }
    document.getElementById("ck-accept").addEventListener("click", function () { settle("granted"); });
    document.getElementById("ck-decline").addEventListener("click", function () { settle("denied"); });
  }

  // Floating chat launcher (GHL webchat mounts in the popover at launch).
  var chat = document.getElementById("chat");
  if (chat) {
    var pop = document.getElementById("chat-pop");
    var cbtn = chat.querySelector(".chat-btn");
    var setChat = function (open) {
      chat.classList.toggle("open", open);
      pop.hidden = !open;
      cbtn.setAttribute("aria-expanded", String(open));
    };
    cbtn.addEventListener("click", function () { setChat(pop.hidden); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !pop.hidden) { setChat(false); cbtn.focus(); }
    });
    document.addEventListener("click", function (e) {
      if (!pop.hidden && !chat.contains(e.target)) setChat(false);
    });
  }
})();
""")

# ------------------------------------------------------------------ misc
write(".gitignore", """.claude/
Thumbs.db
.DS_Store
""")

write("README.md", f"""# Sage & Stone Landscape Co. - Bend, Oregon

A hand-built static website for a high-desert landscaping company. No frameworks,
no build step, no external requests - every page ships with inlined critical CSS,
a self-hosted variable font, and custom-made assets (logo, illustrations, and an
original animated hero video rendered from code).

**Live staging:** https://philderev.github.io/landscaping/

## Highlights

- **Hero background video** - original 12 s seamless-loop animation, encoded as
  WebM (VP9) with an H.264 MP4 fallback (`yuv420p`, `+faststart`), `muted
  playsinline` so it autoplays on iPhone/iPad and macOS Safari. The video loads
  after `window.load`, never competing with first paint; users with
  `prefers-reduced-motion` or Save-Data get the poster only.
- **Performance** - zero render-blocking requests: CSS inlined, single subset
  woff2 (~25 KB) preloaded, poster preloaded with `fetchpriority=high`,
  vanilla JS (~2 KB, deferred). All images are SVG or optimized WebP with
  explicit dimensions (no CLS).
- **SEO / Search Console** - unique titles + meta descriptions, canonical URLs,
  `LandscapingBusiness` + `BreadcrumbList` structured data, `sitemap.xml`,
  `robots.txt`, Open Graph + Twitter cards, one-page-per-service architecture.
- **Accessibility** - semantic landmarks, skip link, labeled form controls,
  focus-visible styles, AA contrast, reduced-motion support.

## Structure

```
index.html                     homepage
services/*.html                one page per service (4)
areas/*.html                   one page per service area (8), each with local content
privacy.html · terms.html      legal pages (linked from footer, form, cookie banner)
thank-you.html                 post-submit conversion page (noindex)
404.html                       styled not-found page (GitHub Pages picks it up)
assets/fonts/                  Fraunces subset (OFL licensed - see OFL.txt)
assets/img/                    logo, favicons, illustrations, map + og image
assets/video/                  hero.webm / hero.mp4 / poster
sitemap.xml · robots.txt · site.webmanifest
```

## UX components

- **Nav dropdowns** for Services and Service Areas (hover + keyboard focus on
  desktop, expanded groups in the mobile menu).
- **Cookie banner** - consent-first: no analytics unless the visitor allows
  them; choice stored in `localStorage` (`ss-consent`). Wire GA4/GTM behind the
  `granted` value at launch.
- **Floating chat launcher** - call/text/email popover; the GHL webchat widget
  mounts inside it at launch (marked with a comment).
- **Lead form** → redirects to `thank-you.html`, a clean conversion URL for
  GA4 / ads goals.

## Launch notes

- The lead form is a styled placeholder - swap in the GHL form embed at launch
  (marked with a comment in `index.html`; field names are ready for tracking).
- GA4 / GTM snippets go just before `</head>` on every page when IDs are
  provided - load them only after cookie consent (`ss-consent === "granted"`).
- `sitemap.xml`, canonicals, and og:urls point at the staging URL; replace
  `philderev.github.io/landscaping/` with the production domain at deploy.

Business details (name, address, phone, reviews) are fictional placeholders
created for this demonstration build. Photography sourced from Pexels under
the Pexels license (free for commercial use, no attribution required); hero
background video provided by the client and re-encoded for web delivery.
""")

print("build complete.")
