---
type: operation
title: "Operation OCTOPUS — Czech-Ukrainian Investment-Fraud Call-Centre Takedown (2025)"
aliases:
  - "Operace OCTOPUS"
  - "OCTOPUS investment fraud Kyiv 2025"
case_id: CYB-2025-OCTOPUS-CZ
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - search-seizure
  - asset_freeze
outcome: success
timeframe:
  announced: 2025-12-16
  start: ""
  end: 2025-11-20
  ongoing: false
crime_types:
  - "[[online-fraud-ic]]"
  - "[[organized-crime-ic]]"
  - "[[money-laundering-ic]]"
crime_type: "[[online-fraud-ic]]"
target_entity: "Investment-fraud call-centre network operating from Kyiv, run by an organized criminal group offering bogus investment products to victims in the Czech Republic and other EU member states"
lead_agency: "[[czechia-police]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[czech-republic]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[czechia-police]]"
  - "[[ukraine-sbu]]"
  - "[[ukraine-police]]"
  - "[[eurojust]]"
legal_basis:
  - "Joint Investigation Team agreement between the Czech Republic and Ukraine, hosted and judicially coordinated by [[eurojust|Eurojust]]"
  - "Czech domestic substantive and procedural law on cyber-enabled fraud and organized crime (investigated by NCTEKK)"
  - "Ukrainian domestic law on fraud, organized crime, and unauthorized access (executed by SBU and National Police of Ukraine)"
mechanisms_used:
  - "[[joint-investigation-team]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[search-seizure]]"
  - "[[electronic-evidence]]"
  - "[[asset-freezing]]"
results:
  arrests: 17
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 138
  other:
    - "19 house searches conducted in Kyiv"
    - "Approximately CZK 33 million seized in mixed currencies"
    - "CRM systems, victim personal data, computer equipment, and mobile phones seized"
    - "31-year-old organizer from the Donetsk region of Ukraine identified as principal"
    - "138 identified victims; estimated true victim count in the thousands across the EU and beyond"
    - "Confirmed damage of CZK 43 million among the identified 138 victims"
edges:
  - source_actor: "czechia-police"
    target_actor: "ukraine-sbu"
    cooperation_type: "joint_investigation"
    legal_basis: "JIT_via_Eurojust"
    direction: "undirected"
  - source_actor: "czechia-police"
    target_actor: "ukraine-police"
    cooperation_type: "joint_investigation"
    legal_basis: "JIT_via_Eurojust"
    direction: "undirected"
  - source_actor: "eurojust"
    target_actor: "czechia-police"
    cooperation_type: "joint_investigation"
    legal_basis: "JIT_via_Eurojust"
    direction: "directed"
  - source_actor: "eurojust"
    target_actor: "ukraine-police"
    cooperation_type: "joint_investigation"
    legal_basis: "JIT_via_Eurojust"
    direction: "directed"
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments"
  - "servers_seized"
  - "domains_seized"
  - "cryptocurrency_seized"
  - "start_date"
related_cases: []
related_operations:
  - "[[ukraine-fraudulent-call-centres-takedown-2025]]"
  - "[[dnipro-fraudulent-call-centre-takedown-2026]]"
  - "[[operation-eur-3m-online-investment-fraud-2025]]"
challenges_encountered: []
lessons_learned:
  - "Bilateral CZ-UA Joint Investigation Teams under Eurojust judicial coordination are reachable for cyber-enabled investment-fraud cases even when Ukraine is not an EU member state, provided Eurojust hosts the JIT instrument."
  - "A single press-release event can announce two operationally distinct JITs (OCTOPUS bilateral CZ-UA and CONNECT quadrilateral CZ-UA-LT-LV); operational separation must be preserved even when joint communication suggests a single action."
source_count: 1
sources:
  - "[[2025-12-16_policie-cz_operation-octopus-investment-fraud-takedown-kyiv]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional record
