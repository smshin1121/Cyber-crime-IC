---
type: operation
title: "Singapore-Thailand Joint Arrest of ALTDOS / DESORDEN / GHOSTR / 0mid16B Data-Breach-Extortion Threat Actor (SPF + Royal Thai Police, 26 February 2025)"
title_ko: "싱가포르·태국 합동 데이터 침해·갈취 위협 행위자 검거 — ALTDOS/DESORDEN/GHOSTR/0mid16B (싱가포르 경찰청 + 태국 왕립경찰, 2025-02-26)"
aliases:
  - "ALTDOS arrest"
  - "DESORDEN arrest"
  - "GHOSTR arrest"
  - "0mid16B arrest"
  - "Singapore Police Royal Thai Police 75-case data breach takedown 2025"
case_id: CYB-2025-201
period: 3
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2025-02-27
  start: 2020
  end: 2025-02-26
  ongoing: false
crime_type: "[[hacking-ic]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[extortion-ic]]"
target_entity: "Single 39-year-old male threat actor operating since 2020 under sequential aliases ALTDOS, DESORDEN, GHOSTR, and 0mid16B — responsible for at least 75 international data-breach-extortion cases (per SPF release; 90+ victims and 13TB of stolen personal data per the corresponding Group-IB release). Actor exploited SQL-injection (sqlmap) and vulnerable Remote Desktop Protocol (RDP) servers to gain unauthorized access, installed cracked CobaltStrike beacons for control, and exfiltrated databases to rented cloud servers. Extortion model: pay-or-be-doxxed against victims, with reputational-pressure escalation via direct customer notifications, media tip-offs, and notifications to data-protection regulators. Victim industries: healthcare, retail, property investment, finance, e-commerce, logistics, technology, hospitality, insurance, recruitment. Victim geography: Thailand, Singapore, Malaysia, Indonesia, India (Asia-Pacific 65 cases), plus UK, US, Canada, and Middle East."
lead_agency: "[[singapore-police]]"
coordinating_body: "[[singapore-police]]"
participating_countries:
  - "[[singapore]]"
  - "[[thailand]]"
participating_agencies:
  - "[[singapore-police]]"
  - "[[thailand-royal-police]]"
organizations:
  - "[[singapore-police]]"
  - "[[thailand-royal-police]]"
mechanisms_used:
  - "[[informal-cooperation]]"
legal_basis:
  - "Bilateral SPF-RTP cybercrime cooperation under standing police-to-police channels (no specific MLAR reference in cited release)."
  - "Thai Criminal Code and Computer-Related Crime Act — basis for the 26 February 2025 arrest in Thailand."
  - "Singapore criminal procedure (Computer Misuse Act etc.) for potential downstream Singapore-side charges arising from the 11 Singapore-victim reports."
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Assets seized: > 10 million THB (laptops, mobile phones, luxury vehicles, branded bags)"
    - "International cases attributed: 75+ (per SPF; 90+ per corresponding Group-IB release)"
    - "Stolen data volume: 13TB+ (per Group-IB release; not enumerated in SPF release)"
    - "Victim countries: Thailand, Singapore, Malaysia, Indonesia, India, UK, US, Canada, Middle East"
    - "Singapore victims (initial): 11 (the triggering report set in 2020)"
    - "Investigation duration: ~5 years (2020 → February 2025)"
    - "Threat-actor aliases tracked: ALTDOS, DESORDEN, GHOSTR, 0mid16B"
edges:
  - source_actor: singapore-police
    target_actor: thailand-royal-police
    cooperation_type: joint_investigation
    legal_basis: bilateral
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific name of the 39-year-old arrested individual (the cited release does not name him)"
  - "specific charges enumerated under Thai Criminal Code / Computer-Related Crime Act"
  - "specific list of 75 victim entities"
  - "specific Singapore-side charging status (the cited release notes 'investigations are ongoing' on the Singapore side)"
  - "specific role of Cyber Security Agency (CSA) of Singapore beyond 'uncovering valuable leads'"
  - "specific role of Group-IB (the cited SPF release does not name Group-IB; only the corresponding Group-IB private-sector release names them)"
  - "specific RDP / SQL-injection victim CVE / vulnerability detail (Group-IB release identifies the modus operandi but not specific exploited products)"
