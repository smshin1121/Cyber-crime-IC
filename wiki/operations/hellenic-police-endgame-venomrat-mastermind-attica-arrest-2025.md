---
type: operation
title: "Hellenic Police — Operation Endgame Greek Limb: VenomRAT Mastermind Arrest in Attica (2025-11-03)"
title_ko: "그리스 경찰청 — Operation Endgame 그리스 분기: VenomRAT 개발자 검거 (아티카, 2025-11-03)"
aliases:
  - "Operation Endgame Greek limb VenomRAT mastermind arrest 2025"
  - "Hellenic Police Cyber Crime Directorate VenomRAT Attica arrest November 2025"
  - "Επιχείρηση Endgame: σύλληψη 38χρονου στην Αττική για VenomRAT (2025)"
  - "Greek arrest of VenomRAT developer Operation Endgame phase Nov 2025"
case_id: CYB-2025-202
period: 3
operation_role: national-limb
parent_operation: "[[operation-endgame-phase3]]"
operation_type: arrest-sweep
status: ongoing
enforcement_type:
  - arrest
  - search-seizure
outcome: partial
timeframe:
  announced: 2025-11-13
  start: 2025-11-03
  end: 2025-11-13
  ongoing: true
crime_types:
  - "[[malware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[hacking-ic]]"
crime_type: "[[malware-ic]]"
target_entity: "A 38-year-old foreign national resident in Attica (multiple Greek-media corroborations identify the suspect as an Albanian national; exact name not disclosed in the Hellenic Police release). Assessed by investigators to be the principal developer and seller, since 2020, of the VenomRAT remote-access trojan distributed as a subscription-based cybercrime-as-a-service platform (€150/month — €1,550/year)."
lead_agency: ""
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[greece]]"
  - "[[france]]"
  - "[[united-states]]"
participating_agencies:
  - "Hellenic Police Cyber Crime Directorate (Διεύθυνση Δίωξης Ηλεκτρονικού Εγκλήματος)"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi]]"
  - "French judicial authorities (issuing authority of the European Arrest Warrant under which the suspect was detained; specific issuing court not disclosed in the Hellenic Police release)"
legal_basis:
  - "[[european-arrest-warrant]] issued by French judicial authorities"
  - "Greek Penal Code cybercrime offences (illegal access to information systems, malware production/distribution); specific Greek charging articles not disclosed in the public release"
  - "Operation Endgame multilateral law-enforcement coordination framework (no specific binding instrument cited in the release; coordination via Europol Joint Cybercrime Action Taskforce (J-CAT) and Eurojust)"
mechanisms_used:
  - "[[european-arrest-warrant]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "approximately US$140,424 (digital wallet seized from the Attica residence)"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Search of the Attica residence carried out by Hellenic Police with FBI representatives participating on-site"
    - "Seizures: 7 hard drives, 3 USB storage devices, 11 debit cards, mobile phones, technical equipment used for malware development and distribution"
    - "Greek prosecution and possible onward surrender/extradition to France under the EAW remain pending as of the 2025-11-13 release; no charges, sentencing, or victim count figures disclosed on the Greek side"
credibility_index: 0.0
source_tier: 1
missing_fields:
  - suspect_name
  - exact_greek_charges
  - eaw_issuing_court_specific
  - victim_count_attributable_to_venomrat
  - sentencing_status
  - extradition_outcome_to_france
related_cases: []
related_operations:
  - "[[operation-endgame]]"
  - "[[operation-endgame-phase3]]"
  - "[[rcmp-cit-v-canada-endgame-surrey-malware-loader-arrest-2025]]"
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[[2025-11-13_astynomia-gr_hellenic-police-operation-endgame-venomrat-mastermind-arrest]]"
created: 2026-05-16
updated: 2026-05-16
---

## Summary

On 2025-11-03 in Attica, Greece, the Hellenic Police Cyber Crime Directorate (Διεύθυνση Δίωξης Ηλεκτρονικού Εγκλήματος) arrested a 38-year-old foreign national assessed to be the principal developer and seller, since 2020, of the VenomRAT remote-access trojan — a subscription-based cybercrime-as-a-service platform. The arrest was carried out pursuant to a European Arrest Warrant issued by French judicial authorities, with U.S. FBI representatives participating on-site at the residential search alongside Hellenic Police officers. The action is the Greek limb of the November 2025 phase of the multilateral Operation Endgame (see umbrella page [[operation-endgame-phase3]]), coordinated by [[europol-ec3]] and [[eurojust]].

