---
aliases:

case_id: CYB-2025-012
challenges_encountered:

coordinating_body: "[[interpol-igci]]"
created: 2026-04-08
credibility_index: 3.45
crime_type: "[[hacking-ic]]"
edges:

enforcement_type:

lead_agency: "[[interpol-igci]]"
legal_basis:

lessons_learned:

mechanisms_used:
  - "[[public-private-cooperation]]"
  - "[[electronic-evidence]]"

missing_fields:

operation_type: infrastructure-seizure
outcome: success
participating_agencies:
  - "[[interpol-igci]]"
  - "[[group-ib]]"
  - "[[kaspersky-lab]]"
  - "[[trend-micro]]"

participating_countries:
  - "[[brunei]]"
  - "[[cambodia]]"
  - "[[hong-kong]]"
  - "[[india]]"
  - "[[indonesia]]"
  - "[[japan]]"
  - "[[kazakhstan]]"
  - "[[laos]]"
  - "[[macau]]"
  - "[[malaysia]]"
  - "[[maldives]]"
  - "[[nepal]]"
  - "[[philippines]]"
  - "[[south-korea]]"
  - "[[singapore]]"
  - "[[sri-lanka]]"
  - "[[thailand]]"
  - "[[timor-leste]]"
  - "[[vietnam]]"
period: 3
related_cases:

related_operations:

results:
  arrests: 32
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:
    - "More than 20,000 malicious IPs and domains disrupted"
    - "100GB+ of data seized"
    - "Operation conducted across 26 Asia-Pacific countries"
    - "Private-sector intelligence support from Group-IB, Kaspersky, and Trend Micro"

  servers_seized: 41
  victims_notified: 216000
source_count: 3
source_tier: 2
sources:
  - "[[2025-04-01-interpol-operation-secure-infostealer]]"
  - "[[2025-04-01_kaspersky-com_kaspersky-supports-interpol-operation-secure]]"
  - "[[2025-04-01_helpnetsecurity-com_operation-secure-disrupts-global-infostealer-malware-operations]]"
status: completed
target_entity: "Infostealer malware infrastructure and operators across Asia-Pacific"
timeframe:
  announced: 2025-06-11
  end: 2025-04-30
  ongoing: false
  start: 2025-01-01
title: "Operation Secure (INTERPOL Infostealer Crackdown)"
title_ko: "Operation Secure (인포스틸러 인프라 단속)"
type: operation
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
summary: "Operation Secure was an INTERPOL-led operation conducted from January to April 2025 across 26 Asia-Pacific countries, targeting infostealer malware infrastructure. The operation resulted in 32 arrests, the takedown of over 20,000 malicious IPs and domains, the seizure of 41 servers and 100GB+ of data, and notifications to more than 216,000 victims."
organizations:
  - "[[interpol-igci]]"
  - "[[group-ib]]"
  - "[[kaspersky-lab]]"
  - "[[trend-micro]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[ransomware-ic]]"
  - "[[malware-ic]]"
---
# Operation Secure (INTERPOL Infostealer Crackdown)

## Summary

Operation Secure was an INTERPOL-led operation conducted from January to April 2025 across 26 Asia-Pacific countries, targeting infostealer malware infrastructure. The operation resulted in 32 arrests, the takedown of over 20,000 malicious IPs and domains, the seizure of 41 servers and 100GB+ of data, and notifications to more than 216,000 victims.

This operation focused specifically on information-stealing malware (infostealers) which harvest credentials, financial data, and personal information from infected systems. Private sector intelligence from Group-IB, Kaspersky, and Trend Micro supported the operation.

> [!note] Naming disambiguation
> This operation should not be confused with the Council of Europe's "Operation SECURE" capacity-building exercise (row 6 of Excel data), which was a training programme, not an enforcement operation.

## Background

### Modus operandi

Operation Secure targeted the infostealer-malware vertical — i.e., information-stealing trojans that infect victim endpoints (typically via phishing, cracked-software lures, malvertising, or drive-by downloads) and exfiltrate browser-stored credentials, browser cookies and session tokens, autofill data, cryptocurrency wallet seeds, email account credentials, and locally cached document and form data to an attacker-controlled command-and-control (C2) server. The harvested credential bundles ("logs") are then resold on cybercrime marketplaces as Initial Access Broker (IAB) inventory feeding ransomware, business email compromise, account takeover, and crypto-asset theft pipelines. The cited tier-1 INTERPOL release does not name specific malware families, but Kaspersky's same-day support release contextualises the operation against the broader Lumma / Redline / Meta / Risepro infostealer family ecosystem that this wiki tracks separately under [[operation-magnus-redline-meta-stealer-takedown-2024|Operation Magnus]] and related actions.

The operation hit infrastructure-layer assets rather than end-user devices: 20,000-plus malicious IPs and domains were taken down, 41 servers were seized, and 100 GB-plus of data was captured for evidence. The action targeted both the C2 infrastructure (for live exfiltration sessions) and the resale-platform infrastructure where infostealer logs are sold.

