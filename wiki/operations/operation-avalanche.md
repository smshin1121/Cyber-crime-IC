---
type: operation
title: Operation Avalanche
title_ko: Operation Avalanche (Avalanche 네트워크 해체)
aliases:
  - Avalanche Takedown
case_id: CYB-2016-001
period: 1
operation_type: takedown
operation_role: umbrella
parent_operation: ""
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
outcome: success
timeframe:
  announced: 2016-11-30
  start: 2012
  end: 2016-11-30
  ongoing: false
crime_type: "[[malware-ic]]"
crime_types:
  - "[[malware-ic]]"
target_entity: Avalanche Network
lead_agency: "[[german-prosecution]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[armenia]]"
  - "[[australia]]"
  - "[[austria]]"
  - "[[azerbaijan]]"
  - "[[belgium]]"
  - "[[belize]]"
  - "[[bulgaria]]"
  - "[[canada]]"
  - "[[colombia]]"
  - "[[finland]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[hungary]]"
  - "[[india]]"
  - "[[italy]]"
  - "[[lithuania]]"
  - "[[luxembourg]]"
  - "[[moldova]]"
  - "[[montenegro]]"
  - "[[netherlands]]"
  - "[[norway]]"
  - "[[poland]]"
  - "[[romania]]"
  - "[[singapore]]"
  - "[[sweden]]"
  - "[[taiwan]]"
  - "[[ukraine]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[interpol]]"
  - "[[fbi]]"
  - "[[usdoj]]"
  - "[[shadowserver]]"
  - "[[icann]]"
legal_basis: []
mechanisms_used:
  - "[[sinkholing]]"
  - "[[informal-cooperation]]"
related_cases: []
related_operations: []
results:
  arrests: 5
  servers_seized: 221
  domains_seized: 800000
  indictments: 0
  decryption_keys_recovered: 0
  victims_notified: 0
  cryptocurrency_seized: ""
  other:
    - "Millions of infected systems and victims in 180+ countries"
    - "Global phishing, spam and malware-distribution infrastructure disrupted"
edges:
  - source_actor: Germany
    target_actor: Europol
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: FBI
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Europol
    target_actor: INTERPOL
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 4.0
source_tier: 2
source_count: 7
sources:
  - "[[2016-11-30_europol-europa-eu_avalanche-network-dismantled-in-international-cyber-operation]]"
  - "[[2026-04-18_justice-gov_avalanche-network-dismantled-international-cyber-operation]]"
  - "[[2017-04-01_eurojust-europa-eu_operation-avalanche-closer-look]]"
  - "[[2026-04-18_bsi-bund-de_avalanche-botnet-infrastructure]]"
  - "[[bbc-operation-avalanche]]"
  - "[[reuters-operation-avalanche]]"
  - "[[kaspersky-operation-avalanche]]"
summary: "Operation Avalanche was a German-origin investigation and multinational takedown that disrupted one of the world's largest malware, phishing and spam infrastructures on 30 November 2016. Europol, Eurojust, INTERPOL, the FBI, BSI and many national partners combined judicial coordination, technical sinkholing, domain blocking and server seizures to break the network."
created: 2026-04-08
updated: 2026-04-26
---
## Summary

Operation Avalanche was a German-origin investigation and multinational takedown that disrupted one of the world's largest malware, phishing and spam infrastructures on 30 November 2016. Europol, Eurojust, INTERPOL, the FBI, BSI and many national partners combined judicial coordination, technical sinkholing, domain blocking and server seizures to break the network.

> [!note] Audit Note — Participating Countries Source Verification (2026-04-21)
> Re-verified on 2026-04-21 using TLS fingerprint impersonation (`curl_cffi` with `chrome124`) to bypass Cloudflare bot protection on the Europol press release. The full 30-country roster is embedded in the Europol page's inline JSON under `"Countries involved:"` and as a structured country-code list.
>
> **All 29 countries currently in `participating_countries` are explicitly named in the Europol primary source** (plus corroborating mentions across Eurojust case report PDF, BSI bund.de, BBC, Kaspersky advisory). Colombia was mistakenly removed earlier on the same day based on partial accessible-source verification and has been **reinstated**.
>
> Primary-source quote (Europol):
> > "Countries involved: Armenia, Australia, Austria, Azerbaijan, Belgium, Belize, Bulgaria, Canada, Colombia, Finland, France, Germany, Gibraltar, Hungary, India, Italy, Lithuania, Luxembourg, Moldova, Montenegro, Netherlands, Norway, Poland, Romania, Singapore, Sweden, Taiwan, Ukraine, United Kingdom, United States."
>
> Note: Europol names **Gibraltar** (in addition to the 29 countries tracked here). Gibraltar is a British Overseas Territory rather than a UN member state and does not currently have a country page in this wiki; flagged as a candidate to add.

## Why The Operation Matters

Avalanche is a reference case for infrastructure takedowns because it was not just an arrest sweep. The public record shows a layered enforcement model:

