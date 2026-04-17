---
operation_role: umbrella
parent_operation: ""
---
﻿---
type: operation
title: "Lumma Stealer Takedown"
aliases: ["LummaC2 Disruption", "Lumma Stealer Disruption"]
operation_type: "takedown"
status: "completed"
enforcement_type:
  - seizure
  - takedown
outcome: "success"
timeframe:
  announced: "2025-05-21"
  start: "2025-05-13"
  end: "2025-05-21"
  ongoing: false
crime_type: "[[hacking-ic|Hacking / Malware Distribution]]"
target_entity: "Lumma Stealer (LummaC2) — Malware-as-a-Service infostealer platform"
lead_agency: "[[us-doj|U.S. Department of Justice]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[united-states|United States]]"
  - "[[japan|Japan]]"
participating_agencies:
  - "[[us-doj|U.S. Department of Justice]]"
  - "[[fbi-cyber-division|FBI Cyber Division]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[japan-npa|Japan Cybercrime Control Center (JC3)]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention]]"
mechanisms_used:
  - "[[public-private-cooperation|Public-Private Cooperation]]"
  - "[[informal-cooperation|Informal Law Enforcement Cooperation]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 2300
  cryptocurrency_seized: ""
  other:
    - "1,300+ domains redirected to Microsoft sinkholes"
    - "300 domains actioned by law enforcement with Europol support"
    - "5 core domains seized by DOJ warrant"
    - "394,000+ infected Windows computers identified (Mar-May 2025)"
    - "1.7 million instances of credential theft identified by FBI"
source_count: 1
sources:
  - "[TechXplore — Global malware federal court Georgia](https://techxplore.com/news/2025-05-global-malware-federal-court-georgia.html)"
created: 2025-05-21
updated: 2026-04-10
---

## Summary

