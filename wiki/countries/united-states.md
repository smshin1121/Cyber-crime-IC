---
bilateral_agreements:
- '[[korea-us-mlat]]'
central_authority:
  budapest: US Department of Justice, Computer Crime and Intellectual Property Section
    (CCIPS)
  mlat: US Department of Justice, Office of International Affairs (OIA)
cooperation_assessment: The United States is almost certainly the most central actor
  in the international cybercrime cooperation network, owing to the global reach of
  US-headquartered technology companies, the extraterritorial application of US criminal
  law, and the dominant role of the FBI and DOJ in leading or participating in multinational
  cybercrime operations. The US has 30+ bilateral MLATs and is a party to the Budapest
  Convention. However, MLAT response times from the US are widely reported to be slow
  (often 180+ days), which has driven development of alternatives such as the CLOUD
  Act.
created: 2026-04-08
cybercrime_legislation:
  data_retention: No mandatory data retention; voluntary preservation via 18 U.S.C.
    § 2703(f)
  primary_law: Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030
  primary_law_date: '1986-10-16'
  procedural_powers:
  - search-and-seizure
  - production-order
  - preservation-order
  - interception
  - real-time-collection
ic_capacity:
  24_7_availability: true
  avg_mlat_response_days: 180+
  digital_forensics: high
  english_proficiency: high
  rating: high
iso_code: US
key_agencies:
- '[[fbi-cyber-division]]'
- '[[us-doj]]'
- '[[us-secret-service]]'
last_verified: '2026-04-10'
legal_system: common-law
notable_cases: []
operations_participated:
- '[[alphabay-takedown]]'
- '[[emotet-takedown]]'
- '[[operation-cronos-phase1]]'
- '[[operation-cronos-phase3]]'
- '[[operation-endgame-phase1]]'
- '[[operation-endgame-phase2]]'
- '[[phobos-8base-crackdown]]'
- '[[qakbot-gallyamov-indictment]]'
- '[[operation-checkmate-blacksuit]]'
- '[[isoon-apt27-indictment]]'
- '[[operation-haechi-v]]'
- '[[operation-haechi-vi]]'
- '[[hive-ransomware-takedown]]'
- '[[operation-shrouded-horizon]]'
- '[[infraud-organization-takedown]]'
- '[[operation-avalanche]]'
- '[[911-s5-botnet-takedown]]'
- '[[goznym-takedown]]'
- '[[fin7-takedown]]'
- '[[proxy-service-takedown-2026-03]]'
- '[[operation-eur-300m-global-credit-card-fraud-2025]]'
- '[[darkmarket-takedown]]'
- '[[operation-us-v-parsarad-nemesis]]'
- '[[doublevpn-takedown]]'
- '[[operation-dark-huntor]]'
- '[[cryptex-pm2btc-sanctions]]'
- '[[lumma-stealer-takedown]]'
- '[[operation-chinese-national-sentenced-prison-role-crypto-scam-targeting-americans]]'
- '[[operation-iranian-man-pleaded-guilty-to-role-in-robbinhood-ransomware]]'
- '[[operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-and-money-laundering-services]]'
- '[[operation-justice-department-secures-forfeiture-of-over-5m-of-funds-traceable-to-business-email-compromise-scheme-target]]'
- '[[operation-law-enforcement-seize-record-amounts-of-illegal-drugs-firearms-and-drug-trafficking-proceeds-in-international-]]'
- '[[operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto]]'
- '[[nemesis-market-takedown]]'
region: north-america
source_count: 1
sources:
- '[[2026-03-12-eurojust-proxy-service-takedown]]'
title: United States of America
treaty_memberships:
- date: '2006-09-29'
  framework: '[[budapest-convention]]'
  reservations: []
  status: party
- date: '2022'
  framework: '[[second-additional-protocol]]'
  reservations: []
  status: signatory
type: country
updated: 2026-04-21
---

## Summary

The United States holds the **highest centrality** in the international cybercrime cooperation network. As home to the world's largest technology companies (Google, Meta, Microsoft, Apple, etc.), the US is *almost certainly* the most frequently requested country for cross-border digital evidence. The [[fbi-cyber-division|FBI Cyber Division]] and [[us-doj|Department of Justice]] lead or participate in the majority of major international cybercrime operations, and US federal prosecutors have brought more international cybercrime cases than any other jurisdiction.

The US legal framework combines the **Computer Fraud and Abuse Act (CFAA)** as the primary cybercrime statute, the **CLOUD Act** (2018) as a mechanism for streamlining cross-border data access, and an extensive network of 30+ bilateral **Mutual Legal Assistance Treaties (MLATs)**.

## Legal Framework for Cybercrime

### Substantive Criminal Law

**Computer Fraud and Abuse Act (CFAA), 18 U.S.C. § 1030 (1986, amended):**
- Unauthorized access to protected computers (§ 1030(a)(2))
- Damage to protected computers (§ 1030(a)(5))
- Trafficking in passwords (§ 1030(a)(6))
- Extortion involving computers (§ 1030(a)(7)) — covers ransomware

**Wire Fraud, 18 U.S.C. § 1343:**
- Broadly applied to cyber-enabled financial fraud (BEC, phishing, etc.)

**Identity Theft, 18 U.S.C. § 1028/1028A:**
- Aggravated identity theft adds mandatory 2-year consecutive sentence

**Economic Espionage Act, 18 U.S.C. § 1831-1839:**
- State-sponsored cyber espionage prosecutions

**CLOUD Act (Clarifying Lawful Overseas Use of Data Act), 2018:**
- Allows US law enforcement to compel US-based providers to produce data stored abroad
- Enables bilateral executive agreements for reciprocal direct access
- *Highly likely* the most significant legislative development for cross-border evidence access since the Budapest Convention

