---
type: operation
title: "TrickBot Botnet Disruption"
aliases:
  - "TrickBot Takedown"
  - "TrickBot Disruption Operation"
case_id: "CYB-2020-003"
period: 2
operation_type: "takedown"
status: "completed"
enforcement_type:
  - takedown
  - seizure
  - indictment
  - arrest
outcome: "partial"
timeframe:
  announced: "2020-10-12"
  start: "2020-10-01"
  end: "2022-02-01"
  ongoing: false
crime_type: "[[ransomware-ic|Ransomware]]"
target_entity: "TrickBot botnet infrastructure"
lead_agency: "[[us-doj|U.S. Department of Justice]]"
coordinating_body: "[[us-doj|U.S. Department of Justice]]"
participating_countries:
  - "[[united-states|United States]]"
  - "[[south-korea|South Korea]]"
participating_agencies:
  - "[[us-doj|U.S. Department of Justice]]"
  - "[[fbi-cyber-division|FBI Cyber Division]]"
  - "[[us-secret-service|U.S. Secret Service]]"
legal_basis:
  - "Computer Fraud and Abuse Act (18 U.S.C. § 1030)"
  - "Wire Fraud (18 U.S.C. § 1343)"
  - "Identity Theft (18 U.S.C. § 1028A)"
  - "Lanham Act (trademark infringement — Microsoft's civil action)"
mechanisms_used:
  - "[[public-private-cooperation|Public-Private Cooperation]]"
  - "[[mutual-legal-assistance|Mutual Legal Assistance]]"
results:
  arrests: 2
  indictments: 9
  servers_seized: 120
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "120 of 128 identified C2 servers disabled within first week"
    - "TrickBot operators forced to rebuild infrastructure"
    - "Vladimir Dunaev arrested in South Korea (Sep 2021), extradited to US"
    - "Alla Witte arrested in Miami (Feb 2021)"
    - "9 Russian nationals indicted (Sep 2023) for TrickBot and Conti conspiracies"
    - "Dunaev sentenced to 64 months (Jan 2024)"
edges:
  - source_actor: "Microsoft"
    target_actor: "US DOJ"
    cooperation_type: "joint_investigation"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "US Cyber Command"
    target_actor: "Microsoft"
    cooperation_type: "technical_assistance"
    legal_basis: "informal"
    direction: "undirected"
  - source_actor: "US DOJ"
    target_actor: "South Korea"
    cooperation_type: "extradition"
    legal_basis: "MLAT"
    direction: "directed"
credibility_index: 4.5
source_tier: 1
missing_fields: []
related_cases:
  - "[[us-v-galochkin-trickbot-conti]]"
related_operations:
  - "[[emotet-takedown|Emotet Takedown]]"
challenges_encountered:
  - "[[jurisdictional-conflicts|Jurisdictional Conflicts]]"
lessons_learned:
  - "Public-private partnerships can accelerate botnet disruption through combined legal and technical capabilities"
  - "Military cyber capabilities (Cyber Command) can complement civilian law enforcement operations"
  - "Botnet disruption is rarely permanent; sustained pressure and follow-on prosecutions are required"
  - "International arrest cooperation (South Korea extradition) demonstrates global reach of US cybercrime enforcement"
source_count: 5
sources:
  - "[Microsoft Blog — New action to combat ransomware (2020-10-12)](https://blogs.microsoft.com/on-the-issues/2020/10/12/trickbot-ransomware-cyberthreat-us-elections/)"
  - "[Microsoft Blog — Update on disruption (2020-10-20)](https://blogs.microsoft.com/on-the-issues/2020/10/20/trickbot-ransomware-disruption-update/)"
  - "[CyberScoop — Cyber Command, Microsoft take action (2020-10-12)](https://cyberscoop.com/trickbot-takedown-cyber-command-microsoft/)"
  - "[DOJ — Multiple Foreign Nationals Charged (2023-09-07)](https://www.secretservice.gov/newsroom/releases/2023/09/multiple-foreign-nationals-charged-connection-trickbot-malware-and-conti)"
  - "[BleepingComputer — Dunaev sentenced (2024-01)](https://www.bleepingcomputer.com/news/security/russian-trickbot-malware-dev-sentenced-to-64-months-in-prison/)"
created: 2026-04-10
updated: 2026-04-12
---

## Summary

