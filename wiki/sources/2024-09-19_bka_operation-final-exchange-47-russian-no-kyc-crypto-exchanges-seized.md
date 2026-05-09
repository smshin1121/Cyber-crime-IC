---
type: source
title: "BKA / ZIT: Cybercrime — Erfolgreicher Schlag gegen die Infrastruktur von digitalen Geldwäschern der Underground Economy (Operation Final Exchange)"
collection_url: https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2024/Presse2024/240919_PM_finalexchange.html
collection_domain: bka.de
source_type: press-release
publisher: "Bundeskriminalamt (BKA) / Generalstaatsanwaltschaft Frankfurt am Main – ZIT"
author: ""
publish_date: 2024-09-19
ingest_date: 2026-05-09
language: de
reliability: high
credibility: confirmed
sensitivity: public
source_class: tier-1-primary-with-tier-2-corroboration
source_tier: 1
pages_updated:
  - operation-final-exchange-bka-russian-crypto-exchanges-2024
key_findings:
  - "BKA and ZIT Frankfurt jointly shut down 47 Germany-hosted no-KYC cryptocurrency exchange services on 19 September 2024, targeting Russian-language platforms used by ransomware groups, darknet vendors, and botnet operators."
  - "Statutory basis cited verbatim in the BKA press release: §§ 127, 261 Abs. 1 Satz 1 Nr. 2 und Abs. 4 StGB (operating criminal trading platforms on the internet + aggravated money laundering)."
  - "Development, production, and backup servers were seized along with transaction data, registration data, and IP addresses; named exchanges include Xchange.cash, Bankcomat.com, 60cek.org, CoinBlinker.com, Cryptostrike, Baksman, Prostocash, and Multichange.net."
  - "No arrests were announced in the 19 September 2024 release; the action is an infrastructure seizure rather than an arrest sweep, in line with the BKA pattern earlier seen with ChipMixer (2023), Qakbot, Emotet, and Operation Endgame."
created: 2026-05-09
raw_path: raw/press-releases/2024-09-19_bka_operation-final-exchange-47-russian-no-kyc-crypto-exchanges-seized.md
text_status: summarized
storage_mode: summary-only
copyright_policy: summary-only
---
## Source Summary

This is the **tier-1 primary German-language press release** issued jointly by the Bundeskriminalamt (BKA) and the Generalstaatsanwaltschaft Frankfurt am Main – Zentralstelle zur Bekämpfung der Internetkriminalität (ZIT) on 19 September 2024 announcing **Operation Final Exchange**: the seizure of the infrastructure of 47 Germany-hosted, Russian-language, no-KYC cryptocurrency exchange services. The release frames the takedown as an attack on the **digital money-laundering layer** of the cybercrime underground economy, naming ransomware groups, darknet vendors, and botnet operators as the principal client base of the targeted platforms.

The BKA URL was directly readable on 2026-05-09. The Wayback Machine had no archived snapshot of the BKA URL at that time, but the BKA primary text was supplemented by tier-2 corroboration from Heise Online (English edition), TheRecord (Recorded Future News), Chainalysis, AMLP Forum, Infosecurity Magazine, and Duane Morris ESE blog. Highly likely (>90%) that the named-exchange list and the Xchange.cash transaction/user statistics reflect the BKA's own briefing material because the same figures recur across independent secondary outlets.

## Statutory Citation (verbatim)

> §§ 127, 261 Abs. 1 Satz 1 Nr. 2 und Abs. 4 StGB

This is the formal charging basis carried in the BKA press release: § 127 StGB (Betreiben krimineller Handelsplattformen im Internet — operating criminal trading platforms on the internet, the relatively new offence introduced as part of Germany's 2021 cybercrime amendments) plus § 261 StGB (Geldwäsche — money laundering), aggravated form.

## Relevance to IC

This source is the strongest publicly available anchor in the wiki for:

1. **No-KYC instant-swap exchange ecosystem as a discrete IC target.** Unlike mixer takedowns ([[treasury-sinbad-mixer-dprk-lazarus-sanctions-2023]], [[de-ch-crypto-mixer-takedown-2025]]) that target a single mixing service, Operation Final Exchange struck **47 platforms simultaneously** — the largest single-action seizure of cryptocurrency-laundering infrastructure on the BKA timeline.
2. **Use of § 127 StGB for IC infrastructure takedowns.** The 2021 German offence of "operating criminal trading platforms on the internet" allows seizure on the basis of platform-design intent (no-KYC + facilitation knowledge) without requiring proof of specific predicate crimes. This is a model worth comparing against U.S. Bank Secrecy Act / 18 U.S.C. § 1960 (unlicensed money transmitting) charges in cases like [[operation-russian-nationals-charged-with-hacking-one-cryptocurrency-exchange-and-illicitly-operating-another]].
3. **Unilateral German action against Russian-language infrastructure.** Russia is not a participating state. This is a single-jurisdiction infrastructure takedown enabled by the fact that the targeted servers were physically Germany-hosted, regardless of who operated them or who used them. This pattern mirrors [[de-ch-crypto-mixer-takedown-2025]] (DE-CH bilateral) but without the cross-border partner.
4. **BKA infrastructure-takedown chronology.** The release explicitly chains Final Exchange to ChipMixer (2023), Qakbot, Emotet, and [[operation-endgame|Operation Endgame]] (2024), positioning this as part of an ongoing strategic shift from individual prosecutions (often blocked by the absence of an extradition treaty with Russia) to **infrastructure denial**.

## Notable Named Exchanges

| Exchange | Notes |
|----------|-------|
| Xchange.cash | Top by transaction volume; ~410,000 user accounts; ~1.28–1.3M transactions processed (per Chainalysis / The Record) |
| Bankcomat.com | Operating since 2012 (per Heise / The Record); among top three by transactions |
| 60cek.org | Among top three by transactions (per Chainalysis) |
| CoinBlinker.com | Named in BKA-aligned coverage |
| Cryptostrike | Named in The Record |
| Baksman | Named in The Record |
| Prostocash | Named in The Record |
| Multichange.net | Named in Infosecurity Magazine |

> [!warning] Contradiction
> **Claim A** (The Record, 20 Sep 2024, reliability: medium): Xchange.cash has been operating "since 2012."
> **Claim B** (Heise / Chainalysis, reliability: medium-high): **Bankcomat.com** has been operating since 2012; Xchange.cash has been operating since 2016 or before.
> **Assessment**: Claim B is *likely* correct — Chainalysis and Heise both source the 2012 figure to Bankcomat, and the 2016+ figure to Xchange.cash; The Record appears to have conflated the two.

## Storage Mode

Stored in **summary-only** mode in compliance with BKA copyright. Direct quotations limited to short statutory citations and short factual elements (splash-banner text, named platforms). The full press-release text remains at the BKA URL.