related_cases: []
related_operations:
  - "[[spf-fpb-operation-cryptoscam-2025]]"
  - "[[afp-rtp-bangkok-scam-centre-operation-firestorm-2025]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "**SPF-RTP bilateral cybercrime cooperation track** is documented as a sustained ~5-year channel capable of producing a multi-alias data-breach-extortion arrest. Adds to the wiki's coverage of SPF-RTP cooperation alongside [[afp-rtp-bangkok-scam-centre-operation-firestorm-2025|AFP-RTP Bangkok Operation Firestorm]] (2025) and [[spf-fpb-operation-cryptoscam-2025|SPF-FPB Operation CryptoScam]] (2025) — establishing Thailand as a recurring SE-Asia cooperation hub for cybercrime LE."
  - "**Cross-jurisdictional alias-correlation tradecraft as the analytical foundation**: ALTDOS → DESORDEN → GHOSTR → 0mid16B (4 aliases over 5 years) required sustained writing-style + format-of-posts + posting-website + target-region pattern analysis to attribute to one actor. The arrest could not have occurred without this analytical layer."
  - "**Extortion-without-encryption pattern is structurally distinct from ransomware**: actor exfiltrated databases and extorted victims for *non-disclosure* (pay or be doxxed) rather than encrypting. Establishes a discrete attack-pattern category in the wiki for *data-breach-extortion-as-a-service* threat actors complementing the ransomware corpus."
  - "**Reputational-pressure escalation as the secondary monetisation channel**: when victims refused payment, the actor notified media and data-protection regulators rather than dumping data immediately on dark web forums. Demonstrates an evolved coercion technique that exploits regulatory reporting infrastructure as an extortion tool."
  - "**Public-private partnership pattern**: Group-IB DCRCs (Singapore + Thailand) provided the long-run private-sector tracking layer; SPF Cybercrime Command + RTP CIB + CSA Singapore provided the public-sector arrest-and-prosecution layer. The cited SPF release thanks CSA Singapore but does not name Group-IB; Group-IB's parallel release names itself as the technical contributor."
  - "**11 Singapore victim reports as the catalyst** for an investigation that grew to 75+ international cases. Demonstrates the multiplier effect of effective national victim-reporting infrastructure (Singapore had it; the actor's Asia-Pacific footprint outside Singapore went largely unreported)."
source_count: 1
sources:
  - "[[2025-02-27_spf-singapore_global-hacker-arrested-thailand-altdos-desorden-ghostr-0mid16b]]"
created: 2026-05-09
updated: 2026-05-09
---

## Summary

On **26 February 2025**, the **Royal Thai Police (RTP) Central Investigation Bureau (CIB)** arrested a **39-year-old male threat actor** in Thailand, suspected of operating under sequential aliases **ALTDOS, DESORDEN, GHOSTR, and 0mid16B** since 2020 and responsible for at least **75 international data-breach-extortion cases** (per SPF; the corresponding Group-IB release reports 90+ victims and 13TB of stolen personal data). The arrest concluded a **~5-year cross-border investigation** led by the **Singapore Police Force Cybercrime Command (SPF CCC)** in collaboration with RTP CIB, supported by the **Cyber Security Agency (CSA) of Singapore** and (per Group-IB) **Group-IB's Digital Crime Resistance Centers in Singapore and Thailand**.

Charges (Thailand): Thai Criminal Code + Computer-Related Crime Act. Assets seized: **> 10 million THB** including laptops, mobile phones, luxury vehicles, and branded bags.

> [!note] 4-alias 5-year correlation
> ALTDOS → DESORDEN → GHOSTR → 0mid16B over 5 years (2020–2025) required sustained writing-style + format-of-posts + posting-website + target-region pattern analysis to attribute to one actor. The arrest depended on this analytical tradecraft layer.

