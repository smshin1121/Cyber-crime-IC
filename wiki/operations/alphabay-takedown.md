---
type: operation
title: "Operation Bayonet -- AlphaBay & Hansa Takedown"
aliases:
  - "Operation Bayonet"
  - "AlphaBay Takedown"
  - "AlphaBay/Hansa Double Sting"
case_id: CYB-2017-002
period: 1
operation_type: takedown
status: completed
enforcement_type:
  - takedown
  - arrest
  - seizure
  - asset_freeze
outcome: success
timeframe:
  announced: 2017-07-20
  start: 2015
  end: 2017-07-20
  ongoing: false
crime_type: "[[online-fraud-ic]]"
target_entity: "AlphaBay and Hansa darknet marketplaces"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[thailand]]"
  - "[[netherlands]]"
  - "[[lithuania]]"
  - "[[canada]]"
  - "[[united-kingdom]]"
  - "[[france]]"
  - "[[germany]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[netherlands-politie]]"
legal_basis:
  - "[[mutual-legal-assistance]]"
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[mutual-legal-assistance]]"
  - "[[informal-cooperation]]"
  - "[[europol-jit]]"
results:
  arrests: 3
  indictments: 1
  servers_seized: 0
  domains_seized: 2
  cryptocurrency_seized: "$8.8 million (FBI) + 726 million Thai baht (~$21.7 million) frozen by Thai police"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "AlphaBay: 400,000 users, 40,000 vendors, 350,000+ listings disrupted"
    - "Hansa: Covertly operated by Dutch police for ~1 month; 10,000 delivery addresses collected"
    - "Alexandre Cazes (AlphaBay admin) died in Thai custody 2017-07-12"
    - "2 Hansa administrators arrested (German nationals)"
    - "27,000 transactions monitored during covert Hansa operation"
    - "Luxury vehicles, residences, and hotel in Thailand seized"
edges:
  - source_actor: FBI
    target_actor: "Thai Royal Police"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: directed
  - source_actor: FBI
    target_actor: "Netherlands NHTCU"
    cooperation_type: joint_investigation
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: "Netherlands NHTCU"
    target_actor: "Europol EC3"
    cooperation_type: info_sharing
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: FBI
    target_actor: "Europol EC3"
    cooperation_type: info_sharing
    legal_basis: bilateral_MOU
    direction: undirected
  - source_actor: "Netherlands NHTCU"
    target_actor: "Germany BKA"
    cooperation_type: evidence_transfer
    legal_basis: Budapest_Convention
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "exact server count"
  - "full list of national agencies in supporting roles"
related_cases:
  - "[[us-v-cazes-alphabay]]"
  - "[[us-v-herrell-alphabay|United States v. Bryan Herrell (AlphaBay Moderator)]]"
  - "[[us-v-almashwali-alphabay|United States v. Abudullah Almashwali (AlphaBay Vendor)]]"
  - "[[us-v-almashwali-alphabay]]"
  - "[[us-v-herrell-alphabay]]"
related_operations:
  - "[[operation-shrouded-horizon]]"
  - "[[darkode-takedown]]"
  - "[[xdedic-marketplace-takedown]]"
  - "[[operation-us-v-almashwali-alphabay]]"
  - "[[operation-us-v-cazes-alphabay]]"
  - "[[operation-us-v-herrell-alphabay]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Sequential takedowns with covert operation of successor marketplace enables maximum intelligence collection"
  - "OPSEC failures by administrators (reused email addresses) remain a primary identification vector"
  - "International cooperation across diverse legal systems (common law / civil law / Thai law) is feasible for high-priority targets"
  - "Darknet marketplace users rapidly migrate to alternatives -- coordinating takedowns of multiple markets simultaneously maximizes disruption"
source_count: 5
sources:
  - "[[2017-07-20-europol-alphabay-hansa-takedown]]"
  - "[[2017-07-20-doj-alphabay-shutdown]]"
  - "[[2017-07-20-dea-alphabay-shutdown]]"
  - "[[2017-07-20-fbi-alphabay-takedown]]"
  - "[[unodc-alphabay-true-crime-story]]"
created: 2026-04-10
updated: 2026-04-26
operation_role: umbrella
parent_operation: ""
summary: "Operation Bayonet was a multinational law enforcement operation that dismantled **AlphaBay** and **Hansa** -- the world's two largest darknet marketplaces -- in **July 2017**. The operation was led by the [[fbi-cyber-division|FBI]] and the US Drug Enforcement Administration (DEA) for the AlphaBay component, while the [[netherlands-politie|Dutch National Police (NHTCU)]] led the Hansa component, with [[europol-ec3|Europol]] coordinating the overall strategy."
jurisdictions:
  - "[[united-states]]"
  - "[[thailand]]"
  - "[[netherlands]]"
  - "[[lithuania]]"
  - "[[canada]]"
  - "[[united-kingdom]]"
  - "[[france]]"
  - "[[germany]]"
