---
type: organization
title: "US Department of Justice (DOJ)"
official_name: "United States Department of Justice"
official_name_ko: "미국 법무부"
aliases: ["DOJ", "US DOJ", "Justice Department", "USDOJ"]
org_type: "national-agency"
parent_org: ""
country: "[[united-states]]"
headquarters: "Washington, D.C., United States"
established: "1870-07-01"
mandate: "Enforce federal law, administer justice, and ensure public safety; central authority for US MLATs; lead federal cybercrime prosecution through CCIPS and US Attorney's Offices."
member_states: 0
key_roles:
  - "Central authority for all US bilateral MLATs"
  - "Federal cybercrime prosecution (CCIPS)"
  - "International extradition processing (OIA)"
  - "Budapest Convention 24/7 contact point (CCIPS)"
  - "Policy coordination for international cybercrime cooperation"
  - "Asset forfeiture and recovery in cybercrime cases"
cooperation_partners:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[uk-nca]]"
  - "[[germany-bka]]"
frameworks_administered: []
mechanisms_operated:
  - "[[mlat-process]]"
operations_participated:
  - "[[operation-cronos-phase1]]"
  - "[[operation-cronos-phase3]]"
  - "[[phobos-8base-crackdown]]"
  - "[[qakbot-gallyamov-indictment]]"
  - "[[operation-endgame-phase1]]"
  - "[[operation-endgame-phase2]]"
  - "[[operation-checkmate-blacksuit]]"
  - "[[isoon-apt27-indictment]]"
  - "[[hive-ransomware-takedown]]"
  - "[[infraud-organization-takedown]]"
  - "[[911-s5-botnet-takedown]]"
  - "[[operation-shrouded-horizon]]"
  - "[[goznym-takedown]]"
  - "[[fin7-takedown]]"
notable_cases: []
contact_point_for:
  - network: "[[24-7-network]]"
    role: "Budapest Convention Art. 35 contact point (USA) — via CCIPS"
  - network: "[[mlat-process]]"
    role: "Central authority for all US MLATs — via OIA"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

The **US Department of Justice (DOJ)** is the central legal authority for international cybercrime cooperation involving the United States. Through its **Office of International Affairs (OIA)**, DOJ serves as the **central authority** for all US bilateral Mutual Legal Assistance Treaties (30+ MLATs). Through the **Computer Crime and Intellectual Property Section (CCIPS)** in the Criminal Division, DOJ leads federal cybercrime prosecution and serves as the **Budapest Convention Art. 35 contact point**.

DOJ prosecutors have brought more international cybercrime cases than *almost certainly* any other prosecution authority globally, including landmark operations such as [[operation-cronos-phase1|Operation Cronos]] (LockBit), [[qakbot-gallyamov-indictment|QakBot]], [[isoon-apt27-indictment|i-Soon/APT27]], and [[infraud-organization-takedown|Infraud Organization]].

## Mandate and Authority

### Office of International Affairs (OIA)
- **Central authority** for all incoming and outgoing MLAT requests
- Processes formal MLA requests from foreign countries seeking US-located evidence
- Coordinates extradition requests to and from the United States
- Handles letters rogatory from countries without MLAT
- OIA is the *almost certainly* the busiest MLAT central authority globally, given the volume of requests involving US-based technology companies

### Computer Crime and Intellectual Property Section (CCIPS)
- Specialized cybercrime prosecutors within the Criminal Division
- Provides guidance and coordination for cybercrime cases across US Attorney's Offices
- Budapest Convention 24/7 contact point
- Develops cybercrime policy and international cooperation strategy
- Coordinates with FBI Cyber Division on investigation strategy

### National Security Division (NSD)
- Handles state-sponsored cyber espionage and cyber attacks
- Prosecuted [[isoon-apt27-indictment|i-Soon/APT27]] case

### US Attorney's Offices
Key districts for cybercrime prosecution:
- **Western District of Pennsylvania (WDPA):** QakBot, Hive, GozNym
- **Eastern District of New York (EDNY):** LockBit (Cronos)
- **Northern District of California (NDCA):** Silicon Valley-connected cases
- **District of New Jersey:** Various cybercrime operations

## Structure Relevant to Cybercrime IC

```
DOJ (Attorney General)
├── Criminal Division
│   ├── CCIPS (Computer Crime and Intellectual Property Section)
│   │   ├── Budapest Convention 24/7 contact
│   │   ├── Cybercrime prosecution coordination
│   │   └── International cooperation policy
│   └── OIA (Office of International Affairs)
│       ├── MLAT central authority
│       ├── Extradition processing
│       └── Letters rogatory
├── National Security Division
│   └── State-sponsored cyber cases (i-Soon/APT27)
├── US Attorney's Offices (94 districts)
│   ├── WDPA (Pittsburgh) — QakBot, Hive
│   ├── EDNY (Brooklyn) — LockBit
│   └── NDCA (San Francisco) — Tech-related cases
└── FBI (investigative arm)
    └── Cyber Division
```

## IC Capabilities

