---
type: operation
title: "DoubleVPN Takedown"
title_ko: "DoubleVPN 소탕"
aliases:
  - "DoubleVPN seizure"
  - "DoubleVPN takedown 2021"
case_id: CYB-2021-051
period: 2
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2021-06-30
  start: 2020-10
  end: 2021-06-29
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
target_entity: "DoubleVPN (multi-layered VPN service marketed to cybercriminals)"
lead_agency: "[[netherlands-politie|Dutch National Police]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[canada]]"
  - "[[germany]]"
  - "[[united-kingdom]]"
  - "[[sweden]]"
  - "[[italy]]"
  - "[[bulgaria]]"
  - "[[switzerland]]"
participating_agencies:
  - "[[netherlands-politie|Dutch National Police]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-secret-service|US Secret Service]]"
  - "[[us-doj|US DOJ]]"
  - "[[canada-rcmp|RCMP]]"
  - "[[germany-bka|BKA]]"
  - "[[uk-nca|UK NCA]]"
legal_basis:
  - "[[empact|EMPACT (European Multidisciplinary Platform Against Criminal Threats)]]"
mechanisms_used:

results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "DoubleVPN web domains and server infrastructure seized across 9 countries"
    - "Customer personal information, logs, and statistics seized from servers"
    - "UK businesses notified of unauthorized network access via DoubleVPN"
    - "Law enforcement splash page displayed on seized domains"
edges:
  - source_actor: "Dutch National Police"
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: EMPACT
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: Eurojust
    cooperation_type: joint_investigation
    legal_basis: EMPACT
    direction: undirected
  - source_actor: "Dutch National Police"
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "UK NCA"
    target_actor: "Europol EC3"
    cooperation_type: info_sharing
    legal_basis: EMPACT
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - servers_seized_count
  - customer_count
related_cases:

related_operations:

challenges_encountered:

lessons_learned:
  - "First law enforcement takedown of a criminal-enabling VPN service — set precedent for targeting cybercrime infrastructure providers"
  - "Dutch 'digital intrusion investigatory power' (hackbevoegdheid) proved essential for penetrating VPN infrastructure"
  - "30+ Europol coordination meetings + 6 Eurojust judicial meetings = 8-month preparation for simultaneous multi-country seizure"
  - "Seizing customer logs enables follow-on investigations against DoubleVPN users"
source_count: 5
sources:
  - "[[europol-doublevpn-takedown|Europol Press Release 2021-06-30]]"
  - "[[2021-06-30_eurojust_coordinated-action-cuts-access-vpn-service-used-ransomware-groups]]"
  - "[[2022-03-02_eurojust_annual-report-2021-doublevpn-case-example]]"
  - "[[2021-06-30_nationalcrimeagency-gov-uk_doublevpn-takedown-nca-takes-uk-server-of-criminal-network-offline]]"
  - "[[2021-06-30_therecord-media_dutch-police-takes-down-doublevpn-a-service-used-by-cybercrime-groups]]"
created: 2026-04-08
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "On **29 June 2021**, law enforcement from **9 countries** simultaneously seized the infrastructure of **DoubleVPN**, a virtual private network service heavily marketed on Russian- and English-language cybercrime forums as a tool for concealing criminal activity, particularly ransomware operations. The operation was led by the [[netherlands-politie|Dutch National Police]] under the jurisdiction of the Dutch National Public Prosecutor's Office, with international coordination by [[europol-ec3|Europol EC3]] and [[eurojust|Eurojust]]."
jurisdictions:
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[canada]]"
  - "[[germany]]"
  - "[[united-kingdom]]"
  - "[[sweden]]"
  - "[[italy]]"
  - "[[bulgaria]]"
  - "[[switzerland]]"
organizations:
  - "[[netherlands-politie|Dutch National Police]]"
  - "[[europol-ec3]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-secret-service|US Secret Service]]"
  - "[[us-doj|US DOJ]]"
  - "[[canada-rcmp|RCMP]]"
  - "[[germany-bka|BKA]]"
  - "[[uk-nca|UK NCA]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[bec-ic]]"
  - "[[ransomware-ic]]"
---
## Summary

On **29 June 2021**, law enforcement from **9 countries** simultaneously seized the infrastructure of **DoubleVPN**, a virtual private network service heavily marketed on Russian- and English-language cybercrime forums as a tool for concealing criminal activity, particularly ransomware operations. The operation was led by the [[netherlands-politie|Dutch National Police]] under the jurisdiction of the Dutch National Public Prosecutor's Office, with international coordination by [[europol-ec3|Europol EC3]] and [[eurojust|Eurojust]].

DoubleVPN offered single, double, triple, and quadruple VPN connections at prices as low as **€22 (~$25)**, providing multi-layered anonymization that made it *highly likely* the preferred tool for ransomware operators targeting government and national infrastructure.

