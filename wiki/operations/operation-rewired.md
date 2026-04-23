---
type: operation
title: "Operation reWired"
title_ko: "Operation reWired (BEC 글로벌 단속)"
aliases:
  - reWired
  - "Operation ReWired"
case_id: ""
period: 2
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - seizure
  - asset_freeze
outcome: success
timeframe:
  announced: 2019-09-10
  start: 2019-05
  end: 2019-09
  ongoing: false
crime_type: "[[bec-ic]]"
target_entity: "International Business Email Compromise (BEC) networks"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[us-doj|US Department of Justice]]"
participating_countries:
  - "[[united-states]]"
  - "[[nigeria]]"
  - "[[turkey]]"
  - "[[ghana]]"
  - "[[france]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[kenya]]"
  - "[[malaysia]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[us-doj|US Department of Justice]]"
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-secret-service|US Secret Service]]"
  - "[[us-dhs|US Department of Homeland Security]]"
  - "[[ic3|Internet Crime Complaint Center (IC3)]]"
legal_basis:
  - "[[mutual-legal-assistance|Mutual Legal Assistance]]"
mechanisms_used:
  - "[[mutual-legal-assistance|MLAT Process]]"
  - "[[informal-cooperation|Informal Police Cooperation]]"
results:
  arrests: 281
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  other:
    - "USD 3.7 million seized"
    - "USD 118 million in fraudulent wire transfers disrupted/recovered"
    - "214 domestic enforcement actions (arrests, warning letters, asset seizures)"
edges:
  - source_actor: FBI
    target_actor: "Nigeria EFCC"
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: FBI
    target_actor: Turkey
    cooperation_type: info_sharing
    legal_basis: MLAT
    direction: directed
  - source_actor: FBI
    target_actor: Ghana
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: directed
  - source_actor: FBI
    target_actor: UK
    cooperation_type: info_sharing
    legal_basis: MLAT
    direction: directed
  - source_actor: FBI
    target_actor: Japan
    cooperation_type: info_sharing
    legal_basis: MLAT
    direction: directed
credibility_index: 4.5
source_tier: 1
missing_fields:
  - case_id
related_operations:
  - "[[operation-wirewire|Operation WireWire (2018)]]"
  - "[[operation-falcon|Operation Falcon]]"
  - "[[black-axe-bec-2021|Black Axe BEC 2021]]"
  - "[[nigerian-bec-convictions-2023|Nigerian BEC Convictions 2023]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional complexity of BEC schemes]]"
lessons_learned:
  - "FBI-EFCC bilateral cooperation was critical for arrests in Nigeria"
  - "Follow-the-money approach through financial institutions is essential for BEC cases"
  - "Successor to Operation WireWire showed value of repeating coordinated sweeps"
source_count: 5
sources:
  - "[[2019-09-10_fbi-gov_operation-rewired-bec-takedown]]"
  - "[[2019-09-10_justice-gov_281-arrested-worldwide-coordinated-international-enforcement-operation-targeting-hundreds]]"
  - "[[2019-09-10_secretservice-gov_281-arrested-worldwide-coordinated-international-enforcement-operation]]"
  - "[[2019-09-11_scworld-com_operation-rewired-campaign]]"
  - "[[2019-09-10_wired-com_email-scammer-global-takedown]]"
created: 2026-04-10
updated: 2026-04-11
operation_role: umbrella
parent_operation: ""
summary: "Operation reWired was a coordinated international law enforcement operation targeting Business Email Compromise (BEC) schemes, announced on 10 September 2019. Led by the [[fbi-cyber-division|FBI]] and coordinated by the [[us-doj|US Department of Justice]] through the International Organized Crime Intelligence and Operations Center (IOC-2), the four-month operation resulted in 281 arrests across 10 countries, the seizure of approximately USD 3.7 million, and the disruption or recovery of approximately USD 118 million in fraudulent wire transfers. The operation was the successor to [[operation-wirewire|Operation WireWire]] (2018) and represented the largest coordinated BEC enforcement action at the time."
jurisdictions:
  - "[[united-states]]"
  - "[[nigeria]]"
  - "[[turkey]]"
  - "[[ghana]]"
  - "[[france]]"
  - "[[italy]]"
  - "[[japan]]"
  - "[[kenya]]"
  - "[[malaysia]]"
  - "[[united-kingdom]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[us-doj|US Department of Justice]]"
  - "[[us-secret-service|US Secret Service]]"
  - "[[us-dhs|US Department of Homeland Security]]"
  - "[[ic3|Internet Crime Complaint Center (IC3)]]"
crime_types:
  - "[[bec-ic]]"
---
## Summary

Operation reWired was a coordinated international law enforcement operation targeting Business Email Compromise (BEC) schemes, announced on 10 September 2019. Led by the [[fbi-cyber-division|FBI]] and coordinated by the [[us-doj|US Department of Justice]] through the International Organized Crime Intelligence and Operations Center (IOC-2), the four-month operation resulted in 281 arrests across 10 countries, the seizure of approximately USD 3.7 million, and the disruption or recovery of approximately USD 118 million in fraudulent wire transfers. The operation was the successor to [[operation-wirewire|Operation WireWire]] (2018) and represented the largest coordinated BEC enforcement action at the time.

