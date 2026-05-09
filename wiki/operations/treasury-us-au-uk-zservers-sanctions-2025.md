---
type: operation
title: "Trilateral Sanctions on Zservers Russian Bulletproof Hosting Provider (2025)"
aliases:
  - "Zservers sanctions"
  - "Treasury SB-0018"
  - "US-AU-UK Zservers BPH sanctions 2025"
  - "Zservers / XHOST trilateral designations"
case_id: CYB-2025-114
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-02-11
  start: 2025-02-11
  end: 2025-02-11
  ongoing: false
crime_types:
  - "[[ransomware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "Zservers, a Barnaul, Russia-headquartered bulletproof hosting (BPH) services provider that leased IP addresses and infrastructure to LockBit ransomware affiliates, plus two Russian-national administrators (Alexander Igorevich Mishin and Aleksandr Sergeyevich Bolshakov). The UK FCDO supplementally designated, the same day, XHOST Internet Solutions LP — a UK-registered front company tied to Zservers — and four additional employees: Ilya Sidorov, Dmitriy Bolshakov, Igor Odintsov, and Vladimir Ananev. The LockBit nexus is established through (i) a 2022 Canadian law-enforcement search of a LockBit affiliate that recovered a laptop running a LockBit programming interface over a Zservers-subleased IP, (ii) a 2022 Russian-cybercriminal IP purchase from Zservers almost certainly used as LockBit chat-server infrastructure, and (iii) a 2023 lease of Zservers infrastructure (including a Russian IP address) to a LockBit affiliate."
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[fbi]]"
  - "[[us-doj]]"
legal_basis:
  - "Executive Order 13694 (2015), as further amended by Executive Order 14144 (2025)"
mechanisms_used:
  - "[[asset-freezing]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 entity designated by OFAC: Zservers"
    - "2 individuals designated by OFAC: Alexander Igorevich Mishin, Aleksandr Sergeyevich Bolshakov (both Russian nationals, Zservers administrators)"
    - "1 additional entity designated by UK FCDO: XHOST Internet Solutions LP (UK-registered front company)"
    - "4 additional individuals designated by UK FCDO: Ilya Sidorov, Dmitriy Bolshakov, Igor Odintsov, Vladimir Ananev"
    - "Coordinated trilateral designations by U.S. (OFAC), Australia (DFAT), and UK (FCDO) issued on the same day"
edges:
  - source_actor: us-treasury
    target_actor: fbi
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: us-treasury
    target_actor: us-doj
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: us-treasury
    target_actor: australia-dfat
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: us-treasury
    target_actor: uk-fcdo
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: canadian-law-enforcement-2022
    target_actor: us-treasury
    cooperation_type: evidence_transfer
    legal_basis: unknown
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific SDN-list identifiers (DOB, passport, address) for Mishin and Bolshakov beyond the press-release narrative"
  - "specific Canadian law-enforcement agency that conducted the 2022 search (release says 'Canadian law enforcement' generically)"
  - "specific MLAT or Five Eyes information-sharing instrument used for trilateral coordination"
  - "specific FCDO sanctions notice / OFSI reference number for XHOST and the four UK-side individuals"
related_cases:
  []
related_operations:
  - "[[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025]]"
  - "[[operation-cronos-phase1]]"
  - "[[operation-cronos-phase3]]"
  - "[[treasury-aeza-group-bulletproof-hosting-sanctions-2025]]"
challenges_encountered:
  []
lessons_learned:
  - "BPH providers are a distinct, designable layer of the ransomware supply chain — sanctioning the infrastructure operator (rather than only the ransomware affiliates) attacks the dependency that the affiliates themselves cannot quickly replace."
  - "Russian BPH operators routinely use UK and other Western shell companies (here, XHOST Internet Solutions LP) as front entities; the UK FCDO supplemental designations show that trilateral coordination can also reach the Western-registered fronts that pure OFAC action would not capture."
  - "Operator-level evidence (the 2023 IP-rotation incident in response to the Lebanese-company complaint) is the kind of 'service desk' record that demonstrates knowing facilitation rather than mere passive hosting — a useful evidentiary template for designating future BPH providers."
  - "This action is highly likely the opening entry in a deliberate 2025 trilateral track against Russian BPH: the same template (US Treasury + Australia DFAT + UK FCDO, E.O. 13694/14144, BPH-as-target) recurs in the Aeza Group designations later in 2025 and in the Media Land / Hypercore designations in November 2025 (SB-0319), constituting a 9-month sustained-pressure chain — the wiki's first record of this chain pattern as a track."
source_count: 1
sources:
  - "[[2025-02-11_treasury_us-au-uk-zservers-sanctions-lockbit-ransomware]]"
created: 2026-05-09
updated: 2026-05-09
---
## Summary

