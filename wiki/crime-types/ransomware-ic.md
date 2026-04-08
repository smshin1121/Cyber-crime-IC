---
type: crime-type
title: "Ransomware — International Cooperation Perspective"
aliases: ["ransomware", "ransomware-as-a-service", "RaaS"]
crime_category: "cyber-dependent"
typical_ic_challenges: []
relevant_legal_frameworks:
  - "[[budapest-convention]]"
typical_mechanisms: []
key_organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
  - "[[uk-nca]]"
notable_operations:
  - "[[operation-cronos-phase1]]"
  - "[[operation-endgame-phase1]]"
  - "[[operation-cronos-phase3]]"
  - "[[phobos-8base-crackdown]]"
  - "[[operation-endgame-phase2]]"
  - "[[qakbot-gallyamov-indictment]]"
  - "[[operation-checkmate-blacksuit]]"
  - "[[operation-synergia-ii]]"
  - "[[operation-serengeti]]"
notable_cases: []
criminalization_status:
  broadly_criminalized: true
  definition_varies: true
  problem_jurisdictions: []
estimated_annual_loss: "Billions of USD globally (exact figure uncertain)"
source_count: 8
sources:
  - "[[2024-02-20-europol-operation-cronos-lockbit]]"
  - "[[2024-05-30-europol-operation-endgame-botnet-takedown]]"
  - "[[2024-10-01-europol-operation-cronos-lockbit-phase3]]"
  - "[[2025-02-11-europol-phobos-8base-ransomware-arrests]]"
  - "[[2025-05-23-europol-operation-endgame-phase2]]"
  - "[[2025-05-22-doj-qakbot-gallyamov-indictment]]"
  - "[[2025-08-11-doj-blacksuit-royal-ransomware-takedown]]"
  - "[[2024-11-06-interpol-operation-synergia-ii]]"
created: 2026-04-08
updated: 2026-04-08
---

## Summary

Ransomware is *almost certainly* the single most significant cybercrime type driving international cooperation in the 2020s. Ransomware attacks encrypt victims' data and demand payment (typically in cryptocurrency) for decryption keys. The Ransomware-as-a-Service (RaaS) model, where developers provide tools to affiliates in exchange for a share of ransom payments, has created a complex criminal ecosystem that spans multiple jurisdictions and requires coordinated international responses.

From an international cooperation perspective, ransomware presents unique challenges: perpetrators are *almost certainly* predominantly based in jurisdictions with limited cooperation willingness, infrastructure is distributed across dozens of countries, cryptocurrency payments cross borders instantly, and victims span every sector and region globally.

The period from February 2024 to August 2025 saw an unprecedented intensification of international enforcement against ransomware. Europol coordinated 5 major operations, while DOJ led 2 additional actions and INTERPOL coordinated infrastructure-focused operations:

| Operation | Date | Target | Key Results |
|-----------|------|--------|-------------|
| [[operation-cronos-phase1]] | Feb 2024 | LockBit | 34 servers, 2 arrests, 5 indictments |
| [[operation-endgame-phase1]] | May 2024 | Dropper malware | 100+ servers, 2,000+ domains, 4 arrests |
| [[operation-cronos-phase3]] | Oct 2024 | LockBit/Evil Corp | 4 arrests, sanctions |
| [[phobos-8base-crackdown]] | Feb 2025 | Phobos/8Base | 4 arrests, 27 servers |
| [[operation-endgame-phase2]] | May 2025 | Initial-access malware | 300 servers, 650 domains, 20 warrants |
| [[qakbot-gallyamov-indictment]] | May 2025 | QakBot/Gallyamov | Indictment, USD 24M+ crypto seized |
| [[operation-checkmate-blacksuit]] | Aug 2025 | BlackSuit (Royal) | 4 servers, 9 domains, USD 1.1M crypto |
| [[operation-synergia-ii]] | Nov 2024 | Cyber infrastructure | 22,800 IPs, 59 servers, 41 arrests (INTERPOL) |

