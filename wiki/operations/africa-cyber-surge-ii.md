---
type: operation
title: "Africa Cyber Surge II"
title_ko: "아프리카 사이버 서지 II"
aliases:
  - "Africa Cyber Surge 2"
  - "ACS II"
case_id: CYB-2023-050
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - takedown
outcome: success
timeframe:
  announced: 2023-08-18
  start: 2023-04-01
  end: 2023-08-01
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "Cybercrime networks tied to phishing, BEC, romance fraud, and related illicit infrastructure across 25 African countries"
lead_agency: "[[interpol]]"
coordinating_body: "[[interpol]]"
participating_countries:
  - "[[cameroon]]"
  - "[[gambia]]"
  - "[[kenya]]"
  - "[[mauritius]]"
  - "[[nigeria]]"
  - "[[south-africa]]"
  - "[[tanzania]]"
participating_agencies:
  - "[[interpol]]"
  - "[[afripol]]"
legal_basis:
  - "INTERPOL-AFRIPOL operational cooperation"
  - "domestic cybercrime authorities of participating countries"
mechanisms_used:
  - "[[informal-cooperation]]"
  - "[[public-private-cooperation]]"
  - "regional capacity-building coordination"
results:
  arrests: 14
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "25 African countries participated."
    - "INTERPOL reported 20,674 suspicious cyber networks identified."
    - "Reported losses linked to the activity exceeded USD 40 million."
edges:
  - source_actor: "INTERPOL"
    target_actor: "AFRIPOL"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 4.12
source_tier: 1
missing_fields:
  - complete_participating_countries
related_cases: []
related_operations:
  - "[[operation-red-card]]"
  - "[[operation-first-light-2024]]"
  - "[[operation-jackal]]"
challenges_encountered: []
lessons_learned:
  - "Pan-African cyber operations need both operational takedown capacity and sustained training support."
  - "Regional announcements should be paired with country-level follow-on reporting to preserve traceability."
source_count: 5
sources:
  - "[[2023-08-18_interpol_cybercrime-14-arrests-thousands-of-illicit-cyber-networks-disrupted-in-africa-operation]]"
  - "[[2023-06-30_coe_glacy-supports-interpols-africa-cyber-surge-operation-ii]]"
  - "[[2023-08-18_group-ib_africa-cyber-surge-ii]]"
  - "[[2023-08-18_kaspersky_assists-interpol-in-operation-to-disrupt-cybercrime-in-african-countries]]"
  - "[[2023-08-18_therecord-media_africa-cyber-surge-14-arrests-interpol]]"
created: 2026-04-08
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
summary: "Africa Cyber Surge II was an INTERPOL-AFRIPOL operation across 25 African countries that produced 14 arrests, mapped more than 20,000 suspicious networks, and linked over USD 40 million in losses to cyber-enabled crime."
jurisdictions:
  - "[[cameroon]]"
  - "[[gambia]]"
  - "[[kenya]]"
  - "[[mauritius]]"
  - "[[nigeria]]"
  - "[[south-africa]]"
  - "[[tanzania]]"
organizations:
  - "[[interpol]]"
  - "[[afripol]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[bec-ic]]"
---
> [!note] Source basis
> This page is now anchored to INTERPOL's official release and supplemented by Council of Europe, Group-IB, Kaspersky, and The Record coverage. The file was also rebuilt from a broken frontmatter state to restore structural integrity.

## Summary

**Africa Cyber Surge II** was a major [[interpol|INTERPOL]]-[[afripol|AFRIPOL]] operation spanning 25 African countries. INTERPOL reported 14 arrests, the identification of 20,674 suspicious cyber networks, and linked losses exceeding USD 40 million across schemes involving phishing, business email compromise, digital extortion, and online fraud.

## Background

### Modus operandi

The 25-country sweep targeted a mixed portfolio of cyber-enabled fraud and supporting criminal infrastructure rather than a single malware family. INTERPOL's release identifies four crime patterns disrupted during the four-month action window (April–August 2023): business email compromise (BEC), phishing kits and credential-harvesting pages, romance and investment fraud, and high-volume malware-hosting infrastructure used to support those schemes. Country-specific examples disclosed by INTERPOL include a Cameroon-based art-sale fraud ring that defrauded victims of approximately USD 850,000, and Kenyan operators of bulk malware-hosting services. Across the operation, 1,442 malicious IP addresses, domains, and servers used to support these schemes were taken down and 20,674 suspicious cyber networks were mapped — meaning the dominant criminal tradecraft was distributed online-fraud infrastructure (mule/phishing/host nodes) rather than centralized ransomware-style intrusion.

