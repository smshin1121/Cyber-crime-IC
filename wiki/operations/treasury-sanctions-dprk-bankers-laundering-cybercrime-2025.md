---
type: operation
title: "Treasury Sanctions DPRK Bankers and Institutions for Laundering Cybercrime and IT Worker Proceeds (November 2025)"
title_ko: "DPRK 사이버범죄 및 IT 노동자 자금세탁 관련 미 재무부 제재 (2025년 11월)"
aliases:
  - "OFAC SB-0302 DPRK Bankers"
  - "Treasury DPRK Cyber Laundering Designations 2025"
  - "OFAC First Credit Bank / Ryujong / KMCTC Designations"
case_id: CYB-2025-110
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-11-04
  start: ""
  end: 2025-11-04
  ongoing: false
crime_type: "[[money-laundering-ic]]"
crime_types:
  - "[[money-laundering-ic]]"
  - "[[online-fraud-ic]]"
target_entity: "Eight individuals and two entities involved in laundering funds derived from DPRK cybercrime (including ransomware) and IT worker fraud schemes — DPRK bankers, China- and Russia-based DPRK financial representatives, Ryujong Credit Bank, and Korea Mangyongdae Computer Technology Company (KMCTC)."
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[north-korea]]"
  - "[[china]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-treasury]]"
organizations:
  - "[[us-treasury]]"
mechanisms_used:
  - "[[asset-freezing]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Executive Order 13694 (as amended by E.O. 13757, E.O. 14144, E.O. 14306) — Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities, section 1(a)(ii)(D)"
  - "Executive Order 13810 — Imposing Additional Sanctions With Respect to North Korea"
  - "Executive Order 13551 — Blocking Property of Certain Persons With Respect to North Korea"
  - "Executive Order 13722 — Blocking the Property of the Government of North Korea and the Workers' Party of Korea, and Prohibiting Certain Transactions With Respect to North Korea"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "8 individuals designated: Jang Kuk Chol, Ho Jong Son, U Yong Su, Ho Yong Chol, Han Hong Gil, Jong Sung Hyok, Choe Chun Pom, Ri Jin Hyok"
    - "2 entities designated: Korea Mangyongdae Computer Technology Company (KMCTC), Ryujong Credit Bank"
    - "First Credit Bank SDN List entry updated to highlight cryptocurrency addresses and activity"
    - "$5.3 million in cryptocurrency identified as managed by Jang and Ho Jong Son for First Credit Bank, partially traced to a DPRK ransomware actor with U.S. victims"
    - "Documented illicit transaction volumes by designees: Ho Yong Chol $2.5M (Korea Daesong Bank) + $85M (other DPRK group); Han Hong Gil $630K; Choe Chun Pom $200K; Ri Jin Hyok $350K"
    - "Cumulative DPRK metric cited: over $3 billion stolen by DPRK-affiliated cybercriminals over past three years, primarily in cryptocurrency"
edges:
  - source_actor: us-treasury
    target_actor: north-korea
    cooperation_type: asset_recovery
    legal_basis: e.o.-13694-13810-13551-13722
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - cryptocurrency_seized (release names funds linked to designees but does not state seizure dollar amount)
  - specific MSMT partner-state actions concurrent with this designation
  - identity of the "DPRK ransomware actor" referenced in connection with First Credit Bank funds
  - whether China or Russia provided any cooperation or were merely host jurisdictions for designees
related_cases: []
related_operations:
  - "[[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025]]"
challenges_encountered:
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "Sanctions targeting DPRK financial-enabler networks require persistent designation of representatives operating from third-country jurisdictions (China, Russia), since the underlying institutions are already blocked."
  - "Cryptocurrency-laundering pathways can be addressed through SDN List enrichment (publishing on-chain addresses) in addition to traditional designations."
  - "MSMT collective monitoring is highly likely an important multilateral predicate for unilateral OFAC actions against DPRK cyber/IT worker financial networks, even where the designations themselves are U.S.-only."
  - "DPRK IT worker revenue obfuscation through Chinese-national banking proxies is a persistent vector that designations alone are unlikely to dismantle without parallel enforcement in host states."
source_count: 1
sources:
  - "[[2025-11-04_treasury_dprk-bankers-laundering-cybercrime-it-worker-funds]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional page
> This operation page is published from a single tier-1 source (OFAC SB-0302). Per the project's preferred publication threshold (`source_count >= 5`), it is treated as provisional pending corroborating sources (MSMT report excerpt, follow-on enforcement actions, partner-state designations).

## Summary

