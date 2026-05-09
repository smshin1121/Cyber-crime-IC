---
type: source
title: "Operazione \"ELICIUS\" — Polizia di Stato dismantles \"Diskstation\" ransomware gang in joint Italy-France-Romania task force coordinated by Europol"
raw_path: "raw/press-releases/2025-07-14_polizia-di-stato_operazione-elicius-diskstation-ransomware.md"
source_type: press-release
publisher: "Polizia di Stato — Servizio Polizia Postale e per la Sicurezza Cibernetica"
author: "Polizia di Stato (Italian State Police), Commissariato di P.S. on-line"
publish_date: 2025-07-14
ingest_date: 2026-05-10
language: it
reliability: high
credibility: confirmed
sensitivity: public
pages_updated:
  - "[[operazione-elicius-italy-france-romania-diskstation-ransomware-2025]]"
  - "[[italy-polizia-postale]]"
  - "[[polizia-di-stato]]"
  - "[[france-national-police]]"
  - "[[romania-police]]"
  - "[[europol-ec3]]"
  - "[[italy]]"
  - "[[france]]"
  - "[[romania]]"
  - "[[ransomware-ic]]"
key_findings:
  - "Italy-led Polizia di Stato investigation coordinated by Procura di Milano dismantled \"Diskstation\" ransomware gang targeting Italian SMEs (graphic-design, film-production, event-management, civil-rights NGO sectors)."
  - "Joint task force formally established under Europol coordination with French and Romanian national police — explicit naming in tier-1 source satisfies L24 ≥2-country IC requirement."
  - "Searches conducted June 2024 in Bucharest at suspects' residences with operators of the Centro Operativo per la Sicurezza Cibernetica (C.O.S.C.) di Milano participating; suspects caught in flagrante delicto."
  - "Primary suspect: 44-year-old Romanian national, placed in pre-trial detention in prison by GIP Tribunale di Milano on charges of unauthorised computer access (art. 615-ter Italian Criminal Code) and extortion (art. 629 Italian Criminal Code)."
  - "Multiple additional Romanian-nationality suspects identified across the criminal chain; investigative methodology = parallel forensic analysis of compromised systems + blockchain analysis of cryptocurrency ransom flows."
  - "Public release date: 14 July 2025; underlying searches: June 2024 → ~13-month evidentiary lag from operational action to disclosure."
created: 2026-05-10
---

## Source Summary

Tier-1 primary source: official Polizia di Stato press release on the agency's national portal (commissariatodips.it). The release announces the conclusion of the investigative phase of Operazione "ELICIUS", a joint Italy-France-Romania action under Europol coordination against the "Diskstation" ransomware gang. The Italian original explicitly names — twice — the foreign LE partners ("le polizie nazionali di Francia e Romania"), satisfying the iter 124 L24 strict ≥2-country IC requirement that participating jurisdictions must be named LE/prosecutorial agencies acknowledged in the tier-1 source.

## IC Pattern

- **Crime type:** ransomware against SMEs, double-extortion model with Bitcoin ransom demand. Targets exploited vulnerabilities in Synology DiskStation NAS appliances (gang's eponymous moniker).
- **IC structure:** Italian-led parallel investigation (Procura di Milano + Polizia Postale C.O.S.C. Milano) → Europol-coordinated **task force** with French and Romanian national police as foreign LE partners. France and Romania were independently investigating the same group; Europol provided the coordination shell to merge efforts.
- **Methodology fingerprint:** dual-track investigation = (a) host-side forensic analysis of compromised victim systems + (b) blockchain analysis of cryptocurrency ransom flows. Cross-border execution = Italian C.O.S.C. operators physically deployed to Bucharest searches in June 2024.
- **Custody pathway:** charges filed in Milan, pre-trial detention applied by Italian GIP — i.e. principal suspect held in Italy under Italian charges, not extradited from Romania. (Suggests EAW or arrest in flagrante by joint team — primary source mentions "in flagrante" arrest during Bucharest searches.)

## Wiki Cross-Corpus Relevance

This is the wiki's first standalone Italy-France-Romania ransomware joint task force record under Europol coordination. Closest precedents:
- [[operation-eastwood]] (NoName057(16) DDoS, July 2025) — Europol-coordinated multi-EU + US action, but distinct crime type (DDoS hacktivism) and different participating roster.
- [[operation-cronos-phase1|Operation Cronos (LockBit)]] — Europol-coordinated ransomware takedown but distinct gang and broader participant roster.

Operation Elicius adds:
- **Italy-Romania bilateral evidentiary cooperation** — Italian operators participating in Bucharest searches at suspects' residences. New record of cross-border physical investigative deployment in EU ransomware context.
- **NAS-vulnerability ransomware as IC subtype** — first wiki record of a ransomware operation specifically tied to Synology DiskStation NAS exploitation (vs. RDP/VPN/phishing initial access).
- **Procura di Milano as Italian central judicial authority for ransomware IC** — augments existing wiki coverage of Italian prosecution offices in cybercrime IC operations.
