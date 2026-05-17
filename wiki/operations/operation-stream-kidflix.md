---
type: operation
title: "Operation Stream"
aliases:
  - "Operation Stream: Kidflix"
  - "Kidflix Takedown"
case_id: CYB-2025-001
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - seizure
  - arrest
outcome: success
timeframe:
  announced: 2025-04-04
  start: 2022-01-01
  end: 2025-03-11
  ongoing: false
crime_type: "[[csam-ic]]"
target_entity: "Kidflix, a large dark-web child sexual abuse material streaming platform"
lead_agency: "[[germany-bka|Bavarian State Criminal Police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[germany]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
  - "[[netherlands-politie]]"
legal_basis:

mechanisms_used:
  - "[[informal-cooperation]]"
results:
  arrests: 79
  indictments: 0
  servers_seized: 1
  domains_seized: 0
  cryptocurrency_seized: undisclosed
  decryption_keys_recovered: 0
  victims_notified: 39
  other:
    - "1,393 suspects were identified worldwide."
    - "More than 3,000 electronic devices were seized."
    - "The platform had 1.8 million registered users."
source_count: 5
sources:
  - "[[2025-04-04-europol-operation-stream-kidflix]]"
  - "[[2025-04-04_securityaffairs-com_operation-stream-kidflix]]"
  - "[[2025-04-03_politie-nl_kidflix-offline-gehaald]]"
  - "[[2025-04-02_bleepingcomputer-com_police-shuts-down-kidflix-child-sexual-exploitation-platform]]"
  - "[[2025-05-15_eucrim_pedophile-platform-kidflix-shut-down]]"
created: 2026-04-08
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
summary: "Operation Stream dismantled the Kidflix dark-web CSAM platform through a Germany-led, Europol-coordinated investigation with Dutch server action, identifying 1,393 suspects and producing 79 arrests worldwide."
jurisdictions:
  - "[[germany]]"
  - "[[netherlands]]"
organizations:
  - "[[germany-bka]]"
  - "[[europol-ec3]]"
  - "[[netherlands-politie]]"
crime_types:
  - "[[csam-ic]]"
related_operations:
  - "[[project-compass-the-com-network-2025]]"
  - "[[operation-fever-cbzc-eu-presidency-2025]]"
  - "[[europol-vidtf-2026-12-children-identified]]"
---
> [!note] Source basis
> This page is now grounded in a collected Europol-centered source wrapper, a Security Affairs summary, and an official Dutch police page confirming the Netherlands-side server action. It replaces an encoding-damaged draft that had no references section despite clear cross-border relevance.

## Summary

**Operation Stream** was a Germany-led, [[europol-ec3|Europol]]-coordinated operation that dismantled **Kidflix**, a major dark-web child sexual abuse material streaming platform. The public record supports a long-running investigation from 2022 to March 2025, a server takedown in the [[netherlands|Netherlands]], and worldwide suspect identification and arrests tied to the platform's financial and hosting infrastructure.

## Background

**Modus operandi.** Kidflix operated since 2021 as a *streaming-oriented* CSAM platform on the dark web — a structurally distinct model from the older download-and-forum CSAM platforms that dominated previous Europol takedowns. The Bavarian State Criminal Police (BLKA) and the Bavarian Central Office for the Prosecution of Cybercrime (ZCB) characterised Kidflix as a high-throughput video-streaming service modelled on legitimate adult-content streaming platforms, with categorised browsing, user accounts, and continuous-playback functionality. The platform monetised access through a cryptocurrency-based subscription / token system: users purchased tokens (primarily in Bitcoin and other cryptocurrencies) which unlocked viewing time, premium categories, and the ability to download videos. Uploaders received token rewards proportional to the views and downloads their uploaded content generated, creating a direct economic incentive to recruit and supply new CSAM. By the time of takedown the platform's library contained approximately **72,000 videos** hosted on a single high-capacity server located in the Netherlands. The catalogue grew through user uploads incentivised by the token-reward system, not through curated mass-import from prior CSAM repositories.

**Victim profile and impact.** The victims are children depicted in the CSAM content distributed through the platform. Europol's announcement reports that the operation directly resulted in the safeguarding of **39 children** — meaning children whose abuse was ongoing or recent and who could be identified, located, and removed from harmful situations as a result of investigative leads developed from Kidflix evidence. The platform's reach was global: **1.8 million registered users worldwide** had account access, and **1,393 suspects were identified** across more than 35 countries on the basis of platform usage data, payment trails, and uploader records. The harm therefore operates at two scales — (a) primary victimisation of the children depicted in the videos, with 39 confirmed safeguarded and an unknown larger universe of depicted children yet to be identified, and (b) the demand-side normalisation effect of 1.8 million accounts engaging with the streaming model.

