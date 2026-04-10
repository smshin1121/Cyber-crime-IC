---
type: operation
title: "Operation LadyBird -- Emotet Botnet Takedown"
aliases:
  - "Operation LadyBird"
  - "Emotet Disruption"
case_id: "CYB-2021-003"
period: 2
operation_type: "takedown"
status: "completed"
enforcement_type:
  - takedown
  - arrest
  - seizure
outcome: "partial"
timeframe:
  announced: "2021-01-27"
  start: "2019"
  end: "2021-04-25"
  ongoing: false
crime_type: "[[ransomware-ic]]"
target_entity: "Emotet botnet infrastructure and operators"
lead_agency: "[[netherlands-politie]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[netherlands]]"
  - "[[germany]]"
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[france]]"
  - "[[ukraine]]"
  - "[[canada]]"
  - "[[lithuania]]"
participating_agencies:
  - "[[netherlands-politie]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[joint-investigation-team]]"
  - "[[europol-jit]]"
  - "[[24-7-network]]"
results:
  arrests: 2
  indictments: 0
  servers_seized: 700
  domains_seized: 2000
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 1000000
  other:
    - "4.3 million compromised email addresses recovered by Dutch police"
    - "Law enforcement deployed uninstall module to infected machines (activated 2021-04-25)"
    - "Emotet botnet resurfaced in November 2021 via TrickBot infrastructure"
edges:
  - source_actor: "Netherlands NHTCU"
    target_actor: "Germany BKA"
    cooperation_type: "joint_investigation"
    legal_basis: "Budapest_Convention"
    direction: "undirected"
  - source_actor: "Netherlands NHTCU"
    target_actor: "Ukraine Cyberpolice"
    cooperation_type: "evidence_transfer"
    legal_basis: "MLAT"
    direction: "directed"
  - source_actor: "Europol EC3"
    target_actor: "FBI"
    cooperation_type: "info_sharing"
    legal_basis: "bilateral_MOU"
    direction: "undirected"
credibility_index: 3.5
source_tier: 1
missing_fields:
  - "cryptocurrency_seized"
  - "full list of national agencies beyond lead participants"
related_cases: []
related_operations:
  - "[[operation-endgame-phase1]]"
  - "[[operation-avalanche]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Botnet infrastructure can be repurposed to deliver uninstall payloads to victims"
  - "Multi-year investigation timeline required to map globally distributed C2 infrastructure"
  - "Despite successful takedown, Emotet resurfaced 10 months later -- infrastructure disruption alone is insufficient without arrests of key operators"
source_count: 5
sources: []
created: 2026-04-10
updated: 2026-04-10
---

## Summary

Operation LadyBird was a multinational law enforcement operation that disrupted the **Emotet botnet** -- described by [[europol-ec3|Europol]] as "the world's most dangerous malware" -- on **27 January 2021**. The operation was coordinated by [[europol-ec3|Europol EC3]] and [[eurojust|Eurojust]], with the [[netherlands-politie|Dutch National Police (NHTCU)]] and Germany's Bundeskriminalamt (BKA) serving as the primary operational leads.

Law enforcement agencies from **eight countries** -- the [[netherlands|Netherlands]], [[germany|Germany]], the [[united-states|United States]], the [[united-kingdom|United Kingdom]], [[france|France]], [[ukraine|Ukraine]], [[canada|Canada]], and [[lithuania|Lithuania]] -- simultaneously seized control of approximately **700 command-and-control (C2) servers** and over **2,000 domains**, redirecting infected machines to law enforcement-controlled infrastructure.

The operation is *almost certainly* one of the most technically innovative botnet takedowns in history: rather than simply shutting down infrastructure, law enforcement used Emotet's own update mechanism to deploy an uninstall module to infected machines worldwide, which activated on **25 April 2021** to remove the malware. However, the outcome is assessed as **partial** because Emotet resurfaced approximately 10 months later in November 2021, rebuilt using TrickBot infrastructure.

## Background

### Emotet's Evolution

Emotet first appeared in **2014** as a banking trojan targeting financial institutions. By 2017, it had evolved into a sophisticated **malware-as-a-service (MaaS) platform** -- a "loader" that provided initial access to compromised systems, which was then sold to other cybercriminal groups. Key characteristics:

