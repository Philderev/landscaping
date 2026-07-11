# Shared stylesheet for Sage & Stone. Inlined into every page by build.py.
# "{R}" is replaced with the relative root prefix ("" or "../") per page.

CSS = r"""
@font-face{
  font-family:"Fraunces";
  src:url("{R}assets/fonts/fraunces-latin.woff2") format("woff2");
  font-weight:300 700;font-display:swap;font-style:normal;
}
@font-face{
  font-family:"Fraunces-fb";
  src:local("Georgia");
  size-adjust:106%;ascent-override:92%;descent-override:24%;line-gap-override:0%;
}
:root{
  --sand:#F2ECD3;--sand-2:#E3D6AC;--cream:#F8F4E2;
  --pine-950:#161F14;--pine-900:#22301D;--pine-700:#3D5236;--pine-500:#55704A;
  --sage:#8FA873;--sage-lt:#C3D2A8;
  --clay:#55704A;--clay-deep:#3D5236;--gold:#CDBA8C;
  --ink:#20302A;--ink-soft:#4A5A50;
  --serif:"Fraunces","Fraunces-fb",Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --wrap:1180px;
  --r-lg:28px;--r-md:18px;
  --shadow:0 20px 50px -18px rgba(18,33,26,.28);
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;font-family:var(--sans);color:var(--ink);background:var(--sand);
  font-size:1.0625rem;line-height:1.65;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;
}
h1,h2,h3,.serif{font-family:var(--serif);font-weight:420;line-height:1.12;color:var(--pine-900);margin:0 0 .5em;letter-spacing:-.01em}
h1{font-size:clamp(2.5rem,6.2vw,4.35rem)}
h2{font-size:clamp(1.9rem,3.6vw,2.9rem)}
h3{font-size:1.35rem;line-height:1.25}
p{margin:0 0 1.1em}
a{color:var(--clay);text-decoration-thickness:1px;text-underline-offset:3px}
a:hover{color:var(--clay-deep)}
img,svg,video{max-width:100%;height:auto;display:block}
ul{padding-left:1.2em}
:focus-visible{outline:3px solid var(--clay);outline-offset:3px;border-radius:4px}
::selection{background:var(--sage-lt);color:var(--pine-950)}

.skip{position:absolute;left:-999px;top:auto;background:var(--pine-950);color:var(--cream);padding:.8rem 1.4rem;z-index:200;border-radius:0 0 12px 0}
.skip:focus{left:0;top:0}

.wrap{max-width:var(--wrap);margin-inline:auto;padding-inline:clamp(1.1rem,4vw,2.5rem)}
.eyebrow{
  display:inline-flex;align-items:center;gap:.6rem;
  font-size:.78rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;
  color:var(--clay);margin-bottom:1.1rem;
}
.eyebrow.on-dark{color:var(--gold)}
.lede{font-size:clamp(1.08rem,1.6vw,1.28rem);color:var(--ink-soft);max-width:58ch}

/* ---------- announcement bar ---------- */
.announce{background:linear-gradient(180deg,var(--pine-900),var(--pine-950));color:var(--cream);border-bottom:1px solid rgba(249,244,233,.1)}
.announce-in{position:relative;display:flex;align-items:center;justify-content:center;gap:1rem;padding-block:.85rem;padding-right:3rem}
.announce-msgs{position:relative;display:grid;justify-items:center}
.announce-msgs p{grid-area:1/1;margin:0;font-size:.88rem;font-weight:600;letter-spacing:.01em;text-align:center;opacity:0;transform:translateY(6px);transition:opacity .5s ease,transform .5s ease;pointer-events:none}
.announce-msgs p.on{opacity:1;transform:translateY(0);pointer-events:auto}
.announce-cta{flex:none;display:inline-flex;align-items:center;background:rgba(249,244,233,.14);color:var(--cream);padding:.4rem 1rem;border-radius:999px;font-size:.78rem;font-weight:700;letter-spacing:.02em;white-space:nowrap;text-decoration:none;transition:background .2s ease,color .2s ease,transform .2s ease}
.announce-cta:hover{background:var(--gold);color:var(--pine-950);transform:translateY(-1px)}
.announce-close{position:absolute;right:.9rem;top:50%;transform:translateY(-50%);width:28px;height:28px;display:flex;align-items:center;justify-content:center;border-radius:50%;background:none;border:none;color:var(--cream);opacity:.7;font-size:1.3rem;line-height:1;cursor:pointer;transition:background .2s ease,opacity .2s ease}
.announce-close:hover{opacity:1;background:rgba(249,244,233,.14)}
.announce.hide{display:none}
@media (prefers-reduced-motion:reduce){
  .announce-msgs p{transition:none;transform:none}
}

/* ---------- header ---------- */
.site-head{
  position:sticky;top:0;z-index:100;
  background:rgba(244,238,227,.96);
  border-bottom:1px solid transparent;transition:border-color .3s,box-shadow .3s;
}
.site-head.scrolled{border-bottom-color:rgba(27,46,36,.12);box-shadow:0 8px 30px -18px rgba(18,33,26,.35)}
.head-in{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding-block:.7rem;min-height:72px}
.brand{display:flex;align-items:center;gap:.7rem;text-decoration:none;color:var(--pine-900)}
.brand svg{width:44px;height:44px;flex:none}
.brand img{height:44px;width:auto;flex:none}
.brand-name{font-family:var(--serif);font-size:1.28rem;font-weight:560;letter-spacing:.01em;line-height:1.05;color:var(--pine-900)}
.nav{display:flex;align-items:center;gap:clamp(1rem,2.4vw,2rem)}
.nav a{font-weight:600;font-size:.95rem;color:var(--pine-900);text-decoration:none;padding:.4rem 0;border-bottom:2px solid transparent}
.nav a:hover,.nav a[aria-current="page"]{border-bottom-color:var(--clay);color:var(--pine-900)}
.nav a.btn,.nav a.btn:hover{color:var(--cream);border-bottom:none}
.nav-phone{display:inline-flex;align-items:center;gap:.45rem}
.nav-toggle{display:none}

/* ---------- buttons ---------- */
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:.55rem;
  font-family:var(--sans);font-weight:700;font-size:1rem;line-height:1;
  padding:1.02rem 1.7rem;border-radius:999px;border:2px solid transparent;
  text-decoration:none;cursor:pointer;
  transition:transform .18s ease,box-shadow .18s ease,background-color .18s,color .18s,border-color .18s;
}
.btn-primary{background:var(--clay);color:var(--cream)}
.btn-primary:hover{background:var(--clay-deep);color:var(--cream);transform:translateY(-2px);box-shadow:0 14px 30px -12px rgba(61,82,54,.55)}
.btn-ghost{border-color:var(--pine-900);color:var(--pine-900);background:transparent}
.btn-ghost:hover{background:var(--pine-900);color:var(--cream);transform:translateY(-2px)}
.btn-ghost.on-dark{border-color:rgba(251,247,239,.75);color:var(--cream)}
.btn-ghost.on-dark:hover{background:var(--cream);color:var(--pine-950)}
.btn .arr{transition:transform .18s}
.btn:hover .arr{transform:translateX(4px)}

/* ---------- hero ---------- */
.hero{position:relative;isolation:isolate;display:flex;flex-direction:column;justify-content:flex-end;
  min-height:min(94vh,980px);min-height:min(94svh,980px);color:var(--cream);overflow:hidden;background:var(--pine-950)}
.hero-media{position:absolute;inset:0;z-index:-2}
.hero-media video{width:100%;height:100%;object-fit:cover;object-position:50% 50%}
.hero::before{content:"";position:absolute;inset:0;z-index:-1;
  background:linear-gradient(100deg,rgba(14,42,27,.92) 0%,rgba(14,42,27,.66) 40%,rgba(16,46,30,.32) 70%,rgba(12,36,23,.5) 100%),
    linear-gradient(180deg,rgba(9,28,18,.55) 0%,rgba(9,28,18,.18) 42%,rgba(7,24,15,.85) 100%)}
.hero::after{content:"";position:absolute;inset:0;z-index:-1;opacity:.08;pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E")}
.hero-in{position:relative;width:100%;padding-top:9.5rem}
.hero h1{color:var(--cream);max-width:13.5ch;font-weight:380;text-wrap:balance}
.hero h1 em{font-style:normal;color:var(--gold);position:relative;white-space:nowrap}
.hero h1 em svg{position:absolute;left:0;bottom:-.12em;width:100%;height:.22em;overflow:visible}
.hero .lede{color:rgba(249,244,233,.88);max-width:52ch;font-size:clamp(1.05rem,1.5vw,1.22rem)}
.hero-cta{display:flex;flex-wrap:wrap;gap:.9rem;margin-top:2rem}
.hero-cta .btn-primary{align-self:center;text-align:center}
.hero-cta .btn-primary:hover{background:var(--gold);color:var(--pine-950)}
.hero-foot{margin-top:clamp(2.5rem,6vh,4.5rem);border-top:1px solid rgba(249,244,233,.22)}
.hero-stats{display:grid;grid-template-columns:repeat(3,auto) 1fr;gap:clamp(1.2rem,4vw,3.5rem);align-items:center;padding-block:1.2rem 1.4rem}
.hero-stats .stat b{display:block;font-family:var(--serif);font-weight:480;font-size:clamp(1.5rem,2.6vw,2.1rem);color:var(--gold);line-height:1}
.hero-stats .stat span{font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:rgba(249,244,233,.75)}
.scroll-cue{justify-self:end;display:flex;align-items:center;gap:.6rem;color:rgba(249,244,233,.7);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;text-decoration:none}
.scroll-cue svg{animation:bob 2.4s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(6px)}}

/* ---------- marquee ---------- */
.marquee{background:var(--pine-950);color:var(--sage-lt);overflow:hidden;border-block:1px solid rgba(249,244,233,.08)}
.marq-track{display:flex;gap:0;width:max-content;animation:marq 30s linear infinite}
.marquee:hover .marq-track{animation-play-state:paused}
.marq-track ul{display:flex;list-style:none;margin:0;padding:.85rem 0;gap:2.6rem;font-size:.85rem;font-weight:600;letter-spacing:.22em;text-transform:uppercase;white-space:nowrap}
.marq-track ul{padding-right:2.6rem}
@keyframes marq{to{transform:translateX(-50%)}}

/* ---------- sections ---------- */
.sec{padding-block:clamp(4rem,9vw,7.5rem);content-visibility:auto;contain-intrinsic-size:auto 900px}
.sec-head{max-width:720px;margin-bottom:clamp(2.2rem,5vw,3.8rem)}
.sec-head.center{margin-inline:auto;text-align:center}
.sec-head.center .eyebrow{justify-content:center}

/* services grid */
.svc-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(1.2rem,2.6vw,2.2rem)}
.svc-card{
  position:relative;display:flex;flex-direction:column;gap:0;
  background:var(--cream);border:1px solid rgba(27,46,36,.08);border-radius:var(--r-lg);
  padding:0;overflow:hidden;text-decoration:none;color:var(--ink);
  transition:transform .25s ease,box-shadow .25s ease;
}
.svc-card:hover{transform:translateY(-6px);box-shadow:var(--shadow)}
.svc-card:nth-child(2){transform:translateY(2.2rem)}
.svc-card:nth-child(2):hover{transform:translateY(calc(2.2rem - 6px))}
.svc-card:nth-child(4){transform:translateY(2.2rem)}
.svc-card:nth-child(4):hover{transform:translateY(calc(2.2rem - 6px))}
.svc-art{background:var(--sand-2);aspect-ratio:16/9.5}
.svc-art{overflow:hidden}
.svc-art img{width:100%;height:100%;object-fit:cover;transition:transform .5s cubic-bezier(.2,.7,.3,1)}
.svc-card:hover .svc-art img{transform:scale(1.07)}
.svc-body{padding:1.6rem 1.7rem 1.8rem}
.svc-body h3{margin-bottom:.45rem}
.svc-body p{color:var(--ink-soft);font-size:.99rem;margin-bottom:1rem}
.svc-more{font-weight:700;font-size:.92rem;color:var(--clay);display:inline-flex;align-items:center;gap:.4rem}
.svc-card:hover .svc-more .arr{transform:translateX(4px)}
.svc-more .arr{transition:transform .2s}

/* dark manifesto */
.dark{background:var(--pine-950);color:#E9E4D5;position:relative;overflow:hidden}
.dark h2,.dark h3{color:var(--cream)}
.dark .lede{color:rgba(233,228,213,.82)}
.contours{position:absolute;inset:0;opacity:.14;pointer-events:none}
.manif{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(2rem,5vw,4.5rem);align-items:center;position:relative}
.manif-copy p{color:rgba(233,228,213,.85)}
.fact-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.fact{background:rgba(249,244,233,.06);border:1px solid rgba(249,244,233,.12);border-radius:var(--r-md);padding:1.3rem 1.4rem}
.fact b{display:block;font-family:var(--serif);font-size:clamp(1.7rem,2.4vw,2.3rem);font-weight:450;color:var(--gold);line-height:1.05;margin-bottom:.3rem}
.fact span{font-size:.85rem;color:rgba(233,228,213,.75);line-height:1.4;display:block}

/* process */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(1.2rem,2.4vw,2rem);counter-reset:step}
.step{position:relative;padding-top:1rem}
.step::before{counter-increment:step;content:"0" counter(step);
  font-family:var(--serif);font-weight:340;font-size:clamp(3rem,5vw,4.2rem);line-height:1;color:transparent;
  -webkit-text-stroke:1.5px var(--clay);display:block;margin-bottom:.9rem}
.step h3{font-size:1.18rem}
.step p{font-size:.95rem;color:var(--ink-soft)}

/* projects */
.proj-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.2rem,2.4vw,2rem)}
.proj{background:var(--cream);border-radius:var(--r-lg);overflow:hidden;border:1px solid rgba(27,46,36,.08);transition:transform .25s,box-shadow .25s}
.proj:hover{transform:translateY(-6px);box-shadow:var(--shadow)}
.proj img{aspect-ratio:4/3;object-fit:cover;width:100%;transition:transform .5s cubic-bezier(.2,.7,.3,1)}
.proj:hover img{transform:scale(1.07)}
.proj-body{padding:1.35rem 1.5rem 1.5rem}
.proj-body h3{font-size:1.22rem;margin-bottom:.3rem}
.proj-body p{font-size:.93rem;color:var(--ink-soft);margin-bottom:.8rem}
.tags{display:flex;flex-wrap:wrap;gap:.45rem;padding:0;margin:0;list-style:none}
.tags li{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--pine-700);
  background:var(--sand-2);border-radius:999px;padding:.32rem .7rem}

/* reviews */
.reviews{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(300px,340px);gap:1.3rem;
  overflow-x:auto;scroll-snap-type:x mandatory;padding:0 clamp(1.1rem,4vw,2.5rem) 1.2rem;
  max-width:var(--wrap);margin-inline:auto;scrollbar-width:thin;scrollbar-color:var(--sage) transparent}
.review{scroll-snap-align:start;background:var(--cream);border:1px solid rgba(27,46,36,.08);box-shadow:var(--shadow);
  border-radius:var(--r-lg);padding:1.5rem 1.6rem 1.4rem;display:flex;flex-direction:column;position:relative}
.review-top{display:flex;align-items:center;gap:.7rem;margin-bottom:.9rem}
.review-avatar{flex:none;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;
  background:var(--clay);color:var(--cream);font-family:var(--serif);font-weight:600;font-size:1.05rem}
.review-top b{display:block;font-size:.95rem;color:var(--pine-900)}
.review-when{font-size:.8rem;color:var(--ink-soft)}
.review p{font-size:.98rem;color:var(--ink);flex:1}
.stars{display:flex;gap:.18rem;margin-bottom:.9rem}
.stars svg{width:16px;height:16px;fill:var(--gold)}
.review footer{margin-top:1rem;padding-top:.9rem;border-top:1px solid rgba(27,46,36,.1);font-size:.85rem;color:var(--ink-soft)}

/* map + areas */
.areas{display:grid;grid-template-columns:.95fr 1.05fr;gap:clamp(2rem,5vw,4rem);align-items:center}
.area-list{display:grid;grid-template-columns:1fr 1fr;gap:.55rem .8rem;padding:0;margin:1.4rem 0 0;list-style:none}
.area-list li{display:flex;align-items:center;gap:.6rem;font-weight:600;color:var(--pine-900);font-size:.98rem}
.area-list li svg{width:15px;height:15px;flex:none;fill:var(--clay)}
.map-card{background:var(--cream);border:1px solid rgba(27,46,36,.08);border-radius:var(--r-lg);padding:clamp(1rem,2vw,1.8rem);box-shadow:var(--shadow)}
.live-map{display:block;width:100%;min-height:440px;border:0;border-radius:18px}
.live-map.side-map{min-height:360px;border-radius:12px}

/* faq */
.faq{max-width:820px;margin-inline:auto}
.faq details{border-bottom:1px solid rgba(27,46,36,.14)}
.faq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1.5rem;
  padding:1.35rem .2rem;font-family:var(--serif);font-size:1.18rem;font-weight:480;color:var(--pine-900)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-family:var(--sans);font-weight:400;font-size:1.7rem;line-height:1;color:var(--clay);transition:transform .25s;flex:none}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 .2rem 1.4rem;color:var(--ink-soft);max-width:68ch}

/* contact */
.contact-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(2rem,5vw,4.5rem)}
.field{margin-bottom:1.15rem}
.field label{display:block;font-weight:700;font-size:.88rem;letter-spacing:.02em;margin-bottom:.4rem;color:var(--pine-900)}
.field input,.field select,.field textarea{
  width:100%;font:inherit;color:var(--ink);background:var(--cream);
  border:1.5px solid rgba(27,46,36,.22);border-radius:12px;padding:.85rem 1rem;
  transition:border-color .2s,box-shadow .2s;
}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--clay);box-shadow:0 0 0 3px rgba(85,112,74,.18)}
.field textarea{min-height:130px;resize:vertical}
.field-row{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.sms-consent{display:flex;align-items:flex-start;gap:.7rem;margin:0 0 1.25rem;color:var(--ink-soft);font-size:.86rem;line-height:1.5;cursor:pointer}
.sms-consent input{width:18px;height:18px;flex:none;margin:.15rem 0 0;accent-color:var(--pine-900)}
.sms-consent span{max-width:58ch}
.form-actions{text-align:center}
.form-actions .btn-primary:hover{background:var(--gold);color:var(--pine-950)}
.form-legal{font-size:.85rem;margin:.9rem 0 0;text-align:center}
.form-note{font-size:.85rem;color:var(--ink-soft)}
.form-ok{display:none;background:var(--pine-700);color:var(--cream);border-radius:var(--r-md);padding:1.2rem 1.4rem;margin-bottom:1.1rem}
.form-ok.show{display:block}
.info-card{background:var(--pine-950);color:#E9E4D5;border-radius:var(--r-lg);padding:clamp(1.6rem,3vw,2.4rem);position:relative;overflow:hidden}
.info-card h3{color:var(--cream)}
.info-card a{color:var(--gold)}
.info-line{display:flex;gap:.9rem;align-items:flex-start;margin-bottom:1.15rem;font-size:.98rem}
.info-line svg{width:20px;height:20px;flex:none;fill:var(--gold);margin-top:.15rem}
.hours{width:100%;border-collapse:collapse;font-size:.95rem;margin-top:.4rem}
.hours td{padding:.32rem 0;border-bottom:1px dashed rgba(249,244,233,.15)}
.hours td:last-child{text-align:right;color:var(--sage-lt)}

/* cta band */
.cta-band{position:relative;overflow:hidden;background:var(--clay);color:var(--cream)}
.cta-band h2{color:var(--cream);max-width:20ch}
.cta-in{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:2rem;padding-block:clamp(3rem,6vw,4.5rem)}

/* footer */
.site-foot{background:var(--pine-950);color:rgba(233,228,213,.78);font-size:.95rem}
.foot-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.1fr;gap:clamp(1.8rem,4vw,3rem);padding-block:clamp(3rem,6vw,4.5rem) 2.5rem}
.site-foot h3{font-family:var(--serif);font-weight:500;color:var(--cream);font-size:1.05rem;margin:0 0 1rem}
.site-foot ul{list-style:none;margin:0;padding:0}
.site-foot li{margin-bottom:.55rem}
.site-foot a{color:rgba(233,228,213,.78);text-decoration:none}
.site-foot a:hover{color:var(--gold)}
.foot-brand>svg{width:52px;height:52px;margin-bottom:1rem}
.foot-brand>img{height:52px;width:auto;margin-bottom:1rem}
.socials svg{margin:0}
.foot-brand p{max-width:34ch;font-size:.92rem}
.foot-legal{border-top:1px solid rgba(249,244,233,.12);padding-block:1.4rem;display:flex;flex-wrap:wrap;gap:1rem;justify-content:space-between;font-size:.83rem;color:rgba(233,228,213,.55)}
.socials{display:flex;gap:.8rem;margin-top:1.2rem}
.socials a{display:grid;place-items:center;width:38px;height:38px;border-radius:50%;border:1px solid rgba(249,244,233,.25)}
.socials a:hover{border-color:var(--gold);background:rgba(205,186,140,.12)}
.socials svg{width:17px;height:17px;fill:currentColor}

/* breadcrumbs + service pages */
.crumbs{padding-top:1.6rem;font-size:.86rem;color:var(--ink-soft)}
.crumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:.5rem;margin:0;padding:0}
.crumbs li+li::before{content:"/";margin-right:.5rem;color:rgba(27,46,36,.35)}
.crumbs a{color:var(--ink-soft);text-decoration:none}
.crumbs a:hover{color:var(--clay)}
.page-hero{padding-block:clamp(2.2rem,5vw,4rem) 0}
.page-hero h1{max-width:16ch}
.page-hero .lede{margin-bottom:0}
.banner-art{margin-top:clamp(2rem,4vw,3rem);border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow)}
.banner-art img{width:100%;aspect-ratio:21/8;object-fit:cover}
.split{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(2rem,5vw,4rem);align-items:start}
.checks{list-style:none;margin:1.2rem 0 0;padding:0;display:grid;gap:.7rem}
.checks li{display:flex;gap:.7rem;align-items:flex-start;font-size:1rem}
.checks svg{width:20px;height:20px;flex:none;fill:var(--sage);margin-top:.2rem}
.side-card{background:var(--cream);border:1px solid rgba(27,46,36,.08);border-radius:var(--r-lg);padding:1.8rem;position:sticky;top:96px}
.side-card .btn{width:100%;margin-top:.6rem}
.side-card .btn-primary:hover{background:var(--gold);color:var(--pine-950)}
.side-card hr{border:none;border-top:1px dashed rgba(27,46,36,.18);margin:1.3rem 0}
.side-links{list-style:none;padding:0;margin:0}
.side-links li{margin-bottom:.6rem}
.side-links a{font-weight:600;text-decoration:none;color:var(--pine-900);display:inline-flex;gap:.45rem;align-items:center}
.side-links a:hover{color:var(--clay)}
.prose h2{font-size:clamp(1.55rem,2.6vw,2.1rem);margin-top:2.2rem}
.prose ul li{margin-bottom:.5rem}

/* reveal animation */
.js .rv{opacity:0;transform:translateY(22px);transition:opacity .7s cubic-bezier(.2,.7,.3,1),transform .7s cubic-bezier(.2,.7,.3,1)}
.js .rv.in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){
  .js .rv{opacity:1;transform:none;transition:none}
  .marq-track{animation:none;flex-wrap:wrap;width:auto}
  .scroll-cue svg{animation:none}
  .btn,.svc-card,.svc-art img,.proj,.proj img{transition:none}
  .svc-card:hover .svc-art img{transform:none}
  .proj:hover img{transform:none}
}

/* 404 */
.err{min-height:70vh;display:grid;place-items:center;text-align:center;padding-block:5rem}
.err .num{font-family:var(--serif);font-weight:340;font-size:clamp(6rem,18vw,11rem);line-height:1;color:transparent;-webkit-text-stroke:2px var(--clay);display:block}

/* ---------- responsive ---------- */
@media (max-width:1020px){
  .steps{grid-template-columns:1fr 1fr;row-gap:2.4rem}
  .proj-grid{grid-template-columns:1fr 1fr}
  .proj:last-child{grid-column:1/-1}
  .foot-grid{grid-template-columns:1fr 1fr}
}
@media (max-width:860px){
  .nav{
    position:fixed;inset:72px 0 auto 0;flex-direction:column;align-items:stretch;gap:0;
    background:var(--sand);border-bottom:1px solid rgba(27,46,36,.12);
    padding:1rem clamp(1.1rem,4vw,2.5rem) 1.6rem;box-shadow:0 30px 40px -20px rgba(18,33,26,.3);
    transform:translateY(-130%);transition:transform .3s ease;visibility:hidden;
  }
  .js .nav{visibility:visible}
  .nav.open{transform:none}
  .nav a{padding:.85rem 0;border-bottom:1px solid rgba(27,46,36,.08);font-size:1.05rem}
  .nav .btn{margin-top:1rem;justify-content:center}
  .nav-toggle{
    display:inline-flex;flex-direction:column;justify-content:center;gap:5px;
    width:46px;height:46px;padding:11px;background:none;border:2px solid var(--pine-900);border-radius:12px;cursor:pointer;
  }
  .nav-toggle span{display:block;height:2px;background:var(--pine-900);border-radius:2px;transition:transform .25s,opacity .2s}
  .nav-toggle[aria-expanded="true"] span:nth-child(1){transform:translateY(7px) rotate(45deg)}
  .nav-toggle[aria-expanded="true"] span:nth-child(2){opacity:0}
  .nav-toggle[aria-expanded="true"] span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
  .svc-grid{grid-template-columns:1fr}
  .svc-card:nth-child(2),.svc-card:nth-child(4){transform:none}
  .svc-card:nth-child(2):hover,.svc-card:nth-child(4):hover{transform:translateY(-6px)}
  .manif,.areas,.contact-grid,.split{grid-template-columns:1fr}
  .side-card{position:static}
  .hero-stats{grid-template-columns:repeat(3,1fr)}
  .scroll-cue{display:none}
  .hero-in{padding-top:7rem}
}
@media (max-width:560px){
  .announce-in{flex-wrap:wrap;gap:.5rem;padding-right:2.6rem}
  .announce-msgs p{font-size:.76rem}
  .steps{grid-template-columns:1fr}
  .proj-grid{grid-template-columns:1fr}
  .field-row{grid-template-columns:1fr}
  .fact-grid{grid-template-columns:1fr 1fr}
  .foot-grid{grid-template-columns:1fr}
  .area-list{grid-template-columns:1fr 1fr}
  .hero-stats{gap:1rem}
  .hero-stats .stat span{font-size:.68rem}
}

/* ---------- nav dropdowns ---------- */
.nav-item{position:relative;display:flex;align-items:center}
.nav-item>a .car{display:inline-block;margin-left:.4rem;font-size:.55rem;transform:translateY(-2px);transition:transform .2s}
.nav-item:hover>a .car,.nav-item:focus-within>a .car{transform:translateY(-2px) rotate(180deg)}
.sub{position:absolute;top:100%;left:50%;translate:-50% 6px;min-width:250px;
  background:var(--cream);border:1px solid rgba(27,46,36,.1);border-radius:16px;
  box-shadow:var(--shadow);padding:.55rem;margin:0;list-style:none;
  opacity:0;visibility:hidden;transition:opacity .2s,translate .2s,visibility .2s;z-index:60}
.nav-item:hover .sub,.nav-item:focus-within .sub{opacity:1;visibility:visible;translate:-50% 0}
.sub.cols{display:grid;grid-template-columns:1fr 1fr;min-width:330px}
.sub a{display:block;padding:.55rem .85rem;border-radius:10px;border-bottom:none;font-weight:600;font-size:.93rem;white-space:nowrap}
.sub a:hover,.sub a[aria-current="page"]{background:var(--sand-2);border-bottom:none}
.nav>.nav-item>a{white-space:nowrap}
.nav a.btn,.nav a.btn:hover{padding:.85rem 1.35rem;font-size:.92rem;white-space:nowrap;flex:none;align-self:center;text-align:center}
.nav a.btn:hover{background:var(--gold);color:var(--pine-950)}
@media (max-width:1150px) and (min-width:861px){.nav-phone{display:none}}

/* ---------- service radio pills ---------- */
fieldset.field{border:none;padding:0;margin:0 0 1.15rem;min-width:0}
fieldset.field legend{font-weight:700;font-size:.88rem;letter-spacing:.02em;margin-bottom:.55rem;color:var(--pine-900);padding:0}
.pills{display:flex;flex-wrap:wrap;gap:.5rem}
.pills label{cursor:pointer;position:relative}
.pills input{position:absolute;opacity:0;pointer-events:none}
.pills span{display:inline-block;padding:.55rem 1.05rem;border-radius:999px;border:1.5px solid rgba(27,46,36,.28);
  font-size:.9rem;font-weight:600;color:var(--pine-900);background:var(--cream);
  transition:background .18s,color .18s,border-color .18s}
.pills label:hover span{border-color:var(--clay);color:var(--clay)}
.pills input:checked+span{background:var(--pine-900);border-color:var(--pine-900);color:var(--cream)}
.pills input:focus-visible+span{outline:3px solid var(--clay);outline-offset:2px}
.consent{font-size:.83rem;color:var(--ink-soft);margin-top:.95rem;max-width:52ch}

/* ---------- footer polish ---------- */
.socials a{display:inline-flex;align-items:center;justify-content:center;line-height:0}
.socials svg{display:block;flex:none}
.area-list a{color:var(--pine-900);text-decoration:none}
.area-list a:hover{color:var(--clay);text-decoration:underline;text-underline-offset:3px}
.foot-legal nav{display:flex;gap:1.2rem}

/* ---------- cookie banner ---------- */
.cookie{position:fixed;left:1.1rem;bottom:1.1rem;z-index:140;max-width:400px;
  background:var(--pine-950);color:#E9E4D5;border:1px solid rgba(249,244,233,.16);border-radius:18px;
  padding:1.15rem 1.3rem;box-shadow:0 24px 60px -18px rgba(0,0,0,.55);
  opacity:0;transform:translateY(14px);transition:opacity .35s,transform .35s;pointer-events:none}
.cookie.show{opacity:1;transform:none;pointer-events:auto}
.cookie p{font-size:.88rem;line-height:1.55;margin:0 0 .95rem}
.cookie a{color:var(--gold)}
.cookie-actions{display:flex;flex-wrap:wrap;gap:.6rem}
.cookie .btn{padding:.62rem 1.1rem;font-size:.85rem}
.cookie .btn-ghost{border-color:rgba(249,244,233,.55);color:var(--cream)}
.cookie .btn-ghost:hover{background:var(--cream);color:var(--pine-950)}

/* ---------- floating chat ---------- */
.chat{position:fixed;right:1.1rem;bottom:1.1rem;z-index:150;display:flex;flex-direction:column;align-items:flex-end;gap:.85rem}
.chat-btn{width:58px;height:58px;border-radius:50%;border:none;background:var(--clay);color:var(--cream);
  display:grid;place-items:center;cursor:pointer;box-shadow:0 14px 34px -10px rgba(61,82,54,.65);
  transition:transform .18s,background .18s}
.chat-btn:hover{background:var(--clay-deep);transform:translateY(-2px)}
.chat-btn svg{width:26px;height:26px;fill:currentColor}
.chat-btn .ic-close{display:none}
.chat.open .ic-chat{display:none}
.chat.open .ic-close{display:block}
.chat-pop{width:min(330px,calc(100vw - 2.4rem));background:var(--cream);border:1px solid rgba(27,46,36,.12);
  border-radius:18px;box-shadow:var(--shadow);overflow:hidden}
.chat-head{background:var(--pine-950);color:var(--cream);padding:1rem 1.2rem;display:flex;gap:.75rem;align-items:center}
.chat-head svg{width:34px;height:34px;flex:none}
.chat-head img{height:34px;width:auto;flex:none}
.chat-head b{font-family:var(--serif);font-weight:520;font-size:1.02rem;display:block;line-height:1.2}
.chat-head span{display:block;font-size:.75rem;color:var(--sage-lt)}
.chat-body{padding:1.05rem 1.2rem 1.2rem}
.chat-body p{font-size:.9rem;color:var(--ink-soft);margin-bottom:.9rem}
.chat-links{display:grid;gap:.5rem}
.chat-links a{display:flex;gap:.65rem;align-items:center;padding:.68rem .85rem;border:1.5px solid rgba(27,46,36,.16);
  border-radius:12px;text-decoration:none;font-weight:600;font-size:.92rem;color:var(--pine-900);transition:border-color .15s,color .15s}
.chat-links a:hover{border-color:var(--clay);color:var(--clay)}
.chat-links svg{width:17px;height:17px;fill:var(--clay);flex:none}

/* ---------- pricing page ---------- */
.tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.2rem,2.4vw,2rem)}
.tier{position:relative;background:var(--cream);border:1px solid rgba(27,46,36,.1);border-radius:var(--r-lg);
  padding:1.9rem 1.8rem;transition:transform .25s,box-shadow .25s}
.tier:hover{transform:translateY(-6px);box-shadow:var(--shadow)}
.tier.pop{background:var(--pine-950);border-color:var(--pine-950);color:#E9E4D5}
.tier.pop h3{color:var(--cream)}
.tier.pop .checks span{color:rgba(233,228,213,.88)}
.tier.pop p{color:rgba(233,228,213,.75)}
.tier-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);white-space:nowrap;background:var(--clay);color:var(--cream);
  font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;border-radius:999px;padding:.38rem .9rem}
.tier h3{margin-bottom:.2rem}
.tier .amount{display:block;font-family:var(--serif);font-weight:460;font-size:clamp(1.9rem,3vw,2.5rem);color:var(--clay);line-height:1.1;margin-bottom:.55rem}
.tier.pop .amount{color:var(--gold)}
.tier p{font-size:.94rem;color:var(--ink-soft);margin-bottom:1.2rem}
.tier{display:flex;flex-direction:column}
.tier .checks{gap:.55rem;flex:1}
.tier .checks li{font-size:.93rem}
.tier .btn{width:100%;margin-top:1.5rem}
.tier.pop .btn-primary:hover{background:var(--gold);color:var(--pine-950)}
.price-groups{display:grid;gap:clamp(1.6rem,3vw,2.4rem)}
.price-group{background:var(--cream);border:1px solid rgba(27,46,36,.09);border-radius:var(--r-lg);padding:clamp(1.4rem,3vw,2.2rem)}
.pg-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:.6rem;margin-bottom:1.1rem}
.pg-head h3{margin:0}
.pg-head a{font-weight:700;font-size:.9rem;text-decoration:none}
.price-list{list-style:none;margin:0;padding:0}
.price-row{display:flex;align-items:baseline;gap:1rem;padding:.95rem 0;border-bottom:1px solid rgba(27,46,36,.08)}
.price-row:last-child{border-bottom:none}
.price-row>div{max-width:34rem}
.price-row b{display:block;color:var(--pine-900);font-size:1rem}
.price-row div span{display:block;font-size:.86rem;color:var(--ink-soft);margin-top:.15rem}
.price-row .dots{flex:1;border-bottom:2px dotted rgba(85,112,74,.35);transform:translateY(-4px);min-width:2rem}
.price-row strong{font-family:var(--serif);font-weight:520;font-size:1.12rem;color:var(--clay);white-space:nowrap}
/* calculator */
.calc{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(1.6rem,3.5vw,3rem);align-items:start}
.calc-form{background:var(--cream);border:1px solid rgba(27,46,36,.09);border-radius:var(--r-lg);padding:clamp(1.5rem,3vw,2.2rem)}
.calc-form fieldset.field{margin-bottom:1.5rem}
.calc-size label{display:flex;align-items:baseline;gap:.4rem;font-weight:700;font-size:.88rem;color:var(--pine-900);margin-bottom:.7rem}
.calc-size output{font-family:var(--serif);font-size:1.3rem;font-weight:520;color:var(--clay);margin-left:.2rem}
.calc-size input[type="range"]{width:100%;accent-color:var(--clay);height:2rem;cursor:pointer}
.calc-scale{display:flex;justify-content:space-between;font-size:.78rem;color:var(--ink-soft);margin-top:.1rem}
.calc-out{background:var(--pine-950);color:#E9E4D5;border-radius:var(--r-lg);padding:clamp(1.7rem,3vw,2.4rem);position:sticky;top:96px}
.calc-out-label{font-size:.78rem;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);margin:0 0 .6rem}
.calc-total{display:block;font-family:var(--serif);font-weight:460;font-size:clamp(2rem,3.6vw,2.9rem);line-height:1.1;color:var(--cream);margin-bottom:.5rem;min-height:1.2em}
.calc-desc{font-size:.95rem;color:var(--sage-lt);margin-bottom:1.2rem}
.calc-notes{list-style:none;margin:0 0 1.6rem;padding:1.1rem 0 0;border-top:1px solid rgba(249,244,233,.15);display:grid;gap:.5rem}
.calc-notes li{font-size:.87rem;color:rgba(233,228,213,.75);padding-left:1.2rem;position:relative}
.calc-notes li::before{content:"—";position:absolute;left:0;color:var(--clay)}
.calc-out .btn{width:100%}

.factors{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1rem,2vw,1.6rem)}
.factor{background:var(--cream);border:1px solid rgba(27,46,36,.09);border-radius:var(--r-md);padding:1.4rem 1.5rem}
.factor h3{font-size:1.08rem;margin-bottom:.4rem}
.factor p{font-size:.92rem;color:var(--ink-soft);margin:0}

/* ---------- legal + thank-you + area pages ---------- */
.legal{max-width:800px}
.legal h2{font-size:1.4rem;margin-top:2.3rem}
.legal .updated{font-size:.9rem;color:var(--ink-soft)}
.thanks{min-height:62vh;display:grid;place-items:center;text-align:center;padding-block:clamp(4rem,9vw,6rem)}
.thanks-ic{width:86px;height:86px;border-radius:50%;background:var(--pine-700);display:grid;place-items:center;margin:0 auto 1.5rem}
.thanks-ic svg{width:42px;height:42px;fill:var(--cream)}
.thanks ol{max-width:430px;margin:1.8rem auto 2.2rem;padding:0;list-style:none;text-align:left;display:grid;gap:.9rem;counter-reset:ts}
.thanks ol li{display:flex;gap:.9rem;align-items:flex-start;color:var(--ink-soft);font-size:.98rem}
.thanks ol li::before{counter-increment:ts;content:counter(ts);flex:none;width:30px;height:30px;border-radius:50%;
  background:var(--sand-2);color:var(--clay);font-weight:700;font-size:.9rem;display:grid;place-items:center}
.fact-lt{background:var(--cream);border:1px solid rgba(27,46,36,.08);border-radius:var(--r-md);padding:1.15rem 1.25rem}
.fact-lt b{display:block;font-family:var(--serif);font-size:1.45rem;font-weight:480;color:var(--clay);line-height:1.1;margin-bottom:.25rem}
.fact-lt span{font-size:.83rem;color:var(--ink-soft);line-height:1.45;display:block}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.8rem}

@media (max-width:860px){
  .nav-item{display:block}
  .nav-item>a .car{display:none}
  .sub{position:static;translate:none;opacity:1;visibility:visible;box-shadow:none;border:none;background:transparent;
    padding:.15rem 0 .55rem .95rem;min-width:0}
  .nav-item:hover .sub,.nav-item:focus-within .sub{translate:none}
  .sub.cols{min-width:0}
  .sub a{white-space:normal;padding:.55rem 0;border-bottom:1px solid rgba(27,46,36,.06);border-radius:0;font-size:.95rem}
  .cookie{left:.8rem;right:calc(.9rem + 66px);bottom:.9rem;max-width:none}
  .chat{right:.9rem;bottom:.9rem}
  .facts{grid-template-columns:1fr 1fr}
  .tiers{grid-template-columns:1fr}
  .tier.pop{order:-1}
  .calc{grid-template-columns:1fr}
  .calc-out{position:static}
  .factors{grid-template-columns:1fr}
  .price-row{flex-wrap:wrap}
  .price-row .dots{display:none}
  .price-row strong{width:100%}
}
"""