## Background

The threat actor's tradecraft (per Group-IB and corroborated by the SPF release):

- **Initial access**: SQL injection (sqlmap) + RDP exploitation against vulnerable internet-facing servers
- **Persistence/control**: Cracked CobaltStrike beacon
- **Exfiltration**: Database export to rented cloud servers (no significant lateral movement)
- **Monetisation primary**: Ransom demand to victim for non-disclosure
- **Monetisation secondary** (when victims refused): Reputational-pressure escalation — direct customer notifications via email or instant messengers; tip-offs to media; notifications to data-protection regulators
- **Monetisation tertiary**: Sale of unique data leaks on dark web forums

Victim industries: healthcare, retail, property investment, finance, e-commerce, logistics, technology, hospitality, insurance, recruitment.

Victim geography (per Group-IB release): primary Asia-Pacific (Thailand, Singapore, Malaysia, Indonesia, India — 65 cases) + UK, US, Canada, Middle East (later phases under GHOSTR / 0mid16B aliases).

The 4-alias trajectory: ALTDOS (Thailand-focus, 2020+) → DESORDEN (Asia-Pacific industry breadth) → GHOSTR (international expansion) → 0mid16B (latest). Group-IB attributed the aliases to one actor based on writing-style correlation, format-of-posts, posting-website preferences, target-region overlap, and timeline correlations.

## Participating Parties

| Agency | Country | Role |
|---|---|---|
| [[singapore-police\|Singapore Police Force (SPF) Cybercrime Command]] | Singapore | **Lead investigative agency**; sustained 5-year tracking from initial 11 Singapore victim reports |
| [[thailand-royal-police\|Royal Thai Police (RTP) Central Investigation Bureau]] | Thailand | **Arresting authority** (26 February 2025); evidence seizure (> 10M THB) |
| Cyber Security Agency (CSA) of Singapore | Singapore | Singapore-side leads support |
| Group-IB Digital Crime Resistance Centers (DCRCs) | Singapore + Thailand | Private-sector long-run tracking + alias correlation (2020–2025) |

## Legal Framework

- **Bilateral SPF-RTP cybercrime cooperation** under standing police-to-police channels — the cited release does not specify a single MLAR or treaty instrument.
- **Thai Criminal Code + Computer-Related Crime Act** — basis for the 26 February 2025 arrest in Thailand.
- **Singapore criminal procedure** (Computer Misuse Act etc.) for potential downstream Singapore-side charges arising from the 11 original Singapore-victim reports.

> [!warning] Legal status check needed
> The cited SPF release does not enumerate specific Thai Criminal Code provisions or Computer-Related Crime Act articles. Subsequent Thai prosecutorial documents may clarify.

## Operational Timeline

| Date | Event |
|---|---|
| 2020 | 11 Singapore victims report ransom demands; SPF Cybercrime Command opens investigation |
| 2020 → 2025 | Sustained tracking by SPF CCC + RTP CIB + Group-IB DCRCs across alias trajectory ALTDOS → DESORDEN → GHOSTR → 0mid16B |
| 2023 | Threat actor banned from data-leak forum for 'scamming' (per Group-IB) |
| 2024 | Threat actor banned from another forum for multi-accounting (per Group-IB) |
| 26 February 2025 | RTP CIB arrests 39-year-old male in Thailand; > 10M THB in assets seized |
| 27 February 2025 | SPF press release announcement |

## Results and Impact

| Metric | Value | Notes |
|---|---|---|
| Arrests | 1 | 39-year-old male, in Thailand |
| Aliases tracked | 4 | ALTDOS, DESORDEN, GHOSTR, 0mid16B |
| International cases | 75+ (SPF) / 90+ (Group-IB) | Asia-Pacific 65 cases per Group-IB |
| Stolen data | 13TB+ (per Group-IB) | Personal data |
| Assets seized | > 10 million THB | Laptops, mobile phones, luxury vehicles, branded bags |
| Initial Singapore victims | 11 | Triggering 2020 report set |