On **2025-02-11**, the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC), Australia's Department of Foreign Affairs and Trade (DFAT), and the United Kingdom's Foreign, Commonwealth and Development Office (FCDO) jointly designated **Zservers**, a Barnaul, Russia-headquartered bulletproof hosting (BPH) provider, for materially supporting [[ransomware-ic|LockBit ransomware]] activity. OFAC concurrently designated Zservers' two Russian-national administrators, Alexander Igorevich Mishin and Aleksandr Sergeyevich Bolshakov, under [[asset-freezing|E.O. 13694 as further amended by E.O. 14144]]. The UK FCDO supplementally designated, the same day, **XHOST Internet Solutions LP** (a UK-registered front company tied to Zservers) and four additional employees (Ilya Sidorov, Dmitriy Bolshakov, Igor Odintsov, Vladimir Ananev). It is *almost certainly* the opening entry in a sustained 2025 US-AU-UK trilateral track against Russian BPH infrastructure.

## Background

LockBit, a Russia-based ransomware-as-a-service operation, is — per the Treasury release — "one of the most deployed ransomware variants" and was responsible for the November 2023 attack against the Industrial Commercial Bank of China U.S. broker-dealer. The post-[[operation-cronos-phase1|Operation Cronos Phase 1]] (Feb 2024) and [[operation-cronos-phase3|Operation Cronos Phase 3]] (May 2024) takedowns degraded LockBit's leak-site and admin infrastructure but did not extinguish the affiliate ecosystem; affiliate operations continued to require *bulletproof hosting* — service providers that, by design, refuse abuse-complaint takedowns and frustrate law-enforcement disruption.

The Treasury action is *highly likely* designed to attack the BPH supply layer rather than affiliates directly. Treasury frames the release as a sequel to the 2024 trilateral cyber sanctions against Alexander Ermakov and members of the Evil Corp ransomware group, signaling that the US-AU-UK cyber-sanctions cell continues to coordinate.

## Participating Parties

- **United States** — OFAC (lead designator); DOJ and FBI provided supporting investigative work per the release.
- **United Kingdom** — FCDO designated Zservers + Mishin + Bolshakov in parallel and *additionally* designated XHOST Internet Solutions LP plus four further UK-side individuals not listed by OFAC.
- **Australia** — DFAT designated under its autonomous cyber-sanctions regime.
- **Russia** — host jurisdiction of Zservers and of all six designated natural persons (two on the OFAC side, four further on the UK side); cooperation by Russian authorities is *almost certainly not* present given the post-2022 collapse of Russia–Western law-enforcement channels.

> [!note] Canadian role
> The press release credits "Canadian law enforcement" with the 2022 search of a LockBit affiliate that produced the laptop-on-Zservers-IP evidence. The specific Canadian agency is not named in the release. This is the only non-trilateral foreign cooperation explicitly cited.

## Legal Framework

- **Designation authority (US):** Executive Order 13694 (2015) — "Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities" — *as further amended by* Executive Order 14144 (2025). Zservers, Mishin, and Bolshakov are all designated under this authority.
- **Designation authority (UK):** UK Cyber (Sanctions) Regulations 2020 — applied via FCDO listing the same day; *highly likely* basis given the standard FCDO trilateral template, though the Treasury press release itself does not enumerate the UK statute.
- **Designation authority (Australia):** Autonomous Sanctions Act 2011 / Autonomous Sanctions (Designated Persons and Entities and Declared Persons — Thematic Sanctions) Instrument 2021 — *highly likely* basis for the DFAT action under the same trilateral template.

The action does **not** rely on extradition, MLAT, or [[mutual-legal-assistance|MLA]]; it is a pure economic-sanctions instrument that operates without Russian cooperation.

## Operational Timeline

- **2022** — Canadian law enforcement searches a known LockBit affiliate; recovers a laptop running a LockBit programming interface over a Zservers-subleased IP address. *(Investigative trigger.)*
- **2022** — A Russian cybercriminal purchases IP addresses from Zservers, *almost certainly* for use as LockBit chat servers.
- **2023** — Zservers leases infrastructure, including a Russian IP address, to a LockBit affiliate.
- **2023** — In response to a Lebanese-company complaint that a Zservers IP was being used in a LockBit ransomware attack, Mishin instructs Bolshakov to assign the malicious user a new IP address while telling the complainant the original IP was cut off. *(Knowing-facilitation evidence.)*
- **2024 (prior year)** — US-AU-UK trilateral cyber sanctions against Alexander Ermakov and Evil Corp set the template the present action follows.
- **2025-02-11** — Trilateral designations announced. OFAC: Zservers + Mishin + Bolshakov. FCDO: same three plus XHOST Internet Solutions LP + Sidorov + Dmitriy Bolshakov + Odintsov + Ananev. DFAT: parallel designations under autonomous sanctions regime.

## Results and Impact

| Designating body | Entities | Individuals |
|---|---|---|
| OFAC (US) | 1 — Zservers | 2 — Mishin, Bolshakov |
| FCDO (UK) | 2 — Zservers, XHOST Internet Solutions LP | 6 — Mishin, A. Bolshakov, Sidorov, D. Bolshakov, Odintsov, Ananev |
| DFAT (AU) | parallel listing under autonomous regime | parallel listing under autonomous regime |