**Financial flow.** Kidflix used cryptocurrency rails throughout the user-to-platform-to-uploader payment chain. Users purchased viewing tokens with Bitcoin and other cryptocurrencies via on-platform top-up flows, the platform held aggregated crypto balances in operator-controlled wallets, and uploader payouts were distributed in crypto. TRM Labs and Chainalysis-style blockchain analysis (referenced through Security Affairs/TRM Labs coverage) supported the multi-year financial tracing that identified the operators and a large fraction of high-value users. Specific cryptocurrency-seizure figures are recorded as **undisclosed** in the public record — Europol and the Dutch police press releases describe the financial tracing as central to suspect identification but do not publish the total seized BTC/ETH or USD-equivalent amount. The frontmatter therefore carries `cryptocurrency_seized: undisclosed` rather than a numeric value.

**Criminal organisation structure.** The Kidflix operator group is described in the public record as a small operational core running the streaming infrastructure, with a much larger "uploader" tier (incentivised users uploading CSAM in exchange for token rewards) and a passive paying-viewer tier (1.8 million accounts). The 79 arrests recorded under Operation Stream therefore span all three layers: (a) the platform operators (small number), (b) prolific uploaders (mid-sized number), and (c) high-engagement paying viewers / users with confirmed possession or production records (the majority). The exact split across the three tiers is not published. Europol's release does not assert that the operator core constitutes a named OCG with a hierarchical command structure — the model is closer to a "for-profit darknet service" run by a small operator team than to a traditional organised-crime hierarchy.

**Cross-border investigative cooperation** was led by Germany (BLKA and ZCB) with the Dutch National Police executing the physical server takedown on **2025-03-11** at German request — the server hosting the ~72,000 videos was physically located in Dutch jurisdiction. Europol coordinated suspect-identification dissemination to 35+ national LE partners through EC3 channels.

## Participating Parties

### Lead / Coordination
- [[germany-bka|Bavarian State Criminal Police and Bavarian cyber prosecutors]]
- [[europol-ec3|Europol EC3]]

### Confirmed Cross-Border Operational Role
- [[netherlands-politie|Dutch National Police]]

### Wider International Scope
- Europol-linked reporting states involvement of more than 35 countries.

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 79 |
| Suspects identified | 1,393 |
| Devices seized | 3,000+ |
| Children protected | 39 |
| Registered users | 1.8 million |
| Videos on seized server | about 72,000 |

## Cooperation Mechanisms Used

The public record supports a long-running multinational investigative model centered on Europol coordination, German lead investigation, and Dutch infrastructure action. Sources also indicate international financial tracing of cryptocurrency transactions through exchanges and related services, but they do not expose the full legal toolkit used for every country.

## Contradictions & Open Questions

- Public sources agree on the broad outcome but do not provide a complete list of the 35+ participating countries.
- The exact number of servers seized is not fully broken out publicly; current public reporting clearly supports at least the Netherlands-hosted server action.
- Court-stage case developments against identified users remain largely undisclosed.
- **Cryptocurrency seizure total is undisclosed.** Europol, Dutch police, and BLKA describe crypto-tracing as central to suspect identification but do not publish a numeric seized-funds figure. The frontmatter carries `cryptocurrency_seized: undisclosed` rather than a value.
- **Split of the 79 arrests across operator / uploader / viewer tiers is not published.** Tier-1 sources name the headline arrest count and the 1,393 globally-identified suspects but do not break out which fraction of arrests targeted operators versus prolific uploaders versus paying viewers.
- **Per-country arrest distribution** beyond the lead Germany and Netherlands roles is not published. The 79 arrests took place across more than 35 jurisdictions but only Germany and the Netherlands have named investigative roles in public statements.
- **Total identified-children pool** beyond the 39 confirmed safeguarded is not published. Whether the ~72,000 videos in the seized library have all been processed for victim identification, or whether processing is ongoing, is not stated.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol / Security Affairs / TRM Labs, 2025-04-04: Europol-led Operation Stream Takes Down Kidflix CSAM Platform.
- Security Affairs / TRM Labs, 2025-04-04: Operation Stream / Kidflix.
- Dutch National Police, 2025-04-03: Kinderpornografisch platform KidFlix offline gehaald.
- Security Affairs / TRM Labs, 2025-04-04: Europol-led Operation Stream Takes Down Kidflix CSAM Platform.
- BleepingComputer, 2025-04-02: Police shuts down KidFlix child sexual exploitation platform.
- eucrim, 2025-05-15: Pedophile Platform 'Kidflix' Shut Down.