- German prosecutors and investigators developed the case over several years.
- Europol and Eurojust handled operational and judicial coordination across borders.
- BSI and technical partners supported sinkholing and post-takedown victim-notification work.
- Domain registries and private-sector partners were needed because the infrastructure used fast-flux and large numbers of abusive domains.

## Participating Parties

**Lead axis:**
- German prosecution and investigators in Verden/Lueneburg
- [[europol-ec3|Europol EC3]]
- [[eurojust]]

**Key operational partners:**
- [[interpol]]
- [[fbi]]
- [[usdoj]]
- BSI
- [[shadowserver]]
- [[icann]]

## Results

- 5 arrests publicly attributed to the operation
- 221 servers targeted for seizure or disruption
- 800,000+ malicious domains blocked

## Cooperation And Legal Analysis

The Eurojust case study is especially important because it confirms the judicial-cooperation side of the operation, not just the media headline numbers. The BSI page is equally important for integrity because it shows that the takedown did not itself clean infected machines; authorities still needed follow-up remediation and victim-notification work. That distinction helps keep the page from overstating what "takedown" meant in practice.

The operation also illustrates a recurring cybercrime pattern: infrastructure disruption requires a mix of criminal procedure, technical operations and private-sector cooperation. Any summary that reduces Avalanche to simple seizure counts misses the actual multinational coordination problem that made the operation notable.

## Follow-Up Actions

> [!warning] No public court documents found
> Public reporting confirms the multinational takedown and related arrests, but the repo does not currently contain a clean, public docket set tying Avalanche to a single court-driven prosecution narrative.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2016-11-30: 'Avalanche' network dismantled in international cyber operation.
- US DOJ USAO, 2016-12-05: Avalanche Network Dismantled in International Cyber Operation.
- Eurojust, 2017-04-01: Operation Avalanche: a closer look.
- Federal Office for Information Security (BSI), 2026-04-18: "Avalanche" botnet infrastructure.
- BBC, 2016-12-01: BBC: Operation Avalanche.
- Reuters, 2024-09-18: Reuters: 'Ghost' Cybercrime Platform Dismantled in Global Operation, 51 Arrested.
- Kaspersky, 2016-2017: Kaspersky: Operation Avalanche.

## Operational Timeline

- 2012: activity or investigation start.
- 2016-11-30: public announcement.
- 2016-11-30: reported enforcement endpoint.
- 2016-11-30: public source coverage from Europol.
- 2016-12-01: public source coverage from BBC.
- 2016-12-05: public source coverage from US DOJ USAO.
- 2016-2017: public source coverage from Kaspersky.
- 2017-04-01: public source coverage from Eurojust.

## Evidence and Attribution Notes

- Operation Avalanche, launched from a German investigation in 2012 and culminating on November 30, 2016, dismantled the world's largest phishing, spam, and malware distribution network known as "Avalanche.
- The network had victimized users in over 180 countries through online banking hacking, phishing, spam, and malware distribution.
- Updated December 5, 2016 Topic Cybercrime Component USAO - Pennsylvania, Western...Release Darknet Drug Trafficker from Western Pennsylvania Sentenced in D.C.
- Eurojust describes Avalanche as a German investigation that began in 2012 and exposed a resilient criminal infrastructure used for malware, phishing and spam at global scale.
- The publication states that the network infected millions of private and business computer systems and enabled credential theft, bank transfers, and money-mule recruitment.
- Eurojust's case study is useful for the judicial-cooperation dimension because it focuses on the legal and coordination problems of a multinational takedown rather than only the press-release headline numbers.
- Eurojust's case study provides the judicial-cooperation view of Operation Avalanche.
- It confirms that the matter originated from a German investigation in 2012, involved a highly resilient fast-flux infrastructure, and required coordinated action across many jurisdictions to disrupt the network and preserve evidence.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| 1 | 'Avalanche' network dismantled in international cyber operation | Europol | 2016-11-30 | https://www.europol.europa.eu/media-press/newsroom/news/%E2%80%98avalanche%E2%80%99-network-dismantled-in-international-cyber-operation |
| 2 | Avalanche network dismantled in international cyber operation | U.S. Department of Justice | repo snapshot | [[2026-04-18_justice-gov_avalanche-network-dismantled-international-cyber-operation]] |
| 3 | Operation Avalanche: a closer look | Eurojust | 2017-04-01 | https://www.eurojust.europa.eu/publication/operation-avalanche-closer-look |
| 4 | "Avalanche" botnet infrastructure | BSI | current | https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Cyber-Sicherheitslage/Methoden-der-Cyber-Kriminalitaet/Botnetze/Botnetz-Avalanche/botnet-avalanche_node.html |
| 5 | Operation Avalanche supplementary coverage | BBC | 2016-2017 | see linked source page |
| 6 | Operation Avalanche supplementary coverage | Reuters | 2016-2017 | see linked source page |
| 7 | Operation Avalanche supplementary coverage | Kaspersky | 2016-2017 | see linked source page |
