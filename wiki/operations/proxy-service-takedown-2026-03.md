---
type: operation
title: "SocksEscort / AVrecon Residential Proxy Takedown (March 2026)"
title_ko: "사이버범죄용 IP 프록시 서비스 단속 (2026년 3월)"
aliases:
  - "SocksEscort Takedown"
  - "SocksEscort Proxy Network Takedown"
  - "AVrecon SocksEscort Takedown"
  - "Eurojust IP Proxy Takedown 2026"
case_id: CYB-2026-001
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - takedown
  - disruption
  - cryptocurrency-freezing
outcome: disrupted
timeframe:
  announced: 2026-03-12
  start: "2020-06"
  end: 2026-03-11
  ongoing: false
crime_type: "[[cybercrime-infrastructure-ic]]"
target_entity: "SocksEscort residential proxy service, AVrecon-infected routers and IoT devices, related command-and-control/payment infrastructure"
lead_agency: "[[us-doj]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[united-states]]"
  - "[[france]]"
  - "[[austria]]"
  - "[[netherlands]]"
  - "[[bulgaria]]"
  - "[[germany]]"
  - "[[hungary]]"
  - "[[romania]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-dcis]]"
  - "IRS Criminal Investigation Oakland Field Office"
  - "[[eurojust]]"
  - "[[europol-ec3]]"
  - "[[france-national-police|French National Police OFAC]]"
  - "[[france-junalco|JIRS/JUNALCO]]"
  - "[[netherlands-om|Public Prosecutor's Office Limburg]]"
  - "[[netherlands-politie|Police Limburg]]"
  - "[[bulgaria-police|Bulgaria GDBOP Cybercrime Directorate]]"
  - "[[germany-lka|Dusseldorf Police / ZAC NRW]]"
  - "[[romania-diicot|Romania DIICOT]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
  - "[[european-investigation-order]]"
mechanisms_used:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[cryptocurrency-seizure]]"
  - "[[european-investigation-order]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 24
  domains_seized: 34
  cryptocurrency_seized: "Approximately EUR 3.5 million frozen by US authorities"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "SocksEscort residential proxy service disrupted on 2026-03-11"
    - "Approximately 369,000 routers and IoT devices compromised or sold as proxy access since 2020"
    - "Approximately 8,000 infected routers listed in the SocksEscort application in February 2026, including about 2,500 in the United States"
    - "Affected device footprint reported across approximately 163 countries; Eurojust framed the enforcement target as serving cybercriminal proxy activity in 102 victim countries"
    - "Approximately 124,000 customer users and more than EUR 5 million in customer payments reported by Eurojust"
edges:
  - source_actor: "United States"
    target_actor: France
    cooperation_type: joint_enforcement
    legal_basis: MLAT
    direction: undirected
  - source_actor: "United States"
    target_actor: Austria
    cooperation_type: joint_enforcement
    legal_basis: MLAT
    direction: undirected
  - source_actor: "United States"
    target_actor: Netherlands
    cooperation_type: joint_enforcement
    legal_basis: MLAT
    direction: undirected
  - source_actor: Eurojust
    target_actor: "European participants"
    cooperation_type: judicial_coordination
    legal_basis: European_Investigation_Order
    direction: directed
  - source_actor: Europol
    target_actor: "Joint operation"
    cooperation_type: technical_assistance
    legal_basis: operational_support
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - public_operator_identity
  - arrests_or_charges_if_any
  - court_docket_numbers
  - exact_seized_domain_and_server_inventory
related_operations:
  - "[[911-s5-botnet-takedown]]"
  - "[[doublevpn-takedown]]"
challenges_encountered:
  - "[[data-sovereignty]]"
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "Residential proxy botnets require simultaneous malware, domain, server, payment, and victim-remediation measures rather than a domain seizure alone."
  - "Eurojust/Europol coordination can align US seizure authority with European Investigation Orders where infected-device infrastructure and operators span several European states."
source_count: 6
sources:
  - "[[2026-03-12-eurojust-proxy-service-takedown]]"
  - "[[2026-03-12_justice-gov_authorities-dismantle-global-malicious-proxy-service-deployed-malware-and-defrauded]]"
  - "[[2026-03-12_fbi-gov_avrecon-malware-infected-routers-exploited-as-residential-proxies-by-socksescort]]"
  - "[[2026-03-13_cyberscoop-com_socksescort-proxy-network-botnet-takedown]]"
  - "[[2026-03-13_cybernews-com_major-residential-proxy-service-socksescort-down]]"
  - "[[2026-03-13_techradar-com_major-socksescort-proxy-network-powered-by-linux-malware-taken-down-by-fbi-and-other-police-forces]]"
