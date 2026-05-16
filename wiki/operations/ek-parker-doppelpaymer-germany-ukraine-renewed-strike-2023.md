---
type: operation
title: "EK Parker DoppelPaymer Germany-Ukraine Renewed Strike (Sept 2023)"
aliases:
  - "EK Parker Phase 2"
  - "DoppelSpider / DoppelPaymer renewed strike"
  - "LKA NRW Doppel Spider Germany-Ukraine searches Sept 2023"
case_id: CYB-2023-985
period: 1
operation_role: standalone
parent_operation: ""
operation_type: joint-investigation
status: ongoing
enforcement_type:
  - search-seizure
  - asset-freeze
  - evidence-seizure
outcome: partial
timeframe:
  announced: 2023-09-18
  start: 2023-09-11
  end: 2023-09-18
  ongoing: true
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[extortion-ic]]"
target_entity: "DoppelSpider / DoppelPaymer ransomware-extortion group (variants DoppelPaymer, PayOrGrief, Entropy); 600+ victims worldwide including Universitätsklinik Düsseldorf (2020) and Funke Mediengruppe (2020); attributed Indrik Spider / Evil Corp ecosystem overlap per secondary reporting"
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[germany]]"
  - "[[ukraine]]"
  - "[[united-states]]"
jurisdictions:
  - "[[germany]]"
  - "[[ukraine]]"
  - "[[united-states]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[us-secret-service]]"
  - "[[ukraine-police]]"
  - "[[europol-ec3]]"
organizations:
  - "[[germany-bka]]"
  - "[[us-secret-service]]"
  - "[[ukraine-police]]"
  - "[[europol-ec3]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[european-arrest-warrant]]"
legal_basis:
  - "German criminal law §§ 253, 263a StGB (commercial digital extortion, computer fraud) and § 303b StGB (Computersabotage); domestic search-and-seizure powers under StPO"
  - "Ukrainian domestic search-and-seizure procedure as executed by Ukrainian police on Ukraine soil"
  - "Coordination via Europol channels for transnational case management and Most-Wanted publication"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "unspecified (cash and assets seized at prosecutor's request — exact amount not disclosed)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "2 sets of search warrants executed: 1 in Germany (against 45-year-old man in southern Germany alleged to have received ransom proceeds), 1 in Ukraine (against 44-year-old Ukrainian alleged to hold key network role)"
    - "Electronic devices seized at both search locations"
    - "Cash and assets (Gelder und Vermögenswerte) seized at German prosecutor's request, parallel to searches"
    - "No arrests announced in primary release; investigation 'andauert' (ongoing)"
    - "Igor Olegovich Turashev and Igor Garshin (a.k.a. Garschin) remain fugitives; remain on Europol Most-Wanted list per release"
edges:
  - source_actor: "Landeskriminalamt NRW (LKA NRW) — Cybercrime Specialists / EK Parker"
    target_actor: "U.S. Secret Service"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "Landeskriminalamt NRW (LKA NRW) — Cybercrime Specialists / EK Parker"
    target_actor: "[[ukraine-police]]"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "Landeskriminalamt NRW (LKA NRW) — Cybercrime Specialists / EK Parker"
    target_actor: "[[europol-ec3]]"
    cooperation_type: "info_sharing"
    legal_basis: "informal"
    direction: "undirected"
credibility_index: 3.4
source_tier: 1
missing_fields:
  - "specific names of US Secret Service field office leading blockchain investigation"
  - "specific Ukrainian National Police unit that executed Ukraine-side search warrants"
  - "exact monetary value of seized cash and assets"
  - "post-search arrest status of either named suspect"
related_cases:
  - "[[us-v-igor-turashev]]"
related_operations:
  - "[[dridex-operations]]"
  - "[[treasury-evil-corp-tri-lateral-us-uk-au-sanctions-2024]]"
challenges_encountered: []
lessons_learned:
  - "Sub-national German LKAs (Land-level criminal police) can lead transnational ransomware investigations when paired with own-domain Europol coordination and bilateral US Secret Service blockchain partnership."
  - "Search-warrant execution on Ukrainian soil by Ukrainian police, parallel to German searches under coordinated timing, is a viable operational pattern for joint German-Ukrainian ransomware actions — even absent formal JIT structure documented in this release."
source_count: 1
sources:
  - "[[2023-09-18_lka-polizei-nrw_ek-parker-renewed-strike-doppelpaymer-germany-ukraine]]"
created: 2026-05-16
updated: 2026-05-16
---

## Summary

