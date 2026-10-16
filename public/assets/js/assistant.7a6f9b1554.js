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

  // Each button is one exact model. This is a convenience list, not a promise
  // of parts stock: customers can enter any unlisted model or choose not sure.
  var MODELS = {
    iPhone: ["iPhone 18 Pro", "iPhone 18 Pro Max", "iPhone 17", "iPhone 17 Pro", "iPhone 17 Pro Max", "iPhone Air", "iPhone 17e",
      "iPhone 16", "iPhone 16 Plus", "iPhone 16 Pro", "iPhone 16 Pro Max", "iPhone 16e",
      "iPhone 15", "iPhone 15 Plus", "iPhone 15 Pro", "iPhone 15 Pro Max",
      "iPhone 14", "iPhone 14 Plus", "iPhone 14 Pro", "iPhone 14 Pro Max",
      "iPhone 13", "iPhone 13 mini", "iPhone 13 Pro", "iPhone 13 Pro Max",
      "iPhone 12", "iPhone 12 mini", "iPhone 12 Pro", "iPhone 12 Pro Max",
      "iPhone 11", "iPhone 11 Pro", "iPhone 11 Pro Max", "iPhone XS", "iPhone XS Max",
      "iPhone XR", "iPhone X", "iPhone 8", "iPhone 8 Plus", "iPhone 7", "iPhone 7 Plus",
      "iPhone SE (3rd generation, 2022)", "iPhone SE (2nd generation, 2020)", "iPhone SE (1st generation, 2016)"],
    Samsung: ["Galaxy S26", "Galaxy S26+", "Galaxy S26 Ultra",
      "Galaxy S25", "Galaxy S25+", "Galaxy S25 Ultra", "Galaxy S25 Edge", "Galaxy S25 FE",
      "Galaxy S24", "Galaxy S24+", "Galaxy S24 Ultra", "Galaxy S24 FE",
      "Galaxy S23", "Galaxy S23+", "Galaxy S23 Ultra", "Galaxy S23 FE",
      "Galaxy S22", "Galaxy S22+", "Galaxy S22 Ultra",
      "Galaxy S21", "Galaxy S21+", "Galaxy S21 Ultra", "Galaxy S21 FE",
      "Galaxy S20", "Galaxy S20+", "Galaxy S20 Ultra", "Galaxy S20 FE",
      "Galaxy S10", "Galaxy S10+", "Galaxy S10e",
      "Galaxy A57 5G", "Galaxy A37 5G", "Galaxy A56 5G", "Galaxy A36 5G", "Galaxy A26 5G",
      "Galaxy A17", "Galaxy A17 5G", "Galaxy A16", "Galaxy A16 5G", "Galaxy A55 5G", "Galaxy A54 5G", "Galaxy A53 5G", "Galaxy A35 5G", "Galaxy A34 5G",
      "Galaxy A25 5G", "Galaxy A15", "Galaxy A15 5G", "Galaxy A14", "Galaxy A14 5G",
      "Galaxy Note20", "Galaxy Note20 Ultra", "Galaxy Note10", "Galaxy Note10+"],
    Other: []
  };

  var state = { brand: "", model: "", repair: "", location: "" };
  var lastPrefilledTown = "";
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

  function revealTop(el) {
    var r = el.getBoundingClientRect(), top = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
    var bar = document.querySelector(".mobile-bar"), bottom = bar && getComputedStyle(bar).display !== "none" ? bar.getBoundingClientRect().top : window.innerHeight;
    if (r.top >= top && r.top + 80 <= bottom) return; // its start is already comfortably visible
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
  }

  function show(idx) {
    stepEls.forEach(function (s, n) { s.classList.toggle("active", n === idx); });
    current = idx;
    if (idx < TOTAL_QUALIFY) setProgress(idx); else setProgress(TOTAL_QUALIFY);
    // move focus to the step heading for screen readers
    var heading = stepEls[idx].querySelector(".q-question, h3, [tabindex='-1']");
    if (heading) { heading.setAttribute("tabindex", "-1"); heading.focus({ preventScroll: true }); }
    // bring the new step's label and question into view (the panel is often taller than a phone screen, so scrolling the
    // whole panel to "nearest" left the new question above the viewport); html scroll-padding keeps it clear of the header
    if (idx > 0) revealTop(stepEls[idx]);
  }

  // ----- Step 1: Brand -----
  root.querySelectorAll("[data-brand]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      state.brand = btn.getAttribute("data-brand");
      state.model = "";
      if (modelSearch) modelSearch.value = "";
      buildModels();
      show(1);
      // Keyboard/screen-reader users land in the labelled model search box,
      // which also announces its hint and the live model count.
      if (modelSearch) modelSearch.focus({ preventScroll: true });
    });
  });

  // ----- Step 2: Model (built dynamically) -----
  var modelWrap = root.querySelector("#q-models");
  var modelSearch = root.querySelector("#q-model-search");
  var modelCount = root.querySelector("#q-model-count");
  var customModel = root.querySelector("#q-model-custom");
  var unsureModel = root.querySelector("#q-model-unsure");
  function modelKey(value) {
    return value.toLowerCase().replace(/\+/g, " plus ").replace(/[^a-z0-9]+/g, " ").trim();
  }
  function chooseModel(model) { state.model = model; show(2); }
  function buildModels() {
    if (!modelWrap) return;
    modelWrap.innerHTML = "";
    var typed = modelSearch ? modelSearch.value.trim() : "";
    var terms = modelKey(typed).split(/\s+/).filter(Boolean);
    var matches = (MODELS[state.brand] || []).filter(function (m) {
      var key = modelKey(state.brand + " " + m);
      return terms.every(function (term) { return key.indexOf(term) !== -1; });
    });
    matches.forEach(function (m) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "q-choice";
      b.textContent = m;
      b.addEventListener("click", function () { chooseModel(m); });
      modelWrap.appendChild(b);
    });
    modelWrap.hidden = matches.length === 0;
    if (modelCount) modelCount.textContent = matches.length ? matches.length + " models — select yours below." :
      (typed ? "No listed match. You can use the model name you've entered." : "Enter your phone's make and model, or choose not sure.");
    if (customModel) {
      customModel.hidden = !typed;
      customModel.textContent = typed ? "Use this model: " + typed : "Use this model";
    }
    var brandLabel = root.querySelector("#q-model-brandlabel");
    if (brandLabel) brandLabel.textContent = state.brand === "Other" ? "Another brand / not sure" : state.brand;
    if (modelSearch) modelSearch.placeholder = state.brand === "iPhone" ? "e.g. iPhone 15 Pro Max" :
      (state.brand === "Samsung" ? "e.g. Galaxy S24 Ultra" : "Enter the full make and model");
  }
  if (modelSearch) {
    modelSearch.addEventListener("input", buildModels);
    modelSearch.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        var buttons = modelWrap.querySelectorAll("button");
        if (buttons.length === 1) buttons[0].click();
        else if (buttons.length) buttons[0].focus();
        else if (modelSearch.value.trim()) customModel.click();
      }
    });
  }
  if (customModel) customModel.addEventListener("click", function () {
    var value = modelSearch.value.trim();
    if (value) chooseModel(value);
  });
  if (unsureModel) unsureModel.addEventListener("click", function () { chooseModel("Not sure"); });

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
  function phoneDescription() {
    if (state.brand === "Other" || modelKey(state.model).indexOf(modelKey(state.brand)) === 0) return state.model;
    return state.brand + " " + state.model;
  }
  function summaryText() {
    return phoneDescription() + " — " + state.repair + " — " + state.location;
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
    // Business name comes from the page (build setting); no hard-coded fallback name.
    var business = root.getAttribute("data-business") || "";
    var waMsg = "Hi" + (business ? " " + enc(business) : "") + ", I'd like a quote.%0A" +
      "Phone: " + enc(phoneDescription()) + "%0A" +
      "Repair: " + enc(state.repair) + "%0A" +
      "Area: " + enc(state.location);
    var waLink = root.querySelector("#q-wa");
    if (waLink) waLink.setAttribute("href", "https://wa.me/" + WA_NUMBER + "?text=" + waMsg);
    // Hidden/structured fields for the form path
    setHidden("brand", state.brand); setHidden("model", state.model);
    // Keep the visible form consistent with the exact stepped selection.
    var phoneModelField = root.querySelector("#f-brandmodel");
    if (phoneModelField) phoneModelField.value = phoneDescription();
    setHidden("repair", state.repair); setHidden("location_qualify", state.location);
    // The visible repair <select> in the form is redundant when the stepped flow
    // already captured it — set its value and hide its field row.
    if (repairField) {
      repairField.value = state.repair;
      if (repairFieldWrap) repairFieldWrap.hidden = true;
      repairField.removeAttribute("required");
    }
    // Refresh an auto-filled town after Back, but keep a customer's manual edit.
    var townField = root.querySelector("#f-town");
    if (townField && (!townField.value || townField.value === lastPrefilledTown)) townField.value = state.location;
    lastPrefilledTown = state.location;
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
      // First real, visible field (skip hidden inputs and the off-screen honeypot).
      var first = detailForm.querySelector('input:not([type="hidden"]):not([tabindex="-1"]), select:not([hidden]), textarea');
      if (first) first.focus();
    });
  }


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
        revealTop(okStep);
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
      revealTop(errStep);
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

  // Deep links such as /get-a-quote/?brand=iPhone open the model step directly
  // (used by the "What phone do you have?" choices). Unknown values are ignored.
  try {
    var pre = new URLSearchParams(window.location.search).get("brand");
    if (pre && Object.prototype.hasOwnProperty.call(MODELS, pre)) {
      state.brand = pre;
      buildModels();
      show(1);
    }
  } catch (e) {}
})();
