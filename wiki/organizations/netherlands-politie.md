---
aliases:

contact_point_for:

cooperation_partners:

country: "[[netherlands]]"
created: 2026-04-08
established: 2007
frameworks_administered:

headquarters: "Driebergen-Rijsenburg, Netherlands"
key_roles:

last_verified: 2026-04-10
mandate: "Investigate complex and high-impact cybercrime cases with national and international"
mechanisms_operated:

member_states: 0
notable_cases:

official_name: "Politie — Dienst Landelijke Recherche — Team High Tech Crime"
official_name_ko: "네덜란드 국가경찰 — 첨단기술범죄수사팀"
operations_participated:
  - "[[alphabay-takedown]]"
  - "[[emotet-takedown]]"
  - "[[operation-bakovia]]"
  - "[[operation-cronos-phase1]]"
  - "[[operation-cronos-phase3]]"
  - "[[operation-dark-huntor]]"
  - "[[operation-endgame]]"
  - "[[operation-endgame-phase1]]"
  - "[[operation-endgame-phase2]]"
  - "[[bidencash-takedown]]"
  - "[[doublevpn-takedown]]"
  - "[[operation-emotet-disruption-ladybird]]"
  - "[[operation-heart-blocker]]"
  - "[[operation-kraken-ghost-platform]]"
  - "[[operation-power-off]]"
  - "[[vpnlab-takedown]]"
  - "[[cryptex-pm2btc-sanctions]]"
  - "[[operation-trojan-shield]]"
org_type: national-unit
parent_org: "[[netherlands-politie-parent]]"
source_count: 0
sources:

status: active
title: "Dutch National Police — National High Tech Crime Unit (NHTCU)"
type: organization
updated: 2026-04-14
---
## Summary

The **National High Tech Crime Unit (NHTCU)** is the specialized cybercrime investigation team within the Dutch National Police (Politie). Part of the **Dienst Landelijke Recherche** (National Detective Service), the NHTCU is *almost certainly* among the top 3 most operationally effective national cybercrime units in Europe, having been instrumental in major international operations including [[operation-endgame-phase1|Operation Endgame]], [[operation-cronos-phase1|Operation Cronos]], [[hive-ransomware-takedown|Hive Ransomware Takedown]], and [[operation-talent|Operation Talent]].

The Netherlands' unique position as **host country for both Europol and [[eurojust]]** in The Hague gives the NHTCU exceptional proximity to EU coordination bodies, facilitating rapid informal coordination before formal legal processes. The 2019 **Wet computercriminaliteit III** granted Dutch police pioneering **remote access powers (hackbevoegdheid)**, making the NHTCU a leader in innovative cybercrime investigation techniques.

## Mandate and Authority

The NHTCU investigates:
- **Complex cybercrime:** Ransomware operations, botnet networks, dark web marketplaces
- **High-impact cases:** Cases with significant national security or economic impact
- **International cases:** Cases requiring cooperation with foreign law enforcement
- **Infrastructure-level targets:** Criminal infrastructure hosting, bulletproof hosting, criminal services

Authority derives from the **Politiewet 2012** (Police Act) and the **Wet computercriminaliteit III** (Computer Crime Act III, 2019) which provides:
- **Hackbevoegdheid:** Legal authority for police to remotely access computer systems
- **Deployment of technical tools:** Installation of monitoring software on suspect systems
- **Data copying:** Remote copying of evidence from suspect systems

## Structure Relevant to Cybercrime IC

The NHTCU operates within the Dienst Landelijke Recherche structure:
- **Investigation teams:** Organized by crime type (ransomware, financial cybercrime, dark web, CSAM)
- **Technical team:** Malware analysis, network forensics, tool development
- **International liaison:** Cooperation coordination with Europol, INTERPOL, bilateral partners
- **FIOD coordination:** Joint operations with [[netherlands-fiod|FIOD]] (Fiscal Intelligence and Investigation Service) for financial cybercrime

## IC Capabilities

- **Europol proximity:** Physical co-location in The Hague enables same-day coordination meetings and rapid informal exchanges
- **Eurojust proximity:** Judicial coordination for JITs and European Investigation Orders (EIOs) facilitated by geographic proximity
- **Hackbevoegdheid:** Remote access capabilities pioneered by Dutch law enable innovative investigation techniques, including deploying "police updates" to compromised systems during takedowns
- **Infrastructure seizure:** Proven capability to seize, analyze, and redirect criminal server infrastructure
- **Cryptocurrency tracing:** Advanced capabilities for blockchain analysis
- **Multilingual:** High English proficiency across the team

