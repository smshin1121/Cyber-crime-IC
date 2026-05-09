---
type: operation
title: "KNPA KMSAuto Clipper Malware — Lithuania-Georgia-Korea Three-State Extradition (2020–2025)"
title_ko: "가상자산 편취 악성프로그램(KMSAuto) 유포 외국인 해커 인터폴 수배·송환 (한국·리투아니아·조지아 공조)"
aliases:
  - "KMSAuto memory-hacking clipper extradition"
  - "KNPA Lithuanian KMSAuto hacker extradition 2025"
  - "Korea-Lithuania-Georgia crypto clipper extradition"
case_id: CYB-2025-122
period: 3
operation_type: joint-investigation
status: completed
enforcement_type:
  - extradition
  - arrest
  - search-seizure
outcome: success
timeframe:
  announced: 2025-12-29
  start: 2020-08
  end: 2025-12
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
target_entity: "29-year-old Lithuanian national 'A' accused of distributing a memory-hacking clipper malware bundled inside cracked Microsoft Windows activation tooling 'KMSAuto', who diverted cryptocurrency receive-addresses on infected hosts to attacker-controlled wallets across 234 countries"
lead_agency: "[[knpa]]"
coordinating_body: "[[knpa]]"
participating_countries:
  - "[[south-korea]]"
  - "[[lithuania]]"
  - "[[georgia]]"
participating_agencies:
  - "[[knpa]]"
  - "[[knpa-cyber-bureau]]"
  - "[[ministry-of-justice-korea]]"
  - "[[supreme-prosecutors-office-korea]]"
  - "[[lithuania-police]]"
  - "[[interpol]]"
legal_basis:
  - "INTERPOL Red Notice (인터폴 적색 수배)"
  - "Korea–Lithuania mutual legal assistance via Korean MOJ and Supreme Prosecutors' Office (형사사법공조)"
  - "Korea–Georgia extradition request (범죄인 인도 요청)"
  - "Korean domestic criminal process — KNPA as requesting state"
mechanisms_used:
  - "[[extradition]]"
  - "[[mutual-legal-assistance]]"
  - "[[informal-cooperation]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 Lithuanian-national suspect (29, identified only as 'A') extradited from Georgia to Korea and remanded into custody"
    - "Joint search of suspect's residence in Lithuania (December 2024) executed with Lithuanian Police; 22 items seized including phone and laptop"
    - "INTERPOL Red Notice issued for arrest at international border (executed at Georgia entry, April 2025)"
    - "2.8 million KMSAuto-bundled clipper-malware distributions worldwide between 2020-04-08 and 2023-01-06"
    - "3,100 cryptocurrency addresses drained across 8,400 transactions for ~₩1.7 billion (~USD 1.18M); 14 distinct crypto assets affected (BTC, LTC, ETH, XRP … DASH per source diagram)"
    - "Victims in 234 countries by ISO country code; 8 confirmed Korean victims with ~₩16M aggregate losses"
    - "6 third-country jurisdictions and 6 foreign cryptocurrency-related companies engaged in the trace-and-attribution phase"
    - "Total elapsed time from initial case opening (2020-08) to suspect extradition (2025-12): 5 years 4 months"
edges:
  - source_actor: knpa
    target_actor: lithuania-police
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: ministry-of-justice-korea
    target_actor: lithuania
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
  - source_actor: knpa
    target_actor: interpol
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: ministry-of-justice-korea
    target_actor: georgia
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: supreme-prosecutors-office-korea
    target_actor: knpa
    cooperation_type: joint_investigation
    legal_basis: domestic_task_force
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "indictments (post-extradition prosecution outcomes pending)"
  - "cryptocurrency_seized (no asset-recovery figure stated in the cited release)"
  - "exact identities of the 6 third-country jurisdictions and 6 foreign exchanges named only as a count in the release"
related_cases:

related_operations:
  - "[[korea-cambodia-philippines-73-extradition-2026]]"
  - "[[knpa-breaking-chains-2nd-international-operation-meeting-2026]]"
challenges_encountered:

