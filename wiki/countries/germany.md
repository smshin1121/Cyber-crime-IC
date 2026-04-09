---
bilateral_agreements:
- '[[us-germany-mlat]]'
central_authority:
  budapest: Bundeskriminalamt (BKA)
  mlat: Federal Office of Justice (Bundesamt für Justiz, BfJ)
cooperation_assessment: Germany is a highly capable cooperation partner with strong
  technical capacity, experienced cybercrime prosecutors (particularly at ZIT Frankfurt),
  and deep integration into EU cooperation mechanisms via Europol and Eurojust. Germany
  has been a key infrastructure host for major takedown operations (Avalanche, Endgame).
  Data retention limitations due to constitutional court decisions may affect some
  cooperation scenarios.
created: 2026-04-08
cybercrime_legislation:
  data_retention: Contested; Telecommunications Act (TKG) provisions largely struck
    down by courts; limited retention in practice
  primary_law: Strafgesetzbuch (StGB) §§ 202a-202d, 303a-303b; BSI-Gesetz
  primary_law_date: '1986-08-15'
  procedural_powers:
  - search-and-seizure
  - production-order
  - preservation-order
  - interception
  - real-time-collection
ic_capacity:
  24_7_availability: true
  avg_mlat_response_days: 90-180
  digital_forensics: high
  english_proficiency: high
  rating: high
iso_code: DE
key_agencies:
- '[[germany-bka]]'
- '[[zit-frankfurt]]'
last_verified: '2026-04-10'
legal_system: civil-law
notable_cases: []
operations_participated:
- '[[operation-endgame-phase1]]'
- '[[operation-endgame-phase2]]'
- '[[operation-cronos-phase1]]'
- '[[operation-cronos-phase3]]'
- '[[operation-avalanche]]'
- '[[phobos-8base-crackdown]]'
- '[[qakbot-gallyamov-indictment]]'
- '[[operation-haechi-v]]'
- '[[hive-ransomware-takedown]]'
region: western-europe
source_count: 0
sources: []
title: Federal Republic of Germany
treaty_memberships:
- date: '2009-03-09'
  framework: '[[budapest-convention]]'
  reservations: []
  status: party
- date: '2022'
  framework: '[[second-additional-protocol]]'
  reservations: []
  status: signatory
type: country
updated: 2026-04-08
---

## Summary

Germany is a **key pillar** of European cybercrime cooperation. The **Bundeskriminalamt (BKA)** ([[germany-bka]]) and the specialized cybercrime prosecutor's office in Frankfurt (**Zentralstelle zur Bekämpfung der Internetkriminalität, ZIT**) have led or co-led some of the most significant cybercrime operations in history, including [[operation-avalanche|Operation Avalanche]] (2016) and [[operation-endgame-phase1|Operation Endgame]] (2024-2025).

Germany's central position in European internet infrastructure makes it both a frequent target and a key partner in infrastructure takedowns. German authorities *almost certainly* host more seized criminal infrastructure during takedown operations than any other EU member state.

## Legal Framework for Cybercrime

### Substantive Criminal Law

**Strafgesetzbuch (StGB) — Criminal Code:**
- § 202a: Data espionage (Ausspähen von Daten)
- § 202b: Phishing / interception of data (Abfangen von Daten)
- § 202c: Acts preparatory to data espionage and phishing (Vorbereiten des Ausspähens und Abfangens von Daten)
- § 202d: Handling stolen data (Datenhehlerei)
- § 263a: Computer fraud (Computerbetrug)
- § 303a: Data manipulation (Datenveränderung)
- § 303b: Computer sabotage (Computersabotage)

**BSI-Gesetz (Federal Office for Information Security Act):**
- Framework for critical infrastructure protection
- Reporting obligations for operators of critical infrastructure

**Netzwerkdurchsetzungsgesetz (NetzDG):**
- Social media compliance obligations for content moderation

### Procedural Powers

- **Search and seizure:** Strafprozessordnung (StPO) §§ 94-98, 102-110; includes electronic evidence
- **Interception:** StPO § 100a; telecommunications surveillance requires court order
- **Online search (Onlinedurchsuchung):** StPO § 100b; remote access to devices; highly restricted, requires judicial authorization for specific serious offences
- **Preservation:** Available under MLA framework; informal police-to-police preservation requests through INTERPOL/Europol channels
- **Data retention:** Contested — Federal Constitutional Court and CJEU rulings have limited mandatory data retention; current framework under TKG provides limited retention capabilities

