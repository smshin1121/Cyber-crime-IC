---
type: operation
title: "Carding Action 2020"
aliases:
  - "e-Commerce Action 2020"
case_id: ""
period: 2
operation_type: joint-investigation
status: completed
enforcement_type:
  - seizure
outcome: success
timeframe:
  announced: 2020-11-26
  start: 2020-09
  end: 2020-11
  ongoing: false
crime_type: "[[carding-fraud-ic]]"
target_entity: "Dark web card shops and compromised payment card data traders"
lead_agency: "[[europol-ec3|Europol EC3]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[italy]]"
  - "[[hungary]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[europol-ec3|Europol EC3]]"
  - "[[group-ib|Group-IB]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention]]"
mechanisms_used:
  - "[[public-private-cooperation|Public-Private Cooperation]]"
  - "[[informal-cooperation|Informal Police Cooperation]]"
results:
  arrests: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  other:
    - "90,000 pieces of compromised card data analysed"
    - "EUR 40 million in potential losses prevented"
edges:
  - source_actor: "Europol EC3"
    target_actor: Group-IB
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: Italy
    target_actor: Hungary
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: "UK DCPCU"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 3.5
source_tier: 2
missing_fields:
  - "arrests (none publicly confirmed)"
  - case_id
related_operations:
  - "[[infraud-organization-takedown|Infraud Organization Takedown]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional complexity of cross-border carding]]"
lessons_learned:
  - "Public-private cooperation with payment card industry significantly amplifies law enforcement reach"
  - "Proactive data analysis can prevent losses before fraud is committed"
source_count: 6
sources:
  - "[[2020-11-26_ukfinance-org-uk_dcpcu-works-with-europol-on-operation-carding-action-2020]]"
  - "[[2020-12-01_cisomag-com_operation-carding-action-2020-cracks-down-credit-card-scammers]]"
  - "[[2020-11-30_association-secure-transactions-eu_carding-action-by-police-prevents-e40-million-in-losses]]"
  - "[[2020-11-26_group-ib-com_carding-action-2020]]"
  - "[[2020-11-27_welivesecurity-com_europol-partners-thwart-credit-card-fraud-scheme]]"
  - "[[2020-11-26_europol-europa-eu_officers-foil-fraudsters-stealing-eur-40-million-in-payment-card-scam]]"
created: 2026-04-10
updated: "2026-04-26"
operation_role: umbrella
parent_operation: ""
summary: "Carding Action 2020 was a three-month intelligence-led operation coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] between September and November 2020. The operation targeted traders of compromised payment card data on dark web card shops and marketplaces. Law enforcement agencies from [[italy|Italy]], [[hungary|Hungary]], and the [[united-kingdom|United Kingdom]] collaborated with [[group-ib|Group-IB]], the sole private-sector cybersecurity partner, and major card payment schemes to analyse approximately 90,000 pieces of stolen card data. The operation is assessed to have prevented an estimated EUR 40 million (approximately USD 48 million) in potential fraud losses. No arrests were publicly announced; the operation was primarily intelligence-driven and preventive in nature."
jurisdictions:
  - "[[italy]]"
  - "[[hungary]]"
  - "[[united-kingdom]]"
organizations:
  - "[[europol-ec3|Europol EC3]]"
  - "[[group-ib|Group-IB]]"
crime_types:
  - "[[carding-fraud-ic]]"
  - "[[dark-web-ic]]"
---
## Summary

Carding Action 2020 was a three-month intelligence-led operation coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] between September and November 2020. The operation targeted traders of compromised payment card data on dark web card shops and marketplaces. Law enforcement agencies from [[italy|Italy]], [[hungary|Hungary]], and the [[united-kingdom|United Kingdom]] collaborated with [[group-ib|Group-IB]], the sole private-sector cybersecurity partner, and major card payment schemes to analyse approximately 90,000 pieces of stolen card data. The operation is assessed to have prevented an estimated EUR 40 million (approximately USD 48 million) in potential fraud losses. No arrests were publicly announced; the operation was primarily intelligence-driven and preventive in nature.

## Background

Payment card fraud (carding) remains one of the most common forms of cyber-enabled financial crime. Stolen card data is typically harvested through phishing websites, banking trojans infecting end-user devices, and JavaScript sniffers (JS-sniffers or Magecart-type attacks) injected into compromised e-commerce platforms. This data is then traded on dark web "card shops" -- dedicated marketplaces where stolen card numbers, CVVs, and associated personally identifiable information are sold in bulk.

By 2020, the expansion of e-skimming attacks targeting merchant point-of-sale systems and e-commerce sites had contributed to a significant increase in compromised card data circulating on the dark web. [[europol-ec3|Europol EC3]] initiated Carding Action 2020 to disrupt this supply chain before the fraud was committed, adopting a proactive, prevention-focused approach rather than a purely enforcement-driven strategy.

## Participating Parties

### Lead and Coordination

| Role | Entity |
|------|--------|
| Coordinator | [[europol-ec3|Europol EC3]] |
| Operational analysis | Europol analysts |

### Law Enforcement Partners

| Country | Agency | Role |
|---------|--------|------|
| [[italy]] | Italian law enforcement | Co-lead |
| [[hungary]] | Hungarian law enforcement | Co-lead |
| [[united-kingdom]] | Dedicated Card and Payment Crime Unit (DCPCU), London Metropolitan Police & City of London Police | Operational support |

### Private Sector Partners

| Entity | Role |
|--------|------|
| [[group-ib|Group-IB]] | Sole cybersecurity company; provided analysis of 90,000 compromised card records |
| Major card schemes | Shared intelligence on compromised accounts (names undisclosed but likely include Visa, Mastercard) |

