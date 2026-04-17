---
type: operation
title: "Operation Dark HunTOR"
aliases:
  - "Dark HunTOR"
  - DarkHunTOR
  - "Operation Dark HunTor"
case_id: CYB-2021-010
period: 2
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - seizure
  - asset_freeze
outcome: success
timeframe:
  announced: 2021-10-26
  start: 2021-01-11
  end: 2021-10-26
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "DarkMarket vendors and dark web drug traffickers"
lead_agency: "[[europol-ec3]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[australia]]"
  - "[[bulgaria]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[italy]]"
  - "[[netherlands]]"
  - "[[switzerland]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[uk-nca]]"
  - "[[germany-bka]]"
  - "[[netherlands-politie]]"
legal_basis:
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[europol-jit]]"
results:
  arrests: 150
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "EUR 26.7 million (~USD 31 million) in cash and virtual currencies"
  other:
    - "234 kg of drugs seized (152 kg amphetamine, 27 kg opioids, 25,000+ ecstasy pills)"
    - "45 firearms seized"
    - "Italian authorities simultaneously shut down DeepSea and Berlusconi marketplaces"
edges:
  - source_actor: "Europol EC3"
    target_actor: FBI
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: "Germany BKA"
    target_actor: "Europol EC3"
    cooperation_type: evidence_transfer
    legal_basis: Budapest_Convention
    direction: directed
  - source_actor: "Europol EC3"
    target_actor: "UK NCA"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
credibility_index: 3.5
source_tier: 2
missing_fields:
  []
related_cases:
  []
related_operations:
  - "[[darkmarket-takedown]]"
  - "[[nemesis-market-takedown]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Seized marketplace infrastructure yields intelligence for follow-on investigations"
  - "Multi-country coordination through J-CAT enables rapid parallel enforcement actions"
  - "EMPACT framework provides effective policy umbrella for EU-US joint operations"
source_count: 5
sources:
  - "[[uk-nca-darkode-forum-takedown|UK NCA: "Operation Dark HunTOR press release]]\""
created: 2026-04-10
updated: 2026-04-10
operation_role: umbrella
parent_operation: ""
---
## Summary

