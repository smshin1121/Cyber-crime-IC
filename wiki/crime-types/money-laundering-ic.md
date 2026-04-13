---
type: crime-type
title: "Money Laundering (Cryptocurrency-Enabled) — International Cooperation Perspective"
aliases:
  - "money laundering"
  - "cryptocurrency laundering"
  - "crypto mixer"
  - "cryptocurrency mixing service"
  - "자금세탁"
crime_category: "cyber-enabled"
typical_ic_challenges:
  - "[[data-sovereignty]]"
  - "[[jurisdictional-conflicts]]"
relevant_legal_frameworks:
  - "[[budapest-convention]]"
typical_mechanisms:
  - "[[mlat-process]]"
  - "[[europol-jit]]"
key_organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
notable_operations:
  - "[[de-ch-crypto-mixer-takedown-2025]]"
  - "[[2bagoldmule-qqaazz]]"
  - "[[cryptex-pm2btc-sanctions]]"
notable_cases: []
criminalization_status:
  broadly_criminalized: true
  definition_varies: true
  problem_jurisdictions: []
estimated_annual_loss: "Tens of billions of USD globally; FATF and Chainalysis estimate hundreds of billions in laundered funds annually across all financial channels"
source_count: 1
sources:
  - "[[2025-12-01-eurojust-de-ch-crypto-mixer-takedown]]"
created: 2026-04-14
updated: 2026-04-14
---

## Summary

Money laundering — particularly **cryptocurrency-enabled money laundering** through mixing services, illicit exchanges, and obfuscation tooling — is a cross-cutting cybercrime enabler that converts the proceeds of nearly every other cybercrime category (ransomware, online fraud, drug trafficking, weapons trafficking, BEC) into spendable value. It is *almost certainly* the most internationally interconnected category of cybercrime activity, because illicit cryptocurrency flows by their nature cross every border with each on-chain hop.

This page focuses on the **international cooperation** dimension: how states and EU agencies coordinate to dismantle laundering infrastructure, freeze cryptocurrency, and prosecute the operators of mixers, swap services, and informal value-transfer networks.

## Criminalization Landscape

- **Broadly criminalized**: Money laundering is criminalized in nearly every jurisdiction, typically under standalone statutes (US 18 U.S.C. § 1956, EU 6th AML Directive, etc.).
- **Definition variation**: Whether *operating* a mixing service (as distinct from using one) is itself criminal varies. The US has prosecuted mixer operators under unlicensed money transmission and conspiracy theories; some EU states require a predicate offence linkage.
- **Crypto-specific gaps**: Regulatory perimeters around crypto-asset service providers (CASPs) under MiCA (EU) and FinCEN (US) are still maturing, leaving informal mixers in legal grey zones in some jurisdictions.

## Typical IC Scenarios

1. **Mixer takedown**: Authorities in the country hosting the mixer's infrastructure coordinate with destination-of-funds jurisdictions to seize servers and freeze cryptocurrency.
2. **Cross-jurisdictional asset tracing**: Multiple countries' financial intelligence units share blockchain analytics and bank account information.
3. **Operator extradition**: Mixer/exchange operators arrested in one country are extradited to a country where prosecutorial theory is more developed (often the US).

## Cooperation Pathways

- **[[europol-ec3|Europol EC3]]** provides cryptocurrency tracing and analytical support to EU member-state investigations.
- **[[eurojust|Eurojust]]** coordinates judicial cooperation, including for non-EU partners (e.g., Switzerland) under bilateral agreements.
- **[[mutual-legal-assistance|MLAT]]** processes are invoked for compelling production from exchanges and freezing assets in non-cooperative jurisdictions.
- **Bilateral DE-CH cooperation** (as in the [[de-ch-crypto-mixer-takedown-2025|December 2025 mixer takedown]]) is *highly likely* a routine pattern, given Switzerland's role as a global financial hub and Germany's role as a major EU enforcement actor.

## Key Operations and Precedents

| Operation | Year | Countries | Outcome |
|-----------|------|-----------|---------|
| [[de-ch-crypto-mixer-takedown-2025]] | 2025 | DE, CH | EUR 25M+ seized, 3 servers down |
| [[cryptex-pm2btc-sanctions]] | 2024 | US-led | Sanctions and indictments |
| [[2bagoldmule-qqaazz]] | 2020 | EU + US | Money mule network dismantled |

## Challenges

- **Speed of crypto flows**: Funds can be moved in seconds across many wallets, outpacing MLA timelines.
- **Mixer deniability**: Operators routinely claim "no knowledge" of customers' criminal proceeds.
- **Jurisdiction shopping**: Mixer hosts are frequently relocated across friendly jurisdictions in response to enforcement pressure.
- **Privacy coin obfuscation**: Monero and similar privacy-preserving chains complicate tracing.

## Korean Context (한국 상황)

[[south-korea|South Korea]]'s position is *likely* significant given its large cryptocurrency exchange market (Upbit, Bithumb) and historical exposure to North Korean DPRK laundering. The Korean Financial Intelligence Unit (KoFIU) cooperates internationally on suspicious cryptocurrency transactions. No direct Korean involvement is documented in the [[de-ch-crypto-mixer-takedown-2025|December 2025 DE-CH mixer takedown]].

## Contradictions & Open Questions

- The exact mixing service taken down in the December 2025 DE-CH operation is not named in the Eurojust release. Identification awaits follow-up reporting.
- The legal basis under which Switzerland (a non-EU state) cooperated with Eurojust in this operation is *likely* the bilateral Eurojust-Switzerland agreement, but is not confirmed in the source.