## Cooperation Mechanisms Used

- **SPF Cybercrime Command — RTP CIB direct bilateral cooperation** (police-to-police, ~5 years sustained)
- **CSA Singapore as Singapore-side cyber-intelligence support** (uncovering valuable leads)
- **Group-IB DCRCs (Singapore + Thailand) as private-sector long-run tracking layer**
- **Cross-jurisdictional alias-correlation tradecraft** as the analytical foundation enabling the eventual arrest

## Challenges and Friction Points

- **Multi-alias persistence**: 4 aliases over 5 years required sustained tracking. Most jurisdictions have neither the budget nor the analytical depth to do this for a single non-state-sponsored cybercriminal.
- **Reporting asymmetry**: 11 Singapore victims initially reported, but Asia-Pacific neighbouring countries appear to have under-reported. The investigation grew because Singapore reporting infrastructure detected the pattern; without it, the actor *likely* would have continued operating.
- **Extortion-not-encryption pattern**: traditional ransomware-focused investigation playbooks may not detect data-breach-extortion actors quickly because there is no encryption signal — only the ransom demand and (eventually) data leaks.

## Lessons Learned

1. **SPF-RTP bilateral cybercrime track** is a documented sustained channel for cross-border cybercrime arrests. Pairs with [[afp-rtp-bangkok-scam-centre-operation-firestorm-2025|AFP-RTP Bangkok Firestorm]] (2025) and [[spf-fpb-operation-cryptoscam-2025|SPF-FPB CryptoScam]] (2025) to establish Thailand as a SE-Asia cybercrime LE cooperation hub.
2. **4-alias / 5-year correlation tradecraft** is the analytical foundation for arrests of multi-alias data-breach-extortion actors. Public-private partnership (police + Group-IB-style threat-intelligence vendors) is the documented format.
3. **Extortion-without-encryption** is a structurally distinct pattern from ransomware — exfiltrate-and-extort (with reputational-pressure escalation) rather than encrypt-and-extort. Warrants its own analytical category.
4. **Reputational-pressure escalation via media + DP regulators** is an evolved coercion technique that exploits regulatory reporting infrastructure as an extortion tool.
5. **National victim-reporting infrastructure as multiplier**: 11 Singapore victims → 75+ international cases discovered because Singapore reporting caught the pattern. Documents the value of low-friction national cybercrime victim reporting.

## Follow-Up Actions

The cited release notes 'investigations are ongoing'. Specific Thailand-side charging documents, Singapore-side parallel charges, and any extradition activity are *unknown* from the cited release.

## Korean Involvement (한국의 참여)

[[south-korea|South Korea]] has no documented involvement in this case. Korean victims among the 75+ international set are *unknown* from the cited SPF release; the corresponding Group-IB release does not enumerate Korean victims either. KNPA Cyber Bureau ↔ SPF/RTP cooperation channels are not enumerated in this case.

## Contradictions & Open Questions

- **Suspect name**: not in the cited release (only age 39 and male).
- **Cited 75 vs. Group-IB 90+**: the SPF release reports 'at least 75 cases internationally' while Group-IB reports 'more than 90 instances of data leaks worldwide'. Likely the difference reflects different counting methodologies (case files vs. distinct data leaks) rather than contradiction.
- **Specific Thai charges**: not enumerated in the cited release.
- **Singapore-side charges**: 'investigations are ongoing' — outcome unknown.
- **Group-IB attribution**: not named in the SPF release; only named in the parallel Group-IB private-sector release.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2025-02-27_spf-singapore_global-hacker-arrested-thailand-altdos-desorden-ghostr-0mid16b\|Global Hacker Arrested In Thailand Arising From Joint Collaboration Between The Singapore Police Force And Royal Thai Police]] | Singapore Police Force | 2025-02-27 | https://www.police.gov.sg/media-hub/news/2025/02/20250227_global_hacker_arrested_in_thailand_arising_from_joint_collaboration_between_spf |
