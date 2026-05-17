---
source_type: press-release
title: "FBI, DC3, and NPA Identification of North Korean Cyber Actors, Tracked as TraderTraitor, Responsible for Theft of $308 Million USD from Bitcoin.DMM.com"
publisher: "Federal Bureau of Investigation (FBI) — National Press Office (in joint name with DC3 and NPA Japan)"
publish_date: "2024-12-24"
language: en
source_url: "https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom"
companion_url_npa_ja: "https://www.npa.go.jp/bureau/cyber/koho/caution/caution20241224.html"
companion_url_cyber_go_jp_en_pdf: "https://www.cyber.go.jp/eng/pdf/Alert_TraderTraitor.pdf"
reliability: high
credibility: confirmed
sensitivity: public
ingest_date: 2026-05-17
fetch_status: "URL is FBI own-domain press release. Direct WebFetch returned HTTP 403 — FBI is on the wiki's BOT_PROTECTED_DOMAINS whitelist (per LESSONS L11, L13) and Cloudflare/Akamai bot protection routinely returns 403 to non-browser clients despite the URL being live in a browser. Content cross-confirmed via NPA-side own-domain joint advisory (npa.go.jp), cyber.go.jp/eng English-language companion PDF, and multiple secondary news outlets (The Record, SecurityWeek, SecurityAffairs, Beyond Identity, Dark Web Informer) reproducing the FBI press release text verbatim."
---

# FBI, DC3, and NPA Identification of North Korean Cyber Actors, Tracked as TraderTraitor, Responsible for Theft of $308 Million USD from Bitcoin.DMM.com

**Publisher**: Federal Bureau of Investigation (FBI) — National Press Office, in joint name with U.S. Department of Defense Cyber Crime Center (DC3) and the National Police Agency of Japan (NPA)
**Date**: 2024-12-24
**URL (own-domain primary)**: https://www.fbi.gov/news/press-releases/fbi-dc3-and-npa-identification-of-north-korean-cyber-actors-tracked-as-tradertraitor-responsible-for-theft-of-308-million-from-bitcoindmmcom

## Companion documents (joint publication, own-domain)

- NPA Japan primary (Japanese): https://www.npa.go.jp/bureau/cyber/koho/caution/caution20241224.html
- NPA Japanese-language PDF: https://www.npa.go.jp/bureau/cyber/pdf/020241224_pa.pdf
- NPA / NISC English-language PDF: https://www.cyber.go.jp/eng/pdf/Alert_TraderTraitor.pdf

## Key statements (verbatim, English)

> The Federal Bureau of Investigation, Department of Defense Cyber Crime Center, and National Police Agency of Japan alerted the public to the theft of cryptocurrency worth $308 million U.S. dollars from the Japan-based cryptocurrency company DMM by North Korean cyber actors in May 2024.

> The theft is affiliated with TraderTraitor threat activity, which is also tracked as Jade Sleet, UNC4899, and Slow Pisces.

> TraderTraitor activity is often characterized by targeted social engineering directed at multiple employees of the same company simultaneously.

> The FBI, National Police Agency of Japan, and other U.S. government and international partners will continue to expose and combat North Korea's use of illicit activities — including cybercrime and cryptocurrency theft — to generate revenue for the regime.

## Attack chain (FBI/DC3/NPA joint attribution)

- **Late March 2024** — A North Korean cyber actor masquerading as a recruiter on LinkedIn contacted an employee at **Ginco**, a Japan-based enterprise cryptocurrency wallet software company, and sent the target a URL linked to a malicious Python script under the guise of a pre-employment test on a GitHub page.
- **After mid-May 2024** — TraderTraitor actors exploited session cookie information to impersonate the compromised employee and gained access to Ginco's unencrypted communications system.
- **Late May 2024** — Actors likely used this access to manipulate a legitimate transaction request by a DMM employee, resulting in the loss of **4,502.9 BTC ≈ USD 308 million** at the time of the attack.

## Cooperating agencies (named verbatim in joint advisory, US-side framing)

| Agency | Country | Role |
|---|---|---|
| Federal Bureau of Investigation (FBI) | United States | Co-attribution lead (US side) |
| Department of Defense Cyber Crime Center (DC3) | United States | Co-attribution and technical analysis |
| National Police Agency of Japan (警察庁 / NPA) | Japan | Co-attribution lead (Japan side) |

The press release is published in joint name on the FBI's own domain (us-side anchor) and simultaneously by NPA Japan on `npa.go.jp` (japan-side anchor) plus a companion English-language PDF on `cyber.go.jp/eng`. This is one of a small number of US-Japan **joint name** cyber-attribution products — distinct from parallel-but-separate national statements.

## Threat-actor profile (FBI attribution)

TraderTraitor is identified by FBI as a North Korea-backed cyber attack group. The FBI release also confirms the cluster is tracked as **Jade Sleet**, **UNC4899**, and **Slow Pisces** by other threat-intelligence providers; in an April 2022 joint advisory with CISA and U.S. Treasury, FBI confirmed that DPRK-backed entities behind TraderTraitor are tracked as **Lazarus Group**, **APT38**, **BlueNoroff**, and **Stardust Chollima**.

## IC significance (FBI / US-side framing)

This is the FBI side of a US-Japan joint operational cyber-attribution. By publishing in joint name with NPA Japan (rather than as a unilateral FBI release citing Japanese cooperation), the FBI signals that the underlying technical and forensic attribution rests on jointly-developed evidence under bilateral US-Japan cyber-cooperation arrangements — including FBI's standing liaison with NPA, the Budapest Convention 24/7 contact network (both states are parties), and informal LE-to-LE technical exchange.

## Wiki ingest notes

- Pages updated: `[[tradertraitor-dmm-bitcoin-cryptocurrency-theft-joint-attribution-2024]]`
- This source is the US-side own-domain anchor for the joint advisory. The Japan-side own-domain anchor (`npa.go.jp`) is filed separately at `raw/press-releases/2024-12-24_npa-japan_tradertraitor-dmm-bitcoin-fbi-dc3-joint-attribution.md` (already ingested).
- Tier-1 own-domain publisher: FBI National Press Office (www.fbi.gov) — passes L24/L25 strict tier-1 test.
- Fetch behaviour: FBI URLs are Cloudflare/Akamai bot-protected (L11/L13) and routinely return 403 to non-browser clients. The URL is verified live by multiple secondary outlets reproducing the FBI text on the same publication date (2024-12-24) and by the joint-publication structure with NPA Japan.
