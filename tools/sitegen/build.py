# Assemble the static site into the project root.
import os
import re

from css import CSS

def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\n+", "", css)
    css = re.sub(r"  +", " ", css)
    return css.strip()
from parts import SITE, head, header, footer, business_schema, breadcrumb_schema
import pages_index
import pages_services

ROOT = r"E:\templates\landscaping website template"
SP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # scratchpad
DATE = "2026-07-08"


def page(*, title, desc, canonical_path, root, body, active="", schemas=None, preload_poster=False):
    css = minify_css(CSS.replace("{R}", root))
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
{head(title=title, desc=desc, canonical_path=canonical_path, root=root, extra_schema=schemas, preload_poster=preload_poster)}
<style>{css}</style>
</head>
<body>
{header(root, active)}
{body}
{footer(root)}
</body>
</html>'''


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
        active="services",
        schemas=schemas,
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
    desc="The page you're looking for doesn't exist. Return to Sage & Stone Landscape Co. — landscape design and build in Bend, Oregon.",
    canonical_path="404.html",
    root="",
    body=err_body,
))

# ------------------------------------------------------------------ robots + sitemap
write("robots.txt", f"""User-agent: *
Allow: /

Sitemap: {SITE['base']}sitemap.xml
""")

urls = [("", "1.0")] + [(f"services/{s}.html", "0.8") for s in pages_services.ORDER]
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
  "theme_color": "#12211A",
  "background_color": "#F4EEE3",
  "display": "browser"
}
""")

# ------------------------------------------------------------------ js
write("assets/js/main.js", r"""// Sage & Stone — progressive enhancement. ~2 KB, no dependencies.
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
        if (p && p.catch) p.catch(function () { /* poster stays — fine */ });
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
      var arm = function () { setTimeout(start, 6000); };
      if (document.readyState === "complete") arm();
      else window.addEventListener("load", arm);
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

  // Lead form — placeholder handler. Swap for the GHL form embed at launch;
  // keep field names (name/phone/email/service/message) for tracking parity.
  var form = document.getElementById("lead-form");
  var ok = document.getElementById("form-ok");
  if (form && ok) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      ok.classList.add("show");
      form.hidden = true;
      ok.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  }
})();
""")

# ------------------------------------------------------------------ misc
write(".gitignore", """.claude/
Thumbs.db
.DS_Store
""")

write("README.md", f"""# Sage & Stone Landscape Co. — Bend, Oregon

A hand-built static website for a high-desert landscaping company. No frameworks,
no build step, no external requests — every page ships with inlined critical CSS,
a self-hosted variable font, and custom-made assets (logo, illustrations, and an
original animated hero video rendered from code).

**Live staging:** https://philderev.github.io/landscaping/

## Highlights

- **Hero background video** — original 12 s seamless-loop animation, encoded as
  WebM (VP9) with an H.264 MP4 fallback (`yuv420p`, `+faststart`), `muted
  playsinline` so it autoplays on iPhone/iPad and macOS Safari. The video loads
  after `window.load`, never competing with first paint; users with
  `prefers-reduced-motion` or Save-Data get the poster only.
- **Performance** — zero render-blocking requests: CSS inlined, single subset
  woff2 (~25 KB) preloaded, poster preloaded with `fetchpriority=high`,
  vanilla JS (~2 KB, deferred). All images are SVG or optimized WebP with
  explicit dimensions (no CLS).
- **SEO / Search Console** — unique titles + meta descriptions, canonical URLs,
  `LandscapingBusiness` + `BreadcrumbList` structured data, `sitemap.xml`,
  `robots.txt`, Open Graph + Twitter cards, one-page-per-service architecture.
- **Accessibility** — semantic landmarks, skip link, labeled form controls,
  focus-visible styles, AA contrast, reduced-motion support.

## Structure

```
index.html                     homepage
services/*.html                one page per service (4)
404.html                       styled not-found page (GitHub Pages picks it up)
assets/fonts/                  Fraunces subset (OFL licensed — see OFL.txt)
assets/img/                    logo, favicons, illustrations, map (SVG) + og image
assets/video/                  hero.webm / hero.mp4 / poster
sitemap.xml · robots.txt · site.webmanifest
```

## Launch notes

- The lead form is a styled placeholder — swap in the GHL form embed at launch
  (marked with a comment in `index.html`; field names are ready for tracking).
- GA4 / GTM snippets go just before `</head>` on every page when IDs are provided.
- `sitemap.xml`, canonicals, and og:urls point at the staging URL; replace
  `philderev.github.io/landscaping/` with the production domain at deploy.

Business details (name, address, phone, reviews) are fictional placeholders
created for this demonstration build.
""")

print("build complete.")
