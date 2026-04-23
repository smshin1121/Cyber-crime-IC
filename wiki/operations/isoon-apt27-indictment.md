---
type: operation
title: "i-Soon/APT27 Indictment (Chinese Contract Hackers)"
aliases:
  - "i-Soon Indictment"
  - "APT27 Indictment"
  - "Anxun Indictment"
operation_type: joint-investigation
status: ongoing
case_id: CYB-2025-004
period: 3
enforcement_type:
  - indictment
  - asset_freeze
outcome: ongoing
credibility_index: 2.28
source_tier: 2
edges:
  - source_actor: FBI
    target_actor: "US DOJ"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
  - source_actor: "US Department of State"
    target_actor: "US Treasury"
    cooperation_type: asset_recovery
    legal_basis: unknown
    direction: undirected
missing_fields:
  - legal_basis
  - mechanisms_used
  - international_cooperation_partners
timeframe:
  announced: 2025-03-05
  start: ""
  end: ""
  ongoing: true
crime_type: "[[hacking-ic]]"
target_entity: "i-Soon (Anxun Information Technology Co. Ltd.) and APT27 members"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[china]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
legal_basis:

mechanisms_used:

results:
  arrests: 0
  indictments: 12
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Rewards for Justice offer of up to USD 10 million"
    - "Treasury sanctions imposed"
    - "12 Chinese nationals charged (2 MPS officers, 8 i-Soon employees, APT27 members)"
related_cases:
  - "[[us-v-wu-haibo-isoon]]"
related_operations:
  - "[[operation-us-v-wu-haibo-isoon]]"
challenges_encountered:
  - "All defendants located in China — arrest and extradition highly unlikely"
  - "State-sponsored nature complicates traditional law enforcement cooperation"
lessons_learned:
  - "Indictments and sanctions serve as deterrence and attribution tools even when arrests are not feasible"
  - "Multi-agency coordination (DOJ, FBI, NCIS, State, Treasury) enables comprehensive response combining criminal, diplomatic, and financial tools"
source_count: 6
sources:
  - "[[2025-03-05-doj-isoon-chinese-hackers-charges]]"
  - "[[2025-03-05_opa_wu-haibo-isoon-indictment]]"
  - "[[2025-03-05_wired-com_us-charges-12-alleged-spies-in-chinas-freewheeling-hacker-for-hire-ecosystem]]"
  - "[[2025-03-06_infosecurity-magazine_us-charges-chinese-hackerforhire]]"
  - "[[2025-03-05_bleepingcomputer-com_us-charges-chinese-hackers-linked-to-critical-infrastructure-breaches]]"
  - "[[2025-03-06_thecyberwire-com_us-justice-department-charges-employees-of-chinese-it-contractor-i-soon]]"
created: 2026-04-08
updated: 2026-04-09
operation_role: umbrella
parent_operation: ""
summary: "On 5 March 2025, the US Department of Justice announced charges against **12 Chinese nationals** affiliated with Anxun Information Technology Co. Ltd. (i-Soon) and Advanced Persistent Threat 27 (APT27). The defendants included two officers of China's Ministry of Public Security (MPS), eight i-Soon employees, and APT27 members. These actors conducted computer intrusions at the direction of China's MPS and Ministry of State Security (MSS) as well as on their own initiative."
jurisdictions:
  - "[[united-states]]"
organizations:
  - "[[fbi-cyber-division]]"
crime_types:
  - "[[hacking-ic]]"
---
## Summary

On 5 March 2025, the US Department of Justice announced charges against **12 Chinese nationals** affiliated with Anxun Information Technology Co. Ltd. (i-Soon) and Advanced Persistent Threat 27 (APT27). The defendants included two officers of China's Ministry of Public Security (MPS), eight i-Soon employees, and APT27 members. These actors conducted computer intrusions at the direction of China's MPS and Ministry of State Security (MSS) as well as on their own initiative.

i-Soon operated as a key player in China's **hacker-for-hire ecosystem**, generating tens of millions of dollars in revenue by charging **USD 10,000 to USD 75,000** per successfully exploited email inbox.

## Background

The i-Soon case reveals the blurred line between state-sponsored cyber espionage and commercial cybercrime in China. i-Soon functioned as a contractor for Chinese intelligence agencies while also pursuing independent hacking operations for profit. Victims included:

- US-based critics and dissidents of the PRC
- A large religious organization in the US
- Foreign ministries in Asia: **Taiwan, India, South Korea, Indonesia**

## Participating Parties

- **US agencies:** DOJ, [[fbi-cyber-division|FBI]], Naval Criminal Investigative Service (NCIS), Department of State, Department of the Treasury
- **Enforcement tools:** Criminal indictments, Rewards for Justice (up to USD 10 million), Treasury sanctions

> [!note] This is primarily a US unilateral action. Other countries listed (China, Taiwan, India, South Korea, Indonesia) are victim or defendant countries, not cooperating law enforcement partners.

## Results and Impact

- **12 individuals indicted** for computer intrusion conspiracies
- **Treasury sanctions** imposed
- **Rewards for Justice** offer of up to USD 10 million
- Attribution of i-Soon's operations publicly documented

## Korean Involvement (한국의 참여)

South Korea is listed as a **victim country** — the South Korean foreign ministry was targeted by i-Soon/APT27 intrusion campaigns. This is relevant to Korea's cybersecurity posture but does not represent Korean law enforcement cooperation in this case.

## Contradictions & Open Questions

- Will any of the 12 defendants ever be apprehended?
- What is the full scope of i-Soon's operations against Asian governments?
- How does this case affect US-China cybersecurity diplomatic engagement?
- What specific data was exfiltrated from the South Korean foreign ministry?

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Justice Department Charges 12 Chinese Contract Hackers and Law Enforcement Officers in Global Computer Intrusion Campaigns | US Department of Justice | 2025-03-05 | https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-hackers-and-law-enforcement-officers-global |
| [2] | Page not found | U.S. District Court for the District of Columbia | 2026-04-17 | https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-hackers-and-law-enforcement-officers-global |
| [3] | US Charges 12 Alleged Spies in China's Freewheeling Hacker-for-Hire Ecosystem | WIRED | 2025-03-05 | https://www.wired.com/story/us-charges-12-alleged-spies-in-chinas-freewheeling-hacker-for-hire-ecosystem |
| [4] | US Charges Members of Chinese Hacker-for-Hire Group i-Soon | Infosecurity Magazine | 2025-03-06 | https://www.infosecurity-magazine.com/news/us-charges-chinese-hackerforhire/ |
| [5] | US charges Chinese hackers linked to critical infrastructure breaches | BleepingComputer | 2025-03-05 | https://www.bleepingcomputer.com/news/security/us-charges-chinese-hackers-linked-to-critical-infrastructure-breaches/ |
| [6] | US Justice Department charges employees of Chinese IT contractor i-Soon | The CyberWire | 2025-03-06 | https://thecyberwire.com/newsletters/daily-briefing/14/43 |