## Criminalization Landscape

Ransomware is broadly criminalized worldwide, though the specific legal provisions vary:

- **Under cybercrime statutes:** Most jurisdictions criminalize unauthorized access, data interference, and system interference — provisions that cover ransomware
- **Under extortion/blackmail statutes:** Ransomware demands constitute extortion in most legal systems
- **Under organized crime statutes:** RaaS operations *likely* qualify as criminal organization activity in many jurisdictions

The [[budapest-convention|Budapest Convention]] provides the most comprehensive international framework for ransomware cooperation, with Articles 2-6 (substantive offenses) covering the conduct underlying ransomware, and Articles 29-35 (international cooperation) providing the procedural mechanisms.

> [!warning] Legal status check needed
> The exact criminalization provisions for ransomware across key jurisdictions need to be mapped from additional sources.

## Typical IC Scenarios

### Scenario 1: Major RaaS Group Takedown
**Pattern:** Multi-year investigation culminating in coordinated action day.
**Example:** [[operation-cronos-phase1|Operation Cronos]] (LockBit) and [[phobos-8base-crackdown|Phobos/8Base Crackdown]]
- Duration: Years of intelligence gathering
- Scale: 10-14 countries, 12-16 agencies
- Coordination: Europol (operational), Eurojust (judicial)
- Results: Arrests, server seizures, cryptocurrency freezing, indictments

### Scenario 2: Infrastructure Disruption (Supply Chain Attack)
**Pattern:** Targeting the dropper malware and initial-access infrastructure that enables ransomware deployment.
**Example:** [[operation-endgame-phase1|Operation Endgame Phase 1]] and [[operation-endgame-phase2|Phase 2]]
- Strategic rationale: Disrupting the upstream supply chain affects multiple ransomware groups simultaneously
- Scale: 100-300+ servers, 650-2,000+ domains per phase
- Force multiplier: Disrupting 6-7 malware families impacts 15+ ransomware groups

### Scenario 3: Follow-Up Enforcement (Sustained Pressure)
**Pattern:** Phased operations that maintain pressure beyond initial takedown.
**Example:** [[operation-cronos-phase3|Operation Cronos Phase 3]]
- Additional arrests months after initial action
- Expansion to financial sanctions (coordination with treasury/finance authorities)
- Identity reveals and most-wanted listings to deter future activity

## Evidence Types and Locations

Ransomware investigations typically involve evidence distributed across:
- **Command and control servers:** Hosted in multiple countries, often on bulletproof hosting
- **Cryptocurrency wallets and exchanges:** Cross-border by nature; require cooperation with exchanges and blockchain analysis
- **Victim systems and logs:** In dozens of countries simultaneously
- **Communication platforms:** Typically encrypted, hosted by various providers
- **Financial records:** Banking data in money laundering countries

## Cooperation Pathways

### Europol-Coordinated Model (Primary Pathway)
The dominant model for major ransomware operations:
1. [[europol-ec3|Europol EC3]] provides coordination hub and analytical support
2. [[eurojust|Eurojust]] provides judicial coordination
3. Participating countries contribute national investigative resources
4. Action days executed simultaneously across multiple countries
5. Post-action phases continue investigation and enforcement

### Key Mechanisms
- **SIENA:** Secure messaging for operational coordination (1,000+ messages for Operation Cronos)
- **Europol operational meetings:** Regular coordination meetings (27 for Cronos, 37 for Phobos/8Base)
- **Joint Investigation Teams (JITs):** Formal multi-country investigative teams
- **No More Ransom:** Public-private decryption tool distribution portal

## Key Operations and Precedents

### Cumulative Enforcement Statistics (Feb 2024 - Aug 2025)