### Mutual Legal Assistance

- **Central authority:** Bundesamt für Justiz (Federal Office of Justice) for formal MLAT requests
- **Execution:** BKA and state criminal police (Landeskriminalämter) execute operational requests
- **EU MLA instruments:** European Investigation Order (EIO) for EU requests — significantly faster than traditional MLAT
- **Federal structure challenge:** Germany's 16 Länder each have their own criminal justice systems; some MLA requests require coordination with state authorities

> [!warning] Legal status check needed
> Verify current status of German data retention legislation following CJEU and BVerfG rulings (as of 2024-2025).

## Treaty Memberships

| Framework | Status | Date | Notes |
|-----------|--------|------|-------|
| [[budapest-convention]] | Party | 2009 | |
| [[second-additional-protocol]] | Signatory | 2022 | |
| UNTOC (Palermo Convention) | Party | 2006 | |
| UNCAC | Party | 2014 | |
| EU European Investigation Order | Participating | 2017 | Transposed into national law |
| US-Germany MLAT | In force | 2010 | |

Germany participates in the Budapest Convention **[[24-7-network]]** and Europol's operational networks.

## Key Agencies

### Bundeskriminalamt (BKA)
See [[germany-bka]] for full profile.
- Federal criminal police; primary IC operational agency
- Houses cybercrime investigation units
- INTERPOL NCB Germany
- Key Europol partner; BKA officers co-located at Europol

### Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT)
- Central Office for Combating Internet Crime, based in Frankfurt am Main
- Part of the Generalstaatsanwaltschaft Frankfurt (General Prosecutor's Office)
- *Highly likely* the most prolific cybercrime prosecution office in continental Europe
- Led prosecutorial side of [[operation-endgame-phase1]], [[operation-endgame-phase2]], [[operation-avalanche]]

### Bundesamt für Verfassungsschutz (BfV)
- Federal Office for the Protection of the Constitution (domestic intelligence)
- Handles state-sponsored cyber espionage threat assessment

### Bundesamt für Sicherheit in der Informationstechnik (BSI)
- Federal Office for Information Security
- National CERT; critical infrastructure protection
- Provides technical analysis support to BKA

## Cooperation Track Record

### As Requesting State

Germany actively sends MLA requests, particularly for:
- Evidence from US-based technology providers
- EU cross-border investigations via European Investigation Order
- Financial crime data from banking jurisdictions

### As Requested State

Germany is *likely* a responsive cooperation partner, though the federal structure can add complexity. The BKA serves as the primary coordination point, but execution may involve state-level authorities (Landeskriminalämter).

### Infrastructure Host for Takedowns

Germany has served as the primary infrastructure host for major operations:
- **[[operation-avalanche]]** (2016): BKA and ZIT co-led; 39 servers seized in Germany; 50+ countries involved
- **[[operation-endgame-phase1]]** (2024): BKA/ZIT led; largest botnet takedown in history
- **[[operation-endgame-phase2]]** (2025): Continuation; 300 servers, 650 domains seized

## Korean Interactions (한국과의 협력)

Korea-Germany cybercrime cooperation is *likely* conducted primarily through multilateral channels:

- **Europol-coordinated operations:** Germany and Korea both participated in [[phobos-8base-crackdown]] (2025) and [[operation-haechi-v]] (2024)
- **Budapest Convention:** Both parties (Germany since 2009, Korea since 2024), providing mutual MLA basis
- **EU-Korea cooperation:** Germany is a key EU member state; broader EU-Korea cooperation frameworks facilitate information sharing
- **No known dedicated bilateral cybercrime MOU** between Korea and Germany

> [!note]
> This page is based on general knowledge of German cybercrime cooperation structures and publicly available information. No collected sources have been ingested for this country profile. Content should be verified against primary sources.

## Contradictions & Open Questions

- What is the practical impact of Germany's data retention limitations on international cooperation?
- How does Germany's federal structure affect MLAT response times?
- What is the current staffing and capacity of ZIT Frankfurt?
- What is the status of Germany's implementation of the Second Additional Protocol?

## References

> [!note]
> This page was created based on general knowledge. No dedicated sources have been ingested (source_count: 0). Key claims should be verified against BKA annual reports, ZIT publications, and Council of Europe data.
