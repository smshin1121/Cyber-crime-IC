---
type: operation
title: "xDedic Marketplace Takedown"
title_ko: "xDedic 마켓플레이스 소탕"
aliases: ["xDedic takedown", "xDedic marketplace seizure 2019"]
case_id: "CYB-2019-051"
period: 2
operation_type: "takedown"
status: "completed"
enforcement_type:
  - "seizure"
  - "takedown"
outcome: "success"
timeframe:
  announced: "2019-01-28"
  start: "2019-01-28"
  end: "2019-01-28"
  ongoing: false
crime_type: "[[cybercrime-forum-ic]]"
target_entity: "xDedic Marketplace"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[belgium]]"
  - "[[ukraine]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "xDedic marketplace seized"
    - "Over 85,000 compromised servers had been listed for sale"
    - "Estimated $68 million in fraud facilitated"
edges:
  - source_actor: "FBI"
    target_actor: "Europol"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
  - source_actor: "FBI"
    target_actor: "Ukraine Cyber Police"
    cooperation_type: "joint_investigation"
    legal_basis: "unknown"
    direction: "undirected"
credibility_index: 1.88
source_tier: 3
missing_fields:
  - "legal_basis"
  - "mechanisms_used"
  - "arrests"
related_cases:
  - "[[us-v-habasescu-xdedic|United States v. Alexandru Habasescu (xDedic)]]"
  - "[[us-v-kharmanskyi-xdedic|United States v. Pavlo Kharmanskyi (xDedic)]]"
  - "[[us-v-pankov-xdedic|United States v. Dariy Pankov (xDedic / NLBrute)]]"
  - "[[us-v-levinson-xdedic|United States v. Allen Levinson (xDedic Tax-Fraud Buyer)]]"
  - "[[us-v-mcneely-xdedic|United States v. McNeely et al. (xDedic Buyers)]]"
  - "[[us-v-ivanov-tolpintsev-xdedic|United States v. Ivanov-Tolpintsev (xDedic Credentials Seller)]]"
  - "[[us-v-adejumo-jinadu-xdedic|United States v. Adejumo and Jinadu (xDedic Tax-Fraud Proceeds)]]"
  - "[[us-v-omotosho-xdedic|United States v. Bamidele Omotosho (xDedic Cyber Scams)]]"
  - "[[us-v-odedeyi-davies-xdedic|United States v. Odedeyi and Davies (xDedic U.K. Extradition Case)]]"
  - "[[us-v-spencer-xdedic|United States v. Joshua Spencer (xDedic)]]"
  - "[[us-v-mckinzie-xdedic|United States v. Harold McKinzie (xDedic)]]"
  - "[[us-v-adafin-xdedic|United States v. Olayemi Adafin (xDedic)]]"
  - "[[us-v-oyebanjo-xdedic|United States v. Olakunle Oyebanjo (xDedic)]]"
  - "[[us-v-taylor-xdedic|United States v. Akinola Taylor (xDedic)]]"
  - "[[us-v-ogunlana-xdedic|United States v. Oluwarotimi Ogunlana (xDedic)]]"
related_operations: []
challenges_encountered: []
lessons_learned: []
source_count: 1
sources:
  - "tier3-thehackernews-xdedic-2019"
created: 2026-04-08
updated: 2026-04-17
---

> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

In January 2019, the FBI, in cooperation with [[europol-ec3|Europol]] and Belgian and Ukrainian authorities, seized **xDedic**, a major online criminal marketplace that sold access to compromised computer servers worldwide. The marketplace had listed over **85,000 compromised servers** for sale and facilitated an estimated **$68 million** in fraud.

The xDedic marketplace operated on the dark web and allowed buyers to search for compromised servers by criteria such as price, geographic location, operating system, and other technical characteristics, enabling a wide range of cybercrimes including tax fraud, ransomware deployment, and data theft.

## Background

xDedic was first identified by Kaspersky Lab in 2016, at which point it offered approximately 70,000 hacked servers for sale. The marketplace operated as a clearinghouse where hackers could sell access to compromised Remote Desktop Protocol (RDP) servers to other criminals, who would then use them as launchpads for further attacks. The marketplace migrated to the dark web after public exposure in 2016.

## Participating Parties

### Lead Agency
- [[fbi-cyber-division|FBI Cyber Division]]

### Coordinating Body
- [[europol-ec3|Europol EC3]]

### Participating Countries
- [[united-states|United States]]
- [[belgium|Belgium]]
- [[ukraine|Ukraine]]

## Legal Framework

Specific legal instruments enabling the cooperation have not been detailed in the Tier 3 source.

## Operational Timeline

| Date | Event |
|------|-------|
| 2016 | Kaspersky Lab publicly identifies xDedic marketplace |
| 2016-2019 | Investigation period |
| 2019-01-28 | xDedic marketplace seized by FBI with international partners |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Marketplace seized | xDedic domain |
| Compromised servers listed | 85,000+ |
| Estimated fraud facilitated | $68 million |
| Countries involved | 3 |

## Cooperation Mechanisms Used

Details not documented in the Tier 3 source. The FBI-Europol-Ukraine cooperation pattern was common for dark web marketplace takedowns in this period.

## Korean Involvement (한국의 참여)

No Korean involvement identified. However, compromised servers in any country could have been listed on xDedic.

## Contradictions & Open Questions

- Were any arrests made in connection with the seizure?
- What technical methods were used to identify the marketplace operators?
- How many victims were notified about their compromised servers?
- What was the role of Belgian law enforcement specifically?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Cyber Criminal Marketplace | The Hacker News | 2019-01-28 | [link](https://thehackernews.com/2019/01/cyber-criminal-marketplace.html) |

