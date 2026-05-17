---
type: operation
title: "Operation Talent"
aliases:
  - Talent
case_id: CYB-2025-011
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2025-01-30
  start: 2025-01-28
  end: 2025-01-30
  ongoing: false
crime_type: "[[hacking-ic]]"
target_entity: "Cracked and Nulled cybercrime forums and their supporting criminal services"
lead_agency: "[[germany-bka]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[germany]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[spain]]"
  - "[[greece]]"
  - "[[romania]]"
  - "[[italy]]"
  - "[[france]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
legal_basis:

mechanisms_used:
  - "[[informal-cooperation]]"
results:
  arrests: 2
  indictments: 0
  servers_seized: 17
  domains_seized: 12
  cryptocurrency_seized: "approximately EUR 300,000 in cash and crypto"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Cracked and Nulled had roughly 10 million registered user accounts combined."
    - "Associated services Sellix and StarkRDP were also disrupted."
    - "Searches were carried out at seven properties."
source_count: 5
sources:
  - "[[2025-01-30-europol-operation-talent]]"
  - "[[2025-01-30_justice-gov_cracked-and-nulled-marketplaces-disrupted-international-cyber-operation]]"
  - "[[2025-01-30_cybernews-com_cracked-and-nulled-seized-in-operation-talent]]"
  - "[[2025-01-31_infosecurity-magazine_operation-talent-cracked-nulled-dismantled]]"
  - "[[2025-01-31_bleepingcomputer-com_operation-talent-cracked-nulled]]"
created: 2026-04-08
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
summary: "Operation Talent was a Germany-led, Europol-supported international operation against the Cracked and Nulled cybercrime forums, producing two arrests, 17 server seizures, and broad evidence capture for follow-on investigations."
jurisdictions:
  - "[[germany]]"
  - "[[united-states]]"
  - "[[australia]]"
  - "[[spain]]"
  - "[[greece]]"
  - "[[romania]]"
  - "[[italy]]"
  - "[[france]]"
organizations:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[malware-ic]]"
---
> [!note] Source basis
> This page has been rebuilt from a malformed dual-frontmatter draft. It now rests on a BKA / Europol-side source page plus DOJ's official January 30, 2025 announcement.

## Summary

**Operation Talent** was a Germany-led, [[europol-ec3|Europol]]-supported international operation targeting the cybercrime forums **Cracked** and **Nulled**. Between 28 and 30 January 2025, authorities from eight countries took coordinated action against the two forums and related criminal services, producing arrests, domain and server seizures, and extensive evidence capture for follow-on international investigations.

## Background

### Modus operandi

Cracked and Nulled were two open-web English-language cybercrime forums that operated as one-stop marketplaces for entry-to-mid-tier cybercrime tooling and stolen data. The forums hosted:

- Stolen-data dumps (credential combos, banking and account data harvested from third-party breaches and infostealer logs).
- Malware-as-a-service offerings, exploit kits, remote-access trojans, and crypter / loader tooling.
- Hacking-tool catalogs (credential-stuffing tools, account-checkers, brute-force utilities).
- Fraud-service marketplaces (carding, SIM-swap services, fake-document and KYC-bypass services).
- AI-assisted attack tooling, named as a forum-content vertical in the public Europol/DOJ narrative — a feature distinguishing Cracked/Nulled from earlier-generation hacker forums (Hackforums, RaidForums) and aligning them with the post-LLM cybercrime-marketplace cohort.

Two supporting infrastructure services were disrupted in the same action: **Sellix**, a payment processor used by Nulled (the BKA characterisation), and **StarkRDP**, a remote desktop protocol (RDP) hosting service marketed and serviced through the same forums. Bundling a payment processor, an RDP infrastructure provider, and the two forum marketplaces in one synchronised takedown is the L26-relevant operational pattern: the action disrupted not just the marketplace front-ends but the financial-rails and bullet-proof infrastructure layers behind them.

### Victim profile and impact

The two forums had approximately 10 million registered user accounts combined at takedown — a scale figure that mixes legitimate lurkers, low-tier buyers, mid-tier sellers, and high-tier operators rather than identifying a discrete victim cohort. The downstream victim population is the credential holders, business email compromise (BEC) targets, fraud-victims, and breached-organisation customers whose data was traded through the forums. Public official reporting does not quantify aggregate fraud losses attributable to Cracked/Nulled listings, per-victim impact figures, or geographic concentration of downstream victims.