- **Modular architecture:** Could deploy additional payloads including banking trojans (TrickBot), ransomware (Ryuk, Conti), and information stealers
- **Spam infrastructure:** Operated one of the world's largest spam botnets, sending millions of phishing emails daily with malicious attachments
- **Polymorphic code:** Changed its code with each download to evade antivirus detection
- **Resilient C2 network:** Hundreds of servers across multiple countries with redundant communication channels

### Scale of the Threat

By 2020, Emotet had infected an estimated **1.6 million computers worldwide** (between April 2020 and January 2021 alone, per DOJ). It served as the entry vector for some of the most damaging ransomware attacks globally, with total damages estimated in the hundreds of millions of dollars. Europol described it as a "door opener" for cybercriminals -- initial Emotet infections were followed by deployment of ransomware or banking trojans by affiliated criminal groups.

### Investigation Origins

The investigation into Emotet's infrastructure began in approximately **2019**, with Dutch and German authorities leading the effort to map the botnet's globally distributed C2 architecture. The investigation was conducted through a [[joint-investigation-team|Joint Investigation Team (JIT)]] facilitated by [[eurojust|Eurojust]].

## Participating Parties

### Lead Agencies

| Country | Agency | Role |
|---------|--------|------|
| [[netherlands]] | [[netherlands-politie]] (NHTCU) | Infrastructure takeover; deployed update module; recovered stolen credentials |
| [[germany]] | BKA (Bundeskriminalamt) | Co-lead; seized 17 C2 servers in Germany; coordinated with prosecutors |

### Coordinating Bodies

| Organization | Role |
|---|---|
| [[europol-ec3]] | Operational coordination, cross-matching intelligence, coordination center |
| [[eurojust]] | Judicial coordination, JIT facilitation |

### Supporting Agencies

| Country | Agency | Role |
|---------|--------|------|
| [[united-states]] | [[fbi-cyber-division]] / US DOJ MDNC | Legal assistance; infrastructure seizure on US soil |
| [[united-kingdom]] | National Crime Agency (NCA) | C2 server seizure; reported ~700 servers taken offline |
| [[france]] | Police Nationale | Infrastructure seizure in French jurisdiction |
| [[ukraine]] | Cyberpolice Department | Property raids in Kharkiv; arrested 2 suspects |
| [[canada]] | RCMP | Infrastructure seizure support |
| [[lithuania]] | Lithuanian Criminal Police Bureau | Infrastructure seizure support |

## Legal Framework

The operation relied on multiple legal cooperation instruments:

- **[[budapest-convention|Budapest Convention]]** (Art. 29-35): Provided the primary legal framework for cross-border evidence preservation and production orders among party states
- **[[mutual-legal-assistance|Mutual Legal Assistance Treaties]]**: Bilateral MLATs enabled evidence sharing and infrastructure seizure across jurisdictions
- **[[joint-investigation-team|Joint Investigation Team]]**: A JIT was established through [[eurojust|Eurojust]] to enable real-time evidence sharing between Netherlands, Germany, and other EU participants
- **EU European Investigation Order**: Used for intra-EU judicial cooperation

The Ukrainian arrests were conducted under Ukrainian domestic criminal procedure, with evidence shared via [[mutual-legal-assistance|MLAT]] channels.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2019 | Investigation begins; Dutch and German authorities start mapping Emotet C2 infrastructure |
| 2020 | JIT established via [[eurojust]]; multi-country infrastructure identification accelerates |
| 2021-01-26 | Coordinated action day preparations finalized across 8 countries |
| **2021-01-27** | **Action day**: Simultaneous seizure of ~700 C2 servers and 2,000+ domains across all participating countries |
| 2021-01-27 | [[netherlands-politie]] deploys update module via Emotet's own infrastructure; infected machines redirected to law enforcement-controlled servers |
| 2021-01-27 | Ukrainian Cyberpolice raids properties in Kharkiv; 2 suspects arrested |
| 2021-01-27 | [[europol-ec3]] and [[eurojust]] announce operation publicly |
| 2021-01-27 | DOJ announces disruption of Emotet botnet |
| 2021-02-17 | Dutch police announce recovery of 4.3 million compromised email addresses; launch online tool for victims to check exposure |
| **2021-04-25** | Law enforcement-deployed uninstall module activates; Emotet self-deletes from infected machines worldwide |
| 2021-11 | Emotet botnet resurfaces, rebuilt using TrickBot infrastructure by the Conti ransomware group |