On 2025-11-04, the U.S. Department of the Treasury's Office of Foreign Assets Control ([[us-treasury|OFAC]]) announced press release SB-0302, designating eight individuals and two entities for laundering funds derived from DPRK cybercrime (including ransomware against U.S. victims) and DPRK IT worker fraud schemes. The action targeted (1) two North Korean bankers managing cryptocurrency for previously-designated First Credit Bank; (2) Korea Mangyongdae Computer Technology Company (KMCTC) and its president for IT worker delegation operations from China; (3) Ryujong Credit Bank for sanctions-evasion remittance between China and North Korea; and (4) five China- or Russia-based representatives of already-designated DPRK financial institutions. OFAC also updated First Credit Bank's SDN entry to surface its cryptocurrency addresses, an enforcement step that is highly likely intended to support compliance screening by virtual-asset service providers.

## Background

Per the release, the Government of the DPRK relies on cybercrime as a significant illicit-revenue stream for its weapons of mass destruction (WMD) and ballistic missile programs. Treasury cites that over the past three years, North Korea-affiliated cybercriminals have stolen over $3 billion, primarily in cryptocurrency. In parallel, DPRK IT workers earn hundreds of millions of dollars per year by obfuscating their nationality on freelance work platforms, sometimes splitting revenue with non-DPRK freelance partners.

The designations are explicitly framed against the backdrop of the October 22 (2025) Multilateral Sanctions Monitoring Team (MSMT) report titled "The DPRK's Violation and Evasion of UN Sanctions Through Cyber and Information Technology Worker Activities." Treasury describes the multilateral context as "stand[ing] alongside the other MSMT participating states in remaining committed to strengthening collective resilience against such threats."

## Designated Targets

**Bankers managing cybercrime cryptocurrency proceeds (E.O. 13694 as amended + E.O. 13810):**

- **Jang Kuk Chol** — North Korean banker, managed funds (including $5.3M in cryptocurrency) for [[north-korea|DPRK]]-designated First Credit Bank.
- **Ho Jong Son** — North Korean banker, same scheme as Jang.

**IT worker delegation network (E.O. 13810):**

- **Korea Mangyongdae Computer Technology Company (KMCTC)** — North Korea-based IT company operating worker delegations from Shenyang and Dandong, [[china]].
- **U Yong Su** — KMCTC president.

**Sanctions-evasion financial institution (E.O. 13810):**

- **Ryujong Credit Bank** — North Korea-based financial institution, facilitated sanctions-avoidance activities between [[china]] and [[north-korea]].

**Overseas representatives of DPRK financial institutions:**

- **Ho Yong Chol** (E.O. 13551) — representative of Korea Daesong Bank; facilitated $2.5M (USD/CNY) on behalf of Korea Daesong Bank, plus $85M+ on behalf of another DPRK government-affiliated group.
- **Han Hong Gil** (E.O. 13810) — Koryo Commercial Bank (KCB) employee; coordinated $630K+ (USD/CNY) on behalf of Ryugyong Commercial Bank.
- **Jong Sung Hyok** (E.O. 13722) — FTB chief representative in Vladivostok, [[russia]].
- **Choe Chun Pom** (E.O. 13722) — DPRK Central Bank representative; facilitated $200K+ (USD/CNY) and coordinated travel for Russian officials to Pyongyang.
- **Ri Jin Hyok** (E.O. 13722) — FTB representative; facilitated $350K+ (USD/CNY/EUR) for FTB front company.

## Participating Parties

- **Lead/coordinating agency:** [[us-treasury|U.S. Department of the Treasury (OFAC)]].
- **Country jurisdiction of action:** [[united-states]] (designating authority).
- **Subject jurisdictions of designees:** [[north-korea]] (DPRK-based bankers and entities), [[china]] (host of KMCTC delegations and several DPRK financial representatives), [[russia]] (host of Vladivostok-based FTB representative).

The release does not name specific cooperating foreign agencies for this particular designation; it does, however, position the action within the multilateral MSMT framework.

## Legal Framework

The legal authorities cited verbatim in the release are:

- **E.O. 13694** (as amended by **E.O. 13757**, **E.O. 14144**, and **E.O. 14306**), section 1(a)(ii)(D) — "Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities" (used for Jang Kuk Chol and Ho Jong Son).
- **E.O. 13810** — DPRK-specific authority for North Korean persons, the IT industry, and the financial services industry (used for Jang, Ho Jong Son, KMCTC, U Yong Su, Ryujong Credit Bank, Han Hong Gil).
- **E.O. 13551** — DPRK financial-network authority (used for Ho Yong Chol, given his Korea Daesong Bank nexus).
- **E.O. 13722** — DPRK government / Workers' Party authority (used for Jong Sung Hyok, Ri Jin Hyok, Choe Chun Pom).

