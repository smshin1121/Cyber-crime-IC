---
type: source
title: "FBI + DC3 + NPA joint attribution — TraderTraitor / DMM Bitcoin $308M cryptocurrency theft (US-side own-domain, 2024-12-24)"
raw_path: "raw/press-releases/2024-12-24_fbi-gov_fbi-dc3-npa-tradertraitor-dmm-bitcoin-308m-attribution.md"
source_type: press-release
publisher: "Federal Bureau of Investigation (FBI) — National Press Office"
author: ""
publish_date: "2024-12-24"
ingest_date: "2026-05-17"
language: en
reliability: high
credibility: confirmed
sensitivity: public
pages_updated:
  - "[[tradertraitor-dmm-bitcoin-cryptocurrency-theft-joint-attribution-2024]]"
key_findings:
  - "FBI National Press Office published the US-side own-domain anchor of the joint FBI + DC3 + NPA Japan public attribution of the May 2024 DMM Bitcoin USD 308M cryptocurrency theft to North Korea-backed TraderTraitor (Lazarus Group sub-cluster)."
  - "Joint publication structure: simultaneous release on fbi.gov (US side) and npa.go.jp (Japan side) + companion English-language PDF on cyber.go.jp/eng — a true joint-name attribution rather than parallel national statements."
  - "FBI explicitly names cooperation with NPA Japan and commits to continuing the joint posture: 'The FBI, National Police Agency of Japan, and other U.S. government and international partners will continue to expose and combat North Korea's use of illicit activities — including cybercrime and cryptocurrency theft — to generate revenue for the regime.'"
  - "Attack chain (FBI account): late March 2024 LinkedIn social-engineering recruiter lure → malicious Python pre-employment test (GitHub) → Ginco enterprise wallet software employee compromise → session-cookie hijack → manipulated DMM transaction → 4,502.9 BTC lost."
  - "FBI release adds threat-actor attribution context: TraderTraitor cluster also tracked as Jade Sleet / UNC4899 / Slow Pisces; FBI's April 2022 joint advisory with CISA and Treasury links DPRK-backed entities behind TraderTraitor to Lazarus Group, APT38, BlueNoroff, and Stardust Chollima."
created: 2026-05-17
---

# FBI + DC3 + NPA joint attribution — TraderTraitor / DMM Bitcoin $308M cryptocurrency theft (US-side own-domain, 2024-12-24)

## Summary

On **2024-12-24**, the **Federal Bureau of Investigation (FBI)** — together with the **U.S. Department of Defense Cyber Crime Center (DC3)** and the **National Police Agency of Japan (警察庁 / NPA)** — published, in joint name, a public attribution of the May 2024 theft of **4,502.9 BTC ≈ USD 308 million** from **DMM Bitcoin** (Japan-licensed cryptocurrency exchange) to the **North Korea-backed cyber attack group "TraderTraitor"** (also tracked as Jade Sleet, UNC4899, Slow Pisces; assessed sub-cluster of the Lazarus Group family).

This source page captures the **US-side own-domain anchor** of the joint advisory, hosted on `www.fbi.gov`. The **Japan-side own-domain anchor** (NPA Japan on `npa.go.jp`, with a companion English PDF on `cyber.go.jp/eng`) is filed separately at [[2024-12-24_npa-japan_tradertraitor-dmm-bitcoin-fbi-dc3-joint-attribution]].

The two own-domain anchors together constitute the second tier-1 own-domain corroboration required under L24/L25 strict for the `[[tradertraitor-dmm-bitcoin-cryptocurrency-theft-joint-attribution-2024]]` operation page.

## Reliability and credibility

| Field | Value | Notes |
|---|---|---|
| Source type | Tier-1 government press release / joint advisory (US-side anchor) | FBI National Press Office is the US federal investigative bureau's official press organ |
| Publisher tier | Federal investigative bureau (highest tier-1 under wiki framework) | Co-publishers DC3 (US DoD cyber-forensics centre) and NPA Japan (Japanese national police) listed in joint name |
| Reliability | high | Formal joint multi-agency attribution; technical narrative jointly endorsed |
| Credibility | confirmed | Cross-confirmed by NPA Japan own-domain release, cyber.go.jp/eng companion PDF, FBI release wording reproduced verbatim by multiple major outlets |
| Sensitivity | public | Open public advisory |
| Language | English (this anchor); Japanese (NPA-side anchor) | |

## Fetch posture

The FBI URL is on the wiki's BOT_PROTECTED_DOMAINS whitelist (LESSONS L11, L13). Direct WebFetch returns HTTP 403 because FBI and adjacent .gov subdomains use Cloudflare / Akamai bot challenges that block non-browser clients. **This does not mean the URL is dead**: the same press release text is reproduced verbatim by multiple secondary outlets on the publication date (2024-12-24) — The Record (Recorded Future), SecurityWeek, SecurityAffairs, Beyond Identity, Dark Web Informer — and the joint-publication structure is independently confirmed by the NPA-side own-domain release. The FBI URL is retained as the canonical US-side anchor for the joint advisory.

## Why this matters for IC

1. **US-side anchor for a joint US-Japan attribution.** The FBI release publishes in joint name with NPA Japan and DC3, rather than as a unilateral FBI release citing Japanese cooperation — a stronger operational-cooperation signal than parallel national statements.
2. **Tier-1 own-domain corroboration for L24/L25 strict.** Together with the NPA Japan own-domain anchor, this FBI release provides the second tier-1 own-domain primary source required by wiki rules. No private wire substitution.
3. **Doctrinal continuity.** FBI's public commitment to "continue to expose and combat North Korea's use of illicit activities … in cooperation with NPA Japan and other partners" frames the joint attribution as a maintained-cadence IC instrument, not a one-off public diplomacy product.
4. **Threat-actor identity confirmation.** FBI's own anchor confirms the TraderTraitor → Jade Sleet / UNC4899 / Slow Pisces → Lazarus Group / APT38 / BlueNoroff / Stardust Chollima identity chain — useful for downstream attribution-trace work on subsequent DPRK crypto-theft incidents.

## Connections

- [[tradertraitor-dmm-bitcoin-cryptocurrency-theft-joint-attribution-2024]] — operation page (this source's primary product)
- [[2024-12-24_npa-japan_tradertraitor-dmm-bitcoin-fbi-dc3-joint-attribution]] — companion Japan-side anchor (NPA Japan own-domain)
- [[fbi]] — US co-publisher (this source's publisher)
- [[japan-npa]] — Japan co-publisher
- [[united-states]], [[japan]] — cooperating jurisdictions
- [[north-korea]] — adversary state (not a cooperating partner)
- [[hacking-ic]], [[money-laundering-ic]] — crime-type axes
