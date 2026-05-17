---
type: operation
title: "Operation PowerOFF"
aliases:
  - PowerOFF
  - "Power Off"
  - "Operation Power Off"
case_id: CYB-2018-006
period: 1
operation_role: umbrella
parent_operation: ""
operation_type: infrastructure-seizure
status: ongoing
enforcement_type:
  - seizure
  - arrest
  - indictment
  - warning
outcome: success
timeframe:
  announced: 2018-12-19
  start: 2018-12
  end: ""
  ongoing: true
crime_type: "[[ddos-ic]]"
crime_types:
  - "[[ddos-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[ddos-extortion]]"
target_entity: "DDoS-for-hire booter and stresser services, administrators, resellers, and users"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[australia]]"
  - "[[austria]]"
  - "[[belgium]]"
  - "[[brazil]]"
  - "[[bulgaria]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[estonia]]"
  - "[[finland]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[japan]]"
  - "[[latvia]]"
  - "[[lithuania]]"
  - "[[luxembourg]]"
  - "[[netherlands]]"
  - "[[norway]]"
  - "[[poland]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[sweden]]"
  - "[[thailand]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
jurisdictions:
  - "[[australia]]"
  - "[[austria]]"
  - "[[belgium]]"
  - "[[brazil]]"
  - "[[bulgaria]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[estonia]]"
  - "[[finland]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[japan]]"
  - "[[latvia]]"
  - "[[lithuania]]"
  - "[[luxembourg]]"
  - "[[netherlands]]"
  - "[[norway]]"
  - "[[poland]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[sweden]]"
  - "[[thailand]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[us-dcis]]"
  - "[[uk-nca]]"
  - "[[netherlands-politie]]"
  - "[[germany-bka]]"
  - "[[poland-police]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[japan-npa]]"
  - "[[france-national-police]]"
  - "[[france-junalco]]"
  - "[[latvia-state-police]]"
  - "[[portuguese-judicial-police]]"
  - "[[sweden-police]]"
  - "[[brazil-ministry-of-justice-public-security]]"
  - "[[thailand-royal-police]]"
organizations:
  - "[[europol-ec3]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[us-dcis]]"
  - "[[uk-nca]]"
  - "[[netherlands-politie]]"
  - "[[germany-bka]]"
  - "[[poland-police]]"
  - "[[australia-afp]]"
  - "[[canada-rcmp]]"
  - "[[japan-npa]]"
  - "[[france-national-police]]"
  - "[[france-junalco]]"
  - "[[latvia-state-police]]"
  - "[[portuguese-judicial-police]]"
  - "[[sweden-police]]"
  - "[[brazil-ministry-of-justice-public-security]]"
  - "[[thailand-royal-police]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[computer-fraud-and-abuse-act]]"
mechanisms_used:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[electronic-evidence]]"
  - "[[mutual-legal-assistance]]"
  - "[[public-private-cooperation]]"
results:
  arrests: 20
  indictments: 8
  servers_seized: 0
  domains_seized: 195
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "At least 195 domain seizure or takedown events are documented across public PowerOFF phases when the prior 142+ corpus aggregate is combined with the April 2026 Europol-reported 53-domain action."
    - "April 2026 phase: 21 participating countries, 53 domains taken down, 25 search warrants, 4 arrests, and more than 75,000 warning emails or letters to identified DDoS-for-hire users."
    - "April 2026 analysis of seized datasets produced intelligence on more than 3 million criminal user accounts."
    - "May 2025 phase: 9 DDoS-for-hire domains seized and four Polish administrators arrested with U.S. assistance."
    - "December 2024 phase: 27 booter or stresser domains seized, three administrators arrested in France and Germany, and 300+ users identified for follow-up."
    - "December 2022 phase: 48 domains seized and six U.S. defendants charged."
edges:
  - source_actor: "FBI Cyber Division"
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "FBI Cyber Division"
    target_actor: "UK NCA"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: "Netherlands Police"
    cooperation_type: information_exchange
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: "Poland Central Cybercrime Bureau"
    cooperation_type: coordinated_action
    legal_basis: unknown
    direction: undirected
credibility_index: 4.4
source_tier: 1
missing_fields:
  - full_unique_domain_deduplication
related_cases:
  - "[[us-v-miller-poweroff]]"
  - "[[2-defendants-charged-in-u-s-courts-as-part-of-global-crackdown-on-booter-services-offering-distributed-denial-]]"