### Victim profile and impact

INTERPOL reports that 216,000-plus victims were notified through the operation. The cited release does not break down victims by country, by language of credentials harvested, or by downstream fraud-loss figure. Given the Asia-Pacific operational footprint (26 jurisdictions), the credential population is likely heavily weighted toward Asia-Pacific regional users — including Korean residents whose credentials are an upstream supply for voice-phishing, romance-scam, and account-takeover schemes tracked elsewhere in this wiki. Aggregate fraud losses across the notified victim cohort are not quantified in the cited source.

### Financial flow

Infostealer-economy proceeds flow primarily through:

1. Per-log sales (typical 1-25 USD per credential bundle on resale marketplaces such as Russian Market, 2easy, Genesis-style platforms),
2. IAB resale of corporate-credential bundles to ransomware operators (which can monetise at five-to-seven figures per ransom event), and
3. Direct monetisation of harvested crypto-wallet seeds and exchange-account credentials.

The cited INTERPOL release records no cryptocurrency-seizure figure for Operation Secure and does not disaggregate proceeds by monetisation channel. The 100 GB of seized data is evidentiary, not laundered-proceeds.

### Criminal organization structure

The 32 arrests are reported as a cohort total across the 26-country roster; the cited tier-1 source does not name specific OCGs, malware-family operators, marketplace administrators, or per-country arrest breakdowns. Infostealer ecosystems are typically structured as loosely federated affiliates — malware-as-a-service (MaaS) operators selling stealer builds, affiliate distributors running spam/phishing campaigns, log-aggregator marketplaces, and downstream IAB resellers — rather than as integrated hierarchies. The release does not disclose which tier or role the 32 arrested individuals occupied, nor whether they include MaaS operators, infrastructure providers, or log resellers.

Infostealers serve as the initial access vector for ransomware, fraud, and identity theft operations. INTERPOL's Asia-South Pacific Cybercrime Operations Desk coordinated this region-wide crackdown as a successor to the [[operation-synergia-ii|Operation Synergia II]] model of large-scale infrastructure takedowns.

## Participating Parties

### Law Enforcement
- **Lead**: [[interpol-igci|INTERPOL]] (Asia-South Pacific Cybercrime Operations Desk)
- **26-country Asia-Pacific coalition reported by INTERPOL**: Brunei, Cambodia, Fiji, Hong Kong (China), India, Indonesia, Japan, Kazakhstan, Kiribati, [[south-korea|South Korea]], Laos, Macau (China), Malaysia, Maldives, Nauru, Nepal, Papua New Guinea, Philippines, Samoa, Singapore, Solomon Islands, Sri Lanka, Thailand, Timor-Leste, Tonga, Vanuatu, Vietnam. INTERPOL labels the effort as 26-country; its public list contains several territories/regions, so country-page metadata tracks the subset with existing country records while the full public list is preserved here.

### Private Sector Partners
- Group-IB
- Kaspersky
- Trend Micro

## Results and Impact

| Metric | Value |
|--------|-------|
| Arrests | 32 |
| Servers seized | 41 |
| Malicious IPs/domains taken down | 20,000+ |
| Data seized | 100GB+ |
| Victims notified | 216,000+ |
| Countries | 26 |

## Cooperation Mechanisms Used

> [!warning] Missing data
> Specific legal frameworks and cooperation mechanisms not detailed in available source. Likely INTERPOL I-24/7 network and bilateral cooperation agreements.

## Korean Involvement (한국의 참여)

South Korea (대한민국) is named verbatim in the INTERPOL 2025-06-11 announcement as one of the 26 cooperating Asia-Pacific jurisdictions for Operation Secure. The cited tier-1 source does not break down which Korean agency or operational unit participated, what number of Korean infostealer infrastructure assets were affected by takedown actions, or what fraction of the 216 000+ notified victims were Korean residents. Likely Korean coordinating channels include the [[knpa|Korean National Police Agency]] and the [[knpa-cyber-bureau|KNPA Cyber Bureau]], which is the routine Korean point-of-contact for INTERPOL-coordinated cyber operations and for the Asia and South Pacific Joint Operations Against Cybercrime (ASPJOC) project under which Operation Secure was organised.

The case is a strong infostealer-IC datapoint for Korea given that infostealer-derived credentials are a recurring upstream supply for Korean voice-phishing, romance-scam, and account-takeover schemes tracked elsewhere in this wiki.

## Contradictions & Open Questions

