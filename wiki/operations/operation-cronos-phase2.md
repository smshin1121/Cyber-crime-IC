---
type: operation
title: "Operation Cronos — Phase 2 (LockBit Administrator Indictment & Sanctions)"
title_ko: "오퍼레이션 크로노스 — 페이즈 2 (LockBit 운영자 기소·제재)"
aliases:
  - "Cronos Phase 2"
  - "LockBit Khoroshev indictment"
  - "Khoroshev LockBitSupp sanctions"
case_id: CYB-2024-201
period: 2
operation_role: phase
parent_operation: "[[operation-cronos-phase1]]"
operation_type: indictment
status: completed
enforcement_type:
  - indictment
  - sanctions
  - asset-freeze
  - reward-offer
outcome: success
timeframe:
  announced: 2024-05-07
  start: 2024-05-07
  end: 2024-05-07
  ongoing: false
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
target_entity: "Dmitry Yuryevich Khoroshev (a.k.a. LockBitSupp / LockBit / putinkrab) — developer and administrator of the LockBit ransomware-as-a-service from September 2019 through May 2024; the broader LockBit ransomware group infrastructure"
lead_agency: "[[us-doj]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[uk-nca]]"
  - "[[australia-afp]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[uk-nca]]"
  - "[[australia-afp]]"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[asset-freezing]]"
legal_basis:
  - "26-count indictment in the District of New Jersey alleging conspiracy to commit fraud and extortion (max aggregate 185 years)"
  - "US Department of Treasury (OFAC) cyber-related sanctions designation, 2024-05-07"
  - "US Department of State reward offer up to USD 10 million for information leading to apprehension and/or conviction"
  - "UK Office of Financial Sanctions Implementation (OFSI) parallel sanctions"
  - "Australia Department of Foreign Affairs and Trade (DFAT) parallel sanctions"
results:
  arrests: 0
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "26-count federal indictment unsealed in the District of New Jersey against Dmitry Yuryevich Khoroshev (a.k.a. LockBitSupp)"
    - "Concurrent OFAC sanctions designation of Khoroshev for cyber-related ransomware activity"
    - "USD 10 million State Department reward offered for information leading to Khoroshev's apprehension or conviction"
    - "Concurrent UK OFSI and Australia DFAT/AFP sanctions actions against Khoroshev"
    - "Five other LockBit affiliates previously charged; two in custody awaiting trial as of the 2024-05-07 announcement"
    - "LockBit alleged to have attacked more than 2,500 victims in at least 120 countries, including 1,800 US victims; USD 500 million+ in ransom proceeds; billions of dollars in broader losses; Khoroshev personally receiving at least USD 100 million through 20% developer share"
edges:
  - source_actor: "us-doj"
    target_actor: "uk-nca"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "us-doj"
    target_actor: "australia-afp"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "uk-nca"
    target_actor: "australia-afp"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields: []
related_cases: []
related_operations:
  - "[[operation-cronos-phase1]]"
  - "[[operation-cronos-phase3]]"
challenges_encountered: []
lessons_learned:
  - "Phase 2 demonstrates the US-UK-Australia three-jurisdiction concurrent-sanctions pattern (Treasury OFAC + UK OFSI + Australia DFAT) layered on top of a US criminal indictment, with international policing partners (FBI, NCA, AFP) named as cooperators. This is a recurring shape for major ransomware-as-a-service attribution waves and warrants tracking as a discrete IC mechanism class."
  - "The Phase 2 wave is the named-suspect attribution layer between Phase 1 (infrastructure disruption, February 2024) and Phase 3 (arrests + further sanctions, October 2024). The umbrella 「Operation Cronos」 is therefore correctly modelled as a multi-phase cycle in which sanctions, indictment, infrastructure seizure, and arrests are deployed in sequence rather than simultaneously."
source_count: 1
sources:
  - "[[2024-05-07_justice-gov-dnj_us-charges-russian-national-developing-operating-lockbit-ransomware]]"
summary: "On 2024-05-07 the US Justice Department (District of New Jersey) unsealed a 26-count indictment against Dmitry Yuryevich Khoroshev (a.k.a. LockBitSupp) — the alleged developer and administrator of LockBit since September 2019. Concurrently, the US Treasury (OFAC) sanctioned Khoroshev, the US State Department offered a USD 10 million reward, and parallel sanctions actions were taken by the UK Office of Financial Sanctions Implementation (OFSI) and Australia's Department of Foreign Affairs and Trade (DFAT). LockBit is described in the indictment as having attacked over 2,500 victims in at least 120 countries (1,800 in the US), with USD 500 million+ in ransom proceeds and Khoroshev personally receiving at least USD 100 million through his 20% developer share."
created: 2026-05-08
updated: 2026-05-08
---
## Summary

On 2024-05-07 the United States Justice Department, through the US Attorney's Office for the District of New Jersey, unsealed a 26-count federal indictment against [[ransomware-ic|Dmitry Yuryevich Khoroshev]] (alias LockBitSupp, LockBit, and putinkrab; 31, of Voronezh, Russia) — the alleged developer and administrator of the [[operation-cronos-phase1|LockBit]] ransomware group from approximately September 2019 through May 2024. Concurrent international actions included a US Treasury (OFAC) sanctions designation, a US Department of State reward offer of up to USD 10 million for information leading to Khoroshev's apprehension or conviction, and parallel sanctions by the UK's Office of Financial Sanctions Implementation (OFSI) and Australia's Department of Foreign Affairs and Trade (DFAT).