created: 2026-04-14
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "On 11 March 2026, authorities in the United States and Europe disrupted SocksEscort, a malware-enabled residential proxy service that sold access to AVrecon-compromised routers and IoT devices. Eurojust reported the takedown of 24 servers in seven countries, seizure of 34 domains, disconnection of infected modems, and approximately EUR 3.5 million in cryptocurrency frozen by US authorities. DOJ and FBI materials identify the service as SocksEscort and the malware family as AVrecon."
jurisdictions:
  - "[[united-states]]"
  - "[[france]]"
  - "[[austria]]"
  - "[[netherlands]]"
  - "[[bulgaria]]"
  - "[[germany]]"
  - "[[hungary]]"
  - "[[romania]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-dcis]]"
  - "[[eurojust]]"
  - "[[europol-ec3]]"
  - "[[shadowserver]]"
crime_types:
  - "[[cybercrime-infrastructure-ic]]"
  - "[[malware-ic]]"
  - "[[online-fraud-ic]]"
  - "[[bank-fraud-ic]]"
---
## Summary

On **11 March 2026**, a US-European law-enforcement action disrupted **SocksEscort**, a residential proxy service that monetized routers and IoT devices infected with **AVrecon** malware. [[eurojust|Eurojust]] announced the public takedown on **12 March 2026**; the [[us-doj|US Department of Justice]] and [[fbi|FBI]] materials identify the service and malware family that the earlier Eurojust framing did not name.

The action was materially larger than the original page reflected. Eurojust reported **24 servers taken down in seven countries**, **34 domains seized**, infected modems disconnected from the proxy service, approximately **EUR 3.5 million in cryptocurrency frozen by US authorities**, about **369,000 compromised routers and other devices across 163 countries**, and roughly **124,000 customer users**. DOJ added that SocksEscort had offered access to about **369,000 IP addresses since summer 2020** and that, as of February 2026, the service listed about **8,000 active infected routers**, including about **2,500 in the United States**.

> [!note] Reconciliation note
> This page originally treated the service as unnamed because it was based on a short Eurojust ingest. Subsequent official DOJ and FBI publications identify the service as **SocksEscort** and the malware as **AVrecon**. The "4 unnamed countries" and "servers not stated" gaps are therefore resolved.

## What Was Targeted

SocksEscort sold paid access to residential IP addresses so customers could route traffic through ordinary home and small-business networks. That made malicious activity appear to originate from legitimate consumer connections rather than from known criminal infrastructure.

The technical substrate was **AVrecon**, malware used to compromise routers and IoT devices. The FBI FLASH says the malware targeted routers and IoT devices across approximately 163 countries, primarily SOHO devices and consumer networking equipment. The proxy service then sold access to those devices as residential proxies.

## Criminal Use

The sources document several abuse patterns:

- Concealing the origin of fraud traffic through residential IP addresses
- Takeovers of bank and cryptocurrency accounts
- Fraudulent unemployment-insurance claims
- Ad fraud, password spraying, marketplace fraud, banking fraud, and romance-fraud activity observed by the FBI and partners
- Use of the proxy network to evade IP reputation, geolocation, and block-list controls

DOJ listed concrete US victim examples, including a New York cryptocurrency-exchange customer defrauded of about USD 1 million in cryptocurrency, a Pennsylvania manufacturing business defrauded of about USD 700,000, and current or former US service members whose MILITARY STAR cards were defrauded of about USD 100,000.

## Participating Parties

