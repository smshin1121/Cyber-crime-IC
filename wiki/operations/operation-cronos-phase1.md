---
type: operation
title: "Operation Cronos — Phase 1 (LockBit Disruption)"
aliases:
  - "Operation Cronos Phase 1"
  - "LockBit takedown Feb 2024"
operation_type: takedown
status: completed
case_id: CYB-2024-002
period: 3
enforcement_type:
  - arrest
  - seizure
  - takedown
  - indictment
  - asset_freeze
outcome: success
credibility_index: 2.28
source_tier: 2
edges:
  - source_actor: "UK NCA"
    target_actor: Europol
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: Eurojust
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
missing_fields:
  - legal_basis
  - mechanisms_used
timeframe:
  announced: 2024-02-20
  start: 2024-02-20
  end: 2024-02-20
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "LockBit ransomware group"
lead_agency: "[[uk-nca]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[sweden]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[japan]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[switzerland]]"
  - "[[finland]]"
  - "[[poland]]"
  - "[[new-zealand]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[uk-nca]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[france-gendarmerie]]"
  - "[[germany-bka]]"
  - "[[netherlands-politie]]"
  - "[[sweden-police]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[japan-npa]]"
  - "[[fbi-cyber-division]]"
  - "[[switzerland-fedpol]]"
legal_basis:

mechanisms_used:

results:
  arrests: 2
  indictments: 5
  servers_seized: 34
  domains_seized: 0
  cryptocurrency_seized: "200+ accounts frozen"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "14,000+ rogue accounts identified for removal"
    - "Free decryption tools released on No More Ransom portal"
    - "3 international arrest warrants issued"
related_cases:
  - "[[us-v-astamirov-vasiliev-lockbit]]"
related_operations:
  - "[[operation-cronos-phase3]]"
  - "[[operation-us-v-astamirov-vasiliev-lockbit]]"
challenges_encountered:

lessons_learned:
  - "Multi-year coordination (27 Europol meetings, 4 technical sprints) enabled simultaneous multi-country action"
  - "Rapid decryption tool release through No More Ransom portal demonstrated victim-centric approach"
  - "SIENA messaging (1,000+ messages) proved essential for secure operational communication"
source_count: 7
sources:
  - "[[2024-02-20-europol-operation-cronos-lockbit]]"
  - "[[2024-05-07_gov-uk_uk-and-allies-sanction-prolific-cyber-hacker]]"
  - "[[2024-07-18_nj_lockbit-astamirov-vasiliev-pleas]]"
  - "[[2024-07-22_justice-gov_lockbit-case-summary-page]]"
  - "[[2024-10-01_europol-europa-eu_operation-cronos-phase-3]]"
  - "[[2024-12-04_nationalcrimeagency-gov-uk_operation-destabilise-nca-disrupts-multi-billion-money-laundering-networks]]"
  - "[[2026-01-28_gov-uk_financial-sanctions-guidance-for-ransomware]]"
created: 2026-04-08
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "**Operation Cronos Phase 1** was a landmark international law enforcement action that disrupted **LockBit**, the world's most deployed ransomware variant since 2022. On 20 February 2024, agencies from 10 countries executed a coordinated takedown of LockBit's infrastructure, led by the [[uk-nca|UK National Crime Agency]] and coordinated by [[europol-ec3|Europol]] and [[eurojust|Eurojust]]."
jurisdictions:
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[sweden]]"
  - "[[australia]]"
  - "[[canada]]"
  - "[[japan]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
  - "[[switzerland]]"
  - "[[finland]]"
  - "[[poland]]"
  - "[[new-zealand]]"
  - "[[ukraine]]"
organizations:
  - "[[uk-nca]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[france-gendarmerie]]"
  - "[[germany-bka]]"
  - "[[netherlands-politie]]"
  - "[[sweden-police]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[japan-npa]]"
  - "[[fbi-cyber-division]]"
  - "[[switzerland-fedpol]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
---
## Summary