This was the **first time law enforcement took direct action against a criminal-enabling VPN service** of this type, setting a precedent for subsequent operations against cybercrime infrastructure providers (cf. [[vpnlab-takedown|VPNLab.net takedown]], January 2022).

## Background

DoubleVPN was a VPN service that routed traffic through multiple servers in different jurisdictions, offering up to quadruple encryption layers to make tracing extremely difficult. Unlike legitimate VPN providers, DoubleVPN was **specifically marketed to cybercriminals**:

- **Advertising venues**: Russian-language (e.g., XSS, Exploit.in) and English-language underground cybercrime forums
- **Target customers**: Ransomware operators, phishing fraudsters, business email compromise actors
- **Pricing**: Starting from €22 for basic connections
- **Technical features**: Single/double/triple/quadruple VPN chains across different countries

The Dutch Public Prosecutor's statement was explicit about the intent: *"By taking legal action, including special investigatory power for digital intrusion, we want to make clear there cannot be any safe havens for these kind of criminals."* (Wieteke Koorn, Leading Dutch Public Prosecutor)

## Participating Parties

### Lead Agency
- [[netherlands-politie|Dutch National Police]], under the Dutch National Public Prosecutor's Office

### Coordinating Bodies
- [[europol-ec3|Europol EC3]] — organized **30+ coordination meetings** and **4 workshops** preparing the takedown; provided analytical and crypto-tracing support
- [[eurojust]] — organized **6 dedicated coordination meetings** since October 2020; established a **coordination centre on the action day**

### Participating Countries and Agencies (9 countries)

| Country | Agency |
|---|---|
| [[netherlands]] | National Police, National Public Prosecutor's Office |
| [[united-states]] | [[fbi-cyber-division|FBI]], [[us-secret-service|US Secret Service]], [[us-doj|US DOJ]] |
| [[canada]] | [[canada-rcmp|RCMP]] |
| [[germany]] | [[germany-bka|BKA]], Prosecutor General's Office Frankfurt |
| [[united-kingdom]] | [[uk-nca|UK NCA]] (National Cyber Crime Unit) |
| [[sweden]] | Swedish Police Authority, Swedish Prosecution Authority |
| [[italy]] | State Police (Postal/Communications Services), Public Prosecutor's Office Milan |
| [[bulgaria]] | General Directorate for Fight Against Organised Crime |
| [[switzerland]] | Cantonal Police Ticino, Public Prosecutor's Office Ticino |

## Legal Framework

- **[[empact|EMPACT]]** (European Multidisciplinary Platform Against Criminal Threats) — the overarching EU framework for prioritized crime areas
- **Dutch digital intrusion investigatory power** (hackbevoegdheid) — the Dutch police used their legal authority for digital intrusion to penetrate DoubleVPN's infrastructure. This is a *legally significant* detail: the Dutch enacted the Computer Crime Act III (Wet computercriminaliteit III) in 2019, granting police the power to hack into criminal infrastructure
- No Joint Investigation Team (JIT) formation was explicitly mentioned

## Operational Timeline

| Date | Event |
|---|---|
| ~2020-10 | Investigation into DoubleVPN begins; Eurojust coordination meetings start |
| 2020-10 – 2021-06 | 30+ Europol coordination meetings, 4 workshops, 6 Eurojust meetings |
| 2021-06-29 | **Action day**: simultaneous seizure of DoubleVPN web domains and servers across 9 countries |
| 2021-06-30 | Public announcement by Europol, Eurojust, Dutch Police, UK NCA |

## Results and Impact

### Infrastructure Seized
- **Web domains** seized and replaced with law enforcement splash page
- **Server infrastructure** across 9 countries simultaneously disconnected
- **Customer personal information, logs, and statistics** seized from DoubleVPN servers — enabling follow-on investigations against criminal users
- **No arrests** were made as part of this operation

### UK-Specific Results
The [[uk-nca|UK NCA]] took the UK node of the DoubleVPN network offline and subsequently:
- Identified **several British businesses** whose networks had been unlawfully accessed through DoubleVPN
- **Directly notified** these organizations and assisted them in securing their systems

### Precedent Value
NCA Deputy Director John Denley stated: *"This is the first time law enforcement has been able to take direct action against a criminal enabling service of this type."* This established a new enforcement model for targeting cybercrime infrastructure providers rather than individual criminal groups.

## Cooperation Mechanisms Used

- **Europol EC3 virtual command post** — established on the action day for real-time coordination
- **Europol analytical and crypto-tracing support** — throughout the investigation
- **Eurojust coordination centre** — judicial coordination on the action day
- **EMPACT framework** — prioritized cybercrime as an EU-wide criminal threat

## Challenges and Friction Points

