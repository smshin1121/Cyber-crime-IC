---
type: operation
title: "Operation Onymous"
aliases:
  - "Op Onymous"
case_id: CYB-2014-001
period: 1
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2014-11-07
  start: 2014-05-01
  end: 2014-11-06
  ongoing: false
crime_type: "[[online-fraud-ic|Online Fraud]]"
target_entity: "Silk Road 2.0, Cloud 9, Hydra, and other Tor hidden services"
lead_agency: "[[fbi-cyber-division|FBI]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[united-states|United States]]"
  - "[[united-kingdom|United Kingdom]]"
  - "[[bulgaria|Bulgaria]]"
  - "[[czech-republic|Czech Republic]]"
  - "[[finland|Finland]]"
  - "[[france|France]]"
  - "[[germany|Germany]]"
  - "[[hungary|Hungary]]"
  - "[[ireland|Ireland]]"
  - "[[latvia|Latvia]]"
  - "[[lithuania|Lithuania]]"
  - "[[luxembourg|Luxembourg]]"
  - "[[netherlands|Netherlands]]"
  - "[[romania|Romania]]"
  - "[[spain|Spain]]"
  - "[[sweden|Sweden]]"
  - "[[switzerland|Switzerland]]"
participating_agencies:
  - "[[fbi-cyber-division|FBI]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust|Eurojust]]"
  - "[[us-dhs|U.S. Department of Homeland Security]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention]]"
  - "U.S. Computer Fraud and Abuse Act"
  - "EU Framework Decision 2005/222/JHA on attacks against information systems"
mechanisms_used:
  - "[[joint-investigation-team|Joint Investigation Team]]"
  - "[[mutual-legal-assistance|Mutual Legal Assistance]]"
  - "[[informal-cooperation|Informal Police-to-Police Cooperation]]"
results:
  arrests: 17
  indictments: 0
  servers_seized: 0
  domains_seized: 267
  cryptocurrency_seized: "USD 1 million in Bitcoin"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "267 .onion addresses seized across 27 separate sites"
    - "Silk Road 2.0 shut down"
    - "Cloud 9 and Hydra marketplaces shut down"
    - "Blake Benthall (Silk Road 2.0 operator) arrested in San Francisco"
    - "Drugs, weapons, cash, and computers seized"
edges:
  - source_actor: FBI
    target_actor: "Europol EC3"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: FBI
    target_actor: Eurojust
    cooperation_type: info_sharing
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: FBI
    target_actor: "US DHS/ICE"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: "UK NCA"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:

related_cases:
  - "[[us-v-benthall-silk-road-2]]"
  - "[[us-v-farrell-silk-road-2]]"
  - "[[us-v-paiva-silk-road-2]]"
related_operations:
  - "[[operation-us-v-benthall-silk-road-2]]"
  - "[[operation-us-v-farrell-silk-road-2]]"
  - "[[operation-us-v-paiva-silk-road-2]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional Conflicts]]"
  - "[[data-sovereignty|Data Sovereignty]]"
lessons_learned:
  - "Tor hidden services are not immune to law enforcement deanonymization"
  - "Undercover infiltration of marketplace staff provides critical intelligence"
  - "Large-scale coordinated takedowns send a strong deterrence signal but may not permanently suppress darknet markets"
  - "Investigation methods that exploit Tor vulnerabilities raise significant research ethics and civil liberties concerns"
source_count: 5
sources:
  - "[Europol IOCTA 2015 — Darknets](https://www.europol.europa.eu/iocta/2015/darknets.html)"
  - "[Wikipedia — Operation Onymous](https://en.wikipedia.org/wiki/Operation_Onymous)"
  - "[FBI press release — Silk Road 2.0 Charged](https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/operator-of-silk-road-2.0-website-charged-in-manhattan-federal-court)"
  - "[ICE press release — International probe leads to arrest](https://www.ice.gov/news/releases/international-probe-leads-arrest-alleged-operator-silk-road-20)"
  - "[GDPO Situation Analysis (Jan 2015)](https://www.swansea.ac.uk/media/Operation-Onymous.pdf)"