## Background

[[bec-ic|Business Email Compromise (BEC)]] is a sophisticated cyber-enabled financial fraud in which criminals use social engineering, phishing, and computer intrusions to compromise legitimate business email accounts and redirect wire transfers to accounts under their control. By 2019, the [[ic3|Internet Crime Complaint Center (IC3)]] had received reports of more than USD 10 billion in BEC-related losses from US victims alone, with the worldwide figure exceeding USD 26 billion since tracking began in 2013.

In 2018, the FBI conducted [[operation-wirewire|Operation WireWire]], the first coordinated BEC enforcement sweep, which resulted in 74 arrests and the recovery of USD 14 million. Building on that precedent, Operation reWired was designed as a larger, more ambitious successor targeting BEC networks spanning multiple continents, with a particular focus on the [[nigeria|Nigeria]]-to-[[united-states|United States]] BEC corridor.

The operation was funded and coordinated through the DOJ's IOC-2, a multi-agency fusion centre that combines resources from federal law enforcement to tackle transnational organized crime.

## Participating Parties

### US Federal Agencies

| Agency | Role |
|--------|------|
| [[fbi-cyber-division|FBI]] | Lead agency; 39 of 56 field offices participated |
| [[us-doj|US Department of Justice]] | Overall coordination via IOC-2 |
| [[us-secret-service|US Secret Service]] | Financial crime investigation |
| [[us-dhs|Department of Homeland Security]] | Immigration and Customs Enforcement support |
| US Department of the Treasury | Financial intelligence |
| US Postal Inspection Service | Mail fraud component |
| US Department of State | International coordination |
| Internal Revenue Service (IRS) | Tax fraud and financial analysis |

### International Law Enforcement Partners

| Country | Agency | Arrests |
|---------|--------|---------|
| [[united-states]] | FBI, USSS, and federal/state task forces | 74 |
| [[nigeria]] | Economic and Financial Crimes Commission (EFCC) | 167 |
| [[turkey]] | Turkish National Police | 18 |
| [[ghana]] | Ghana Police Service | 15 |
| [[france]] | French law enforcement | Number undisclosed |
| [[italy]] | Italian law enforcement | Number undisclosed |
| [[japan]] | [[japan-npa|Japanese law enforcement]] | Number undisclosed |
| [[kenya]] | Kenyan law enforcement | Number undisclosed |
| [[malaysia]] | [[malaysia-police|Malaysian law enforcement]] | Number undisclosed |
| [[united-kingdom]] | [[uk-nca|UK law enforcement]] | Number undisclosed |

> [!note] Arrest distribution
> The DOJ press release confirmed 281 total arrests. Country-specific arrest counts were disclosed for the US (74), Nigeria (167), Turkey (18), and Ghana (15), totalling 274. The remaining 7 arrests were distributed among France, Italy, Japan, Kenya, Malaysia, and the UK but individual country totals were not specified.

## Legal Framework

The operation leveraged multiple legal mechanisms:

- **[[mutual-legal-assistance|Mutual Legal Assistance Treaty (MLAT)]]** requests for formal evidence gathering and asset seizure across jurisdictions
- **FBI Legal Attache (Legat) network**: The FBI's overseas offices facilitated coordination with host-country law enforcement
- **Bilateral agreements**: The FBI-EFCC cooperation in Nigeria operated through a bilateral partnership framework that had been strengthened through prior engagements including [[operation-wirewire|Operation WireWire]]
- US domestic law: 18 U.S.C. ss 1343 (wire fraud), 18 U.S.C. ss 1956 (money laundering), 18 U.S.C. ss 1030 (computer fraud and abuse)

## Operational Timeline

| Date | Event |
|------|-------|
| May 2019 | Operation reWired commenced; coordinated investigation phase began |
| May-Sep 2019 | FBI field offices, working with state/local task forces, developed cases against BEC networks |
| May-Sep 2019 | International coordination with EFCC and other foreign partners |
| Sep 2019 | Coordinated arrest sweep executed across 10 countries |
| 2019-09-10 | DOJ and FBI publicly announced results: 281 arrests, USD 3.7M seized, USD 118M disrupted/recovered |

## Results and Impact

### Enforcement Results

| Metric | Value |
|--------|-------|
| Total arrests | 281 |
| US arrests | 74 |
| Nigeria arrests (EFCC) | 167 |
| Turkey arrests | 18 |
| Ghana arrests | 15 |
| Other countries (FR, IT, JP, KE, MY, UK) | 7 |
| US domestic enforcement actions | 214 |
| Cash seized | ~USD 3.7 million |
| Fraudulent wire transfers disrupted/recovered | ~USD 118 million |

### EFCC-Specific Results

Nigeria's EFCC reported recovering USD 169,850 and NGN 92,000,000 (approximately USD 250,000) from suspected BEC perpetrators as part of their contribution to the operation.

### Comparison with Predecessor

