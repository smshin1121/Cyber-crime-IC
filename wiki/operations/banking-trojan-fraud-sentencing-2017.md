---
aliases:

case_id: CYB-2017-051
challenges_encountered:

coordinating_body: ""
created: 2026-04-08
credibility_index: 2.55
crime_type: "[[banking-trojan-ic]]"
edges:

enforcement_type:

lead_agency: ""
legal_basis:

lessons_learned:

mechanisms_used:

missing_fields:

operation_type: joint-investigation
outcome: success
participating_agencies:

participating_countries:

period: 1
related_cases:

related_operations:

results:
  arrests: 1
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 1
  other:

  servers_seized: 0
  victims_notified: 0
source_count: 5
source_tier: 3
sources:
  - "[[bbc-banking-trojan-fraud-sentencing]]"
  - "[[2025-06-25_helpnetsecurity-com_the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans]]"
  - "[[2015-06-25_scworld-com_europol-takes-down-high-profile-ukraine-based-cybergang]]"
  - "[[2015-06-27_thehackernews-com_europol-arrests-gang-behind-zeus-and-spyeye-banking-malware]]"
  - "[[2015-06-29_techmonitor-ai_zeus-spyeye-malware-gang-members-arrested-in-ukraine]]"
status: absorbed
target_entity: "Banking fraud perpetrator (used home IP)"
timeframe:
  announced: 2017-01-01
  end: 2017-12-31
  ongoing: false
  start: 2017-01-01
title: "Banking Trojan Fraud Sentencing"
title_ko: "뱅킹 트로이목마 사기 판결"
type: operation
updated: 2026-04-26
operation_role: follow-on
parent_operation: "[[zeus-spyeye-jit-takedown]]"
summary: "A cybercriminal who used banking trojans for financial fraud was sentenced to **5 years in prison** after being identified in part because he used his home IP address during the fraud. The case illustrates how basic operational security failures can enable law enforcement to identify and prosecute cybercriminals even in technically sophisticated fraud schemes."
crime_types:
  - "[[banking-trojan-ic]]"
  - "[[malware-ic]]"
---
> [!note] This operation is documented from a Tier 3 (cybersecurity media) source. Additional verification from official sources (Tier 1-2) would strengthen data reliability.

## Summary

A cybercriminal who used banking trojans for financial fraud was sentenced to **5 years in prison** after being identified in part because he used his home IP address during the fraud. The case illustrates how basic operational security failures can enable law enforcement to identify and prosecute cybercriminals even in technically sophisticated fraud schemes.

## Background

Banking trojan fraud involves deploying malware that intercepts online banking sessions to steal credentials and redirect funds. While the technical aspects of such attacks can be sophisticated, the perpetrator in this case made a critical error by conducting fraudulent activities from his home IP address, making identification straightforward for investigators.

## Participating Parties

> [!warning] Legal status check needed
> The specific law enforcement agencies and any international cooperation elements need verification from official sources.

## Legal Framework

Specific legal details beyond the 5-year sentence are not available from the Tier 3 source.

## Operational Timeline

| Date | Event |
|------|-------|
| ~2017 | Sentencing: 5-year prison term for banking trojan fraud |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Arrests | 1 |
| Sentence | 5 years in prison |

## Cooperation Mechanisms Used

Not detailed in available Tier 3 source.

## Lessons Learned

1. **OpSec failures enable prosecution:** The use of a home IP address for criminal activity provided investigators with a direct link to the perpetrator's identity.

## Korean Involvement (한국의 참여)

No Korean involvement identified.

## Contradictions & Open Questions

- What was the suspect's nationality and where was the prosecution?
- Were there international cooperation elements in the investigation?
- What was the total financial loss attributed to the scheme?
- What specific banking trojan was used?

## Follow-Up Actions

> [!warning] No public court documents found
> Web search (2026-04-17) yielded no publicly accessible court filings
> for this operation. Possible reasons: non-US jurisdiction with no
> public court records system, sealed proceedings, or operation did
> not result in formal prosecution.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- BBC News, 2018-04-26: BBC News: Polish Banking Trojan Fraudster (Tomasz Skowron) Sentenced to Five Years.
- Help Net Security, 2015-06-25: The downfall of a major cybercrime ring exploiting banking Trojans.
- SC Media, 2015-06-25: Europol takes down high profile Ukraine-based cybergang.
- The Hacker News, 2015-06-27: Europol Arrests Gang Behind Zeus and SpyEye Banking Malware.
- Tech Monitor, 2015-06-29: Zeus & SpyEye malware gang members arrested in Ukraine.

## Evidence and Attribution Notes

- Tomasz Skowron, a 29-year-old Polish national, was sentenced to 5 years in a UK court for his role in a banking-trojan money-laundering and fraud scheme that stole approximately £840,000 (~USD 1.035 million) from victims worldwide
- Skowron's accomplice Piotr Ptach received a 3-year sentence for recruiting money mules; both were part of a broader Eastern European cybercrime cell that deployed banking trojans to harvest online-banking credentials
- Operational-security failure: Skowron was identified because he used his *home IP address* to access compromised victim bank accounts and transfer funds — a critical OPSEC error that directly enabled attribution
- UK police arrested Skowron in December 2014 based on intelligence from the UK banking industry (private-sector–LE cooperation)
- The case illustrates the money-mule prosecution pathway: rather than the original malware operators (who were *likely* in Eastern Europe and un-extradited), the UK authorities prosecuted the local cash-out layer
- Note: The BBC News URL (uk-43893420) could not be fetched directly (BBC blocks automated access); these findings are reconstructed from corroborating BleepingComputer, The Register, and MetaCompliance reporting that reference the same defendants and facts
- Help Net Security summarized the JIT action in Ukraine against Zeus and SpyEye actors.
- The report described five arrests, house searches, and seizure of devices.

<!-- SOURCE_ENRICHMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | BBC News: Polish Banking Trojan Fraudster (Tomasz Skowron) Sentenced to Five Years | BBC News | 2018-04-26 | https://www.bbc.com/news/uk-43893420 |
| [2] | The downfall of a major cybercrime ring exploiting banking Trojans | Help Net Security | 2015-06-25 | https://www.helpnetsecurity.com/2015/06/25/the-downfall-of-a-major-cybercrime-ring-exploiting-banking-trojans/ |
| [3] | Europol takes down high profile Ukraine-based cybergang | SC Media | 2015-06-25 | https://www.scworld.com/news/europol-takes-down-high-profile-ukraine-based-cybergang |
| [4] | Europol Arrests Gang Behind Zeus and SpyEye Banking Malware | The Hacker News | 2015-06-27 | https://thehackernews.com/2015/06/zeus-spyeye-banking-malware.html?m=1 |
| [5] | Zeus & SpyEye malware gang members arrested in Ukraine | Tech Monitor | 2015-06-29 | https://www.techmonitor.ai/hardware/zeus-spyeye-malware-gang-members-arrested-in-ukraine-4611234 |