On 18 September 2023, the Pressestelle of the Landeskriminalamt Nordrhein-Westfalen (LKA NRW) announced the execution of a renewed wave of search warrants in Germany and Ukraine against members of the DoppelSpider / DoppelPaymer ransomware-extortion group. The action — the second operational phase of the LKA NRW Ermittlungskommission "Parker" investigation — targeted two specific individuals identified through **joint blockchain investigations by LKA NRW and the U.S. Secret Service**: a 44-year-old Ukrainian alleged to hold a key role inside the network (subject of Ukraine-side search warrant) and a 45-year-old man in southern Germany alleged to have received ransom proceeds (subject of Germany-side search warrant). LKA NRW and ZAC NRW (Zentral- und Ansprechstelle Cybercrime) lead the German investigations, with **Europol coordinating the investigation globally** and hosting the existing Most-Wanted listings of Igor Olegovich Turashev and Igor Garshin — both of whom remain fugitives as of the release date.

DoppelPaymer (alias variants PayOrGrief, Entropy) extorted over 600 victims worldwide between approximately 2017 and 2022, including the catastrophic 2020 Universitätsklinik Düsseldorf hospital attack (linked indirectly to one fatality during a patient transfer) and the 2020 Funke Mediengruppe newspaper-publisher attack. The group overlaps in personnel and infrastructure with the Indrik Spider / Evil Corp ecosystem prosecuted separately in the United States; see [[us-v-igor-turashev]] for the U.S. Dridex case naming the same Turashev.

No arrests were announced in this release. The investigation is described as ongoing ("Die Ermittlungen der EK Parker dauern an").

## Background

The DoppelPaymer ransomware operation — sometimes self-named "Doppel Spider" — emerged in the late 2010s and became one of the most consequential European-targeting ransomware brands during 2019-2022. The variant lineage runs DoppelPaymer → PayOrGrief → Entropy, with the same operators rebranding to evade attribution. Per the LKA NRW release, the **first known attack of this lineage** targeted UK National Health Service / UK healthcare infrastructure in May 2017, with the operation subsequently expanding worldwide.

The LKA NRW Ermittlungskommission "Parker" task force was established to coordinate all German federal cases involving DoppelPaymer and to lead the worldwide investigation jointly with Europol. The German investigations have been ongoing since 2020. In March 2023, EK Parker announced the public identification of Igor Olegovich Turashev and Igor Garshin (a.k.a. Garschin) as principal subjects and placed both on the Europol Most-Wanted list. The September 2023 action announced here is the **second operational phase**: search warrants against two additional persons of interest identified through subsequent blockchain analysis.

## Participating parties

**Lead German bodies (primary release):**
- **Landeskriminalamt Nordrhein-Westfalen (LKA NRW) — Cybercrime-Spezialisten**: lead investigation unit; operates EK Parker task force
- **Zentral- und Ansprechstelle Cybercrime NRW (ZAC NRW)**: prosecutor-side liaison body, attached to Generalstaatsanwaltschaft Köln; co-leads German case coordination
- **Bundeskriminalamt (BKA)** [[germany-bka]]: federal coordination role per German cybercrime architecture (not explicitly named in the 18 Sept release but co-lead of the broader German investigation per the prior 6 March 2023 release referenced)
- **Düsseldorf-area prosecution authorities**: applied for asset-seizure orders parallel to searches

**Foreign LE cooperation explicitly named:**
- **U.S. Secret Service (USSS)** [[us-secret-service]]: joint blockchain investigations with LKA NRW that identified the 44-year-old Ukrainian and 45-year-old German subjects
- **Europol / EC3** [[europol-ec3]]: global investigation coordination; hosts Most-Wanted publication for Turashev and Garshin
- **Ukrainian police** [[ukraine-police]]: described as "Polizeien anderer Länder" — executed search warrants in Ukraine against the 44-year-old Ukrainian suspect

