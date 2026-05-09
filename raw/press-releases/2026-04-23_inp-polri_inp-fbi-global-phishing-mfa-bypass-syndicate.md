---
source_url: https://inp.polri.go.id/artikel/inp-and-fbi-uncover-global-phishing-syndicate-responsible-for-20-million-loss
publisher: Indonesian National Police (INP) — official English newsroom (inp.polri.go.id)
publish_date: 2026-04-23
fetch_date: 2026-05-09
language: en
fetch_method: curl_cffi chrome124 + BeautifulSoup html.parser
http_status: 200
content_length_chars: 1185
---

# INP and FBI Uncover Global Phishing Syndicate Responsible for $20 Million Loss

**Source:** https://inp.polri.go.id/artikel/inp-and-fbi-uncover-global-phishing-syndicate-responsible-for-20-million-loss
**Outlet:** Indonesian National Police — official English newsroom (`inp.polri.go.id`), maintained by Divisi Humas Polri.
**Published:** 2026-04-23 02:30:00 (frontmatter `pubdate`, `createdate`, `publishdate` meta tags all agree).
**Byline:** `(mg/inp/pr/rs)` — INP Public Relations Division, citing antaranews.com for the official quote.

---

## Body (verbatim)

Inp.polri.go.id - Jakarta. The Indonesian National Police (INP) and the FBI have uncovered a cross-border phishing syndicate that targeted 34,000 victims globally.

Authorities arrested a couple, identified as GWL and FYT, in Jakarta on Wednesday (22/4/2026) for developing and selling malicious scripts that successfully bypassed Multi-Factor Authentication (MFA), resulting in estimated losses of $20 million.

"The INP will not provide space for cybercriminals. Anyone involved, whether creators, sellers, or users, will be dealt with firmly," said Inspector General Nunung Syaifuddin, the Deputy Chief of the Criminal Investigation Agency, as cited by antaranews.com.

Investigations revealed that suspect GWL, a self-taught developer, had been creating phishing tools since 2018, while suspect FYT managed the proceeds via crypto wallets. The syndicate's tools compromised 17,000 accounts, affecting victims in the United States and nine Indonesian corporate entities.

Both suspects face up to 15 years in prison under the Electronic Information and Transactions (ITE) Law for their roles in enabling massive digital fraud and Business Email Compromise (BEC) schemes.

(mg/inp/pr/rs)

---

## Extracted facts

| Field | Value |
|---|---|
| Lead agency | Indonesian National Police (INP) — Bareskrim (Criminal Investigation Agency) |
| Foreign cooperating agency | FBI (United States) |
| Senior official cited | Inspector General Nunung Syaifuddin, Deputy Chief of Bareskrim |
| Suspects | GWL (developer, active since 2018), FYT (cryptocurrency proceeds manager) |
| Suspect relationship | "a couple" |
| Arrest date | 2026-04-22 (Wednesday) |
| Arrest location | Jakarta, Indonesia |
| Modus operandi | Developing and selling malicious scripts that bypassed MFA, enabling BEC |
| Compromised accounts | 17,000 |
| Total victims globally | 34,000 |
| Loss estimate | USD 20 million |
| Indonesian corporate victims | 9 entities |
| US victims | Yes (named explicitly) |
| Charges | Up to 15 years under Indonesia's Electronic Information and Transactions (ITE) Law |
| Cooperation type | Joint investigation / information-sharing across INP–FBI |

## IC scope (≥ 2 country test — PASS)

- **Indonesia** — host state, lead investigation, arrests, prosecution venue.
- **United States** — FBI as named foreign cooperating agency; US victims named explicitly in source.

## Verification notes

- TLS impersonation (`curl_cffi` + `chrome124`) returned HTTP 200 with full article body of 1,185 chars in `div.content`. No Cloudflare/Akamai challenge.
- Publication metadata confirmed by three independent meta tags (`pubdate`, `createdate`, `publishdate`) all set to `2026-04-23 02:30:00`.
- Outlet is the official English-language newsroom of Polri (Indonesian National Police), Humas (Public Relations) division — tier-1 primary source.
- Source explicitly attributes the official quote to antaranews.com (Indonesia's state news agency) — secondary primary source for the quote, but the page itself remains the tier-1 anchor for the operation.
- Distinct from existing wiki entries on Indonesian cybercrime: NOT the W3LL phishing kit takedown (different actors, different toolkit, different jurisdiction lead), NOT the Bali villa raid 2024, NOT Operation Cyber Guardian (which was CSAM, not BEC/phishing).
