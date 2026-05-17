---
type: operation
title: "TraderTraitor / DMM Bitcoin $308M Cryptocurrency Theft — NPA-FBI-DC3 Joint Attribution (2024)"
title_ko: "트레이더트레이터 / DMM 비트코인 3.08억 달러 암호화폐 탈취 — 일본 경찰청·FBI·DC3 공동 귀속 발표 (2024)"
aliases:
  - "TraderTraitor DMM Bitcoin joint attribution 2024"
  - "DMM Bitcoin 308M USD theft joint advisory"
  - "DPRK TraderTraitor DMM cryptocurrency theft attribution"
  - "Jade Sleet / UNC4899 / Slow Pisces DMM Bitcoin attribution"
case_id: CYB-2024-997
period: 3
operation_type: joint-investigation
status: completed
enforcement_type:
  - indictment
outcome: partial
timeframe:
  announced: 2024-12-24
  start: 2024-03
  end: 2024-12-24
  ongoing: false
crime_types:
  - "[[hacking-ic]]"
  - "[[money-laundering-ic]]"
crime_type: "[[hacking-ic]]"
target_entity: "North Korea-backed cyber attack group TraderTraitor (a.k.a. Jade Sleet / UNC4899 / Slow Pisces; assessed Lazarus Group sub-cluster) — responsible for May 2024 theft of 4,502.9 BTC ≈ USD 308M from DMM Bitcoin via supply-chain compromise of wallet-software vendor Ginco"
lead_agency: "[[japan-npa]]"
coordinating_body: ""
participating_countries:
  - "[[japan]]"
  - "[[united-states]]"
participating_agencies:
  - "[[japan-npa]]"
  - "[[fbi]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Joint public attribution of USD 308M / 4,502.9 BTC theft to DPRK-affiliated TraderTraitor / Lazarus sub-cluster"
    - "Joint technical advisory (Japanese-language + English-language) published simultaneously on NPA, cyber.go.jp, FBI own-domains"
    - "Public naming of supply-chain compromise pathway via Ginco enterprise wallet software (LinkedIn social-engineering → malicious Python pre-employment test → session-cookie hijack)"
edges:
  - source_actor: "[[japan-npa]]"
    target_actor: "[[fbi]]"
    cooperation_type: "joint_investigation"
    legal_basis: "bilateral_MOU"
    direction: "undirected"
  - source_actor: "[[japan-npa]]"
    target_actor: "[[fbi]]"
    cooperation_type: "info_sharing"
    legal_basis: "bilateral_MOU"
    direction: "undirected"
credibility_index: 4.5
source_tier: 1
missing_fields:
  - arrests
  - indictments
  - cryptocurrency_seized
related_cases: []
related_operations:
  - "[[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]]"
  - "[[treasury-sanctions-dprk-it-worker-network-andreyev-chinyong-2025]]"
  - "[[us-rok-japan-joint-statement-dprk-it-workers-2025-08]]"
challenges_encountered: []
lessons_learned:
  - "Joint multi-government public attribution of a state-affiliated cyber actor is itself an IC instrument — typically deployed 6-12 months after incident to combine evidence sharing, joint forensic analysis, and political concurrence."
  - "Supply-chain compromise pathways (wallet-software vendor employee → exchange) are the dominant vector for large-scale DPRK crypto-theft; attribution must trace the full chain back to the recruiting-platform lure."
  - "NPA Japan + US FBI + US DoD Cyber Crime Center (DC3) tri-party attribution shows operational US-Japan cyber cooperation extends beyond diplomacy-level to joint technical attribution."
source_count: 2
sources:
  - "[[2024-12-24_npa-japan_tradertraitor-dmm-bitcoin-fbi-dc3-joint-attribution]]"
  - "[[2024-12-24_fbi-gov_fbi-dc3-npa-tradertraitor-dmm-bitcoin-308m-attribution]]"
created: 2026-05-17
updated: 2026-05-17
---

## Summary

On **2024-12-24**, the **National Police Agency of Japan (警察庁 / NPA)**, the **U.S. Federal Bureau of Investigation (FBI)**, and the **U.S. Department of Defense Cyber Crime Center (DC3)** published a joint advisory attributing the **May 2024 theft of 4,502.9 BTC (≈ USD 308 million / JPY ≈ 48.2 billion)** from **DMM Bitcoin** — a Japan-licensed cryptocurrency exchange — to the North Korea-backed cyber attack group **TraderTraitor** (a.k.a. **Jade Sleet, UNC4899, Slow Pisces**; assessed sub-cluster of the **Lazarus Group**).