The release also references **multiple UN Security Council resolutions (UNSCRs)** and the **Multilateral Sanctions Monitoring Team (MSMT)** as multilateral predicates.

## Operational Timeline

| Date | Event |
|---|---|
| 2025 (prior) | First Credit Bank, Korea Daesong Bank, KCB, Ryugyong Commercial Bank, FTB, and DPRK Central Bank previously designated by OFAC. |
| 2025-10-22 | MSMT report "The DPRK's Violation and Evasion of UN Sanctions Through Cyber and Information Technology Worker Activities" issued. |
| 2025-11-04 | OFAC press release SB-0302 issued; 8 individuals and 2 entities designated; First Credit Bank SDN entry updated to surface cryptocurrency addresses. |

## Results and Impact

Per the verbatim release:

- **10 designations**: 8 individuals + 2 entities.
- **First Credit Bank SDN entry updated** with cryptocurrency addresses (compliance-screening enrichment).
- **All property and interests in property of designees** in U.S. jurisdiction or under U.S. person control are blocked and must be reported to OFAC.
- **50% derivative-blocking rule** applies to entities owned in aggregate by designees.
- **Secondary sanctions risk** flagged for non-U.S. financial institutions transacting with designees.

The release does not state a specific dollar amount of frozen U.S. assets attributable to this designation; the dollar figures cited (e.g., $5.3M cryptocurrency, $85M USD transactions) describe documented illicit activity, not seizures.

## Cooperation Mechanisms Used

- **[[asset-freezing]]** — primary mechanism; SDN List blocking action triggers U.S. jurisdictional asset freeze.
- **[[informal-cooperation]]** — the MSMT framework is explicitly cited as the multilateral context, though MSMT itself is a monitoring/reporting body, not a designation authority. Likely indicating informal information-sharing predicate for the designations.

The release does not document any formal mutual legal assistance, extradition, or joint investigation with [[china]] or [[russia]]; both countries appear as host jurisdictions of designees rather than cooperating partners.

## Challenges and Friction Points

- **[[jurisdictional-conflicts]]** — Several designees operate from [[china]] (Shenyang, Dandong) and [[russia]] (Vladivostok). U.S. designations cannot directly compel arrests or asset freezes in those jurisdictions; secondary-sanctions exposure is the indirect lever.
- **Cryptocurrency obfuscation** — Highly likely a persistent challenge; OFAC's SDN-List enrichment with on-chain addresses is a partial mitigant for compliance screening but does not recover already-laundered funds.
- **DPRK IT worker identity obfuscation** — Use of false/stolen identities and Chinese-national banking proxies is unlikely to be resolved by designations alone without enforcement in host states.

## Lessons Learned

- Sanctions targeting DPRK financial-enabler networks require persistent designation of overseas representatives, since the underlying institutions are already blocked.
- Cryptocurrency-laundering pathways can be addressed through SDN List enrichment (publishing on-chain addresses) alongside designations.
- MSMT collective monitoring is highly likely an important multilateral predicate for unilateral OFAC actions, even where the designations themselves are U.S.-only.

## Follow-Up Actions

The release indicates that "Treasury will continue to pursue the facilitators and enablers behind these schemes." Follow-on designations against additional DPRK financial enablers and IT-worker network operators are highly likely over the medium term.

## Korean Involvement (한국의 참여)

The release does not document direct involvement by [[south-korea]] (ROK) law enforcement or financial regulators in this U.S. action. Given South Korea's role as a frequent target of DPRK cyber-enabled financial theft and as a participant in the MSMT framework, parallel ROK actions or information-sharing are roughly even chance to have occurred but are not documented in this primary source.

## Contradictions & Open Questions

- The release does not name the "DPRK ransomware actor" linked to a portion of the $5.3M cryptocurrency managed by First Credit Bank. Identification would clarify the connection to broader [[ransomware-ic|ransomware]] operations.
- Whether [[china]] or [[russia]] provided cooperation, refused cooperation, or were not engaged at all by U.S. authorities prior to designation is not stated.
- The relationship between this OFAC action and the [[us-doj-coordinated-nationwide-actions-dprk-it-workers-2025|2025 DOJ DPRK IT-worker enforcement actions]] is not explicitly described, though both target the same revenue-generation ecosystem.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2025-11-04_treasury_dprk-bankers-laundering-cybercrime-it-worker-funds\|Treasury Sanctions DPRK Bankers and Institutions Involved in Laundering Cybercrime Proceeds and IT Worker Funds]] | US Department of the Treasury (OFAC), Press Release SB-0302 | 2025-11-04 | https://home.treasury.gov/news/press-releases/sb0302 |
