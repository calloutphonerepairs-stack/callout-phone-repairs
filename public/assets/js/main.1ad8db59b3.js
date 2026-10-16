/* Call Out Phone Repairs Pontypridd — global behaviour. Vanilla, deferred, progressive enhancement. No analytics. */
(function () {
  "use strict";

  /* ---- Mobile navigation ---- */
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("mobile-menu");
  if (toggle && menu) {
    var closeMenu = function () {
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open menu");
      menu.classList.remove("open");
      document.body.style.overflow = "";
    };
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      toggle.setAttribute("aria-label", open ? "Open menu" : "Close menu");
      if (!open) {
        var hdr = document.querySelector(".site-header");
        if (hdr) document.documentElement.style.setProperty("--menu-top", Math.max(0, Math.round(hdr.getBoundingClientRect().bottom)) + "px");
      }
      menu.classList.toggle("open", !open);
      document.body.style.overflow = !open ? "hidden" : "";
    });
    menu.addEventListener("click", function (e) { if (e.target.closest("a")) closeMenu(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("open")) { closeMenu();
        /* keyboard close: show the focus ring even if the menu was opened by tap. focus() is ignored on an element that
           already has focus (a tapped button keeps it), so release it first. */
        if (document.activeElement === toggle) toggle.blur();
        toggle.focus({ focusVisible: true });
      }
    });
  }

  /* ---- Real header and action-bar heights (responsive correction) ----
     Enlarged text can make the header and the fixed bar taller than the CSS defaults. Measure them so the menu
     panel, scroll offsets and the page's bottom spacing follow the real sizes. If the header and the fixed bar together
     would cover more than 30% of the screen, the header stops being sticky (class on <html>) and scrolls away with the page. */
  (function trackHeights() {
    var root = document.documentElement, header = document.querySelector(".site-header"), bar = document.querySelector(".mobile-bar");
    var measure = function () {
      var bh = 0;
      if (bar) {
        var shown = window.getComputedStyle(bar).display !== "none";
        bh = shown ? bar.offsetHeight : 0;
        if (shown) root.style.setProperty("--stickybar-real", bh + "px"); else root.style.removeProperty("--stickybar-real");
      }
      if (header) {
        var hh = header.offsetHeight;
        root.style.setProperty("--header-h", hh + "px");
        root.classList.toggle("header-static", hh + bh > window.innerHeight * 0.3);
      }
    };
    measure();
    window.addEventListener("resize", measure);
    window.addEventListener("load", measure);
    if (window.ResizeObserver) { var ro = new ResizeObserver(measure); if (header) ro.observe(header); if (bar) ro.observe(bar); }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
  })();

  /* ---- Scroll reveal removed (v4) ----
     Sections are never hidden waiting for an animation. The former observer-based reveal
     could leave content invisible if the observer failed after arming, so it was removed
     at source, and the "reveal" class was removed from the HTML too: the previous live
     stylesheet hid ".reveal" by default, so a cached copy of it must have nothing to hide. */

  /* ---- No analytics (October 2026) ----
     Google Analytics and its consent bar have been removed: nothing loads gtag.js
     and nothing is measured. A visitor who accepted analytics on the old site may
     still hold its cookies, so delete only those Google Analytics cookies (_ga,
     _ga_<id>, legacy _gid/_gat) on each domain variant gtag could have used, plus the
     old consent record. Nothing else in cookies or storage is touched. */
  (function cleanUpOldAnalytics() {
    try { window.localStorage.removeItem("copr-consent"); } catch (e) {}
    var names = document.cookie.split(";").map(function (c) { return c.split("=")[0].trim(); })
      .filter(function (n) { return /^(_ga(_.+)?|_gid|_gat(_.+)?)$/.test(n); });
    if (!names.length) return;
    var host = window.location.hostname, parts = host.split(".");
    var domains = ["", host, "." + host];
    for (var i = 1; i < parts.length - 1; i++) domains.push("." + parts.slice(i).join("."));
    names.forEach(function (name) {
      domains.forEach(function (d) {
        document.cookie = name + "=; Max-Age=0; path=/" + (d ? "; domain=" + d : "") + "; SameSite=Lax";
      });
    });
  })();
})();

/* Repair motion player (home hero). Runs only with no reduced-motion preference; deferred, so it never blocks parsing or first
   paint. Plays once when the phone first enters view, then marks html.rm-done (CSS hides the cracked state). No inline script
   is needed, so the site's Content-Security-Policy stays unchanged. */
(function () {
  var root = document.documentElement;
  if (root.classList.contains("rm-done") || !window.matchMedia || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var hero = document.querySelector(".hero.d2r"), dev = hero && hero.querySelector(".d2r-device");
  var done = false;
  function finish() { if (done) return; done = true; if (hero) hero.classList.remove("is-repairing"); root.classList.add("rm-done"); }
  if (!dev || !("IntersectionObserver" in window)) { finish(); return; }
  function play() { if (done || hero.classList.contains("is-repairing")) return; hero.classList.add("is-repairing"); setTimeout(finish, 2600); }
  // Cracked hold (v4): the timer starts only once the tab is visible and a frame showing the phone has been painted
  // (two animation frames after the visibility check), so the visitor sees the cracked screen for about 1.1 s before the
  // existing repair transition (600 ms here + the transition's own 0.5-0.55 s delay before anything moves).
  var HOLD = 600;
  function holdThenPlay() {
    if (document.visibilityState === "hidden") {
      var onVis = function () { if (document.visibilityState !== "hidden") { document.removeEventListener("visibilitychange", onVis); holdThenPlay(); } };
      document.addEventListener("visibilitychange", onVis); return;
    }
    requestAnimationFrame(function () { requestAnimationFrame(function () { setTimeout(play, HOLD); }); });
  }
  function watch() {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        // 35% of the phone visible, or (very tall phone at enlarged text) the phone filling half the screen
        if (e.isIntersecting && (e.intersectionRatio >= 0.35 || e.intersectionRect.height >= window.innerHeight * 0.5)) { io.disconnect(); holdThenPlay(); }
      });
    }, { threshold: [0, 0.1, 0.2, 0.35, 0.6] });
    io.observe(dev);
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(watch, watch); else watch();
  var mq = window.matchMedia("(prefers-reduced-motion: reduce)");
  if (mq.addEventListener) mq.addEventListener("change", function () { if (mq.matches) finish(); });
})();