The attribution was published simultaneously by NPA on its own domain (Japanese narrative + Japanese-language PDF + English-language PDF on `cyber.go.jp/eng`) and by the FBI on `fbi.gov`. It is one of the largest single-incident cryptocurrency thefts ever publicly tied in joint multi-state name to a specific DPRK-affiliated threat-actor cluster.

This page documents the **joint attribution as an IC product**, not the underlying May 2024 incident as a stand-alone hacking event.

## Background

DMM Bitcoin was one of Japan's licensed cryptocurrency exchanges. In late May 2024, DMM Bitcoin disclosed an unauthorised outflow of approximately 4,502.9 BTC and acknowledged the loss as approximately JPY 48.2 billion at the prevailing rate. The exchange initially declined to publicly attribute the theft. In December 2024, DMM Bitcoin announced it would shut down its exchange business and transfer customer assets to SBI VC Trade — a direct consequence of the loss.

For seven months between the May 2024 loss and the December 2024 joint attribution, no government publicly named the perpetrator. The joint NPA–FBI–DC3 advisory of 2024-12-24 closed that public attribution gap.

## Participating Parties

| Party | Role |
|---|---|
| [[japan-npa]] (警察庁 — Cyber Affairs Bureau) | Lead Japanese investigator; primary publisher (`npa.go.jp`) |
| 関東管区警察局 (Kanto Regional Police Bureau, Japan) | Co-investigator on Japan side |
| 警視庁 (Tokyo Metropolitan Police Department, Japan) | Co-investigator on Japan side |
| [[fbi]] (United States Federal Bureau of Investigation) | US co-publisher; lead US investigator; published companion release on `fbi.gov` |
| U.S. Department of Defense Cyber Crime Center (DC3) | Joint technical attribution and analysis partner |
| NISC (内閣サイバーセキュリティセンター) | Japan inter-agency coordination |
| 金融庁 (Financial Services Agency / FSA, Japan) | Sector-regulator coordination (cryptocurrency exchange licensee oversight) |

DMM Bitcoin and the supply-chain-compromise victim **Ginco Inc.** (a Japan-based enterprise cryptocurrency wallet software company) are private-sector entities affected, not LE participants.

The DPRK / TraderTraitor / Lazarus cluster is the **adversary**, not a cooperating jurisdiction; see [[north-korea]].

## Legal Framework

The joint attribution operates under:

- **Bilateral US-Japan cyber cooperation channels** — operational law-enforcement information sharing between FBI and NPA Cyber Affairs Bureau, increasingly invoked since the 2023-2025 surge in DPRK crypto-theft attributions.
- **Budapest Convention 24/7 contact network** — both Japan and the United States are States Parties; the 24/7 network is the formal preservation/expedited-disclosure mechanism for cybercrime evidence requests across borders.
- **Informal LE-to-LE liaison** via the FBI Legal Attaché (Tokyo) and the NPA International Cooperation Division — the working-level channel for operational cyber-investigation coordination.
- **Public-attribution as IC instrument** — there is no separate treaty governing joint attribution; it functions as a political-operational act underpinned by the above operational channels.

## Operational Timeline

| Date | Event |
|---|---|
| Late March 2024 | A North Korean cyber actor masquerading as a recruiter on LinkedIn contacted an employee at **Ginco** (Japan-based enterprise cryptocurrency wallet software vendor). Sent target a URL linked to a malicious Python script under guise of a pre-employment test, hosted on GitHub. |
| April – mid-May 2024 | TraderTraitor compromise of Ginco employee maintained; session-cookie information exfiltrated. |
| After mid-May 2024 | TraderTraitor actors used session-cookie information to impersonate the compromised Ginco employee and gained access to Ginco's unencrypted communications system. |
| Late May 2024 | Actors manipulated a legitimate transaction request originated by a DMM Bitcoin employee, resulting in loss of **4,502.9 BTC ≈ USD 308M / JPY ≈ 48.2bn**. |
| 31 May 2024 (approx.) | DMM Bitcoin publicly discloses unauthorised outflow; no perpetrator named. |
| Dec 2024 | DMM Bitcoin announces shutdown and transfer of customer assets to SBI VC Trade. |
| **2024-12-24** | **NPA Japan + FBI + DC3 publish simultaneous joint advisory** attributing the loss to TraderTraitor (a.k.a. Jade Sleet / UNC4899 / Slow Pisces; Lazarus Group sub-cluster). |

## Results and Impact

- **No arrests, no indictments, no seizures** were announced as part of this joint advisory. The operation is a **joint public attribution**, not a takedown.
- **Publicly documented attack chain** — first joint multi-state narrative of the supply-chain compromise pathway from LinkedIn lure → Ginco employee compromise → DMM transaction manipulation → 4,502.9 BTC loss.
- **DMM Bitcoin shutdown**: market-confidence consequence of the loss; joint attribution acted as a public signal supporting orderly wind-down and customer-asset transfer to SBI VC Trade.
- **Cluster-naming consolidation**: the joint advisory canonicalised the link between TraderTraitor, Jade Sleet, UNC4899, and Slow Pisces — previously tracked under separate names by different threat-intel vendors — and confirmed the assessed Lazarus-Group affiliation.