### Financial flow

Sellix — the payment-processor backbone behind Nulled — was named as a disrupted infrastructure component in the same action, indicating that the forum economy ran through a captive (or forum-controlled) payment-processing layer rather than purely peer-to-peer cryptocurrency. Approximately EUR 300,000 in cash and cryptocurrency was seized in the operation. The cited tier-1 sources do not disclose the breakdown between cash vs. crypto, the specific cryptocurrencies seized, or the wallet addresses traced; aggregate marketplace turnover and lifetime forum revenue are also not quantified.

### Criminal organization structure

Two arrests were made and seven properties were searched, with 17 servers and 12 domains plus related accounts seized. The cited tier-1 sources do not name the two arrested individuals, do not disclose their forum roles (administrator / moderator / Sellix-operator / StarkRDP-operator / both), and do not characterise the broader organisational structure of the two forum administrations. The Cracked and Nulled forums were operationally distinct platforms with separate administrative leadership, but the bundling of Sellix and StarkRDP in the same synchronised action — alongside the eight-country coordinated execution — implies that the two forum administrations and their supporting service providers were operationally linked at the infrastructure level, even if not legally consolidated into a single OCG in the cited release.

Public official reporting indicates that the forums were deeply embedded in the global underground economy rather than being marginal websites, which makes Operation Talent a meaningful infrastructure-disruption case rather than a single-platform seizure.

## Participating Parties

### Lead / Coordination
- [[germany-bka|Germany BKA]]
- [[europol-ec3|Europol EC3]]

### Confirmed Participating Countries
- [[germany|Germany]]
- [[united-states|United States]]
- [[australia|Australia]]
- [[spain|Spain]]
- [[greece|Greece]]
- [[romania|Romania]]
- [[italy|Italy]]
- [[france|France]]

### Confirmed U.S. Role
- [[us-doj|U.S. Department of Justice]]
- [[fbi-cyber-division|FBI]]

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 2 |
| Searches | 7 properties |
| Servers seized | 17 |
| Domains / accounts seized | 12 domains and related accounts reported by BKA |
| Cash / cryptocurrency | around EUR 300,000 |
| Scale of platforms | about 10 million registered user accounts combined |

## Cooperation Mechanisms Used

The sources clearly support synchronized multinational police action with Europol support and U.S. judicial involvement. The public record does not spell out the exact mutual legal assistance and evidence-transfer instruments, so this page confines itself to what is documented: Germany-led operational action, Europol support, and DOJ/FBI participation.

## Contradictions & Open Questions

- Public figures vary slightly across summaries on the exact count of accounts, domains, and seized services, but the core seizure narrative is consistent.
- Follow-on prosecutions against sellers and users of the forums are expected but not yet fully visible in public reporting.
- The extent of Europol's public-facing own announcement page remains underdocumented in the current source set; this page therefore leans on BKA and DOJ official anchors.
- **L26 gap — OCG identification**: the cited tier-1 sources do not name the two arrested individuals, do not disclose their forum roles (administrator / moderator / Sellix-operator / StarkRDP-operator), and do not characterise the relationship between the Cracked and Nulled forum administrations.
- **L26 gap — financial flow detail**: the EUR ~300,000 cash-and-crypto seizure is not disaggregated between cash and cryptocurrency, the specific cryptocurrencies seized are not named, and aggregate marketplace turnover or lifetime forum revenue figures are not disclosed.
- **L26 gap — victim quantification**: aggregate downstream fraud losses traceable to Cracked/Nulled listings, per-victim impact, and geographic concentration of downstream victims are not quantified in the cited release; the 10 million user-account figure mixes legitimate lurkers with operators and is not a victim count.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Germany BKA / Europol-supported operation, 2025-01-30: Operation Talent.
- U.S. Department of Justice, 2025-01-30: Cracked and Nulled Marketplaces Disrupted in International Cyber Operation.
- Cybernews, 2025-01-30: Cracked and Nulled seized in Operation Talent.
- Infosecurity Magazine, 2025-01-31: Operation Talent dismantles Cracked and Nulled.
- BleepingComputer, 2025-01-31: Operation Talent disrupts Cracked and Nulled cybercrime forums.

