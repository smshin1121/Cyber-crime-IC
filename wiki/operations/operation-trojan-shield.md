---
type: operation
title: "Operation Trojan Shield (AN0M)"
aliases:
  - "Operation Ironside"
  - AN0M
  - ANOM
case_id: CYB-2021-680
period: 2
operation_type: undercover
status: completed
enforcement_type:
  - infiltration
  - arrest
  - seizure
  - indictment
outcome: success
timeframe:
  announced: 2021-06-08
  start: 2018
  end: 2021-06-08
  ongoing: false
crime_type: "[[organized-crime-ic]]"
target_entity: "Transnational organized crime networks relying on encrypted AN0M devices"
lead_agency: "[[fbi-cyber-division]]"
coordinating_body: "[[europol-ec3]]"
participating_countries:
  - "[[united-states]]"
  - "[[australia]]"
  - "[[netherlands]]"
  - "[[sweden]]"
  - "[[germany]]"
  - "[[international]]"
participating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[australia-afp]]"
  - "[[europol-ec3]]"
  - "[[netherlands-politie]]"
  - "[[sweden-police]]"
legal_basis:
  - "[[mutual-legal-assistance]]"
mechanisms_used:
  - "[[joint-investigation-team]]"
results:
  arrests: 800
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "$48 million+ in cash and virtual assets reported seized"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "27 million messages reviewed"
    - "12,000+ AN0M devices distributed"
    - "700+ searches conducted"
    - "8 tons of cocaine and 22 tons of cannabis seized"
    - "250 firearms seized"
edges:
  - source_actor: "[[fbi-cyber-division]]"
    target_actor: "[[australia-afp]]"
    cooperation_type: undercover_platform
    legal_basis: "undercover authority"
    direction: undirected
  - source_actor: "[[fbi-cyber-division]]"
    target_actor: "[[europol-ec3]]"
    cooperation_type: intelligence_sharing
    legal_basis: "[[mutual-legal-assistance]]"
    direction: undirected
credibility_index: 4.8
source_tier: 1
missing_fields:

related_cases:
  - "[[us-v-anom-distributors]]"
related_operations:
  - "[[operation-us-v-anom-distributors]]"
challenges_encountered:
  - "The operation required maintaining covert trust in an FBI-controlled encrypted device ecosystem over several years."
  - "Operational secrecy had to be balanced against rapid intervention once imminent violent threats were detected."
lessons_learned:
  - "Purpose-built criminal communications infrastructure can be turned into a high-value intelligence collection channel."
  - "Large-scale encrypted platform disruption is most effective when synchronized with simultaneous arrests and searches."
source_count: 4
sources:
  - "[[2021-06-08_fbi-gov_fbi-and-global-partners-announce-results-of-operation-trojan-shield]]"
  - "[[2021-06-08-europol-trojan-shield-an0m]]"
  - "[[2021-06-08_sdca_anom-enterprise-indictment]]"
  - "[[2026-04-17_justice-gov_distributor-anom-hardened-encrypted-devices-sentenced-63-months-prison-racketeer]]"
created: 2026-04-12
updated: 2026-05-17
operation_role: umbrella
parent_operation: ""
organizations:
  - "[[fbi-cyber-division]]"
  - "[[europol-ec3]]"
  - "[[australia-afp]]"
  - "[[netherlands-politie]]"
  - "[[sweden-police]]"
crime_types:
  - "[[organized-crime-ic]]"
summary: "Operation Trojan Shield was a long-running FBI and AFP undercover operation built around AN0M encrypted devices. By June 8, 2021, the operation had enabled more than 800 arrests, hundreds of searches, and major drug, firearm, and asset seizures across multiple jurisdictions."
---
## Summary

Operation Trojan Shield was a multi-year undercover operation in which the [[fbi-cyber-division|FBI]] and the [[australia-afp|Australian Federal Police]] helped place AN0M encrypted devices into transnational criminal networks, then used court-authorized access to those communications to support coordinated arrests and seizures. Official FBI and Europol statements describe it as the largest law-enforcement operation ever mounted against encrypted criminal communications.

The action reached its public culmination on 2021-06-08, when partner agencies executed synchronized arrests, searches, and seizures across more than a dozen countries. The operation is important in this wiki because it sits at the intersection of undercover platform deployment, intelligence sharing, and multinational evidentiary exploitation.