created: 2026-04-10
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "Operation Onymous was a joint international law enforcement operation conducted on 5-6 November 2014 by the [[fbi-cyber-division|FBI]], [[europol-ec3|Europol]], [[eurojust|Eurojust]], and the [[us-dhs|U.S. Department of Homeland Security]], targeting darknet markets and other hidden services on the Tor network. The operation resulted in the seizure of 267 .onion addresses across 27 distinct websites — including Silk Road 2.0, Cloud 9, and Hydra — the arrest of 17 individuals, and the seizure of approximately USD 1 million in Bitcoin along with cash, drugs, weapons, and computers. Blake Benthall, the alleged operator of Silk Road 2.0 (pseudonym \"Defcon\"), was arrested in San Francisco. The operation involved 17 European countries plus the United States and represented the largest coordinated action against Tor hidden services at the time. However, it also generated significant controversy regarding the methods used to deanonymize Tor hidden services, including questions about a possible Carnegie Mellon University research exploit."
jurisdictions:
  - "[[united-states|United States]]"
  - "[[united-kingdom|United Kingdom]]"
  - "[[bulgaria|Bulgaria]]"
  - "[[czech-republic|Czech Republic]]"
  - "[[finland|Finland]]"
  - "[[france|France]]"
  - "[[germany|Germany]]"
  - "[[hungary|Hungary]]"
  - "[[ireland|Ireland]]"
  - "[[latvia|Latvia]]"
  - "[[lithuania|Lithuania]]"
  - "[[luxembourg|Luxembourg]]"
  - "[[netherlands|Netherlands]]"
  - "[[romania|Romania]]"
  - "[[spain|Spain]]"
  - "[[sweden|Sweden]]"
  - "[[switzerland|Switzerland]]"
organizations:
  - "[[fbi-cyber-division|FBI]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[eurojust|Eurojust]]"
  - "[[us-dhs|U.S. Department of Homeland Security]]"
crime_types:
  - "[[online-fraud-ic|Online Fraud]]"
  - "[[dark-web-ic]]"
---
## Summary

Operation Onymous was a joint international law enforcement operation conducted on 5-6 November 2014 by the [[fbi-cyber-division|FBI]], [[europol-ec3|Europol]], [[eurojust|Eurojust]], and the [[us-dhs|U.S. Department of Homeland Security]], targeting darknet markets and other hidden services on the Tor network. The operation resulted in the seizure of 267 .onion addresses across 27 distinct websites — including Silk Road 2.0, Cloud 9, and Hydra — the arrest of 17 individuals, and the seizure of approximately USD 1 million in Bitcoin along with cash, drugs, weapons, and computers. Blake Benthall, the alleged operator of Silk Road 2.0 (pseudonym "Defcon"), was arrested in San Francisco. The operation involved 17 European countries plus the United States and represented the largest coordinated action against Tor hidden services at the time. However, it also generated significant controversy regarding the methods used to deanonymize Tor hidden services, including questions about a possible Carnegie Mellon University research exploit.

## Background

### Darknet Market Landscape in 2014

Operation Onymous took place in the aftermath of the [[silk-road-takedown|original Silk Road takedown]] in October 2013 and the arrest of its founder Ross Ulbricht. Following Silk Road's closure, numerous successor marketplaces emerged on the Tor network, with Silk Road 2.0 launching within weeks of the original's seizure. By mid-2014, dozens of darknet marketplaces were operating, creating a perception that law enforcement's ability to act against Tor-based criminality was limited.

### Silk Road 2.0

Silk Road 2.0 launched in November 2013 and was operated by Blake Benthall, a 26-year-old former SpaceX employee, under the pseudonym "Defcon." The marketplace replicated the functionality of the original Silk Road, facilitating sales of illegal drugs, weapons, forged documents, and other contraband. By November 2014, the site was generating millions of dollars in monthly sales and had attracted thousands of vendors and buyers.

