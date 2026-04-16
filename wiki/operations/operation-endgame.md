---
type: operation
title: "Operation Endgame"
aliases:
  - "Endgame"
  - "Europol Endgame"
operation_type: "takedown"
status: "ongoing"
enforcement_type:
  - "arrest"
  - "seizure"
  - "takedown"
  - "asset_freeze"
  - "indictment"
outcome: "success"
timeframe:
  announced: "2024-05-30"
  start: "2024-05-27"
  end: ""
  ongoing: true
crime_type: "[[ransomware-ic]]"
target_entity: "Dropper/loader malware ecosystem enabling ransomware (IcedID, SystemBC, Pikabot, Smokeloader, Bumblebee, Trickbot, DanaBot, Qakbot, Bumblebee, Lactrodectus, Hijackloader, Warmcookie, Rhadamanthys)"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[australia]]"
  - "[[armenia]]"
  - "[[bulgaria]]"
  - "[[canada]]"
  - "[[denmark]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[lithuania]]"
  - "[[netherlands]]"
  - "[[portugal]]"
  - "[[romania]]"
  - "[[switzerland]]"
  - "[[ukraine]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[australia-afp]]"
  - "[[armenia-police]]"
  - "[[belgium-federal-police]]"
  - "[[bulgaria-police]]"
  - "[[canada-rcmp]]"
  - "[[denmark-police]]"
  - "[[fbi-cyber-division]]"
  - "[[france-gendarmerie]]"
  - "[[france-junalco]]"
  - "[[france-national-police]]"
  - "[[germany-bka]]"
  - "[[germany-frankfurt-prosecutor]]"
  - "[[germany-lka]]"
  - "[[lithuania-police]]"
  - "[[netherlands-politie]]"
  - "[[portugal-police]]"
  - "[[romania-police]]"
  - "[[switzerland-fedpol]]"
  - "[[uk-nca]]"
  - "[[ukraine-police]]"
  - "[[us-dcis]]"
  - "[[us-doj]]"
  - "[[us-secret-service]]"
legal_basis:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[europol-jit]]"
  - "[[joint-investigation-team]]"
results:
  arrests: 9
  indictments: 16
  servers_seized: 400
  domains_seized: 2650
  cryptocurrency_seized: "EUR 21.2 million+ (cumulative across all phases)"
  other:
    - "20 international arrest warrants issued"
    - "18 suspects added to EU Most Wanted list"
    - "10 international arrest warrants (Phase 1)"
    - "99 crypto wallets blocked (Phase 1)"
    - "16 Russian nationals indicted for DanaBot (Phase 2)"
    - "300,000+ computers infected by DanaBot alone"
    - "Smokeloader customer database seized and exploited for follow-up arrests"
source_count: 9
sources:
  - "[[2024-05-30-europol-operation-endgame-botnet-takedown]]"
  - "[[2025-05-23-europol-operation-endgame-phase2]]"
  - "[[europol-operation-endgame-phase-2-ransomware-kill-chain-disruption]]"
  - "[[the-hacker-news-operation-endgame-phase-2-ransomware-kill-chain-disrup]]"
related_cases:
  - "[[us-v-gallyamov-qakbot]]"
  - "[[us-v-stepanov-danabot]]"
related_operations:
  - "[[operation-endgame-phase1]]"
  - "[[operation-endgame-phase2]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Targeting upstream dropper/loader infrastructure disrupts the entire ransomware supply chain more effectively than pursuing individual ransomware operators"
  - "Sustained multi-phase campaigns compound pressure on criminal ecosystems over time"
  - "Seized databases (e.g., Smokeloader customer list) provide intelligence for follow-up enforcement against demand-side actors"
  - "On-site command posts at Europol HQ enable real-time coordination across jurisdictions and time zones"
  - "EU Most Wanted listings and international arrest warrants create persistent legal pressure even without immediate physical arrests"
created: 2026-04-10
updated: 2026-04-10
---

## Summary

**Operation Endgame** is the **largest-ever international law enforcement operation against botnets and the ransomware-enabling malware ecosystem**. Launched in May 2024 and still ongoing as of 2026, the operation has been conducted in multiple phases coordinated by [[europol-ec3|Europol]] and [[eurojust|Eurojust]], with participation from law enforcement agencies across at least 15 countries.

