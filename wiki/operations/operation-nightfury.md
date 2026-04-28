---
operation_role: umbrella
parent_operation: ""
summary: "**Operation NightFury** was an INTERPOL-coordinated operation that resulted in the arrest of **3 Indonesian nationals** involved in **Magecart**-style web skimming attacks using the **GetBilling** JavaScript skimmer. The operation involved cooperation between INTERPOL, Indonesian law enforcement, and private sector cybersecurity firm **Group-IB**, which provided critical intelligence."
aliases:
  - "Operation Night Fury"
  - "Magecart Indonesia arrest"
  - "GetBilling operation"
case_id: CYB-2020-051
challenges_encountered:

coordinating_body: "[[interpol]]"
created: 2026-04-08
credibility_index: 2.55
crime_type: "[[online-fraud-ic]]"
edges:

enforcement_type:

lead_agency: "[[interpol]]"
legal_basis:

lessons_learned:

mechanisms_used:

missing_fields:

operation_type: arrest-sweep
outcome: success
participating_agencies:
  - "[[interpol]]"
  - "[[indonesia-police]]"
participating_countries:
  - "[[indonesia]]"
  - "[[singapore]]"
period: 2
related_cases:

related_operations:

results:
  arrests: 3
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 0
  other:

  servers_seized: 0
  victims_notified: 0
source_count: 6
source_tier: 3
sources:
  - "[[group-ib-operation-nightfury-magecartgetbilling]]"
  - "[[cyberscoop-operation-nightfury-magecartgetbilling]]"
  - "[[2020-01-28_techtarget-com_3-magecart-suspects-arrested-in-interpol-operation]]"
  - "[[2020-01-27_bleepingcomputer-com_first-magecart-hackers-caught-infected-hundreds-of-web-stores]]"
  - "[[2020-01-25_thehackernews-com_interpol-arrests-3-indonesian-credit-card-hackers-for-magecart-attacks]]"
  - "[[2020-01-28_infosecurity-magazine_suspected-magecart-hackers-arrested-in-indonesia]]"
status: completed
target_entity: "Magecart/GetBilling web skimming group"
timeframe:
  announced: 2020-01-24
  end: 2020-01-24
  ongoing: false
  start: 2020-01-24
title: "Operation NightFury (Magecart/GetBilling)"
title_ko: "나이트퓨리 작전 (Magecart/GetBilling)"
type: operation
updated: 2026-04-27
---
## Summary

**Operation NightFury** was an INTERPOL-coordinated operation that resulted in the arrest of **3 Indonesian nationals** involved in **Magecart**-style web skimming attacks using the **GetBilling** JavaScript skimmer. The operation involved cooperation between INTERPOL, Indonesian law enforcement, and private sector cybersecurity firm **Group-IB**, which provided critical intelligence.

The arrests represented a significant action against Magecart-type web skimming groups operating in Southeast Asia.

## Background

Magecart is an umbrella term for cybercriminal groups and techniques that involve injecting malicious JavaScript code into e-commerce websites to steal payment card data during checkout. The GetBilling variant was a specific skimmer tool used by the arrested suspects. The suspects compromised hundreds of e-commerce websites to steal credit card details from unsuspecting shoppers.

## Participating Parties

### Coordinating Body
- [[interpol|INTERPOL]]

### Participating Countries
- [[indonesia|Indonesia]]
- [[singapore|Singapore]]

### Private Sector Support
- Group-IB (threat intelligence and technical analysis)

## Legal Framework

Specific legal instruments not detailed in public sources.

## Operational Timeline

| Date | Event |
|------|-------|
| Pre-2020 | Investigation with Group-IB intelligence support |
| 2020-01-24 | 3 arrests in Indonesia announced |

## Results and Impact

| Metric | Count |
|--------|-------|
| Arrests | 3 |
| Countries involved | 2 (+ INTERPOL coordination) |

## Cooperation Mechanisms Used

INTERPOL coordination with local law enforcement, supported by private sector threat intelligence from Group-IB.

## Korean Involvement (한국의 참여)

No Korean involvement identified. South Korean e-commerce sites could potentially be targets of Magecart-style attacks.

## Contradictions & Open Questions