> This page is published with a single tier-1 primary source (Czech Police NCTEKK press release of 2025-12-16). Below the preferred publication threshold of `source_count >= 5`, but retained because the source is a tier-1 official press release that uniquely names this branch of the operation. To be enriched as additional Eurojust, Ukrainian Prosecutor General, or independent reporting becomes available.

## Summary

Operation OCTOPUS was an investment-fraud call-centre takedown coordinated by [[eurojust|Eurojust]] through a bilateral [[joint-investigation-team|Joint Investigation Team]] between the [[czech-republic|Czech Republic]] and [[ukraine|Ukraine]]. The Czech [[czechia-police|National Centre Against Terrorism, Extremism and Cybercrime (NCTEKK)]], the [[ukraine-sbu|Security Service of Ukraine (SBU)]], and the [[ukraine-police|National Police of Ukraine]] dismantled a Kyiv-based criminal group that was offering fraudulent investment products to victims in the Czech Republic and other EU member states.

On the action day of 2025-11-20, Ukrainian authorities executed 19 house searches in Kyiv, detained 17 persons, and seized approximately CZK 33 million in mixed currencies along with CRM systems, victim personal data, computer equipment, and mobile phones. The group's principal organizer is named in the Czech Police release as a 31-year-old from the Donetsk region. To date, 138 victims have been identified with confirmed losses of CZK 43 million; the actual victim count is highly likely to be in the thousands across the EU and beyond, based on the Czech Police's own framing.

The operation was announced jointly with [[ukraine-fraudulent-call-centres-takedown-2025|Operation CONNECT]] in a Czech Police press release of 2025-12-16. The two operations are operationally distinct: OCTOPUS was a bilateral CZ-UA JIT against an investment-fraud network, whereas CONNECT was a quadrilateral CZ-UA-LT-LV JIT against police/bank impersonation call centres.

## Background

Investment-fraud call-centre networks are a well-documented strand of European cybercrime activity that connects [[online-fraud-ic|online investment fraud]] with cross-border [[organized-crime-ic|organized criminal groups]]. Operations such as the [[eurojust-100m-crypto-investment-fraud-takedown-2025|EUR 100 million crypto investment fraud takedown]] and [[crypto-investment-fraud-spain-460m-takedown-2025|Spain EUR 460 million crypto investment fraud takedown]] illustrate the same general pattern of high-volume call-centre infrastructure servicing multinational victim pools through cold-call boiler-room sales.

The OCTOPUS investigation matured during 2024-2025 in parallel with [[ukraine-fraudulent-call-centres-takedown-2025|Operation CONNECT]]. The Czech Police press release groups the two operations under a single communication but is explicit that the JIT compositions, fraud schemes, action days, and victim populations differ.

## Participating Parties

| Role | Party |
|---|---|
| Lead investigative authority (CZ) | [[czechia-police|NCTEKK — National Centre Against Terrorism, Extremism and Cybercrime]] |
| Operational partner (UA) | [[ukraine-sbu|Security Service of Ukraine (SBU)]] |
| Operational partner (UA) | [[ukraine-police|National Police of Ukraine]] |
| Judicial coordination | [[eurojust|Eurojust]] |
| Source-backed participating countries | [[czech-republic|Czech Republic]], [[ukraine|Ukraine]] |

The Czech Police press release does not name a Czech prosecution authority, a Ukrainian Prosecutor General contact, or any third-state participation in OCTOPUS specifically. The press release is silent on Europol involvement.

## Legal Framework

The case was coordinated by [[eurojust|Eurojust]] through a [[joint-investigation-team|Joint Investigation Team]] between the Czech Republic and Ukraine. Ukraine is a non-EU partner; Eurojust hosting of CZ-UA JITs has been a recurrent instrument for cyber-enabled fraud cases involving Ukrainian-based call-centre infrastructure.

The Czech Police press release does not cite specific articles of the Czech criminal code, the Ukrainian criminal code, or the [[budapest-convention|Budapest Convention]]. As a fact, both states are parties to the Budapest Convention, which provides background harmonization for substantive cybercrime offenses and procedural powers, although it is not asserted as the legal basis in this release.

