---
type: operation
title: "Dridex/Evil Corp Disruption and Prosecution"
aliases:
  - "Dridex Takedown"
  - "Bugat Botnet Takedown"
  - "Evil Corp Sanctions"
  - "Cridex Disruption"
case_id: CYB-2015-007
period: 1
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - indictment
  - takedown
  - extradition
  - asset_freeze
outcome: partial
timeframe:
  announced: 2015-10-13
  start: 2015-08
  end: 2019-12-05
  ongoing: false
crime_type: "[[online-fraud-ic|Banking Trojan Fraud]]"
target_entity: "Evil Corp cybercriminal organization; Dridex/Bugat/Cridex banking trojan operators"
lead_agency: "[[fbi-cyber-division|FBI Cyber Division (Pittsburgh Field Office)]]"
coordinating_body: "[[europol-ec3|Europol EC3]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[germany]]"
  - Moldova
  - Cyprus
participating_agencies:
  - "[[fbi-cyber-division|FBI Cyber Division]]"
  - "[[uk-nca|UK National Crime Agency (NCA)]]"
  - "[[us-doj|US Department of Justice]]"
  - "[[us-treasury|US Treasury Department (OFAC)]]"
  - "[[europol-ec3|Europol EC3]]"
  - "[[germany-bka|Germany BKA]]"
legal_basis:
  - "[[mlat-process|US-UK MLAT]]"
  - "[[mlat-process|US-Moldova MLAT]]"
  - "US Computer Fraud and Abuse Act (18 U.S.C. SS 1030)"
  - "US Wire Fraud statute (18 U.S.C. SS 1343)"
  - "US Bank Fraud statute (18 U.S.C. SS 1344)"
  - "International Emergency Economic Powers Act (IEEPA) -- OFAC sanctions"
mechanisms_used:
  - "[[mlat-process|MLAT]]"
  - "FBI-NCA bilateral cooperation"
  - "Botnet sinkholing (technical disruption)"
  - "OFAC sanctions (asset freeze)"
results:
  arrests: 1
  indictments: 3
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Dridex botnet sinkholed via P2P network poisoning (October 2015)"
    - "Andrey Ghinkul arrested in Cyprus (August 2015), extradited to US (February 2016), sentenced to time served (December 2018)"
    - "Maksim Yakubets and Igor Turashev indicted (December 2019)"
    - "$5 million reward offered for Yakubets -- largest cyber reward at time of announcement"
    - "OFAC sanctions against 17 individuals and 7 entities associated with Evil Corp"
    - "Over $100 million in estimated theft from victims in 40+ countries"
    - "Estimated $10 million in direct US losses, GBP 20 million in UK losses"
edges:
  - source_actor: FBI
    target_actor: "UK NCA"
    cooperation_type: joint_investigation
    legal_basis: MLAT
    direction: undirected
  - source_actor: FBI
    target_actor: "Dell SecureWorks"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
  - source_actor: "UK NCA"
    target_actor: "Shadowserver Foundation"
    cooperation_type: technical_assistance
    legal_basis: informal
    direction: undirected
  - source_actor: "US DOJ"
    target_actor: Moldova
    cooperation_type: extradition
    legal_basis: MLAT
    direction: directed
  - source_actor: "US Treasury OFAC"
    target_actor: "Evil Corp"
    cooperation_type: asset_recovery
    legal_basis: IEEPA
    direction: directed
  - source_actor: "Europol EC3"
    target_actor: FBI
    cooperation_type: info_sharing
    legal_basis: Budapest_Convention
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:

related_cases:
  - "[[us-v-yakubets-dridex]]"
  - "[[us-v-ghinkul-dridex|United States v. Ghinkul (Bugat/Dridex)]]"
  - "[[us-v-ghinkul-dridex]]"
related_operations:
  - "[[goznym-takedown|GozNym Takedown]]"
  - "[[zeus-spyeye-takedown|Zeus/SpyEye Takedown]]"
  - "[[operation-avalanche|Operation Avalanche]]"
  - "[[operation-us-v-ghinkul-dridex]]"
challenges_encountered:
  - "[[data-sovereignty]]"
