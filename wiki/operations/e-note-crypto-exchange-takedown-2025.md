---
type: operation
title: "E-Note Crypto Exchange Takedown (US-Germany-Finland, 2025)"
title_ko: "E-Note 암호화폐 거래소 단속 (미국·독일·핀란드, 2025)"
aliases:
  - "E-Note takedown"
  - "E-Note crypto exchange seizure"
case_id: CYB-2025-202
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - takedown
  - search-seizure
  - indictment
  - online-content-takedown
outcome: success
timeframe:
  announced: 2025-12-17
  start: 2017
  end: 2025-12-17
  ongoing: false
crime_type: "[[money-laundering-ic]]"
crime_types:
  - "[[money-laundering-ic]]"
  - "[[ransomware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
target_entity: "E-Note cryptocurrency exchange and payment-processing service (e-note.com, e-note.ws, jabb.mn) — alleged to have laundered USD 70 million+ in cybercrime proceeds since 2017, including ransomware and account-takeover proceeds targeting US healthcare and critical-infrastructure victims"
lead_agency: "[[us-doj]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[united-states]]"
  - "[[germany]]"
  - "[[finland]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[germany-bka]]"
  - "[[finland-nbi]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[germany-bka]]"
  - "[[finland-nbi]]"
mechanisms_used:
  - "[[search-seizure]]"
  - "[[domain-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "Eastern District of Michigan indictment, 1 count: 18 U.S.C. § 1956(h) (conspiracy to commit money laundering)"
  - "Court-authorized seizure of three E-Note-associated domains (e-note.com, e-note.ws, jabb.mn) and associated servers"
results:
  arrests: 0
  indictments: 1
  servers_seized: 0
  domains_seized: 3
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Mykhalio Petrovich Chudnovets, 39, Russian national, indicted in EDMI on one count of money laundering conspiracy (max 20 years)"
    - "Three E-Note-associated domains seized: e-note.com, e-note.ws, jabb.mn"
    - "Servers and associated mobile applications hosting the E-Note crypto exchange and payment-processing service seized"
    - "FBI identified USD 70 million+ in illicit proceeds transferred through E-Note since 2017"
    - "Court documents allege Chudnovets has laundered money for cybercriminals since 2010 (personal money-mule activity), evolving into the E-Note online platform circa 2011"
    - "US victims include healthcare and critical-infrastructure sectors"
edges:
  - source_actor: "us-doj"
    target_actor: "germany-bka"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "us-doj"
    target_actor: "finland-nbi"
    cooperation_type: joint_investigation
    legal_basis: informal
    direction: undirected
  - source_actor: "fbi"
    target_actor: "germany-bka"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
  - source_actor: "fbi"
    target_actor: "finland-nbi"
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "specific arrest count (Chudnovets's custody status not described in cited source)"
  - "specific MLAT or treaty article cited for German/Finnish cooperation"
related_cases: []
related_operations:
  - "[[us-v-volkov-yanluowang-sentencing]]"
  - "[[operation-cronos-phase2]]"
challenges_encountered: []
lessons_learned:
  - "E-Note's ~14-year operational lifespan (2011 platform launch through 2025 seizure) demonstrates the long-tail nature of public-record cybercrime money-laundering platform takedowns: investigative continuity across multiple US enforcement administrations was required to build the indictment against a single Russian-national operator."
  - "The US-Germany-Finland cooperation pattern in this case adds two new European jurisdictions to the wiki's recurring transnational money-laundering takedown roster, broadening the SNA edge data for European cooperation in non-EU-member-state ransomware-laundering investigations beyond the Cronos / Endgame core."
  - "The Russian-national operator pattern continues — like Volkov (Yanluowang IAB) and Khoroshev (LockBit administrator), Chudnovets is publicly identified by name despite Russia not being a cooperating state."
source_count: 1
sources:
  - "[[2025-12-17_doj-edmi_e-note-crypto-exchange-takedown]]"
summary: "On 2025-12-17 the US Attorney's Office for the Eastern District of Michigan, the FBI Detroit Division, and the Michigan State Police announced the takedown of the E-Note cryptocurrency exchange and payment-processing service, with cooperation from the German Federal Criminal Police Office and the Finnish National Bureau of Investigation. A federal indictment was unsealed against Mykhalio Petrovich Chudnovets, 39, a Russian national, on one count of money laundering conspiracy (max 20 years). Three domains (e-note.com, e-note.ws, jabb.mn) and associated servers and mobile applications were seized. FBI identified USD 70 million+ in illicit proceeds transferred through E-Note since 2017, including ransomware and account-takeover proceeds targeting US healthcare and critical-infrastructure victims."
created: 2026-05-08
updated: 2026-05-08
---
## Summary

On 2025-12-17 the US Attorney's Office for the Eastern District of Michigan, the FBI Detroit Division, and the Michigan State Police announced the takedown of the E-Note cryptocurrency exchange and payment-processing service. The German Federal Criminal Police Office ([[germany-bka|BKA]]) and the Finnish National Bureau of Investigation ([[finland-nbi|NBI]]) are named as cooperating European authorities. A federal indictment was unsealed against Mykhalio Petrovich Chudnovets, 39, a Russian national alleged to have controlled and operated E-Note from approximately 2011 through 2025, on one count of money laundering conspiracy carrying a maximum 20-year prison term.