## Cooperation Mechanisms Used

- **Bilateral US-Japan cyber-cooperation operational channel** (FBI Legal Attaché Tokyo ↔ NPA International Cooperation Division / Cyber Affairs Bureau).
- **Joint technical forensic analysis** between NPA's Cyber Affairs Bureau and the U.S. DoD Cyber Crime Center (DC3).
- **Co-publication on respective own-domains** as the operational form of joint public attribution — a deliberate diplomatic-LE choice over single-state attribution.

## Challenges and Friction Points

| Challenge | Notes |
|---|---|
| 7-month attribution lag | Likely *highly likely* attributable to the time required for cross-border evidence sharing, joint forensic analysis, and political concurrence to publish — not to technical attribution alone. |
| No arrests / extradition | TraderTraitor operators are assessed to operate inside DPRK territory; no extradition pathway exists, so joint attribution is the principal available IC instrument. |
| Recovery of stolen BTC | Cryptocurrency tracing requires onward cooperation with mixer-takedown operations and exchange-level KYC freezes; no announced recovery as of the 2024-12-24 advisory. |
| Sector consequence | DMM Bitcoin's shutdown raises broader concern about supply-chain attack pathways through wallet-software vendors; sector-regulator FSA cooperation is partly an outcome rather than precondition. |

## Lessons Learned

1. **Joint public attribution is itself an IC product.** It requires bilateral evidence sharing, joint forensic analysis, and political concurrence — measured in months, not days. The 7-month NPA-FBI-DC3 lag is representative.
2. **Supply-chain compromise is the dominant vector** for high-value DPRK cryptocurrency theft — attribution must trace the full chain from the social-engineering lure on the recruiting platform back through the vendor compromise to the final loss.
3. **Tri-party (NPA + FBI + DC3)** is a higher operational signal than bilateral (NPA + FBI) attribution — DC3's joint forensic involvement signals that US Department of Defense cyber-forensic capabilities are part of the bilateral US-Japan cyber-attribution stack.

## Follow-Up Actions

- DMM Bitcoin wound down its exchange business in 2025; SBI VC Trade absorbed customer accounts and assets.
- Subsequent DPRK-attribution releases ([[treasury-sanctions-dprk-it-worker-network-andreyev-chinyong-2025]], [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]], [[us-rok-japan-joint-statement-dprk-it-workers-2025-08]]) deepened the multi-government public-attribution pattern against DPRK cyber-revenue generation.

## Korean Involvement (한국의 참여)

이 작전 자체는 일본 경찰청과 미국 FBI·DC3의 양국·삼자 공동 귀속 발표로, **한국 수사기관의 직접 참여는 없다.** 다만 한국은 별도 트랙으로 동일한 DPRK 사이버 위협 행위자 군 (Lazarus / TraderTraitor 클러스터)을 추적하고 있으며, 2025년 8월의 [[us-rok-japan-joint-statement-dprk-it-workers-2025-08|미-한-일 3자 공동성명]]은 본 TraderTraitor / DMM 사건의 일본 단독 귀속 트랙을 3자 협력 구조로 확장하는 후속 조치 성격을 갖는다.

## Contradictions & Open Questions

- **Pre-attribution period.** Why did DMM Bitcoin's May 2024 disclosure precede the public attribution by seven months? *Highly likely* a deliberate IC sequencing decision rather than a technical attribution delay — the joint forensic narrative published 2024-12-24 implies the technical attribution was substantially settled earlier.
- **Recovery prospects.** Has any portion of the 4,502.9 BTC been recovered, seized at exchange off-ramps, or frozen under OFAC / Treasury cyber-sanctions designations? Not addressed in the joint advisory; subsequent OFAC actions on DPRK crypto-laundering nodes do not specifically tie back to the DMM tranche.
- **DC3 role.** What specific forensic contribution did the U.S. DoD Cyber Crime Center make distinct from the FBI's contribution? The joint advisory names DC3 as co-author but does not delineate the workshare.

> [!note] Translation note
> NPA Japan = 警察庁; "Cyber Affairs Bureau" = サイバー警察局; DC3 = US Department of Defense Cyber Crime Center (米国国防総省サイバー犯罪センター). "TraderTraitor" is a US-naming-side cluster name; the NPA Japanese-language release uses both カタカナ transliteration and the English form. "Lazarus Group" is industry-standard tracking-name for the broader DPRK cyber-attack family of clusters.
