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
areas/*.html                   one page per service area (8), each with local content
privacy.html · terms.html      legal pages (linked from footer, form, cookie banner)
thank-you.html                 post-submit conversion page (noindex)
404.html                       styled not-found page (GitHub Pages picks it up)
assets/fonts/                  Fraunces subset (OFL licensed — see OFL.txt)
assets/img/                    logo, favicons, illustrations, map + og image
assets/video/                  hero.webm / hero.mp4 / poster
sitemap.xml · robots.txt · site.webmanifest
```

## UX components

- **Nav dropdowns** for Services and Service Areas (hover + keyboard focus on
  desktop, expanded groups in the mobile menu).
- **Cookie banner** — consent-first: no analytics unless the visitor allows
  them; choice stored in `localStorage` (`ss-consent`). Wire GA4/GTM behind the
  `granted` value at launch.
- **Floating chat launcher** — call/text/email popover; the GHL webchat widget
  mounts inside it at launch (marked with a comment).
- **Lead form** → redirects to `thank-you.html`, a clean conversion URL for
  GA4 / ads goals.

## Launch notes

- The lead form is a styled placeholder — swap in the GHL form embed at launch
  (marked with a comment in `index.html`; field names are ready for tracking).
- GA4 / GTM snippets go just before `</head>` on every page when IDs are
  provided — load them only after cookie consent (`ss-consent === "granted"`).
- `sitemap.xml`, canonicals, and og:urls point at the staging URL; replace
  `philderev.github.io/landscaping/` with the production domain at deploy.

Business details (name, address, phone, reviews) are fictional placeholders
created for this demonstration build. Photography sourced from Pexels under
the Pexels license (free for commercial use, no attribution required); hero
background video provided by the client and re-encoded for web delivery.