### Victim profile and impact

Tier-1 reporting attributes more than USD 40 million in linked financial losses to the networks disrupted during the operation window, but does not publish a per-victim or per-country breakdown. Victims of the named Cameroon art-sale fraud were buyers of high-value items targeted by impersonation; victims of the BEC/phishing/romance components reach across Africa and to extra-regional residents whose funds were routed through African mule infrastructure, but tier-1 sources do not disclose victim counts.

### Financial flow

INTERPOL's release totals the USD 40 million figure as financial losses linked to the identified networks. The release does not disclose how funds were laundered, what share was recovered, or what crypto/cash-out pathway each scheme used.

### Criminal organization structure

Tier-1 sources describe the 14 arrests as distributed across multiple participating African countries and tied to multiple separate criminal cells rather than to one named transnational organization. INTERPOL discloses arrest counts at country level (e.g., 3 arrests in Cameroon for art-sale fraud) but does not publish ringleader names, group hierarchies, nationalities of accused, or evidence that the disrupted cells coordinated with each other.

## Participating Parties

### Coordinating Bodies
- [[interpol|INTERPOL]]
- [[afripol|AFRIPOL]]

### Confirmed Participating Countries Mentioned in Public Reporting
- [[cameroon|Cameroon]]
- [[gambia|Gambia]]
- [[kenya|Kenya]]
- [[mauritius|Mauritius]]
- [[nigeria|Nigeria]]
- [[south-africa|South Africa]]
- [[tanzania|Tanzania]]

> [!warning] Scope note
> INTERPOL disclosed that 25 African countries participated, but the complete public country list was not included in the anchor release. This page only lists countries explicitly supported by the cited material.

## Legal Framework

Public reporting does not enumerate the precise domestic statutes used in each participating country. What is clear is that the operation relied on INTERPOL-AFRIPOL coordination, national police action, and training or support channels reinforced by external partners such as the Council of Europe and private-sector cyber firms.

## Operational Timeline

| Date | Event |
|------|-------|
| 2023-04 | Operation period begins across participating African countries. |
| 2023-06-30 | Council of Europe GLACY+ publicly notes support to Africa Cyber Surge II. |
| 2023-08-01 | Reported operation window ends. |
| 2023-08-18 | INTERPOL announces the operation's results. |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 14 |
| Participating countries | 25 |
| Suspicious cyber networks identified | 20,674 |
| Reported losses linked | More than USD 40 million |

## Cooperation Mechanisms Used

Africa Cyber Surge II combined supranational coordination with operational assistance and capacity building. INTERPOL and AFRIPOL handled the regional orchestration, while partner organizations helped train investigators and supply threat-intelligence context. That matters because pan-African operations often fail if tactical disruption is not matched by investigator training and sustained regional coordination.

## Contradictions & Open Questions

- Public reporting is consistent on the headline metrics, but it does not disclose a full list of all 25 participating states.
- Arrest counts are clear; prosecution and conviction outcomes remain opaque at the country level.
- It remains unclear how many of the 20,674 suspicious networks were directly remediated versus only mapped or referred onward.
- **L26 gap — victim profile:** tier-1 sources do not publish per-scheme victim counts (only an aggregate USD 40M loss figure and one named USD 850K Cameroon case).
- **L26 gap — financial flow:** tier-1 sources do not disclose laundering pathways, asset-recovery share, or per-scheme cash-out mechanics.
- **L26 gap — OCG structure:** tier-1 sources name no ringleaders, no nationalities of accused, and provide no evidence the disrupted cells coordinated with each other beyond shared crime patterns.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- INTERPOL, 2023-08-18: Cybercrime: 14 arrests, thousands of illicit cyber networks disrupted in Africa operation.
- Council of Europe, 2023-06-30: GLACY+ supports INTERPOL’s Africa Cyber Surge Operation II.
- Group-IB, 2023-08-18: Group-IB makes key contribution to INTERPOL-led Africa Cyber Surge II operation, leading to arrests of 14 suspects.
- Kaspersky, 2023-08-18: Kaspersky assists INTERPOL in operation to disrupt cybercrime in African countries.
- The Record, 2023-08-18: Africa Cyber Surge 14 Arrests Interpol.