## Results and Impact

### Immediate Results

| Metric | Value | Source |
|--------|-------|--------|
| C2 servers seized/disabled | ~700 | NCA / Europol |
| Domains seized | 2,000+ | Europol |
| German C2 servers seized | 17 | BKA |
| Suspects arrested | 2 (Ukraine) | Ukrainian Cyberpolice |
| Infected machines identified | 1.6 million (Apr 2020 - Jan 2021) | US DOJ |
| Compromised credentials recovered | 4.3 million email addresses + passwords | Dutch National Police |
| Victim notification | 1 million+ systems cleaned via uninstall module | Europol |

### Strategic Impact

1. **Temporary disruption of MaaS ecosystem:** Emotet's takedown deprived ransomware operators (Ryuk, Conti) of their primary initial access vector for approximately 10 months
2. **Pioneering victim remediation:** The deployment of a law enforcement-controlled update to clean infected machines was *almost certainly* unprecedented in scale and set a new operational template
3. **Intelligence harvest:** The seized infrastructure and credentials database provided extensive intelligence on the broader cybercrime ecosystem
4. **Credential notification:** Dutch police created an online tool allowing potential victims to check if their email credentials were compromised

### Limitations

The operation's outcome is assessed as **partial** because:
- Only **2 arrests** were made (in Ukraine), and no senior Emotet developers or operators were publicly charged
- The botnet **resurfaced in November 2021**, rebuilt through TrickBot infrastructure by actors associated with the Conti ransomware group
- The resurgence demonstrates that infrastructure takedowns without corresponding arrests of key operators provide only temporary disruption

## Cooperation Mechanisms Used

| Mechanism | Application |
|-----------|-------------|
| [[joint-investigation-team]] | JIT between Netherlands, Germany, and other EU states via [[eurojust]] |
| [[europol-jit]] | Europol hosted operational coordination center; provided cross-matching analysis |
| [[mutual-legal-assistance]] | MLATs used for cross-border evidence sharing and infrastructure seizure |
| [[24-7-network]] | *Likely* used for urgent preservation requests during infrastructure mapping phase |
| DNS Sinkholing | Law enforcement redirected C2 traffic to controlled servers |
| Victim Notification | Dutch police published compromised credential checker; deployed uninstall module |

### Technical Innovation: The Uninstall Module

The most technically distinctive aspect of Operation LadyBird was the deployment of a law enforcement-created DLL ("EmotetLoader.dll") via Emotet's own update mechanism. This module:

1. Was pushed to infected machines after C2 infrastructure was seized
2. Contained a time-delayed activation set for **25 April 2021** (giving a ~3 month window for ISPs and CERTs to notify affected organizations)
3. On activation, it deleted all Emotet-related services, removed registry keys, terminated running processes, and self-deleted
4. This approach was *almost certainly* the first operational use of "police malware" deployed through a botnet's own infrastructure to protect victims at scale

## Challenges and Friction Points

- **Jurisdictional complexity:** Emotet's C2 infrastructure spanned dozens of countries; coordinating simultaneous action across 8 jurisdictions required extensive preparation
- **Victim notification at scale:** With 1.6 million infected machines, notifying victims and ensuring cleanup was a logistical challenge
- **Legal authority for "police malware":** The deployment of an uninstall module to victim machines raised legal questions about law enforcement's authority to modify third-party systems, even for remediation purposes
- **Resilience of criminal networks:** Despite the takedown, the underlying criminal operators retained the knowledge and relationships to rebuild the botnet within 10 months

## Lessons Learned