The TrickBot disruption was a multi-pronged effort in October 2020 involving both U.S. military cyber operations and a private-sector-led legal action to disable one of the world's largest and most persistent botnets. U.S. Cyber Command conducted offensive operations to interfere with TrickBot's command-and-control (C2) infrastructure, while Microsoft, acting under a court order from the U.S. District Court for the Eastern District of Virginia, took down 120 of 128 identified TrickBot servers in the first week. The urgency was driven by concerns that TrickBot-deployed ransomware could disrupt U.S. election infrastructure ahead of the November 2020 presidential election. While the initial disruption was temporary — TrickBot operators eventually rebuilt portions of their infrastructure — the operation was followed by a sustained law enforcement campaign that produced arrests and indictments through 2024, including the arrest of developer Vladimir Dunaev in [[south-korea|South Korea]] and the indictment of nine Russian nationals.

## Background

### What Was TrickBot

TrickBot was a modular banking trojan that first appeared in 2016 as a successor to the Dyre banking trojan. Initially designed to steal financial credentials, it evolved into a versatile malware platform used for:

- **Credential theft**: banking credentials, email accounts, cryptocurrency wallets
- **Ransomware delivery**: served as the primary delivery mechanism for Ryuk and later Conti ransomware
- **Network reconnaissance**: lateral movement tools for enterprise network compromise
- **Data exfiltration**: sensitive data harvesting from compromised organizations

At its peak, TrickBot controlled an estimated 1-3 million infected devices worldwide, operated by a Russian-speaking criminal group. The botnet's victims included hospitals, schools, businesses, and government entities, with tens of millions of dollars in losses.

### Election Security Concern

In October 2020, U.S. government officials assessed that TrickBot posed a potential threat to election infrastructure. The concern was that TrickBot-deployed ransomware could lock election-related IT systems (voter registration databases, county government networks) in the weeks before the November 3, 2020 presidential election. This assessment provided the impetus for the accelerated disruption timeline.

### Dual Operations

Unusually, two separate entities — U.S. Cyber Command and Microsoft — pursued independent but complementary disruption campaigns:

1. **U.S. Cyber Command**: conducted offensive cyber operations to directly interfere with TrickBot's C2 communications, sending commands to infected devices to sever their connection to the botnet
2. **Microsoft (civil action)**: filed a lawsuit and obtained a court order to seize TrickBot C2 infrastructure through ISP cooperation

The two efforts were described as "distinct" by officials, though they were aware of each other and likely benefited from deconfliction.

## Participating Parties

### U.S. Government
- **U.S. Cyber Command** — conducted offensive cyber operations against TrickBot C2 infrastructure
- **[[fbi-cyber-division|FBI Cyber Division]]** — criminal investigation and subsequent arrests
- **[[us-doj|U.S. Department of Justice]]** — prosecution through three federal districts (Northern District of Ohio, Middle District of Tennessee, Southern District of California)
- **[[us-secret-service|U.S. Secret Service]]** — investigation support

### Private Sector Coalition (Microsoft-led)
| Partner | Role |
|---------|------|
| Microsoft Digital Crimes Unit | Legal action, C2 server takedown |
| FS-ISAC (Financial Services ISAC) | Co-plaintiff, financial sector intelligence |
| ESET | Threat intelligence, technical analysis |
| Lumen (Black Lotus Labs) | C2 infrastructure mapping |
| NTT | Technical analysis |
| Symantec (Broadcom) | Threat intelligence |

### International Cooperation (Post-Disruption Phase)
- **[[south-korea|South Korea]]** — arrested Vladimir Dunaev in September 2021 and extradited him to the United States

## Legal Framework

The TrickBot disruption relied on an unusual combination of legal authorities:

### Microsoft's Civil Action
- **Lanham Act (trademark)**: Microsoft argued that TrickBot operators misused Microsoft's trademarks by corrupting Microsoft products on infected computers, enabling a civil trademark claim
- **U.S. District Court for the Eastern District of Virginia**: granted the court order authorizing Microsoft to disable C2 IP addresses, render server content inaccessible, and block operators from acquiring new servers

### Criminal Prosecution
- **Computer Fraud and Abuse Act (18 U.S.C. § 1030)**: primary federal cybercrime statute
- **Wire Fraud (18 U.S.C. § 1343)**: covering financial fraud conducted through the botnet
- **Aggravated Identity Theft (18 U.S.C. § 1028A)**: for theft of personal information

