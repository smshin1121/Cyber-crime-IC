---
type: case
title: "United States v. Yakubets and Turashev (Dridex/Evil Corp)"
case_number: "W.D. Pa. (10-count); D. Neb."
jurisdiction: "U.S. District Court, Western District of Pennsylvania; U.S. District Court, District of Nebraska"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: indicted
crime_charged:
  - "[[online-fraud-ic]]"
  - "[[malware-ic]]"
defendants:
  - name: "Maksim V. Yakubets"
    nationality: Russian
    status: fugitive
    sentence: ""
    location_at_arrest: "At large (Moscow, Russia)"
  - name: "Igor Turashev"
    nationality: Russian
    status: fugitive
    sentence: ""
    location_at_arrest: "At large (Russia)"
  - name: "Andrey Ghinkul"
    nationality: Moldovan
    status: sentenced
    sentence: "Time served"
    location_at_arrest: Cyprus
related_operation: "[[dridex-operations]]"
ic_elements:
  mlat_requests:
    - "United Kingdom"
    - Moldova
  extradition: "Ghinkul (Cyprus to US, 2016)"
  evidence_from_abroad:
    - "United Kingdom"
    - Germany
    - Moldova
    - Cyprus
  foreign_arrests:
    - "Cyprus (Ghinkul, August 2015)"
  asset_freezing:
    - "OFAC sanctions: "17 individuals, 7 entities (Evil Corp)\""
cooperating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[uk-nca]]"
  - "[[us-doj]]"
  - "[[us-treasury]]"
  - "[[europol-ec3]]"
  - "[[germany-bka]]"
legal_frameworks_invoked:
  - "[[mlat-process]]"
mechanisms_used:
  - "[[mlat-process]]"
key_legal_issues:
  - "[[data-sovereignty]]"
precedent_value: "Landmark — combined indictment + sanctions + reward approach; USD 5 million reward (largest cyber reward at the time); sanctions imposed on cybercriminal organization"
source_count: 2
sources:
  - "[[2019-12-05_wdpa_yakubets-turashev-dridex-indictment]]"
  - "[[2015-10-13_wdpa_ghinkul-bugat-dridex-indictment]]"
created: 2026-04-12
updated: 2026-04-12
summary: "United States v. Yakubets and Turashev is the December 2019 indictment of Maksim V. Yakubets (aka \"aqua\"), leader of the Evil Corp cybercriminal organization, and Igor Turashev for conspiracy, computer hacking, wire fraud, and bank fraud related to the Dridex (Bugat/Cridex) banking trojan. The Dridex malware infected computers in 40+ countries and caused over USD 100 million in theft."
---
## Summary

United States v. Yakubets and Turashev is the December 2019 indictment of Maksim V. Yakubets (aka "aqua"), leader of the Evil Corp cybercriminal organization, and Igor Turashev for conspiracy, computer hacking, wire fraud, and bank fraud related to the Dridex (Bugat/Cridex) banking trojan. The Dridex malware infected computers in 40+ countries and caused over USD 100 million in theft.

The case is *almost certainly* the most significant example of the US government's "three-pronged" approach to cybercrime: combining criminal indictment, OFAC economic sanctions (17 individuals, 7 entities), and a USD 5 million reward — the largest cyber reward at the time of announcement.

## Facts

Evil Corp is a Russia-based cybercriminal organization led by Yakubets and operating primarily from Moscow. The Dridex malware evolved through several versions (Cridex, Bugat v4, Dridex/Bugat v5) and spread through phishing emails containing malicious Microsoft Office documents. According to the US Treasury, Yakubets also provided direct assistance to the Russian government's malicious cyber efforts, highlighting the nexus between state-sponsored and criminal cyber operations.

## International Cooperation Elements

### FBI-NCA Joint Investigation

The FBI (Pittsburgh Field Office) and UK National Crime Agency conducted a parallel investigation, with evidence sharing facilitated by the US-UK MLAT.

### Ghinkul Arrest and Extradition

Andrey Ghinkul, a Dridex botnet administrator, was arrested in Cyprus in August 2015, extradited to the US in February 2016, and sentenced to time served in December 2018.

### Technical Disruption

On 13 October 2015, the FBI, NCA, Dell SecureWorks, and Shadowserver Foundation executed a botnet sinkholing operation against the Dridex P2P network.

### Sanctions

OFAC designated 17 individuals and 7 entities associated with Evil Corp under the International Emergency Economic Powers Act (IEEPA), freezing all US-jurisdictional assets.

## Legal Analysis

### Precedent Value

**Landmark.** The combined indictment + sanctions + reward approach became a template for subsequent cybercrime enforcement actions, particularly against Russian-origin groups where arrest is not feasible. The OFAC sanctions imposed real economic costs on Evil Corp and created legal complications for any entity interacting with designated individuals.

## Proceedings Timeline

| Date | Event |
|------|-------|
| 2015-08 | Ghinkul arrested in Cyprus |
| 2015-10-13 | Ghinkul indictment announced; Dridex botnet sinkholed |
| 2016-02 | Ghinkul extradited to US |
| 2018-12-06 | Ghinkul sentenced to time served |
| 2019-12-05 | Yakubets and Turashev indictment unsealed |
| 2019-12-05 | OFAC sanctions against Evil Corp |
| 2019-12-05 | USD 5 million reward announced |

## Cooperation Effectiveness

The FBI-NCA bilateral cooperation is *almost certainly* a model for US-UK cybercrime investigations. However, the principal targets (Yakubets and Turashev) remain at large in Russia, and Evil Corp subsequently pivoted to ransomware operations — an outcome assessment of **partial success**.

## Korean Relevance (한국 관련성)

No Korean involvement identified. However, the sanctions-based enforcement model is relevant as a reference for Korean authorities considering how to apply economic pressure on cybercriminal organizations beyond traditional prosecution.

## Contradictions & Open Questions

1. Yakubets's alleged ties to Russian government cyber operations raise questions about state protection.
2. Evil Corp's pivot to ransomware (WastedLocker, Hades) after sanctions undermines the effectiveness narrative.
3. The USD 5 million reward has not resulted in Yakubets's arrest as of April 2026.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Russian National Charged (Dridex/Evil Corp) | DOJ OPA | 2019-12-05 | https://www.justice.gov/archives/opa/pr/russian-national-charged-decade-long-series-hacking-and-bank-fraud-offenses-resulting-tens |
| 2 | Yakubets/Turashev Indictment PDF | DOJ | 2019-12-05 | https://www.justice.gov/opa/press-release/file/1223586/download |
| 3 | Bugat Botnet Administrator Arrested | DOJ W.D. Pa. | 2015-10-13 | https://www.justice.gov/usao-wdpa/pr/major-computer-hacking-forum-dismantled |
