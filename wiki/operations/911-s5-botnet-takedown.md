---
aliases:

case_id: CYB-2024-014
challenges_encountered:

coordinating_body: "[[fbi]]"
created: 2026-04-08
credibility_index: 4.0
crime_type: "[[malware-ic]]"
edges:

enforcement_type:

lead_agency: "[[usdoj]]"
legal_basis:

lessons_learned:

mechanisms_used:
  - "[[search-seizure]]"
  - "[[asset-freezing]]"
  - "[[public-private-cooperation]]"

missing_fields:

operation_type: takedown
outcome: success
participating_agencies:
  - "[[usdoj]]"
  - "[[fbi]]"
  - "[[us-treasury]]"

participating_countries:
  - "[[united-states]]"
  - "[[germany]]"
  - "[[singapore]]"
  - "[[thailand]]"

period: 3
related_cases:
  - "[[us-v-yunhe-wang-911-s5]]"
related_operations:
  - "[[operation-us-v-yunhe-wang-911-s5]]"
results:
  arrests: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 1
  other:
    - "19 million+ compromised IP addresses across nearly 200 countries identified"
    - "911 S5 residential proxy service disrupted"
    - "OFAC sanctions targeted YunHe Wang, two associates, and three linked entities"

  servers_seized: 0
  victims_notified: 0
source_count: 5
source_tier: 2
sources:
  - "[[2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet]]"
  - "[[2024-05-29_ic3-gov_guidance-on-the-911-s5-residential-proxy-service]]"
  - "[[2024-06-07_fbi-gov_the-911-s5-cyber-threat]]"
  - "[[2024-05-28_treasury-gov_treasury-sanctions-a-cybercrime-network-associated-with-the-911-s5-botnet]]"
  - "[[2024-05-29_fbi-gov_how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors]]"

status: completed
target_entity: "911 S5 Botnet"
timeframe:
  announced: 2024-05
  end: 2024-05
  ongoing: false
  start: 2024-05
title: "911 S5 Botnet Dismantling"
title_ko: "911 S5 Botnet Dismantling (공식 작전명 미확인)"
type: operation
updated: 2026-04-28
operation_role: umbrella
parent_operation: ""
summary: "The U.S. Department of Justice and FBI, in cooperation with Germany, Singapore, and Thailand, dismantled the 911 S5 botnet -- the world's largest botnet, which had infected over 19 million IP addresses across nearly 200 countries. The administrator, YunHe Wang, was arrested. The botnet had been used to facilitate large-scale fraud, identity theft, child sexual exploitation, bomb threats, and illegal financial transactions."
organizations:
  - "[[usdoj]]"
  - "[[fbi]]"
crime_types:
  - "[[malware-ic]]"
  - "[[csam-ic]]"
---
## Summary

The 911 S5 action was a U.S.-led disruption of a residential-proxy botnet and fraud-enabling service. The DOJ and FBI record the operation as a coordinated multinational action with Germany, Singapore, and Thailand; the companion IC3 and FBI advisories explain the victim-side infection model, while the Treasury release adds a sanctions and financial-disruption layer.

The target was not a single malware family in isolation. 911 S5 operated as a proxy infrastructure built from compromised residential devices, including infections tied to bundled or pirated VPN applications. That infrastructure let customers route traffic through victims' IP addresses and was used in fraud, identity theft, child exploitation activity, bomb threats, illegal transactions, and access-brokering.

## Participating Parties

| Role | Parties |
|---|---|
| Lead criminal authority | [[usdoj|U.S. Department of Justice]] |
| Investigative and victim-guidance authority | [[fbi|FBI]], including IC3-facing public guidance |
| Financial disruption | [[us-treasury|U.S. Department of the Treasury / OFAC]] |
| Named partner jurisdictions | [[germany|Germany]], [[singapore|Singapore]], [[thailand|Thailand]] |

## Results and Impact

- YunHe Wang, described in the DOJ source as the administrator of 911 S5, was arrested.
- The botnet was assessed in the official source set as affecting more than 19 million IP addresses across nearly 200 countries.
- IC3 and FBI guidance identified the residential-proxy infection path and gave cleanup guidance for affected users.
- OFAC sanctions targeted Wang, two associates, and three linked entities, showing that the disruption combined criminal process with financial restrictions.

## Cooperation Model

The action combines three layers: criminal investigation and arrest coordination by DOJ/FBI, partner-country assistance from Germany, Singapore, and Thailand, and a parallel Treasury/OFAC sanctions action. For dataset use, this page should therefore be read as a botnet-service disruption with both technical-remediation and financial-disruption components.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- U.S. Department of Justice, 2024-05-29: 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation.
- Internet Crime Complaint Center (IC3), 2024-05-29: Guidance on the 911 S5 Residential Proxy Service.
- Federal Bureau of Investigation, 2024-06-07: Inside the FBI Podcast: The 911 S5 Cyber Threat.
- U.S. Department of the Treasury, 2024-05-28: Treasury Sanctions a Cybercrime Network Associated with the 911 S5 Botnet.
- Federal Bureau of Investigation, 2024-05-29: How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors.