Direct disruption of LockBit operations is *unlikely* in the short term, since (i) the BPH entity remains physically in Russia, (ii) no servers were seized, and (iii) no individuals were arrested. The action's value is *highly likely* expectation-setting and supply-chain costing: Russian BPH providers can no longer count on undetected Western shell-company structures, and any Western financial institution touching Zservers- or XHOST-routed payments now faces secondary-sanctions exposure. This complements rather than replaces the law-enforcement disruption tracks ([[operation-cronos-phase1|Cronos Phase 1]], [[operation-cronos-phase3|Cronos Phase 3]]).

## Cooperation Mechanisms Used

- **Trilateral information-sharing** — US (OFAC), UK (FCDO), Australia (DFAT) coordinated designations on a single day. The specific information-sharing instrument is not disclosed; it is *highly likely* a Five Eyes / cyber-sanctions cell channel rather than a treaty-based MLAT request.
- **Domestic interagency** — DOJ and FBI provided supporting investigation per the release.
- **Foreign law-enforcement input** — 2022 Canadian search produced foundational evidence; the route by which that evidence reached OFAC is not specified.
- **Sanctions-regime stacking** — UK FCDO additionally designated a UK-registered front (XHOST Internet Solutions LP) that OFAC could not reach as effectively; the trilateral structure thus extends the geographic and corporate-veil reach of any single jurisdiction acting alone.

## Challenges and Friction Points

- **No extradition pathway.** All six designated natural persons are Russian nationals, *almost certainly* in Russia; arrest or extradition is *highly unlikely* under current conditions.
- **No physical seizure.** The press release records no server, domain, or cryptocurrency seizure — pure designations.
- **Unverified UK supplemental detail in OFAC body.** The UK FCDO designations of XHOST + four employees are not enumerated by name in the OFAC release body; cross-confirmation against the FCDO sanctions notice is required for full citation precision.
- **Rebranding risk.** As later seen with the Aeza → Hypercore rebranding documented in [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|the November 2025 SB-0319 designations]], BPH operators commonly re-incorporate under new shells; ongoing monitoring is required.

## Lessons Learned

- **The BPH layer is designable.** Treating the hosting provider — not just the affiliates — as a sanctions target attacks a dependency that affiliates cannot quickly replace.
- **Trilateral structure extends reach.** UK FCDO captured a UK-registered front (XHOST) and four further individuals that OFAC alone did not list, demonstrating the value of distributing the designating authority across jurisdictions.
- **Operator-level "service desk" evidence matters.** The 2023 IP-rotation incident (Mishin instructing Bolshakov to issue a new IP while lying to the complainant) is the kind of granular operational record that distinguishes knowing facilitation from passive hosting and is *highly likely* to recur as the evidentiary template for designating future BPH providers.
- **First entry in a 9-month sustained-pressure chain.** The Feb 2025 Zservers action, the July 2025 Aeza Group action, and the November 2025 [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|Media Land + Hypercore designations (SB-0319)]] form a deliberate 9-month US-AU-UK BPH-sanctions track. This wiki page is the first record of that chain pattern as a track rather than three discrete actions.

## Follow-Up Actions

- *Highly likely* July 2025 Aeza Group designations (track-internal sequel; not yet documented as a standalone wiki operation page).
- 2025-11-19 [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|Media Land + Hypercore designations (SB-0319)]] — closes the 9-month chain by sanctioning a separate BPH cluster (Media Land LLC and three sister companies, plus the Aeza-rebrand-front Hypercore Ltd.) under the same trilateral template.
- Continued FBI/CISA advisories on BPH-provider risk indicators (parallel guidance accompanied the November 2025 action).

## Korean Involvement (한국의 참여)

No direct Korean participation. South Korea is not a designating party in the trilateral US-AU-UK BPH-sanctions track. Indirect Korean relevance:

- South Korean financial institutions and crypto-asset service providers handling cross-border ransom payments fall within secondary-sanctions exposure if they process funds traceable to Zservers, XHOST Internet Solutions LP, Mishin, or Bolshakov; KoFIU's general practice is to align with OFAC SDN listings.
- South Korean victim entities of LockBit affiliates that used Zservers infrastructure benefit indirectly from the disruption of BPH supply chains, though no Korean victim is identified by Treasury in this release.
- The trilateral track is *roughly even chance* to expand to a quadrilateral structure including Korea or Japan in future rounds, but no public signal of that expansion appears in the present release.

## Contradictions & Open Questions

- **UK supplemental count.** Treasury body text designates only Zservers + Mishin + Bolshakov; the UK FCDO additionally designated XHOST Internet Solutions LP and four further individuals. The exact one-to-one mapping of UK-only designees to evidentiary basis is not established in the OFAC release.
- **Canadian agency identity.** "Canadian law enforcement" — RCMP? a provincial force? — is not specified.
- **Aeza Group coverage gap.** The intermediate (July 2025) Aeza Group designations are referenced in [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|the November 2025 Media Land action]] but do not yet have a standalone operation page in this wiki. Filling that gap would close the 9-month-chain documentation.
- **Information-sharing instrument.** The specific channel by which OFAC, FCDO, and DFAT coordinated the same-day designations is not disclosed — *highly likely* a Five Eyes cyber-sanctions cell, but not confirmed.