related_operations:
  - "[[ddos-for-hire-sweep-2016]]"
  - "[[operation-us-v-miller-poweroff]]"
  - "[[operation-power-off-2026-04]]"
  - "[[operation-power-off-2025-05]]"
  - "[[de-hesse-rlp-flight-rcs-dstat-cc-poweroff-takedown-2024]]"
  - "[[bangkok-ccib-fluxstress-netdowner-ddos-as-a-service-german-arrest-2026]]"
challenges_encountered:
  - "[[data-sovereignty]]"
  - "Reconstituted booter services repeatedly reappeared under new domains after earlier seizures."
lessons_learned:
  - "Sustained, multi-phase pressure is more useful than one-off takedowns against commoditized DDoS-for-hire markets."
  - "Demand-side deterrence matters: user identification, warning letters, search ads, and prevention messages complement administrator arrests and domain seizures."
  - "Private-sector hosting, payment, search, cloud, and threat-intelligence partners are central to identifying operators, customers, and reconstituted services."
  - "Public sources must distinguish domain-seizure events from unique criminal platforms because reconstituted domains can be counted in multiple phases."
source_count: 9
sources:
  - "[[2026-04-17_europol_europol-supported-global-operation-targets-over-75-000-users]]"
  - "[[2024-12-11_europol-europa-eu_law-enforcement-shuts-down-27-ddos-booters-ahead-of-annual-christmas-attacks]]"
  - "[[2024-09-01_justice-gov_law-enforcement-seizes-9-ddos-for-hire-webpages]]"
  - "[[2026-04-18_justice-gov_2-defendants-charged-us-courts-part-global-crackdown-booter-services-offering]]"
  - "[[2026-04-18_justice-gov_federal-authorities-seize-13-internet-domains-associated-booter-websites-offered-ddos]]"
  - "[[2022-12-14_justice-gov_federal-prosecutors-in-los-angeles-and-alaska-charge-6-defendants]]"
  - "[[2024-07-15_cdca_miller-poweroff-sentencing]]"
  - "[[2024-12-12_cyberscoop-com_international-crackdown-disrupts-ddos-for-hire-operations]]"
  - "[[2024-12-12_theregister-com_operation-poweroff-extinguishes-18-more-ddos-booters]]"
created: 2026-04-10
updated: 2026-05-17
summary: "Operation PowerOFF is an ongoing multi-phase international law enforcement campaign against DDoS-for-hire booter and stresser services. Public Europol and DOJ records show recurring enforcement from 2018 through the April 2026 action week, combining domain seizures, administrator arrests, U.S. prosecutions, user identification, warning campaigns, and public-private cooperation. The latest documented phase involved 21 countries, 53 domain takedowns, 25 search warrants, 4 arrests, more than 75,000 warning messages, and intelligence derived from more than 3 million user accounts."
---
# Operation PowerOFF

## Summary

Operation PowerOFF is an ongoing international law enforcement campaign against DDoS-for-hire infrastructure. The campaign targets both supply and demand: administrators of booter and stresser services, reconstituted domains, technical infrastructure, payment flows, and users who pay to launch attacks.

The public source record now supports treating PowerOFF as a canonical operation-level page rather than as a set of disconnected U.S. prosecutions. Europol's April 2026 announcement confirms the campaign remained active after the December 2024 phase and had moved into a larger prevention-and-enforcement cycle across 21 countries.

## Background

### Modus operandi

Booter and stresser services (also called "IP stressers" or "DDoS-for-hire") are commercial websites that rent distributed denial-of-service attack capacity to paying customers on a subscription basis. Per DOJ and Europol releases, operators advertise tiered packages (typically USD 5-200 per month) granting customers the ability to launch attacks of a defined size, duration, and protocol against a target IP or hostname supplied through a web panel. Behind the panel, operators maintain reflection-and-amplification infrastructure leveraging misconfigured DNS, NTP, Memcached, and CLDAP servers, as well as compromised IoT devices, to multiply attack bandwidth to tens or hundreds of Gbps. Customers require no technical skill; the panel abstracts the underlying botnet and reflector network behind a "select target, click attack" interface. DOJ filings in the 2022 and 2023 phases describe operators using fictitious "stress testing" terms-of-service language as a fig leaf while marketing capacity openly to gaming, school, and small-business targets.

