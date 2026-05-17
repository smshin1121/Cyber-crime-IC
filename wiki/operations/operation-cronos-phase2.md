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
updated: 2026-05-17
---
## Summary

On 2024-05-07 the United States Justice Department, through the US Attorney's Office for the District of New Jersey, unsealed a 26-count federal indictment against [[ransomware-ic|Dmitry Yuryevich Khoroshev]] (alias LockBitSupp, LockBit, and putinkrab; 31, of Voronezh, Russia) — the alleged developer and administrator of the [[operation-cronos-phase1|LockBit]] ransomware group from approximately September 2019 through May 2024. Concurrent international actions included a US Treasury (OFAC) sanctions designation, a US Department of State reward offer of up to USD 10 million for information leading to Khoroshev's apprehension or conviction, and parallel sanctions by the UK's Office of Financial Sanctions Implementation (OFSI) and Australia's Department of Foreign Affairs and Trade (DFAT).

This wave is the named-suspect attribution and prosecution layer of the multi-phase [[operation-cronos-phase1|Operation Cronos]], filling the gap between the February 2024 NCA-led infrastructure disruption ([[operation-cronos-phase1|Phase 1]]) and the October 2024 NCA-led arrests and additional sanctions wave ([[operation-cronos-phase3|Phase 3]]).

## Background

### Modus operandi

LockBit operated under the **ransomware-as-a-service (RaaS)** model. Per the
unsealed DOJ DNJ indictment and prior DOJ/NCA filings, the LockBit
intrusion chain followed the canonical "human-operated ransomware" pattern:
(1) **initial access** obtained either by affiliates directly (via phishing,
RDP brute-force, exploitation of vulnerable internet-facing services, or
purchase from initial-access brokers feeding off [[operation-magnus-redline-meta-stealer-takedown-2024|infostealer-harvested credentials]]); (2) **internal
reconnaissance and lateral movement** within the victim network using
off-the-shelf and custom tooling; (3) **privilege escalation** to domain
administrator; (4) **defence-evasion** and disabling of endpoint protection,
backup systems, and shadow copies; (5) **double-extortion staging** —
exfiltration of victim data to attacker-controlled storage before encryption,
to support the "name and shame" data-leak-site (DLS) extortion layer; and
(6) **encryption deployment** of the LockBit locker payload (LockBit 1.0 →
LockBit 2.0 → LockBit 3.0/Black → LockBit Green generations, per public
threat-intelligence reporting). Victims received a ransom note pointing to a
Tor-hosted negotiation portal, with the parallel threat that exfiltrated data
would be published on the LockBit DLS if the demand was not met. Khoroshev,
as alleged developer/administrator, maintained the locker codebase, the
affiliate control panel, the DLS, and the negotiation infrastructure.

### Victim profile and impact

The DOJ DNJ indictment characterises the LockBit victim cohort as
**more than 2,500 victims in at least 120 countries, including
approximately 1,800 victims in the United States**, with victim verticals
spanning **hospitals, schools, critical infrastructure, multinational
corporations, small businesses, and government and law-enforcement
agencies**. The healthcare and education exposures translated into
operational impacts on patient care, scheduled clinical procedures,
school-system data, and municipal-service continuity; the critical-
infrastructure exposures included multiple incidents on industrial-control
and public-utility operators. Aggregate ransom proceeds extracted from
victims are stated at **at least USD 500 million**, with **billions of
dollars in broader losses** (downtime, remediation, regulatory exposure,
data-leak harm to natural-person data subjects swept up in exfiltrated
corporate datasets) attributable to LockBit attacks. The 1,800 US-victim
floor and the 120-country footprint make LockBit, on the indictment's own
figures, the largest single-RaaS-brand victim base publicly documented by
US prosecutors as of 2024-05-07.

### Financial flow

The LockBit revenue model rested on a **20/80 split**: per the indictment,
**Khoroshev typically received a 20 percent developer share of each ransom
payment**, with the responsible **affiliate receiving the remaining 80
percent**. Victim payments were demanded and settled in cryptocurrency
(predominantly Bitcoin, with some affiliates accepting other tokens at the
negotiation stage). On Khoroshev's 20-percent slice alone, the indictment
alleges he personally received **at least USD 100 million in cryptocurrency
disbursements** through his developer shares — implying an affiliate-side
aggregate proceeds figure several-fold larger and consistent with the
"USD 500 million-plus" group-level ransom-proceeds figure. After
disbursement, proceeds flowed through standard ransomware-laundering
pipelines (mixers, chain-hopping across multiple cryptocurrency tokens,
nested exchange accounts on lower-KYC venues, and conversion to fiat through
high-risk over-the-counter brokers). The concurrent **OFAC sanctions
designation**, **UK OFSI sanctions**, and **Australia DFAT sanctions**
specifically target the laundering and cash-out leg by freezing
US/UK/Australia-touching financial-system assets attributed to Khoroshev and
prohibiting US/UK/Australian persons from transacting with him under
penalty of secondary sanctions.

### Criminal organisation structure

LockBit displays the canonical **RaaS three-layer structure**: (1) a small
core **developer/administrator** team — the DOJ DNJ indictment attributes
that role to Khoroshev as the principal developer/administrator from
September 2019 through May 2024, with the broader Cronos operation
identifying additional charged co-conspirators tracked in
[[operation-cronos-phase1]] and [[operation-cronos-phase3]]; (2) an
**affiliate** layer composed of recruited operators who pay (or are revenue-
shared with) the core to access the locker, the panel, the DLS, and the
negotiation infrastructure, and who in practice run the intrusion campaigns
end-to-end against named victims; and (3) an **initial-access-broker / IAB**
upstream layer that supplies affiliates with pre-compromised credentials and
foothold access. Public reporting and the Phase 1/Phase 3 Cronos artefacts
identify multiple charged affiliates of various nationalities — including
Russian, Belarusian-Canadian, and dual-national defendants — and at least
two affiliates were in custody awaiting trial as of the 2024-05-07 Phase 2
announcement. The cooperation/recruitment perimeter alleged in the
indictment spans the Russian Federation (Khoroshev's residence) and other
jurisdictions where affiliates lived or operated; the indictment does not
assert any *state-sponsored* role and is structured around an organised-
criminal-group framing.

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
- **L26 gap — laundering-chain specifics:** the DOJ DNJ release describes the 20/80 split and Khoroshev's USD 100 million-plus personal proceeds but does not enumerate the specific cryptocurrency mixers, OTC brokers, nested exchange accounts, or cash-out venues used by Khoroshev or the affiliate layer. Background's "Financial flow" subsection therefore describes the laundering pipeline qualitatively; quantitative chain-analysis figures await OFAC sanctions-designation supporting material and any subsequent forfeiture pleadings.
- **L26 gap — per-victim/per-vertical impact breakdown:** the indictment supplies aggregate figures (2,500+ victims, 120+ countries, 1,800 US, USD 500M+ proceeds) but does not publish a per-vertical or per-country victim-impact breakdown. Background's "Victim profile and impact" subsection reflects the named verticals (healthcare, education, critical infrastructure, MNCs, SMBs, government and LE) from the indictment's narrative without quantitative disaggregation.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2024-05-07_justice-gov-dnj_us-charges-russian-national-developing-operating-lockbit-ransomware\|U.S. Charges Russian National with Developing and Operating Lockbit Ransomware]] | US DOJ DNJ / USAO-NJ | 2024-05-07 | https://www.justice.gov/usao-nj/pr/us-charges-russian-national-developing-and-operating-lockbit-ransomware |