### Investigation Methods

The FBI's investigation of Silk Road 2.0 involved multiple techniques:

1. **Undercover infiltration**: An HSI (Homeland Security Investigations) special agent successfully infiltrated the support staff running Silk Road 2.0, gaining access to private administrative areas and interacting directly with Benthall
2. **Server identification**: Government investigators located the Silk Road 2.0 server in a foreign country and briefly took it offline to make a copy. The resulting automated notification emails were sent to Benthall's personal email, which Google then linked to the server via IP address records
3. **Tor deanonymization**: The FBI stated it deanonymized Benthall's identity in May 2014, which coincided with a period when researchers from Carnegie Mellon University's CERT/CC had identified a vulnerability in the Tor network (active approximately February to July 2014)

## Participating Parties

### Lead Agencies
- **[[fbi-cyber-division|FBI]]** — led the Silk Road 2.0 investigation and coordinated U.S. actions
- **[[europol-ec3|Europol EC3]]** — coordinated European law enforcement actions

### U.S. Agencies
| Agency | Role |
|--------|------|
| [[fbi-cyber-division\|FBI]] | Lead U.S. investigation, Benthall arrest |
| [[us-dhs\|DHS / HSI (ICE)]] | Undercover infiltration of Silk Road 2.0 |
| [[eurojust\|Eurojust]] | Judicial coordination for European actions |

### European Countries (16)
[[bulgaria|Bulgaria]], [[czech-republic|Czech Republic]], [[finland|Finland]], [[france|France]], [[germany|Germany]], Hungary, [[ireland|Ireland]], [[latvia|Latvia]], [[lithuania|Lithuania]], Luxembourg, [[netherlands|Netherlands]], [[romania|Romania]], [[spain|Spain]], [[sweden|Sweden]], [[switzerland|Switzerland]], [[united-kingdom|United Kingdom]]

> [!note] Country count discrepancy
> Europol announced "17 countries" participated in Operation Onymous. The 16 European countries listed above plus the United States account for 17. Some sources state "21 countries" participated; the discrepancy likely arises from counting additional non-European partner countries whose participation has not been individually confirmed in official press releases.

## Legal Framework

- **[[budapest-convention|Budapest Convention]]** — provided the primary framework for cross-border cooperation among European participants, many of whom are parties to the Convention
- **U.S. Computer Fraud and Abuse Act (18 U.S.C. § 1030)** — basis for federal charges against Benthall
- **EU Framework Decision 2005/222/JHA** — on attacks against information systems, providing harmonized offense definitions for EU member states
- **National criminal laws** — each participating country executed seizure orders under domestic law

The charges against Blake Benthall were filed in the Southern District of New York (Manhattan Federal Court) and included conspiracy to commit narcotics trafficking, conspiracy to commit computer hacking, and money laundering.

## Operational Timeline

| Date | Event |
|------|-------|
| 2013-10 | Original [[silk-road-takedown\|Silk Road takedown]]; Ross Ulbricht arrested |
| 2013-11 | Silk Road 2.0 launches under Blake Benthall ("Defcon") |
| 2014-05 | FBI claims to have deanonymized Benthall's identity |
| 2014-02 to 2014-07 | Carnegie Mellon CERT/CC Tor vulnerability reportedly active |
| 2014-07-04 | Tor Project patches the vulnerability exploited by CERT researchers |
| 2014-11-05 | Blake Benthall arrested in San Francisco |
| 2014-11-05 to 11-06 | Coordinated takedown of 267 .onion addresses across 27 sites |
| 2014-11-07 | FBI and Europol announce Operation Onymous publicly |
| 2015-11 | Court documents raise questions about CERT/Tor vulnerability exploitation |

## Results and Impact