The Lumma Stealer Takedown was a major public-private operation announced on May 21, 2025, that disrupted the infrastructure of **Lumma Stealer (LummaC2)**, one of the world's most widely used information-stealing malware platforms. Microsoft's Digital Crimes Unit (DCU) led the civil legal action, obtaining a court order from the U.S. District Court for the Northern District of Georgia, while the [[us-doj|U.S. Department of Justice]] unsealed warrants to seize five core domains. [[europol-ec3|Europol's EC3]] coordinated European law enforcement, and Japan's Cybercrime Control Center (JC3) facilitated the suspension of locally based infrastructure.

The operation resulted in the seizure or sinkholing of approximately **2,300 malicious domains** that formed Lumma's command-and-control (C2) network, severing communications between the malware and an estimated **394,000+ infected Windows computers** worldwide.

This operation is *highly likely* one of the largest public-private takedowns of an infostealer infrastructure to date, notable for its reliance on civil court orders (Microsoft) in parallel with criminal warrants (DOJ).

## Background

Lumma Stealer, also known as **LummaC2**, was a Malware-as-a-Service (MaaS) platform that enabled cybercriminals to purchase and deploy information-stealing malware. The malware harvested sensitive data from infected systems including:

- User login credentials (passwords, session tokens)
- Financial information (credit card numbers, bank account details)
- Cryptocurrency wallet data
- Personal identification information

The developer, known by the internet alias **"Shamel"** and *likely* based in Russia, marketed Lumma via Telegram and Russian-language forums. The service operated on a tiered pricing model: $250, $500, $1,000 for various feature levels, and $20,000 for full source code access. In a November 2023 interview, "Shamel" claimed approximately **400 active clients**.

Lumma had been deployed to enable a broad range of criminal activity including ransomware attacks on schools, fraudulent bank transfers, and cryptocurrency theft. The FBI identified at least **1.7 million instances** in which the malware was used to steal sensitive information.

## Participating Parties

### Law Enforcement

| Agency | Country | Role |
|--------|---------|------|
| [[us-doj|U.S. Department of Justice]] | [[united-states|United States]] | Unsealed warrants; seized 5 core domains and central command structure |
| [[fbi-cyber-division|FBI Cyber Division]] | [[united-states|United States]] | Investigation; identified 1.7 million theft instances |
| [[europol-ec3|Europol EC3]] | EU | Coordinated European law enforcement; facilitated 300 domain seizures |
| Japan Cybercrime Control Center (JC3) | [[japan|Japan]] | Suspended locally based Lumma infrastructure |

### Private Sector Partners

| Organization | Role |
|-------------|------|
| **Microsoft Digital Crimes Unit (DCU)** | Led civil legal action; filed lawsuit; sinkholed 1,300+ domains |
| ESET | Cybersecurity intelligence and technical support |
| Cloudflare | Infrastructure disruption support |
| Lumen Technologies | Network-level disruption |
| Bitsight | Threat intelligence |
| CleanDNS | Domain takedown support |
| GMO Registry | Domain registry cooperation |

## Legal Framework

The operation employed a **dual-track legal approach** — civil and criminal actions in parallel:

1. **Civil Action (Microsoft)**: Microsoft's DCU filed a lawsuit on **May 13, 2025** in the **U.S. District Court for the Northern District of Georgia**. The court granted a temporary restraining order against 10 unidentified defendants (including "Shamel" and others supporting Lumma's infrastructure), authorizing the seizure and redirection of approximately 2,300 malicious domains.

2. **Criminal Action (DOJ)**: On **May 19, 2025**, the DOJ unsealed **two warrants** authorizing the seizure of **five Internet domains** used to operate the Lumma malware service. These domains served as the administration panel and marketplace where the malware was sold.

3. **Europol Legal Basis**: Europol operated under **Article 26 of Europol's Regulation**, which enables Europol to receive information from and collaborate with private parties to prevent and combat serious crime.

> [!note] Legal basis detail
> The specific Budapest Convention articles invoked for cross-border cooperation in this operation are not detailed in available sources. The cooperation appears to have relied primarily on informal law enforcement channels and public-private partnership mechanisms rather than formal MLAT processes.

## Operational Timeline

| Date | Event |
|------|-------|
| 2022 (est.) | Lumma Stealer begins operations as a MaaS platform |
| 2023-11 | Developer "Shamel" claims ~400 active clients in interview |
| 2025-03-16 | Start of Microsoft's monitoring period identifying 394,000+ infections |
| 2025-05-13 | Microsoft DCU files civil lawsuit in Northern District of Georgia |
| 2025-05-16 | End of Microsoft's monitoring period |
| 2025-05-19 | DOJ unseals two warrants authorizing seizure of five core domains |
| 2025-05-21 | Coordinated public announcement; infrastructure disrupted globally |

## Results and Impact

### Quantitative Results

- **~2,300 domains** seized or disrupted (Lumma's C2 backbone)
- **1,300+ domains** redirected to Microsoft sinkholes
- **300 domains** actioned by law enforcement with Europol support
- **5 core domains** seized by DOJ warrant (administration and distribution)
- **394,000+ infected Windows computers** identified (March 16 — May 16, 2025)
- **1.7 million theft instances** identified by FBI investigators
- **0 arrests** announced at time of takedown

### Impact Assessment

The operation severed the communication link between Lumma's C2 servers and infected endpoints. The sinkholed domains allowed Microsoft to collect telemetry data from callbacks, providing ongoing threat intelligence. The seizure of administration domains disrupted the marketplace where the malware was sold to affiliates.

> [!warning] Operational resilience concern
> Post-takedown reporting (as of late May 2025) indicated that Lumma Stealer operators *likely* attempted to rebuild infrastructure, a pattern commonly observed in MaaS takedowns. The long-term effectiveness of this disruption will depend on sustained enforcement pressure.

## Cooperation Mechanisms Used

1. **[[public-private-cooperation|Public-Private Cooperation]]**: The defining feature of this operation. Microsoft led the civil legal track while coordinating with DOJ, Europol, and JC3. Private sector partners (ESET, Cloudflare, Lumen, Bitsight, CleanDNS, GMO Registry) provided technical capabilities for infrastructure disruption.

2. **Civil-Criminal Parallel Approach**: Microsoft used civil court orders for domain seizure (broader scope, ~2,300 domains) while DOJ used criminal warrants for the five most critical domains. This dual approach is a model pioneered by Microsoft in earlier operations (e.g., Trickbot, Necurs).

3. **[[informal-cooperation|Informal Law Enforcement Cooperation]]**: Cross-border coordination between U.S., European, and Japanese authorities appears to have been conducted through informal channels and established relationships rather than formal MLAT processes.

4. **Domain Registry Cooperation**: Domain registrars and DNS providers cooperated to transfer, suspend, or redirect malicious domains to sinkholes.

## Challenges and Friction Points

1. **No Arrests**: Despite the scale of the operation, no arrests were announced. The developer "Shamel" is *likely* based in Russia, a jurisdiction that does not extradite its nationals and has limited cooperation with Western law enforcement on cybercrime matters.

2. **MaaS Resilience**: Malware-as-a-Service platforms are designed for rapid infrastructure reconstitution. Domain seizures disrupt but may not permanently disable the operation.

3. **Attribution Challenges**: While "Shamel" was identified by alias, achieving positive identification and arrest remains challenging given the developer's *likely* location in Russia.

4. **Scale of Infections**: With 394,000+ infected systems identified in a two-month window, the remediation burden falls on individual users and organizations worldwide.

## Lessons Learned

1. **Civil-criminal dual track is effective for infrastructure takedowns**: Microsoft's civil court orders provided broader domain seizure authority than criminal warrants alone, while DOJ's criminal warrants targeted the most critical nodes.

2. **Private sector as force multiplier**: Microsoft's DCU brought technical capabilities, legal resources, and domain expertise that complemented law enforcement's authority. The involvement of seven private sector partners demonstrates the value of broad coalitions.

3. **Europol Article 26 enables public-private collaboration**: Europol's regulatory framework for engaging with private parties proved effective for coordinating European aspects of the operation.

4. **Sinkholing provides ongoing intelligence**: Redirecting domains to sinkholes rather than simply taking them offline allowed continued monitoring of infected systems and provided data for remediation efforts.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.


- Ongoing monitoring of sinkholed domains for callback traffic
- Data from seized infrastructure expected to support further investigations
- Remediation efforts for 394,000+ identified infected systems
- Continued investigation into "Shamel" and Lumma's operator network
- Monitoring for infrastructure reconstitution attempts

## Korean Involvement (한국의 참여)

No known South Korean involvement in this operation has been reported. South Korea was not listed among the participating countries or agencies. However, given the global nature of infostealer infections (394,000+ systems worldwide), it is *possible* that Korean systems were among those affected. [[south-korea|South Korea's]] cybersecurity agencies (including [[kisa|KISA]]) would be relevant for any domestic remediation efforts related to Lumma infections on Korean networks.

## Contradictions & Open Questions

1. **Exact takedown date**: Sources variously report May 13 (Microsoft lawsuit filing), May 19 (DOJ warrants unsealed), and May 21 (public announcement) as the operation date. The operation was *almost certainly* a multi-day coordinated action rather than a single-day event.

2. **Number of domains**: Most sources cite "approximately 2,300" domains, though the breakdown between Microsoft-sinkholed (~1,300), law enforcement-actioned (~300), and remaining domains (~700 showing seizure notices) requires clarification.

3. **No arrest timeline**: Whether arrests are expected or whether this was purely an infrastructure disruption operation is not clear from available sources.

4. **Developer location**: "Shamel" is described as "based in Russia" but this has not been independently confirmed by law enforcement in public statements.

5. **Infection count methodology**: The 394,000 figure covers a specific two-month window (March 16 — May 16, 2025) and *likely* understates the total number of systems ever infected by Lumma.