The operation's strategic innovation lies in targeting **dropper and loader malware** — the initial-access infrastructure that ransomware operators depend on — rather than pursuing ransomware groups directly. By disrupting the upstream supply chain, Operation Endgame has *almost certainly* degraded the operational capacity of multiple ransomware affiliates simultaneously.

Across all phases (May 2024 through May 2025), Operation Endgame has resulted in:

- **9+ arrests** and **20+ international arrest warrants**
- **400+ servers** seized or taken down
- **2,650+ domains** seized or neutralized
- **EUR 21.2 million+** in cryptocurrency seized
- **16 indictments** (DanaBot operators) by the US DOJ
- **18 suspects** added to the EU Most Wanted list

For detailed accounts of individual phases, see [[operation-endgame-phase1|Phase 1 (May 2024)]] and [[operation-endgame-phase2|Phase 2 (May 2025)]].

## Background

### The Dropper/Loader Ecosystem

Dropper malware (also called "loaders" or "initial access tools") forms the critical first stage of the ransomware attack chain. These programs are designed to surreptitiously install additional malware onto compromised systems, bypassing security measures and providing initial access that is then sold to or used by ransomware operators.

The six malware families initially targeted — **IcedID**, **SystemBC**, **Pikabot**, **Smokeloader**, **Bumblebee**, and **Trickbot** — were connected to at least **15 ransomware groups**, including notorious operations such as BlackBasta, REvil, and Conti. The dropper ecosystem operates as a service model: operators maintain networks of infected computers and sell access to the highest bidder, typically ransomware affiliates.

### Strategic Rationale

Prior to Operation Endgame, international ransomware enforcement typically targeted individual ransomware groups or their operators. Operation Endgame represented a strategic shift toward **supply-chain disruption**: by taking down the dropper infrastructure that multiple ransomware groups depend on, law enforcement could degrade numerous criminal operations simultaneously. This approach *likely* provides a greater force-multiplier effect per unit of enforcement effort.

### Investigation Origins

The investigation was initiated and led by **France**, **Germany**, and the **Netherlands**, with coordination from [[europol-ec3|Europol]] and [[eurojust|Eurojust]]. The [[germany-bka|German Federal Criminal Police Office (BKA)]] and the [[germany-frankfurt-prosecutor|Central Office for the Fight against Cyber Crime (ZIT)]] at the Frankfurt Public Prosecutor General's Office played a central role in the investigation phase, particularly in matching digital identities from seized databases to real individuals — a forensic process that took months.

## Participating Parties

### Coordinating Bodies

| Body | Role |
|------|------|
| [[europol-ec3\|Europol EC3]] | Operational coordination; hosted command posts at HQ |
| [[eurojust\|Eurojust]] | Judicial coordination for arrest warrants and seizure orders |

### Participating Countries

**Core partners (all phases):** [[denmark]], [[france]], [[germany]], [[netherlands]], [[united-kingdom]], [[united-states]]

**Phase 1 supporting countries:** [[armenia]], [[australia]], [[bulgaria]], [[lithuania]], [[portugal]], [[romania]], [[switzerland]], [[ukraine]]

**Phase 2 additional countries:** [[canada]]

### Participating Agencies

| Country | Agency |
|---------|--------|
| International | [[europol-ec3\|Europol]], [[eurojust\|Eurojust]] |
| Australia | [[australia-afp\|AFP]] |
| Armenia | [[armenia-police\|Armenian Police]] |
| Belgium | [[belgium-federal-police\|Federal Police]] |
| Bulgaria | [[bulgaria-police\|Bulgarian Police]] |
| Canada | [[canada-rcmp\|RCMP]] |
| Denmark | [[denmark-police\|Danish Police]] |
| France | [[france-national-police\|National Police]], [[france-gendarmerie\|Gendarmerie]], [[france-junalco\|JUNALCO]] |
| Germany | [[germany-bka\|BKA]], [[germany-lka\|LKA]], [[germany-frankfurt-prosecutor\|ZIT Frankfurt]] |
| Lithuania | [[lithuania-police\|Lithuanian Police]] |
| Netherlands | [[netherlands-politie\|Politie]] |
| Portugal | [[portugal-police\|Portuguese Police]] |
| Romania | [[romania-police\|Romanian Police]] |
| Switzerland | [[switzerland-fedpol\|Fedpol]] |
| Ukraine | [[ukraine-police\|Ukrainian Police]] |
| United Kingdom | [[uk-nca\|NCA]] |
| United States | [[fbi-cyber-division\|FBI]], [[us-doj\|DOJ]], [[us-secret-service\|Secret Service]], [[us-dcis\|DCIS]] |