- **No arrests**: Despite seizing infrastructure and customer data, no operators were publicly identified or arrested. This may reflect the operators' use of their own anonymization tools.
- **Server count undisclosed**: Neither Europol nor participating agencies disclosed the total number of servers seized — unusual for infrastructure-seizure operations that typically emphasize scale.

## Lessons Learned

1. **Infrastructure-first approach**: Targeting the enabling service rather than individual criminal users disrupts a broader ecosystem. The seized customer logs enable subsequent investigations.
2. **Dutch hackbevoegdheid as enabler**: The Netherlands' 2019 Computer Crime Act III providing legal authority for digital intrusion was *almost certainly* essential for penetrating DoubleVPN's infrastructure. This makes the Netherlands a uniquely positioned lead for similar operations.
3. **Extensive preparation**: 8 months of coordination (30+ Europol meetings, 6 Eurojust meetings, 4 workshops) for a single action day demonstrates the investment required for multi-country simultaneous seizure.
4. **Successor operations**: The DoubleVPN model was replicated for [[vpnlab-takedown|VPNLab.net]] (January 2022, 15 servers across 10 countries) — showing institutional learning.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.


- Customer data seized from DoubleVPN servers *likely* fed into subsequent ransomware investigations across participating countries
- The [[vpnlab-takedown|VPNLab.net takedown]] (January 2022) directly referenced the DoubleVPN precedent
- The broader trend of targeting criminal infrastructure (VPNs, bulletproof hosting, encrypted communications) continued through 2022-2025

## Korean Involvement (한국의 참여)

No known Korean involvement in this operation. However, DoubleVPN's customer base *likely* included actors targeting Korean entities, given the global reach of ransomware operations the service facilitated.

## Contradictions & Open Questions

- **How many servers were seized?** Neither Europol nor any participating agency disclosed the total server count — a notable omission for an infrastructure seizure operation.
- **Were DoubleVPN operators ever identified?** No arrests or indictments were announced. Whether the customer data led to identification of operators is unknown.
- **What was the customer base size?** The number of DoubleVPN subscribers and the proportion engaged in criminal activity was not disclosed.
- **Relationship to subsequent ransomware arrests**: Did the seized DoubleVPN logs directly contribute to ransomware operator arrests in 2021-2022?

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2021-06-30: Europol: Coordinated action cuts off access to VPN service used by ransomware groups.
- Eurojust, 2021-06-30: Coordinated action cuts off access to VPN service used by ransomware groups.
- Eurojust, 2022-03-02: Eurojust Annual Report 2021: DoubleVPN case example.
- UK NCA, 2021-06-30: DoubleVPN takedown: NCA takes UK server of criminal network offline.
- The Record, 2021-06-30: Dutch police takes down DoubleVPN, a service used by cybercrime groups.

## Evidence and Attribution Notes

- DoubleVPN web domains and server infrastructure seized across 9 countries on 29 June 2021
- Dutch National Police led the operation under the Dutch National Public Prosecutor's Office; Europol EC3 organized 30+ coordination meetings and 4 workshops
- Eurojust organized 6 dedicated coordination meetings since October 2020 and established a coordination centre on the action day
- DoubleVPN offered single/double/triple/quadruple VPN connections from €22, marketed on Russian and English cybercrime forums
- Customer personal information, logs, and statistics were seized — enabling follow-on investigations
- No arrests announced; first law enforcement takedown of a criminal-enabling VPN service
- Participating agencies: Dutch Police, FBI, US Secret Service, DOJ, RCMP, BKA, NCA, Swedish Police, Italian State Police, Bulgarian GDOC, Cantonal Police Ticino
- Operating under EMPACT framework; Dutch 'hackbevoegdheid' (digital intrusion power) used

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Coordinated action cuts off access to VPN service used by ransomware groups | Europol | 2021-06-30 | https://www.europol.europa.eu/media-press/newsroom/news/coordinated-action-cuts-access-to-vpn-service-used-ransomware-groups |
| [2] | Coordinated action cuts off access to VPN service used by ransomware groups | Eurojust | 2021-06-30 | https://www.eurojust.europa.eu/news/coordinated-action-cuts-access-vpn-service-used-ransomware-groups |
| [3] | DoubleVPN takedown: NCA takes UK server of criminal network offline | UK NCA | 2021-06-30 | https://www.nationalcrimeagency.gov.uk/news/doublevpn-takedown-nca-takes-uk-server-of-criminal-network-offline |
| [4] | Dutch police takes down DoubleVPN, a service used by cybercrime groups | The Record | 2021-06-30 | https://therecord.media/dutch-police-takes-down-doublevpn-a-service-used-by-cybercrime-groups |
| [5] | Eurojust Annual Report 2021: DoubleVPN case example | Eurojust | 2022-03-02 | https://www.eurojust.europa.eu/annual-report-2021/cybercrime/case-examples |