## Operational Timeline

| Date | Event |
|---|---|
| Pre-2025-11-20 | Joint investigation conducted under a Eurojust-coordinated bilateral CZ-UA JIT (start date not disclosed in the source) |
| 2025-11-20 | OCTOPUS action day in Kyiv: 19 house searches, 17 detentions, CZK 33 million in seizures |
| 2025-12-09 | Separate CONNECT action day (Kyiv, Ivano-Frankivsk, Dnipro) — see [[ukraine-fraudulent-call-centres-takedown-2025]] |
| 2025-12-16 | NCTEKK joint press release announcing both OCTOPUS and CONNECT |

## Results and Impact

- 17 persons detained
- 19 house searches executed in Kyiv
- Approximately CZK 33 million in mixed-currency seizures
- 138 identified victims to date; CZK 43 million in confirmed losses
- Principal organizer identified: 31-year-old from the Donetsk region of Ukraine
- CRM systems, victim databases, computers, and mobile phones seized
- Czech Police characterizes the actual victim population as likely in the thousands across the EU, although this is a forward-looking estimate rather than confirmed enumeration

## Cooperation Mechanisms Used

- **Joint Investigation Team via Eurojust ([[joint-investigation-team]]).** Bilateral CZ-UA composition. The press release identifies Eurojust as the judicial coordinator and the JIT as the formal cooperation instrument.
- **Search and seizure ([[search-seizure]]).** Ukrainian authorities executed all 19 searches on Ukrainian territory.
- **Electronic evidence collection ([[electronic-evidence]]).** CRM systems, victim personal-data sets, computers, and mobile phones were seized for forensic analysis.
- **Asset freezing ([[asset-freezing]]).** Approximately CZK 33 million in mixed currencies was secured.

## Challenges and Friction Points

The press release does not enumerate friction. Likely structural challenges, based on the broader pattern of CZ-UA call-centre operations, include obtaining timely electronic evidence from Ukrainian territory in wartime conditions, harmonizing victim identification across CZ-UA evidence streams, and converting the announced detentions into Czech or Ukrainian indictments. None of these are asserted by the source; they are listed only as analytical context.

## Lessons Learned

1. **Eurojust-hosted bilateral CZ-UA JITs remain operational for cyber-enabled fraud.** The OCTOPUS instrument suggests that despite Ukraine's wartime conditions and non-EU status, Eurojust-hosted CZ-UA JITs continue to deliver action days, detentions, and seizures on Ukrainian territory.
2. **Operational distinctness must be preserved when announcements are bundled.** OCTOPUS and CONNECT were communicated jointly but are operationally separate (different JIT membership, different fraud type, different action day, different victim pool). Wiki integrity requires recording them as separate operations even when a single press release links them.

## Follow-Up Actions

The press release does not enumerate follow-up actions, indictments, victim-notification programs, or asset-recovery distributions. To be updated as additional public reporting (Eurojust standalone release, Ukrainian Prosecutor General communications, Czech court filings) becomes available.

## Korean Involvement (한국의 참여)

None reported. The press release identifies victims in the Czech Republic and other EU member states. No Korean nationals, Korean agencies, or Korean territory are named.

## Contradictions & Open Questions

- **Number of identified victims vs. estimated total.** The press release asserts 138 confirmed victims with CZK 43 million in damage but estimates the true population in the thousands. This is a forward-looking estimate, not a confirmed figure, and should not be treated as a hard victim count.
- **Start date of the JIT.** The press release does not disclose when the bilateral CZ-UA JIT was established. The duration of the underlying investigation is therefore unknown.
- **Indictment status.** The press release reports detentions but does not indicate whether Czech or Ukrainian formal charges have been filed against the 17 detained persons. Status updates from the Czech Public Prosecutor's Office or the Ukrainian Prosecutor General would clarify.
- **Europol involvement.** The press release does not mention [[europol-ec3|Europol EC3]] participation. Whether OCTOPUS received any operational support from Europol is unstated.
