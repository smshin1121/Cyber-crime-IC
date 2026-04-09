---
aliases:
- US Treasury
- Treasury OFAC
- Treasury FinCEN
- OFAC
- FinCEN
contact_point_for: []
cooperation_partners:
- '[[fbi-cyber-division]]'
- '[[us-doj]]'
- '[[europol-ec3]]'
country: '[[united-states]]'
created: 2026-04-10
established: '1789'
frameworks_administered: []
headquarters: Washington, D.C., United States
key_roles:
- OFAC cyber sanctions designations under Executive Order 13694 (as amended by EO
  13757)
- Treasury designations against ransomware groups, mixers, and crypto exchanges
- FinCEN Bank Secrecy Act enforcement against virtual currency money services businesses
- FinCEN ransomware advisories and guidance
- Cooperation with foreign financial intelligence units (via FinCEN)
- Multilateral sanctions coordination with allies
mandate: Apply US economic sanctions and financial regulatory tools against cybercriminals,
  state-sponsored cyber actors, and illicit virtual currency ecosystems. OFAC designates
  cyber-related sanctions targets (ransomware operators, mixers, exchanges). FinCEN
  enforces Bank Secrecy Act requirements against money transmitters and virtual currency
  businesses used by cybercriminals.
mechanisms_operated: []
notable_cases: []
official_name: United States Department of the Treasury — Office of Foreign Assets
  Control and Financial Crimes Enforcement Network
operations_participated:
- '[[911-s5-botnet-takedown]]'
- '[[cryptex-pm2btc-sanctions]]'
- '[[operation-wirewire]]'
org_type: national-agency
parent_org: '[[us-federal-government]]'
source_count: 4
sources: []
title: US Department of the Treasury — OFAC and FinCEN (Cyber)
type: organization
updated: '2026-04-09'
---

## Summary

The US Department of the Treasury plays a central role in international cybercrime cooperation through two distinct tools:

1. **Office of Foreign Assets Control (OFAC)** — imposes economic sanctions against cybercriminals, state-sponsored cyber actors, and illicit virtual currency services under Executive Order 13694 (issued April 2015, amended by EO 13757 in December 2016).
2. **Financial Crimes Enforcement Network (FinCEN)** — enforces Bank Secrecy Act requirements against money services businesses (including virtual currency exchanges and mixers) and issues guidance on cybercrime-related financial flows.

Together, Treasury actions have become a **force multiplier** for law enforcement, complementing arrests and indictments with economic exclusion of cybercriminal infrastructure. Notable actions include the **Tornado Cash** and **Blender.io** mixer designations (2022) and repeated sanctions against DPRK's Lazarus Group and affiliated actors.

## Mandate and Authority

### OFAC cyber authority

- **Executive Order 13694 (April 2015)** — authorized sanctions against "significant malicious cyber-enabled activities"
- **Executive Order 13757 (December 2016)** — expanded EO 13694 to reach election-interference cyber actors
- **International Emergency Economic Powers Act (IEEPA)** — underlying statutory authority
- **CAATSA (2017)** — additional Russia-specific cyber sanctions authority

### FinCEN authority

- **Bank Secrecy Act (31 U.S.C. § 5311 et seq.)**
- **USA PATRIOT Act**
- **Anti-Money Laundering Act of 2020**
- **FinCEN 2019 guidance** on virtual currency business models

## Structure Relevant to Cybercrime IC

- **OFAC (Office of Foreign Assets Control):** Sanctions designations, licensing, enforcement. Within Treasury's Office of Terrorism and Financial Intelligence (TFI).
- **FinCEN (Financial Crimes Enforcement Network):** BSA enforcement, Suspicious Activity Report (SAR) analysis, financial intelligence. Within TFI.
- **Office of Foreign Assets Control Compliance and Enforcement Divisions.**
- **Treasury Office of Cybersecurity and Critical Infrastructure Protection (OCCIP).**

## IC Capabilities

