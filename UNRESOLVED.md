# Unresolved Items — needs your input before launch

Nothing below is fabricated or guessed. Where a fact was unknown, the copy was written to be true but non-specific, with an internal HTML-comment `DEV:` marker in the source (never visible to customers). These are the only outstanding items.

| # | Item | Where | What's needed | Blocks launch? |
|---|------|-------|---------------|----------------|
| 1 | **Email delivery config** (code is done) | `functions/quote.js` uses Resend | Code complete. You only need to: verify `send.calloutphonerepairs.co.uk` in Resend + add its DNS records, and set the `RESEND_API_KEY` env var in Cloudflare Pages, then redeploy. Full steps in README → "Post-deploy configuration". | Form email only — WhatsApp/Call work now; form fails safely to them until the key is set. |
| 2 | **Owner name / bio** | `/about/` | Your name (and any honest detail) for the About page and optional `Person` schema. | No — page is live and honest without it. |
| 3 | **Supported model ranges** | `/screen-repair/iphone/`, `/screen-repair/samsung/` | Exact model ranges you service, if you want them stated. Currently neutral ("a range of… tell us your model and we'll confirm"). | No. |
| 4 | **Google review link + rating** | `/reviews/` | Your Google Business Profile review link once live. No star rating anywhere until you provide a verified current rating. | No. |
| 5 | **Privacy policy legal review** | `/privacy-policy/` | Check against ICO / UK GDPR guidance; confirm data-controller details. Current text is a plain-English starting point. | Recommended before launch. |
| 6 | **Real photos (optional, later)** | site-wide | Launch is intentionally illustration-led. Real photos can be added later as earned — never fabricated. | No. |
| 7 | **Photo upload (removed for launch)** | quote form | Deliberately removed — customers send photos via WhatsApp. If you later want in-form photo upload, it needs image storage (e.g. Cloudflare R2) or email attachment wiring; ask and it can be added post-launch. | No. |

## Highest-impact next action

Get your **Google Business Profile** live and start earning **genuine reviews**. Trust signals are thin at launch (no reviews, no photos) — unavoidable, not a design flaw. The site holds the review slots; real reviews are the compounding asset on-page work can't replace, especially for the map pack.

## Honest ranking note

No ranking guarantees. This is the strongest realistic foundation. Distant towns (Cardiff, Merthyr) are an organic long-game — the pages are honest about proximity and compete on the come-to-you angle, not on promises.
