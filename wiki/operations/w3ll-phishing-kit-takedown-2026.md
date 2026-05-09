---
type: operation
title: "W3LL Phishing Kit / W3LLSTORE Takedown — first US-Indonesia coordinated action against a phishing kit developer (FBI Atlanta + Indonesian National Police, April 2026)"
title_ko: "W3LL 피싱 킷 / W3LLSTORE 마켓플레이스 단속 — 미국·인도네시아 최초의 피싱 킷 개발자 공조 작전 (FBI 애틀랜타 + 인도네시아 국가경찰, 2026-04)"
aliases:
  - "W3LL phishing kit takedown"
  - "W3LLSTORE takedown"
  - "FBI Atlanta Indonesian National Police W3LL operation"
  - "G.L. phishing developer takedown"
case_id: CYB-2026-088
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - infrastructure-seizure
outcome: success
timeframe:
  announced: 2026-04-10
  start: ""
  end: 2026-04-10
  ongoing: false
crime_type: "[[online-fraud-ic]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "W3LL phishing kit and the supporting W3LLSTORE marketplace — a phishing-as-a-service (PhaaS) ecosystem operated by an Indonesia-based developer ('G.L.', detained per the FBI Atlanta release). The W3LL phishing kit (priced at approximately USD 500 per access) impersonated legitimate login pages and uniquely captured *session data alongside credentials*, enabling multi-factor-authentication bypass and persistent account access. Supporting W3LLSTORE marketplace facilitated the sale of 25,000+ compromised accounts (2019–2023) including remote desktop connection access. After W3LLSTORE shut down in 2023, the kit continued to be marketed via encrypted messaging platforms (rebranded), and from 2023 to 2024 alone targeted 17,000+ victims worldwide with USD 20,000,000+ in attempted fraud."
lead_agency: "[[fbi]]"
coordinating_body: "[[fbi]]"
participating_countries:
  - "[[united-states]]"
  - "[[indonesia]]"
participating_agencies:
  - "[[fbi]]"
  - "[[indonesia-police]]"
organizations:
  - "[[fbi]]"
  - "[[indonesia-police]]"
mechanisms_used:
  - "[[informal-cooperation]]"
legal_basis:
  - "Bilateral US-Indonesia law enforcement cooperation as facilitated by FBI Atlanta Field Office and the Indonesian National Police; specific legal instrument (MLAR vs. police-to-police) not specified in the cited release."
  - "U.S. Attorney's Office for the Northern District of Georgia: prosecutorial vehicle for US-side infrastructure seizures."
  - "Indonesian national criminal procedure: basis for the detention of alleged developer G.L. on Indonesian soil."
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Detention of alleged developer 'G.L.' in Indonesia by the Indonesian National Police"
    - "Seizure of key domains tied to the W3LL operation"
    - "Identification and seizure of US-side infrastructure facilitating the phishing service (FBI Atlanta + USAO-NDGA)"
    - "USD 20,000,000+ in attempted fraud documented"
    - "17,000+ victims worldwide (2023–2024 phase alone)"
    - "25,000+ compromised accounts previously sold via W3LLSTORE marketplace (2019–2023)"
    - "Phishing kit pricing: approximately USD 500 per access"
    - "Pattern: Post-2023 W3LLSTORE shutdown migration to encrypted messaging platforms"
edges:
  - source_actor: fbi
    target_actor: indonesia-police
    cooperation_type: joint_investigation
    legal_basis: bilateral
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "Specific developer name and full identification of 'G.L.' (only initials given in the FBI Atlanta release)"
  - "Specific arrest/charge count vs. detention status — the cited release uses 'detained' not 'arrested'; charging in Indonesia (or extradition request to US) is not detailed"
  - "Specific domain count seized; the release describes 'key domains' without enumeration"
  - "Specific encrypted-messaging-platform identification (post-2023 W3LL distribution channel — Telegram? — not named)"
  - "Specific cryptocurrency-seizure totals (the release reports USD 20M attempted fraud but no recovered-funds figure)"
  - "Whether MLAR or informal police-to-police cooperation channel was the operative legal instrument between US and Indonesia"
  - "Whether the 'rebranded' post-2023 phishing kit retains the W3LL name or operates under a different brand"
related_cases:
  []