## Background

### Modus operandi

AN0M was an FBI/AFP-developed encrypted-handset platform supplied through a covert administrator network. After earlier criminal-encrypted-phone disruptions (e.g., Phantom Secure 2018, EncroChat 2020, Sky ECC 2021) pushed organised crime groups toward new providers, law enforcement and partner services exploited the demand for a supposedly secure handset ecosystem. Per the FBI and SDCA indictment releases, AN0M devices — appearing on the surface as a generic Android handset with hardened messaging — were stripped of normal functionality (no voice calls, no email, no GPS) and ran a hidden encrypted-messaging app concealed inside a calculator icon. Criminal end-users paid roughly USD 1,500–2,500 every six months for a device, and could only message other AN0M users, creating a pure criminal-traffic channel. **Unbeknownst to the users, the AN0M app blind-copied (BCC'd) every message and attachment in plaintext to FBI-controlled servers**, where partner agencies could read traffic in near real time. Over the operational window the platform yielded approximately **27 million messages** in 45+ languages, including operational planning for drug shipments, weapons movements, money-laundering corridors, contract killings, and political-corruption payments.

### Victim profile and impact

Unlike a typical cybercrime IC operation, the Trojan Shield victim pool is the broad civilian population exposed to the trafficking, violence, and corruption activities discussed on AN0M — not direct victims of a single computer-crime offence. Per Europol and the SDCA indictment, intelligence derived from AN0M led to direct interventions against at least **150 imminent threats to life** (planned hits and violent acts averted), the seizure of **8 tons of cocaine, 22 tons of cannabis, 2 tons of methamphetamine and amphetamine, 6 tons of synthetic-drug precursors, and 250 firearms**, plus over **USD 48 million in cash and virtual assets**. Indirect victim populations include the consumer markets for narcotics intercepted; the targets of the 150+ averted violent threats; and corruption victims of the law-enforcement officers identified through AN0M traffic in multiple participating jurisdictions.

### Financial flow

The illicit financial flows surfaced through AN0M included (i) **bulk-cash courier networks** moving narcotics proceeds across Australia, the Netherlands, Germany, and the US; (ii) **cryptocurrency laundering** of trafficking proceeds (tens of millions in virtual assets seized); (iii) **trade-based money laundering** routing through real-estate and bulk-commodity transactions across multiple continents; and (iv) **corruption payments** to compromised public officials including in at least one EU member state. The platform itself generated revenue for its criminal-administrator distributors via the periodic device-subscription fees (USD 1,500–2,500 per six months per device, 12,000+ devices in circulation), which subsequent SDCA prosecution against the distributor network treated as racketeering proceeds — see the 2026-04-17 SDCA distributor sentencing (63 months).

### Criminal organization structure

AN0M's user base, per Europol, spanned **more than 300 transnational criminal syndicates** operating in 100+ countries. Major user clusters identified included Australian Outlaw Motorcycle Gangs, Italian organised-crime affiliates (including 'Ndrangheta-linked clans operating in Europe and South America), Balkan trafficking cartels, Asian drug-trafficking networks operating through Hong Kong and Thailand, and South American narcotics suppliers. The platform was not itself an OCG — it was an intelligence channel deliberately seeded into pre-existing OCGs — but the AN0M distributor network (a hierarchy of regional resellers who served as marketing nodes into criminal communities) was itself prosecuted as a racketeering enterprise in the SDCA AN0M Enterprise indictment ([[us-v-anom-distributors]]).

Trojan Shield generated evidentiary value before the overt phase, which made the operation both a disruption action and a long-horizon intelligence-collection programme.

## Participating Parties

### Lead Agency
- [[fbi-cyber-division|FBI Cyber Division]]

### Coordinating and Core Partners
- [[australia-afp|Australian Federal Police]]
- [[europol-ec3|Europol EC3]]
- [[netherlands-politie|Dutch National Police]]
- [[sweden-police|Swedish Police Authority]]

### Participating Jurisdictions
- [[united-states|United States]]
- [[australia|Australia]]
- [[netherlands|Netherlands]]
- [[sweden|Sweden]]
- [[germany|Germany]]
- [[international|Multiple additional partner jurisdictions]]

## Legal Framework

