---
type: operation
title: "CyberBunker Bulletproof Hosting Takedown"
title_ko: "사이버벙커 방탄호스팅 소탕"
aliases:
  - "CyberBunker 2.0 Raid"
  - "Traben-Trarbach Data Centre Raid"
  - "CB3ROB Takedown"
case_id: ""
period: 2
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - arrest
  - seizure
outcome: success
timeframe:
  announced: 2019-09-27
  start: 2015
  end: 2021-12-13
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "CyberBunker 2.0 (CB3ROB) bulletproof hosting operation in former NATO bunker"
lead_agency: "[[germany-lka|Rhineland-Palatinate LKA]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[germany]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[germany-lka|Rhineland-Palatinate LKA]]"
  - "[[germany-bka|Bundeskriminalamt (BKA)]]"
  - "[[europol-ec3|Europol EC3]]"
legal_basis:
  - "[[budapest-convention|Budapest Convention]]"
mechanisms_used:
  - "[[joint-investigation-team|Joint Investigation Team]]"
  - "[[informal-cooperation|Informal Police Cooperation]]"
results:
  arrests: 7
  indictments: 8
  servers_seized: 200
  domains_seized: 0
  cryptocurrency_seized: ""
  other:
    - "5,000 sq metre former NATO bunker facility raided by 600+ police officers"
    - "8 defendants convicted (December 2021)"
    - "Main defendant sentenced to 5 years 9 months"
    - "Mobile phones, documents, and large sums of cash seized"
edges:
  - source_actor: "Germany LKA Rhineland-Palatinate"
    target_actor: "Germany BKA"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: Germany
    target_actor: Netherlands
    cooperation_type: evidence_transfer
    legal_basis: Budapest_Convention
    direction: directed
  - source_actor: Germany
    target_actor: "Europol EC3"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - case_id
  - cryptocurrency_seized
related_operations:
  - "[[darkmarket-takedown|DarkMarket Takedown (2021)]]"
related_cases:

challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional complexity of bulletproof hosting]]"
lessons_learned:
  - "Physical infrastructure seizure requires massive tactical resources"
  - "Bulletproof hosting prosecution is legally complex -- convictions for membership in criminal organization are more achievable than accessory charges for hosted crimes"
  - "Multi-year investigation patience essential for complex infrastructure cases"
source_count: 5
sources:
  - "[[2020-07-21_lgtr-justiz-rlp-de_cyberbunker-indictment-admitted]]"
  - "[[2021-12-13_lgtr-justiz-rlp-de_cyberbunker-judgment]]"
  - "[[2023-09-12_lgtr-justiz-rlp-de_cyberbunker-convictions-final]]"
  - "[[2021-01-01_bka-de_cybercrime-bundeslagebild-2021-cyberbunker]]"
  - "[[2019-09-30_arstechnica_com_cyberbunker-raid]]"
created: 2026-04-10
updated: 2026-04-18
operation_role: umbrella
parent_operation: ""
summary: "The CyberBunker Takedown was a major German law enforcement operation targeting a bulletproof hosting provider operating from a former NATO bunker in Traben-Trarbach, Rhineland-Palatinate, [[germany|Germany]]. On 26-27 September 2019, more than 600 police officers raided the underground facility, arrested seven suspects and seized roughly 200 servers. The resulting prosecution against eight defendants culminated in December 2021 convictions for participation in a criminal organization, and those convictions were largely confirmed as final in September 2023. The operation became a landmark European bulletproof-hosting case and directly fed the later [[darkmarket-takedown|DarkMarket takedown]]."
jurisdictions:
  - "[[germany]]"
  - "[[netherlands]]"
organizations:
  - "[[germany-lka|Rhineland-Palatinate LKA]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[germany-bka|Bundeskriminalamt (BKA)]]"
crime_types:
  - "[[online-fraud-ic]]"
---
## Summary