| Country / Body | Publicly identified participants | Role |
|---|---|---|
| [[united-states]] | [[us-doj]], US Attorney's Office for the Eastern District of California, [[fbi|FBI Sacramento]], [[us-dcis|DCIS]], IRS Criminal Investigation Oakland, DOJ OIA, DOJ National Security Cyber Section, DOJ CCIPS, ICHIP The Hague, FinCEN, California Highway Patrol | US-led court-authorized disruption, domain seizures, investigation, crypto/financial support |
| [[france]] | Paris J3 Anti-Cybercrime unit, JIRS/JUNALCO financial and cybercrime section, [[france-national-police\|OFAC]] | Server/infrastructure action and judicial coordination |
| [[austria]] | Criminal Intelligence Service Austria, Cybercrime-Competence-Center C4, Public Prosecutor's Office Vienna | Server/infrastructure action and judicial coordination |
| [[netherlands]] | Public Prosecutor's Office Limburg, Police Limburg / Dutch National Police | Server/infrastructure action and judicial coordination |
| [[bulgaria]] | District Public Prosecution Office Plovdiv, GDBOP Cybercrime Directorate | Action-day support through Eurojust-transmitted judicial request |
| [[germany]] | Dusseldorf Police Headquarters, ZAC NRW | Server/infrastructure and judicial support |
| [[hungary]] | Prosecution Service of Hungary, National Bureau of Investigation Cybercrime Department | Server/infrastructure and judicial support |
| [[romania]] | Prosecutor's Office of the High Court of Cassation and Justice, DIICOT Central Office, Central Cybercrime Unit, Romanian Police | Server/infrastructure and judicial support |
| [[eurojust]] | Coordination meetings and action-day judicial coordination | Prepared and synchronized cross-border judicial measures |
| [[europol-ec3\|Europol]] | Operational/analytical support, crypto tracing, malware and network analysis, Virtual Command Post | Technical and operational support |
| Private/technical partners | Lumen Black Lotus Labs, [[shadowserver\|Shadowserver Foundation]] | Technical assistance and network-disruption support |

## Legal and Cooperation Model

The operation combined several layers of authority rather than relying on a single seizure:

- **US court-authorized seizure warrants** against US-registered domains connected to the proxy service.
- **European Investigation Orders** prepared through Eurojust for infrastructure in France, Germany, Hungary, the Netherlands, Romania, and the United States.
- **Eurojust coordination** for prosecutors and investigating judges, including repeated meetings in The Hague.
- **Europol operational support**, including crypto tracing, malware analysis, network analysis, database cross-checks, and an action-day Virtual Command Post.
- **Private-sector technical support** from Lumen Black Lotus Labs and Shadowserver.

## Operational Timeline

| Date | Event |
|---|---|
| Summer 2020 | DOJ says SocksEscort had begun offering access to compromised IP addresses by this period. |
| February 2026 | DOJ says the SocksEscort application listed approximately 8,000 infected routers available to customers, including about 2,500 in the United States. |
| 2026-03-11 | Coordinated operation targeted the proxy-service infrastructure; Eurojust reports 24 servers taken down in seven countries and 34 domains seized. |
| 2026-03-12 | Eurojust, DOJ/USAO EDCA, IRS-CI, and the FBI FLASH publicly documented the takedown from different perspectives. |
| 2026-03-13 | CyberScoop, Cybernews, and TechRadar added trade-press coverage naming SocksEscort and describing the AVrecon/proxy-botnet context. |
| 2026-04-18 | DOJ Cyber & IP Europe later confirmed ICHIP The Hague's Eurojust coordination-center role and listed the eight participating countries. |

## Results and Impact

| Metric | Value | Source basis |
|---|---:|---|
| Servers taken down | 24 | Eurojust |
| Countries hosting taken-down servers | 7 | Eurojust |
| Domains seized | 34 | Eurojust |
| Cryptocurrency frozen | approx. EUR 3.5 million | Eurojust |
| Customer payments to platform | more than EUR 5 million | Eurojust |
| Customer users | approx. 124,000 | Eurojust |
| Compromised routers / devices | approx. 369,000 | Eurojust, DOJ, FBI |
| Countries with compromised devices | approx. 163 | Eurojust, FBI |
| Active infected routers listed in app | approx. 8,000 as of February 2026 | DOJ / IRS-CI |
| Active infected routers in US | approx. 2,500 as of February 2026 | DOJ / IRS-CI |

## Assessment

This operation should be treated as a **malware-enabled residential proxy botnet disruption**, not as a generic proxy-site seizure. The core enforcement value came from synchronizing four disruption surfaces:

1. **Infrastructure:** server takedown and domain seizure
2. **Malware ecosystem:** AVrecon C2 and relay disruption
3. **Financial layer:** payment platform targeting and cryptocurrency freezing
4. **Victim network cleanup:** disconnection of infected modems from the proxy service and FBI defensive guidance