Operation Dark HunTOR was a coordinated international law enforcement action announced on 26 October 2021 that resulted in the arrest of 150 suspected dark web drug traffickers across nine countries. The operation seized approximately EUR 26.7 million (~USD 31 million) in cash and cryptocurrency, 234 kg of drugs, and 45 firearms. Coordinated by [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and [[eurojust|Eurojust]], Dark HunTOR is almost certainly the largest follow-on enforcement action stemming from a single dark web marketplace seizure, building directly on the January 2021 takedown of [[darkmarket-takedown|DarkMarket]].

The operation demonstrated the "cascade" model of dark web enforcement: seizing marketplace infrastructure, extracting intelligence on vendors, and coordinating simultaneous arrest sweeps across multiple jurisdictions.

## Background

### DarkMarket Takedown (January 2021)

On 11 January 2021, German authorities (Zentralstelle zur Bekampfung der Internetkriminalitat, ZIT, and [[germany-bka|BKA]]) shut down DarkMarket, then the world's largest illegal dark web marketplace, and arrested its alleged operator, an Australian national, near the German-Danish border. At the time of its closure, DarkMarket had nearly 500,000 users, over 2,400 vendors, and had facilitated at least 320,000 transactions valued at over EUR 140 million in cryptocurrency. Crucially, German authorities seized the marketplace's servers, located in Moldova and Ukraine, which contained extensive data on vendors, buyers, and transaction records.

### Intelligence Exploitation

Following the DarkMarket seizure, [[europol-ec3|Europol EC3]] spent approximately ten months compiling intelligence packages from the seized infrastructure to identify high-value targets -- vendors who had been actively trafficking drugs and other illicit goods through the marketplace. This intelligence was shared with participating agencies through the Joint Cybercrime Action Taskforce (J-CAT), hosted at Europol headquarters in The Hague.

### JCODE Partnership

On the US side, the operation was led by the Joint Criminal Opioid and Darknet Enforcement (JCODE) team, a multi-agency initiative within the [[us-doj|Department of Justice]] focused on disrupting opioid trafficking on the darknet. JCODE brought together the FBI, DEA, HSI, USPIS, and IRS-CI.

## Participating Parties

### Coordinating Bodies

| Body | Role |
|---|---|
| [[europol-ec3]] | Intelligence analysis, J-CAT coordination, operational hub |
| [[eurojust]] | Judicial coordination across EU member states |

### Participating Countries and Agencies

| Country | Arrests | Key Agencies |
|---|---|---|
| [[united-states]] | 65 | FBI, DEA, HSI, USPIS, IRS-CI (via JCODE) |
| [[germany]] | 47 | BKA, ZIT, state police agencies |
| [[united-kingdom]] | 24 | [[uk-nca]], NPCC |
| [[italy]] | 4 | Public Prosecutor's Office Brescia, Guardia di Finanza |
| [[netherlands]] | 4 | [[netherlands-politie]] |
| [[france]] | 3 | National Police, National Gendarmerie, Customs |
| [[switzerland]] | 2 | Zurich Cantonal Police |
| [[bulgaria]] | 1 | General Directorate Combating Organized Crime |
| [[australia]] | 0 | Australian Federal Police (AFP) -- intelligence support |

### Policy Framework

The operation was conducted within the European Multidisciplinary Platform Against Criminal Threats (EMPACT), which provides a strategic framework for EU security priorities and enables structured cooperation between EU member states and third countries.

## Legal Framework

The operation relied on multiple legal instruments:

1. **[[budapest-convention|Budapest Convention on Cybercrime]]** (Art. 29-35): Provided the foundation for cross-border evidence preservation and production requests between European parties and the US.
2. **EMPACT**: EU policy framework that authorized the prioritization of dark web crime as a collective enforcement target.
3. **Bilateral MLATs**: Evidence sharing between the US (via JCODE) and European counterparts likely utilized existing bilateral [[mlat-process|MLAT]] channels alongside the Budapest Convention framework.
4. **Eurojust coordination**: Facilitated judicial authorization for simultaneous enforcement actions across multiple EU jurisdictions.

> [!note] Legal basis detail
> The precise legal instruments used for each bilateral evidence exchange have not been publicly disclosed. The above assessment is based on the standard legal frameworks available for EU-US law enforcement cooperation (confidence: likely).

## Operational Timeline

| Date | Event |
|---|---|
| 2021-01-11 | DarkMarket taken down by German authorities; operator arrested; servers seized in Moldova and Ukraine |
| 2021-01 to 2021-10 | Europol EC3 compiles intelligence packages from seized DarkMarket infrastructure; targets identified via J-CAT |
| 2021-10 (exact date undisclosed) | Coordinated arrest operations executed simultaneously across nine countries |
| 2021-10-26 | Europol, DOJ, and participating agencies publicly announce results of Operation Dark HunTOR |
| 2021-10-26 | Deputy AG Lisa Monaco delivers remarks at press conference; Italian authorities announce DeepSea and Berlusconi marketplace seizures |
| 2021-10-27 | [[uk-nca|UK NCA]] publishes UK-specific results: 24 arrests, GBP 220,000+ cash/bitcoin, 50+ kg drugs |

## Results and Impact

### Quantitative Results

| Metric | Amount |
|---|---|
| Arrests | 150 across 9 countries |
| Cash and cryptocurrency seized | EUR 26.7 million (~USD 31 million) |
| Drugs seized | 234 kg total |
| -- Amphetamine | 152 kg |
| -- Opioids | 27 kg |
| -- Ecstasy pills | 25,000+ |
| -- Cocaine | ~21.6 kg |
| -- MDMA | ~32.5 kg |
| Firearms seized | 45 |

### Concurrent Italian Operations

Italian authorities, working in parallel under the Dark HunTOR umbrella, shut down two additional dark web marketplaces:
- **DeepSea marketplace**: Seized with administrator arrested
- **Berlusconi marketplace**: Seized with administrator arrested
- Combined cryptocurrency seizure from these two platforms: EUR 3.6 million

### Strategic Impact

Operation Dark HunTOR demonstrated three strategically significant patterns for dark web enforcement:

1. **Follow-on investigation model**: The operation proved that seizing marketplace infrastructure yields intelligence for sustained law enforcement action well beyond the initial takedown. The ten-month gap between the DarkMarket seizure and Dark HunTOR arrests suggests a methodical exploitation of seized data.

2. **Deterrence messaging**: Deputy AG Monaco stated that the operation sent "a clear message to anyone selling or buying illegal goods on the dark web: the international law enforcement community has the means and the will to track you down" (DOJ, 2021-10-26).

3. **EU-US operational bridge**: The operation successfully bridged the EU-centric EMPACT framework with the US-centric JCODE initiative, using J-CAT as the coordination layer.

## Cooperation Mechanisms Used

| Mechanism | Role in Operation |
|---|---|
| J-CAT (Joint Cybercrime Action Taskforce) | Primary coordination layer at Europol HQ; intelligence package distribution |
| EMPACT | EU policy framework authorizing collective enforcement priority |
| JCODE | US multi-agency darknet enforcement team; led US-side arrests |
| [[eurojust]] coordination meetings | Judicial authorization for simultaneous EU arrest operations |
| Europol operational analysis | EC3 compiled intelligence from seized DarkMarket servers |

## Challenges and Friction Points

1. **Jurisdictional complexity**: With vendors in nine countries, each arrest required domestic legal authorization, creating coordination challenges around timing synchronization.
2. **Data sovereignty**: Seized servers were located in Moldova and Ukraine (non-EU states), raising potential legal questions about the admissibility of evidence obtained from those servers in EU courts.
3. **Cryptocurrency tracing**: The EUR 26.7 million in seized cryptocurrency required forensic blockchain analysis across multiple exchanges and wallet types.

## Lessons Learned

1. **Infrastructure seizure enables cascade enforcement**: The DarkMarket-to-Dark-HunTOR pipeline demonstrated that a single marketplace takedown can generate intelligence for 150+ arrests across nine countries, if the seized data is methodically exploited.

2. **J-CAT as a model for transatlantic coordination**: The Joint Cybercrime Action Taskforce at Europol proved effective as a neutral coordination layer between EU law enforcement and US JCODE, bridging different legal traditions and operational cultures.

3. **Parallel marketplace seizures multiply impact**: Italy's simultaneous takedown of DeepSea and Berlusconi marketplaces under the Dark HunTOR umbrella demonstrated that coordinated multi-target operations amplify disruption of the dark web ecosystem.

4. **Time-delayed enforcement is viable**: The ten-month gap between DarkMarket seizure and Dark HunTOR arrests shows that patient intelligence exploitation can be more productive than immediate arrest sweeps.

## Korean Involvement (한국의 참여)

There is no publicly available evidence of South Korean participation in Operation Dark HunTOR. The operation's scope was limited to nine countries (US, Germany, UK, Italy, Netherlands, France, Switzerland, Bulgaria, Australia), all of which are either EU member states, Five Eyes partners, or established Europol cooperation partners.

However, the operation's follow-on investigation model is relevant to Korean law enforcement practice. The Korean National Police Agency (경찰청) and Korea Internet & Security Agency (KISA) have participated in similar dark web enforcement operations through [[interpol-igci|INTERPOL IGCI]] channels, particularly in the context of CSAM and drug trafficking investigations. The cascade intelligence model demonstrated by Dark HunTOR could be applied to future INTERPOL-coordinated operations in which Korea participates.

## Contradictions & Open Questions

1. **Arrest count discrepancy**: Some early media reports cited "more than 150" arrests, while official Europol and DOJ statements consistently state exactly 150. The NCA's UK-specific press release states 24 UK arrests, which is consistent with Europol's total. This is likely a rounding issue in media coverage rather than a substantive contradiction.

2. **DarkMarket operator nationality**: The DarkMarket operator arrested in January 2021 has been described as an "Australian national" in some sources, but details of his identity, charges, and legal proceedings in Germany have been limited. His prosecution status as of 2021-10 is unclear from public sources.

3. **MLAT vs. informal channels**: The extent to which formal MLAT requests versus informal police-to-police channels (through J-CAT) were used for evidence sharing between EU countries and the US has not been publicly detailed.

4. **Long-term prosecutorial outcomes**: The 150 arrests were announced in October 2021, but conviction rates and sentences resulting from these arrests have not been comprehensively reported as of the available sources.

> [!note] Source diversity
> This page is primarily based on official press releases from Europol (2021-10-26), DOJ/DEA (2021-10-26), and NCA (2021-10-27), supplemented by secondary reporting from BleepingComputer and SecurityAffairs. Additional primary sources (e.g., Italian judiciary statements, German BKA press releases) would strengthen the page.

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References
| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | 150 arrested in dark web drug bust as police seize EUR 26 million | Europol | 2021-10-26 | https://www.europol.europa.eu/media-press/newsroom/news/150-arrested-in-dark-web-drug-bust-police-seize-%E2%82%AC26-million |
| [2] | Department of Justice Announces Results of Operation Dark HunTor | US DOJ/DEA | 2021-10-26 | https://www.dea.gov/press-releases/2021/10/26/department-justice-announces-results-operation-dark-huntor |
| [3] | International operation targets dark web drugs marketplace | UK NCA | 2021-10-27 | https://www.nationalcrimeagency.gov.uk/news/international-operation-targets-dark-web-drugs-marketplace |
| [4] | Deputy AG Lisa Monaco Delivers Remarks on Operation Dark HunTor | US DOJ | 2021-10-26 | https://www.justice.gov/archives/opa/speech/deputy-attorney-general-lisa-o-monaco-delivers-remarks-operation-dark-huntor |
| [5] | Police arrest 150 dark web vendors of illegal drugs and guns | BleepingComputer | 2021-10-26 | https://www.bleepingcomputer.com/news/security/police-arrest-150-dark-web-vendors-of-illegal-drugs-and-guns/ |
