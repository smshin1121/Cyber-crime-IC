---
type: operation
title: "IP Proxy Service for Cybercriminals Takedown (March 2026)"
title_ko: "사이버범죄용 IP 프록시 서비스 단속 (2026년 3월)"
aliases:
  - "Eurojust IP Proxy Takedown 2026"
  - "FR-AT-NL-US Proxy Service Takedown"
case_id: CYB-2026-001
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - seizure
  - takedown
outcome: partial
timeframe:
  announced: 2026-03-12
  start: ""
  end: 2026-03-12
  ongoing: false
crime_type: "[[hacking-ic]]"
target_entity: "Unnamed website offering IP proxy services to cybercriminals; same operators allegedly hosted a payment platform for the proxy service"
lead_agency: "[[eurojust]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[france]]"
  - "[[austria]]"
  - "[[netherlands]]"
  - "[[united-states]]"
participating_agencies:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
legal_basis:
  - "[[budapest-convention]]"
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[europol-jit|Joint Investigation Team]]"
  - "[[mutual-legal-assistance|MLAT Process]]"
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "IP proxy service dismantled"
    - "102 victim countries identified per Eurojust release"
    - "Associated payment platform also targeted"
edges:
  - source_actor: France
    target_actor: Austria
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: France
    target_actor: Netherlands
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: France
    target_actor: "United States"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: Eurojust
    target_actor: France
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: directed
  - source_actor: Europol
    target_actor: France
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: directed
credibility_index: 3.5
source_tier: 1
missing_fields:
  - operation_name
  - service_name
  - arrests
  - indictments
  - servers_seized_count
  - 4_unnamed_participating_countries
related_operations:
  - "[[doublevpn-takedown]]"
challenges_encountered:
  - "[[data-sovereignty]]"
  - "[[jurisdictional-conflicts]]"
lessons_learned:
  - "Cross-Atlantic FR-AT-NL-US judicial cooperation under Eurojust coordination can dismantle cybercrime anonymisation infrastructure even where the underlying victim base spans 102 countries"
source_count: 5
sources:
  - "[[2026-03-12-eurojust-proxy-service-takedown]]"
  - "[[2025-05-09_politie-nl_anyproxy-amsterdam-fbi]]"
  - "[[2026-03-13_cyberscoop-com_socksescort-proxy-network-botnet-takedown]]"
  - "[[2026-03-13_cybernews-com_major-residential-proxy-service-socksescort-down]]"
  - "[[2026-03-13_techradar-com_major-socksescort-proxy-network-powered-by-linux-malware-taken-down-by-fbi-and-other-police-forces]]"
created: 2026-04-14
updated: "2026-04-26"
operation_role: umbrella
parent_operation: ""
summary: "On **12 March 2026**, [[eurojust|Eurojust]] announced the takedown of an unnamed website allegedly offering **IP proxy services for cybercriminals in 102 countries** of victims. The operation was conducted by authorities from **eight countries** — only four of which are publicly named: [[france|France]], [[austria|Austria]], the [[netherlands|Netherlands]], and the [[united-states|United States]] — coordinated by [[eurojust|Eurojust]] and [[europol-ec3|Europol]]. The operators of the proxy service are also suspected of running an associated **payment platform** for the service."
jurisdictions:
  - "[[france]]"
  - "[[austria]]"
  - "[[netherlands]]"
  - "[[united-states]]"
organizations:
  - "[[eurojust]]"
  - "[[europol-ec3]]"
crime_types:
  - "[[hacking-ic]]"
  - "[[malware-ic]]"
---
## Summary

On **12 March 2026**, [[eurojust|Eurojust]] announced the takedown of an unnamed website allegedly offering **IP proxy services for cybercriminals in 102 countries** of victims. The operation was conducted by authorities from **eight countries** — only four of which are publicly named: [[france|France]], [[austria|Austria]], the [[netherlands|Netherlands]], and the [[united-states|United States]] — coordinated by [[eurojust|Eurojust]] and [[europol-ec3|Europol]]. The operators of the proxy service are also suspected of running an associated **payment platform** for the service.

The Eurojust release does not name the proxy service, the operation, the four unnamed participating countries, the arrests count, or the number of servers seized. It is *almost certainly* one of a continuing series of EU/US cybercrime anonymisation-infrastructure takedowns and *likely* relates to a malware-distributed proxy botnet (residential proxy / SOCKS proxy networks built from compromised devices), based on the framing "after identifying numerous victims of the malware used to gain access to IP addresses for the proxy service."

> [!note] Unnamed operation
> The proxy service and the operation itself are unnamed in the Eurojust press release. The wiki slug `proxy-service-takedown-2026-03` is descriptive only. If a name surfaces in follow-up reporting, this page should be renamed.

> [!note] 8 countries total, 4 named
> The Eurojust release states that authorities from **eight countries** participated. Only **four are named** (France, Austria, Netherlands, US). The identities of the remaining four are not disclosed in the source.

## Background

IP proxy services for cybercriminals — also called "residential proxy services," "SOCKS proxy networks," or "anonymisation services" — provide criminals with the ability to route their malicious traffic through legitimate-looking IP addresses, defeating geographic and reputation-based defences. The IP addresses are typically obtained by:

1. **Infecting victim devices** with malware that turns them into proxy nodes (residential proxy botnets such as 911 S5, RSOCKS)
2. **Compromising routers, IoT devices, or VPSs** without owner consent
3. **In rare cases, recruiting voluntary node operators**