- Per-country breakdown of arrests and infrastructure actions not disclosed in the cited tier-1 source. The 32 arrests, 41 servers, 100 GB+ of seized data, and 20 000+ disrupted IPs/domains are reported as cohort totals.
- **L26 gap — modus operandi specificity**: the cited INTERPOL release does not name specific malware families targeted (Lumma, RedLine, Meta, RisePro, Raccoon, Vidar, etc.); the operation is described at the "infostealer infrastructure" abstraction level only.
- **L26 gap — financial flow**: the cited release does not quantify infostealer-log resale proceeds, IAB downstream monetisation, or aggregate ransomware-attributable losses traceable to logs sourced through the seized infrastructure.
- **L26 gap — OCG structure**: the 32 arrested individuals' roles (MaaS operators / infrastructure providers / marketplace administrators / affiliate distributors) are not disclosed; whether the 32-arrest cohort represents a coordinated OCG or independent actors across 26 jurisdictions is unspecified.
- **L26 gap — victim quantification**: per-jurisdiction victim breakdown, language/region of harvested credentials, and downstream fraud-loss aggregates across the 216 000-plus notified population are not disclosed.
- The wiki record's `participating_countries` frontmatter currently captures the 19 jurisdictions in the 26-country INTERPOL roster that have existing country pages in this wiki: Brunei, Cambodia, Hong Kong, India, Indonesia, Japan, Kazakhstan, Laos, Macau, Malaysia, Maldives, Nepal, Philippines, South Korea, Singapore, Sri Lanka, Thailand, Timor-Leste, and Vietnam. The remaining 7 source-named jurisdictions — Fiji, Kiribati, Nauru, Papua New Guinea, Samoa, Solomon Islands, Tonga, and Vanuatu — are named verbatim in the cited INTERPOL release but do not yet have country pages in this wiki and are therefore listed in the prose roster only. (Counted as 8 entries; the eighth Pacific entry, Macau, is treated as a Chinese region in INTERPOL's text and is captured separately above.)
- Legal basis for cross-border data sharing across 26 jurisdictions is not specified in the cited tier-1 source; the standing Asia-South Pacific Joint Operations Against Cybercrime (ASPJOC) project structure is the operational frame named in same-day INTERPOL coverage.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- INTERPOL, 2025-06-11: 20,000 malicious IPs and domains taken down in INTERPOL infostealer crackdown.
- Kaspersky, 2025-06-11: Operation Secure: Kaspersky supports INTERPOL in curbing infostealer threat.
- Help Net Security, 2025-06-11: Infostealer crackdown: Operation Secure takes down 20,000 malicious IPs and domains.

## Operational Timeline

- 2025-01-01: activity or investigation start.
- 2025-06-11: public announcement.
- 2025-04-30: reported enforcement endpoint.
- 2025-06-11: public source coverage from Help Net Security, INTERPOL, and Kaspersky.

## Legal and Procedural Posture

- Recorded crime classification: hacking, ransomware, malware.
- The record is categorized as infrastructure-seizure with status completed.

## Evidence and Attribution Notes

- INTERPOL reported that Operation Secure ran from January to April 2025 and was publicly announced on 2025-06-11.
- Operation Secure was an INTERPOL-led operation conducted from January to April 2025 across 26 Asia-Pacific countries, targeting infostealer malware infrastructure.
- The operation resulted in 32 arrests, the takedown of over 20,000 malicious IPs and domains, the seizure of 41 servers and 100GB+ of data, and notifications to more than 216,000 victims.
- Kaspersky described Operation Secure as an Asia-Pacific crackdown on infostealer infrastructure across 26 countries.
- The release attributed 20,000-plus malicious IPs and domains disrupted and more than 216,000 victim notifications to the operation.
- Kaspersky described **Operation Secure** as a 26-country Asia-Pacific enforcement action against infostealer infrastructure.
- Help Net Security reported the same 20,000-plus takedown figure, 41 server seizures, 32 arrests, and 216,000 victim notifications.

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against Infostealer malware infrastructure and operators across Asia-Pacific, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Interpol Igci and coordination to Interpol Igci, with participating or affected jurisdictions recorded as India, Indonesia, Japan, South Korea, Singapore, Thailand.

The cooperation model is visible primarily through the lead/coordinating agencies and country list; detailed legal mechanism fields remain sparse.

Operational results captured for the canonical record: 32 arrests; 41 servers seized; 216000 victims notified.

The canonical source set contains 3 reference(s): 2025 04 01 Interpol Operation Secure Infostealer, 2025 04 01 Kaspersky Com Kaspersky Supports Interpol Operation Secure, 2025 04 01 Helpnetsecurity Com Operation Secure Disrupts Global Infostealer Malware Operations.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 20,000 malicious IPs and domains taken down in INTERPOL infostealer crackdown | INTERPOL | 2025-06-11 | https://www.interpol.int/en/News-and-Events/News/2025/20-000-malicious-IPs-and-domains-taken-down-in-INTERPOL-infostealer-crackdown |
| [2] | Operation Secure: Kaspersky supports INTERPOL in curbing infostealer threat | Kaspersky | 2025-06-11 | https://www.kaspersky.com/about/press-releases/operation-secure-kaspersky-supports-interpol-in-curbing-infostealer-threat |
| [3] | Infostealer crackdown: Operation Secure takes down 20,000 malicious IPs and domains | Help Net Security | 2025-06-11 | https://www.helpnetsecurity.com/2025/06/11/operation-secure-cybercrime-infostealer-crackdown/ |