related_operations:
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[bidencash-takedown]]"
  - "[[leakbase-takedown-2026]]"
  - "[[tycoon-2fa-phishing-as-a-service-takedown-2026]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "**First US-Indonesia coordinated action against a phishing kit developer** — explicitly framed by FBI Atlanta as a precedent. Adds the US-Indonesia bilateral track to the wiki's PhaaS-ecosystem disruption corpus alongside [[labhost-phishing-as-a-service-takedown-2024|LabHost]] (Europol-led, EU + Asia-Pacific) and [[leakbase-takedown-2026|LeakBase]] (Europol-led, 14-country)."
  - "**MFA-bypassing session-data capture** is the technical innovation that elevated W3LL beyond a generic phishing kit and made it a 'full-service cybercrime platform' (per FBI Atlanta SAC). Establishes session-data capture as a documented attribute of *senior-tier* PhaaS kits."
  - "**Post-marketplace migration to encrypted messaging platforms** — after W3LLSTORE shut down in 2023, the kit was rebranded and marketed via encrypted messaging. Demonstrates that PhaaS ecosystems persist beyond marketplace-level enforcement, requiring follow-on developer-targeting actions like this one."
  - "**Field-office-led international cooperation pattern** — FBI Atlanta Field Office (rather than FBI HQ Cyber Division) led this US-Indonesia bilateral track, paired with USAO-NDGA. Demonstrates that field-office-level US international cybercrime cooperation works at the bilateral scale on a single-developer target."
  - "**Asymmetric documented vs. inferred metrics** — 25,000 accounts sold 2019-2023 + 17,000 victims targeted 2023-2024 + USD 20M+ attempted fraud is a layered metric set. The cited release does not consolidate these into a single 'total victims' figure, leaving cumulative impact partially un-summed."
source_count: 1
sources:
  - "[[2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll]]"
created: 2026-05-09
updated: 2026-05-09
---
## Summary

On **10 April 2026**, the **FBI Atlanta Field Office** and the **Indonesian National Police (Polri)** jointly announced the takedown of the **W3LL phishing kit** and its supporting marketplace **W3LLSTORE** — described by FBI Atlanta as the *first coordinated action against a phishing kit developer between the United States and Indonesia*. Indonesian authorities **detained the alleged developer 'G.L.'**; FBI Atlanta and the U.S. Attorney's Office for the Northern District of Georgia identified and seized US-side infrastructure facilitating the phishing service; key domains tied to the operation were seized.

> [!note] First US-Indonesia coordinated action against a phishing kit developer
> The FBI Atlanta press release explicitly characterises this case as a precedent for US-Indonesia bilateral cybercrime cooperation. Adds Indonesia to the wiki's PhaaS-disruption cooperation map alongside the EU-led [[labhost-phishing-as-a-service-takedown-2024|LabHost]] takedown and the [[leakbase-takedown-2026|LeakBase]] 14-country action.

## Background

The **W3LL phishing kit** was a phishing-as-a-service tool priced at approximately **USD 500 per access**. It enabled criminals to impersonate legitimate login pages and — uniquely — *captured session data alongside credentials*, enabling **multi-factor-authentication bypass** and persistent account access. The kit was supported by an online marketplace called **W3LLSTORE**, where criminals could buy and sell stolen credentials and unauthorized system access (including remote desktop connections).

Activity timeline:

| Period | Activity |
|---|---|
| 2019–2023 | W3LLSTORE marketplace operated; facilitated the sale of **25,000+ compromised accounts** |
| 2023 | W3LLSTORE shut down |
| 2023–2024 | W3LL phishing kit rebranded and marketed via **encrypted messaging platforms**; **17,000+ victims worldwide targeted** |
| 10 April 2026 | Joint FBI Atlanta + Indonesian National Police action: G.L. detained; infrastructure seized; key domains seized |

Documented attempted fraud across the operation: **over USD 20 million**.

The cited release notes that the developer behind the tool *also collected and resold access to compromised accounts*, amplifying the reach of the scheme beyond direct kit sales.

## Participating Parties

| Party | Country | Role |
|---|---|---|
| [[fbi\|FBI Atlanta Field Office]] | United States | Lead US investigator; identified and seized US-side phishing infrastructure |
| U.S. Attorney's Office for the Northern District of Georgia (USAO-NDGA) | United States | Prosecutorial assistance; backed US-side seizure actions |
| [[indonesia-police\|Indonesian National Police (Polri)]] | Indonesia | Detained alleged developer 'G.L.' on Indonesian soil; seized key domains |

> [!note] First coordinated US-Indonesia phishing-developer action
> FBI Atlanta credits the Indonesian National Police for *the first coordinated action against a phishing kit developer between the United States and Indonesia*. The legal instrument (MLAR vs. police-to-police informal cooperation) is not specified in the cited release.

## Legal Framework

- **Bilateral US-Indonesia law enforcement cooperation** — FBI Atlanta + Indonesian National Police; specific legal instrument not detailed in the cited release.
- **U.S. Attorney's Office for the Northern District of Georgia** — prosecutorial vehicle for the US-side infrastructure seizures and (presumed) sealed indictment supporting domain seizures.
- **Indonesian national criminal procedure** — basis for the detention of G.L. on Indonesian soil.

> [!warning] Legal status check needed
> The cited release does not specify whether G.L. has been *charged* in Indonesia, whether US authorities have lodged an extradition request, or whether the post-detention process is sealed-indictment-driven. Subsequent reporting may clarify.

## Operational Timeline

| Date | Event |
|---|---|
| 2019 | W3LLSTORE marketplace established |
| 2019–2023 | W3LLSTORE marketplace operates; 25,000+ compromised accounts sold |
| 2023 | W3LLSTORE marketplace shut down (cause not stated in release) |
| 2023–2024 | W3LL phishing kit rebranded; marketed via encrypted messaging platforms; 17,000+ victims targeted; USD 20M+ attempted fraud cumulative |
| (date undated) | FBI Atlanta + USAO-NDGA infrastructure-seizure investigation; coordination with Indonesian National Police initiated |
| (date undated) | Indonesian National Police detains G.L.; key domains seized |
| 10 April 2026 | FBI Atlanta press release announcing the takedown |

