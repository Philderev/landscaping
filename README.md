# Sage & Stone Landscape Co. — Bend, Oregon

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