## Operational Timeline

- 2025-01-28: activity or investigation start.
- 2025-01-30: public announcement.
- 2025-01-30: reported enforcement endpoint.
- 2025-01-30: public source coverage from Cybernews, Germany BKA / Europol-supported operation, U.S. Department of Justice.
- 2025-01-31: public source coverage from BleepingComputer, Infosecurity Magazine.

## Legal and Procedural Posture

- Recorded crime classification: hacking and malware.
- Recorded enforcement posture: Arrest, Seizure, Takedown.
- The record is categorized as takedown with status completed.

## Evidence and Attribution Notes

- German authorities led an internationally coordinated action against Cracked and Nulled.
- The operation produced two arrests, 17 server seizures, and wide evidence capture.
- It confirms the U.S. role, the international coalition, and the disruption of Cracked and Nulled.
- Cybernews reported that Cracked and Nulled were seized in the Germany-led Operation Talent.
- The report noted related action against Sellix and StarkRDP and the scale of the two forums' user bases.
- Cybernews reported on the seizure of **Cracked** and **Nulled** under **Operation Talent**, including disruption of supporting services.
- Infosecurity Magazine reported that Operation Talent dismantled the Cracked and Nulled cybercrime forums.
- The article highlighted server seizures, arrests, and the involvement of Germany, the United States, and multiple European partners.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- U.S. Department of Justice, 2025-01-30: Victims Affected The Justice Department today announced its participation in a multinational operation involving actions in the United States, Romania, Australia, France, Germany, Spain, Italy, and Greece to disrupt and take down the infrastructure of the online cybercrime marketplaces known as Cracked and Nulled.
- U.S. Department of Justice, 2025-01-30: The operation was announced in conjunction with Operation Talent, a multinational law enforcement operation supported by Europol to investigate Cracked and Nulled.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against Cracked and Nulled cybercrime forums and their supporting criminal services, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Germany Bka and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Germany, United States, Australia, Spain, Greece, Romania, Italy, France.

The cooperation model is documented through named agencies and partners: Germany Bka, Europol Ec3, Fbi Cyber Division, Us Doj; mechanisms: informal cooperation; enforcement posture: Arrest, Seizure, Takedown.

Operational results captured for the canonical record: 2 arrests; 17 servers seized; 12 domains seized; cryptocurrency/asset result recorded as approximately EUR 300,000 in cash and crypto; Cracked and Nulled had roughly 10 million registered user accounts combined.; Associated services Sellix and StarkRDP were also disrupted.; Searches were carried out at seven properties..

The canonical source set contains 5 reference(s): 2025 01 30 Europol Operation Talent, 2025 01 30 Justice Gov Cracked And Nulled Marketplaces Disrupted International Cyber Operation, 2025 01 30 Cybernews Com Cracked And Nulled Seized In Operation Talent, 2025 01 31 Infosecurity Magazine Operation Talent Cracked Nulled Dismantled, 2025 01 31 Bleepingcomputer Com Operation Talent Cracked Nulled.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operation Talent | Germany BKA / Europol-supported operation | 2025-01-30 | https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2025/Presse2025/250130_Operation_Talent.html |
| [2] | Cracked and Nulled Marketplaces Disrupted in International Cyber Operation | U.S. Department of Justice | 2025-01-30 | https://www.justice.gov/opa/pr/cracked-and-nulled-marketplaces-disrupted-international-cyber-operation |
| [3] | Cracked and Nulled seized in Operation Talent | Cybernews | 2025-01-30 | https://cybernews.com/news/cracked-nulled-seized-operation-talent/ |
| [4] | Operation Talent dismantles Cracked and Nulled | Infosecurity Magazine | 2025-01-31 | https://www.infosecurity-magazine.com/news/operation-talent-cracked-nulled/ |
| [5] | Operation Talent disrupts Cracked and Nulled cybercrime forums | BleepingComputer | 2025-01-31 | https://www.bleepingcomputer.com/news/security/operation-talent-disrupts-cracked-and-nulled-cybercrime-forums/ |
