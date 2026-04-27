---
type: operation
title: "Lumma Stealer Takedown"
aliases:
  - "LummaC2 Disruption"
  - "Lumma Stealer Disruption"
case_id: CYB-2025-012
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2025-05-21
  start: 2025-05-13
  end: 2025-05-21
  ongoing: false
crime_type: "[[hacking-ic]]"
target_entity: "LummaC2 / Lumma Stealer malware-as-a-service infrastructure"
lead_agency: "[[us-doj]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[japan]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[japan-npa]]"
legal_basis:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[public-private-cooperation]]"
  - "[[informal-cooperation]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 2300
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "More than 1,300 domains were redirected to Microsoft sinkholes."
    - "The DOJ seized five core domains used as Lumma administration panels."
    - "Microsoft identified more than 394,000 infected Windows computers between March 16 and May 16, 2025."
    - "The FBI identified at least 1.7 million credential-theft instances tied to LummaC2."
source_count: 5
sources:
  - "[[2025-05-21_microsoft_lumma-stealer-global-action]]"
  - "[[2025-05-21_justice-gov_lumma-stealer-domain-seizures]]"
  - "[[2025-05-21_microsoft-security-blog_lumma-stealer-analysis]]"
  - "[[2025-05-21_bleepingcomputer-com_lumma-infostealer-malware-operation-disrupted-2300-domains-seized]]"
  - "[[2025-05-21_wired-com_lumma-stealer-takedown-disrupted]]"
created: 2025-05-21
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "The Lumma Stealer takedown was a U.S.-led, Europol-supported, public-private operation that disrupted roughly 2,300 LummaC2 domains and combined Microsoft civil action with DOJ criminal seizure warrants."
jurisdictions:
  - "[[united-states]]"
  - "[[japan]]"
organizations:
  - "[[us-doj]]"
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
  - "[[japan-npa]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[malware-ic]]"
---
> [!note] Source basis
> This page is rebuilt from official Microsoft and DOJ material. The prior version had a malformed `sources` field and no usable references table, which made a legitimate international operation look under-sourced.

## Summary

**Lumma Stealer Takedown** was a coordinated public-private operation announced on 21 May 2025 against the **LummaC2** infostealer ecosystem. The operation combined **Microsoft civil action**, **DOJ criminal domain seizures**, **Europol coordination on the European side**, and **Japan-side infrastructure disruption assistance**, making it a strong international-cooperation case even though no arrests were announced at the takedown stage.

## Background

LummaC2 was a malware-as-a-service platform used to steal credentials, banking data, and cryptocurrency wallet information. The key reason this page belongs in the operation corpus is that it demonstrates a recurring modern pattern in cybercrime response: a hybrid disruption model where private-sector litigation, criminal seizure authority, and cross-border operational coordination are used together against resilient malware infrastructure.

## Participating Parties

### Government / Law Enforcement
- [[us-doj|U.S. Department of Justice]]
- [[fbi-cyber-division|FBI]]
- [[europol-ec3|Europol EC3]]
- [[japan-npa|Japan-side cybercrime control authorities / JC3 support]]

### Private-Sector Partners
- Microsoft Digital Crimes Unit
- Microsoft Threat Intelligence

## Results and Impact

| Metric | Detail |
|--------|--------|
| Domains disrupted | approximately 2,300 |
| Domains redirected to Microsoft sinkholes | 1,300+ |
| Core domains seized by DOJ | 5 |
| Infected Windows computers identified by Microsoft | 394,000+ |
| Credential-theft instances identified by FBI | at least 1.7 million |

## Cooperation Mechanisms Used

The operation is notable because the cooperation model is explicit in the sources. Microsoft used a civil court order in the Northern District of Georgia; DOJ used criminal seizure warrants; Europol facilitated European law-enforcement action; and Japan-side partners supported local infrastructure suspension. This is a cleaner example of public-private international disruption than many follow-on DOJ-only pages in the corpus.

## Contradictions & Open Questions

- The operation did not produce public arrests, so operator attribution remains incomplete in the public record.
- Some public summaries cite the coordination date differently because the civil filing, warrant execution, and public announcement happened on different days.
- The current source set strongly supports disruption mechanics but less strongly supports long-term operator-side outcomes.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Microsoft, 2025-05-21: Disrupting Lumma Stealer: Microsoft leads global action against favored cybercrime tool.
- U.S. Department of Justice, 2025-05-21: Justice Department Seizes Domains Behind Major Information-Stealing Malware Operation.
- Microsoft Security Blog, 2025-05-21: Lumma Stealer: Breaking down the delivery techniques and capabilities of a prolific infostealer.
- BleepingComputer, 2025-05-21: Lumma infostealer malware operation disrupted, 2,300 domains seized.
- WIRED, 2025-05-21: Authorities Carry Out Elaborate Global Takedown of Infostealer Heavily Used by Cybercriminals.