### Private Sector Partners

Multiple private-sector cybersecurity companies provided technical support, including threat intelligence and infrastructure identification. Microsoft participated in the Lumma Stealer disruption that ran concurrently with Phase 2, identifying 394,000 infected Windows machines between March and May 2025.

## Legal Framework

The operation involved law enforcement and judicial authorities from at least 15 countries. The legal framework *likely* relied on several instruments:

- **[[budapest-convention|Budapest Convention on Cybercrime]]** — provides the primary treaty framework for cross-border cybercrime cooperation among the participating states, all of which are parties or have cooperative arrangements
- **[[joint-investigation-team|Joint Investigation Teams (JITs)]]** — formal JITs were established through [[eurojust|Eurojust]] to enable multi-jurisdictional investigation and evidence sharing
- **European Arrest Warrants** — used for the 10 arrest warrants issued by German authorities in Phase 1 and the 20 international arrest warrants in Phase 2
- **National criminal law** — arrests in Armenia and Ukraine were executed under domestic legal authority with international coordination
- **US federal law** — the 16-count indictment against DanaBot operators was filed under US computer fraud and related statutes

> [!warning] Legal status check needed
> The specific treaty provisions invoked for cross-border server seizures (e.g., whether [[second-additional-protocol|Second Additional Protocol]] provisions on direct cooperation with service providers were used) require confirmation from official judicial sources.

## Operational Timeline

### Phase 1: Dropper Takedown (May 2024)

| Date | Event |
|------|-------|
| Pre-2024 | Multi-country investigation phase; digital forensics to identify operators |
| 2024-05-27 | Action days begin |
| 2024-05-27 to 2024-05-29 | 100+ servers taken down across 10 countries; 2,000+ domains seized; 4 arrests (1 Armenia, 3 Ukraine); 16 location searches; 99 crypto wallets blocked |
| 2024-05-30 | Public announcement by Europol; 8 German suspects added to EU Most Wanted list |

See [[operation-endgame-phase1]] for full details.

### Smokeloader Customer Follow-up (April 2025)

| Date | Event |
|------|-------|
| 2024-05 to 2025-04 | BKA and partners analyze seized Smokeloader customer database, linking online aliases to real identities |
| 2025-04-09 | Europol announces follow-up: 5 customers of the Smokeloader pay-per-install botnet (operated by actor "Superstar") detained or subjected to "knock-and-talk" interviews |
| 2025-04 | Additional server takedowns related to Smokeloader infrastructure |

This phase marked a shift from targeting **suppliers** (infrastructure operators) to targeting the **demand side** (customers who purchased botnet access for criminal purposes). Some detained suspects cooperated with law enforcement and allowed examination of their digital devices.

### Phase 2: Ransomware Kill Chain Disruption (May 2025)

| Date | Event |
|------|-------|
| 2025-05-19 | Phase 2 action days begin |
| 2025-05-19 to 2025-05-22 | 300 servers taken down; 650 domains neutralized; EUR 3.5M cryptocurrency seized |
| 2025-05-23 | Public announcement by Europol and Eurojust; DOJ unseals 16-count indictment against DanaBot operators; 20 international arrest warrants issued; 18 suspects added to EU Most Wanted |

Phase 2 expanded the target set to include **Bumblebee, Lactrodectus, Qakbot, Hijackloader, DanaBot, Trickbot, and Warmcookie**. The US DOJ charged 16 Russian nationals, including Aleksandr Stepanov (39) and Artem Kalinkin (34), both of Novosibirsk, Russia, for operating the DanaBot malware network that infected 300,000+ computers and caused an estimated USD 50 million+ in damages.

See [[operation-endgame-phase2]] for full details.

## Results and Impact

### Cumulative Results Across All Phases

