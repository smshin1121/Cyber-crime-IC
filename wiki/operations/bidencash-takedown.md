---
type: operation
title: "BidenCash Marketplace Seizure"
title_ko: "BidenCash 마켓플레이스 압수"
aliases:
  - "BidenCash Takedown"
  - "BidenCash Domain Seizure"
case_id: ""
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - takedown
  - asset_freeze
outcome: success
timeframe:
  announced: 2025-06-05
  start: 2025-05-27
  end: 2025-06-05
  ongoing: false
crime_type: "[[carding-fraud-ic]]"
target_entity: "BidenCash carding marketplace (dark web and clearnet domains)"
lead_agency: "[[us-secret-service|US Secret Service]]"
coordinating_body: "[[us-doj|US Department of Justice]]"
participating_countries:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[finland]]"
  - "[[germany]]"
  - "[[france]]"
  - "[[denmark]]"
participating_agencies:
  - "[[us-doj|US Department of Justice]]"
  - "[[us-secret-service|US Secret Service]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[netherlands-politie|Dutch National High Tech Crime Unit]]"
  - "[[europol-ec3|Europol EC3]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention]]"
  - "[[mutual-legal-assistance|Mutual Legal Assistance]]"
mechanisms_used:
  - "[[mutual-legal-assistance|MLAT Process]]"
  - "[[public-private-cooperation|Public-Private Cooperation]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 145
  cryptocurrency_seized: "undisclosed amount"
  other:
    - "145 darknet and clearnet domains seized"
    - "Cryptocurrency funds seized"
    - "Marketplace supported 117,000+ customers"
    - "15 million+ payment card numbers trafficked"
    - "USD 17 million+ in marketplace revenue"
edges:
  - source_actor: "US Secret Service"
    target_actor: "Dutch NHTCU"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: directed
  - source_actor: FBI
    target_actor: "US Secret Service"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "US Secret Service"
    target_actor: "Searchlight Cyber"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
  - source_actor: "US Secret Service"
    target_actor: "Shadowserver Foundation"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - case_id
  - arrests
  - "cryptocurrency_seized (exact amount)"
related_cases:
  - "[[in-re-bidencash-marketplace-seizure]]"
related_operations:
  - "[[operation-endgame|Operation Endgame]]"
  - "[[rydox-marketplace-takedown|Rydox Marketplace Takedown]]"
  - "[[operation-in-re-bidencash-marketplace-seizure]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Cross-border domain seizure coordination]]"
  - "[[data-sovereignty|Data sovereignty across multiple hosting jurisdictions]]"
lessons_learned:
  - "Coordinated multi-country domain seizure can effectively shut down distributed dark web infrastructure"
  - "Public-private partnerships with dark web intelligence firms enhance takedown capabilities"
  - "Domain seizure without arrests leaves operators potentially able to reconstitute"
source_count: 5
sources:
  - "[US Secret Service Press Release (2025-06-05)](https: "//www.secretservice.gov/newsroom/releases/2025/06/us-government-seizes-approximately-145-criminal-marketplace-domains)\""
  - "[DOJ Press Release via Fortune (2025-06-05)](https: "//fortune.com/crypto/2025/06/05/doj-seizes-crypto-web-domains-online-marketplace-bidencash/)\""
  - "[The Record (2025-06)](https: "//therecord.media/bidencash-cybercrime-darknet-market-takedown-us-netherlands)\""
  - "[The Hacker News (2025-06)](https: "//thehackernews.com/2025/06/doj-seizes-145-domains-tied-to.html)\""
  - "[Help Net Security (2025-06-06)](https: "//www.helpnetsecurity.com/2025/06/06/bidencash-marketplace-domains-seized/)\""
created: 2026-04-10
updated: 2026-04-11
operation_role: umbrella
parent_operation: ""
summary: "On 5 June 2025, the US Attorney's Office for the Eastern District of Virginia announced the seizure of approximately 145 domains (both darknet and clearnet) and cryptocurrency funds associated with the BidenCash criminal marketplace. The operation was led by the [[us-secret-service|US Secret Service]] Frankfurt Resident Office and Cyber Investigative Section, together with the [[fbi-cyber-division|FBI]] Albuquerque Field Office, and coordinated by the [[us-doj|US Department of Justice]]. International partners included the [[netherlands-politie|Dutch National High Tech Crime Unit]] and private-sector firms Searchlight Cyber and The Shadowserver Foundation. The seized domains were redirected to a US law enforcement-controlled server. BidenCash, which had operated since March 2022, had served over 117,000 customers, facilitated the trafficking of more than 15 million payment card numbers, and generated over USD 17 million in revenue. The seizure was part of the broader [[operation-endgame|Operation Endgame]] framework. No arrests were announced as of the seizure date."
jurisdictions:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[finland]]"
  - "[[germany]]"
  - "[[france]]"
  - "[[denmark]]"
organizations:
  - "[[us-secret-service|US Secret Service]]"
  - "[[us-doj|US Department of Justice]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[netherlands-politie|Dutch National High Tech Crime Unit]]"
  - "[[europol-ec3|Europol EC3]]"