lessons_learned:
  - "The 2025-12-29 KNPA release is the first wiki-recorded Korean operation that explicitly chains INTERPOL Red Notice, formal MLA via Korean MOJ + SPO, and a Georgia-side extradition request as the same end-to-end cooperation flow with Lithuania as the joint-search jurisdiction. This three-state pattern (host → transit/arrest → requesting) is a discrete cooperation topology to track separately from the Korea-Cambodia/Philippines bilateral extradition pattern in the wiki."
  - "Public Korean-press disclosure that 'A' was arrested in Georgia on entry from Lithuania (April 2025) materially demonstrates that an active INTERPOL Red Notice can be operationalised at a non-EU CIS-region border once the suspect transits out of his home jurisdiction; the host-state Lithuanian search (December 2024) generated the evidentiary basis for the Red Notice rather than for a Lithuanian prosecution."
  - "The clipper/memory-hacking malware family bundled with cracked Microsoft Windows activation tooling is documented in this operation as a specific cyber-enabled monetisation vector for cryptocurrency theft — distinct from ransomware and from forum-based wallet phishing. Future Korean clipper cases should be cross-referenced to this baseline."
source_count: 1
sources:
  - "[[2025-12-29_korea-kr_knpa-kmsauto-lithuanian-hacker-georgia-extradition]]"
created: 2026-05-09
updated: 2026-05-09
---

## Summary

On 2025-12-29 the [[knpa|Korean National Police Agency]] National Office of Investigation (국가수사본부) announced the extradition into [[south-korea|Korea]] of a 29-year-old [[lithuania|Lithuanian]] national identified only as 'A', accused of distributing a memory-hacking clipper malware bundled inside cracked Microsoft Windows activation tooling 'KMSAuto'. The malware silently rewrote cryptocurrency receive-addresses at transmission time on infected hosts, redirecting funds to attacker-controlled wallets. Across 2020-04-08 to 2023-01-06 the campaign distributed 2.8 million copies of the bundle worldwide, drained 3,100 distinct cryptocurrency addresses across 8,400 transactions for ~₩1.7 billion (~USD 1.18M), and reached victims in 234 countries (ISO basis), including 8 confirmed Korean victims with ~₩16M aggregate losses.