The operation seized three E-Note-associated domains (e-note.com, e-note.ws, jabb.mn) and associated servers and mobile applications hosting the crypto exchange and payment-processing service. The FBI identified USD 70 million or more in illicit proceeds transferred through E-Note and its associated money-mule network since 2017, with proceeds linked to ransomware attacks and account-takeover schemes targeting US victims, including organisations in the healthcare and critical-infrastructure sectors.

## Background

Court documents allege that Chudnovets has laundered money for cybercriminals since 2010 — beginning with personal money-mule networks before evolving the operation into a more scalable online platform. The 2011 platform launch and the 2017 start date of the FBI's tracking window establish a multi-decade operational lifespan for the underlying enterprise, with the 2025 seizure representing the public-record terminus of that lifespan.

## Participating Parties

| Role | Parties |
|---|---|
| US prosecutorial line | US Attorney's Office for the Eastern District of Michigan (USAO-EDMI; United States Attorney Jerome F. Gorgon, Jr.) |
| US lead investigator | [[fbi\|FBI]] Detroit Division (Special Agent in Charge Jennifer Runyan) |
| US state-level partner | Michigan State Police (including the Michigan Cyber Command Center) |
| German cooperation | [[germany-bka\|German Federal Criminal Police Office (Bundeskriminalamt / BKA)]] |
| Finnish cooperation | [[finland-nbi\|Finnish National Bureau of Investigation (Keskusrikospoliisi / KRP)]] |
| Source-backed participating countries | [[united-states\|United States]] (charging and seizing state); [[germany\|Germany]] (cooperation); [[finland\|Finland]] (cooperation); [[russia\|Russia]] (defendant nationality and stated residence) |

## Operational Timeline

| Date | Event | Source |
|---|---|---|
| 2010 | Per court documents, Chudnovets begins laundering money for cybercriminals via personal money-mule networks | DOJ EDMI 2025-12-17 |
| 2011 (approx.) | E-Note platform launched as a more scalable online operation | DOJ EDMI 2025-12-17 |
| 2017 | FBI tracking window begins; USD 70M+ in proceeds traced through the platform from this date forward | DOJ EDMI 2025-12-17 |
| 2025-12-17 | DOJ EDMI announcement and concurrent indictment unsealing; domain seizures executed | DOJ EDMI 2025-12-17 |

## Results and Impact

- 1 federal indictment (Chudnovets) on one count of money laundering conspiracy.
- 3 E-Note-associated domains seized: e-note.com, e-note.ws, jabb.mn.
- Servers and associated mobile applications seized.
- USD 70 million+ in illicit proceeds traced through E-Note since 2017 (FBI figure).
- US-victim sectors named: healthcare and critical infrastructure.

## Cooperation Mechanisms Used

The cited release describes US-Germany-Finland cooperation through informal law-enforcement channels, with the German BKA and Finnish NBI named as cooperating European authorities supporting the US-led seizure and indictment. The release does not enumerate a specific MLAT instrument, EU European Investigation Order (EIO) execution, or Joint Investigation Team (JIT) designation. The legal-basis classification therefore follows [[search-seizure|US domestic search-and-seizure]] and [[domain-seizure|domain seizure]] for the US-side actions, with [[informal-cooperation|informal European cooperation]] supplying the corroborating intelligence and infrastructure-discovery support.

## Korean Involvement (한국의 참여)

South Korea is not named in the cited DOJ EDMI announcement as a victim, source, or cooperation jurisdiction for this operation. The case is recorded in the wiki for the US-Germany-Finland cooperation pattern in cybercrime money-laundering platform takedowns and the Russian-national-operator attribution category. Korean exposure to E-Note-style money-laundering services is not directly informed by this source, but the cooperation pattern is structurally relevant to the broader Korean voice-phishing-proceeds and ransomware-proceeds-laundering corpus tracked elsewhere in this wiki.

## Contradictions & Open Questions

- Chudnovets's custody status (whether arrested, in detention, or at large) is not described in the cited source.
- The specific MLAT, EIO, or treaty basis for the German and Finnish cooperation is not enumerated.
- The full set of cybercrime-group clients of E-Note (e.g., specific named ransomware affiliates) is not identified in the cited source.
- The DOJ EDMI press release URL was not directly accessible from this corpus's TLS-spoofing fetch tool or Anthropic WebFetch on 2026-05-08; verbatim content was captured from same-day tier-2 reporting reproducing the USAO-EDMI press conference content. Re-fetch should refresh the raw archive when the DOJ URL becomes accessible.

## References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| [1] | [[2025-12-17_doj-edmi_e-note-crypto-exchange-takedown\|U.S. and International Partners Take Down E-Note Crypto Exchange and Indict Russian Operator (USAO–EDMI announcement)]] | USAO Eastern District of Michigan; FBI Detroit; Michigan State Police | 2025-12-17 | https://www.justice.gov/usao-edmi/news-and-press-releases-9 |