## Operational Timeline

- 2022-01-01: activity or investigation start.
- 2025-04-04: public announcement.
- 2025-03-11: reported enforcement endpoint.
- 2025-04-02: public source coverage from BleepingComputer.
- 2025-04-03: public source coverage from Dutch National Police.
- 2025-04-04: public source coverage from Europol / Security Affairs / TRM Labs, Security Affairs / TRM Labs.
- 2025-05-15: public source coverage from eucrim.

## Legal and Procedural Posture

- Recorded crime classification: CSAM.
- Recorded enforcement posture: Takedown, Seizure, Arrest.
- The record is categorized as takedown with status completed.

## Evidence and Attribution Notes

- Operation Stream — Kidflix CSAM Platform Takedown An international law enforcement operation named "Operation Stream" dismantled Kidflix, one of the largest known child sexual abuse material (CSAM) streaming platforms on the dark web.
- The operation was led by the Bavarian State Criminal Police (Bayerisches Landeskriminalamt) and the Bavarian Central Office for the Prosecution of Cybercrime (ZCB), with coordination by Europol across 35 countries.
- **Platform: "** Kidflix — CSAM streaming platform operational since 2021"
- An international law enforcement operation named "Operation Stream" dismantled Kidflix, one of the largest known child sexual abuse material (CSAM) streaming platforms on the dark web.
- Source referenced by ic-statistics-dashboard.
- Dutch police confirm Netherlands-based server action on March 11, 2025 at Germany's request.
- The release confirms the platform had roughly 1.8 million users and that more than 1,400 users were identified globally.
- **Operation Stream** was a Germany-led, Europol-coordinated operation that dismantled **Kidflix**, a major dark-web child sexual abuse material streaming platform.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against Kidflix, a large dark-web child sexual abuse material streaming platform, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Bavarian State Criminal Police and coordination to Europol Ec3, with participating or affected jurisdictions recorded as Germany and Netherlands.

The cooperation model is documented through named agencies and partners: Germany Bka, Europol Ec3, Netherlands Politie; mechanisms: informal cooperation; enforcement posture: Takedown, Seizure, Arrest.

Operational results captured for the canonical record: 79 arrests; 1 servers seized; 39 victims notified; cryptocurrency/asset result recorded as undisclosed; 1,393 suspects were identified worldwide.; More than 3,000 electronic devices were seized.; The platform had 1.8 million registered users..

The canonical source set contains 6 reference(s): 2025 04 04 Europol Operation Stream Kidflix Takedown, 2025 04 04 Securityaffairs Com Operation Stream Kidflix, 2025 04 03 Politie Nl Kidflix Offline Gehaald, 2025 04 04 Europol Operation Stream Kidflix, 2025 04 02 Bleepingcomputer Com Police Shuts Down Kidflix Child Sexual Exploitation Platform, 2025 05 15 Eucrim Pedophile Platform Kidflix Shut Down.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol-led Operation Stream Takes Down Kidflix CSAM Platform | Security Affairs | 2025-04-04 | https://securityaffairs.com/176154/cyber-crime/europol-led-op-shuts-down-csam-platform-kidflix.html |
| [2] | Operation Stream / Kidflix | Security Affairs / TRM Labs | 2025-04-04 | https://securityaffairs.com/176270/cyber-crime/operation-stream-kidflix-takedown.html |
| [3] | Kinderpornografisch platform KidFlix offline gehaald | Dutch National Police | 2025-04-03 | https://www.politie.nl/nieuws/2025/april/2/11-kinderpornografisch-platform-kidflix-offline-gehaald.html |
| [4] | Police shuts down KidFlix child sexual exploitation platform | BleepingComputer | 2025-04-02 | https://www.bleepingcomputer.com/news/security/police-shuts-down-kidflix-child-sexual-exploitation-platform/ |
| [5] | Pedophile Platform 'Kidflix' Shut Down | eucrim | 2025-05-15 | https://eucrim.eu/news/pedophile-platform-kidflix-shut-down/ |