crime_types:
  - "[[carding-fraud-ic]]"
---
## Summary

On 5 June 2025, the US Attorney's Office for the Eastern District of Virginia announced the seizure of approximately 145 domains (both darknet and clearnet) and cryptocurrency funds associated with the BidenCash criminal marketplace. The operation was led by the [[us-secret-service|US Secret Service]] Frankfurt Resident Office and Cyber Investigative Section, together with the [[fbi-cyber-division|FBI]] Albuquerque Field Office, and coordinated by the [[us-doj|US Department of Justice]]. International partners included the [[netherlands-politie|Dutch National High Tech Crime Unit]] and private-sector firms Searchlight Cyber and The Shadowserver Foundation. The seized domains were redirected to a US law enforcement-controlled server. BidenCash, which had operated since March 2022, had served over 117,000 customers, facilitated the trafficking of more than 15 million payment card numbers, and generated over USD 17 million in revenue. The seizure was part of the broader [[operation-endgame|Operation Endgame]] framework. No arrests were announced as of the seizure date.

## Background

### BidenCash Marketplace

BidenCash was a dark web marketplace specializing in the sale of stolen payment card data and associated personally identifiable information (PII). Launched in March 2022, it quickly became one of the most prominent carding platforms by offering:

- **Stolen credit and debit card numbers** with full details (card number, expiration, CVV, cardholder name, address)
- **Personal identification information** linked to card holders
- A user-friendly interface that simplified the process of buying and selling stolen data
- Both darknet (.onion) and clearnet mirror domains for accessibility

The marketplace gained notoriety in October 2022 when it publicly released approximately 1.2 million stolen credit card records as a "promotion" to attract new customers. This tactic was repeated on subsequent occasions, with millions of cards dumped publicly.

By the time of its seizure, BidenCash had:

| Metric | Value |
|--------|-------|
| Active customers | 117,000+ |
| Payment cards trafficked | 15 million+ |
| Revenue generated | USD 17 million+ |
| Operating period | March 2022 - June 2025 (~3 years) |

### Operation Endgame Context

The BidenCash seizure occurred as part of a coordinated multi-national action week beginning 27 May 2025, under the [[operation-endgame|Operation Endgame]] umbrella. [[operation-endgame|Operation Endgame]] is a Europol-led initiative focused on dismantling cybercrime infrastructure. On the same day as the BidenCash seizure, authorities from the [[united-states|US]], [[netherlands|Netherlands]], [[finland|Finland]], [[germany|Germany]], [[france|France]], and [[denmark|Denmark]] took coordinated actions against several criminal domain infrastructures.

## Participating Parties

### US Agencies

| Agency | Role |
|--------|------|
| [[us-doj|US DOJ]], Eastern District of Virginia | Prosecuting authority; obtained seizure warrants |
| [[us-secret-service|US Secret Service]], Frankfurt Resident Office | Lead investigative agency |
| [[us-secret-service|US Secret Service]], Cyber Investigative Section | Technical investigation |
| [[fbi-cyber-division|FBI]], Albuquerque Field Office | Co-investigating agency |

### International Partners

| Country | Entity | Role |
|---------|--------|------|
| [[netherlands]] | [[netherlands-politie|Dutch National High Tech Crime Unit]] | Domain seizure assistance; infrastructure takedown |
| [[finland]] | Finnish law enforcement | Coordinated action (under Operation Endgame umbrella) |
| [[germany]] | German law enforcement | Coordinated action |
| [[france]] | French law enforcement | Coordinated action |
| [[denmark]] | Danish law enforcement | Coordinated action |

### Private Sector

| Entity | Role |
|--------|------|
| Searchlight Cyber | Dark web intelligence and investigation support |
| The Shadowserver Foundation | Technical assistance with infrastructure identification |

> [!note] Participant scope
> Finland, Germany, France, and Denmark are listed as participating countries based on the coordinated Endgame action week. Their specific contributions to the BidenCash seizure itself vs. other concurrent Endgame actions are not fully delineated in public reporting. The direct bilateral cooperation for BidenCash was primarily US-Netherlands.

## Legal Framework

- **US federal seizure warrants**: The US Attorney for the Eastern District of Virginia obtained warrants authorizing the seizure of 145 domains and cryptocurrency
- **[[mutual-legal-assistance|Mutual Legal Assistance]]**: Coordination with [[netherlands|Dutch]] authorities for domain infrastructure located in or routed through the Netherlands
- **[[budapest-convention|Budapest Convention]]**: Likely provided the framework for cross-border cooperation, given that all participating states are parties
- **18 U.S.C. ss 1029** (fraud and related activity in connection with access devices): The primary US statute addressing trafficking in stolen payment card data

## Operational Timeline

