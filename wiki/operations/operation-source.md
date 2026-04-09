---
type: operation
title: "Operation Source"
title_ko: "Operation Source (Beebone 봇넷 해체)"
aliases: ["Beebone Botnet Takedown"]
case_id: "CYB-2015-003"
period: 1
operation_type: "takedown"
status: "completed"
enforcement_type: ["takedown", "seizure"]
outcome: "success"
timeframe:
  announced: "2015-04"
  start: "2015-04"
  end: "2015-04"
  ongoing: false
crime_type: "[[malware-ic]]"
target_entity: "Beebone Botnet (polymorphic)"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[eu-member-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[europol-ec3]]"
  - "[[j-cat]]"
  - "[[dutch-nhtcu]]"
  - "[[fbi]]"
  - "[[intel-security]]"
  - "[[kaspersky-lab]]"
  - "[[shadowserver]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 100
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "100+ command-and-control domains blocked"
    - "Polymorphic Beebone botnet neutralized"
edges:
  - source_actor: "Europol EC3"
    target_actor: "Dutch NHTCU"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "Europol EC3"
    target_actor: "FBI"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
credibility_index: 2.28
source_tier: 2
missing_fields: ["legal_basis", "mechanisms_used"]
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "[1] Europol News (2015-04)"
created: 2026-04-08
updated: 2026-04-08
---

## Summary

In April 2015, Europol and the Netherlands High Tech Crime Unit, in cooperation with the FBI, EU member state agencies, and major cybersecurity firms, conducted Operation Source to neutralize the polymorphic Beebone botnet. The operation blocked over 100 command-and-control server domains, disrupting the distribution of financial information-stealing malware, ransomware, rootkits, and fake antivirus software.

## Participating Parties

**Lead Agencies:**
- Europol European Cybercrime Centre (EC3)
- Joint Cybercrime Action Taskforce (J-CAT)
- Netherlands High Tech Crime Unit (NHTCU)

**Key Partners:**
- FBI (United States)
- Intel Security
- Kaspersky Lab
- Shadowserver

**Participating Countries:**
Netherlands, United States, EU member states (Germany, France, Italy, etc.)

## Results

- **100+ command-and-control domains** blocked
- Polymorphic Beebone botnet neutralized
- Distribution of ransomware, financial malware, rootkits disrupted

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | International Police Operation Targets Polymorphic Beebone Botnet | Europol | 2015-04 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/international-police-operation-targets-polymorphic-beebone-botnet) |