organizations:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[netherlands-politie]]"
crime_types:
  - "[[online-fraud-ic]]"
  - "[[malware-ic]]"
  - "[[dark-web-ic]]"
---
## Summary

Operation Bayonet was a multinational law enforcement operation that dismantled **AlphaBay** and **Hansa** -- the world's two largest darknet marketplaces -- in **July 2017**. The operation was led by the [[fbi-cyber-division|FBI]] and the US Drug Enforcement Administration (DEA) for the AlphaBay component, while the [[netherlands-politie|Dutch National Police (NHTCU)]] led the Hansa component, with [[europol-ec3|Europol]] coordinating the overall strategy.

## Audit Note

This remains an umbrella operation because AlphaBay and Hansa were handled as linked but distinct phases of a multinational takedown. The Hansa covert-operation phase should not be collapsed into the AlphaBay seizure itself.

The operation is *almost certainly* the most sophisticated darknet marketplace takedown in history, employing an unprecedented **double-sting strategy**: the [[netherlands-politie|Dutch police]] covertly seized and operated the Hansa marketplace for approximately one month before AlphaBay was publicly shut down, anticipating that AlphaBay users would migrate to Hansa. This migration trap allowed law enforcement to collect extensive evidence on thousands of vendors and buyers.

AlphaBay's administrator, **Alexandre Cazes** (Canadian, age 25), was arrested by Thai police on **5 July 2017** in Bangkok on behalf of the United States. Cazes died in Thai custody on **12 July 2017** in an apparent suicide. Hansa's two German administrators were arrested by German police. At the time of shutdown, AlphaBay had approximately **400,000 users**, **40,000 vendors**, and over **350,000 listings** for illegal goods and services.

[[europol-ec3|Europol]] described Operation Bayonet as "one of the most sophisticated takedown operations ever seen in the fight against criminal activities online."

## Background

### AlphaBay

AlphaBay was launched in **September 2014** by Alexandre Cazes (alias "Alpha02" and "Admin"), a Canadian citizen living in Thailand. It rapidly grew to become the largest darknet marketplace, surpassing the original Silk Road in scale:

- **350,000+ listings** at time of shutdown, including:
  - 250,000+ drug listings
  - 100,000+ listings for stolen/fraudulent identification documents, malware, hacking tools, firearms, and fraudulent services
- **400,000 registered users** and **40,000 vendors** (per FBI estimates)
- **$600,000-$800,000 in daily transactions** at peak
- Over **$1 billion in cryptocurrency transactions** facilitated over its lifetime
- Operated as a Tor hidden service with Bitcoin and Monero payment options

### Hansa Market

Hansa was the **second-largest** darknet marketplace, operating since 2015. It was administered by two German nationals. After AlphaBay's closure, Hansa experienced a massive influx of users -- vendor registrations surged from approximately 1,000 to 8,000 per day.

### How Cazes Was Identified

Cazes was identified through critical operational security (OPSEC) failures:

- He used his personal Hotmail address (`pimp_alex_91@hotmail.com`) as the "From" address in system-generated welcome and password reset emails sent to new AlphaBay users
- This email address was linked to his real identity through other online accounts
- Additional digital breadcrumbs connected "Alpha02" to Cazes' known online personas

### Investigation Origins

The FBI investigation into AlphaBay began in approximately **2015**. The Dutch police investigation into Hansa began independently. The strategic decision to coordinate the two takedowns into a single operation -- the "double sting" -- was *likely* made in early-to-mid 2017 in coordination with [[europol-ec3|Europol]].

## Participating Parties

### Lead Agencies (AlphaBay)

| Country | Agency | Role |
|---------|--------|------|
| [[united-states]] | [[fbi-cyber-division]] | Lead investigation; identification of Cazes; coordination of arrest request |
| [[united-states]] | DEA (Drug Enforcement Administration) | Co-lead; drug trafficking dimension |
| [[thailand]] | Royal Thai Police | Arrest of Cazes; asset seizure; custody |

### Lead Agencies (Hansa)

| Country | Agency | Role |
|---------|--------|------|
| [[netherlands]] | [[netherlands-politie]] (NHTCU) | Covert takeover and operation of Hansa; intelligence collection |
| [[germany]] | BKA (Bundeskriminalamt) | Arrest of 2 Hansa administrators (German nationals) |