The public record indicates a mix of undercover authority, judicially supervised interception or lawful access mechanisms, and cross-border evidence sharing. The exact legal process varied by jurisdiction, but the operational model depended on undercover deployment of a communications platform, lawful access to message traffic, and [[mutual-legal-assistance|mutual legal assistance]] for coordinated international evidence exploitation.

## Operational Timeline

| Date | Event |
|------|-------|
| 2018 | AN0M undercover platform begins circulating in criminal networks |
| 2019-2020 | Large message volumes are collected and analyzed across partner jurisdictions |
| 2021-06-08 | Public announcement and synchronized global enforcement phase |

## Results and Impact

| Metric | Reported result |
|--------|-----------------|
| Arrests | 800+ |
| Searches | 700+ |
| Criminal syndicates affected | 300+ |
| Messages reviewed | 27 million |
| Devices in circulation | 12,000+ |
| Drug seizures | 8 tons cocaine, 22 tons cannabis |
| Firearms seized | 250 |
| Cash / asset seizures | $48M+ |

The scale matters because the operation turned encrypted communications themselves into the main evidentiary channel. It also demonstrated that multinational timing is critical: arrests and searches had to be synchronized so intelligence collection did not collapse before overt action began.

## Cooperation Mechanisms Used

- [[joint-investigation-team|Operational coordination through multinational law-enforcement structures]]
- [[mutual-legal-assistance|Cross-border evidence and arrest support]]
- Undercover platform deployment and intelligence sharing

## Challenges and Friction Points

- Maintaining covert credibility for AN0M required long-term operational discipline.
- Message exploitation created an analytical burden because the dataset was massive and time-sensitive.
- The same platform that produced evidentiary value also created intervention dilemmas when messages revealed imminent violence.

## Follow-Up Actions

Trojan Shield produced downstream prosecutions and defendant-specific enforcement pages, including [[us-v-anom-distributors]] and its linked follow-on operation [[operation-us-v-anom-distributors]]. It also became a benchmark example for later discussions about the limits and possibilities of lawful access to criminal communications services.

## Contradictions & Open Questions

- **L26 gap — direct cyber-victim attribution**: The Trojan Shield victim profile is constituted by the trafficking, violence, and corruption activities discussed on AN0M rather than by direct cyber-victims of a computer-crime offence. Mapping AN0M-derived prosecutions to victim populations downstream of the intercepted criminal activity is left to the relevant case pages.
- **L26 gap — full money-laundering corridor map**: Bulk-cash, cryptocurrency, trade-based, and corruption-payment channels are individually attested but a consolidated AN0M-traffic-derived corridor map across all 16+ participating jurisdictions has not been published.
- **L26 gap — OCG roster**: Europol's "300+ criminal syndicates" framing is aggregate. Individual syndicate names, hierarchies, and Trojan-Shield-attributable arrests by syndicate are dispersed across national prosecution records and have not been consolidated.
- **Lawful-access legality across jurisdictions**: The lawful-access basis differed by partner — third-country relay through a partner jurisdiction (Lithuania has been publicly identified as the relay state in some reporting) raised admissibility questions that some national courts addressed only after the public disclosure phase. A consolidated legal-authority map across the 16+ jurisdictions has not been published.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- US Federal Bureau of Investigation, 2021-06-08: FBI and Global Partners Announce Results of Operation Trojan Shield.
- Europol, 2021-06-08: 800 criminals arrested in biggest ever law enforcement operation against encrypted communication.
- FBI, 2021-06-08: FBI and Global Partners Announce Results of Operation Trojan Shield.
- US DOJ (Southern District of California), 2021-06-08: FBI’s Encrypted Phone Platform Infiltrated Hundreds of Criminal Syndicates; Result is Massive Worldwide Takedown.
- justice.gov, 2026-04-17: Distributor of ANOM Hardened Encrypted Devices Sentenced to 63 Months in Prison for Racketeering Conspiracy.

## Evidence and Attribution Notes

