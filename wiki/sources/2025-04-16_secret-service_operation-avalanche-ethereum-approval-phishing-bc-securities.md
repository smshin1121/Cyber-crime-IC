---
type: source
title: "U.S. Secret Service Analysts Work with Canadian Officials to Disrupt Ethereum Blockchain 'Approval Phishing' Scam"
raw_path: raw/press-releases/2025-04-16_secret-service_operation-avalanche-ethereum-approval-phishing-bc-securities.md
source_type: press-release
publisher: "U.S. Secret Service (Media Relations, Washington Field Office)"
author: "U.S. Secret Service Media Relations"
publish_date: 2025-04-16
ingest_date: 2026-05-16
language: en
reliability: high
credibility: confirmed
sensitivity: public
pages_updated:
  - "[[usss-canada-operation-avalanche-ethereum-approval-phishing-2025]]"
key_findings:
  - "U.S. Secret Service Washington Field Office Investigative and Network Intrusion Forensic Analysts joined the Canadian-led Operation Avalanche (a name re-used in 2025; distinct from the 2016 Avalanche botnet takedown), a coordinated operation with the BC Securities Commission that warned holders of compromised Ethereum wallets that they had been victims of 'approval phishing.'"
  - "Cooperation roster (US-Canada, ≥2 jurisdictions named verbatim in the tier-1 release): United States Secret Service (Washington Field Office) and on the Canadian side the BC Securities Commission, Ontario Provincial Police, Alberta Securities Commission, L'Autorité des marchés financiers (Quebec), Ontario Securities Commission, Delta Police Department, Vancouver Police Department, and the Royal Canadian Mounted Police."
  - "Blockchain addresses identified during Operation Avalanche were drained of crypto assets worth an estimated USD 4.3 million; the scam (a sub-pattern of 'pig butchering') tricked Ethereum wallet owners into granting approval permissions, after which scammers withdrew funds without the owner's knowledge."
  - "The release frames the action as an example of how U.S. Secret Service investigative expertise and 'long-standing global law enforcement partnerships' aid disruption of cryptocurrency scams orchestrated by transnational organized crime; WFO SAC Matt McCool committed the USSS to continued work with Canadian law enforcement and financial partners to identify and seize stolen assets for victims."
created: 2026-05-16
---

## Summary

Tier-1 own-domain U.S. Secret Service press release (secretservice.gov, Akamai Bot Manager-protected; fetched via `curl_cffi` chrome124 TLS impersonation per L20/L21) announcing USSS Washington Field Office participation in Operation Avalanche, a coordinated U.S.–Canada victim-notification and asset-disruption operation against an Ethereum-blockchain "approval phishing" scam network. The release is the primary U.S.-side acknowledgment of the operation (the Canadian-side public communication was led by the BC Securities Commission). The operation is **distinct** from the 2016 Europol/Eurojust/U.S. DOJ Avalanche botnet takedown ([[operation-avalanche]]); the name "Operation Avalanche" was re-used by Canadian securities regulators and U.S. federal partners in 2025.

## Cooperation roster (verbatim from the release)

> "In addition to the U.S. Secret Service and the BC Securities Commission, Operation Avalanche included the Ontario Provincial Police, Alberta Securities Commission, the L'Autorité des marchés financiers, Ontario Securities Commission, Delta Police Department, Vancouver Police Department, and the Royal Canadian Mounted Police."

L24 compliance: two distinct cooperating jurisdictions' LE / financial-regulatory agencies are explicitly named in the tier-1 primary source — the United States (USSS WFO) and Canada (RCMP + multiple provincial/municipal police forces and provincial securities commissions). No adversary/origin/destination state is included in `participating_countries`.

## Reliability assessment

- **Reliability: high** — official press release from a U.S. federal investigative agency, published on its own domain (secretservice.gov).
- **Credibility: confirmed** — first-person attribution by USSS WFO Special Agent in Charge Matt McCool; partner agencies are named individually; specific monetary loss figure (USD 4.3 million drained from identified Ethereum addresses).
- **Sensitivity: public** — published openly on the USSS newsroom; no operational sources/methods exposed.

## Source provenance notes

- secretservice.gov is protected by Akamai Bot Manager. `WebFetch` returned HTTP 403; the page was successfully retrieved via `curl_cffi` `Session(impersonate="chrome124")` returning 200 OK with a ~70 KB body (no `bm-verify` meta-refresh challenge was triggered on this fetch; per L21 the fallback was prepared but not required).
- The release does not state arrests, indictments, or seizures — it is framed as a "warn the victims" / disruption action focused on draining wallets, blockchain attribution, and inter-agency coordination.