| Metric | Total |
|--------|-------|
| Operations | 8 (5 Europol-coordinated + 2 DOJ-led + 1 INTERPOL) |
| Arrests | 55+ (14 Europol + 41 Synergia II) |
| Servers seized/taken down | 533+ |
| Domains seized/neutralized | 2,659+ |
| IPs taken down | 22,800 (Synergia II) |
| Cryptocurrency seized | EUR 21.2M+ (Endgame) + USD 25.1M+ (QakBot + BlackSuit) + 200+ accounts (Cronos) |
| International arrest warrants | 23+ |
| EU Most Wanted additions | 18 |
| Companies warned | 400+ |
| Countries participating | 95+ unique (Synergia II alone involved 95) |

### Operation Details

**[[operation-cronos-phase1|Operation Cronos Phase 1]]** (February 2024): Disrupted LockBit, the world's most deployed ransomware. 10 countries, 12 agencies, led by [[uk-nca|UK NCA]]. 34 servers seized, 2 arrests, free decryption tools released.

**[[operation-endgame-phase1|Operation Endgame Phase 1]]** (May 2024): Largest-ever botnet takedown targeting dropper malware. 13 countries, 15 agencies. 100+ servers, 2,000+ domains, 4 arrests. Strategic shift to upstream infrastructure targeting.

**[[operation-cronos-phase3|Operation Cronos Phase 3]]** (October 2024): 4 new LockBit arrests, 9 servers seized. First coordinated financial sanctions against ransomware-linked actors (Australia/UK/US vs Evil Corp affiliates).

**[[phobos-8base-crackdown|Phobos/8Base Crackdown]]** (February 2025): 4 Russian nationals (8Base leadership) arrested, 27 servers taken down. 6-year investigation. Notable for Phobos administrator arrest in [[south-korea|South Korea]] and extradition to US.

**[[operation-endgame-phase2|Operation Endgame Phase 2]]** (May 2025): 300 servers, 650 domains, EUR 3.5M seized. 20 international arrest warrants, 18 EU Most Wanted listings.

**[[qakbot-gallyamov-indictment|QakBot/Gallyamov Indictment]]** (May 2025): DOJ-led multinational effort. Indictment of Qakbot leader Rustam Gallyamov (Moscow, Russia). USD 24M+ in cryptocurrency seized. 7 countries and Europol cooperated. Continues from FBI's August 2023 QakBot botnet takedown. Notable for demonstrating that infrastructure takedowns alone may not stop determined operators.

**[[operation-checkmate-blacksuit|Operation Checkmate]]** (August 2025): DOJ-led takedown of BlackSuit (formerly Royal) ransomware. 4 servers, 9 domains seized across 8 countries. USD 1.1M cryptocurrency seized. 5 US agencies (DOJ, HSI, USSS, IRS-CI, FBI) plus 7 international partners.

**[[operation-synergia-ii|Operation Synergia II]]** (April-August 2024): INTERPOL-coordinated infrastructure operation across 95 countries targeting phishing, ransomware, and information stealer infrastructure. 22,800 malicious IPs taken down, 59 servers seized, 41 arrests. Demonstrated INTERPOL's unique global convening power alongside private sector partners (Group-IB, Trend Micro, Kaspersky, Team Cymru).

## Challenges

### Jurisdictional Safe Havens
Ransomware operators are *almost certainly* predominantly based in jurisdictions (particularly Russia) where extradition and cooperation with Western law enforcement are not available. This creates a persistent enforcement gap that limits the reach of international cooperation.

### Cryptocurrency and Financial Flows
While cryptocurrency seizures have become more effective (EUR 21.2M+ in Operation Endgame alone), the speed and global reach of cryptocurrency transfers continue to challenge traditional asset freezing mechanisms.

### Scale and Complexity
The RaaS model creates a distributed criminal ecosystem: developers, affiliates, initial-access brokers, money launderers, and bulletproof hosting providers each operate in different jurisdictions, requiring multi-pronged enforcement strategies.

