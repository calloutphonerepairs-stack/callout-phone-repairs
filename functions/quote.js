/**
 * Cloudflare Pages Function — /quote
 * Handles quote & contact form submissions.
 *
 * Responsibilities:
 *   - Full server-side validation
 *   - Spam protection (honeypot + basic checks)
 *   - Deliver enquiry to calloutphonerepairs@gmail.com via Resend
 *   - Never fail silently: always return a clear JSON status
 *
 * EMAIL PROVIDER: Resend (https://resend.com).
 *   The API key is read from the environment variable RESEND_API_KEY.
 *   It is NEVER hardcoded and NEVER exposed to the client (this file runs
 *   server-side only, on Cloudflare's edge). If RESEND_API_KEY is missing,
 *   the function returns a friendly configuration error (HTTP 503) instead
 *   of crashing, and the client shows its WhatsApp/Call fallback.
 *
 * Post-deploy configuration required (see README / deploy notes):
 *   - Cloudflare Pages env var: RESEND_API_KEY (Production + Preview)
 *   - Resend: verify the sending domain send.calloutphonerepairs.co.uk
 *     and add the DNS records Resend provides (SPF/DKIM, + DMARC recommended).
 */

// Where enquiries are delivered.
const DESTINATION = "calloutphonerepairs@gmail.com";

// Verified Resend sender (must be on a domain verified in Resend).
// Using a dedicated subdomain (send.calloutphonerepairs.co.uk) is best practice
// so transactional mail is isolated from any mail on the root domain.
const FROM = "Website Enquiries <quotes@send.calloutphonerepairs.co.uk>";

export async function onRequestPost(context) {
  const { request, env } = context;
  try {
    const form = await request.formData();

    // Detect a no-JavaScript submission (a normal browser form navigation) vs.
    // the JS fetch(). Native navigations send Sec-Fetch-Mode: navigate and an
    // Accept: text/html preference; fetch() does not. For no-JS submitters we
    // return a proper HTML page instead of raw JSON.
    const sfm = request.headers.get("Sec-Fetch-Mode") || "";
    const accept = request.headers.get("Accept") || "";
    const wantsHtml = sfm === "navigate" || (accept.includes("text/html") && sfm !== "cors" && sfm !== "same-origin");
    const reply = (obj, status = 200) => (wantsHtml ? htmlResponse(obj, status) : json(obj, status));

    // 1) Honeypot — bots fill hidden fields
    if ((form.get("company") || "").trim() !== "") {
      // Pretend success to the bot; do nothing.
      return reply({ ok: true });
    }

    // 2) Collect + validate
    const data = {
      name: clean(form.get("name")),
      phone: clean(form.get("phone")),
      email: clean(form.get("email")),
      contact_pref: clean(form.get("contact_pref")),
      town: clean(form.get("town")),
      brand: clean(form.get("brand")),
      model: clean(form.get("model")),
      phone_model: clean(form.get("phone_model")),
      repair: clean(form.get("repair")),
      description: clean(form.get("description")),
      consent: form.get("consent") ? "yes" : "no",
      source: clean(form.get("source")) || "website",
      submitted_at: new Date().toISOString(),
    };

    const errors = [];
    if (!data.name) errors.push("name");
    if (!/[0-9]{6,}/.test((data.phone || "").replace(/\s/g, ""))) errors.push("phone");
    if (!data.town) errors.push("town");
    if (data.consent !== "yes") errors.push("consent");

    if (errors.length) {
      return reply({ ok: false, error: "validation", fields: errors }, 400);
    }

    // 3) Deliver. Never fail silently.
    const delivered = await sendEmail(env, data);
    if (!delivered.ok) {
      // Missing configuration -> friendly 503 (server not ready), not a crash.
      if (delivered.configError) {
        return reply(
          {
            ok: false,
            error: "not_configured",
            message:
              "Sorry — our online form isn't quite ready to send yet. Please reach us on WhatsApp or by phone and we'll help straight away.",
          },
          503
        );
      }
      // Genuine delivery failure -> 502, so the client shows WhatsApp/Call fallback.
      return reply(
        { ok: false, error: "delivery", message: delivered.message || "Could not send right now." },
        502
      );
    }

    return reply({ ok: true });
  } catch (err) {
    return json({ ok: false, error: "server", message: "Unexpected error." }, 500);
  }
}

// Reject non-POST cleanly.
export async function onRequest(context) {
  if (context.request.method !== "POST") {
    return new Response("Method Not Allowed", { status: 405, headers: { Allow: "POST" } });
  }
  return onRequestPost(context);
}

function clean(v) {
  return (v == null ? "" : String(v)).trim().slice(0, 2000);
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", "Cache-Control": "no-store" },
  });
}

/**
 * HTML response for no-JavaScript submitters, so they never land on raw JSON.
 * Mirrors the site's look minimally (no external assets) and always offers
 * WhatsApp/Call as a fallback. Success and error variants.
 */