| Metric | Phase 1 (May 2024) | Smokeloader Follow-up (Apr 2025) | Phase 2 (May 2025) | Cumulative |
|--------|-------------------|----------------------------------|-------------------|------------|
| Arrests/Detentions | 4 | 5 | 0 | 9 |
| Servers seized/taken down | 100+ | Additional | 300 | 400+ |
| Domains seized/neutralized | 2,000+ | — | 650 | 2,650+ |
| Cryptocurrency seized | EUR 69M blocked (suspect assets) | — | EUR 3.5M | EUR 21.2M+ (enforcement total) |
| Arrest warrants | 10 | — | 20 | 30+ |
| EU Most Wanted | 8 | — | 18 | 26 |
| Indictments | — | — | 16 (DanaBot) | 16 |
| Malware families targeted | 6 | 1 | 7 | 13 |

### Malware Families Disrupted

| Malware | Type | Phase Targeted | Connection to Ransomware |
|---------|------|----------------|--------------------------|
| IcedID | Banking trojan / loader | Phase 1 | Initial access for ransomware groups |
| SystemBC | Proxy / backdoor | Phase 1 | C2 communication for ransomware |
| Pikabot | Loader | Phase 1 | Successor to Qakbot; initial access |
| Smokeloader | Pay-per-install loader | Phase 1 + Follow-up | Distribution platform for varied payloads |
| Bumblebee | Loader | Phase 1 + Phase 2 | Initial access for Conti/BlackBasta affiliates |
| Trickbot | Banking trojan / loader | Phase 1 + Phase 2 | Initial access; linked to Conti ecosystem |
| DanaBot | Banking trojan / botnet | Phase 2 | Credential theft; ransomware deployment |
| Qakbot | Banking trojan / loader | Phase 2 | Initial access; operator indicted |
| Lactrodectus | Loader | Phase 2 | IcedID successor |
| Hijackloader | Loader | Phase 2 | Multi-stage payload delivery |
| Warmcookie | Loader | Phase 2 | Initial access via phishing |
| Rhadamanthys | Info-stealer | Phase 2 | Credential theft enabling ransomware |

### Financial Impact

One of the primary suspects identified during Phase 1 had earned at least **EUR 69 million in cryptocurrency** from renting out criminal infrastructure used to deploy ransomware. An asset freeze of EUR 69 million was obtained, and 99 crypto wallets with a total volume of over EUR 70 million were blocked at various cryptocurrency exchanges.

Across all enforcement actions, total seizures exceeded **EUR 21.2 million** (approximately USD 24 million). The US DOJ also filed a forfeiture complaint for USD 24 million in digital assets seized from the Qakbot operator Gallyamov (see [[qakbot-gallyamov-indictment]]), plus approximately USD 4 million in additional Bitcoin and USDT tokens.

### Impact on Ransomware Ecosystem

The operation *likely* had significant disruptive effects on the ransomware ecosystem, though quantifying the precise impact remains difficult:

- Multiple ransomware affiliates lost their primary initial-access channels simultaneously
- The "pay-per-install" business model was disrupted, forcing criminal actors to rebuild infrastructure
- Customer databases seized enabled law enforcement to pursue demand-side actors, creating a chilling effect on future botnet service purchases
- However, some malware families (notably DanaBot) showed signs of reconstituting infrastructure after the takedowns, indicating that sustained enforcement pressure is required

## Cooperation Mechanisms Used

### Europol Command Post

Europol hosted on-site command posts at its headquarters in The Hague during both Phase 1 and Phase 2 action weeks. During Phase 1, more than 20 officers from Denmark, France, Germany, the Netherlands, and the United States were present for real-time coordination. This enabled:

- Synchronized server takedowns across multiple time zones
- Rapid decision-making when unexpected situations arose during action days
- Real-time intelligence sharing between participating agencies

### Eurojust Judicial Coordination

[[eurojust|Eurojust]] provided judicial coordination for:

- Multi-jurisdictional arrest warrants (10 in Phase 1, 20 in Phase 2)
- Cross-border evidence preservation and transfer orders
- Coordination of seizure orders across different legal systems
- Facilitation of mutual legal assistance between participating states

### Joint Investigation Teams

