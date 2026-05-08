---
type: operation
title: "xss.is Russian-speaking Cybercrime Forum Takedown (Kyiv arrest, French-led + Ukrainian SBU + Europol EC3, 2025-07-22)"
title_ko: "xss.is 러시아어 사이버범죄 포럼 단속 (키예프 검거, 프랑스 주도 + 우크라이나 SBU + Europol EC3, 2025-07-22)"
aliases:
  - "xss.is takedown 2025"
  - "DaMaGeLaB cybercrime forum administrator arrest"
  - "Russian-speaking cybercrime forum Kyiv arrest"
case_id: CYB-2025-215
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - domain-seizure
outcome: success
timeframe:
  announced: 2025-07-23
  start: 2013
  end: 2025-07-22
  ongoing: false
crime_type: "[[cybercrime-forum-ic]]"
crime_types:
  - "[[cybercrime-forum-ic]]"
  - "[[malware-ic]]"
  - "[[ransomware-ic]]"
target_entity: "xss.is (formerly DaMaGeLaB) — Russian-speaking cybercrime forum active 2013-2025 with 50,000+ registered users; central marketplace for stolen data, hacking tools, malware, compromised-system access, and ransomware-related services. The administrator (with nearly 20 years of cybercrime activity; alleged pseudonym 'toha' per third-party reporting) also ran thesecure.biz, a private messaging platform tailored to cybercriminals; he served as trusted-third-party arbiter for criminal disputes and guaranteed transaction security, earning EUR 7 million+ in advertising and facilitation fees"
lead_agency: "[[france-national-police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[france]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[france-national-police]]"
  - "[[ukraine-sbu]]"
  - "[[europol-ec3]]"
organizations:
  - "[[france-national-police]]"
  - "[[ukraine-sbu]]"
  - "[[europol-ec3]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "French Police investigation initiated July 2021 by the Brigade de lutte contre la cybercriminalité (Préfecture de Police de Paris)"
  - "Paris Prosecutor (Parquet de Paris — JUNALCO) judicial direction"
  - "Ukrainian Security Service (SBU) — Cybercrime Department + General Prosecutor's Office of Ukraine partnership"
  - "Europol virtual command post established September 2024"
  - "Europol mobile office on-site deployment to Kyiv during the action week"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 arrest in Kyiv, Ukraine on 2025-07-22: suspected forum administrator (alleged pseudonym 'toha' per third-party reporting; not in primary Europol release)"
    - "Forum xss.is (formerly DaMaGeLaB) clearnet domain seized by French BL2C with SBU Cyber Department assistance (per third-party reporting; primary release does not enumerate specific seizure-banner text)"
    - "thesecure.biz private cybercriminal messaging platform attributed to same administrator (status of takedown not enumerated)"
    - "Underlying disrupted ecosystem: 50,000+ registered xss.is users; 12 years of operation (2013-2025); marketplace for stolen data, hacking tools, malware, compromised-system access, ransomware-related services"
    - "Suspect revenue: EUR 7,000,000+ in advertising and facilitation fees over operational lifetime"
    - "Coordinated enforcement actions in Kyiv during the action week for evidence-gathering and infrastructure dismantling"
edges:
  - source_actor: france-national-police
    target_actor: ukraine-sbu
    cooperation_type: joint_investigation
    legal_basis: bilateral
    direction: undirected
  - source_actor: europol-ec3
    target_actor: france-national-police
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
  - source_actor: europol-ec3
    target_actor: ukraine-sbu
    cooperation_type: coordination
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific name and aliases of the arrested administrator (the primary Europol release does not name the administrator; third-party reporting cites 'toha')"
  - "post-2025-07-22 procedural status (extradition request to France, prosecution timeline)"
  - "specific status of the thesecure.biz private messaging platform (primary release describes it but does not enumerate takedown actions on it)"
  - "specific Europol IOCTA 2025 cross-references for xss.is data marketplaces (the report is referenced but not excerpted)"
related_cases: []
related_operations:
  - "[[leakbase-takedown-2026]]"
  - "[[labhost-phishing-as-a-service-takedown-2024]]"
  - "[[archetyp-market-takedown-operation-deep-sentinel-2025]]"
  - "[[operation-stream-kidflix]]"