function htmlResponse(obj, status = 200) {
  const ok = obj && obj.ok === true;
  const WA = "https://wa.me/447347715961";
  const TEL = "tel:+447347715961";
  const heading = ok ? "Thanks — we've got your enquiry" : "That didn't send";
  let message;
  if (ok) {
    message =
      "We'll be in touch during our hours (08:00–20:00, daily) with a price and a time that works for you. Nothing is booked until we've spoken.";
  } else if (obj && obj.error === "validation") {
    message =
      "Some details were missing or looked incorrect (please check your name, phone number, town and that you ticked consent), then go back and try again.";
  } else {
    message =
      "Something went wrong on our side and your enquiry wasn't sent. Please message us on WhatsApp or give us a call — we'll help straight away.";
  }
  const accent = ok ? "#2563EB" : "#B91C1C";
  const body = `<!DOCTYPE html>
<html lang="en-GB"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>${ok ? "Enquiry sent" : "Enquiry not sent"} — Call Out Phone Repairs</title>
<style>
  body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:#F8FAFC;color:#0F172A;line-height:1.6}
  .wrap{max-width:560px;margin:0 auto;padding:48px 24px;min-height:100vh;display:flex;flex-direction:column;justify-content:center}
  .card{background:#fff;border:1px solid #E2E8F0;border-radius:16px;padding:32px;box-shadow:0 12px 32px rgba(15,23,42,.06)}
  h1{font-size:1.5rem;margin:0 0 12px;color:${accent}}
  p{margin:0 0 20px;color:#475569}
  .btns{display:flex;flex-direction:column;gap:12px}
  a.btn{display:block;text-align:center;text-decoration:none;font-weight:600;padding:14px 20px;border-radius:12px;border:1.5px solid #E2E8F0}
  a.primary{background:#2563EB;color:#fff;border-color:#2563EB}
  a.wa{background:#25D366;color:#06301B;border-color:#25D366}
  a.ghost{background:#fff;color:#0F172A}
</style></head>
<body><div class="wrap"><div class="card">
  <h1>${heading}</h1>
  <p>${message}</p>
  <div class="btns">
    ${ok ? "" : `<a class="btn wa" href="${WA}">Message us on WhatsApp</a><a class="btn ghost" href="${TEL}">Call 07347 715961</a>`}
    <a class="btn ${ok ? "primary" : "ghost"}" href="/">Back to the website</a>
  </div>
</div></div></body></html>`;
  return new Response(body, {
    status,
    headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" },
  });
}

/**
 * Email delivery via Resend.
 * Returns:
 *   { ok: true }                                   on success
 *   { ok: false, message, code? }                  on failure
 *   { ok: false, configError: true, message }      when RESEND_API_KEY is absent
 *
 * The API key is read from env.RESEND_API_KEY (Cloudflare Pages env var).
 * It is never hardcoded and never sent to the browser.
 */
async function sendEmail(env, data) {
  // 10) Missing key -> friendly configuration error, no crash.
  const apiKey = env && env.RESEND_API_KEY;
  if (!apiKey) {
    return {
      ok: false,
      configError: true,
      message: "Email is not configured yet (missing RESEND_API_KEY).",
    };
  }

  const deviceLabel =
    [data.brand, data.model].filter(Boolean).join(" ") ||
    data.phone_model ||
    "(device not specified)";
  const subject = `New quote enquiry — ${deviceLabel} — ${data.town}`;

  // Plain-text body (primary — reliable in every mail client).
  const text =
`New enquiry from the Call Out Phone Repairs website.

Name:            ${data.name}
Phone:           ${data.phone}
Email:           ${data.email || "(not provided)"}
Preferred:       ${data.contact_pref || "(not specified)"}
Town/Postcode:   ${data.town}

Phone brand:     ${data.brand || "(not provided)"}
Phone model:     ${data.model || "(not provided)"}
Phone (typed):   ${data.phone_model || "(not provided)"}
Repair needed:   ${data.repair || "(not specified)"}
Description:     ${data.description || "(none)"}

Consent given:   ${data.consent}
Source:          ${data.source}
Submitted:       ${data.submitted_at}
`;

  // Lightweight HTML version (all values escaped to prevent injection).
  const rows = [
    ["Name", data.name],
    ["Phone", data.phone],
    ["Email", data.email || "(not provided)"],
    ["Preferred contact", data.contact_pref || "(not specified)"],
    ["Town / Postcode", data.town],
    ["Phone brand", data.brand || "(not provided)"],
    ["Phone model", data.model || "(not provided)"],
    ["Phone (typed)", data.phone_model || "(not provided)"],
    ["Repair needed", data.repair || "(not specified)"],
    ["Description", data.description || "(none)"],
    ["Consent given", data.consent],
    ["Source", data.source],
    ["Submitted", data.submitted_at],
  ]
    .map(
      ([k, v]) =>
        `<tr><td style="padding:4px 12px 4px 0;color:#475569;white-space:nowrap;vertical-align:top">${escapeHtml(
          k
        )}</td><td style="padding:4px 0;color:#0F172A">${escapeHtml(v)}</td></tr>`
    )
    .join("");
  const html =
    `<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;line-height:1.5;color:#0F172A">` +
    `<p style="margin:0 0 12px">New enquiry from the Call Out Phone Repairs website.</p>` +
    `<table style="border-collapse:collapse">${rows}</table>` +
    `</div>`;

  // Build the Resend payload. Reply-To is set to the customer's email (6)
  // ONLY when they supplied a valid-looking address, so a reply goes to them.
  const payload = {
    from: FROM,
    to: [DESTINATION],
    subject,
    text,
    html,
  };
  if (data.email && /.+@.+\..+/.test(data.email)) {
    payload.reply_to = data.email;
  }

  try {
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      return { ok: true };
    }

    // Surface a useful (non-secret) reason for logs / the 502 response.
    let detail = "";
    try {
      const errBody = await res.json();
      detail = errBody && (errBody.message || errBody.error || "");
    } catch (_) {
      /* ignore parse issues */
    }
    return {
      ok: false,
      code: res.status,
      message: `Email provider returned ${res.status}${detail ? `: ${detail}` : ""}`,
    };
  } catch (e) {
    return { ok: false, message: "Could not reach the email provider." };
  }
}

// Escape user-supplied values for safe HTML embedding.
function escapeHtml(v) {
  return String(v == null ? "" : v).replace(/[&<>"']/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
  });
}