The page is also a useful comparator for [[911-s5-botnet-takedown|911 S5]] and other residential-proxy botnet takedowns because the cases involve commercialized access to compromised residential IP space. SocksEscort differs in that the public record emphasizes AVrecon malware, European server coordination, and action-day judicial synchronization through Eurojust.

## Korean Involvement (한국 관련성)

No [[south-korea|South Korean]] law-enforcement participation is publicly documented. Because the FBI and Eurojust describe compromised devices across approximately **163 countries**, Korean devices could be part of the global victim footprint, but none of the current official sources identify Korea-specific victims, servers, agencies, or remediation steps. This page should therefore not assert Korean involvement without a later Korea-specific source.

## Open Questions

- No public source reviewed here identifies the service operators by name.
- No arrests, indictments, or docket numbers are public in the collected sources; the numeric arrest and indictment fields remain **0 / not publicly reported**, not a confirmed absence of suspects.
- The exact domain list and server inventory are not fully reproduced on this page; the FBI FLASH supplies defensive indicators, but not a complete seized-asset ledger.
- Eurojust reports approximately 124,000 customer users and more than EUR 5 million in customer payments; DOJ focuses on US victim fraud examples. The sources do not yet provide a full global victim-loss total.
- The final legal status of the payment platform and frozen cryptocurrency remains unclear.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Eurojust, 2026-03-12: Official judicial-coordination release with the 24-server, 34-domain, EUR 3.5 million, 369,000-device, 163-country, and eight-country participation metrics.
- DOJ / USAO EDCA, 2026-03-12: Official US press release naming SocksEscort, describing the malware-enabled residential proxy model, and listing US investigators and supporting international authorities.
- FBI, 2026-03-12: AVrecon FLASH linking the malware family to SocksEscort, describing router/IoT compromise methods, and providing defensive indicators and remediation guidance.
- CyberScoop, 2026-03-13: Trade-press coverage naming SocksEscort and summarizing the proxy-botnet scale and customer-payment figure.
- Cybernews, 2026-03-13: Trade-press coverage focused on the residential-proxy business model and compromised home-internet footprint.
- TechRadar, 2026-03-13: Short technical trade-press summary emphasizing AVrecon/Linux-router malware and the multinational enforcement result.

## Evidence and Attribution Notes

- The service name is no longer unknown: DOJ, FBI, and multiple follow-up reports identify it as **SocksEscort**.
- The malware family is no longer unknown: the FBI FLASH identifies **AVrecon**.
- The eight participating countries are no longer unknown: Eurojust/DOJ identify the United States, France, Austria, the Netherlands, Bulgaria, Germany, Hungary, and Romania.
- Anyproxy is a related residential-proxy precedent, but it is not a direct source for this March 2026 action and is therefore removed from this page's reference count.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Servers used for cybercrime around the world taken down | Eurojust | 2026-03-12 | https://www.eurojust.europa.eu/news/servers-used-cybercrime-around-world-taken-down |
| [2] | Authorities Dismantle Global Malicious Proxy Service that Deployed Malware and Defrauded Thousands of U.S. Persons, Businesses, and Financial Institutions of Millions of Dollars in Losses | US DOJ USAO EDCA | 2026-03-12 | https://www.justice.gov/usao-edca/pr/authorities-dismantle-global-malicious-proxy-service-deployed-malware-and-defrauded |
| [3] | AVrecon Malware-Infected Routers Exploited as Residential Proxies by SocksEscort | FBI | 2026-03-12 | https://www.fbi.gov/file-repository/cyber-alerts/avrecon-malware-infected-routers-exploited-as-residential-proxies-by-socksescort.pdf |
| [4] | Authorities takedown global proxy network SocksEscort | CyberScoop | 2026-03-13 | https://cyberscoop.com/socksescort-proxy-network-botnet-takedown/ |
| [5] | Authorities shut down cybercrime service that sold access to 369,000 home internet connections | Cybernews | 2026-03-13 | https://cybernews.com/security/major-residential-proxy-service-socksescort-down/ |
| [6] | Major SocksEscort proxy network powered by Linux malware taken down by FBI and other police forces | TechRadar | 2026-03-13 | https://www.techradar.com/pro/security/major-socksescort-proxy-network-powered-by-linux-malware-taken-down-by-fbi-and-other-police-forces |