challenges_encountered: []
lessons_learned:
  - "First wiki record of the French Police Brigade de lutte contre la cybercriminalité (BL2C, Préfecture de Police de Paris) + Paris Prosecutor (Parquet de Paris JUNALCO) as France-side cybercrime authorities leading a transnational cybercrime forum takedown."
  - "First wiki record of the Europol virtual command post mechanism (established September 2024 for this case) as a discrete IC support class — distinct from the on-site coordination centre and the Europol specialist on-site deployment."
  - "Establishes the trusted-third-party-arbiter cybercrime-forum-business-model class — the admin not only ran the forum but also arbitrated criminal disputes and guaranteed transaction security for forum users, earning EUR 7M+ in advertising and facilitation fees over ~12 years of operation."
  - "Multi-platform takedown pattern: xss.is forum + thesecure.biz private messaging service attributed to the same administrator demonstrates the architecture-stack approach for a single high-value cybercrime-infrastructure operator."
  - "Russian-speaking cybercrime forum class (50,000+ users, 12-year operational lifetime) is now formally documented in the wiki via a single primary tier-1 source — complementary to the English-speaking [[leakbase-takedown-2026|LeakBase forum (March 2026, 142,000+ users)]]."
source_count: 1
sources:
  - "[[2025-07-23_europol_xss-is-cybercrime-forum-administrator-arrested-ukraine]]"
summary: "On 2025-07-22 in Kyiv, Ukraine, the suspected administrator of xss.is (formerly DaMaGeLaB) — a 12-year-running Russian-speaking cybercrime forum with 50,000+ registered users — was arrested in a French-led, Ukrainian SBU-partnered, Europol EC3-coordinated takedown. Lead investigators: French Police Brigade de lutte contre la cybercriminalité (BL2C, Préfecture de Police de Paris) + Paris Prosecutor (Parquet de Paris JUNALCO). Ukrainian partners: SBU Cybercrime Department + General Prosecutor's Office of Ukraine. Europol EC3 contributions: virtual command post (September 2024); operational + analytical support throughout; Europol mobile office deployed to Kyiv during the action week. The administrator (allegedly pseudonymous 'toha' per third-party reporting; nearly 20 years of cybercrime activity) also ran thesecure.biz, a private messaging platform for cybercriminals. The administrator earned EUR 7 million+ in advertising and facilitation fees, served as trusted-third-party arbiter for criminal disputes, and guaranteed transaction security for forum users. The xss.is forum was a central marketplace for stolen data, hacking tools, malware, compromised-system access, and ransomware-related services."
created: 2026-05-09
updated: 2026-05-09
---
## Summary

On **2025-07-22** in **Kyiv, Ukraine**, the suspected administrator of **xss.is** (formerly **DaMaGeLaB**) — a 12-year-running Russian-speaking cybercrime forum with **50,000+ registered users** — was arrested in a French-led, Ukrainian SBU-partnered, Europol EC3-coordinated takedown. The forum was a central marketplace for stolen data, hacking tools, malware, compromised-system access, and ransomware-related services. The administrator, who has been active in the cybercrime ecosystem for nearly two decades (allegedly pseudonymous "toha" per third-party reporting), also ran **thesecure.biz**, a private messaging platform tailored to cybercriminals. Through xss.is + thesecure.biz, the suspect is thought to have earned **over EUR 7 million** in advertising and facilitation fees, serving as a trusted-third-party arbiter for criminal disputes and guarantor of transaction security for forum users.

## Background

The forum **xss.is** was active since **2013** (12+ years of operation as of the 2025-07-22 takedown) and operated as a central platform "used to coordinate, advertise and recruit" by some of the most active cybercriminal networks. The Europol release ties xss.is's role explicitly to Europol's **2025 Internet Organised Crime Threat Assessment (IOCTA)**, which highlights the booming black market for stolen data as a critical driver of the cybercrime economy: platforms like xss.is enable the trade and monetisation of compromised data, hacking tools, and illicit services that fuel ransomware, fraud, identity theft, and extortion.

## Participating Parties