## Results and Impact

| Metric | Value | Notes |
|---|---|---|
| Developer detained | 1 | 'G.L.', detained by Indonesian National Police |
| Domains seized | "key domains" | Specific count not enumerated in release |
| US-side infrastructure | seized | FBI Atlanta + USAO-NDGA |
| Documented attempted fraud | USD 20,000,000+ | Across W3LL operation |
| Victims targeted (2023–2024 alone) | 17,000+ | Worldwide |
| Compromised accounts sold (2019–2023) | 25,000+ | Via W3LLSTORE marketplace |
| W3LL kit pricing | ~USD 500 per access | Per FBI Atlanta release |

## Cooperation Mechanisms Used

- **Bilateral FBI Atlanta + Indonesian National Police investigation** — US field-office-led cooperation track (rather than HQ-to-HQ Cyber Division)
- **US-side infrastructure seizure (FBI Atlanta + USAO-NDGA)** complementing Indonesian-side detention and domain-seizure
- **Specific legal instrument not detailed** — MLAR vs. police-to-police informal cooperation unspecified

## Challenges and Friction Points

- **Indonesia-developer + US-victims pattern**: the developer (Indonesia) and the bulk of victims (worldwide; FBI Atlanta-led case implies US-targeted victims) are in different jurisdictions. The US-Indonesia bilateral cooperation channel is *likely* nascent for cybercrime — explicitly framed by FBI Atlanta as a 'first-of-its-kind' action.
- **Post-marketplace migration to encrypted messaging**: after W3LLSTORE shut down in 2023, the kit migrated to encrypted messaging platforms, demonstrating that PhaaS ecosystems require persistent follow-on enforcement after marketplace-level disruption.
- **MFA-bypass via session-data capture**: a technical capability of the kit that distinguishes W3LL from generic credential-stealing phishing; means that *prior credential rotations* by victims are insufficient to evict attackers from compromised accounts post-W3LL infection.
- **Asymmetric metric set**: 25,000 accounts (2019-2023) + 17,000 victims (2023-2024) + USD 20M+ attempted fraud is not consolidated into a single cumulative figure in the release.

## Lessons Learned

1. **First US-Indonesia coordinated action against a phishing kit developer** — adds the US-Indonesia bilateral track to the wiki's PhaaS disruption coverage. The cooperation pattern (FBI field office + USAO + Indonesian National Police) is *likely* a template for follow-on US-Indonesia cybercrime actions.
2. **MFA-bypassing session-data capture is a senior-tier PhaaS attribute**. Establishes a technical-sophistication marker that may be useful for distinguishing top-tier PhaaS kits in the wiki's future ingest decisions.
3. **PhaaS ecosystem persistence beyond marketplace shutdown**. After W3LLSTORE shut down in 2023, the kit continued to be marketed via encrypted messaging platforms (rebranded). Marketplace-level enforcement is *unlikely* to fully disrupt mature PhaaS ecosystems without a follow-on developer-targeting action like this one.
4. **Field-office-led US international cooperation track**. FBI Atlanta Field Office (rather than FBI HQ Cyber Division) drove this US-Indonesia bilateral case, paired with USAO-NDGA. This is structurally distinct from FBI HQ-driven multi-country takedowns (e.g., [[hive-ransomware-takedown|Hive]]) and shows that field-office-scale US international cybercrime cooperation works at the bilateral scale.

## Follow-Up Actions

The cited release does not enumerate post-detention follow-up steps — Indonesian charging, US extradition request, asset recovery, or victim notification. Subsequent reporting may clarify.

## Korean Involvement (한국의 참여)

[[south-korea|South Korea]] has no documented involvement in this operation. Korean victims among the 17,000+ targeted users worldwide are *unknown* from the cited release; *likely* a non-trivial fraction given the global scope of W3LL's targeting. The KNPA Cyber Bureau ↔ FBI Atlanta channel is not enumerated in this case.

## Contradictions & Open Questions

- **Developer identity**: only initials 'G.L.' are given. Specific name, full identification, and Indonesian-side charging status are not detailed.
- **Post-2023 rebranded kit name**: not stated. The kit was 'rebranded' but the new brand identity is not disclosed.
- **Encrypted-messaging-platform identification**: 'encrypted messaging platforms' is unspecified; Telegram is *likely* but not confirmed.
- **Specific seized-domain count**: 'key domains' is not enumerated.
- **MLA framework vs. police-to-police channel**: the cited release does not specify the legal cooperation instrument used between FBI and the Indonesian National Police.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll\|FBI Atlanta, Indonesian Authorities Take Down Global Phishing Network Behind Millions in Fraud Attempts]] | FBI Atlanta Field Office | 2026-04-10 | https://www.fbi.gov/contact-us/field-offices/atlanta/news/fbi-atlanta-indonesian-authorities-take-down-global-phishing-network-behind-millions-in-fraud-attempts |