- How many websites were compromised by the GetBilling group?
- How much financial loss was attributed to the group?
- Were the suspects convicted and sentenced?
- What was Singapore's specific role in the operation?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Group-IB, 2020-01-24: Group-IB: Night Fury — INTERPOL-coordinated arrest of Magecart/GetBilling operators.
- CyberScoop, 2020-01-27: CyberScoop: Indonesian Police Arrest 3 Men for Alleged Magecart-Style Attacks (Operation NightFury / GetBilling).
- TechTarget, 2020-01-28: 3 Magecart suspects arrested in Interpol operation.
- BleepingComputer, 2020-01-27: First MageCart Hackers Caught, Infected Hundreds of Web Stores.
- The Hacker News, 2020-01-25: Interpol Arrests 3 Indonesian Credit Card Hackers for Magecart Attacks.
- Infosecurity Magazine, 2020-01-28: Suspected Magecart Hackers Arrested in Indonesia.

## Evidence and Attribution Notes

- On 24 January 2020, INTERPOL's ASEAN Cybercrime Operations Desk announced the results of Operation Night Fury, which resulted in the arrest of 3 Indonesian nationals involved in a Magecart-style JavaScript web skimming operation known as 'GetBilling'
- Private-sector origin: The operation was driven by intelligence provided by Singapore-based cybersecurity firm Group-IB, which had been tracking GetBilling since 2018 and had identified infrastructure linking the group to hundreds of compromised e-commerce sites worldwide
- Technical profile: GetBilling deployed obfuscated JavaScript skimmers that were injected into e-commerce payment checkout pages to exfiltrate customer payment card data, shipping details and personal information — the hallmark Magecart pattern
- Scope of compromise: Group-IB's report describes that GetBilling had compromised 'hundreds' of online stores across multiple countries, though no specific country list was published beyond confirmation that victims spanned Asia-Pacific, Europe and North America
- Operation Night Fury was also folded into INTERPOL's broader ASEAN 'Operation Goldfish Alpha/Night Fury' reporting, presenting the arrests as part of a regional cyberthreat response rather than a standalone named action
- Historical significance: This was one of the first publicly announced arrests of Magecart operators anywhere in the world — the broader Magecart umbrella (estimated 20+ distinct groups) had been tracked by security researchers since 2015 without successful takedowns until this Indonesia action
- 3 Indonesian men arrested on 20 December 2019 in Jakarta and Yogyakarta for Magecart-style web skimming attacks, announced by INTERPOL on 27 January 2020 as 'Operation NightFury'
- Suspects faced up to 10 years in prison under Indonesian law if convicted

<!-- SOURCE_ENRICHMENT_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a arrest-sweep against Magecart/GetBilling web skimming group, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Interpol and coordination to Interpol, with participating or affected jurisdictions recorded as Indonesia and Singapore.

The cooperation model is documented through named agencies and partners: Interpol and Indonesia Police.

Operational results captured for the canonical record: 3 arrests.

The canonical source set contains 6 reference(s): Group Ib Operation Nightfury Magecartgetbilling, Cyberscoop Operation Nightfury Magecartgetbilling, 2020 01 28 Techtarget Com 3 Magecart Suspects Arrested In Interpol Operation, 2020 01 27 Bleepingcomputer Com First Magecart Hackers Caught Infected Hundreds Of Web Stores, 2020 01 25 Thehackernews Com Interpol Arrests 3 Indonesian Credit Card Hackers For Magecart Attacks, 2020 01 28 Infosecurity Magazine Suspected Magecart Hackers Arrested In Indonesia.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Group-IB: Night Fury — INTERPOL-coordinated arrest of Magecart/GetBilling operators | Group-IB | 2020-01-24 | https://www.group-ib.com/media-center/press-releases/night-fury/ |
| [2] | CyberScoop: Indonesian Police Arrest 3 Men for Alleged Magecart-Style Attacks (Operation NightFury / GetBilling) | CyberScoop | 2020-01-27 | https://cyberscoop.com/magecart-arrest-indonesia-interpol-getbilling/ |
| [3] | 3 Magecart suspects arrested in Interpol operation | TechTarget | 2020-01-28 | https://www.techtarget.com/searchsecurity/news/252477470/3-Magecart-suspects-arrested-in-Interpol-operation |
| [4] | First MageCart Hackers Caught, Infected Hundreds of Web Stores | BleepingComputer | 2020-01-27 | https://www.bleepingcomputer.com/news/security/first-magecart-hackers-caught-infected-hundreds-of-web-stores/ |
| [5] | Interpol Arrests 3 Indonesian Credit Card Hackers for Magecart Attacks | The Hacker News | 2020-01-25 | https://thehackernews.com/2020/01/indonesian-magecart-hackers.html?m=1 |
| [6] | Suspected Magecart Hackers Arrested in Indonesia | Infosecurity Magazine | 2020-01-28 | https://www.infosecurity-magazine.com/news/suspected-magecart-hackers/ |