> [!note] Participant scope
> The participating country list is limited to those named in Europol and Group-IB press releases. Additional countries may have contributed through Europol information-sharing channels but were not publicly credited.

## Legal Framework

The operation relied on [[public-private-cooperation|public-private cooperation]] mechanisms rather than formal mutual legal assistance processes. [[europol-ec3|Europol EC3]] facilitated the coordination and information exchange between law enforcement authorities and private-sector partners under its mandate to support EU member states in combating cybercrime. The [[budapest-convention|Budapest Convention on Cybercrime]] likely provided the underlying legal framework for cross-border cooperation, given that all participating states are parties.

## Operational Timeline

| Date | Event |
|------|-------|
| September 2020 | Operation commenced; data collection and analysis phase began |
| Sep-Nov 2020 | Group-IB analysed approximately 90,000 pieces of compromised card data |
| Sep-Nov 2020 | Card schemes and law enforcement cross-referenced compromised data with active accounts |
| 2020-11-26 | Europol publicly announced the operation and its results |

## Results and Impact

| Metric | Value |
|--------|-------|
| Compromised card records analysed | ~90,000 |
| Estimated losses prevented | EUR 40 million (~USD 48 million) |
| Publicly confirmed arrests | 0 |
| Card data sources identified | Phishing sites, banking trojans, JS-sniffers on e-commerce sites |

The 90,000 card records analysed by Group-IB all contained full card data (card number, expiration date, CVV, and in many cases cardholder name and address). Sources of compromise included:

- **Phishing websites** impersonating legitimate banks or payment portals
- **Banking trojans** installed on end-user devices
- **JS-sniffers** (Magecart-type scripts) injected into hijacked e-commerce merchant websites

The primary outcome was preventive: compromised cards were flagged to issuing banks for blocking or enhanced monitoring before fraudulent transactions could be completed.

## Cooperation Mechanisms Used

1. **[[public-private-cooperation|Public-Private Cooperation]]**: The defining feature of this operation. Group-IB's threat intelligence on compromised card data was shared with Europol, which coordinated its distribution to national law enforcement and card schemes for rapid mitigation.

2. **[[informal-cooperation|Informal Police Cooperation]]**: Europol facilitated real-time information exchange between participating agencies without formal MLAT requests, enabling rapid identification of compromised accounts.

3. **Europol Operational Support**: Europol analysts provided operational analysis on large volumes of data and expertise in payment card fraud.

## Challenges and Friction Points

- **Attribution difficulty**: Identifying the individuals behind dark web card shop operations remains technically challenging due to anonymization tools and cryptocurrency payments.
- **[[jurisdictional-conflicts|Jurisdictional complexity]]**: Compromised card data originates from victims worldwide, is sold on servers in multiple jurisdictions, and purchased by fraudsters in yet other jurisdictions, making enforcement action complex.
- **Scale of the problem**: 90,000 records represents only a fraction of the total volume of stolen card data circulating on the dark web at any given time.

## Lessons Learned

1. **Prevention as a strategy**: Carding Action 2020 demonstrated that proactive analysis and notification can prevent significant financial losses without requiring arrests or takedowns.

2. **Private-sector intelligence is essential**: [[group-ib|Group-IB]]'s contribution was critical. Law enforcement alone does not have the same visibility into dark web card shops that specialized cybersecurity firms possess.

3. **Scalable model**: The operation established a template for future carding action operations. Europol subsequently conducted similar operations in later years, building on this public-private partnership model.

## Korean Involvement (한국의 참여)

No Korean participation in Carding Action 2020 has been publicly documented. However, [[south-korea|South Korea]] faces significant card fraud challenges, and Korean payment card data has been found on dark web card shops. Future iterations of similar Europol-led carding actions could benefit from engagement with [[knpa|Korean National Police Agency]] cybercrime units and Korean financial institutions.

## Contradictions & Open Questions

- **Arrest count unclear**: No arrests were publicly announced by Europol or participating agencies. It remains uncertain whether the intelligence gathered led to subsequent law enforcement actions that were not publicly attributed to this operation.
- **Scope of private-sector participation**: Europol referenced "card schemes" but did not name them. The full extent of private-sector involvement beyond Group-IB is unclear.
- **Follow-up operations**: Whether the intelligence from this operation fed into subsequent enforcement actions has not been publicly disclosed.


## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | DCPCU works with Europol on operation Carding Action 2020 | UK Finance | 2020-11-26 | https://www.ukfinance.org.uk/press/press-releases/dcpcu-works-with-europol-on-operation-carding-action-2020 |
| [2] | Operation Carding Action 2020 Cracks Down Credit Card Scammers | CISO MAG | 2020-12-01 | https://cisomag.com/credit-card-scammers-arrested-in-carding-scam-2020/ |
| [3] | Carding Action by Police prevents EUR 40 million in losses | EAST | 2020-11-30 | https://www.association-secure-transactions.eu/carding-action-by-police-prevents-e40-million-in-losses/ |
| [4] | Carding Action 2020: Group-IB supports Europol-backed operation saving EUR 40 million | Group-IB | 2020-11-26 | https://www.group-ib.com/it/media-center/press-releases/carding-action-2020/ |
| [5] | Europol and partners thwart credit card fraud scheme | WeLiveSecurity | 2020-11-27 | https://www.welivesecurity.com/2020/11/27/europol-partners-thwart-credit-card-fraud-scheme/ |
| [6] | Officers foil fraudsters stealing EUR 40 million in payment card scam | Europol | 2020-11-26 | https://www.europol.europa.eu/newsroom/news/officers-foil-fraudsters-stealing-%E2%82%AC40-million-in-payment-card-scam |