- FBI official announcement of Operation Trojan Shield results (8 June 2021).
- Over 800 arrests across 16+ countries; 27 million encrypted messages reviewed.
- FBI-AFP joint-developed AN0M encrypted device platform; 12,000+ devices distributed.
- Operation Trojan Shield was a multi-year undercover operation in which the FBI and the Australian Federal Police helped place AN0M encrypted devices into transnational criminal networks, then used court-authorized access to those communications to support coordinated arrests and seizures.
- Official FBI and Europol statements describe it as the largest law-enforcement operation ever mounted against encrypted criminal communications.
- FBI, Dutch National Police, and Swedish Police Authority supported by Europol and 16 partner countries.
- 700+ house searches, 800+ arrests, 8 tons cocaine, 22 tons cannabis, 250 firearms, $48M+ seized.
- AN0M platform: 12,000+ devices, 300+ criminal syndicates across 100+ countries, 27 million messages reviewed over 18 months.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US Federal Bureau of Investigation, 2021-06-08: The FBI, along with the Drug Enforcement Administration, Australian Federal Police, Europol, and law enforcement partners in more than a dozen countries, are announcing the results of that covert effort, known as Operation Trojan Shield.
- US Federal Bureau of Investigation, 2021-06-08: Law enforcement has also been able to mitigate direct threat-to-life situations.
- FBI, 2021-06-08: The FBI, along with the Drug Enforcement Administration, Australian Federal Police, Europol, and law enforcement partners in more than a dozen countries, are announcing the results of that covert effort, known as Operation Trojan Shield.
- FBI, 2021-06-08: Law enforcement has also been able to mitigate direct threat-to-life situations.
- justice.gov, 2026-04-17: Attorneys Front Office Office Criminal Division Civil Division Other Agencies District History Programs Victim Witness Assistance Project Safe Neighborhoods Project Guardian Project Safe Childhood Environmental Justice ## Extraction Notes - parser: document - fetcher: doj_fetch - fetched_at: 2026-04-25T14:21:03+00:00 - final_url:

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a undercover against Transnational organized crime networks relying on encrypted AN0M devices, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Fbi Cyber Division and coordination to Europol Ec3, with participating or affected jurisdictions recorded as United States, Australia, Netherlands, Sweden, Germany, International.

The cooperation model is documented through named agencies and partners: Fbi Cyber Division, Australia Afp, Europol Ec3, Netherlands Politie, Sweden Police; mechanisms: Joint Investigation Team; legal basis: mutual legal assistance; enforcement posture: Infiltration, Arrest, Seizure, Indictment.

Operational results captured for the canonical record: 800 arrests; cryptocurrency/asset result recorded as $48 million+ in cash and virtual assets reported seized; 27 million messages reviewed; 12,000+ AN0M devices distributed; 700+ searches conducted; 8 tons of cocaine and 22 tons of cannabis seized.

The canonical source set contains 6 reference(s): 2021 06 08 Fbi Operation Trojan Shield, 2021 06 08 Europol Trojan Shield An0m, 2021 06 08 Fbi Gov Fbi And Global Partners Announce Results Of Operation Trojan Shield, 2021 06 08 Europol Europa Eu 800 Criminals Arrested In Biggest Ever Law Enforcement Operation Against Encrypt, 2021 06 08 Sdca Anom Enterprise Indictment, 2026 04 17 Justice Gov Distributor Anom Hardened Encrypted Devices Sentenced 63 Months Prison Racketeer.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | FBI and Global Partners Announce Results of Operation Trojan Shield | FBI | 2021-06-08 | https://www.fbi.gov/news/stories/fbi-global-partners-announce-results-of-operation-trojan-shield-060821 |
| [2] | 800 criminals arrested in biggest ever law enforcement operation against encrypted communication | Europol | 2021-06-08 | https://www.europol.europa.eu/media-press/newsroom/news/800-criminals-arrested-in-biggest-ever-law-enforcement-operation-against-encrypted-communication |
| [3] | FBI’s Encrypted Phone Platform Infiltrated Hundreds of Criminal Syndicates; Result is Massive Worldwide Takedown | US DOJ (Southern District of California) | 2021-06-08 | https://www.justice.gov/usao-sdca/pr/fbi-s-encrypted-phone-platform-infiltrated-hundreds-criminal-syndicates-result-massive |
| [4] | Distributor of ANOM Hardened Encrypted Devices Sentenced to 63 Months in Prison for Racketeering Conspiracy | justice.gov | 2026-04-17 | https://www.justice.gov/usao-sdca/pr/distributor-anom-hardened-encrypted-devices-sentenced-63-months-prison-racketeering |
