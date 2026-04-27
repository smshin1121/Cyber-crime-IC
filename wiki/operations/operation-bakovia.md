---
type: operation
title: "Operation Bakovia (CTB-Locker/Cerber Ransomware)"
title_ko: "Operation Bakovia (CTB-Locker/Cerber 랜섬웨어)"
aliases:
  - "Operation Bakovia"
  - "CTB-Locker Cerber arrests"
case_id: CYB-2018-050
period: 1
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2017-12-20
  start: 2017-12-14
  end: 2017-12-20
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "CTB-Locker and Cerber ransomware distributors"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[romania]]"
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[romania-diicot]]"
  - "[[fbi-cyber-division]]"
  - "[[uk-nca]]"
  - "[[netherlands-politie]]"
  - "McAfee Advanced Threat Research"
legal_basis:

mechanisms_used:

results:
  arrests: 5
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Six houses searched in eastern Romania"
    - "CTB-Locker and Cerber distributors tied to ransomware-as-a-service affiliate activity"
    - "Hard drives, laptops, external storage, cryptocurrency mining devices, documents, and SIM cards seized"
edges:
  - source_actor: Europol
    target_actor: "Romania DIICOT"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "Dutch National Police"
    target_actor: "McAfee Advanced Threat Research"
    cooperation_type: intelligence_sharing
    legal_basis: unknown
    direction: undirected
credibility_index: 2.0
source_tier: 3
missing_fields:
  - legal_basis
  - mechanisms_used
  - exact_arrest_details
related_cases:

related_operations:

challenges_encountered:

lessons_learned:
  - "Public-private malware analysis materially improved attribution in a ransomware distributor case."
  - "Affiliate-level ransomware enforcement can disrupt high-volume campaigns even when core developers are not arrested."
source_count: 5
sources:
  - "[[2017-12-01_cyberscoop-com_ctb-locker-cerber-ransomware-arrests-europol-mcafee]]"
  - "[[2017-12-20_mcafee_mcafee-labs-advanced-threat-research-aids-arrest-of-suspected-cybercrime-gang-linked-to-top-malware-ctb-locker]]"
  - "[[2017-12-20_bleepingcomputer_five-romanians-arrested-for-spreading-ctb-locker-and-cerber-ransomware]]"
  - "[[2017-12-20_portswigger-daily-swig_arrests-made-in-connection-with-ctb-locker-cerber-ransomware]]"
  - "[[2017-12-20_thehackernews_romanian-police-arrest-5-people-for-spreading-ctb-locker-and-cerber-ransomware]]"
created: 2026-04-08
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "**Operation Bakovia** was a joint international law-enforcement action targeting distributors of the CTB-Locker and Cerber ransomware families. The operation culminated in Romania in December 2017 with five arrests, six house searches, and evidence seizures, supported by Europol, Dutch and British investigators, U.S. authorities, and McAfee's malware-analysis team."
jurisdictions:
  - "[[romania]]"
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[united-kingdom]]"
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[romania-diicot]]"
  - "[[fbi-cyber-division]]"
  - "[[uk-nca]]"
  - "[[netherlands-politie]]"
  - "McAfee Advanced Threat Research"
crime_types:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
---
> [!note] This operation remains media-heavy, but it now has multiple corroborating sources, including McAfee's first-hand description of its investigative support.

## Summary

Operation Bakovia targeted distributors of the CTB-Locker and Cerber ransomware families rather than the malware developers themselves. Public reporting indicates the suspects operated as ransomware-as-a-service affiliates, using spam campaigns and malicious attachments to infect victims in Europe and the United States.

## Background

CTB-Locker was one of the earliest ransomware families to make extensive use of Tor-hidden infrastructure. Cerber later became one of the most profitable ransomware-as-a-service families. The Bakovia case is useful because it shows law enforcement moving against operators who distributed and monetized these malware families at scale.

## Participating Parties

### Coordinating Body
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust]]

### Participating Countries
- [[romania|Romania]]
- [[netherlands|Netherlands]]
- [[united-kingdom|United Kingdom]]
- [[united-states|United States]]

### Participating Agencies
- [[romania-diicot|Romania DIICOT]]
- [[europol-ec3|Europol EC3]]
- [[fbi-cyber-division|FBI Cyber Division]]
- [[uk-nca|UK National Crime Agency]]
- [[netherlands-politie|Dutch National Police]]
- McAfee Advanced Threat Research

## Operational Timeline

| Date | Event |
|------|-------|
| 2015-2017 | Dutch, Romanian, British, and U.S.-linked investigative work on CTB-Locker and Cerber distribution activity |
| 2017-12-14 | McAfee says Operation Bakovia began |
| 2017-12 | Six searches conducted in eastern Romania |
| 2017-12-20 | Public reporting confirms five arrests linked to CTB-Locker and Cerber distribution |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 5 |
| Houses searched | 6 |
| Countries materially involved | 4 |

The seized material reportedly included hard drives, laptops, external storage devices, cryptocurrency mining devices, documents, and hundreds of SIM cards.

## Cooperation Mechanisms Used

Public reporting indicates a mixed cooperation model:

- Europol coordination and analytical support
- Dutch investigative access to malware-distribution infrastructure
- U.S. Secret Service and FBI intelligence links on Cerber activity affecting U.S. victims
- McAfee malware analysis for attribution and evidentiary support

## Korean Involvement

No Korean involvement was identified in the available public sources.

## Contradictions & Open Questions

- The public record is still thin on the exact charging and court outcome after arrest.
- Europol and Eurojust involvement imply formal judicial cooperation, but the specific instrument is not publicly documented.
- Available sources do not clearly separate CTB-Locker victim counts from Cerber victim counts.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search and archive review through 2026-04-23 did not surface open court records tied to this operation.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- CyberScoop, 2017-12-01: CTB-Locker Cerber ransomware arrests — Europol, McAfee.
- McAfee, 2017-12-20: McAfee Labs Advanced Threat Research Aids Arrest of Suspected Cybercrime Gang Linked to Top Malware CTB Locker.
- BleepingComputer, 2017-12-20: Five Romanians Arrested for Spreading CTB-Locker and Cerber Ransomware.
- The Daily Swig, 2017-12-20: Arrests made in connection with CTB-Locker, Cerber ransomware.
- The Hacker News, 2017-12-20: Romanian Police Arrest 5 People for Spreading CTB Locker and Cerber Ransomware.

## Legal and Procedural Posture

- Recorded crime classification: ransomware and malware.
- Recorded enforcement posture: Arrest and Seizure.
- The record is categorized as arrest-sweep with status completed.

## Evidence and Attribution Notes

- **Operation Bakovia** was a joint international law enforcement action targeting the distributors of **CTB-Locker** and **Cerber** ransomware, two of the most widespread ransomware families in 2016-2017.
- Coordinated by Europol, the operation resulted in arrests in Romania, with support from the FBI, UK NCA, and Dutch National Police.
- McAfee provided key private-sector intelligence support.
- McAfee stated that Operation Bakovia began on 14 December 2017 and that six houses in eastern Romania were searched while investigators pursued CTB-Locker and Cerber distributors.
- The company described its own malware-analysis support for Dutch investigators, adding evidence of a public-private investigative model.
- McAfee's account adds technical and operational context for Operation Bakovia, especially the malware-analysis role that helped attribute the actors behind CTB-Locker and Cerber distribution.
- McAfee described its support to the investigation later identified as Operation Bakovia.
- The company said Dutch investigators asked its Advanced Threat Research team to analyze malware samples from a server used to distribute CTB-Locker, and the inquiry later expanded to Cerber based on U.S. Secret Service information.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a arrest-sweep against CTB-Locker and Cerber ransomware distributors, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Europol Ec3 and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Romania, Netherlands, United States, United Kingdom.

The cooperation model is documented through named agencies and partners: Europol Ec3, Eurojust, Romania Diicot, Fbi Cyber Division, Uk Nca, Netherlands Politie, Mcafee Advanced Threat Research; enforcement posture: Arrest and Seizure.

Operational results captured for the canonical record: 5 arrests; Six houses searched in eastern Romania; CTB-Locker and Cerber distributors tied to ransomware-as-a-service affiliate activity; Hard drives, laptops, external storage, cryptocurrency mining devices, documents, and SIM cards seized.

The canonical source set contains 5 reference(s): 2017 12 01 Cyberscoop Com Ctb Locker Cerber Ransomware Arrests Europol Mcafee, 2017 12 20 Mcafee Mcafee Labs Advanced Threat Research Aids Arrest Of Suspected Cybercrime Gang Linked To Top Malware Ctb Locker, 2017 12 20 Bleepingcomputer Five Romanians Arrested For Spreading Ctb Locker And Cerber Ransomware, 2017 12 20 Portswigger Daily Swig Arrests Made In Connection With Ctb Locker Cerber Ransomware, 2017 12 20 Thehackernews Romanian Police Arrest 5 People For Spreading Ctb Locker And Cerber Ransomware.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis, Mechanisms Used, Exact Arrest Details.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | CTB-Locker Cerber ransomware arrests — Europol, McAfee | CyberScoop | 2017-12-01 | https://cyberscoop.com/ctb-locker-cerber-ransomware-arrests-europol-mcafee/ |
| [2] | McAfee Labs Advanced Threat Research Aids Arrest of Suspected Cybercrime Gang Linked to Top Malware CTB Locker | McAfee | 2017-12-20 | https://www.mcafee.com/blogs/other-blogs/mcafee-labs/advanced-threat-research/ |
| [3] | Five Romanians Arrested for Spreading CTB-Locker and Cerber Ransomware | BleepingComputer | 2017-12-20 | https://www.bleepingcomputer.com/news/security/five-romanians-arrested-for-spreading-ctb-locker-and-cerber-ransomware/ |
| [4] | Arrests made in connection with CTB-Locker, Cerber ransomware | The Daily Swig | 2017-12-20 | https://portswigger.net/daily-swig/arrests-made-in-connection-with-ctb-locker-cerber-ransomware |
| [5] | Romanian Police Arrest 5 People for Spreading CTB Locker and Cerber Ransomware | The Hacker News | 2017-12-20 | https://thehackernews.com/2017/12/ctb-locker-cerber-ransomware.html |