The Eurojust release explicitly references "the malware used to gain access to IP addresses for the proxy service," which *strongly implies* a residential proxy botnet model — comparable to prior takedowns such as [[911-s5-botnet-takedown|911 S5]] (2024) and RSOCKS (2022).

## Participating Parties

| Country | Role |
|---------|------|
| [[france]] | Co-lead enforcement (likely investigative anchor given Eurojust framing) |
| [[austria]] | Co-lead enforcement |
| [[netherlands]] | Co-lead enforcement |
| [[united-states]] | Co-lead enforcement (transatlantic anchor) |
| (4 unnamed countries) | Participating; identities not disclosed in the Eurojust release |

| Coordinating Body | Role |
|-------------------|------|
| [[eurojust]] | Judicial coordination across the 4 named EU and the US |
| [[europol-ec3]] | Operational and analytical support |

> [!note] Source gap on agency identities
> The Eurojust release does not specify which national agencies led each country's component (e.g., for the US, this could be the [[fbi-cyber-division|FBI]], [[us-doj|DOJ]], or another body — none is confirmed).

## Legal Framework

- **[[budapest-convention|Budapest Convention]]**: All four named participants (France, Austria, Netherlands, US) are parties, providing the multilateral framework for cross-border preservation, search and seizure, and MLA.
- **EU Joint Investigation Team framework**: For the EU members (FR, AT, NL), a [[europol-jit|JIT]] is *highly likely* though not stated.
- **US-EU Mutual Legal Assistance Agreement**: Provides the formal channel between the US and the three named EU members.
- **Eurojust coordination**: Cross-jurisdictional judicial coordination, including with the US under the Eurojust-US cooperation agreement.

## Operational Timeline

| Date | Event |
|------|-------|
| (Pre-2026) | Investigation initiated after identification of malware victims used to build the proxy service |
| (Pre-2026) | Coordinated FR-AT-NL-US (+ 4 unnamed) action against the service |
| 2026-03-12 | Eurojust announces the takedown via press release |

## Results and Impact

| Metric | Value |
|--------|-------|
| Servers seized | not stated (count unknown) |
| Arrests | not stated |
| Indictments | not stated |
| Victim countries | **102** |
| Associated payment platform | also targeted |

The disclosed metric — **102 countries of victims** — is consistent with a global residential proxy botnet built from compromised consumer devices.

## Cooperation Mechanisms Used

1. **Multi-jurisdictional FR-AT-NL-US judicial cooperation** through Eurojust coordination
2. **Europol operational/analytical support** — *likely* including malware analysis and victim identification
3. **MLAT and (likely) JIT instruments** for cross-border server access and parallel arrests

## Challenges and Friction Points

- **Cross-Atlantic coordination**: 4 EU members + US requires bridging both EU MLA instruments and the US-EU MLA Agreement.
- **Hidden participants**: Four of the eight participating countries are not named — *likely* due to ongoing investigations or sensitivity of those jurisdictions' roles.
- **Information opacity**: The release omits the service name, server count, arrests, and the underlying malware family.

## Lessons Learned

- Cross-Atlantic FR-AT-NL-US cooperation under Eurojust can dismantle global cybercrime anonymisation infrastructure with victim bases spanning 102 countries.
- The pairing of an anonymisation service with a payment platform run by the same operators is *almost certainly* a recurring structural pattern in cybercrime-as-a-service ecosystems.

## Korean Involvement (한국의 참여)

No [[south-korea|South Korean]] participation is documented in this operation. Korean victims are *likely* among the 102 identified victim countries, given the global reach of residential proxy botnets and Korea's high broadband penetration. The [[knpa-cyber-bureau|Korean National Police Agency]] cybercrime units would *likely* be informed via Europol or INTERPOL channels for any Korea-resident infected devices.

## Contradictions & Open Questions

- **What is the name of the proxy service?** Not stated in the Eurojust release.
- **Which malware was used to build the proxy network?** Not stated — *likely* a residential proxy botnet but unconfirmed.
- **Which four countries are unnamed in the release?** Not disclosed.
- **How many servers were seized and how many arrests were made?** Not stated.
- **What is the relationship to prior residential proxy botnet takedowns** ([[911-s5-botnet-takedown|911 S5]], RSOCKS)? Not addressed in the source.
- **Is the operation linked to a named campaign** (e.g., Operation Endgame, Operation Power Off)? No linkage is stated.


## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Servers used for cybercrime around the world taken down | Eurojust | 2026-03-12 | https://www.eurojust.europa.eu/news/servers-used-cybercrime-around-world-taken-down |
| [2] | Internationale cybercrime aangepakt: Politie Amsterdam en FBI ontmantelen proxydienst Anyproxy | Politie | 2025-05-09 | https://www.politie.nl/nieuws/2025/mei/9/internationale-cybercrime-aangepakt-politie-amsterdam-en-fbi-ontmantelen-proxydienst-anyproxy.html |
| [3] | Authorities takedown global proxy network SocksEscort | CyberScoop | 2026-03-13 | https://cyberscoop.com/socksescort-proxy-network-botnet-takedown/ |
| [4] | Authorities shut down cybercrime service that sold access to 369,000 home internet connections | Cybernews | 2026-03-13 | https://cybernews.com/security/major-residential-proxy-service-socksescort-down/ |
| [5] | Major SocksEscort proxy network powered by Linux malware taken down by FBI and other police forces | TechRadar | 2026-03-13 | https://www.techradar.com/pro/security/major-socksescort-proxy-network-powered-by-linux-malware-taken-down-by-fbi-and-other-police-forces |
