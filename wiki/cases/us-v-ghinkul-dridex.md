---
type: case
title: "United States v. Ghinkul (Bugat/Dridex)"
case_number: "W.D. Pa. indictment announced 2015-10-13"
jurisdiction: "U.S. District Court, Western District of Pennsylvania"
jurisdiction_country: "[[united-states]]"
case_type: prosecution
status: sentenced
crime_charged:
  - "[[malware-ic]]"
  - "[[online-fraud-ic]]"
defendants:
  - name: "Andrey Ghinkul"
    nationality: Moldovan
    status: sentenced
    sentence: "Time served"
    location_at_arrest: Cyprus
related_operation: "[[dridex-operations]]"
ic_elements:
  mlat_requests:
    - Cyprus
    - "United Kingdom"
    - Moldova
  extradition: "Ghinkul was arrested in Cyprus and extradited to the United States in February 2016."
  evidence_from_abroad:
    - Cyprus
    - "United Kingdom"
    - Moldova
  foreign_arrests:
    - Cyprus
  asset_freezing:
    []
cooperating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[uk-nca]]"
  - "[[us-doj]]"
legal_frameworks_invoked:
  - "[[computer-fraud-and-abuse-act]]"
  - "[[wire-fraud-statute]]"
mechanisms_used:
  - "[[mutual-legal-assistance]]"
  - "[[extradition-request]]"
key_legal_issues:
  - "[[jurisdictional-conflicts]]"
  - "[[data-sovereignty]]"
precedent_value: "High - Ghinkul is the only Dridex operator case in the repository that progressed from foreign arrest to U.S. extradition and sentence, making it the clearest custody anchor for the broader Dridex/Evil Corp operation."
source_count: 1
sources:
  - "[[2015-10-13_wdpa_ghinkul-bugat-dridex-indictment]]"
created: 2026-04-17
updated: 2026-04-17
summary: "United States v. Ghinkul is the arrest-and-extradition phase of the broader [[dridex-operations|Dridex/Evil Corp disruption and prosecution]]. It is the repository's most concrete Dridex case involving actual custody over an operator."
---
## Summary

United States v. Ghinkul is the arrest-and-extradition phase of the broader [[dridex-operations|Dridex/Evil Corp disruption and prosecution]]. It is the repository's most concrete Dridex case involving actual custody over an operator.

## Facts

DOJ alleged that Ghinkul helped administer the Bugat/Dridex botnet and participated in conspiracy, unauthorized computer access, computer damage, wire fraud, and bank fraud. The public materials connect him to a malware ecosystem that targeted bank accounts and fraudulent transfers in the United States.

The same day DOJ announced the indictment, law enforcement and private-sector partners also carried out a technical disruption of the Dridex peer-to-peer botnet. That makes this case especially useful because it sits at the intersection of prosecution and technical takedown.

## International Cooperation Elements

### Evidence Gathering

The case relied on multinational coordination among the FBI, the UK National Crime Agency, and other partners working on the Dridex disruption. The evidentiary picture therefore went beyond a single-country arrest request.

### Arrest and Extradition

Ghinkul was arrested in Cyprus in August 2015 and extradited to the United States in February 2016. He later pleaded guilty and was sentenced to time served in December 2018.

### Asset Recovery

The public materials emphasize botnet disruption rather than forfeiture. The more important asset-denial outcome was temporary operational control over Dridex command channels through sinkholing.

## Legal Analysis

### Jurisdiction

The Western District of Pennsylvania had a direct U.S. nexus because the indictment tied the malware conduct to bank-fraud and wire-fraud effects within the district, including attempted fraudulent transfers involving Pennsylvania victims.

### Key Legal Issues

- **Transit-state extradition:** The case demonstrates how an operator from a non-U.S. and non-Russian-protective environment could still be brought to U.S. court through arrest in a cooperative third country.
- **Case-plus-disruption model:** It also shows how a technical sinkholing action can be paired with a criminal prosecution instead of being treated as a purely defensive network event.

### Precedent Value

The case has *high* value because it is the most concrete proof in the Dridex record that international cooperation produced a real defendant in U.S. court, not only at-large indictments and sanctions.

## Proceedings Timeline

| Date | Event |
|------|-------|
| 2015-08 | Ghinkul arrested in Cyprus |
| 2015-10-13 | DOJ announces Ghinkul indictment and Dridex disruption |
| 2016-02 | Ghinkul extradited to the United States |
| 2017-02 | Ghinkul pleads guilty |
| 2018-12-06 | Ghinkul sentenced to time served |

## Cooperation Effectiveness

The case suggests that the Dridex operation's first phase was operationally effective because it combined arrest, extradition, and botnet disruption. Its limitation was strategic rather than tactical: the principal Evil Corp leadership still remained outside U.S. custody.

## Korean Relevance

No South Korean role is identified in the collected source. The case remains relevant because banking-trojan operations often require exactly this mix of third-country arrest, technical disruption, and multinational evidence coordination.

## Contradictions & Open Questions

1. Public materials do not fully explain why Ghinkul ultimately received a time-served sentence.
2. The collected source does not disclose the full plea terms or cooperation posture.
3. The division of responsibility between Ghinkul and later-indicted Evil Corp leadership remains only partially described in public summaries.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Bugat Botnet Administrator Arrested and Malware Disabled | DOJ OPA / W.D. Pa. | 2015-10-13 | https://www.justice.gov/opa/pr/bugat-botnet-administrator-arrested-and-malware-disabled |