**Operation Cronos Phase 1** was a landmark international law enforcement action that disrupted **LockBit**, the world's most deployed ransomware variant since 2022. On 20 February 2024, agencies from 10 countries executed a coordinated takedown of LockBit's infrastructure, led by the [[uk-nca|UK National Crime Agency]] and coordinated by [[europol-ec3|Europol]] and [[eurojust|Eurojust]].

The operation resulted in 34 servers seized across 8 countries, 2 arrests, 5 indictments, the freezing of over 200 cryptocurrency accounts, and the identification of 14,000+ rogue accounts. Free decryption tools were made available to victims worldwide through the "No More Ransom" portal.

This was *almost certainly* one of the most significant ransomware disruption operations in history, both in terms of the target's scale (LockBit had been the dominant ransomware variant globally) and the breadth of international cooperation involved.

## Background

LockBit emerged in late 2019 and by 2022 had become the most deployed ransomware variant worldwide. Operating as a Ransomware-as-a-Service (RaaS) platform, LockBit provided affiliates with malware tools in exchange for a share of ransom payments. The group's victims spanned critical infrastructure, healthcare, financial services, and government entities across dozens of countries.

The investigation that led to Operation Cronos involved sustained multi-year preparation, with [[europol-ec3|Europol]] organizing 27 operational meetings and 4 technical sprints to coordinate the action.

## Participating Parties

### Lead Agency
- [[uk-nca|UK National Crime Agency (NCA)]]

### Coordinating Bodies
- [[europol-ec3|Europol]] — operational coordination, analytical support, 27 operational meetings
- [[eurojust|Eurojust]] — judicial coordination

### Participating Countries (10)
France, Germany, Netherlands, Sweden, Australia, Canada, Japan, United Kingdom, United States, Switzerland

### Supporting Countries (4)
Finland, Poland, New Zealand, Ukraine

### Participating Agencies (12)
[[uk-nca]], [[europol-ec3]], [[eurojust]], [[france-gendarmerie|French Gendarmerie]], [[germany-bka|German BKA]], [[netherlands-politie|Dutch National Police]], [[sweden-police|Swedish Police]], [[australia-afp|Australian Federal Police]], [[canada-rcmp|RCMP]], [[japan-npa|Japanese NPA]], [[fbi-cyber-division|FBI]], [[switzerland-fedpol|Swiss Fedpol]]

## Legal Framework

The operation involved judicial actions in multiple jurisdictions:
- **French authorities** issued arrest warrants and indictments
- **US authorities** issued indictments (5 total between French and US)
- **Arrests** executed in Poland and Ukraine at the request of French judicial authorities

> [!info] Legal-basis note
> Specific legal bases (treaty provisions, domestic authorities) for the cross-border enforcement actions need to be identified from additional sources.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2024 | Multi-year investigation with 27 Europol operational meetings |
| Pre-2024 | 4 technical sprints conducted |
| 2024-02-20 | Coordinated action day: 34 servers seized across 8 countries |
| 2024-02-20 | 2 arrests in Poland and Ukraine |
| 2024-02-20 | 200+ cryptocurrency accounts frozen |
| 2024-02-20 | 14,000+ rogue accounts identified |
| 2024-02-20 | Decryption tools released on No More Ransom |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 2 (Poland, Ukraine) |
| International arrest warrants | 3 |
| Indictments | 5 (France, US) |
| Servers seized | 34 (across 8 countries) |
| Cryptocurrency accounts frozen | 200+ |
| Rogue accounts identified | 14,000+ |
| Operational meetings | 27 |
| Technical sprints | 4 |
| SIENA messages exchanged | 1,000+ |

The release of free decryption tools on the "No More Ransom" portal (available in 37 languages, covering 120+ solutions for 150+ ransomware types) was *highly likely* to have provided immediate relief to victims worldwide.

## Cooperation Mechanisms Used

- **SIENA** (Secure Information Exchange Network Application): 1,000+ operational messages exchanged
- **Europol operational meetings:** 27 meetings organized for planning and coordination
- **Technical sprints:** 4 sprints for coordinated technical analysis
- **No More Ransom portal:** Joint public-private initiative for victim decryption tool distribution

## Lessons Learned