The Hellenic Police announced the arrest publicly on 2025-11-13, aligned with the synchronised European Operation Endgame disclosure window (2025-11-10 through 2025-11-14). This sub-operation page is filed as a companion to the umbrella phase-3 page, mirroring the existing pattern for the Canadian RCMP-CIT-V Surrey limb arrest ([[rcmp-cit-v-canada-endgame-surrey-malware-loader-arrest-2025]]).

## Background

VenomRAT was operated since 2020 as a subscription-based remote-access trojan sold to a global buyer base. Subscription pricing reported in the Hellenic Police release and Greek-media reproductions: €150 per month to €1,550 per year. The malware, once installed on a victim device, allowed the buyer to: take full remote control of the device; log keystrokes; capture video and audio via the device camera and microphone; exfiltrate text data; and access cryptocurrency wallets stored on the device. VenomRAT was identified by Europol/Eurojust in the umbrella November 2025 Operation Endgame release as one of three "cybercrime-as-a-service enablers" targeted in this phase, alongside the Rhadamanthys infostealer and the Elysium botnet — collectively assessed to have infected hundreds of thousands of victim devices worldwide and to have supplied access to downstream ransomware and credential-theft operators.

The Hellenic Police identified the Attica-resident 38-year-old as the principal author of VenomRAT through a combination of Greek investigative leads, Europol Joint Cybercrime Action Taskforce (J-CAT) analytical product, and a European Arrest Warrant request originating from French judicial authorities. The suspect's nationality is not disclosed in the Hellenic Police release; Greek-media corroborations identify him as an Albanian national.

## Participating Parties

- **Hellenic Police Cyber Crime Directorate (Διεύθυνση Δίωξης Ηλεκτρονικού Εγκλήματος)** — Greek arresting authority. Conducted the 2025-11-03 arrest and on-site residential search in Attica. (Operational lead for the Greek limb. Hellenic Police does not yet have a dedicated wiki organisation page; per LESSONS.md L23 the `lead_agency` frontmatter field is therefore left empty and the agency is preserved here in prose plus in the `participating_agencies` plain-text entry.)
- **[[europol-ec3]]** — operational coordinating body for Operation Endgame; supplied analytical product and J-CAT coordination across all participating jurisdictions.
- **[[eurojust]]** — judicial coordinating body; supported European Arrest Warrant execution and cross-border evidence handling.
- **[[fbi]]** — U.S. Federal Bureau of Investigation. Representatives participated on-site at the 2025-11-03 search of the suspect's Attica residence (explicitly named in the Hellenic Police release).
- **French judicial authorities** — issuing authority of the European Arrest Warrant under which the Attica arrest was executed. Specific issuing court is not disclosed in the Hellenic Police release.
- Wider November 2025 Operation Endgame jurisdictions per the umbrella Europol release (background context, not all explicitly named as having cooperated on the Greek arrest specifically): Australia, Belgium, Canada, Denmark, France, Germany, Greece, Lithuania, the Netherlands, the United Kingdom, and the United States. The Greek limb's `participating_countries` field is restricted to those whose LE/prosecutorial cooperation on the Greek arrest is explicitly named in the tier-1 release (per LESSONS.md L24 strict): Greece (arresting authority), France (EAW issuer), and the United States (FBI on-site presence at the search).

## Legal Framework

The arrest was executed under a [[european-arrest-warrant]] issued by French judicial authorities — a Council Framework Decision 2002/584/JHA mechanism providing for streamlined cross-border surrender within the EU. The Greek charges (illegal access to information systems and malware production/distribution under Greek Penal Code provisions implementing the Budapest Convention substantive-law articles) and the underlying French indictment are not detailed in the Hellenic Police release; specific charging articles will only become clear in subsequent Greek and French court documents.

Operational coordination operated through the Europol Joint Cybercrime Action Taskforce (J-CAT) and Eurojust judicial coordination meetings, both of which are standing mechanisms rather than ad-hoc instruments for this case.

## Operational Timeline

- **Pre-2025**: French judicial investigation into VenomRAT victims and infrastructure; European Arrest Warrant issued by French judicial authorities for the Attica-resident suspect (exact issuing date not disclosed publicly).
- **2025-11-03 (early hours, Attica)**: Hellenic Police Cyber Crime Directorate, with U.S. FBI representatives on-site, executes the arrest of the 38-year-old suspect and search warrant at the residence. Seizures: 7 hard drives, 3 USB devices, 11 debit cards, mobile phones, malware-development equipment, and a digital wallet containing cryptocurrency valued at approximately US$140,424.
- **2025-11-10 through 2025-11-14**: Synchronised wider Operation Endgame action window across Germany (1 location), Greece (1 — the Attica arrest), and the Netherlands (9 locations). 1,025 servers dismantled and 20 domains seized across all jurisdictions.
- **2025-11-13 (Athens)**: Hellenic Police publishes the Greek-side press release on astynomia.gr aligned with the Europol/Eurojust umbrella disclosure.
- **Post-2025-11-13**: Greek prosecution proceedings and possible onward surrender/extradition to France pursuant to the EAW remain pending. Outcomes not disclosed as of the source date.

