/* Call Out Phone Repairs — global behaviour. Vanilla, deferred, progressive enhancement. */
(function () {
  "use strict";

  /* ---- Mobile navigation ---- */
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("mobile-menu");
  if (toggle && menu) {
    var closeMenu = function () {
      toggle.setAttribute("aria-expanded", "false");
      menu.classList.remove("open");
      document.body.style.overflow = "";
    };
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      menu.classList.toggle("open", !open);
      document.body.style.overflow = !open ? "hidden" : "";
    });
    menu.addEventListener("click", function (e) {
      if (e.target.tagName === "A") closeMenu();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("open")) { closeMenu(); toggle.focus(); }
    });
  }

  /* ---- Scroll reveal (respects reduced motion) ---- */
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (!reduceMotion && "IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("in"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- Lightweight click tracking (no dependency; hooks analytics if present) ---- */
  function track(name, detail) {
    try {
      if (window.dataLayer) window.dataLayer.push({ event: name, detail: detail });
      // Cloudflare Web Analytics / custom endpoint can be wired here later.
      document.dispatchEvent(new CustomEvent("copr:track", { detail: { name: name, data: detail } }));
    } catch (e) {}
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a");
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("wa.me") > -1) track("whatsapp_click", { where: a.dataset.where || "link" });
    else if (href.indexOf("tel:") === 0) track("call_click", { where: a.dataset.where || "link" });
  });
  window.coprTrack = track;
})();