**Victim profile + impact.** Public DOJ and Europol releases identify recurring victim categories: online gaming services and individual gamers (where attacks are launched mid-match for competitive advantage or extortion), schools and universities (attacks during exam or remote-learning periods), financial-services firms, internet service providers, government websites, and small-to-medium businesses. The 2022 DOJ CDCA wave alleged that seized booters had been used against "millions of victims" worldwide. The April 2026 phase recovered intelligence on more than 3 million user accounts held in seized service databases, indicating a large active customer base launching attacks against an even larger target population. Quantified victim financial loss is not consistently disclosed; impacts are typically measured in downtime, mitigation costs, and lost transactions rather than direct theft.

### Financial flow

Booter services are commercialized through web-payment rails: cryptocurrency (BTC, ETH, occasional Monero), PayPal, gift cards, and prepaid voucher resellers, routed through middleman payment processors that obscure operator identity. DOJ records describe operator revenues in the hundreds of thousands to low millions of USD per service across the documented lifetime; the May 2025 Polish-administrator phase referenced operators that had been monetizing services for several years before takedown. Money laundering follows commodity-cybercrime patterns: cash-out via cryptocurrency exchanges, peer-to-peer markets, and reinvestment into hosting and domain infrastructure. The April 2026 phase explicitly tied "intelligence on more than 3 million criminal user accounts" to follow-on financial-attribution work.

### Criminal organization structure

Booter operations are typically small, loosely structured teams of 1-6 individuals rather than hierarchical OCGs: a lead administrator, one or two co-developers maintaining the attack panel and reflector list, and resellers or affiliates handling marketing on hacking forums (HackForums historically, Telegram and Discord increasingly). DOJ defendants charged in 2022-2026 phases were typically young (late teens to early 30s), often U.S., U.K., German, French, or Polish nationals, operating independently rather than under organized-crime umbrellas. Reconstitution after takedown is a defining feature: Europol and DOJ both document the same operators relaunching seized services under new domains within weeks, which is why PowerOFF is structured as a sustained multi-phase campaign rather than a single takedown.

## Scope and Boundary

This page is the operation-level aggregation point for PowerOFF. Defendant-specific U.S. records such as [[operation-us-v-miller-poweroff]] and [[us-v-miller-poweroff]] remain follow-on records and should not be counted as separate international-cooperation operations.

The record is distinct from [[ddos-for-hire-sweep-2016]], the earlier 2016 Europol/FBI demand-side sweep. That 2016 action established a precursor model for identifying and warning DDoS-for-hire users, while PowerOFF is the named multi-phase campaign that began in the later booter-service takedown cycle.

## Participation

The April 2026 Europol phase named 21 participating countries: Australia, Austria, Belgium, Brazil, Bulgaria, Denmark, Estonia, Finland, Germany, Japan, Latvia, Lithuania, Luxembourg, the Netherlands, Norway, Poland, Portugal, Sweden, Thailand, the United Kingdom, and the United States.

The broader PowerOFF record also includes countries named in earlier phases, including Canada, France, and Romania. Public sources identify Europol EC3, the FBI, DOJ, DCIS, the UK NCA, Netherlands Police, Germany's BKA, Poland's Central Cybercrime Bureau, and several national cybercrime units as recurring or phase-specific participants.

## Operational Model

- **Infrastructure disruption:** Authorities seized or disabled booter and stresser domains used to sell DDoS-for-hire services.
- **Administrator accountability:** DOJ records tie the campaign to U.S. charges, guilty pleas, and sentencings; Europol reporting identifies arrests of administrators in Europe.
- **Demand-side deterrence:** PowerOFF uses warning letters, email campaigns, search-engine ads, YouTube ads, blockchain warning messages, and removal of search-result URLs to reach users.
- **Data exploitation:** Seized service databases allow participating countries to identify high-value users, geolocate accounts, and prepare follow-up activity.
- **Public-private support:** Hosting, cloud, payment, search, and threat-intelligence providers support identification, seizure, and prevention work.

## Timeline

| Date | Phase | Publicly documented result |
|---|---|---|
| 2018-12 | Initial PowerOFF wave | DOJ later described 15 DDoS-for-hire domains seized and three defendants charged. |
| 2022-12-14 | Major U.S.-linked wave | 48 domains seized; six U.S. defendants charged; FBI, UK NCA, and Netherlands Police launched deterrence ads. |
| 2023-05-08 | Reconstitution sweep | 13 domains seized, including 10 reincarnations of previously seized services; four defendants had pleaded guilty. |
| 2024-07-15 | Sentencing output | Jeremiah Sam Evans Miller sentenced for RoyalStresser.com, a PowerOFF-linked booter service. |
| 2024-12-11 | Christmas-season action | 27 booter or stresser websites seized; three administrators arrested in France and Germany; 300+ users identified for follow-up. |
| 2025-05-07 | U.S.-Poland phase | 9 domains seized; Poland announced four administrator arrests assisted by U.S. authorities. |
| 2026-04-13 | Global action week | 21 countries; 53 domains taken down; 25 search warrants; 4 arrests; 75,000+ warning messages. |