The CyberBunker Takedown was a major German law enforcement operation targeting a bulletproof hosting provider operating from a former NATO bunker in Traben-Trarbach, Rhineland-Palatinate, [[germany|Germany]]. On 26-27 September 2019, more than 600 police officers, including tactical units, raided the 5,000 square metre underground facility, arrested seven suspects, and seized approximately 200 servers. The facility, known as CyberBunker 2.0 (or CB3ROB), had hosted numerous dark web marketplaces, drug trading platforms, and fraud sites. Following a trial of more than a year, the Trier Regional Court convicted eight defendants in December 2021 for membership in a criminal organization, with sentences ranging from a one-year suspended sentence to five years and nine months in prison for the main defendant, a Dutch national named Herman Johan Xennt. The case was a landmark in bulletproof hosting prosecution and directly enabled the subsequent [[darkmarket-takedown|DarkMarket takedown]] in January 2021.

## Background

### CyberBunker Origins

CyberBunker was founded by Dutch national Herman Johan Xennt, who in 1995 purchased a former NATO bunker in Kloetinge, the Netherlands, to operate a "bulletproof hosting" service -- a hosting provider that promises clients near-total anonymity and refuses to comply with law enforcement takedown requests. The business model was to host any content except child sexual abuse material and terrorism-related content.

After the original Dutch facility was shut down following a fire in 2002, Xennt relocated operations. In 2013, he purchased a decommissioned German military bunker in Traben-Trarbach along the Mosel River in Rhineland-Palatinate. The five-storey underground facility, originally built to withstand nuclear attack, had iron blast doors and was nearly impenetrable -- making it an ideal location for a covert hosting operation.

### What CyberBunker Hosted

The bulletproof hosting facility serviced a number of dark web platforms, including:

- **Wall Street Market**: One of the largest dark web marketplaces for drugs, hacking tools, and stolen data (taken down separately in May 2019)
- **Cannabis Road**: A drug-trading platform
- **Orange Chemicals**: A synthetic drug marketplace
- **Flugsvamp**: A Swedish-language dark web drug market
- **Fraudsters**: A forum for trading illegal drugs, counterfeit money, and fake identification documents
- **[[darkmarket-takedown|DarkMarket]]**: What would become the world's largest dark web marketplace at the time of its separate takedown in January 2021

Investigators estimated that CyberBunker's clients were responsible for hundreds of thousands of individual criminal offences.

## Participating Parties

### Law Enforcement

| Entity | Role |
|--------|------|
| [[germany-lka|Rhineland-Palatinate LKA]] (State Criminal Police) | Lead investigating agency; began investigation in 2015 |
| [[germany-bka|BKA (Federal Criminal Police)]] | Federal support; tactical entry team |
| Rhineland-Palatinate General Prosecutor's Office (Koblenz) | Prosecuting authority |
| [[europol-ec3|Europol EC3]] | International coordination and intelligence support |
| German Federal Police (tactical units) | Physical raid execution |

### Defendants

| Defendant | Nationality | Sentence |
|-----------|-------------|----------|
| Herman Johan Xennt (main defendant) | Dutch | 5 years, 9 months |
| Defendant 2 | Not publicly disclosed | 4 years, 3 months |
| Defendants 3-7 | Dutch and German nationals | 2 years, 4 months to 4 years, 3 months |
| Defendant 8 | Not publicly disclosed | 1-year suspended sentence |

> [!note] Nationality
> The majority of defendants were Dutch nationals. Xennt's Dutch nationality and the cross-border nature of the operation (Dutch nationals operating in Germany) illustrate the international dimension of the case.

## Legal Framework

### Investigation Phase

In 2015, a German cybercrime unit within the Rhineland-Palatinate LKA began investigating Xennt's activities based on intelligence about the Traben-Trarbach facility. The investigation employed:

- **Intercepted web traffic analysis**: Authorities monitored internet traffic flowing to and from the bunker
- **Undercover operations**: Investigators created a scam lottery website and sought to host it on CyberBunker to prove the company knowingly aided criminal activity
- **Traditional surveillance**: Physical monitoring of the bunker facility over several years

