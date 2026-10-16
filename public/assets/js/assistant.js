/* Quote Assistant — vanilla, progressive enhancement.
   Enhances a plain <form> (which works without JS) into a stepped app-like flow.
   Never shows prices. Never confirms a booking. Delivers details to the Pages Function. */
(function () {
  "use strict";

  var root = document.getElementById("quote-assistant");
  if (!root) return;

  var WA_NUMBER = "447347715961";

  // ---- Progressive enhancement bootstrap ----
  // The plain form (#quote-form inside #q-plain) is the no-JS default.
  // Move it into the stepped flow's finish slot, then reveal the stepped UI.
  var plainWrap = root.querySelector("#q-plain");
  var stepped = root.querySelector(".q-stepped");
  var formSlot = root.querySelector("#q-form-slot");
  var theForm = root.querySelector("#quote-form");
  if (!stepped || !theForm) return; // nothing to enhance; leave plain form working
  if (formSlot && theForm) {
    formSlot.appendChild(theForm);   // relocate the real form into the finish step
    theForm.hidden = true;           // hidden until the user chooses "send my details"
    theForm.noValidate = true;       // JS handles validation now; suppress native bubbles (no source-level novalidate, so no-JS keeps native validation)
  }
  // Now that JS custom validation is active, disable native validation to avoid
  // double messaging. (Removed from source HTML so no-JS keeps native validation.)
  theForm.setAttribute("novalidate", "");
  // The stepped flow captures brand/model/repair/location itself, so inject hidden
  // fields to carry those structured values, and hide the visible repair <select>
  // (its value is set from the stepped choice). If the user opens the form directly,
  // the select is revealed again by q-show-form logic below.
  function ensureHidden(name) {
    var el = theForm.querySelector('input[name="' + name + '"]');
    if (!el) { el = document.createElement("input"); el.type = "hidden"; el.name = name; theForm.appendChild(el); }
    return el;
  }
  ensureHidden("brand"); ensureHidden("model");
  var repairField = theForm.querySelector('#f-repair');
  var repairFieldWrap = repairField ? repairField.closest(".field") : null;
  if (plainWrap) plainWrap.setAttribute("data-enhanced", "true"); // CSS hides it
  stepped.hidden = false;            // reveal the stepped experience

  // Model lists (generic, non-exhaustive; "Other / not sure" always available).
  var MODELS = {
    iPhone: ["iPhone 15 / Plus / Pro / Pro Max", "iPhone 14 / Plus / Pro / Pro Max", "iPhone 13 / mini / Pro / Pro Max", "iPhone 12 / mini / Pro / Pro Max", "iPhone 11 / Pro", "iPhone SE / XR / X", "Older / not sure"],
    Samsung: ["Galaxy S24 / S23 / S22", "Galaxy S21 / S20 / S10", "Galaxy A-series", "Galaxy Note", "Galaxy Z Fold / Flip", "Older / not sure"],
    Other: ["Google Pixel", "OnePlus", "Huawei", "Motorola", "Xiaomi", "Another brand / not sure"]
  };

  var state = { brand: "", model: "", repair: "", location: "" };
  var stepEls = Array.prototype.slice.call(root.querySelectorAll(".q-step"));
  var progressEl = root.querySelector(".q-progress");
  var current = 0;
  var TOTAL_QUALIFY = 4; // brand, model, repair, location

  // Build progress segments
  if (progressEl) {
    for (var i = 0; i < TOTAL_QUALIFY; i++) {
      var seg = document.createElement("div");
      seg.className = "q-progress-seg";
      seg.innerHTML = '<span class="fill"></span>';
      progressEl.appendChild(seg);
    }
  }

  function setProgress(idx) {
    if (!progressEl) return;
    var segs = progressEl.querySelectorAll(".q-progress-seg");
    segs.forEach(function (s, n) {
      s.classList.toggle("done", n < idx);
      s.classList.toggle("active", n === idx);
    });
  }

  function show(idx) {
    stepEls.forEach(function (s, n) { s.classList.toggle("active", n === idx); });
    current = idx;
    if (idx < TOTAL_QUALIFY) setProgress(idx); else setProgress(TOTAL_QUALIFY);
    // move focus to the step heading for screen readers
    var heading = stepEls[idx].querySelector(".q-question, h3, [tabindex='-1']");
    if (heading) { heading.setAttribute("tabindex", "-1"); heading.focus({ preventScroll: true }); }
    // keep the shell in view on mobile
    var shell = root.querySelector(".quote-shell");
    if (shell && idx > 0) shell.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  // ----- Step 1: Brand -----
  root.querySelectorAll("[data-brand]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      state.brand = btn.getAttribute("data-brand");
      buildModels();
      show(1);
    });
  });

  // ----- Step 2: Model (built dynamically) -----
  var modelWrap = root.querySelector("#q-models");
  function buildModels() {
    if (!modelWrap) return;
    modelWrap.innerHTML = "";
    (MODELS[state.brand] || MODELS.Other).forEach(function (m) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "q-choice";
      b.textContent = m;
      b.addEventListener("click", function () { state.model = m; show(2); });
      modelWrap.appendChild(b);
    });
    var brandLabel = root.querySelector("#q-model-brandlabel");
    if (brandLabel) brandLabel.textContent = state.brand;
  }

  // ----- Step 3: Repair -----
  root.querySelectorAll("[data-repair]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      state.repair = btn.getAttribute("data-repair");
      show(3);
    });
  });

  // ----- Step 4: Location -> Finish -----
  var locInput = root.querySelector("#q-location");
  var locBtn = root.querySelector("#q-location-next");
  var locError = root.querySelector("#q-location-error");
  if (locBtn) {
    locBtn.addEventListener("click", function () {
      var v = (locInput.value || "").trim();
      if (v.length < 2) {
        locInput.setAttribute("aria-invalid", "true");
        locInput.closest(".field").classList.add("invalid");
        if (locError) locError.textContent = "Please enter your town or postcode so we know we can reach you.";
        locInput.focus();
        return;
      }
      locInput.removeAttribute("aria-invalid");
      locInput.closest(".field").classList.remove("invalid");
      state.location = v;
      renderFinish();
      show(4);
    });
    locInput.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); locBtn.click(); } });
  }

  // ----- Finish step -----
  function summaryText() {
    return state.brand + " " + state.model + " — " + state.repair + " — " + state.location;
  }
  function renderFinish() {
    var chips = root.querySelector("#q-summary");
    if (chips) {
      chips.innerHTML = "";
      [["Phone", state.brand], ["Model", state.model], ["Repair", state.repair], ["Area", state.location]].forEach(function (pair) {
        var c = document.createElement("span");
        c.className = "q-chip";
        c.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>' + escapeHtml(pair[1]);
        chips.appendChild(c);
      });
    }
    // Pre-fill WhatsApp
    var waMsg = "Hi Call Out Phone Repairs, I'd like a quote.%0A" +
      "Phone: " + enc(state.brand + " " + state.model) + "%0A" +
      "Repair: " + enc(state.repair) + "%0A" +
      "Area: " + enc(state.location);
    var waLink = root.querySelector("#q-wa");
    if (waLink) waLink.setAttribute("href", "https://wa.me/" + WA_NUMBER + "?text=" + waMsg);
    // Hidden/structured fields for the form path
    setHidden("brand", state.brand); setHidden("model", state.model);
    setHidden("repair", state.repair); setHidden("location_qualify", state.location);
    // The visible repair <select> in the form is redundant when the stepped flow
    // already captured it — set its value and hide its field row.
    if (repairField) {
      repairField.value = state.repair;
      if (repairFieldWrap) repairFieldWrap.hidden = true;
      repairField.removeAttribute("required");
    }
    // Prefill visible town field if empty
    var townField = root.querySelector("#f-town");
    if (townField && !townField.value) townField.value = state.location;
  }
  function enc(s){ return encodeURIComponent(s); }
  function escapeHtml(s){ return String(s).replace(/[&<>"']/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]; }); }
  function setHidden(name, val){ var el = root.querySelector('[name="'+name+'"]'); if (el) el.value = val; }

  // Back buttons
  root.querySelectorAll("[data-back]").forEach(function (btn) {
    btn.addEventListener("click", function () { show(Math.max(0, current - 1)); });
  });

  // Toggle the "send details" form open within finish
  var showFormBtn = root.querySelector("#q-show-form");
  var detailForm = theForm; // the relocated #quote-form
  if (showFormBtn && detailForm) {
    showFormBtn.addEventListener("click", function () {
      detailForm.hidden = false;
      showFormBtn.hidden = true;
      var first = detailForm.querySelector("input, select, textarea");
      if (first) first.focus();
    });
  }

  if (window.coprTrack) {
    root.querySelectorAll("#q-wa").forEach && root.querySelectorAll("#q-wa").forEach(function(){});
  }
  var waFinish = root.querySelector("#q-wa");
  if (waFinish) waFinish.addEventListener("click", function(){ if (window.coprTrack) window.coprTrack("quote_whatsapp", { summary: summaryText() }); });

  // ----- Form submission (fetch to Pages Function; graceful fallback) -----
  var form = root.querySelector("#quote-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validateForm(form)) return;
      var submitBtn = form.querySelector("[type=submit]");
      var original = submitBtn ? submitBtn.textContent : "";
      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Sending…"; }

      var data = new FormData(form);
      fetch(form.getAttribute("action") || "/quote", { method: "POST", body: data })
        .then(function (r) {
          // Only a 2xx counts. Parse body and require ok:true too, so a
          // misconfigured backend can never trigger a false success screen.
          if (!r.ok) return Promise.reject(r);
          return r.json().then(function (body) {
            if (body && body.ok === true) return body;
            return Promise.reject(body || {});
          }).catch(function () { return Promise.reject({}); });
        })
        .then(function () {
          gotoResult(true);
          if (window.coprTrack) window.coprTrack("quote_form_submit", { summary: summaryText() });
        })
        .catch(function () {
          // Failure: keep the user's entered data in the fields, show error + WA/Call.
          gotoResult(false);
          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = original; }
        });
    });
  }

  function gotoResult(ok) {
    if (ok) {
      // Success: replace the flow with the success panel.
      stepEls.forEach(function (s) { s.classList.remove("active"); });
      var okStep = root.querySelector("#q-success");
      if (okStep) {
        okStep.classList.add("active");
        var h = okStep.querySelector("h3"); if (h){ h.setAttribute("tabindex","-1"); h.focus(); }
        okStep.scrollIntoView({ behavior: "smooth", block: "center" });
      }
      if (progressEl) setProgress(TOTAL_QUALIFY);
      return;
    }
    // Failure: DO NOT hide the finish step — the user's data must stay in the
    // form and remain editable/retryable. Reveal the error panel inline above it.
    var errStep = root.querySelector("#q-error");
    if (errStep) {
      errStep.classList.add("active");
      var eh = errStep.querySelector("h3"); if (eh){ eh.setAttribute("tabindex","-1"); eh.focus(); }
      errStep.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  function validateForm(f) {
    var ok = true;
    f.querySelectorAll("[required]").forEach(function (el) {
      var wrap = el.closest(".field") || el.closest(".consent");
      var valid = el.type === "checkbox" ? el.checked : (el.value || "").trim().length > 0;
      if (el.type === "tel") valid = /[0-9]{6,}/.test((el.value||"").replace(/\s/g,""));
      if (!valid) {
        ok = false;
        el.setAttribute("aria-invalid", "true");
        if (wrap) wrap.classList.add("invalid");
      } else {
        el.removeAttribute("aria-invalid");
        if (wrap) wrap.classList.remove("invalid");
      }
    });
    if (!ok) {
      var firstBad = f.querySelector('[aria-invalid="true"]');
      if (firstBad) firstBad.focus();
    }
    return ok;
  }

  // init
  setProgress(0);
})();