### Military Authority
- U.S. Cyber Command's authority to conduct offensive cyber operations derives from Title 10 and specific cyber operations authorities granted by the Secretary of Defense. The precise legal basis for the TrickBot operation has not been publicly disclosed.

## Operational Timeline

| Date | Event |
|------|-------|
| 2016 | TrickBot first observed in the wild |
| 2018-2019 | TrickBot becomes one of the world's largest botnets; Ryuk ransomware delivery begins |
| 2020-10-01 (approx.) | U.S. Cyber Command begins offensive operations against TrickBot C2 infrastructure |
| 2020-10-12 | Microsoft announces civil action; court order obtained from E.D. Virginia |
| 2020-10-12 to 10-18 | 120 of 128 identified TrickBot C2 servers disabled |
| 2020-10-20 | Microsoft reports TrickBot operators' focus shifted to rebuilding rather than attacking |
| 2020-11-03 | U.S. presidential election proceeds without TrickBot-related disruption |
| 2021-02 | Alla Witte (Latvian national) arrested in Miami, charged with TrickBot-related offenses |
| 2021-09 | Vladimir Dunaev arrested in [[south-korea\|South Korea]] |
| 2021-10 | Dunaev extradited to the United States |
| 2022 (early) | TrickBot infrastructure effectively dismantled; operators transition to other malware |
| 2023-06 | Witte pleads guilty, sentenced to 32 months |
| 2023-09-07 | DOJ unseals three indictments charging 9 Russian nationals (including Maksim Galochkin) with TrickBot and Conti conspiracies |
| 2023-11-30 | Dunaev pleads guilty to conspiracy charges |
| 2024-01 | Dunaev sentenced to 64 months in prison |

## Results and Impact

### Immediate Disruption (October 2020)
- **120 of 128 C2 servers** disabled within the first week
- TrickBot operators forced to prioritize infrastructure rebuilding over launching new attacks
- No TrickBot-related ransomware disruption of U.S. election infrastructure

### Limitations
- TrickBot operators gradually rebuilt portions of their infrastructure in the weeks following the disruption
- Security researchers (e.g., Intel 471) assessed the disruption would have only "short-term impact"
- The botnet was not permanently destroyed by the October 2020 operation alone

### Long-Term Prosecution Results (2021-2024)
- **Alla Witte**: Latvian national, arrested in Miami (February 2021), pleaded guilty (June 2023), sentenced to 32 months
- **Vladimir Dunaev**: Russian national, arrested in [[south-korea|South Korea]] (September 2021), extradited to U.S., pleaded guilty (November 2023), sentenced to 64 months
- **9 Russian nationals indicted** (September 2023): Maksim Galochkin, Mikhail Tsarev, Andrey Zhuykov, Dmitry Putilin, Sergey Loguntsov, Max Mikhailov, Valentin Karyagin, Maksim Rudenskiy, and Galochkin — charged in three federal districts for TrickBot and Conti ransomware conspiracies
- Maximum penalties: up to 35 years (Dunaev charges), up to 25 years (Conti conspiracy charges)

### TrickBot's End
By early 2022, TrickBot's operators effectively abandoned the botnet, transitioning to other malware platforms (notably BazarLoader/BazarBackdoor and eventually Conti ransomware operations). The combined pressure of the 2020 disruption, ongoing investigations, and the leak of Conti internal communications ("Conti Leaks," February 2022) contributed to the group's fragmentation.

## Cooperation Mechanisms Used

1. **[[public-private-cooperation|Public-Private Cooperation]]** — the defining feature of this operation. Microsoft's civil legal authority (trademark law) was used alongside government criminal and military cyber authorities, creating a multi-vector disruption strategy.
2. **Industry threat intelligence sharing** — ESET, Lumen, NTT, and Symantec provided technical intelligence that informed both the court filing and the operational targeting.
3. **[[mutual-legal-assistance|Mutual Legal Assistance]]** — formal MLA process used for Dunaev's arrest in South Korea and extradition to the United States.
4. **Civil court orders for infrastructure takedown** — Microsoft's novel use of trademark law to obtain server takedown orders has been replicated in subsequent botnet disruptions.

## Challenges and Friction Points