- **MLAT processing:** Central authority for 30+ bilateral MLATs; handles thousands of requests annually
- **CLOUD Act implementation:** Administers bilateral executive agreements for streamlined data access
- **Sealed indictment strategy:** DOJ frequently uses sealed indictments against foreign cybercriminals, unsealing upon arrest or as deterrence
- **Asset forfeiture:** Extensive powers for seizing cryptocurrency and other digital assets in cybercrime cases
- **Grand jury subpoena power:** Can compel US-based providers to produce evidence
- **International training:** CCIPS and OIA conduct training for foreign prosecutors and judges

## Key Operations and Cases

### Ransomware Operations

| Operation | Year | DOJ Role | Key Prosecution Action |
|-----------|------|----------|----------------------|
| [[operation-cronos-phase1]] | 2024 | EDNY prosecution | Indictment of LockBit leadership |
| [[operation-cronos-phase3]] | 2024 | EDNY prosecution | Additional indictments |
| [[phobos-8base-crackdown]] | 2025 | Prosecution | Phobos admin extradited from Korea |
| [[qakbot-gallyamov-indictment]] | 2025 | WDPA prosecution | Gallyamov indicted; $24M+ crypto seized |
| [[operation-checkmate-blacksuit]] | 2025 | Prosecution | BlackSuit/Royal ransomware disruption |
| [[hive-ransomware-takedown]] | 2023 | Prosecution | Hive infrastructure seized after infiltration |

### State-Sponsored Operations

| Operation | Year | DOJ Role | Target |
|-----------|------|----------|--------|
| [[isoon-apt27-indictment]] | 2025 | NSD prosecution | 12 Chinese contract hackers indicted |

### Financial Cybercrime

| Operation | Year | DOJ Role | Key Result |
|-----------|------|----------|------------|
| [[infraud-organization-takedown]] | 2018 | Lead prosecution | $530M fraud ring; 36 indicted across 17 countries |
| [[911-s5-botnet-takedown]] | 2024 | Prosecution | Residential proxy botnet operator arrested |
| [[goznym-takedown]] | 2019 | WDPA prosecution | Banking malware; multinational takedown |
| [[fin7-takedown]] | 2018 | Prosecution | FIN7 leadership arrested |

## Cooperation Track Record

### As Central Authority

DOJ OIA processes MLA requests from virtually every country with which the US has an MLAT or bilateral cooperation channel. Key challenges:
- **Volume bottleneck:** *Likely* the highest volume of incoming MLA requests globally
- **Processing delays:** Standard MLAT requests may take 180+ days
- **CLOUD Act alternative:** Bilateral executive agreements intended to reduce delays to days/weeks
- **Prioritization:** Urgent requests (imminent threat to life, time-sensitive evidence) receive expedited processing

### Prosecution Leadership

DOJ has *almost certainly* prosecuted more international cybercrime cases than any other single prosecution authority, establishing key legal precedents for:
- Extraterritorial jurisdiction over foreign cybercriminals
- Cryptocurrency seizure and forfeiture
- Conspiracy charges for cybercrime-as-a-service operators
- Sealed indictment strategy for deterrence

### Eurojust Cooperation

DOJ maintains a US liaison prosecutor at [[eurojust]] in The Hague, facilitating coordination on cases involving both US and EU interests.

## Capacity Building

DOJ conducts extensive international training through:
- **OPDAT (Office of Overseas Prosecutorial Development, Assistance and Training):** Trains foreign prosecutors
- **CCIPS international programs:** Cybercrime-specific capacity building
- **ILEA (International Law Enforcement Academies):** Training centers in multiple countries

## Korean Interactions (한국과의 협력)

DOJ is *highly likely* the most important US counterpart for Korean cybercrime cooperation:

- **Korea-US MLAT (2000):** DOJ OIA processes all Korean MLA requests to the US and vice versa
- **[[phobos-8base-crackdown]]:** DOJ prosecuted the Phobos administrator who was arrested in South Korea and extradited to the US; demonstrates complete arrest-to-prosecution cooperation cycle
- **[[isoon-apt27-indictment]]:** DOJ indicted Chinese hackers who targeted South Korea's Ministry of Foreign Affairs; Korea was a victim in a DOJ-led case
- **Evidence requests:** Korean prosecutors *likely* send significant volume of MLA requests to DOJ OIA for evidence held by US-based technology companies (Google, Meta, Microsoft, Apple)
- **CCIPS contact:** Korean 24/7 Network requests are received by DOJ CCIPS

## Contradictions & Open Questions

- What is DOJ's current MLAT backlog for cybercrime-related requests?
- How many CLOUD Act executive agreements are currently in force or under negotiation?
- What is the volume of Korea-US MLA requests processed annually?
- How does DOJ prioritize incoming MLA requests (by crime severity, country, urgency)?
- What is the CCIPS staffing level and how has it evolved?

## References

> [!note]
> This page was created based on general knowledge. No dedicated sources have been ingested (source_count: 0). Key claims should be verified against DOJ annual reports, CCIPS publications, and OIA statistics.