Formal [[joint-investigation-team|Joint Investigation Teams (JITs)]] were established to enable multi-jurisdictional investigation. The JIT framework, facilitated by Eurojust, allowed investigators from different countries to share evidence and coordinate actions within a unified legal framework, avoiding the delays typically associated with formal [[mlat-process|MLAT requests]].

### Database Exploitation

A particularly notable mechanism was the **exploitation of seized databases** for follow-up enforcement. The Smokeloader customer database seized during Phase 1 was systematically analyzed by [[germany-bka|BKA]] investigators who spent months matching online aliases and usernames to real-world identities. This intelligence was then shared with law enforcement partners across multiple countries, enabling the April 2025 demand-side enforcement wave.

### EU Most Wanted List

The addition of suspects to Europol's **EU Most Wanted** list (8 in Phase 1, 18 in Phase 2) served as both a public awareness mechanism and a tool for international fugitive tracking, increasing the likelihood of identification and arrest when suspects travel.

## Challenges and Friction Points

### Jurisdictional Complexity

The operation required coordination across at least 15 countries with different legal systems, procedural requirements, and evidentiary standards. Synchronized action days required meticulous pre-planning to ensure that all participants could execute their assigned tasks within their respective legal frameworks.

### Russian-Based Suspects

Many of the identified suspects, including the 16 DanaBot operators indicted by the US DOJ, are based in Russia. Given the current geopolitical situation and the absence of extradition cooperation with Russia, these suspects remain effectively beyond the reach of law enforcement. The international arrest warrants and EU Most Wanted listings create a legal framework for arrest if suspects travel to cooperating jurisdictions, but direct enforcement in Russia is *highly unlikely*.

### Infrastructure Reconstitution

Some targeted malware families showed signs of reconstituting operations after the takedowns. DanaBot, in particular, resurfaced with new infrastructure, suggesting that infrastructure takedowns alone — without arresting the operators — provide only temporary disruption. This underscores the need for sustained, multi-phase campaigns rather than one-off actions.

### Demand-Side Enforcement Scale

While the Smokeloader customer follow-up (5 detentions) demonstrated the feasibility of demand-side enforcement, the scale of the botnet customer base *almost certainly* far exceeds law enforcement capacity to pursue every user. Prioritization and deterrence effects are key considerations.

## Lessons Learned

1. **Supply-chain disruption as force multiplier:** Targeting dropper/loader infrastructure disrupts multiple ransomware operations simultaneously. This upstream approach *almost certainly* provides greater impact per unit of enforcement effort than targeting individual ransomware groups.

2. **Multi-phase sustained campaigns:** The progression from Phase 1 (May 2024) through the Smokeloader follow-up (April 2025) to Phase 2 (May 2025) demonstrates that sustained campaigns compound pressure on criminal ecosystems. Criminal actors face continuous uncertainty about which infrastructure will be targeted next.

3. **Demand-side enforcement:** The Smokeloader customer arrests marked a strategic expansion from supply-side (infrastructure operators) to demand-side (service purchasers) enforcement. This "whole ecosystem" approach sends a deterrent message that purchasing botnet services carries real arrest risk.

4. **Database intelligence exploitation:** Seized infrastructure databases are not just evidence for ongoing cases — they are intelligence assets that enable entirely new lines of investigation. The months-long BKA effort to de-anonymize Smokeloader customers illustrates the long-term investigative value of infrastructure seizures.

5. **Real-time coordination infrastructure:** Europol command posts with 20+ officers from multiple countries enable the kind of synchronized, multi-timezone action that infrastructure takedowns require. This institutional capability is *almost certainly* essential for operations at this scale.

## Follow-Up Actions

- **Ongoing investigation:** Europol has stated explicitly that Operation Endgame is not concluded and further enforcement phases are planned.
- **Fugitive pursuit:** The 30+ international arrest warrants and 26 EU Most Wanted listings create a persistent legal framework for future arrests when suspects travel to cooperating jurisdictions.
- **DanaBot reconstitution monitoring:** The resurfacing of DanaBot with new infrastructure after the Phase 2 takedown *likely* requires continued monitoring and potential further enforcement action.
- **Related proceedings:** The [[qakbot-gallyamov-indictment|Qakbot/Gallyamov indictment]] and associated asset forfeiture proceedings are ongoing in US courts.

## Korean Involvement (한국의 참여)

