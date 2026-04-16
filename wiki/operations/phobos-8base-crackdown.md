---
aliases:
- Phobos 8Base operation
- 8Base arrests Feb 2025
case_id: CYB-2025-003
challenges_encountered: []
coordinating_body: '[[europol-ec3]]'
created: 2026-04-08
credibility_index: 3.25
crime_type: '[[ransomware-ic]]'
edges:
- cooperation_type: joint_investigation
  direction: undirected
  legal_basis: unknown
  source_actor: Europol
  target_actor: FBI
- cooperation_type: extradition
  direction: directed
  legal_basis: MLAT
  source_actor: South Korea Police
  target_actor: FBI
- cooperation_type: joint_investigation
  direction: undirected
  legal_basis: unknown
  source_actor: Europol
  target_actor: Eurojust
enforcement_type:
- arrest
- seizure
- takedown
- extradition
lead_agency: '[[europol-ec3]]'
legal_basis: []
lessons_learned:
- Multi-year sustained investigation (2019-2025) with 37 operational meetings enabled
  identification of leadership
- Prior arrests of affiliates and administrators in various countries built intelligence
  for the final crackdown
- Proactive victim notification (400+ companies) demonstrated a protective dimension
  beyond enforcement
- South Korea-US extradition of Phobos administrator demonstrates East Asian contribution
  to global ransomware enforcement
mechanisms_used: []
missing_fields:
- legal_basis
- mechanisms_used
- specific_korean_agency
- extradition_legal_basis
operation_type: arrest-sweep
outcome: success
participating_agencies:
- '[[europol-ec3]]'
- '[[eurojust]]'
- '[[belgium-federal-police]]'
- '[[czechia-police]]'
- '[[france-national-police]]'
- '[[germany-bka]]'
- '[[japan-npa]]'
- '[[poland-police]]'
- '[[romania-police]]'
- '[[singapore-police]]'
- '[[spain-guardia-civil]]'
- '[[sweden-police]]'
- '[[switzerland-fedpol]]'
- '[[thailand-royal-police]]'
- '[[uk-nca]]'
- '[[fbi-cyber-division]]'
participating_countries:
- '[[belgium]]'
- '[[czechia]]'
- '[[france]]'
- '[[germany]]'
- '[[japan]]'
- '[[poland]]'
- '[[romania]]'
- '[[singapore]]'
- '[[spain]]'
- '[[sweden]]'
- '[[switzerland]]'
- '[[thailand]]'
- '[[united-kingdom]]'
- '[[united-states]]'
period: 3
related_cases: []
related_operations: []
results:
  arrests: 4
  cryptocurrency_seized: ''
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:
  - 'Prior arrests: Phobos administrator in South Korea (June 2024), extradited to
    US (Nov 2024)'
  - 'Prior arrest: Phobos affiliate in Italy (2023) on French warrant'
  - 37 Europol operational meetings
  - ~600 SIENA operational messages
  - 2 Eurojust coordination meetings
  servers_seized: 27
  victims_notified: 400
source_count: 1
source_tier: 2
sources:
- '[[2025-02-11-europol-phobos-8base-ransomware-arrests]]'
status: completed
target_entity: Phobos and 8Base ransomware groups
timeframe:
  announced: '2025-02-11'
  end: 2025-02
  ongoing: false
  start: 2019-02
title: Phobos/8Base Ransomware Crackdown
type: operation
updated: '2026-04-09'
---

## Summary

The **Phobos/8Base Ransomware Crackdown** was a coordinated international operation that resulted in the arrest of **4 Russian nationals** who were key figures behind the **8Base** ransomware group, and the takedown of **27 servers** connected to their criminal network. Announced on 11 February 2025, the operation involved 14 countries and 16 agencies, with [[europol-ec3|Europol]] having coordinated the investigation since February 2019.

This operation is *almost certainly* one of the most significant for the Korean international cooperation context, as it includes the **arrest of a Phobos administrator in [[south-korea|South Korea]]** in June 2024 and subsequent extradition to the United States in November 2024.

## Background

**Phobos** ransomware emerged around 2018 and became one of the more prolific ransomware families, characterized by its deployment through compromised Remote Desktop Protocol (RDP) connections. **8Base** was a ransomware group that *likely* operated as a major user and distributor of Phobos ransomware.

[[europol-ec3|Europol]] began supporting the investigation in February 2019, making this a sustained multi-year effort spanning approximately 6 years before the final arrests. During this period, 37 operational meetings were organized and nearly 600 operational messages were exchanged via SIENA.

Prior enforcement actions that built toward the February 2025 crackdown:
- **2023:** Key Phobos affiliate arrested in Italy on a French arrest warrant
- **June 2024:** Phobos administrator arrested in **South Korea**
- **November 2024:** Phobos administrator extradited from South Korea to the United States

## Participating Parties