### Quantitative Results
- **17 arrests** across participating countries
- **267 .onion addresses seized** across 27 distinct hidden service websites
- **USD 1 million** in Bitcoin seized
- **Cash, drugs, weapons, and computers** seized (specific quantities not publicly aggregated)
- **Key marketplaces shut down**: Silk Road 2.0, Cloud 9, Hydra (not to be confused with the later Russian-language Hydra marketplace shut down in 2022)

### Key Arrest: Blake Benthall
Blake Benthall was arrested in San Francisco on November 5, 2014, and charged in Manhattan Federal Court with conspiracy to commit narcotics trafficking, computer hacking conspiracy, and money laundering. He was accused of operating Silk Road 2.0 under the pseudonym "Defcon."

### Deterrence Impact
Operation Onymous sent a strong signal that Tor-based hidden services were not immune to law enforcement action. In the immediate aftermath:
- Several darknet marketplaces voluntarily shut down
- Forum discussions reflected increased uncertainty among operators and users about Tor's security
- The Tor Project itself published a blog post expressing concern about the methods used

### Limitations
Despite the scale of the operation, new darknet marketplaces continued to emerge. The "whack-a-mole" pattern persisted, with [[alphabay-takedown|AlphaBay]] and other successors quickly filling the void left by Silk Road 2.0 and the other seized sites.

## Cooperation Mechanisms Used

1. **[[joint-investigation-team|Joint Investigation Team]]** — likely employed for the coordinated European actions, though specific JIT details are not publicly documented
2. **[[mutual-legal-assistance|Mutual Legal Assistance]]** — formal MLA requests for cross-border evidence gathering and server identification
3. **[[informal-cooperation|Informal Police-to-Police Cooperation]]** — real-time intelligence exchange between FBI and European law enforcement through Europol's secure communication channels
4. **[[eurojust|Eurojust]]** judicial coordination — enabled simultaneous legal actions across 16 European jurisdictions
5. **Undercover operations** — HSI agent infiltration of Silk Road 2.0 staff was a key intelligence source

## Challenges and Friction Points

### Tor Deanonymization Controversy
The most significant controversy surrounding Operation Onymous concerns the methods used to identify hidden service operators and server locations. Court documents released in November 2015 revealed that:

- The FBI's deanonymization of hidden services occurred in May 2014, during the same period when Carnegie Mellon University's CERT/CC had identified and was exploiting a vulnerability in the Tor network
- The Tor Project patched this vulnerability on July 4, 2014
- In November 2015, the Tor Project publicly alleged that the FBI had paid Carnegie Mellon USD 1 million to exploit the Tor vulnerability and identify hidden service users, which the FBI denied
- The episode raised significant questions about research ethics, the boundary between academic security research and law enforcement assistance, and whether warrantless exploitation of Tor constitutes an illegal search

### Scale Discrepancies
Initial claims stated "over 400" hidden service websites were seized. The actual confirmed number was 267 .onion addresses across 27 distinct sites. The discrepancy appears to result from counting individual .onion addresses (including mirrors and duplicates) versus distinct website operations.

### Jurisdictional Complexity
With 17+ countries involved and seizures of infrastructure hosted across multiple jurisdictions, the operation required extensive pre-coordination to ensure legal validity of seizure orders in each jurisdiction. The specific challenges encountered have not been publicly documented in detail.

## Lessons Learned

1. **Tor is not impervious**: Operation Onymous demonstrated that law enforcement possesses or can acquire the capability to deanonymize Tor hidden services, fundamentally changing the risk calculus for darknet marketplace operators.
2. **Undercover infiltration remains highly effective**: The human intelligence component (undercover agent on Silk Road 2.0 staff) provided critical evidence that technical methods alone might not have yielded.
3. **Coordinated multi-country takedowns have deterrent value**: The scale of Operation Onymous — 17 countries, 27 sites, 17 arrests — generated significant media coverage and demonstrably affected darknet operator behavior, at least temporarily.
4. **Investigation methods require transparency**: The CERT/Tor controversy underscored the importance of transparent legal process in cyber investigations, as questions about the legality of the deanonymization method could have undermined prosecutions.
5. **Market displacement persists**: Despite the operation's scale, darknet markets quickly reconstituted, indicating that takedowns alone cannot eliminate the phenomenon without addressing underlying demand.