No direct Korean involvement in any phase of Operation Endgame has been identified as of April 2026. South Korea was not among the participating countries in either Phase 1 or Phase 2.

However, Operation Endgame is relevant to Korean cybersecurity interests in several respects:

- **Ransomware impact:** The dropper malware families targeted by Operation Endgame have been used globally, and South Korean organizations have been victims of ransomware deployed through these initial-access channels
- **Cooperation model:** The operation provides a model for the kind of multi-lateral, Europol-coordinated enforcement action that South Korea could participate in through its growing engagement with European law enforcement (사이버범죄 국제공조 모델로서의 참고 가치)
- **Budapest Convention participation:** As South Korea continues to engage with the [[budapest-convention|Budapest Convention]] framework, participation in future phases of operations like Endgame could strengthen Korea's role in international cybercrime enforcement

## Contradictions & Open Questions

1. **Arrest count discrepancy:** Some sources report 4 arrests in Phase 1 while the German BMI reports 4 "temporary detentions" — the distinction between formal arrest and temporary detention may reflect different legal frameworks across jurisdictions.

2. **Financial figures:** The relationship between the EUR 69 million in suspect cryptocurrency holdings (Phase 1), the EUR 70 million in blocked crypto wallets, and the EUR 21.2 million cumulative enforcement seizure total is not fully clear. The EUR 69M/70M figures may represent identified assets subject to freeze orders, while EUR 21.2M represents actually seized/forfeited funds.

3. **DanaBot source verification:** The 16 DanaBot indictments and 300,000 infection figure originate primarily from news reporting (Tier 3 sources). Official DOJ indictment text would provide definitive confirmation.

4. **Reconstitution rates:** How quickly and effectively have the targeted malware families reconstituted after each phase? DanaBot has reportedly resurfaced, but systematic assessment of reconstitution across all 13 targeted families is lacking.

5. **Measurable ransomware impact:** What was the quantifiable effect on global ransomware deployment rates following each phase? No systematic assessment has been publicly released.

6. **Phase 1 server locations:** Servers were seized in Bulgaria, Canada, Germany, Lithuania, the Netherlands, Romania, Switzerland, the United Kingdom, United States, and Ukraine — but the distribution across countries has not been specified in detail.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Largest ever operation against botnets hits dropper malware ecosystem | Europol | 2024-05-30 | [link](https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem) |
| [2] | Operation Endgame: Coordinated Worldwide Law Enforcement Action Against Network of Cybercriminals | FBI | 2024-05-29 | [link](https://www.fbi.gov/news/press-releases/operation-endgame-coordinated-worldwide-law-enforcement-action-against-network-of-cybercriminals) |
| [3] | Worldwide investigation against cyber crime crowned by success | German BMI | 2024-05-30 | [link](https://www.bmi.bund.de/SharedDocs/kurzmeldungen/EN/2024/05/endgame.html) |
| [4] | Operation Endgame follow-up leads to five detentions and interrogations as well as server takedowns | Europol | 2025-04-09 | [link](https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-follow-leads-to-five-detentions-and-interrogations-well-server-takedowns) |
| [5] | Operation ENDGAME strikes again: the ransomware kill chain broken at its source | Europol | 2025-05-23 | [link](https://www.europol.europa.eu/media-press/newsroom/news/operation-endgame-strikes-again-ransomware-kill-chain-broken-its-source) |
| [6] | Operation Endgame — official page | Europol | ongoing | [link](https://www.europol.europa.eu/operations-services-and-innovation/operations/operation-endgame) |
| [7] | 'Operation Endgame' Hits Malware Delivery Platforms | KrebsOnSecurity | 2024-05-30 | [link](https://krebsonsecurity.com/2024/05/operation-endgame-hits-malware-delivery-platforms/) |
| [8] | U.S. Dismantles DanaBot Malware Network, Charges 16 | The Hacker News | 2025-05-23 | [link](https://thehackernews.com/2025/05/us-dismantles-danabot-malware-network.html) |
| [9] | DanaBot botnet disrupted, QakBot leader indicted | Help Net Security | 2025-05-23 | [link](https://www.helpnetsecurity.com/2025/05/23/operation-endgame-danabot-botnet-disrupted-qakbot-leader-indicted/) |