lessons_learned:
  - "Combined legal-technical disruption (indictment + sinkholing) is more effective than either alone; sinkholing without arrests allows rebuilding"
  - "International extradition from non-cooperative jurisdictions (Russia) remains the primary barrier to prosecuting state-adjacent cybercriminals"
  - "OFAC sanctions provide an alternative enforcement mechanism when arrest is not feasible, imposing real economic costs on cybercriminal organizations"
  - "Public-private partnership with cybersecurity firms (Dell SecureWorks, Fox-IT, Shadowserver) is essential for the technical disruption component"
  - "FBI-NCA bilateral cooperation is a model for US-UK cybercrime investigations"
source_count: 8
sources:
  - "[1] DOJ: "Bugat Botnet Administrator Arrested and Malware Disabled (2015-10-13)\""
  - "[2] FBI: "Bugat Botnet Administrator Arrested (2015-10-13)\""
  - "[3] DOJ: "Russian National Charged with Decade-Long Series of Hacking (2019-12-05)\""
  - "[4] US Treasury: "Sanctions Evil Corp (2019-12-05)\""
  - "[5] NCA: "International law enforcement operation exposes the world's most harmful cyber crime group (2019-12-05)\""
  - "[6] DOJ: "Moldovan Sentenced for Distributing Multifunction Malware Package (2018-12-06)\""
  - "[7] The Hacker News: "FBI Puts $5 Million Bounty (2019-12-05)\""
  - "[8] Dell SecureWorks: "Dridex (Bugat v5) Botnet Takeover Operation (2015-10)\""
created: 2026-04-10
updated: 2026-04-17
operation_role: umbrella
parent_operation: ""
---
## Summary

The Dridex/Evil Corp disruption and prosecution was a **multi-year international law enforcement operation** targeting the Dridex banking trojan (also known as Bugat and Cridex) and its operators within the Russia-based cybercriminal organization **Evil Corp**. The operation unfolded in two major phases: (1) the **October 2015 technical disruption and arrest** of botnet administrator Andrey Ghinkul, conducted jointly by the [[fbi-cyber-division|FBI]] and [[uk-nca|UK National Crime Agency (NCA)]]; and (2) the **December 2019 indictment, sanctions, and reward** targeting Evil Corp leader **Maksim Yakubets** and deputy **Igor Turashev**, coordinated between the [[us-doj|US DOJ]], [[us-treasury|US Treasury (OFAC)]], and NCA.

The Dridex malware infected computers in over **40 countries** and caused more than **USD 100 million** in theft from banks and financial institutions. The operation is significant for international cooperation because it combined **technical disruption** (botnet sinkholing via public-private partnership), **criminal prosecution** (indictment and extradition), and **financial sanctions** (OFAC designation) -- a three-pronged approach that became a template for subsequent banking trojan operations.

The outcome is assessed as **partial success**: one defendant was arrested, extradited, and sentenced, and the botnet was temporarily disrupted; however, the principal targets (Yakubets and Turashev) remain at large in Russia, and Evil Corp subsequently pivoted to ransomware operations.

## Background

### The Dridex Malware

Dridex (originally known as Bugat v5, and earlier as Cridex) is a banking trojan that spreads primarily through phishing emails containing malicious Microsoft Office documents with macro payloads. Once installed, the malware steals online banking credentials and enables fraudulent wire transfers. The malware evolved through several versions:

- **Cridex** (2011-2012): Initial version targeting banking credentials
- **Bugat v4** (2012-2014): Enhanced version with modular architecture
- **Dridex/Bugat v5** (2014-present): Peer-to-peer (P2P) botnet architecture making takedown more difficult

### Evil Corp

Evil Corp is a Russia-based cybercriminal group led by **Maksim V. Yakubets** (aka "aqua"), operating primarily from Moscow. The group developed and deployed the Dridex malware at scale, maintaining a sophisticated criminal enterprise that infected hundreds of thousands of computers worldwide. According to the US Treasury, Yakubets also **provided direct assistance to the Russian government's malicious cyber efforts**, highlighting the nexus between state-sponsored and criminal cyber operations.

## Participating Parties