## Evidence and Attribution Notes

- INTERPOL and AFRIPOL coordinated Africa Cyber Surge II across 25 African countries.
- The operation led to 14 arrests, the identification of 20,674 suspicious cyber networks, and the reporting of more than USD 40 million in linked losses.
- INTERPOL listed concrete operational highlights in Cameroon, Nigeria, Mauritius, Gambia, and Kenya.
- This is the anchor official source for Africa Cyber Surge II.
- The Council of Europe documented its GLACY+ support for the Africa Cyber Surge II tabletop exercise and operational preparation in Tanzania.
- The page confirms the training and capacity-building layer that preceded the action phase.
- This Council of Europe page is valuable because it shows the preparatory capacity-building and training work behind Africa Cyber Surge II.
- Group-IB described its intelligence contribution to Africa Cyber Surge II.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- INTERPOL, 2023-08-18: Cybercrime: 14 arrests, thousands of illicit cyber networks disrupted in Africa operation Networks identified linked to financial losses of more than USD 40 million DAR ES SALAM, Tanzania – INTERPOL and AFRIPOL have coordinated an operation across 25 African countries that enabled investigators to arrest 14 suspected cybercriminals and.
- INTERPOL, 2023-08-18: The four-month Africa Cyber Surge II operation was launched in April 2023 and focused on identifying cybercriminals and compromised infrastructure.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a arrest-sweep against Cybercrime networks tied to phishing, BEC, romance fraud, and related illicit infrastructure across 25 African countries, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Interpol and coordination to Interpol, with participating or affected jurisdictions recorded as Cameroon, Gambia, Kenya, Mauritius, Nigeria, South Africa, Tanzania.

The cooperation model is documented through named agencies and partners: Interpol and Afripol; enforcement posture: Arrest and Takedown.

Operational results captured for the canonical record: 14 arrests; 25 African countries participated.; INTERPOL reported 20,674 suspicious cyber networks identified.; Reported losses linked to the activity exceeded USD 40 million..

The canonical source set contains 5 reference(s): 2023 08 18 Interpol Cybercrime 14 Arrests Thousands Of Illicit Cyber Networks Disrupted In Africa Operation, 2023 06 30 Coe Glacy Supports Interpols Africa Cyber Surge Operation Ii, 2023 08 18 Group Ib Africa Cyber Surge Ii, 2023 08 18 Kaspersky Assists Interpol In Operation To Disrupt Cybercrime In African Countries, 2023 08 18 Therecord Media Africa Cyber Surge 14 Arrests Interpol.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis, Mechanisms Used, Complete Participating Countries.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Cybercrime: 14 arrests, thousands of illicit cyber networks disrupted in Africa operation | INTERPOL | 2023-08-18 | https://www.interpol.int/en/News-and-Events/News/2023/Cybercrime-14-arrests-thousands-of-illicit-cyber-networks-disrupted-in-Africa-operation |
| [2] | GLACY+ supports INTERPOL's Africa Cyber Surge Operation II | Council of Europe | 2023-06-30 | https://www.coe.int/en/web/cybercrime/-/glacy-supports-interpol-s-africa-cyber-surge-operation-ii |
| [3] | Africa Cyber Surge II | Group-IB | 2023-08-18 | https://www.group-ib.com/media-center/press-releases/africa-cyber-surge-ii/ |
| [4] | Kaspersky assists INTERPOL in operation to disrupt cybercrime in African countries | Kaspersky | 2023-08-18 | https://usa.kaspersky.com/about/press-releases/kaspersky-assists-interpol-in-operation-to-disrupt-cybercrime-in-african-countries |
| [5] | INTERPOL-led Africa Cyber Surge II operation leads to 14 arrests | The Record | 2023-08-18 | https://therecord.media/africa-cyber-surge-14-arrests-interpol |