1. **Multi-year coordination pays off:** The sustained investment of 27 operational meetings and 4 technical sprints enabled the simultaneous multi-country action that was essential for preventing the target from relocating infrastructure.
2. **Victim-centric approach:** The rapid release of decryption tools via No More Ransom demonstrated that operational outcomes can directly benefit victims, not just serve enforcement objectives.
3. **SIENA as backbone:** Over 1,000 SIENA messages confirmed this platform as the critical secure communication channel for large-scale EU-coordinated operations.
4. **Phase approach:** The operation was designed as a continuing campaign (Phase 1), with follow-up actions planned — this was *highly likely* intentional to maintain sustained pressure on the ransomware ecosystem.

## Follow-Up Actions

- [[operation-cronos-phase3|Operation Cronos Phase 3]] (October 2024): 4 additional arrests, 9 servers seized, financial sanctions against Evil Corp affiliates

## Korean Involvement (한국의 참여)

No direct Korean involvement in Operation Cronos Phase 1 was identified. However, the operation is relevant to Korea's cybercrime cooperation framework as LockBit victims included entities worldwide, and Korea's 2024 accession to the [[budapest-convention]] enhances future cooperation channels for similar operations.

## Contradictions & Open Questions

- What specific legal bases (treaty provisions) were invoked for the cross-border arrests in Poland and Ukraine?
- What was the exact scope and timing of the investigation phase preceding the action day?
- How many victims were directly assisted by the released decryption tools?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2024-02-20: Law enforcement disrupt world's biggest ransomware operation - Operation Cronos (LockBit).
- Foreign, Commonwealth & Development Office, 2024-05-07: UK and Allies Sanction Prolific Cyber Hacker.
- US DOJ (District of New Jersey), 2024-07-18: Two Foreign Nationals Plead Guilty to Participation in LockBit Ransomware Group.
- DOJ NJ, 2024-07-22: LockBit case summary page.
- Europol, 2024-10-01: Operation Cronos Phase 3.
- National Crime Agency, 2024-12-04: Operation Destabilise: NCA disrupts multi-billion money laundering networks.
- Office of Financial Sanctions Implementation, 2026-01-28: Financial sanctions guidance for ransomware.

## Evidence and Attribution Notes

- Operation Cronos Phase 1 disrupted LockBit, the world's most deployed ransomware since 2022, on 20 February 2024
- 10 countries participated with 12 agencies, led by UK NCA, coordinated by Europol and Eurojust
- 34 servers seized across 8 countries, 2 arrests (Poland, Ukraine), 5 indictments, 200+ cryptocurrency accounts frozen
- Free decryption tools released on No More Ransom portal covering 150+ ransomware types
- Europol organized 27 operational meetings and 4 technical sprints; 1,000+ SIENA messages exchanged
- On 20 February 2024, law enforcement agencies from 10 countries disrupted the LockBit ransomware operation in a joint action known as **Operation Cronos**, led by the UK's National Crime Agency and coordinated by Europol and Eurojust.
- LockBit had been the most deployed ransomware variant worldwide since 2022, having emerged in late 2019.
- The operation resulted in the seizure of 34 servers across 8 countries, 2 arrests, 5 indictments, the freezing of over 200 cryptocurrency accounts, and the identification of 14,000 rogue accounts for removal.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- Foreign, Commonwealth & Development Office, 2024-05-07: Today’s sanctions target Russian national Dmitry Khoroshev who has been identified, as part of an ongoing international law enforcement investigation, as one of the leaders of LockBit, the ransomware group responsible for extorting over $1 billion from thousands of victims globally.
- Foreign, Commonwealth & Development Office, 2024-05-07: In February the NCA announced that it had infiltrated the group’s network and taken control of its services , compromising the entire criminal enterprise.
- DOJ NJ, 2024-07-22: 24-299 Case Summary : Defendants Matveev, Vasiliev, Astamirov, Sungatov, Kondratyev, and Khoroshev have been charged for their role in a conspiracy to deploy a ransomware variant known as “LockBit,” a prolific form of malware and, at relevant times, the most deployed ransomware variant across the world.
- DOJ NJ, 2024-07-22: law, LockBit victims anywhere in the world are entitled to certain rights as a crime victim with respect to the ongoing LockBit prosecutions, including the right to claim restitution and/or to submit a victim impact statement to the Court for consideration at the sentencing of any LockBit defendant.
- National Crime Agency, 2024-12-04: Operation Destabilise: NCA disrupts $multi-billion Russian money laundering networks with links to, drugs, ransomware and espionage, resulting in 84 arrests - National Crime Agency --> Skip to content Quick exit Cymraeg Reporting SARs CSEA Reporting for Industry Protecting the public from serious and organised crime Who we are show.
- Office of Financial Sanctions Implementation, 2026-01-28: Financial sanctions guidance for ransomware - GOV.UK Cookies on GOV.UK We use some essential cookies to make this website work.
- Office of Financial Sanctions Implementation, 2026-01-28: Cyber resilience and mitigating ransomware attacks Print this page © Crown copyright 2026 This publication is licensed under the terms of the Open Government Licence v3.0 except where otherwise stated.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against LockBit ransomware group, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Uk Nca and coordination to Europol Ec3, with participating or affected jurisdictions recorded as France, Germany, Netherlands, Sweden, Australia, Canada, Japan, United Kingdom, United States, Switzerland, Finland, Poland, New Zealand, Ukraine.