**Law Enforcement:**
- [[fbi-cyber-division|FBI Cyber Division]] (Pittsburgh Field Office) -- lead US investigative agency
- [[uk-nca|UK National Crime Agency (NCA)]] -- lead UK investigative agency, conducted sinkholing
- [[us-doj|US Department of Justice]] (Western District of Pennsylvania, District of Nebraska) -- prosecution
- [[us-treasury|US Treasury Department, OFAC]] -- sanctions and asset freezing
- [[europol-ec3|Europol EC3]] and J-CAT -- coordination and intelligence sharing
- [[germany-bka|Germany BKA]] -- investigation support
- UK GCHQ -- intelligence support
- London Metropolitan Police -- investigation support
- Moldova law enforcement -- arrest assistance

**Private Sector Partners:**
- **Dell SecureWorks** (Counter Threat Unit) -- developed and executed botnet sinkholing strategy
- **Fox-IT** -- technical analysis and disruption support
- **Shadowserver Foundation** -- sinkhole infrastructure
- **S21sec** -- malware analysis
- **Abuse.ch** -- threat intelligence
- **Spamhaus** -- spam and botnet tracking

## Legal Framework

### Criminal Charges

**Against Andrey Ghinkul (W.D. Pa.):**
Nine-count indictment: criminal conspiracy, unauthorized computer access with intent to defraud, damaging a computer, wire fraud, and bank fraud under 18 U.S.C. SS 1030 (CFAA), 18 U.S.C. SS 1343 (wire fraud), and 18 U.S.C. SS 1344 (bank fraud).

**Against Maksim V. Yakubets (W.D. Pa., D. Neb.):**
Charges related to a "decade-long series of hacking and bank fraud offenses resulting in tens of millions of dollars in losses." Charges included conspiracy, computer fraud, wire fraud, and bank fraud. Yakubets was charged in two separate indictments in different districts.

**Against Igor Turashev:**
Charged alongside Yakubets for his role as an administrator of the Dridex malware.

### Sanctions

On 5 December 2019, OFAC designated **17 individuals and 7 entities** associated with Evil Corp under the International Emergency Economic Powers Act (IEEPA), freezing all US-jurisdictional assets and prohibiting US persons from transacting with them.

### Reward

The US State Department announced a reward of up to **USD 5 million** under the Transnational Organized Crime Rewards Program for information leading to Yakubets' arrest and/or conviction -- the **largest such reward for a cybercriminal** at the time.

## Operational Timeline

- **2011-12-16**: Ghinkul allegedly attempted electronic transfer of $999,000 from Sharon, Pennsylvania City School District's account at First National Bank to an account in Kiev, Ukraine, using phishing-obtained credentials
- **2012-2014**: Bugat/Cridex evolves into Dridex with P2P botnet architecture
- **2015-08 (early August)**: Andrey Ghinkul (aka Andrei Ghincul, "Smilex"), 30, of Moldova, **arrested in Cyprus** based on US warrant
- **2015-10-13**: **Coordinated disruption announced**: FBI and NCA publicly announce Dridex botnet sinkholing and Ghinkul's indictment. Dell SecureWorks, working with FBI, NCA, and Shadowserver Foundation, poisons each sub-botnet's P2P network and redirects infected systems to a sinkhole controlled by law enforcement
- **2015-10-13**: DOJ unseals nine-count indictment against Ghinkul in the Western District of Pennsylvania
- **2016-02**: Ghinkul **extradited from Cyprus to the United States**
- **2017-02**: Ghinkul pleads guilty to conspiracy charges in W.D. Pa.
- **2018-12-06**: Ghinkul **sentenced to time served** by US District Judge Bissoon (W.D. Pa.), having spent approximately 3+ years in custody since arrest
- **2019-12-05**: **Coordinated second phase**: DOJ unseals indictments against Maksim V. Yakubets and Igor Turashev; US Treasury OFAC sanctions 17 individuals and 7 Evil Corp entities; State Department announces $5 million reward; NCA publishes detailed intelligence on Evil Corp's structure and operations
- **2019-12-05**: NCA reveals Yakubets' connection to Russian state intelligence services

## Results and Impact

### Quantitative Results

