---
type: operation
title: "Operation Source"
title_ko: "Operation Source (Beebone 봇넷 해체)"
aliases:
  - "Beebone Botnet Takedown"
case_id: CYB-2015-003
period: 1
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - seizure
outcome: success
timeframe:
  announced: 2015-04
  start: 2015-04
  end: 2015-04
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
legal_basis:

mechanisms_used:

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
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "Europol EC3"
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 2.28
source_tier: 2
missing_fields:
  - legal_basis
  - mechanisms_used
related_cases:

related_operations:

challenges_encountered:

lessons_learned:

source_count: 5
sources:
  - "[[europol-operation-source]]"
  - "[[2015-04-09_scworld-com_international-effort-takes-down-beebone-botnet]]"
  - "[[2015-04-09_securityweek-com_authorities-takedown-beebone-botnet-international-operation]]"
  - "[[2015-04-09_arstechnica_us-european-police-take-down-highly-elusive-botnet-known-as-beebone]]"
  - "[[2015-04-10_wired-com_beebone-botnet-bites-the-dust]]"
created: 2026-04-08
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "In April 2015, Europol and the Netherlands High Tech Crime Unit, in cooperation with the FBI, EU member state agencies, and major cybersecurity firms, conducted Operation Source to neutralize the polymorphic Beebone botnet. The operation blocked over 100 command-and-control server domains, disrupting the distribution of financial information-stealing malware, ransomware, rootkits, and fake antivirus software."
jurisdictions:
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[eu-member-states]]"
organizations:
  - "[[europol-ec3]]"
  - "[[j-cat]]"
  - "[[dutch-nhtcu]]"
  - "[[fbi]]"
  - "[[intel-security]]"
  - "[[kaspersky-lab]]"
  - "[[shadowserver]]"
crime_types:
  - "[[malware-ic]]"
  - "[[ransomware-ic]]"
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

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2015-04-09: Europol: International Police Operation Targets Polymorphic Beebone Botnet (Operation Source).
- SC Media, 2015-04-09: International effort takes down Beebone botnet.
- SecurityWeek, 2015-04-09: Authorities Takedown Beebone Botnet in International Operation.
- Ars Technica, 2015-04-09: US, European police take down highly elusive botnet known as Beebone.
- Wired, 2015-04-10: Beebone Botnet bites the dust.

## Operational Timeline

- 2015-04: activity or investigation start.
- 2015-04: public announcement.
- 2015-04: reported enforcement endpoint.
- 2015-04-09: public source coverage from Ars Technica, Europol, SC Media, SecurityWeek.
- 2015-04-10: public source coverage from Wired.

## Legal and Procedural Posture

- Recorded crime classification: malware and ransomware.
- Recorded enforcement posture: Takedown and Seizure.
- The record is categorized as takedown with status completed.

## Evidence and Attribution Notes

- Europol EC3, the Joint Cybercrime Action Taskforce (J-CAT), and the Dutch National High Tech Crime Unit (NHTCU) sinkholed the Beebone (W32/Worm-AAEH) polymorphic botnet on 8 April 2015 in a coordinated international action
- The botnet was neutralized by registering, suspending, or seizing command-and-control (C&C) domains used for malware communication — sinkhole methodology rather than server seizure
- 5 million unique polymorphic samples of the W32/Worm-AAEH family identified; 205,000+ samples collected from 23,000 systems across 195 countries during 2013-2014
- ~12,000 computers actively infected at time of takedown, though Europol noted many additional infections likely existed; United States had the most infections, followed by Japan, India, and Taiwan
- The operation used Beebone as a distribution vector for other malware: financial credential stealers, ransomware, rootkits, and fake antivirus software — making the takedown a force multiplier against multiple malware families
- Participating organizations: Europol EC3 (coordination), J-CAT, Dutch NHTCU, FBI, US National Cyber Investigative Joint Task Force, Eurojust (judicial coordination), plus private-sector partners Intel Security, Kaspersky Lab, Shadowserver, F-Secure, Symantec, and TrendMicro
- Operation Source is an early example of the public-private-partnership (PPP) model for botnet takedowns that would later be refined in Operations Avalanche (2016), Andromeda (2017), and Endgame (2024-2025)
- SC Media reported that Operation Source targeted the Beebone botnet through sinkholing and domain seizures.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Europol: International Police Operation Targets Polymorphic Beebone Botnet (Operation Source) | Europol | 2015-04-09 | https://www.europol.europa.eu/media-press/newsroom/news/international-police-operation-targets-polymorphic-beebone-botnet |
| [2] | International effort takes down Beebone botnet | SC Media | 2015-04-09 | https://www.scworld.com/news/international-effort-takes-down-beebone-botnet |
| [3] | Authorities Takedown Beebone Botnet in International Operation | SecurityWeek | 2015-04-09 | https://www.securityweek.com/authorities-takedown-beebone-botnet-international-operation/ |
| [4] | US, European police take down highly elusive botnet known as Beebone | Ars Technica | 2015-04-09 | https://arstechnica.com/information-technology/2015/04/us-european-police-take-down-highly-elusive-botnet-known-as-beebone/ |
| [5] | Beebone Botnet bites the dust | Wired | 2015-04-10 | https://www.wired.com/beyond-the-beyond/2015/04/beebone-botnet-bites-dust |