| Country | Lead Authority |
|---|---|
| France (lead) | Paris Prosecutor (Parquet de Paris — JUNALCO); [[france-national-police\|French Police — Paris Police Prefecture]] (Préfecture de Police de Paris — Brigade de lutte contre la cybercriminalité / BL2C) |
| Ukraine (partner) | General Prosecutor's Office of Ukraine; [[ukraine-sbu\|Security Service of Ukraine (SBU) — Cybercrime Department]] |
| Coordinating | [[europol-ec3\|Europol European Cybercrime Centre (EC3)]] (virtual command post September 2024; mobile office deployment to Kyiv during action week; analytical and operational support throughout) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2013 | xss.is (formerly DaMaGeLaB) founded; ~20-year cybercrime tenure of administrator begins | Europol 2025-07-23 |
| 2021-07 | French Police initiate investigation | Europol 2025-07-23 |
| 2024-09 | Operational phase moves to Ukraine; French police investigators deployed on the ground; Europol establishes a virtual command post | Europol 2025-07-23 |
| 2025-07-22 (action day) | Suspected administrator arrested in Kyiv; coordinated enforcement actions in Kyiv to gather evidence and dismantle infrastructure; Europol mobile office deployed to Kyiv | Europol 2025-07-23 |
| 2025-07-23 | Europol public announcement | Europol 2025-07-23 |

## Results and Impact

- **1 arrest** in Kyiv, Ukraine: suspected forum administrator.
- **xss.is forum disrupted** (50,000+ registered users, 12 years of operation).
- **thesecure.biz private messaging service** attributed to the same administrator (status of takedown not specified in the cited primary release).
- **EUR 7,000,000+** in suspected criminal revenue from advertising and facilitation fees.
- **Domain seizure**: xss.is clearnet domain taken over by French BL2C with SBU Cyber Department assistance (per third-party reporting; the primary release does not enumerate specific seizure-banner text).
- **Underlying disrupted ecosystem**: stolen-data marketplace, hacking-tool sales, malware sales, compromised-system access sales, ransomware-related services trade.

## Cooperation Mechanisms Used

The cited release describes three discrete IC mechanism classes for this operation:

1. **French-Ukrainian bilateral cybercrime cooperation** with French police investigators deployed on the ground in Ukraine from September 2024 onward.
2. **Europol virtual command post** (established September 2024) — first wiki record of this discrete IC support mechanism class. Distinct from on-site coordination centres and from Europol specialist deployments.
3. **Europol mobile office on-site deployment to Kyiv** during the action week for on-site coordination + evidence collection — structurally similar to the Europol cryptocurrency-expert deployment to Portugal in [[eurojust-100m-crypto-investment-fraud-takedown-2025|the 2025-09 Eurojust €100M crypto-investment-fraud takedown]] and the Europol specialist deployment to the Dutch National Police in [[labhost-phishing-as-a-service-takedown-2024|LabHost takedown]].

## Korean Involvement (한국의 참여)

South Korea is not named in the cited Europol release among the participating jurisdictions. The case is recorded in the wiki for the French-Ukrainian bilateral cooperation pattern + Europol virtual command post mechanism class. Korean exposure to xss.is as a marketplace for stolen Korean credentials / data is *likely* present given the global 50,000+ user scale but is not enumerated in this source.

## Contradictions & Open Questions

- The primary Europol release does not name or alias the arrested administrator; third-party reporting cites pseudonym "toha".
- Post-2025-07-22 procedural status — extradition request to France, prosecution timeline, indictment counts — not enumerated in the cited release.
- The specific status of the thesecure.biz private cybercriminal messaging platform takedown (separate from the xss.is forum takedown) is not enumerated in the cited release.
- The IOCTA 2025 report is referenced contextually but specific xss.is excerpts from IOCTA 2025 are not provided in the cited release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-07-23_europol_xss-is-cybercrime-forum-administrator-arrested-ukraine\|Key figure behind major Russian-speaking cybercrime forum targeted in Ukraine]] | Europol | 2025-07-23 | https://www.europol.europa.eu/media-press/newsroom/news/key-figure-behind-major-russian-speaking-cybercrime-forum-targeted-in-ukraine |