| Metric | Result |
|--------|--------|
| Arrests | 1 (Ghinkul, Cyprus, August 2015) |
| Extraditions | 1 (Ghinkul, Cyprus to US, February 2016) |
| Convictions/Sentences | 1 (Ghinkul, time served, December 2018) |
| Indictments (at large) | 2 (Yakubets, Turashev) |
| OFAC sanctions | 17 individuals, 7 entities |
| Reward offered | USD 5 million (Yakubets) |
| Estimated victim losses | USD 100M+ globally; $10M US; GBP 20M UK |
| Countries affected | 40+ |

### Technical Disruption

The October 2015 sinkholing operation, executed by Dell SecureWorks CTU researchers in collaboration with FBI, NCA, and the Shadowserver Foundation, **poisoned each Dridex sub-botnet's P2P network** and redirected infected systems to law enforcement-controlled sinkholes. This temporarily disrupted the botnet's command-and-control infrastructure and prevented operators from issuing new commands to infected machines.

However, the disruption was **temporary**. Evil Corp subsequently rebuilt the Dridex infrastructure and pivoted to ransomware operations (WastedLocker, Hades, Phoenix), demonstrating the limitations of technical disruption without the arrest of principal operators.

### Sanctions Impact

The OFAC sanctions against Evil Corp had a significant follow-on effect: they created legal risk for any organization (including ransomware victims and their intermediaries) that paid ransom to Evil Corp affiliates, as such payment could constitute a sanctions violation. This effectively **weaponized sanctions as a deterrent against ransomware payments** -- a mechanism later used against other cybercriminal groups.

## Cooperation Mechanisms Used

1. **[[mlat-process|Mutual Legal Assistance Treaty (MLAT)]]** -- Formal evidence exchange between US-UK and US-Moldova for indictment, arrest, and extradition
2. **FBI-NCA Bilateral Cooperation** -- Close bilateral partnership between the two agencies, with NCA conducting UK-side sinkholing while FBI managed US-side technical operations
3. **Europol EC3 / J-CAT** -- Intelligence coordination and information sharing hub
4. **Public-Private Partnership** -- Dell SecureWorks, Fox-IT, Shadowserver Foundation, and others provided critical technical capabilities for botnet sinkholing that law enforcement alone could not execute
5. **OFAC Sanctions** -- Treasury Department financial sanctions as an alternative enforcement mechanism when arrest is not feasible
6. **Extradition (Cyprus to US)** -- Ghinkul's extradition from Cyprus demonstrated the viability of arresting cybercriminals transiting through cooperative jurisdictions
7. **State Department Reward Program** -- Transnational Organized Crime Rewards Program used to incentivize intelligence on Yakubets' location

## Challenges and Friction Points

- **Russian non-cooperation**: Yakubets and Turashev remain in Russia, which does not extradite its nationals and has not acted on US indictments. Russia's refusal to cooperate is the primary barrier to prosecution of the principal defendants
- **State-criminal nexus**: The NCA and Treasury revelations that Yakubets **provided direct assistance to Russian government cyber efforts** highlighted the challenge of pursuing cybercriminals who enjoy state protection
- **Temporary technical disruption**: The Dridex botnet was rebuilt after sinkholing, demonstrating that technical disruption without arrests provides only temporary relief
- **Evolution to ransomware**: Evil Corp's pivot from banking trojans to ransomware (WastedLocker, Hades, Phoenix, Macaw Locker) showed the group's adaptability and the limitations of disrupting one malware family
- **Sanctions compliance complexity**: OFAC sanctions against Evil Corp created compliance challenges for ransomware victims and incident response firms navigating whether payment would violate sanctions

## Lessons Learned

1. **Three-pronged approach (prosecution + technical disruption + sanctions)** is more effective than any single mechanism, but still insufficient when principal targets enjoy state protection in non-cooperative jurisdictions
2. **Public-private partnership is essential for technical operations**: Law enforcement lacks the deep technical expertise to execute botnet sinkholing alone; cybersecurity firms like Dell SecureWorks and Shadowserver are indispensable partners
3. **Extradition via transit countries works**: Ghinkul's arrest in Cyprus while transiting from Moldova demonstrates the value of monitoring travel patterns and leveraging cooperative third-country jurisdictions
4. **OFAC sanctions as cybercrime tool**: The Evil Corp case established sanctions as a viable enforcement mechanism against cybercriminal organizations, later applied to other groups
5. **FBI-NCA bilateral model**: The close US-UK cooperation in this case -- with FBI managing prosecution and NCA managing UK-side technical operations -- became a template for subsequent banking trojan and ransomware operations