### Prosecution Legal Issues

The prosecution faced a significant legal challenge. The Trier Regional Court **convicted** all eight defendants of forming and being members of a criminal organization (Bildung einer kriminellen Vereinigung, German Criminal Code ss 129). However, the court **acquitted** the defendants of being accessories to the approximately 250,000 individual crimes allegedly committed through the hosted websites.

The court ruled that operating a bulletproof hosting service did not automatically make the operators legally complicit in every crime committed by their clients, even if the operators knew the services were used for criminal purposes. This distinction had significant implications for future bulletproof hosting prosecutions across Europe.

## Operational Timeline

| Date | Event |
|------|-------|
| 2013 | Xennt purchases the former military bunker in Traben-Trarbach |
| 2014 | CyberBunker 2.0 (CB3ROB) begins operations in the German facility |
| 2015 | Rhineland-Palatinate LKA cybercrime unit begins investigation |
| 2015-2019 | Multi-year investigation: traffic interception, undercover operations, surveillance |
| 2019-05 | Wall Street Market taken down (one of CyberBunker's largest clients) |
| 2019-09-26/27 | 600+ police officers raid the bunker facility; 7 persons arrested |
| 2019-09-28 | Public announcement of the raid and seizure |
| 2019-09-30 | Additional details released; approximately 200 servers confirmed seized |
| 2020-10-19 | Trial begins at the Trier Regional Court |
| 2021-01-11 | [[darkmarket-takedown|DarkMarket]] taken down by German police (investigation enabled by CyberBunker seizure) |
| 2021-12-13 | Verdict: 8 defendants convicted of membership in criminal organization; acquitted of accessory charges |

## Results and Impact

### Direct Results

| Metric | Value |
|--------|-------|
| Persons arrested | 7 (initial raid) |
| Persons convicted | 8 |
| Servers seized | ~200 |
| Police deployed | 600+ |
| Investigation duration | 4+ years (2015-2019) |
| Trial duration | ~14 months (Oct 2020 - Dec 2021) |

### Broader Impact

1. **DarkMarket takedown enabled**: Intelligence and data from the CyberBunker seizure directly led to the identification and takedown of [[darkmarket-takedown|DarkMarket]] in January 2021 by German police in cooperation with international partners. DarkMarket was the world's largest dark web marketplace at the time, with nearly 500,000 users.

2. **Bulletproof hosting legal precedent**: The trial established important -- if mixed -- precedent for prosecuting bulletproof hosting operators. The conviction for criminal organization membership succeeded, but the acquittal on accessory charges highlighted the legal difficulty of holding hosting providers liable for their clients' crimes.

3. **Physical infrastructure seizure model**: The operation demonstrated that even heavily fortified physical infrastructure can be seized with sufficient tactical resources and planning.

## Cooperation Mechanisms Used

1. **German federal-state cooperation**: The case required coordination between the state-level LKA (which initiated the investigation) and federal BKA (which provided tactical and intelligence support for the raid).

2. **[[europol-ec3|Europol EC3]]** provided international intelligence support, particularly regarding the international criminal networks using CyberBunker's services.

3. **[[informal-cooperation|Informal cooperation]]** with [[netherlands|Dutch]] authorities was likely necessary given the Dutch nationality of the main defendant and other suspects, though details of Dutch law enforcement involvement have not been extensively reported.

4. **Cross-border evidence**: The operation's intelligence fed into investigations in multiple other countries, most notably the [[darkmarket-takedown|DarkMarket]] case.

## Challenges and Friction Points

- **Physical fortification**: The bunker's five-storey underground structure with blast doors required a military-style tactical entry with 600+ officers -- an unusual scale for a cybercrime operation.
- **Legal liability threshold**: The acquittal on accessory charges (250,000 individual crimes) demonstrated that German criminal law has a high threshold for holding infrastructure providers liable for client conduct, even when the providers are aware of criminal use.
- **Multi-year investigation**: The four-year investigation (2015-2019) required sustained resources and commitment from a state-level agency.
- **[[jurisdictional-conflicts|Cross-border dimension]]**: Dutch nationals operating in Germany, serving clients worldwide, created a complex jurisdictional picture.

## Lessons Learned

1. **Physical infrastructure remains a viable target**: Despite the trend toward cloud and distributed hosting, some criminal operations rely on physical infrastructure that can be seized -- requiring tactical capabilities rarely used in cybercrime investigations.

2. **Criminal organization charges as fallback**: When accessory liability for hosted crimes is legally difficult to establish, prosecution for membership in a criminal organization (ss 129 StGB) can serve as an effective alternative theory.

3. **Intelligence cascade effect**: Seizing a bulletproof hosting facility generates vast intelligence that enables downstream investigations and takedowns ([[darkmarket-takedown|DarkMarket]] being the most significant example).

4. **Investigation patience pays off**: The four-year investigation built a strong evidentiary foundation that survived a 14-month trial.

## Korean Involvement (한국의 참여)

No [[south-korea|South Korean]] involvement in the CyberBunker takedown has been publicly documented. The case is nonetheless relevant to Korea as a precedent for bulletproof hosting prosecution and for the intelligence cascade model where a single infrastructure takedown enables multiple subsequent operations. Korean cybercrime units may encounter similar bulletproof hosting challenges in the Asia-Pacific region.

## Contradictions & Open Questions

- **Accessory liability gap**: The acquittal on accessory charges for approximately 250,000 crimes creates a potential loophole for bulletproof hosting operators who can argue they did not directly participate in client activities. Whether German law has been amended to address this gap is unclear.
- **Eighth defendant**: Seven persons were arrested during the raid, but eight were convicted. The identity and circumstances of the eighth defendant have not been clearly reported.
- **Cryptocurrency seizure**: The amount of cryptocurrency seized from the facility has not been publicly disclosed, though CyberBunker's operations were reportedly crypto-fuelled.
- **Connection to original CyberBunker**: The relationship between the original Dutch CyberBunker (1990s-2002) and the German operation (2013-2019) was primarily through Xennt personally. Whether any Dutch investigation preceded the German operation is unclear.

## Follow-Up Actions

> [!info] Public judicial notices available
> As of 2026-04-18, the repo includes official Trier Regional Court
> notices covering indictment admission, judgment, and the later
> confirmation that the principal convictions became final. Full
> underlying German court filings are not mirrored in the repo.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Anklage gegen acht Angeklagte im Verfahren um den sogenannten Cyberbunker in Traben-Trarbach zugelassen | Landgericht Trier | 2020-07-21 | https://lgtr.justiz.rlp.de/presse-aktuelles/detail/anklage-gegen-acht-angeklagte-im-verfahren-um-den-sogenannten-cyberbunker-in-traben-trarbach-zugelassen |
| 2 | Urteil im sog. Cyberbunkerverfahren | Landgericht Trier | 2021-12-13 | https://lgtr.justiz.rlp.de/presse-aktuelles/detail/urteil-im-sog-cyberbunkerverfahren |
| 3 | Verurteilungen der Angeklagten im Cyberbunker-Verfahren rechtskräftig | Landgericht Trier | 2023-09-12 | https://lgtr.justiz.rlp.de/presse-aktuelles/detail/verurteilungen-der-angeklagten-im-cyberbunker-verfahren-rechtskraeftig |
| 4 | Cybercrime Bundeslagebild 2021 - CyberBunker section | Bundeskriminalamt | 2021 | https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/JahresberichteUndLagebilder/Cybercrime/cybercrimeBundeslagebild2021.pdf?__blob=publicationFile&v=6 |
| 5 | German police seize bulletproof hosting data center in former NATO bunker | Ars Technica | 2019-09-30 | https://arstechnica.com/information-technology/2019/09/german-police-seize-bulletproof-hosting-data-center-in-former-nato-bunker/ |