The cooperation model is documented through named agencies and partners: Uk Nca, Europol Ec3, Eurojust, France Gendarmerie, Germany Bka, Netherlands Politie, Sweden Police, Australia Afp, Canada Rcmp, Japan Npa; enforcement posture: Arrest, Seizure, Takedown, Indictment, Asset Freeze.

Operational results captured for the canonical record: 2 arrests; 5 indictments; 34 servers seized; cryptocurrency/asset result recorded as 200+ accounts frozen; 14,000+ rogue accounts identified for removal; Free decryption tools released on No More Ransom portal; 3 international arrest warrants issued.

The canonical source set contains 7 reference(s): 2024 02 20 Europol Operation Cronos Lockbit, 2024 05 07 Gov Uk Uk And Allies Sanction Prolific Cyber Hacker, 2024 07 18 Nj Lockbit Astamirov Vasiliev Pleas, 2024 07 22 Justice Gov Lockbit Case Summary Page, 2024 10 01 Europol Europa Eu Operation Cronos Phase 3, 2024 12 04 Nationalcrimeagency Gov Uk Operation Destabilise Nca Disrupts Multi Billion Money Laundering Networks, plus 1 more.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis and Mechanisms Used.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Law enforcement disrupt world's biggest ransomware operation - Operation Cronos (LockBit) | Europol | 2024-02-20 | https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation |
| [2] | UK and Allies Sanction Prolific Cyber Hacker | Foreign, Commonwealth & Development Office | 2024-05-07 | https://www.gov.uk/government/news/uk-and-allies-sanction-prolific-cyber-hacker |
| [3] | Two Foreign Nationals Plead Guilty to Participation in LockBit Ransomware Group | US DOJ (District of New Jersey) | 2024-07-18 | https://www.justice.gov/usao-nj/pr/two-foreign-nationals-plead-guilty-participation-lockbit-ransomware-group |
| [4] | LockBit case summary page | DOJ NJ | 2024-07-22 | https://www.justice.gov/usao-nj/lockbit |
| [5] | Operation Cronos Phase 3 | Europol | 2024-10-01 | https://www.europol.europa.eu/media-press/newsroom/news/lockbit-power-cut-four-new-arrests-and-financial-sanctions-against-affiliates |
| [6] | Operation Destabilise: NCA disrupts multi-billion money laundering networks | National Crime Agency | 2024-12-04 | https://www.nationalcrimeagency.gov.uk/news/operation-destabilise-nca-disrupts-multi-billion-russian-money-laundering-networks-with-links-to-drugs-ransomware-and-espionage-resulting-in-84-arrests |
| [7] | Financial sanctions guidance for ransomware | Office of Financial Sanctions Implementation | 2026-01-28 | https://www.gov.uk/government/publications/financial-sanctions-guidance-for-ransomware/financial-sanctions-guidance-for-ransomware |