| Metric | WireWire (2018) | reWired (2019) |
|--------|-----------------|----------------|
| Total arrests | 74 | 281 |
| Cash seized | ~USD 2.4M | ~USD 3.7M |
| Wire transfers recovered | ~USD 14M | ~USD 118M |
| Countries | 5 | 10 |

The significant increase across all metrics likely reflects both the growing scale of BEC crime and improved international coordination mechanisms.

## Cooperation Mechanisms Used

1. **[[mutual-legal-assistance|Mutual Legal Assistance]]**: Formal MLAT requests were used for evidence gathering and asset seizure in jurisdictions requiring judicial authorization.

2. **[[informal-cooperation|Informal Police-to-Police Cooperation]]**: The FBI's Legat network enabled rapid information sharing with foreign counterparts, particularly the FBI Legal Attache in Lagos (established 2015) for coordination with the EFCC.

3. **IOC-2 Fusion Centre**: The DOJ's International Organized Crime Intelligence and Operations Center served as the operational hub, combining intelligence from multiple US agencies.

4. **Financial institution cooperation**: Banks and financial institutions assisted in identifying suspicious wire transfers and freezing accounts.

## Challenges and Friction Points

- **Scale of BEC globally**: Even with 281 arrests, BEC losses continued to grow after the operation, suggesting that enforcement alone is insufficient to deter the crime.
- **[[jurisdictional-conflicts|Jurisdictional complexity]]**: BEC schemes typically involve email compromise in one country, victim organizations in another, money mule networks in a third, and ultimate beneficiaries in a fourth, creating complex multi-jurisdictional investigations.
- **Money mule networks**: Many US-based arrests involved money mules rather than scheme organizers, raising questions about whether the operation reached the highest levels of BEC networks.
- **Extradition challenges**: Most Nigeria-based arrests were handled by the EFCC under Nigerian law rather than through extradition to the US, resulting in potentially lighter sentences.

## Lessons Learned

1. **Bilateral partnerships are force multipliers**: The FBI-EFCC partnership, strengthened over successive operations ([[operation-wirewire|WireWire]] then reWired), enabled arrest of BEC perpetrators in their home country -- a capability the FBI cannot achieve unilaterally.

2. **Repeat coordinated sweeps**: Building on [[operation-wirewire|Operation WireWire]] demonstrated that recurring enforcement actions amplify deterrence and build institutional cooperation capacity.

3. **Follow-the-money approach**: Recovery of USD 118 million in fraudulent transfers showed that financial intelligence and rapid bank notification are critical to mitigating BEC losses even when arrests are delayed.

4. **Whole-of-government approach**: The involvement of seven US federal agencies (FBI, USSS, DHS, Treasury, USPIS, State, IRS) demonstrated that BEC investigation requires cross-functional collaboration beyond traditional cybercrime units.

## Korean Involvement (한국의 참여)

No [[south-korea|South Korean]] participation in Operation reWired has been publicly documented. However, South Korea is a significant BEC target, and Korean companies -- particularly those engaged in international trade -- have reported losses to BEC schemes. The [[knpa|Korean National Police Agency]] has investigated BEC cases with international dimensions, but formal participation in US-led BEC sweeps has not been publicly reported.

## Contradictions & Open Questions

- **Arrest quality vs. quantity**: Media reports noted that many US arrests were of money mules rather than BEC scheme organizers. The long-term impact on BEC networks requires further assessment.
- **Nigeria arrest details**: The EFCC reported only USD 169,850 and NGN 92 million recovered from 167 arrests, suggesting many arrestees may have been low-level operatives.
- **Disposition of cases**: The final judicial outcomes (convictions, sentences, acquittals) for the 281 arrestees have not been comprehensively tracked in public reporting.
- **Japanese participation**: The inclusion of [[japan]] is notable as the only East Asian country in the operation, but no details of Japanese arrests or cooperation have been publicly disclosed.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Operation reWired | FBI | 2019-09-10 | https://www.fbi.gov/news/stories/operation-rewired-bec-takedown-091019 |
| [2] | 281 Arrested Worldwide in Coordinated International Enforcement Operation Targeting Hundreds of Individuals in Cyber-Enabled Financial Fraud | U.S. Department of Justice | 2019-09-10 | https://www.justice.gov/archives/opa/pr/281-arrested-worldwide-coordinated-international-enforcement-operation-targeting-hundreds |
| [3] | 281 Arrested Worldwide in Coordinated International Enforcement Operation Targeting Hundreds of Individuals in Cyber-enabled Financial Fraud | U.S. Secret Service | 2019-09-10 | https://www.secretservice.gov/press/releases/2019/09/281-arrested-worldwide-coordinated-international-enforcement-operation |
| [4] | Authorities arrest 281 alleged BEC scammers in Operation reWired campaign | SC Media | 2019-09-11 | https://www.scworld.com/news/authorities-arrest-281-alleged-bec-scammers-in-operation-rewired-campaign |
| [5] | 281 Alleged Email Scammers Arrested in Massive Global Sweep | Wired | 2019-09-10 | https://www.wired.com/story/email-scammer-global-takedown |