1. **Infrastructure seizure is necessary but insufficient:** Without arresting key developers and operators, criminal networks can rebuild. The Emotet resurgence in November 2021 demonstrated that botnet takedowns require complementary arrest operations
2. **JITs enable innovative operations:** The JIT structure facilitated the unprecedented deployment of a law enforcement-controlled update module across jurisdictions
3. **Victim remediation at scale is feasible:** The time-delayed uninstall approach proved that law enforcement can remediate victim machines globally, but raises governance questions about authority and liability
4. **Public-private cooperation essential:** ISPs, CERTs, and security vendors played a critical role in victim notification during the 3-month window before the uninstall module activated
5. **Template for future operations:** Operation LadyBird's approach directly influenced subsequent botnet operations including [[operation-endgame-phase1|Operation Endgame]] (2024)

## Korean Involvement (한국의 참여)

South Korea was **not among the eight participating countries** in Operation LadyBird. However, the operation is relevant to Korean cybersecurity interests in several ways:

- **Emotet infections in Korea:** South Korea was among the countries where Emotet C2 infrastructure was identified, though it was not a primary hosting location
- **Downstream ransomware impact:** Emotet served as the primary delivery mechanism for Ryuk and Conti ransomware, which *likely* affected Korean organizations
- **TrickBot connection:** An alleged developer of TrickBot -- the malware used to rebuild Emotet after the takedown -- was arrested in South Korea in 2022, demonstrating Korea's role in the broader cybercrime enforcement ecosystem
- **Operational template:** The cooperation model demonstrated in Operation LadyBird has been applied in subsequent operations where Korea participated, such as the [[phobos-8base-crackdown|Phobos/8Base crackdown]] (2025) coordinated by [[europol-ec3|Europol]]

> [!note]
> Korea's participation in [[europol-ec3|Europol's]] J-CAT (Joint Cybercrime Action Taskforce) provides a channel for intelligence sharing on botnet operations, though Korea was not a J-CAT participant at the time of Operation LadyBird.

## Contradictions & Open Questions

1. **Arrest count discrepancy:** Europol and DOJ press releases focus on "disruption" without specifying a precise arrest count. Ukrainian Cyberpolice reported 2 arrests in Kharkiv, but some media sources reported higher numbers. The 2 arrests figure is *likely* correct based on primary source consistency.

2. **Server count variation:** Europol reported "hundreds of servers," the UK NCA cited approximately 700, and the BKA reported 17 in Germany specifically. These figures are *likely* compatible (700 total, 17 in Germany), but the exact count may vary depending on whether backup/relay nodes are included.

3. **Emotet's resurgence and operator identity:** The same operators behind the original Emotet *likely* rebuilt the botnet using TrickBot/Conti infrastructure. If so, the 2 Ukrainian arrests did not capture the core development team. The relationship between Emotet operators and the Conti group remains an open question.

4. **Legal authority for victim remediation:** The legal basis for deploying an uninstall module to victim machines varies by jurisdiction. No public legal challenge has been reported, but the practice raises unresolved questions about proportionality and authority.

> [!warning] Outcome qualification
> Despite being widely reported as a success, Operation LadyBird achieved only **temporary disruption**. Emotet's resurgence in November 2021 demonstrates the limitations of infrastructure-focused takedowns without corresponding arrests of core operators.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| [1] | World's most dangerous malware EMOTET disrupted through global action | Europol | 2021-01-27 | [link](https://www.europol.europa.eu/media-press/newsroom/news/world%E2%80%99s-most-dangerous-malware-emotet-disrupted-through-global-action) |
| [2] | Emotet Botnet Disrupted in International Cyber Operation | US DOJ | 2021-01-27 | [link](https://www.justice.gov/archives/opa/pr/emotet-botnet-disrupted-international-cyber-operation) |
| [3] | Internationale politieoperatie LadyBird: wereldwijd botnet Emotet ontmanteld | Dutch National Police | 2021-01-27 | [link](https://www.politie.nl/nieuws/2021/januari/27/11-internationale-politieoperatie-ladybird-botnet-emotet-wereldwijd-ontmanteld.html) |
| [4] | Major operation to take down dangerous malware systems | Eurojust | 2021-01-27 | [link](https://www.eurojust.europa.eu/news/major-operation-take-down-dangerous-malware-systems) |
| [5] | Emotet Botnet Disrupted in International Cyber Operation | US DOJ MDNC | 2021-01-27 | [link](https://www.justice.gov/usao-mdnc/pr/emotet-botnet-disrupted-international-cyber-operation) |