## Results

| Metric | Publicly supported value |
|---|---:|
| Participating countries in latest phase | 21 |
| Countries documented across phases | 24 |
| Domain seizure/takedown events | 195+ |
| Arrests recorded across public phase summaries | 20+ |
| U.S. defendants charged in public DOJ PowerOFF waves | 8+ |
| April 2026 search warrants | 25 |
| April 2026 warning messages | 75,000+ |
| User accounts in seized datasets | 3,000,000+ |

The domain count is an operational count, not a deduplicated count of unique platforms. DOJ and Europol both describe reconstituted booter services that returned under new domains after earlier seizures.

## Evidence Notes

The strongest current source is Europol's April 2026 release, which confirms the latest international phase, the 21-country list, the 53-domain takedown, 4 arrests, 25 search warrants, 75,000 warning messages, and use of seized datasets containing more than 3 million user accounts.

DOJ CDCA releases provide the strongest U.S. judicial trace: the 2022 six-defendant/48-domain wave, the 2023 13-domain reconstitution sweep, the 2024 two-defendant/27-domain action, the 2025 9-domain action with Polish arrests, and the Miller sentencing follow-on.

## Contradictions & Open Questions

- Aggregate victim financial impact across PowerOFF phases is not disclosed in tier-1 sources; only operator-side metrics (domains, arrests, user-account counts) are systematically reported.
- Public sources do not provide a consolidated cumulative revenue figure for seized booter services across the 2018-2026 phase set.
- The 3-million-user-account figure from the April 2026 phase is reported as a count of records in seized datasets; the proportion of unique paying customers versus duplicate or test accounts is not disclosed.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol-supported global operation targets over 75 000 users engaged in DDoS attacks | Europol | 2026-04-17 | https://www.europol.europa.eu/media-press/newsroom/news/europol-supported-global-operation-targets-over-75-000-users-engaged-in-ddos-attacks |
| [2] | Law enforcement shuts down 27 DDoS booters ahead of annual Christmas attacks | Europol | 2024-12-11 | https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-shuts-down-27-ddos-booters-ahead-of-annual-christmas-attacks |
| [3] | Law Enforcement Seizes 9 DDoS-for-Hire Webpages as Part of Global Crackdown on Booter and Stresser DDoS Services | US DOJ CDCA | 2025-05-07 | https://www.justice.gov/usao-cdca/pr/law-enforcement-seizes-9-ddos-hire-webpages-part-global-crackdown-booter-and-stresser |
| [4] | 2 Defendants Charged in U.S. Courts as Part of Global Crackdown on Booter Services Offering Distributed Denial-of-Service Attacks | US DOJ CDCA | 2024-12-11 | https://www.justice.gov/usao-cdca/pr/2-defendants-charged-us-courts-part-global-crackdown-booter-services-offering |
| [5] | Federal Authorities Seize 13 Internet Domains Associated with Booter Websites that Offered DDoS Computer Attack Services | US DOJ CDCA | 2023-05-08 | https://www.justice.gov/usao-cdca/pr/federal-authorities-seize-13-internet-domains-associated-booter-websites-offered-ddos |
| [6] | Federal Prosecutors in Los Angeles and Alaska Charge 6 Defendants with Operating Websites that Offered Computer Attack Services | US DOJ CDCA | 2022-12-14 | https://www.justice.gov/usao-cdca/pr/federal-prosecutors-los-angeles-and-alaska-charge-6-defendants-operating-websites |
| [7] | Texas Man Sentenced to 9 Months in Federal Prison for Operating Website that Offered Computer Attack Services | US DOJ CDCA | 2024-07-15 | https://www.justice.gov/usao-cdca/pr/texas-man-sentenced-9-months-federal-prison-operating-website-offered-computer-attack |
| [8] | International crackdown disrupts DDoS-for-hire operations | CyberScoop | 2024-12-12 | https://cyberscoop.com/international-crackdown-disrupts-ddos-for-hire-operations/ |
| [9] | Operation PowerOFF extinguishes 18 more DDoS booters | The Register | 2024-12-12 | https://www.theregister.com/2024/12/12/operation_poweroff_ddos_takedowns/ |