## Operational Timeline

- 2025-05-13: activity or investigation start.
- 2025-05-21: public announcement.
- 2025-05-21: reported enforcement endpoint.
- 2025-05-21: public source coverage from BleepingComputer, Microsoft, Microsoft Security Blog, U.S. Department of Justice.

## Legal and Procedural Posture

- Recorded crime classification: hacking and malware.
- Recorded enforcement posture: Seizure and Takedown.
- Legal or procedural basis recorded in metadata: Budapest Convention.
- The record is categorized as takedown with status completed.

## Evidence and Attribution Notes

- Microsoft says approximately 2,300 Lumma-linked domains were seized, blocked, or redirected.
- The post names DOJ, Europol EC3, and Japan's JC3 as partners.
- It is the principal source for the criminal-seizure side of the operation.
- Microsoft details LummaC2's malware-as-a-service structure and delivery ecosystem.
- The post confirms that disruption involved approximately 2,300 malicious domains.
- BleepingComputer reported that 2,300 domains tied to Lumma were disrupted in a joint Microsoft-DOJ-Europol-Japan action.
- The article highlighted the role of Europol and the Japan Cybercrime Control Center in regional infrastructure seizures.
- WIRED reported that Lumma was disrupted through coordinated action involving Microsoft, DOJ, Europol, and Japan.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- U.S. Department of Justice, 2025-05-21: We are grateful for their work and dedication.” “Malware like LummaC2 is deployed to steal sensitive information such as user login credentials from millions of victims in order to facilitate a host of crimes, including fraudulent bank transfers and cryptocurrency theft,” said Matthew R.
- U.S. Department of Justice, 2025-05-21: Together, we are making it harder, and more painful, for cyber criminals to operate.” As alleged in the affidavits filed in support of the government’s seizure warrants, the administrators of LummaC2 used the seized websites to distribute LummaC2, an information-stealing malware, to their affiliates and other cyber criminals.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against LummaC2 / Lumma Stealer malware-as-a-service infrastructure, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Us Doj and coordination to Europol Ec3, with participating or affected jurisdictions recorded as United States and Japan.

The cooperation model is documented through named agencies and partners: Us Doj, Fbi Cyber Division, Europol Ec3, Japan Npa; mechanisms: Public Private Cooperation and informal cooperation; legal basis: Budapest Convention; enforcement posture: Seizure and Takedown.

Operational results captured for the canonical record: 2300 domains seized; More than 1,300 domains were redirected to Microsoft sinkholes.; The DOJ seized five core domains used as Lumma administration panels.; Microsoft identified more than 394,000 infected Windows computers between March 16 and May 16, 2025.; The FBI identified at least 1.7 million credential-theft instances tied to LummaC2..

The canonical source set contains 5 reference(s): 2025 05 21 Microsoft Lumma Stealer Global Action, 2025 05 21 Justice Gov Lumma Stealer Domain Seizures, 2025 05 21 Microsoft Security Blog Lumma Stealer Analysis, 2025 05 21 Bleepingcomputer Com Lumma Infostealer Malware Operation Disrupted 2300 Domains Seized, 2025 05 21 Wired Com Lumma Stealer Takedown Disrupted.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Disrupting Lumma Stealer: Microsoft leads global action against favored cybercrime tool | Microsoft | 2025-05-21 | https://blogs.microsoft.com/on-the-issues/2025/05/21/microsoft-leads-global-action-against-favored-cybercrime-tool/ |
| [2] | Justice Department Seizes Domains Behind Major Information-Stealing Malware Operation | U.S. Department of Justice | 2025-05-21 | https://www.justice.gov/opa/pr/justice-department-seizes-domains-behind-major-information-stealing-malware-operation |
| [3] | Lumma Stealer: Breaking down the delivery techniques and capabilities of a prolific infostealer | Microsoft Security Blog | 2025-05-21 | https://www.microsoft.com/en-us/security/blog/2025/05/21/lumma-stealer-breaking-down-the-delivery-techniques-and-capabilities-of-a-prolific-infostealer/ |
| [4] | Lumma infostealer malware operation disrupted, 2,300 domains seized | BleepingComputer | 2025-05-21 | https://www.bleepingcomputer.com/news/security/lumma-infostealer-malware-operation-disrupted-2-300-domains-seized/ |
| [5] | Authorities Carry Out Elaborate Global Takedown of Infostealer Heavily Used by Cybercriminals | WIRED | 2025-05-21 | https://www.wired.com/story/lumma-stealer-takedown-disrupted/ |