### Reconstitution
Ransomware groups *likely* reconstitute operations relatively quickly after takedowns by rebuilding infrastructure in new locations. This motivates the phased, sustained operational approach seen in Operations Cronos and Endgame.

## Statistics and Trends

Based on the 8 ingested operations (2024-2025), key trends include:
1. **Increasing scale:** From 34 servers (Cronos Phase 1) to 300 servers (Endgame Phase 2) over 15 months
2. **Supply chain targeting:** Shift from targeting ransomware groups directly to disrupting upstream dropper/initial-access infrastructure
3. **Financial sanctions integration:** First use of coordinated financial sanctions alongside criminal enforcement (Cronos Phase 3)
4. **Sustained campaigns:** Multi-phase operations (Cronos: 3+ phases; Endgame: 2+ phases) rather than one-off actions
5. **Proactive victim protection:** Warning 400+ companies of imminent attacks (Phobos/8Base)

## Prevention and Disruption

International cooperation on ransomware includes both reactive (enforcement) and proactive (disruption) elements:
- **No More Ransom portal:** Europol-led initiative providing free decryption tools (37 languages, 120+ solutions)
- **Victim notifications:** Proactive warnings to potential victims (400+ companies in Phobos/8Base operation)
- **Infrastructure takedowns:** Removing servers and domains to disrupt operations
- **Financial disruption:** Cryptocurrency seizures and account freezing

## Korean Context (한국 상황)

Korea's involvement in international ransomware enforcement was demonstrated by the [[phobos-8base-crackdown|Phobos/8Base operation]], where a Phobos administrator was arrested in South Korea (June 2024) and extradited to the United States (November 2024). This case is *highly likely* the most significant instance of Korean participation in international ransomware enforcement actions.

Korea's 2024 accession to the [[budapest-convention]] enhances the legal framework for future ransomware cooperation, providing enhanced channels for evidence preservation (Art. 29), mutual assistance for stored data (Art. 31), and 24/7 network contact (Art. 35).

## Contradictions & Open Questions

- What is the measurable impact of these operations on global ransomware attack rates?
- How quickly do targeted groups reconstitute after takedowns?
- What is the actual recovery rate for ransomware victims through decryption tools?
- How effective are financial sanctions as a long-term deterrent for ransomware actors?
- What proportion of ransomware proceeds is successfully seized through international cooperation?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Law enforcement disrupt world's biggest ransomware operation — Operation Cronos (LockBit) | Europol | 2024-02-20 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation) |
| [2] | Largest ever operation against botnets — Operation Endgame | Europol | 2024-05-30 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem) |
| [3] | LockBit power cut: four new arrests — Operation Cronos Phase 3 | Europol | 2024-10-01 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/lockbit-power-cut-four-new-arrests-and-financial-sanctions-against-affiliates) |
| [4] | Key figures behind Phobos and 8Base ransomware arrested | Europol | 2025-02-11 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown) |
| [5] | Operation Endgame strikes again: the ransomware kill chain broken at its source | Europol | 2025-05-23 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source) |
| [6] | Leader of Qakbot Malware Conspiracy Indicted — Gallyamov | US DOJ | 2025-05-22 | [원본](https://www.justice.gov/opa/pr/leader-qakbot-malware-conspiracy-indicted-involvement-global-ransomware-scheme) |
| [7] | Coordinated Disruption Actions Against BlackSuit (Royal) Ransomware — Operation Checkmate | US DOJ | 2025-08-11 | [원본](https://www.justice.gov/opa/pr/justice-department-announces-coordinated-disruption-actions-against-blacksuit-royal) |
| [8] | INTERPOL cyber operation takes down 22,000 malicious IP addresses — Operation Synergia II | INTERPOL | 2024-11-06 | [원본](https://www.interpol.int/News-and-Events/News/2024/INTERPOL-cyber-operation-takes-down-22-000-malicious-IP-addresses) |