| Date | Event |
|------|-------|
| March 2022 | BidenCash marketplace begins operations |
| October 2022 | BidenCash publicly dumps ~1.2 million stolen card records as promotion |
| 2023-2024 | Multiple additional public card dumps attract law enforcement attention |
| 2025 (prior to May) | US Secret Service and FBI investigation leads to identification of infrastructure |
| 2025-05-27 | Coordinated Operation Endgame action week begins; multi-country takedowns executed |
| 2025-06-05 | US DOJ announces seizure of 145 BidenCash domains and cryptocurrency |
| 2025-06-05 | Seized domains redirected to US law enforcement-controlled server displaying seizure notice |

## Results and Impact

### Seizure Results

| Metric | Value |
|--------|-------|
| Domains seized | ~145 (darknet and clearnet) |
| Cryptocurrency seized | Undisclosed amount |
| Arrests | 0 (as of announcement) |
| Indictments | 0 (as of announcement) |

### Marketplace Impact

| Metric | Lifetime Value |
|--------|----------------|
| Total customers served | 117,000+ |
| Payment cards trafficked | 15 million+ |
| Revenue generated | USD 17 million+ |
| Years of operation | ~3 (March 2022 - June 2025) |

### Infrastructure Disruption

All BidenCash domains (both .onion hidden services and clearnet mirror sites) were redirected to a law enforcement splash page, effectively shutting down the marketplace. The cryptocurrency seizure aimed to deny the operators access to their proceeds.

## Cooperation Mechanisms Used

1. **[[mutual-legal-assistance|Mutual Legal Assistance]]**: Formal legal cooperation with the Netherlands for domain infrastructure in Dutch jurisdiction.

2. **[[public-private-cooperation|Public-Private Cooperation]]**: Searchlight Cyber provided dark web monitoring and intelligence, while The Shadowserver Foundation assisted with technical infrastructure identification. This follows an increasingly common model where private dark web intelligence firms support law enforcement investigations.

3. **[[operation-endgame|Operation Endgame]] framework**: The seizure was part of a broader coordinated action week involving multiple countries and multiple targets, demonstrating the Endgame model of sustained, multi-wave disruption campaigns against cybercrime infrastructure.

4. **US Secret Service overseas presence**: The involvement of the Secret Service Frankfurt Resident Office highlights the importance of permanent law enforcement liaison offices in key European jurisdictions for coordinating cybercrime operations.

## Challenges and Friction Points

- **No arrests announced**: As of the seizure date, no individuals had been publicly charged or arrested. Domain seizure without operator arrests risks reconstitution of the marketplace under new infrastructure.
- **[[data-sovereignty|Multi-jurisdictional infrastructure]]**: BidenCash operated across numerous hosting providers and jurisdictions, requiring coordination with multiple countries to achieve comprehensive domain seizure.
- **Cryptocurrency tracing**: The exact amount of cryptocurrency seized was not disclosed, suggesting possible challenges in fully tracing and seizing the marketplace's financial proceeds.
- **Operator identification**: The marketplace operators have not been publicly identified, leaving open whether they can be located and prosecuted.

## Lessons Learned

1. **Endgame as a sustainable model**: The integration of the BidenCash takedown into the broader [[operation-endgame|Operation Endgame]] framework demonstrates a shift from one-off takedowns toward sustained, multi-wave campaigns against cybercrime infrastructure.

2. **Secret Service leadership on financial cybercrime**: The Secret Service's lead role reflects its mandate over financial crimes and its growing capability in dark web investigations, complementing the FBI's broader cybercrime mandate.

3. **Private-sector intelligence is decisive**: Searchlight Cyber and The Shadowserver Foundation's contributions underscore that law enforcement increasingly depends on private dark web intelligence firms for visibility into criminal marketplaces.

4. **Domain seizure as disruption, not elimination**: Without arrests, domain seizure disrupts operations but does not permanently disable threat actors. The operators may attempt to rebuild under different branding.

## Korean Involvement (한국의 참여)

No [[south-korea|South Korean]] participation in the BidenCash seizure has been publicly documented. However, South Korean payment card data was likely among the 15 million+ cards trafficked on the platform, as BidenCash was known to sell card data from victims worldwide. Korean financial institutions and the [[knpa|Korean National Police Agency]] cybercrime units have an interest in monitoring and responding to such marketplace takedowns to protect Korean cardholders.

## Contradictions & Open Questions

- **Operation Endgame connection**: Some sources describe the seizure as "part of Operation Endgame," while others frame it as an independent US-led action that coincided with the Endgame action week. The precise organizational relationship requires clarification.
- **Operator identity**: The BidenCash operators have not been publicly identified or charged. Whether sealed indictments exist is unknown.
- **Cryptocurrency amount**: The exact amount of cryptocurrency seized was not disclosed in any public announcement.
- **Reconstitution risk**: Previous dark web marketplace takedowns (e.g., Silk Road, AlphaBay) have shown that operators or competitors often launch replacement platforms. Whether BidenCash operators will attempt reconstitution remains an open question.

> [!note] Post-seizure status
> As of early 2026, BidenCash domains remain offline and redirected to the law enforcement seizure notice. No successor marketplace operating under the BidenCash brand has been identified.