## Operational Timeline

- 2024-05: activity or investigation start.
- 2024-05: public announcement.
- 2024-05: reported enforcement endpoint.
- 2024-05-28: public source coverage from U.S. Department of the Treasury.
- 2024-05-29: public source coverage from Federal Bureau of Investigation, Internet Crime Complaint Center (IC3), U.S. Department of Justice.
- 2024-06-07: public source coverage from Federal Bureau of Investigation.

## Legal and Procedural Posture

- Recorded crime classification: malware and CSAM.
- The record is categorized as takedown with status completed.
- Related legal or operational records: Us V Yunhe Wang 911 S5.

## Evidence and Attribution Notes

- This DOJ Office of Public Affairs release is the principal public description of the May 2024 911 S5 disruption.
- It provides the operation date, arrest timing, global infection scale, and the seizure figures most useful for the corresponding operation and case pages.
- The U.S. Department of Justice and FBI, in cooperation with Germany, Singapore, and Thailand, dismantled the 911 S5 botnet -- the world's largest botnet, which had infected over 19 million IP addresses across nearly 200 countries.
- The botnet had been used to facilitate large-scale fraud, identity theft, child sexual exploitation, bomb threats, and illegal financial transactions.
- IC3 described 911 S5 as one of the largest residential proxy services and botnets, with more than 19 million compromised IP addresses in over 190 countries.
- The advisory identified the VPN applications tied to the proxy backdoor, including MaskVPN, DewVPN, PaladinVPN, ProxyGate, ShieldVPN, and ShineVPN.
- The advisory framed the botnet as a vehicle for fraud, identity theft, child exploitation, and initial access brokering.
- This public-service announcement gives the clearest victim-facing explanation of how 911 S5 spread through bundled VPN applications and pirated software.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- FBI, 2024-06-07: Title: Inside the FBI Podcast: The 911 S5 Cyber Threat | Federal Bureau of Investigation URL Source: Markdown Content: _[An energetic track featuring pulsating synthesizers begins.]_ **Narrator:** Downloading pirated content of any kind comes with inherent risks.
- FBI, 2024-06-07: The FBI and our partners recently caught bad cyber actors doing just that: using infected video games and software to hijack victims’ machines and commit cybercrimes—and then make it appear as though victims were the ones responsible for that illegal activity.
- U.S. Treasury, 2024-05-28: Department of the Treasury About Treasury Enter Search Term(s): Advanced Search General Information Role of the Treasury Officials Organizational Chart Orders and Directives Offices Domestic Finance Economic Policy General Counsel International Affairs Management Public Affairs Tax Policy Terrorism and Financial Intelligence Tribal and.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a takedown against 911 S5 Botnet, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Usdoj and coordination to Fbi, with participating or affected jurisdictions recorded as United States, Germany, Singapore, and Thailand.

The cooperation model is visible through DOJ/FBI criminal process, named partner jurisdictions, public victim guidance, and the related Treasury/OFAC financial-disruption action.

Operational results captured for the canonical record: 1 arrest; 1 indictment; disruption of a residential-proxy botnet affecting 19 million+ IP addresses; OFAC sanctions against the administrator network.

The canonical source set contains 5 reference(s): 2024 05 29 Justice Gov Justice Department Leads Effort To Dismantle 911 S5 Botnet, 2024 05 29 Ic3 Gov Guidance On The 911 S5 Residential Proxy Service, 2024 06 07 Fbi Gov The 911 S5 Cyber Threat, 2024 05 28 Treasury Gov Treasury Sanctions A Cybercrime Network Associated With The 911 S5 Botnet, 2024 05 29 Fbi Gov How To Identify And Remove Vpn Applications That Contain 911 S5 Backdoors.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
No frontmatter missing-field flags are currently carried on this page.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | 911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation | U.S. Department of Justice | 2024-05-29 | https://www.justice.gov/archives/opa/pr/911-s5-botnet-dismantled-and-its-administrator-arrested-coordinated-international-operation |
| [2] | Guidance on the 911 S5 Residential Proxy Service | IC3 | 2024-05-29 | https://www.ic3.gov/PSA/2024/PSA240529 |
| [3] | Inside the FBI Podcast: The 911 S5 Cyber Threat | FBI | 2024-06-07 | https://www.fbi.gov/news/podcasts/inside-the-fbi-podcast-the-911-s5-cyber-threat |
| [4] | Treasury Sanctions a Cybercrime Network Associated with the 911 S5 Botnet | U.S. Treasury | 2024-05-28 | https://home.treasury.gov/news/press-releases/jy2375 |
| [5] | How to Identify and Remove VPN Applications That Contain 911 S5 Backdoors | FBI | 2024-05-29 | https://www.fbi.gov/investigate/cyber/how-to-identify-and-remove-vpn-applications-that-contain-911-s5-backdoors |
