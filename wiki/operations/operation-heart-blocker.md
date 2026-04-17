---
type: operation
title: "Operation Heart Blocker"
title_ko: "하트 블로커 작전"
aliases:
  - "Heart Blocker"
  - "HeartSender Takedown"
  - "Saim Raza Takedown"
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - arrest
  - indictment
outcome: success
timeframe:
  announced: 2025-01-29
  start: 2025-01-29
  end: 2025-05-16
  ongoing: false
crime_type: "[[bec-ic|Business Email Compromise (BEC)]]"
target_entity: "HeartSender / Saim Raza cybercrime marketplace network"
lead_agency: "[[us-doj|U.S. Department of Justice]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[pakistan]]"
participating_agencies:
  - "[[us-doj|U.S. Department of Justice]]"
  - "[[fbi-cyber-division|FBI Cyber Division]]"
  - "[[netherlands-politie|Dutch National Police (Politie)]]"
  - "[[pakistan-fia|Pakistan Federal Investigation Agency (FIA / NCCIA)]]"
legal_basis:
  - "[[mlat-process|US-Netherlands MLAT]]"
mechanisms_used:
  - "[[mlat-process|Mutual Legal Assistance]]"
  - "[[informal-cooperation|Informal Police-to-Police Cooperation]]"
results:
  arrests: 21
  indictments: 0
  servers_seized: 39
  domains_seized: 39
  cryptocurrency_seized: ""
  other:
    - "Millions of victim records recovered from seized servers"
    - "At least 100,000 records pertaining to Dutch citizens"
    - "$3 million in confirmed US victim losses (DOJ estimate)"
    - "$50 million+ in US losses (Pakistan NCCIA estimate)"
    - "63 additional European cases under investigation"
    - "21 suspects arrested in Pakistan (May 2025 follow-up)"
    - "Instructional YouTube videos used for training removed"
source_count: 5
related_cases:
  - "[[in-re-heartsender-seizure]]"
sources:
  - "[1] US DOJ Press Release (2025-01-29)"
  - "[2] KrebsOnSecurity (2025-01-30)"
  - "[3] KrebsOnSecurity — Pakistan Arrests (2025-05-28)"
  - "[4] CyberScoop (2025-01-30)"
  - "[5] Hackread (2025-01-30)"
created: 2026-04-10
updated: 2026-04-10
related_operations:
  - "[[operation-in-re-heartsender-seizure]]"
---
## Summary

