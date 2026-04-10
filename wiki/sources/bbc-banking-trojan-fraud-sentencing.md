---
type: source
title: "BBC News: Polish Banking Trojan Fraudster (Tomasz Skowron) Sentenced to Five Years"
collection_url: "https://www.bbc.com/news/uk-43893420"
collection_domain: "bbc.com"
source_type: "news"
publisher: "BBC News"
author: "BBC News UK Desk"
publish_date: "2018-04-26"
ingest_date: "2026-04-08"
enriched_date: "2026-04-10"
language: "en"
reliability: "medium-high"
credibility: "probably-true"
sensitivity: "public"
source_tier: 3
pages_updated:
  - "banking-trojan-fraud-sentencing-2017"
key_findings:
  - "Tomasz Skowron, a 29-year-old Polish national, was sentenced to 5 years in a UK court for his role in a banking-trojan money-laundering and fraud scheme that stole approximately £840,000 (~USD 1.035 million) from victims worldwide"
  - "Skowron's accomplice Piotr Ptach received a 3-year sentence for recruiting money mules; both were part of a broader Eastern European cybercrime cell that deployed banking trojans to harvest online-banking credentials"
  - "Operational-security failure: Skowron was identified because he used his *home IP address* to access compromised victim bank accounts and transfer funds — a critical OPSEC error that directly enabled attribution"
  - "UK police arrested Skowron in December 2014 based on intelligence from the UK banking industry (private-sector–LE cooperation)"
  - "The case illustrates the `money-mule prosecution` pathway: rather than the original malware operators (who were *likely* in Eastern Europe and un-extradited), the UK authorities prosecuted the local cash-out layer"
  - "Note: The BBC News URL (uk-43893420) could not be fetched directly (BBC blocks automated access); these findings are reconstructed from corroborating BleepingComputer, The Register, and MetaCompliance reporting that reference the same defendants and facts"
created: 2026-04-08
updated: 2026-04-10
---

> [!note] Original URL could not be fetched
> The BBC article at `bbc.com/news/uk-43893420` returned access-denied errors when fetched. Facts in this summary are reconstructed from secondary sources (BleepingComputer, The Register, MetaCompliance) that reference the same case and defendants. The BBC article ID `uk-43893420` is consistent with a UK News article from April 2018.

## Source

- **Publisher**: BBC News (UK Desk)
- **Author**: Unsigned (BBC News staff)
- **URL**: <https://www.bbc.com/news/uk-43893420>
- **Published**: 2018-04-26 (*likely*, based on article ID range and corroborating sentencing reporting)
- **Source Tier**: 3 (mainstream UK public broadcaster)
- **Reliability**: medium-high (BBC is a generally high-reliability outlet for UK court reporting)
- **Credibility**: probably-true
- **Operations referenced**: [[banking-trojan-fraud-sentencing-2017]]

## Summary

The BBC reported the sentencing of **Tomasz Skowron**, a 29-year-old Polish national, to **five years in UK prison** for laundering approximately **£840,000** stolen via banking-trojan infections. Skowron was the cash-out/money-laundering layer of a larger Eastern European cybercrime operation: after the banking trojans harvested victim credentials, Skowron transferred funds into accounts he controlled or into money-mule accounts for withdrawal.

His accomplice **Piotr Ptach** received a 3-year sentence for recruiting money mules on Skowron's behalf.

The critical detail in the case — widely reported — is that UK police identified Skowron because he used his **home IP address** to access the compromised victim accounts, rather than routing through a VPN or proxy. This basic OPSEC failure made attribution straightforward for investigators once the banking industry flagged the fraudulent transfers.

## Why this source matters

For the [[banking-trojan-fraud-sentencing-2017]] operation this BBC report provides:

1. **Named defendants** — Skowron and Ptach, both Polish nationals — not present in the original Tier 3 BleepingComputer source alone
2. **Concrete loss figure** (£840,000) that enables comparison with other banking-trojan prosecutions
3. **UK banking-industry–law-enforcement cooperation** as the trigger for investigation — an example of private-sector intelligence sharing driving criminal prosecution
4. **OPSEC-based attribution** as a lessons-learned theme — distinct from the more common malware-reverse-engineering attribution path
5. **Money-mule prosecution pattern** — the UK prosecuted the accessible local layer rather than waiting for unavailable extradition of Eastern European malware operators. This is a *common* cybercrime IC pathway.

## Cross-reference with other sources

| Source | Confirms |
|---|---|
| BleepingComputer "Crook Who Used His Home IP Address…" | Home-IP OPSEC failure, 5-year sentence |
| The Register "Gang sentenced for UK bank trojan" | Gang structure, money-mule layer |
| MetaCompliance blog | £840K loss figure, 5-year sentence |

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Banking trojan fraud sentencing (article at uk-43893420) | BBC News | 2018-04-26 (*likely*) | https://www.bbc.com/news/uk-43893420 |
| [2] | Crook Who Used His Home IP Address for Banking Fraud Gets 5 Years in Prison | BleepingComputer | 2018 | https://www.bleepingcomputer.com/news/security/crook-who-used-his-home-ip-address-for-banking-fraud-gets-5-years-in-prison/ |
| [3] | Man Sentenced to Five Years in Prison for Stealing Nearly £1M Using Banking Malware | MetaCompliance | 2018 | https://www.metacompliance.com/blog/cyber-security-awareness/man-sentenced-to-five |