**Jurisdictions of search execution:** Germany (NRW; southern Germany) + Ukraine (against the 44-year-old Ukrainian's residence)

## Legal framework

- **German substantive law:** §§ 253, 263a, 303a, 303b StGB (commercial digital extortion, computer fraud, data alteration, computer sabotage)
- **German procedural law:** StPO §§ 102, 105 (search and seizure); StPO § 111e (asset seizure on prosecutor application)
- **Cross-border coordination channels:** Europol Most-Wanted publication; ZAC NRW federal case-coordination; LKA NRW / U.S. Secret Service informal blockchain cooperation
- **Ukrainian execution basis:** Ukrainian Code of Criminal Procedure search-and-seizure rules; Ukrainian National Police as executing authority

The release does not name a Joint Investigation Team (JIT) formally constituted at Eurojust, nor does it cite Mutual Legal Assistance requests — the cooperation is described in informal-coordination terms with Europol as the central international coordinator.

## Operational timeline

| Date | Event |
|------|-------|
| 2017-05 | First known DoppelPaymer-lineage attack; UK National Health Service / UK healthcare sector |
| 2020 | DoppelPaymer attacks against Universitätsklinik Düsseldorf and Funke Mediengruppe (Germany) |
| 2020-onward | German federal investigations under LKA NRW EK Parker begin |
| 2023-02-28 | LKA NRW executes first wave of EK Parker search warrants in Germany and Ukraine |
| 2023-03-06 | LKA NRW announces public manhunt for Turashev and Garshin; Europol Most-Wanted listing |
| 2023-09 (week of 11 Sept) | Second wave of search warrants executed in Germany (southern Germany resident) and Ukraine (44-year-old Ukrainian residence); electronic devices, cash, and assets seized |
| 2023-09-18 | LKA NRW Pressestelle announces second-phase action |
| 2023-09-18 onward | Investigation continues; no arrests of Turashev or Garshin announced |

## Results and impact

Per the LKA NRW 2023-09-18 release:
- **Searches executed:** 2 sets — Germany (45-year-old man in southern Germany) + Ukraine (44-year-old Ukrainian)
- **Arrests:** 0 reported in primary release (investigation "andauert" — ongoing)
- **Seizures:** Electronic devices at both search locations; cash and asset seizures (Gelder und Vermögenswerte) at German prosecutor's request, parallel to searches; exact monetary value not disclosed in primary release
- **Continuing fugitive status:** Igor Olegovich Turashev and Igor Garshin (a.k.a. Garschin) remain fugitives on Europol Most-Wanted list — release expresses hope that new evidence may yield new leads

## Cooperation mechanisms used

- **Joint blockchain investigation** (LKA NRW + U.S. Secret Service) — identified the two new suspects through cryptocurrency-flow analysis
- **Europol global coordination** — coordinates worldwide investigation against the group; hosts Most-Wanted publications
- **Parallel search execution** (LKA NRW + Ukrainian police) — search warrants executed in Germany and Ukraine in the same operational week
- **Asset seizure** — Düsseldorf-area prosecution authorities obtained court orders for cash/asset seizure parallel to the German search

## Challenges and friction points

- **Fugitive suspects on Russian / hostile-jurisdiction soil**: Turashev and Garshin remain at large despite Europol Most-Wanted listing — typical pattern for senior ransomware operators with Russia-nexus protection
- **Search-warrant execution in Ukraine during ongoing war**: The September 2023 Ukraine-side search was executed under wartime conditions, with Ukrainian police acting on cooperating-jurisdiction request from German colleagues
- **Brand-rebranding evasion**: DoppelPaymer → PayOrGrief → Entropy reflects operator rebranding to evade attribution and infrastructure takedowns — attribution challenges typical of ransomware operator lifecycle

## Lessons learned

- **Sub-national German LKAs (Land-level criminal police) can lead transnational ransomware investigations** when paired with own-domain Europol coordination and bilateral US Secret Service blockchain partnership.
- **Search-warrant execution on Ukrainian soil by Ukrainian police, parallel to German searches under coordinated timing**, is a viable operational pattern for joint German-Ukrainian ransomware actions — even absent formal JIT structure documented in this release.
- **Investigation continuity across multiple operational phases**: EK Parker shows how a single task force can deliver sequential strikes against the same network over months/years, with each phase building on the previous.

## Korean involvement (한국의 참여)

None reported in the LKA NRW 18 September 2023 press release. South Korean victims of DoppelPaymer have been reported in the secondary literature but are not addressed in this primary IC release.

## Contradictions & open questions

- **Number of suspects executed against in Phase 2**: Primary release describes two specific subjects (44-year-old Ukrainian + 45-year-old German). It is unclear whether additional, unnamed search warrants were also executed against other persons.
- **Post-search arrest status**: No subsequent LKA NRW release at time of ingest confirms whether either of the two new subjects was formally arrested or only had their residence searched.
- **U.S. Secret Service field office and exact unit**: The release names "U.S. Secret Service" generically; the specific field office leading the blockchain partnership is not disclosed.
- **Ukrainian National Police unit**: The release refers to "Polizeien anderer Länder" — the specific Ukrainian National Police Cyberpolice unit (Департамент кіберполіції) that executed the Ukrainian search is not named.
- **Relationship to U.S. Dridex / Evil Corp case (Turashev co-defendant)**: Igor Olegovich Turashev is also a defendant in [[us-v-igor-turashev]] / Dridex case — the LKA NRW release does not address the US-DOJ-side proceedings or any coordination with the Western District of Pennsylvania prosecution.
- **Joint Investigation Team status**: Release does not state whether a formal Eurojust-JIT was established between Germany and Ukraine for the cross-border searches, or whether the cooperation operated on ad-hoc / Europol-channel basis.

## Sources

- [[2023-09-18_lka-polizei-nrw_ek-parker-renewed-strike-doppelpaymer-germany-ukraine]] — LKA NRW Pressestelle release (primary, German, public)