## Korean Involvement (한국의 참여)

There is no publicly reported Korean involvement in Operation Onymous. The operation predates [[south-korea|South Korea's]] increased engagement in international cybercrime cooperation frameworks. However, the operation is relevant to Korea as:

- A foundational case demonstrating the feasibility of large-scale international cooperation against darknet criminality
- A precursor to later operations in which Korean agencies have participated
- A study in the legal and ethical challenges of Tor deanonymization that Korean law enforcement will likely encounter in future investigations

## Contradictions & Open Questions

- **Carnegie Mellon / FBI relationship**: The exact nature of the relationship between Carnegie Mellon's CERT/CC and the FBI remains disputed. The FBI denied paying USD 1 million, but has not provided an alternative explanation for how the Tor vulnerability was exploited in coordination with law enforcement. The Tor Project maintains its allegation.
- **Country count**: Sources variously report 17, 18, or 21 countries participating. The discrepancy has not been officially clarified.
- **Hidden service count**: The initially claimed "400+" sites was revised to 267 .onion addresses / 27 sites. The reason for the original inflation is unclear.
- **Legal validity of evidence**: If the Tor deanonymization relied on an exploit developed without a warrant, the admissibility of evidence derived from it could be challenged. The resolution of this legal question in the Benthall case is not widely documented.
- **Benthall case outcome**: The final disposition of Blake Benthall's case after his arrest has received limited public reporting. His plea and sentencing outcomes are not clearly documented in available sources.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2015-01-01: IOCTA 2015 — Darknets.
- Wikipedia, 2026-04-17: Operation Onymous.
- FBI, 2014-11-06: Operator of Silk Road 2.0 Website Charged in Manhattan Federal Court.
- ICE / HSI, 2014-11-06: International probe leads to the arrest of the alleged operator of "Silk Road 2.0".
- Swansea University, 2015-01-01: GDPO Situation Analysis — Operation Onymous.

## Evidence and Attribution Notes

- Operation Onymous was a joint international law enforcement operation conducted on 5-6 November 2014 by the FBI, Europol, Eurojust, and the U.S. Department of Homeland Security, targeting darknet markets and other hidden services on the Tor network.
- The operation resulted in the seizure of 267 .onion addresses across 27 distinct websites — including Silk Road 2.0, Cloud 9, and Hydra — the arrest of 17 individuals, and the seizure of approximately USD 1 million in Bitcoin along with cash, drugs, weapons, and computers.
- Blake Benthall, the alleged operator of Silk Road 2.0 (pseudonym "Defcon"), was arrested in San Francisco.
- The operation involved 17 European countries plus the United States and represented the largest coordinated action against Tor hidden services at the time.
- However, it also generated significant controversy regarding the methods used to deanonymize Tor hidden services, including questions about a possible Carnegie Mellon University research exploit.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | IOCTA 2015 — Darknets | Europol | 2015 | [Link](https://www.europol.europa.eu/iocta/2015/darknets.html) |
| 2 | Operation Onymous | Wikipedia | (ongoing) | [Link](https://en.wikipedia.org/wiki/Operation_Onymous) |
| 3 | Operator of Silk Road 2.0 Website Charged in Manhattan Federal Court | FBI | 2014-11-06 | [Link](https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/operator-of-silk-road-2.0-website-charged-in-manhattan-federal-court) |
| 4 | International probe leads to the arrest of the alleged operator of "Silk Road 2.0" | ICE / HSI | 2014-11-06 | [Link](https://www.ice.gov/news/releases/international-probe-leads-arrest-alleged-operator-silk-road-20) |
| 5 | GDPO Situation Analysis — Operation Onymous | Swansea University | 2015-01 | [Link](https://www.swansea.ac.uk/media/Operation-Onymous.pdf) |