## Key Operations and Cases

| Operation | Year | NHTCU Role | Key Contribution |
|-----------|------|-----------|-----------------|
| [[operation-endgame-phase1]] | 2024 | Key participant | Infrastructure seizure; botnet sinkholing |
| [[operation-endgame-phase2]] | 2025 | Key participant | 300 servers, 650 domains |
| [[operation-cronos-phase1]] | 2024 | Key participant | LockBit infrastructure analysis |
| [[operation-cronos-phase3]] | 2024 | Key participant | Additional arrests |
| [[phobos-8base-crackdown]] | 2025 | Key participant | 8Base infrastructure analysis |
| [[hive-ransomware-takedown]] | 2023 | Key participant | Hive infrastructure infiltration; decryption keys recovered |
| [[operation-avalanche]] | 2016 | Key participant | Infrastructure seizure |
| [[operation-talent]] | 2025 | Key participant | Cracked/Nulled forum takedown |
| [[operation-nova]] | 2020 | Key participant | VPN service takedown |

### Innovative Techniques

The NHTCU has pioneered several innovative approaches:
- **[[emotet-takedown|Emotet uninstall module (Operation LadyBird, 2021)]]:** After seizing Emotet C2 infrastructure, Dutch police deployed a law enforcement-created DLL via Emotet's own update mechanism that self-deleted the malware from ~1 million infected machines on 25 April 2021 -- *almost certainly* the first operational use of "police malware" to protect victims at scale
- **[[alphabay-takedown|Hansa covert operation (Operation Bayonet, 2017)]]:** Dutch police covertly operated the Hansa darknet marketplace for ~1 month after seizing it, collecting vendor IP addresses, buyer delivery addresses, and transaction data on 27,000 illegal transactions before revealing the operation
- **Hive infiltration:** Dutch police infiltrated Hive ransomware infrastructure for months before the takedown, collecting decryption keys that were shared with 1,500+ victims [^hive]

[^hive]: > [!note] Based on general knowledge; not verified against a collected source.

## Cooperation Track Record

### Europol Operations

The NHTCU participates in *almost certainly* all major Europol-coordinated cybercrime operations due to:
- Geographic proximity to Europol headquarters
- High operational capability
- Dutch internet infrastructure's central role in European connectivity

### Bilateral Partnerships

- **BKA (Germany):** Closest operational partner; joint operations on Avalanche, Endgame, and many others
- **FBI:** Regular bilateral cooperation on ransomware and financial cybercrime
- **UK NCA:** Cooperation on organized cybercrime
- **French JUNALCO:** Judicial cooperation on cybercrime

### Infrastructure Hosting

The Netherlands is a major internet exchange point (AMS-IX) and hosting center, which means:
- Criminal infrastructure frequently transits or is hosted in the Netherlands
- NHTCU has deep expertise in server seizure and network analysis
- Requests to take down Dutch-hosted criminal infrastructure are frequent

## Capacity Building

The NHTCU contributes to capacity building through:
- Training programs for EU and non-EU partner countries
- INTERPOL training workshops
- Sharing investigative techniques and methodologies

## Korean Interactions (한국과의 협력)

Korea-NHTCU cybercrime cooperation is *likely* indirect, mediated through multilateral channels:

- **Europol-coordinated operations:** Both Korean agencies and NHTCU participated in [[phobos-8base-crackdown]] (2025)
- **Budapest Convention:** Both countries are parties, providing mutual MLA legal basis
- **Europol/Eurojust hosting:** Korean liaison with EU agencies takes place in Dutch territory
- **No known dedicated bilateral cybercrime cooperation** between NHTCU and KNPA Cyber Bureau

## Contradictions & Open Questions

- What is the NHTCU's current staffing level and how has it evolved since 2020?
- How does the hackbevoegdheid power interact with cross-border operations — can it be used on foreign servers?
- What is the NHTCU's capacity for handling simultaneous major operations?
- How does NHTCU coordinate with other Dutch agencies (AIVD, FIOD) on cybercrime cases?

## References

> [!note]
> This page was created based on general knowledge. No dedicated sources have been ingested (source_count: 0). Key claims should be verified against Dutch National Police annual reports and Europol publications.