### Coordinating Bodies
- [[europol-ec3|Europol]] — coordination since February 2019, 37 operational meetings
- [[eurojust|Eurojust]] — 2 coordination meetings

### Participating Countries (14)
Belgium, Czechia, France, Germany, Japan, Poland, Romania, Singapore, Spain, Sweden, Switzerland, Thailand, United Kingdom, United States

### Participating Agencies (16)
[[europol-ec3]], [[eurojust]], [[belgium-federal-police|Belgian Federal Police]], [[czechia-police|Czech Police]], [[france-national-police|French National Police]], [[germany-bka|German BKA]], [[japan-npa|Japanese NPA]], [[poland-police|Polish Police]], [[romania-police|Romanian Police]], [[singapore-police|Singapore Police Force]], [[spain-guardia-civil|Spanish Guardia Civil]], [[sweden-police|Swedish Police]], [[switzerland-fedpol|Swiss Fedpol]], [[thailand-royal-police|Royal Thai Police]], [[uk-nca|UK NCA]], [[fbi-cyber-division|FBI]]

## Legal Framework

- **Italy (2023):** Arrest of Phobos affiliate on French arrest warrant — demonstrating European Arrest Warrant / Eurojust-facilitated cross-border arrests
- **South Korea (June 2024):** Arrest of Phobos administrator — *likely* under bilateral cooperation framework or Interpol Red Notice
- **South Korea to US (November 2024):** Extradition of Phobos administrator — *likely* under Korea-US bilateral extradition treaty

> [!warning] Legal status check needed
> Exact legal basis for the South Korea arrest and Korea-US extradition needs to be confirmed from additional sources.

## Operational Timeline

| Date | Event |
|------|-------|
| 2019-02 | Europol begins supporting investigation |
| 2023 | Phobos affiliate arrested in Italy on French warrant |
| 2024-06 | Phobos administrator arrested in South Korea |
| 2024-11 | Phobos administrator extradited from South Korea to US |
| 2025-02 | 4 Russian nationals arrested (8Base leadership) |
| 2025-02 | 27 servers taken down |
| 2025-02 | 400+ companies warned of ongoing/imminent attacks |
| 2025-02-11 | Public announcement by Europol |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests (Feb 2025) | 4 (Russian nationals, 8Base leadership) |
| Prior arrests | 2+ (Italy 2023, South Korea 2024) |
| Servers taken down | 27 |
| Companies warned | 400+ |
| Europol operational meetings | 37 |
| SIENA messages | ~600 |
| Investigation duration | ~6 years |

The proactive warning of 400+ companies of ongoing or imminent ransomware attacks demonstrated a *highly likely* effective protective dimension that went beyond traditional enforcement.

## Cooperation Mechanisms Used

- **SIENA:** ~600 operational messages over the investigation
- **Europol operational meetings:** 37 meetings across the 6-year investigation
- **Eurojust coordination:** 2 coordination meetings for judicial cooperation
- **Extradition:** South Korea to US (November 2024)
- **European Arrest Warrant / equivalent:** Italy arrest on French warrant (2023)

## Lessons Learned

1. **Long-duration investigations yield leadership targets:** The 6-year investigation timeline enabled identification of leadership rather than just operational affiliates.
2. **Building on prior arrests:** Each prior arrest (Italy 2023, South Korea 2024) generated intelligence that contributed to the final 8Base leadership crackdown.
3. **Proactive victim protection:** Warning 400+ companies of ongoing or imminent attacks demonstrates that enforcement operations can have immediate protective effects.
4. **East Asian cooperation:** The South Korea arrest and extradition demonstrates that ransomware enforcement reaches beyond the traditional EU-US axis.

## Korean Involvement (한국의 참여)

**This operation has direct Korean involvement:**

- **June 2024:** Phobos administrator arrested in **South Korea** (대한민국)
- **November 2024:** Extradited from South Korea to the United States

This represents a significant instance of Korean participation in international ransomware enforcement. The arrest and extradition *likely* involved Korea's [[knpa-cyber-bureau|Cyber Investigation Bureau (사이버수사국)]] and [[spo-international-cooperation|Ministry of Justice International Criminal Affairs Division (법무부 국제형사과)]], though the specific Korean agencies are not named in the Europol press release.

The successful extradition demonstrates the practical effectiveness of the Korea-US bilateral relationship for cybercrime cooperation, consistent with [[south-korea|South Korea's cooperation profile]].

## Contradictions & Open Questions

- Which specific Korean agency executed the arrest of the Phobos administrator?
- What was the legal basis for the South Korea arrest (Red Notice, MLAT, bilateral cooperation)?
- What was the specific legal basis for the Korea-US extradition?
- What role, if any, did Korean digital forensics play in the broader investigation?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Key figures behind Phobos and 8Base ransomware arrested in international cybercrime crackdown | Europol | 2025-02-11 | [원본](https://www.europol.europa.eu/media-press/newsroom/news/key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown) |