## Korean Involvement (한국의 참여)

There is no confirmed direct Korean involvement in the Dridex/Evil Corp operation. However, the case is relevant to Korean interests because:

- Dridex targeted banking credentials in **40+ countries**, and Korean financial institutions were likely among the potential targets
- The OFAC sanctions framework applied to Evil Corp has implications for Korean organizations that may interact with sanctioned entities in ransomware contexts
- The FBI-NCA bilateral cooperation model is analogous to Korean bilateral cooperation frameworks with the US and UK on cybercrime

## Contradictions & Open Questions

1. **Ghinkul's sentence**: DOJ press releases confirm Ghinkul was sentenced to "time served" by Judge Bissoon on approximately 6 December 2018, having spent over 3 years in custody. The specific terms of his plea agreement have not been publicly disclosed. It is unclear whether he provided cooperation that justified the lenient sentence.
2. **Dridex victim losses**: The FBI estimates "$10 million in direct US losses" while the NCA cites "GBP 20 million in UK losses." The USD 100 million global figure is from the Treasury Department. These figures may cover different time periods or methodologies, and the actual total is likely higher given the 40+ countries affected.
3. **Yakubets' Russian government ties**: The NCA and Treasury stated that Yakubets "provides direct assistance to the Russian government's malicious cyber efforts," but the specific nature of this assistance has not been publicly detailed. It is unclear whether Yakubets operates under FSB direction or provides services on a transactional basis.
4. **Evil Corp evolution**: After Dridex, Evil Corp deployed multiple ransomware variants (WastedLocker, Hades, Phoenix, Macaw Locker, potentially LockBit affiliates). Whether subsequent enforcement actions against these ransomware families should be considered extensions of the Dridex operation or separate operations is an open categorization question.

> [!warning] Legal status check needed
> Yakubets and Turashev remain at large as of the last verified date. Their status and the $5 million reward should be verified against current FBI Most Wanted listings.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| [1] | Bugat Botnet Administrator Arrested and Malware Disabled | US DOJ | 2015-10-13 | https://www.justice.gov/opa/pr/bugat-botnet-administrator-arrested-and-malware-disabled |
| [2] | Bugat Botnet Administrator Arrested and Malware Disabled | FBI Pittsburgh | 2015-10-13 | https://www.fbi.gov/contact-us/field-offices/pittsburgh/news/press-releases/bugat-botnet-administrator-arrested-and-malware-disabled |
| [3] | Russian National Charged with Decade-Long Series of Hacking and Bank Fraud | US DOJ | 2019-12-05 | https://www.justice.gov/archives/opa/pr/russian-national-charged-decade-long-series-hacking-and-bank-fraud-offenses-resulting-tens |
| [4] | Treasury Sanctions Evil Corp, the Russia-Based Cybercriminal Group Behind Dridex Malware | US Treasury | 2019-12-05 | https://home.treasury.gov/news/press-releases/sm845 |
| [5] | International law enforcement operation exposes the world's most harmful cyber crime group | NCA | 2019-12-05 | https://nca-newsroom.prgloo.com/news/international-law-enforcement-operation-exposes-the-worlds-most-harmful-cyber-crime-group |
| [6] | Moldovan Sentenced for Distributing Multifunction Malware Package | US DOJ WDPA | 2018-12-06 | https://www.justice.gov/usao-wdpa/pr/moldovan-sentenced-distributing-multifunction-malware-package |
| [7] | Dridex (Bugat v5) Botnet Takeover Operation | Dell SecureWorks (Sophos) | 2015-10 | https://www.sophos.com/en-us/research/dridex-bugat-v5-botnet-takeover-operation |
| [8] | FBI Puts $5 Million Bounty On Russian Hackers Behind Dridex Banking Malware | The Hacker News | 2019-12-05 | https://thehackernews.com/2019/12/dridex-russian-hackers-wanted-by-fbi.html |