- **Temporary disruption only**: The October 2020 operation did not permanently disable TrickBot. Botnet operators rebuilt infrastructure within weeks, though at reduced capacity. This highlights the inherent limitation of technical disruption without simultaneously arresting operators.
- **Dual-track coordination**: U.S. Cyber Command and Microsoft pursued separate operations that required deconfliction to avoid interfering with each other. The exact coordination mechanism has not been publicly described.
- **Attribution to prosecution gap**: While the botnet's Russian-speaking operators were identified relatively quickly, converting attribution into arrests required years and depended on operators traveling to countries with U.S. extradition treaties (South Korea, in Dunaev's case).
- **Legal authority questions**: The use of military cyber capabilities (Cyber Command) for what is essentially a criminal matter raised questions about the appropriate legal authorities and the boundary between military and law enforcement operations.

## Lessons Learned

1. **Public-private partnerships expand the legal toolkit**: Microsoft's use of civil trademark law provided a faster path to server takedowns than criminal process alone. This model has been adopted in subsequent operations (e.g., [[emotet-takedown|Emotet]], ZLoader).
2. **Technical disruption requires follow-on prosecution**: The October 2020 disruption bought time (protecting the election) but did not eliminate TrickBot. Only the sustained prosecution campaign (2021-2024) produced lasting consequences for operators.
3. **International arrest cooperation extends enforcement reach**: Dunaev's arrest in South Korea demonstrates that cybercriminals are vulnerable when they travel to countries with strong law enforcement cooperation with the United States.
4. **Election security provides political urgency**: The election security framing accelerated both government and private sector action, demonstrating that clear threat narratives can mobilize resources.

## Korean Involvement (한국의 참여)

[[south-korea|South Korea]] played a direct and significant role in the TrickBot prosecution:

- **Arrest of Vladimir Dunaev**: In September 2021, South Korean authorities arrested Dunaev, a Russian national, at the request of the United States. Dunaev was a TrickBot developer who had traveled to South Korea.
- **Extradition to the United States**: Dunaev was extradited to the United States in October 2021 to face charges in the Northern District of Ohio.
- **Outcome**: Dunaev pleaded guilty in November 2023 and was sentenced to 64 months in prison in January 2024.

This arrest and extradition demonstrate South Korea's capacity and willingness to cooperate in international cybercrime enforcement, even for cases where the criminal activity did not directly target Korean interests. It is a notable example of [[south-korea|Korea's]] role as a reliable partner in the global cybercrime enforcement network.

## Contradictions & Open Questions

- **Cyber Command legal authority**: The precise legal basis for U.S. Cyber Command's offensive operations against TrickBot has not been publicly disclosed. Whether this was conducted under Title 10 military authority, an intelligence authority, or a specific cyber operations authorization remains unclear.
- **Coordination between Cyber Command and Microsoft**: While officials described the operations as "distinct," the degree of coordination and deconfliction between the two efforts is not publicly documented.
- **Short-term vs. long-term effectiveness**: Intel 471 and other researchers assessed the initial disruption as having only "short-term impact." The long-term effectiveness argument rests on the subsequent prosecution campaign, which took years to materialize.
- **Remaining fugitives**: Of the 9 indicted Russian nationals, most remain at large in Russia, where they are unlikely to be extradited. The practical enforcement impact is limited to travel restrictions and asset seizures.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | New action to combat ransomware ahead of U.S. elections | Microsoft | 2020-10-12 | [Link](https://blogs.microsoft.com/on-the-issues/2020/10/12/trickbot-ransomware-cyberthreat-us-elections/) |
| 2 | An update on disruption of Trickbot | Microsoft | 2020-10-20 | [Link](https://blogs.microsoft.com/on-the-issues/2020/10/20/trickbot-ransomware-disruption-update/) |
| 3 | Cyber Command, Microsoft take action against Trickbot | CyberScoop | 2020-10-12 | [Link](https://cyberscoop.com/trickbot-takedown-cyber-command-microsoft/) |
| 4 | Multiple Foreign Nationals Charged in Connection with Trickbot and Conti | U.S. Secret Service / DOJ | 2023-09-07 | [Link](https://www.secretservice.gov/newsroom/releases/2023/09/multiple-foreign-nationals-charged-connection-trickbot-malware-and-conti) |
| 5 | Russian TrickBot malware dev sentenced to 64 months in prison | BleepingComputer | 2024-01 | [Link](https://www.bleepingcomputer.com/news/security/russian-trickbot-malware-dev-sentenced-to-64-months-in-prison/) |
