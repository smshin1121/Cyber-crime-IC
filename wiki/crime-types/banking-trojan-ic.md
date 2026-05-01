---
type: crime-type
title: "Banking Trojan Operations"
aliases:
  - "banking malware"
  - "banking trojan"
crime_category: cyber-dependent
typical_ic_challenges:
  - "credential theft evidence"
  - "money mule networks"
  - "victims and banks in several countries"
relevant_legal_frameworks:
  - "[[budapest-convention]]"
typical_mechanisms:
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[asset-freezing]]"
  - "[[public-private-cooperation]]"
key_organizations:
  - "[[europol-ec3]]"
  - "[[fbi]]"
  - "[[uk-nca]]"
  - "[[eurojust]]"
notable_operations:
  - "[[zeus-spyeye-jit-takedown]]"
  - "[[banking-trojan-fraud-sentencing-2017]]"
notable_cases:
  []
criminalization_status:
  broadly_criminalized: true
  definition_varies: true
  problem_jurisdictions:
    []
estimated_annual_loss: ""
source_count: 4
sources:
  - "[[2019-05-01_europol-europa-eu_goznym-malware-cybercriminal-network-dismantled-in-international-operation]]"
  - "[[2015-10-13_justice-gov_bugat-botnet-administrator-arrested-and-malware-disabled]]"
  - "[[2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware]]"
  - "[[2019-12-05_thehackernews-com_fbi-puts-5-million-bounty-on-russian-hackers-behind-dridex-banking-malware]]"
created: 2026-04-17
updated: "2026-04-29"
status: active
---
## Summary

Banking-trojan cooperation cases focus on malware designed to steal online-banking credentials, manipulate sessions, or support fraudulent transfers. These cases frequently combine cyber intrusion evidence with financial-crime evidence. The malware operator, botnet administrator, money mule recruiter, cash-out layer, victim bank, and hosting provider may all sit in different countries.

## Cooperation Pattern

GozNym, Bugat/Dridex, Zeus, and SpyEye records show why banking-trojan cases often require several cooperation tracks at once. Technical disruption can neutralize botnet infrastructure, but prosecution usually also needs victim-bank records, account-opening evidence, payment traces, and evidence tying defendants to malware administration or mule management. Public-private support matters because banks and security companies often detect command-and-control infrastructure and money-mule patterns before a formal action day.

## Menu Use

Use this page where the malware's primary purpose is online-banking theft or unauthorized funds transfer. Use [[malware-ic]] for broader malware families and [[money-mule-networks]] when the source mainly documents recruitment, account control, or laundering after the initial credential theft. The distinction prevents the same operation from being reduced to either a purely technical botnet case or a purely financial-fraud case.

## Analytical Use

Within this wiki, **Banking Trojan Operations** is a control node for comparing records that describe the offense pattern, evidence sources, and cross-border investigative pressure points. Use the page to separate three questions that often become mixed in operation narratives: what conduct or authority is being discussed, which agency or state actor exercised it, and where the cross-border dependency appears in the evidence chain. That separation makes the menu more useful for comparing takedowns, prosecutions, extradition matters, and assistance requests without treating every related record as the same kind of cooperation event.

## Integrity Notes

The page groups terminology; it is not independent proof that the concept, crime type, mechanism, or framework applied in every linked matter. Operation and case pages remain the controlling records for arrests, seizures, requests, treaty use, and participating agencies. When adding future links, keep the distinction between direct source evidence, inferred analytical classification, and catalog navigation visible in the target page.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2019-05-01_europol-europa-eu_goznym-malware-cybercriminal-network-dismantled-in-international-operation|Goznym Malware Cybercriminal Network Dismantled In International Operation]] | Europol | 2019-05-01 | https://www.europol.europa.eu/media-press/newsroom/news/goznym-malware-cybercriminal-network-dismantled-in-international-operation |
| [2] | [[2015-10-13_justice-gov_bugat-botnet-administrator-arrested-and-malware-disabled|Bugat Botnet Administrator Arrested and Malware Disabled]] | US DOJ | 2015-10-13 | https://www.justice.gov/opa/pr/bugat-botnet-administrator-arrested-and-malware-disabled |
| [3] | [[2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware|Europol Arrests Gang Behind Zeus and SpyEye Banking Malware]] | The Hacker News | 2015-06-27 | https://thehackernews.com/2015/06/zeus-spyeye-banking-malware.html?m=1 |
| [4] | [[2019-12-05_thehackernews-com_fbi-puts-5-million-bounty-on-russian-hackers-behind-dridex-banking-malware|FBI Puts $5 Million Bounty On Russian Hackers Behind Dridex Banking Malware]] | The Hacker News | 2019-12-05 | https://thehackernews.com/2019/12/dridex-russian-hackers-wanted-by-fbi.html |