This wave is the named-suspect attribution and prosecution layer of the multi-phase [[operation-cronos-phase1|Operation Cronos]], filling the gap between the February 2024 NCA-led infrastructure disruption ([[operation-cronos-phase1|Phase 1]]) and the October 2024 NCA-led arrests and additional sanctions wave ([[operation-cronos-phase3|Phase 3]]).

## Background

LockBit operated under the ransomware-as-a-service (RaaS) model, with Khoroshev allegedly designing and maintaining the LockBit ransomware code, recruiting affiliates to deploy it, and operating the infrastructure including a control panel for affiliates and a public-facing data leak site. According to the indictment, Khoroshev typically received a 20% developer share of each ransom payment, with the responsible affiliate receiving the remaining 80%. During the scheme, Khoroshev alone allegedly received at least USD 100 million in cryptocurrency disbursements through his developer shares of LockBit ransom payments. LockBit attacked more than 2,500 victims in at least 120 countries — including 1,800 victims in the United States — with at least USD 500 million in ransom proceeds and billions of dollars in broader losses to victims spanning hospitals, schools, critical infrastructure, multinational corporations, small businesses, and government and law-enforcement agencies.

## Participating Parties

| Role | Parties |
|---|---|
| US lead investigator and charging authority | [[fbi\|FBI]] (Newark Field Office); US Attorney's Office for the District of New Jersey; [[us-doj\|US DOJ]] Criminal Division (CCIPS, Computer Crime and Intellectual Property Section) |
| US sanctions authority | US Department of Treasury (Office of Foreign Assets Control / OFAC) |
| US reward authority | US Department of State |
| UK cooperation | [[uk-nca\|National Crime Agency (NCA)]] Cyber Division; UK HM Treasury Office of Financial Sanctions Implementation (OFSI) |
| Australian cooperation | [[australia-afp\|Australian Federal Police (AFP)]]; Australian Department of Foreign Affairs and Trade (DFAT) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2024-02-19 / 2024-02-20 | Phase 1 — NCA-led infrastructure disruption announced | (See [[operation-cronos-phase1]]) |
| 2024-05-07 | Phase 2 — DOJ unseals 26-count indictment; concurrent OFAC sanctions; US/UK/Australia parallel sanctions; State Department USD 10M reward | DOJ DNJ 2024-05-07 |
| 2024-10-01 | Phase 3 — NCA arrests and additional sanctions wave | (See [[operation-cronos-phase3]]) |

## Results and Impact

- 26-count federal indictment unsealed against Dmitry Yuryevich Khoroshev in the District of New Jersey (max aggregate penalty 185 years in prison).
- US Treasury OFAC sanctions designation against Khoroshev for cyber-related ransomware activity.
- US Department of State reward offer up to USD 10 million for information leading to apprehension or conviction.
- UK OFSI and Australia DFAT parallel sanctions designations.
- Five other LockBit affiliates previously charged in the multi-phase operation; two in custody awaiting trial as of the 2024-05-07 announcement.
- LockBit cohort scale: 2,500+ victims in 120+ countries; 1,800 US victims; USD 500 million+ in ransom proceeds; Khoroshev personally received USD 100 million+ through 20% developer share.

## Cooperation Mechanisms Used

The cited release describes US-UK-Australia three-jurisdiction concurrent-sanctions cooperation layered on top of a US criminal indictment. The release does not enumerate a specific MLAT instrument or a Joint Investigation Team (JIT). The cooperation pattern is instead a parallel-tracks model: each jurisdiction executes its own sanctions or charging instrument under its domestic legal authority, coordinated in timing through informal information-sharing channels among the FBI, NCA, AFP, OFAC, OFSI, and DFAT.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited tier-1 DOJ DNJ release among the cooperating jurisdictions or among the LockBit attribution actors. The case is recorded in the wiki for the multi-phase Operation Cronos enrichment and the verbatim US-UK-Australia three-jurisdiction concurrent-sanctions pattern. LockBit attribution context is relevant to the broader Korean ransomware IC posture tracked elsewhere in this wiki, given LockBit's scale (2,500+ victims in 120+ countries) and the recurring Korean participation in INTERPOL ransomware-coordination operations.

## Contradictions & Open Questions

- Khoroshev was, as of the 2024-05-07 announcement, at large in Russia; the indictment is one of the rare US ransomware indictments that names a Russian-national administrator, but Khoroshev's apprehension would require his exit from Russian protection.
- The cited DOJ DNJ release names "five other LockBit affiliates" previously charged, with "two in custody awaiting trial". Their identity, charges, and case progressions are tracked in separate wiki records and case pages where available.
- Treasury OFAC and State Department reward documents are referenced through the DOJ DNJ release; standalone source pages for those documents may be added separately when their independent fact content (sanctions text, reward terms) is materially distinct from the DOJ DNJ release.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2024-05-07_justice-gov-dnj_us-charges-russian-national-developing-operating-lockbit-ransomware\|U.S. Charges Russian National with Developing and Operating Lockbit Ransomware]] | US DOJ DNJ / USAO-NJ | 2024-05-07 | https://www.justice.gov/usao-nj/pr/us-charges-russian-national-developing-and-operating-lockbit-ransomware |