Operation Heart Blocker was a joint US-Dutch law enforcement action on January 29, 2025, targeting the HeartSender cybercrime marketplace network (also known as Saim Raza). The U.S. Department of Justice and the Dutch National Police coordinated the seizure of 39 domains and their associated servers that had been operating since at least 2020 as marketplaces selling phishing kits, credential-stealing tools, email extractors, and scam page generators. These tools were used by transnational organized crime groups to conduct [[bec-ic|business email compromise (BEC)]] schemes, resulting in over $3 million in confirmed US victim losses according to the DOJ (later revised to over $50 million by Pakistan's NCCIA).

In a significant follow-up action in May 2025, Pakistan's National Cyber Crime Investigation Agency (NCCIA) arrested 21 individuals linked to the operation, including alleged ringleader Rameez Shahzad (alias "Saim Raza"), demonstrating a rare instance of a Pakistan-based cybercrime network being disrupted through coordinated international action.

## Background

The HeartSender network was operated by a group known alternately as **Saim Raza**, **The Manipulaters**, and more recently under the Pakistani front company **WeCodeSolutions**. The group had been under law enforcement scrutiny for nearly a decade, having been profiled by cybersecurity journalist Brian Krebs as early as 2015.

The Saim Raza-run websites operated as open marketplaces — not on the dark web but on the clear internet — advertising and selling cybercrime-as-a-service tools under brands including:
- **HeartSender** — email and SMS spamming tools
- **Fudtools** — "Fully Un-Detectable" phishing kits
- **Fudpage** — scam landing pages mimicking legitimate services
- **Fudsender** — bulk email delivery tools
- **FudCo** — additional fraud tools

Beyond selling tools, the group provided **instructional YouTube videos** teaching purchasers with little technical expertise how to deploy the tools against victims — effectively democratizing BEC fraud.

The primary victims of downstream attacks were users of Microsoft 365, Yahoo, AOL, Intuit, iCloud, and ID.me services.

## Participating Parties

**Lead Agency:**
- [[us-doj|U.S. Department of Justice]] — seizure warrants and coordination

**Key Partners:**
- [[fbi-cyber-division|FBI Cyber Division]] — investigation and execution
- [[netherlands-politie|Dutch National Police (Politie)]] — server seizure, victim data analysis, coordination with European cases
- [[pakistan-fia|Pakistan FIA / NCCIA]] — domestic arrests of suspects (May 2025 follow-up)

**Participating Countries (3):**
United States, Netherlands, Pakistan

## Legal Framework

The operation was conducted under US federal computer fraud and wire fraud statutes. The seizure warrants were issued by US courts, and the Dutch National Police executed seizures under mutual legal assistance arrangements.

Key legal instruments:
- US Computer Fraud and Abuse Act (18 U.S.C. Section 1030)
- US Wire Fraud statute (18 U.S.C. Section 1343)
- [[mlat-process|US-Netherlands Mutual Legal Assistance Treaty]] — for cross-border server seizure coordination
- Pakistan Prevention of Electronic Crimes Act (PECA) 2016 — basis for NCCIA arrests

> [!note] Legal Basis Note
> The DOJ press release described this as a "coordinated" action with the Dutch National Police. The specific legal instrument enabling Dutch participation was not explicitly stated but is *likely* the US-Netherlands MLAT or an equivalent bilateral cooperation agreement. The Dutch simultaneously seized servers within their jurisdiction.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2015 | Group begins operations as "The Manipulaters" (per KrebsOnSecurity reporting) |
| ~2020 | HeartSender / Saim Raza marketplace becomes operational |
| 2025-01-29 | **Operation Heart Blocker executed**: US DOJ and Dutch National Police seize 39 domains and associated servers |
| 2025-01-29 | DOJ announces seizure; seized domains display law enforcement takedown banner |
| 2025-01-30 | Dutch authorities confirm millions of victim records recovered, including 100,000+ Dutch citizen records |
| 2025-05-15 | Pakistan NCCIA raids in Lahore's Bahria Town targeting HeartSender Group |
| 2025-05-16 | NCCIA raids in Multan targeting southern operations hub |
| 2025-05-16 | 21 suspects arrested in Pakistan, including Rameez Shahzad (alias Saim Raza) |
| 2025-05 | Pakistan authorities revise victim losses estimate to over $50 million (US) |
| 2025-05 | European authorities disclose 63 additional cases under investigation |

## Results and Impact

**Phase 1 — Domain Seizure (January 2025):**
- 39 domains seized (US and Netherlands)
- 39 servers taken down
- Millions of victim records recovered
- 100,000+ records pertaining to Dutch citizens identified
- Takedown banners placed on seized domains
- Instructional YouTube content flagged

**Phase 2 — Pakistan Arrests (May 2025):**
- 21 suspects arrested across Lahore and Multan
- Key arrests:
  - **Rameez Shahzad** (alias Saim Raza) — alleged mastermind, Lahore
  - **Muhammad Aslam** — Rameez's father
  - **Hussnain Haider** — alleged Multan operations head
  - 18 additional associates
- WeCodeSolutions identified as corporate front

**Financial Impact:**
- DOJ initial estimate: over $3 million in US victim losses
- Pakistan NCCIA estimate: over $50 million in US losses
- 63 additional European cases under investigation

> [!warning] Loss Figure Discrepancy
> **Claim A** (Source: DOJ press release [1], reliability: high): Tools resulted in "over $3 million" in victim losses.
> **Claim B** (Source: Pakistan NCCIA via KrebsOnSecurity [3], reliability: medium): Group connected to "more than $50m in losses in the United States alone."
> **Assessment**: The $3 million figure *likely* represents confirmed, adjudicated losses attributable to specific BEC schemes linked to HeartSender tools. The $50 million figure *possibly* represents a broader estimate of total downstream losses from all tools sold through the marketplace. The actual figure is likely between these estimates.

## Cooperation Mechanisms Used

1. **[[mlat-process|Mutual Legal Assistance]]** — The US-Netherlands cooperation for cross-border domain and server seizure almost certainly relied on MLAT or equivalent bilateral arrangements.

2. **[[informal-cooperation|Informal Police-to-Police Cooperation]]** — The FBI had been tracking "The Manipulaters" for years, and coordination with Dutch authorities likely included informal intelligence sharing prior to the formal seizure.

3. **Subsequent Pakistan Cooperation** — The May 2025 arrests by Pakistan's NCCIA represented a follow-up action enabled by information from the domain seizure. This cooperation with Pakistan — which has historically been challenging for cybercrime enforcement — was a significant development.

## Challenges and Friction Points

1. **Extended timeline** — Despite the group being publicly known since ~2015 (profiled by KrebsOnSecurity), it took nearly a decade to execute enforcement action. This delay highlights the difficulty of acting against cybercrime operations in jurisdictions with limited enforcement capacity or willingness.

2. **Pakistan enforcement gap** — Until the May 2025 arrests, Pakistan-based cybercrime operations have been notoriously difficult to disrupt through international cooperation. The NCCIA arrests represent a *likely* positive shift, though sustainability of this enforcement posture remains to be seen.

3. **Cybercrime-as-a-service model** — Disrupting the marketplace does not eliminate the tools already distributed. Customers who previously purchased phishing kits may continue using them.

4. **Loss quantification** — The significant discrepancy between DOJ ($3M) and NCCIA ($50M) loss estimates illustrates the difficulty of attributing downstream fraud losses to a specific tool provider.

5. **Open-internet operation** — The fact that HeartSender operated openly on the clear internet (not dark web) with YouTube instructional videos raises questions about why platform providers (domain registrars, YouTube) did not act earlier.

## Lessons Learned

1. **Infrastructure seizure combined with arrests** produces the most comprehensive disruption. The January seizure disrupted operations; the May arrests in Pakistan disrupted the operators.

2. **Long-term intelligence gathering** was critical — the FBI's decade-long monitoring of the group enabled precise targeting of the network.

3. **Pakistan cooperation on cybercrime** is possible but appears to require sustained international pressure and clear evidence packages.

4. **Cybercrime-as-a-service requires upstream disruption** — prosecuting individual BEC operators is insufficient when tool providers enable thousands of attacks.

## Follow-Up Actions

- Pakistan NCCIA arrested 21 suspects in May 2025, including alleged ringleader Rameez Shahzad.
- European authorities are investigating 63 additional cases linked to HeartSender tools.
- Dutch authorities continue analysis of millions of victim records recovered from seized servers.
- It is unknown whether US indictments have been or will be filed against the Pakistan-based operators.

## Korean Involvement (한국의 참여)

No known Korean involvement in Operation Heart Blocker. However:
- BEC fraud is a global threat affecting Korean companies, particularly those engaged in international trade.
- The cybercrime-as-a-service model demonstrated by HeartSender is relevant to Korean law enforcement's understanding of the BEC ecosystem.
- Korean phishing victims using services like Microsoft 365 may have been impacted by tools sold through HeartSender.

## Contradictions & Open Questions

**Open Questions:**
1. Will US authorities seek extradition of Rameez Shahzad or other Pakistan-based suspects, or will prosecution proceed domestically in Pakistan?
2. What is the actual scale of losses attributable to HeartSender tools ($3M per DOJ vs. $50M+ per NCCIA)?
3. How many downstream BEC schemes globally relied on HeartSender tools?
4. Were domain registrars and YouTube notified about the criminal use of their platforms prior to the takedown? If so, why was no action taken?
5. What was the revenue earned by the HeartSender marketplace operators over its ~5 years of operation?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Justice Department Announces Seizure of Cybercrime Websites Selling Hacking Tools to Transnational Organized Crime Groups | US DOJ | 2025-01-29 | [원본](https://www.justice.gov/opa/pr/justice-department-announces-seizure-cybercrime-websites-selling-hacking-tools-transnational) |
| [2] | FBI, Dutch Police Disrupt 'Manipulaters' Phishing Gang | KrebsOnSecurity | 2025-01-30 | [원본](https://krebsonsecurity.com/2025/01/fbi-dutch-police-disrupt-manipulaters-phishing-gang/) |
| [3] | Pakistan Arrests 21 in 'Heartsender' Malware Service | KrebsOnSecurity | 2025-05-28 | [원본](https://krebsonsecurity.com/2025/05/pakistan-arrests-21-in-heartsender-malware-service/) |
| [4] | Department of Justice partners with Dutch police to break up HeartSender network | CyberScoop | 2025-01-30 | [원본](https://cyberscoop.com/doj-saim-raza-heartsender-takedown/) |
| [5] | HeartSender Cybercrime Network Dismantled in Joint US-Dutch Operation | Hackread | 2025-01-30 | [원본](https://hackread.com/heartsender-cybercrime-network-dismantled-us-dutch-op/) |