The cooperation chain is named explicitly in the KNPA release as: KNPA / Korean MOJ / Korean SPO ↔ Lithuanian MOJ + [[lithuania-police|Lithuanian Police]] (joint search of A's residence, December 2024, 22 items seized) → [[interpol|INTERPOL]] Red Notice → [[georgia|Georgian]] Police (arrest April 2025 on entry from Lithuania) → Korean [[extradition|extradition]] request to Georgia → custody in Korea late 2025. Total elapsed time from initial case opening (August 2020) to extradition was 5 years 4 months.

## Background

A single bitcoin-misdirection victim report in August 2020 ('비트코인 1개를 송금했는데 엉뚱한 주소로 송금되어 잃어버렸다', i.e. one bitcoin then valued at ~₩12 million sent to an unintended address) opened the case at the [[knpa-cyber-bureau|KNPA Cyber Investigation function]]. Forensic examination of the victim's host disclosed a 'memory-hacking' clipper that automatically replaced the destination cryptocurrency address with an attacker-controlled address at the moment of transmission. The clipper had been delivered as a payload bundled with KMSAuto, a Microsoft Windows volume-licensing-bypass utility frequently downloaded from non-official channels by users seeking to avoid Windows activation. KNPA's release explicitly attributes victim exposure to the use of non-genuine software ('정품 소프트웨어를 사용하지 않았기 때문에 피해가 발생').

Through follow-the-money work across domestic Korean cryptocurrency exchanges plus 6 third-country jurisdictions and 6 foreign cryptocurrency-related companies, KNPA traced the proceeds, expanded the Korean victim count from 1 to 8 (adding 7 victims with Korean losses totalling ~₩16M), reconstructed the full distribution timeline, and identified A as a Lithuanian-resident natural person.

## Participating Parties

| Role | Parties |
|---|---|
| Lead requesting authority | [[knpa\|KNPA National Office of Investigation (국가수사본부)]] — 사이버테러대응과 |
| Korean MLA conduits | [[ministry-of-justice-korea\|Ministry of Justice Korea]], [[supreme-prosecutors-office-korea\|Supreme Prosecutors' Office Korea]] |
| Host-state joint-search authorities | Lithuanian Ministry of Justice and [[lithuania-police\|Lithuanian Police]] |
| International notice channel | [[interpol\|INTERPOL]] (Red Notice) |
| Arresting authority | Georgian Police (state agency in [[georgia\|Georgia]]) |
| Source-backed participating countries | [[south-korea\|South Korea]] (requesting), [[lithuania\|Lithuania]] (host / joint search), [[georgia\|Georgia]] (arrest / surrendering state) |

## Legal Framework

The KNPA release names the cooperation backbone as a layered stack:

1. Korea–Lithuania **mutual legal assistance** (형사사법공조), routed through Korean Ministry of Justice and Supreme Prosecutors' Office, which authorised the joint search-and-seizure of A's Lithuanian residence in December 2024 and the seizure of 22 items including phone and laptop;
2. **INTERPOL Red Notice** ('인터폴 적색 수배') issued at KNPA request after Korea concluded that the evidentiary basis was sufficient to prosecute A in Korea;
3. **Korea–Georgia extradition request** ('범죄인 인도 요청') filed once A was arrested by Georgian Police on entry from Lithuania in April 2025, executed jointly by Korean police, Korean MOJ, and Korean SPO.

The release does not name a specific bilateral MLAT or extradition treaty; the cooperation is described as 'KNPA + Korean MOJ + Korean SPO + Lithuanian MOJ + Lithuanian Police + Georgian Police + INTERPOL' working in 'tight cooperation' (긴밀한 공조 / 긴밀히 협력).

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2020-04-08 | Earliest dated KMSAuto-bundled clipper distributions begin (per attached KNPA diagram) | KNPA 2025-12-29 |
| 2020-08 | Victim report of misdirected 1 BTC (~₩12M at the time); KNPA opens case | KNPA 2025-12-29 |
| 2023-01-06 | Latest dated KMSAuto-bundled clipper distributions in the campaign window | KNPA 2025-12-29 |
| 2024 (year) | KNPA enters one-year coordination cycle with Lithuanian MOJ and Lithuanian Police on coercive-investigation strategy | KNPA 2025-12-29 |
| 2024-12 (early) | Joint Korea-Lithuania search-and-seizure of A's residence in Lithuania; 22 items including phone and laptop seized | KNPA 2025-12-29 |
| 2025-04 | Georgian Police arrest A on entry from Lithuania to Georgia, on the active INTERPOL Red Notice | KNPA 2025-12-29 |
| 2025 (Q2–Q4) | Korea–Georgia extradition processing (KNPA + Korean MOJ + Korean SPO) | KNPA 2025-12-29 |
| 2025-12-28 09:00 | Online/broadcast embargo lift on the KNPA press release | KNPA 2025-12-29 |
| 2025-12-29 | Print-edition publication of the KNPA press release; A in Korean custody on remand for flight risk and evidence-destruction risk | KNPA 2025-12-29 |

## Results and Impact

| Item | Value |
|---|---|
| Suspects extradited | 1 (Lithuanian national, 29) |
| Joint-search items seized in Lithuania | 22 (incl. phone, laptop) |
| Total KMSAuto-bundled distributions worldwide | 2,800,000 |
| Distinct cryptocurrency addresses drained | 3,100 |
| Theft-event count | 8,400 |
| Aggregate stolen value | ~₩1,700,000,000 (~USD 1.18M) |
| Distinct cryptocurrency assets affected | 14 |
| Countries with victims (ISO basis) | 234 |
| Confirmed Korean victims | 8 |
| Korean victim aggregate losses | ~₩16,000,000 |
| Third-country jurisdictions traced | 6 |
| Foreign cryptocurrency-related companies engaged for tracing | 6 |
| Elapsed time, case opening to extradition | 5 years 4 months |

## Cooperation Mechanisms Used

- **Mutual legal assistance (MLA / 형사사법공조)** between Korea (MOJ + SPO + KNPA) and Lithuania (MOJ + Police) for the December 2024 joint search-and-seizure of A's residence — see [[mutual-legal-assistance]] and [[mlat-process|MLAT process]] for the general mechanism.
- **INTERPOL Red Notice** ([[interpol|INTERPOL]]) issued at KNPA request as the international border-control instrument that produced A's arrest by Georgian Police in April 2025.
- **State-to-state extradition request** from Korea to Georgia for surrender of A — see [[extradition|extradition mechanism]].
- **Operational liaison** between KNPA and Lithuanian Police throughout 2024 prior to the formal MLA execution — captured under [[informal-cooperation|informal cooperation]] as the pre-MLA coordination channel that calibrated the December 2024 search.
- **Public-private cooperation with cryptocurrency exchanges and 6 foreign crypto-related companies** to trace stolen funds and confirm additional Korean victims (treated here as part of the financial-investigation phase rather than as a separate listed mechanism in the cited release).

## Challenges and Friction Points

- The KNPA release does not state a recovery figure for the ~₩1.7 billion stolen value; whether seized assets in Lithuania (December 2024) included any cryptocurrency-relevant material beyond device evidence is not specified.
- The release names 6 third-country jurisdictions and 6 foreign cryptocurrency-related companies as part of the tracing effort but does not enumerate them; this limits the ability to attribute specific multilateral cooperation flows on the financial-investigation side.
- The full crime-period (2020-04-08 to 2023-01-06) is closed-ended in the source diagram but A's arrest in Georgia did not occur until April 2025 — the gap reflects host-state coordination cycle (one year of 2024 negotiation plus December 2024 search) rather than passive delay.

## Lessons Learned

- The Korea–Lithuania–Georgia three-state pattern documented here (host of suspect → transit/arrest jurisdiction → requesting state) is operationally distinct from the Korea-Cambodia/Philippines bilateral extradition pattern previously recorded in the wiki: Lithuania never prosecutes A; its role is exclusively joint-search and evidence-base construction in support of a Korean prosecution. Wiki users tracking Korean-led extradition mechanics should treat this as a separate topology category.
- INTERPOL Red Notices remain operationally effective at non-EU CIS-region borders even after a multi-year fugitive period, when the requesting state has secured prior MLA-based search evidence in the suspect's host state and the suspect transits out of his home jurisdiction.
- Clipper / memory-hacking malware distributed via cracked Microsoft Windows activation tooling (KMSAuto family) is here documented as a specific cyber-enabled monetisation vector for cryptocurrency theft, distinct from ransomware and from wallet-phishing forums; future Korean clipper cases should be cross-referenced to this 2020–2025 baseline.

## Follow-Up Actions

- Korean prosecution-phase outcomes (indictment date, charges filed, court of first instance, sentencing where applicable) are pending as of the cited 2025-12-29 release; this operation page should be revisited when the Korean indictment becomes public.
- KNPA's release notes that the agency is investigating possible accomplices ('공범 추적 중' is reported in same-day Korean press coverage of the briefing); a follow-up release naming additional suspects, additional jurisdictions, or additional crypto recovery should be ingested as it becomes available.

## Korean Involvement (한국의 참여)

This operation is Korea-led: the requesting state is Korea, the lead agency is the [[knpa|KNPA]] National Office of Investigation (국가수사본부), and the responsible operational unit is 사이버테러대응과 (Cyber Terror Response Division) within 수사국. Korean Ministry of Justice and the Supreme Prosecutors' Office are explicitly named as the formal-MLA conduits to Lithuanian counterparts, and Korean police, MOJ, and SPO are jointly named as the institutions that filed and processed the Korea-to-Georgia extradition request. The Korean victim cohort (8 persons, ~₩16M aggregate) is small relative to the global scale (234 countries, ~₩1.7B aggregate), but Korean jurisdiction is anchored both by the Korean victim count and by the original 2020-08 victim report that opened the case. KNPA Cyber Investigation Senior Officer 박우현 (Park Woo-hyun) is named as the public spokesperson, and KNPA frames the operation as a model for transnational cooperation in cases where a foreign national victimises Koreans from outside Korea ('초국가적 협업으로 끝까지 추적').

## Contradictions & Open Questions

- The KNPA release reports both 8,400 theft events drained from 3,100 cryptocurrency addresses and a stolen value of ~₩1.7 billion; some same-day Korean-press coverage rounds the address count or transaction count differently — the KNPA PDF figures (3,100 addresses, 8,400 events, ₩1.7B) are treated as the authoritative numbers in this wiki.
- The 6 third-country jurisdictions traced for crypto follow-the-money are not enumerated in the cited release; this leaves a documented but unattributed multilateral cooperation surface.
- Same-day press coverage references investigation of possible accomplices ('공범 추적 중') beyond the cited release; the original KNPA PDF does not name additional suspects.
- The release does not state whether any portion of the ~₩1.7 billion stolen value has been recovered or frozen, in Korea or abroad.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-12-29_korea-kr_knpa-kmsauto-lithuanian-hacker-georgia-extradition\|가상자산 편취 악성프로그램(KMSAuto) 유포 외국인 해커 인터폴 수배 후 한국 송환·구속]] | 경찰청 국가수사본부 (KNPA, via Korea.kr 정책브리핑) | 2025-12-29 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156737083 |