## Results and Impact

- **Arrests**: 1 (Attica, 2025-11-03).
- **Cryptocurrency seized**: approximately US$140,424 (from the residential digital wallet).
- **Physical seizures**: 7 hard drives, 3 USB storage devices, 11 debit cards, mobile phones, malware-development equipment.
- **Wider context (Operation Endgame Nov 2025 phase, not attributed solely to the Greek limb)**: 1,025 servers dismantled, 20 domains seized, 11 physical search locations across 3 countries.
- **Indictments, sentencing, victim count, extradition outcome**: not disclosed as of the 2025-11-13 release.

## Cooperation Mechanisms Used

- **European Arrest Warrant ([[european-arrest-warrant]])** — the operative legal mechanism that authorised the Greek police to arrest the suspect on Greek territory on behalf of French prosecutorial interests, with downstream surrender to France contemplated.
- **[[europol-ec3]] J-CAT operational coordination** — analytical product, target-package preparation, multi-jurisdictional action-day synchronisation.
- **[[eurojust]] judicial coordination** — cross-border evidentiary and procedural alignment.
- **Bilateral US–Greece operational cooperation** — FBI on-site presence at the Attica residential search, reflecting joint US interest in the VenomRAT victim base (the United States is one of the principal victim jurisdictions for VenomRAT-enabled intrusions).

## Challenges and Friction Points

- **Cross-jurisdictional prosecution allocation**: the suspect is physically in Greece, the EAW was issued by France, the FBI participated in the on-site search, and victims span all 11 Operation Endgame jurisdictions. Final prosecutorial venue (Greek prosecution, French prosecution post-surrender, or paralleled proceedings) is not disclosed as of the 2025-11-13 release.
- **Public attribution constraints**: the suspect's name and full charging detail are withheld in the Hellenic Police release in line with Greek procedural-secrecy norms during pre-trial phases. Greek-media corroborations identifying the suspect as an Albanian national are not embedded in the tier-1 Hellenic Police press release itself.

## Lessons Learned

- Operation Endgame continues to demonstrate the "umbrella + national-limb" reporting pattern: each participating jurisdiction publishes a national-side press release on the action day aligned with the Europol/Eurojust umbrella release, with the national-side releases adding jurisdictional procedural detail (here, the EAW basis, the FBI on-site presence, and the specific Attica seizures) that the umbrella release does not contain. This sub-operation page captures the Greek-side procedural detail that complements [[operation-endgame-phase3]].
- The cooperation pattern (Greek arrest under French-issued EAW with US FBI on-site) is a textbook illustration of [[european-arrest-warrant]] mechanics combined with informal bilateral US–EU operational cooperation outside any single MLAT instrument.

## Follow-Up Actions

- Track downstream Greek prosecution proceedings and any surrender to France under the EAW.
- Track downstream French indictment unsealing (if any) for the underlying VenomRAT charges.
- Track downstream US prosecutorial filings (if any) given the FBI on-site role and US victim exposure.

## Korean Involvement (한국의 참여)

No South Korean (or other Korean) law-enforcement involvement is named in the Hellenic Police release or the Europol/Eurojust umbrella release for this phase. Korea was not in the 11-jurisdiction Operation Endgame Nov 2025 participating roster.

## Contradictions & Open Questions

> [!note] Suspect nationality
> Greek-media reproductions of the Hellenic Police release identify the suspect as an Albanian national; the Hellenic Police release itself describes him as "a 38-year-old foreign national" without specifying nationality. This page records the broader "foreign national" framing in the structured frontmatter and notes the Greek-media corroboration in prose, pending confirmation of nationality in a court filing.

> [!note] Specific charging articles
> Specific Greek Penal Code charging articles and the specific French indictment count are not disclosed in the tier-1 release. Confidence on the broader malware-distribution and cybercrime-as-a-service framing is *highly likely* (>80%) given the consistent description across Hellenic Police, Europol, and Eurojust releases; confidence on any specific charging-article enumeration remains low pending court documents.
