// Sage & Stone — progressive enhancement. ~2 KB, no dependencies.
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

  // Lead form — placeholder handler. Swap for the GHL form embed at launch;
  // keep field names (name/phone/email/service/message) for tracking parity.
  // On success the visitor lands on the thank-you page (a clean conversion
  // URL for GA4/ads goals). Nothing is transmitted in this demo build.
  var form = document.getElementById("lead-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      window.location.href = "thank-you.html";
    });
  }

  // Cookie banner. No analytics load unless the visitor allows them —
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