- **Multilateral sanctions coordination:** US Treasury routinely coordinates cyber sanctions with the EU, UK, Canada, Australia, and Japan to maximize impact. Examples include joint designations following major ransomware incidents.
- **FinCEN Egmont Group participation:** FinCEN is the US member of the Egmont Group of Financial Intelligence Units, enabling secure information sharing with 160+ foreign FIUs.
- **Sanctions-based deterrence:** OFAC designations impose global consequences on designated actors by cutting off access to US financial systems and compelling foreign compliance.
- **SDN List publication:** The Specially Designated Nationals list is used by global financial institutions as a de facto compliance baseline.

## Key Operations and Cases

### Virtual Currency Mixer Designations

- **Blender.io (6 May 2022):** First OFAC designation of a virtual currency mixer. Used by DPRK's Lazarus Group to launder proceeds from the Axie Infinity Ronin Bridge hack.
- **Tornado Cash (8 August 2022):** Second and more controversial mixer designation. OFAC cited laundering of over USD 7 billion since 2019, including USD 455+ million stolen by the Lazarus Group, USD 96M from the Harmony Bridge Heist (June 2022), and USD 7.8M from the Nomad Heist (August 2022).
- **Roman Semenov (Tornado Cash co-founder) designation (August 2023).**

> [!warning] Legal status check needed
> On **21 March 2025**, OFAC officially lifted sanctions on Tornado Cash and removed its associated addresses following the Fifth Circuit's November 2024 decision in *Van Loon v. Department of the Treasury*, which held that immutable smart contracts could not be "property" subject to OFAC designation. Tornado Cash founders (Semenov, Storm, and others) remain under separate criminal indictment and related designations. Status should be reverified.

### FinCEN enforcement

- **Larry Harmon / Helix mixer ($60 million civil penalty, 2020)** — first FinCEN action against a virtual currency mixer for BSA violations.
- **Ransomware advisory (October 2020; updated November 2021)** — advised financial institutions on ransomware-related SAR filing.

### Ransomware and state-sponsored designations

- Multiple designations of Russian ransomware actors (Evil Corp, Conti associates, LockBit affiliates)
- DPRK Lazarus Group and affiliated APT actors
- Iranian cyber actors (IRGC-affiliated)

## Cooperation Track Record

Treasury's cooperation impact on cybercrime is *highly likely* substantial but qualitatively different from traditional law enforcement: it works through **financial exclusion** rather than arrest. OFAC designations create secondary compliance pressure on foreign financial institutions, which is *highly likely* more effective than MLAT-based fund recovery for freezing cryptocurrency and conventional funds.

## Contradictions & Open Questions

- The *Van Loon* decision and the 2025 lifting of Tornado Cash sanctions raise questions about the legal durability of OFAC designations against **code** and **immutable smart contracts** (as opposed to individuals and identifiable entities).
- How does OFAC balance deterrence value against the practical impact of designations that cybercriminal actors can partially evade through alternative rails?
- FinCEN's ability to enforce BSA against non-US virtual currency businesses remains contested.
- Tension between US unilateral sanctions and multilateral instruments (particularly EU sanctions processes) sometimes complicates joint cyber enforcement.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| [1] | US Treasury Sanctions Notorious Virtual Currency Mixer Tornado Cash | US Treasury | 2022-08-08 | https://home.treasury.gov/news/press-releases/jy0916 |
| [2] | Treasury Designates Roman Semenov, Co-Founder of Sanctioned Virtual Currency Mixer Tornado Cash | US Treasury | 2023-08 | https://home.treasury.gov/news/press-releases/jy1702 |
| [3] | A Legal Whirlwind Settles: Treasury Lifts Sanctions on Tornado Cash | Venable LLP | 2025-04 | https://www.venable.com/insights/publications/2025/04/a-legal-whirlwind-settles-treasury-lifts-sanctions |
| [4] | OFAC Sanctions Virtual Currency Mixer Tornado Cash and Faces Crypto Backlash | Money Laundering Watch | 2022-08 | https://www.moneylaunderingnews.com/2022/08/ofac-sanctions-virtual-currency-mixer-tornado-cash-and-faces-crypto-backlash/ |