### Procedural Powers

- **Search and seizure:** Fourth Amendment protections; warrants required for content data (Carpenter v. United States, 2018)
- **Stored Communications Act (SCA), 18 U.S.C. § 2701-2712:** Framework for compelling subscriber data, traffic data, and content from providers
- **Pen register / trap-and-trace (18 U.S.C. § 3121-3127):** Real-time collection of metadata
- **Wiretap Act (Title III), 18 U.S.C. § 2510-2522:** Real-time content interception; requires court order
- **Preservation orders (18 U.S.C. § 2703(f)):** 90-day preservation requests to providers; commonly used in IC context

### Mutual Legal Assistance

- **Central authority:** [[us-doj|Department of Justice]], Office of International Affairs (OIA)
- **30+ bilateral MLATs** in force
- **Budapest Convention** Chapter IV provides additional multilateral MLA basis
- **CLOUD Act executive agreements:** Bilateral agreements enabling direct law enforcement-to-provider requests (first agreement: US-UK, 2019)
- **Average processing time:** *Likely* 180+ days for standard MLAT requests; significantly faster for urgent requests and CLOUD Act pathways

> [!warning] Legal status check needed
> Verify the current number of CLOUD Act executive agreements in force and the complete list of US bilateral MLATs relevant to cybercrime.

## Treaty Memberships

| Framework | Status | Date | Notes |
|-----------|--------|------|-------|
| [[budapest-convention]] | Party | 2006 | Among the first ratifiers |
| [[second-additional-protocol]] | Signatory | 2022 | Pending ratification |
| UNTOC (Palermo Convention) | Party | 2005 | |
| UNCAC | Party | 2006 | |
| US-Korea MLAT | In force | 2000 | |
| US-UK MLAT | In force | 1996 | |
| US-Germany MLAT | In force | 2010 | |
| US-Netherlands MLAT | In force | 1983 | |
| US-Australia MLAT | In force | 1999 | |
| US-Japan MLAT | In force | 2006 | |

The US participates in the **G7 24/7 Cyber Network** and the Budapest Convention **24/7 Network** ([[24-7-network]]).

## Key Agencies

### Federal Bureau of Investigation (FBI) — Cyber Division
See [[fbi-cyber-division]] for full profile.
- Lead federal agency for investigating cyber attacks and intrusions
- Cyber Action Teams (CATs) deploy internationally
- Legal Attache (Legat) offices in 60+ countries
- Operates Internet Crime Complaint Center (IC3)

### Department of Justice (DOJ)
See [[us-doj]] for full profile.
- **Office of International Affairs (OIA):** Central authority for all incoming/outgoing MLATs
- **Computer Crime and Intellectual Property Section (CCIPS):** Specialized cybercrime prosecutors; Budapest Convention 24/7 contact
- **National Security Division (NSD):** State-sponsored cyber cases
- US Attorney's Offices (particularly WDPA, EDNY, NDCA) handle major cybercrime prosecutions

### US Secret Service
- Electronic Crimes Task Forces (ECTFs) in 40+ US cities
- Focuses on financial cybercrime, identity theft, network intrusions affecting financial infrastructure
- International partnerships through field offices abroad

## Cooperation Track Record

### As Requesting State

The US is the world's largest **requester** of cross-border digital evidence, driven by:
- US-based platforms holding data relevant to foreign crimes
- Extraterritorial application of US criminal law to foreign-based cybercriminals
- International investigations led by FBI Cyber Division

### As Requested State

The US is *almost certainly* the most frequently **requested** country for MLA in cybercrime cases, because most major technology companies are headquartered in the US. Processing times are a widely acknowledged bottleneck:
- Standard MLAT requests: *Likely* 180+ days
- Emergency requests: Significantly faster
- CLOUD Act pathways: Intended to reduce delays to days/weeks

### Notable Partnerships

- **Five Eyes (FVEY):** Intelligence-sharing alliance (US, UK, Canada, Australia, New Zealand) — extends to cybercrime through informal cooperation
- **US-EU:** Europol cooperation on ransomware takedowns, financial cybercrime
- **US-Korea:** Active bilateral cooperation on North Korea-related cyber operations, ransomware, voice phishing

## Korean Interactions (한국과의 협력)

Korea-US cybercrime cooperation is *highly likely* the strongest bilateral cyber IC relationship Korea maintains:

- **Korea-US MLAT (2000):** Primary formal channel; used for evidence requests involving US-based tech platforms
- **[[phobos-8base-crackdown]]:** Phobos ransomware administrator arrested in South Korea (June 2024) and extradited to the US (November 2024) — demonstrating the full cooperation cycle from arrest to extradition
- **[[isoon-apt27-indictment]]:** US DOJ indicted Chinese hackers who targeted South Korea's foreign ministry, among other victims
- **[[operation-haechi-v]] / [[operation-haechi-vi]]:** US participated in Korea-led INTERPOL HAECHI operations against cyber-enabled financial crime
- **North Korea cyber threat:** Joint focus area; US and Korean agencies cooperate on cryptocurrency theft and ransomware attributed to DPRK-affiliated actors

> [!note]
> This page is based on general knowledge of US cybercrime cooperation structures and publicly available information. No collected sources have been ingested for this country profile. Content should be verified against primary sources.

## Contradictions & Open Questions

- What is the current average MLAT processing time for cybercrime-related requests to the US?
- How many CLOUD Act executive agreements are currently in force?
- What is the status of US ratification of the Second Additional Protocol to the Budapest Convention?
- How does the US prioritize incoming MLAT requests (by crime type, requesting country, urgency)?

## References

> [!note]
> This page was created based on general knowledge. No dedicated sources have been ingested (source_count: 0). Key claims should be verified against official DOJ, FBI, and Council of Europe publications.