### Coordinating Bodies

| Organization | Role |
|---|---|
| [[europol-ec3]] | Strategic coordination between FBI and Dutch police; intelligence sharing; 10,000 delivery addresses distributed internationally |
| [[eurojust]] | Judicial coordination for EU-side operations |

### Supporting Agencies

| Country | Role |
|---------|------|
| [[lithuania]] | Infrastructure assistance |
| [[canada]] | Investigation support (Cazes' nationality) |
| [[united-kingdom]] | Operational support |
| [[france]] | Operational support |

## Legal Framework

- **US-Thailand MLAT**: Enabled the arrest request for Cazes in Thailand and asset seizure
- **[[budapest-convention|Budapest Convention]]**: Provided framework for cross-border evidence sharing among European participants
- **[[mutual-legal-assistance|Bilateral MLATs]]**: Used for evidence transfers between US and European jurisdictions
- **EU mutual recognition instruments**: Used for cooperation between Netherlands and Germany on the Hansa component
- **Thai Narcotics Act and Computer Crime Act**: Thai domestic legal authority for the arrest and asset seizure

The US filed a **criminal complaint and civil forfeiture action** (US District Court, Eastern District of California) against AlphaBay's assets and Cazes' personal property.

## Operational Timeline

| Date | Event |
|------|-------|
| Sept 2014 | AlphaBay launched by Alexandre Cazes in Thailand |
| ~2015 | FBI opens investigation into AlphaBay |
| ~2016 | Dutch police begin investigation into Hansa Market |
| **2017-06-20** | German police arrest Hansa's two administrators (German nationals) |
| **2017-06-20** | [[netherlands-politie]] (NHTCU) takes covert control of Hansa Market; begins impersonating administrators |
| 2017-06-20 to 2017-07-04 | Dutch police covertly operate Hansa, collecting vendor IP addresses, buyer locations, and transaction data |
| **2017-07-04** | AlphaBay servers seized; marketplace goes offline |
| **2017-07-05** | Alexandre Cazes arrested by Thai Royal Police at his Bangkok residence on behalf of the US |
| 2017-07-05 to 2017-07-20 | AlphaBay users migrate en masse to Hansa; vendor registrations surge to 8,000/day |
| **2017-07-12** | Alexandre Cazes found dead in Thai police custody; Thai authorities rule suicide |
| 2017-07-12 to 2017-07-20 | Dutch police continue to operate Hansa, collecting evidence on migrating AlphaBay users |
| **2017-07-20** | Hansa Market publicly shut down; Operation Bayonet announced jointly by DOJ, Europol, and Dutch police |
| 2017-07-24 | Thai police announce seizure of 726 million Thai baht (~$21.7 million) in Cazes' assets |

## Results and Impact

### Immediate Results

| Metric | Value | Source |
|--------|-------|--------|
| Darknet markets shut down | 2 (AlphaBay + Hansa) | DOJ / Europol |
| Arrests | 3 (Cazes + 2 Hansa admins) | DOJ / Europol |
| AlphaBay users disrupted | ~400,000 | FBI |
| AlphaBay vendors disrupted | ~40,000 | FBI |
| AlphaBay listings removed | 350,000+ | DOJ |
| Assets seized (FBI) | $8.8 million (crypto + bank accounts) | DOJ |
| Assets frozen (Thai police) | 726 million baht (~$21.7 million) | Thai police |
| Hansa delivery addresses collected | 10,000+ | Europol |
| Hansa transactions monitored | 27,000 | Dutch police |
| Hansa vendor IP addresses recorded | Thousands | Dutch police |

### The Hansa Intelligence Operation

During the approximately one month that Dutch police covertly operated Hansa, they implemented several intelligence collection measures:

1. **Modified the PGP encryption feature** to record plaintext copies of encrypted messages before encryption
2. **Recorded all user passwords in plaintext**, enabling cross-referencing with accounts on other marketplaces where users reused passwords
3. **Modified the photo metadata stripping tool** to record GPS coordinates and other metadata from vendor photos before stripping them
4. **Wiped the existing photo database**, forcing vendors to re-upload photos (now with metadata captured)
5. **Collected real IP addresses** of vendors who used Hansa without proper Tor configuration
6. **Distributed 10,000 delivery addresses** to [[europol-ec3|Europol]] for international follow-up investigations

### Strategic Impact

1. **Disrupted darknet ecosystem:** The simultaneous takedown of the two largest markets, combined with intelligence from the covert Hansa operation, generated **hundreds of follow-up investigations** across Europe and globally
2. **Demonstrated the "double sting" model:** Operation Bayonet proved that coordinating the covert operation of one marketplace with the public takedown of another maximizes intelligence collection by exploiting user migration patterns
3. **Deterrence effect:** The revelation that Hansa had been operated by police for a month created significant distrust in the darknet marketplace ecosystem
4. **Asset recovery:** Over $30 million in combined assets seized/frozen
5. **Template for future operations:** The strategic approach influenced subsequent marketplace takedowns

### Limitations

- AlphaBay was **relaunched in August 2021** by a self-described co-founder ("DeSnake"), demonstrating the difficulty of permanently eliminating darknet marketplaces
- Cazes' death precluded prosecution and potential intelligence from cooperation
- The darknet marketplace ecosystem reconstituted rapidly, with users migrating to Dream Market and other alternatives

## Cooperation Mechanisms Used

| Mechanism | Application |
|-----------|-------------|
| [[mutual-legal-assistance]] | US-Thailand MLAT for arrest/extradition request; bilateral MLATs for evidence sharing |
| [[informal-cooperation]] | FBI-NHTCU coordination on double-sting strategy |
| [[europol-jit]] | Europol coordinated intelligence distribution from Hansa operation to member states |
| US forfeiture proceedings | Civil forfeiture complaint for AlphaBay assets and Cazes' property |
| Covert marketplace operation | Dutch police operated Hansa for ~1 month -- *almost certainly* unprecedented at this scale |

### Key Cooperation Innovation: The Double Sting

The most strategically significant aspect of Operation Bayonet was the **coordinated sequencing** of two takedowns:

1. **Phase 1 (Covert):** Dutch police silently take over Hansa (June 20)
2. **Phase 2 (Overt):** FBI shuts down AlphaBay (July 4-5)
3. **Phase 3 (Collection):** Users migrate from AlphaBay to police-controlled Hansa; intelligence collection maximized
4. **Phase 4 (Reveal):** Hansa publicly shut down (July 20); operation announced

This approach required:
- **Precise timing** between FBI and Dutch police actions
- **Trust** between US and Dutch law enforcement to maintain operational security for weeks
- **Europol coordination** to manage multi-jurisdictional intelligence flows
- **Restraint** -- allowing 27,000 illegal transactions on Hansa to build evidence rather than immediately shutting it down

## Challenges and Friction Points

- **Jurisdictional complexity:** The operation spanned at least 8 countries with different legal systems (common law, civil law, Thai law), requiring extensive legal coordination
- **Cazes' death:** The apparent suicide of the primary target in Thai custody prevented prosecution and potential cooperation that could have yielded intelligence on broader criminal networks
- **Ethical and legal questions:** Dutch police's decision to allow 27,000 illegal transactions during the covert Hansa operation raised questions about the limits of undercover operations and potential entrapment
- **Cryptocurrency tracing:** Tracing and seizing cryptocurrency assets across multiple blockchain networks and exchanges required specialized technical capabilities
- **Temporary disruption:** Despite the operation's success, darknet marketplaces reconstituted within months, and AlphaBay itself relaunched in 2021

## Lessons Learned

1. **OPSEC failures remain the primary identification vector:** Cazes was identified through a reused personal email address -- even sophisticated administrators make basic security mistakes
2. **Coordinated multi-market takedowns maximize impact:** The double-sting approach exploited predictable user migration behavior, dramatically increasing intelligence yield compared to isolated takedowns
3. **Covert marketplace operation is operationally feasible:** Dutch police demonstrated that law enforcement can successfully impersonate marketplace administrators for extended periods without detection
4. **International cooperation across diverse legal traditions is achievable:** Despite the complexity of coordinating across US, EU, and Thai legal systems, the operation succeeded through a combination of formal MLATs and informal police-to-police cooperation
5. **Asset seizure is a key disruption vector:** The seizure of $30+ million in assets -- particularly cryptocurrency and luxury property -- demonstrates the importance of financial investigation in darknet operations
6. **Permanence remains elusive:** AlphaBay's 2021 relaunch by a different administrator highlights that marketplace disruption is temporary without ongoing enforcement pressure

## Korean Involvement (한국의 참여)

South Korea was **not among the participating countries** in Operation Bayonet. However, the operation has relevance for Korean law enforcement:

- **Darknet marketplace use in Korea:** Korean nationals have been identified as users and vendors on international darknet marketplaces, though the extent of Korean AlphaBay participation is not publicly documented
- **Operational template:** The cooperation model between US, European, and Thai authorities demonstrated in Operation Bayonet provides a precedent for similar cross-jurisdictional operations involving Asian countries
- **Thai cooperation precedent:** The successful arrest of a Canadian suspect in [[thailand|Thailand]] on behalf of the US demonstrates the feasibility of law enforcement cooperation in Southeast Asia, relevant to Korean investigations that require arrests in the region (cf. [[korea-cambodia-scam-repatriation]])
- **Drug trafficking nexus:** AlphaBay facilitated international drug trafficking that *likely* had supply chain connections to the Asia-Pacific region

> [!note]
> No Korean law enforcement agency has publicly reported participation in Operation Bayonet or follow-up investigations. Korea's engagement with darknet marketplace enforcement has been primarily through INTERPOL-coordinated operations.

## Contradictions & Open Questions

1. **Cazes' death:** Cazes' death was ruled a suicide by Thai authorities. No public contradictions to this finding have been credibly reported, but the circumstances -- death in custody before extradition -- have generated speculation. The suicide finding is assessed as *likely* accurate based on official Thai forensic examination.

2. **User/vendor count estimates:** FBI cited 200,000 users and 40,000 vendors; some sources cite 400,000 users. The discrepancy *likely* reflects the difference between active and registered accounts. The DOJ's 200,000 figure may reflect active users, while 400,000 includes dormant accounts.

3. **Total transaction value:** Estimates range from "hundreds of millions" (DOJ) to "$1 billion" (various media). The $1 billion figure *likely* refers to cumulative lifetime transaction volume in cryptocurrency, while lower estimates may refer to specific time periods.

4. **Legal authority for covert marketplace operation:** The legal basis under which Dutch police operated Hansa -- effectively facilitating 27,000 illegal transactions -- has not been publicly challenged in court but raises unresolved questions about the boundaries of undercover operations in the digital domain.

5. **AlphaBay relaunch (2021):** A new AlphaBay launched in August 2021 by "DeSnake" (self-described original co-founder and security administrator). The relationship between DeSnake and the original operation remains an open question for law enforcement.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2017-07-20: Massive blow to criminal Dark Web activities after globally coordinated operation.
- US Department of Justice (Office of Public Affairs), 2017-07-20: AlphaBay, the Largest Online 'Dark Market,' Shut Down.
- US Drug Enforcement Administration, 2017-07-20: AlphaBay, Largest Online 'Dark Market,' Shut Down.
- US Federal Bureau of Investigation, 2017-07-20: AlphaBay Takedown.
- UN Office on Drugs and Crime (UNODC), --: True Crime Story: AlphaBay.

## Evidence and Attribution Notes

- AlphaBay had 200,000+ users and 40,000 vendors; over USD 1 billion transacted since 2014.
- Main suspect arrested in Thailand; two Hansa administrators arrested in Germany.
- Servers seized in Canada, Netherlands, Germany, and Lithuania; millions in cryptocurrencies frozen.
- DOJ official announcement of AlphaBay takedown, July 20, 2017.
- Alexandre Cazes identified as administrator; arrested in Thailand on 5 July 2017.
- Civil forfeiture action filed in US District Court, Eastern District of California.
- Operation Bayonet was a multinational law enforcement operation that dismantled **AlphaBay** and **Hansa** -- the world's two largest darknet marketplaces -- in **July 2017**.
- The operation was led by the FBI and the US Drug Enforcement Administration (DEA) for the AlphaBay component, while the Dutch National Police (NHTCU) led the Hansa component, with Europol coordinating the overall strategy.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| [1] | Massive blow to criminal Dark Web activities after globally coordinated operation | Europol | 2017-07-20 | [link](https://www.europol.europa.eu/media-press/newsroom/news/massive-blow-to-criminal-dark-web-activities-after-globally-coordinated-operation) |
| [2] | AlphaBay, the Largest Online 'Dark Market,' Shut Down | US DOJ | 2017-07-20 | [link](https://www.justice.gov/opa/pr/alphabay-largest-online-dark-market-shut-down) |
| [3] | AlphaBay, Largest Online 'Dark Market,' Shut Down | DEA | 2017-07-20 | [link](https://www.dea.gov/press-releases/2017/07/20/alphabay-largest-online-dark-market-shut-down) |
| [4] | AlphaBay Takedown | FBI | 2017-07-20 | [link](https://www.fbi.gov/news/stories/alphabay-takedown) |
| [5] | True Crime Story: AlphaBay | UNODC | -- | [link](https://www.unodc.org/unodc/untoc20/truecrimestories/alphabay.html) |
