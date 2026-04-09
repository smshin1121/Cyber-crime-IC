---
administered_by: ''
aliases:
- voluntary disclosure
- provider-direct request
- direct access to subscriber information
- direct request to service provider
cases_using: []
created: 2026-04-10
formality: semi-formal
legal_basis:
- '[[cloud-act]]'
- '[[second-additional-protocol]]'
- Stored Communications Act (18 U.S.C. § 2701 et seq.)
limitations:
- Provider discretion for voluntary disclosures
- Content data typically excluded — requires warrant/MLAT/executive agreement
- Subject to provider's domestic law (blocking statutes, GDPR, etc.)
- No compelled production without legal process valid in provider's jurisdiction
- Variable provider response times (days to months)
mechanism_type: provider-disclosure
operations_using: []
participants:
  count: 0
  notable_members:
  - Meta (Facebook/Instagram/WhatsApp)
  - Google/Alphabet
  - Microsoft
  - X Corp (Twitter)
  - Apple
  - Amazon
  type: mixed
purpose: Law enforcement requests for user data sent directly to service providers
  without going through the traditional MLAT process — most commonly used to obtain
  subscriber information and non-content records.
related_mechanisms:
- '[[mlat-process]]'
- '[[24-7-network]]'
scope:
  arrest_coordination: false
  asset_tracing: false
  content_data: false
  evidence_preservation: true
  evidence_production: true
  intelligence_sharing: false
  real_time_data: false
  subscriber_info: true
  traffic_data: true
source_count: 6
sources: []
speed: days
title: Direct Provider Request
type: mechanism
updated: 2026-04-10
---

## Summary

The **Direct Provider Request** mechanism allows law enforcement to obtain user account information directly from online service providers — most commonly US-headquartered platforms such as Meta, Google, Microsoft, Apple, and X — **without routing the request through a formal MLAT**. It has become the single most-used pathway for cross-border digital evidence in cybercrime investigations, *almost certainly* exceeding MLAT volume by an order of magnitude for subscriber information queries.

The mechanism covers a spectrum from **purely voluntary disclosures** (informal requests, emergency disclosures) to **quasi-formal direct channels** created by the US [[cloud-act|CLOUD Act]] and the [[second-additional-protocol|Second Additional Protocol to the Budapest Convention (CETS 224)]].

## Legal Basis

### United States — the center of gravity

Because most of the major global platforms are US-headquartered, US law governs how they respond to foreign law enforcement requests:

- **Stored Communications Act (SCA), 18 U.S.C. § 2701 et seq.** — governs disclosure of stored communications; permits voluntary disclosure of **non-content** records to foreign law enforcement under § 2702(c)(6); prohibits voluntary disclosure of **content** except in specified emergencies.
- **[[cloud-act|Clarifying Lawful Overseas Use of Data Act (CLOUD Act), 2018]]** — (a) clarifies that US providers must produce data stored abroad in response to valid US legal process, and (b) authorizes the US to enter into **Executive Agreements** with qualifying foreign governments, allowing those governments to issue direct production orders (including for content) to US providers.
- **CLOUD Act Executive Agreements in force (as of 2026):** United Kingdom (entered into force October 2022), Australia (signed December 2021). Additional agreements under negotiation.

### Council of Europe — [[second-additional-protocol|Second Additional Protocol to the Budapest Convention]]

Adopted in 2022, CETS 224 creates two direct cooperation tools:
- **Article 7 — Direct cooperation for subscriber information:** A competent authority in one party may issue an order directly to a service provider in the territory of another party for subscriber information.
- **Article 8 — Giving effect to orders from another party:** A party may issue a production order that must be executed by the provider in another party's territory.

As of early 2026, CETS 224 has only 3 ratifications (Japan, Serbia, Hungary) and has not entered into force.

### EU / e-Evidence package

EU Regulation 2023/1543 on European Production and Preservation Orders for electronic evidence ("e-Evidence Regulation") provides a direct production order mechanism between EU member states and binds providers offering services in the EU. Application began 18 August 2026.

## How It Works

### Voluntary request workflow

```
Law enforcement officer          Service provider
                                 
1. Identifies target account    
   (username, email, etc.)       
                                 
2. Submits request via           
   provider's LE portal         
   (Meta LEP, Google LERS,      
    Microsoft LERT, etc.)       
                ──────────────►
                                 3. Reviews legal basis
                                    and jurisdiction
                                 
                                 4. Applies internal policy
                                    (type of data, requester,
                                     emergency status)
                                 
                                 5. Produces non-content
                                    records, or refuses
                ◄──────────────     content requests
6. Receives data                 
```

### Emergency disclosure

Under 18 U.S.C. § 2702(b)(8) / (c)(4), a US provider **may** voluntarily disclose content or non-content records — including to foreign law enforcement — if it has "a good faith belief that an emergency involving danger of death or serious physical injury to any person" requires disclosure. Used for imminent threats to life: kidnapping, self-harm, terror plots, active shooter scenarios.

### CLOUD Act executive agreement workflow

For qualifying foreign governments (currently UK, Australia), the process is a **compelled production order** rather than voluntary:

1. Qualifying authority issues a production order under its own law
2. Order is transmitted directly to the US-based provider
3. Provider must comply, subject to defined grounds for challenge (US persons, conflict with US law)
4. No routing through US DOJ/OIA required

## Scope and Capabilities

| Data Type | Voluntary (non-EA country) | CLOUD Act EA (UK/AU) | CETS 224 | MLAT |
|-----------|---------------------------|---------------------|----------|------|
| Basic subscriber info | Yes (most providers, with legal process) | Yes | Yes (Art. 7) | Yes |
| Traffic/transaction logs | Often yes (provider discretion) | Yes | Varies | Yes |
| Stored content | **No** (except § 2702 emergencies) | Yes | No (content excluded) | Yes |
| Real-time interception | No | Limited | No | Exceptional |
| Compelled production | No | Yes | Yes (Art. 8) | Yes |

## Practical Usage

Direct provider requests are *almost certainly* the most heavily used cross-border evidence pathway for cybercrime investigators globally. Typical use cases:

- **Voice phishing (보이스피싱) investigations:** Obtaining account holder information for messaging apps and social media
- **Ransomware investigations:** Subscriber info for Telegram/ICQ accounts used for negotiations
- **Child sexual abuse material (CSAM):** Emergency disclosures and NCMEC CyberTipline-derived requests
- **BEC fraud:** Gmail/Outlook account subscriber information and login IP addresses
- **Stalkerware / harassment cases:** Subscriber info for tip/trace investigations

Major US providers publish **Transparency Reports** showing request volumes by country — these reports *highly likely* underreport actual requests because they exclude certain legal process categories.

## Advantages

- **Speed:** Days rather than months (compared to MLAT)
- **Volume:** Providers can handle high request volumes through online portals
- **Simplicity:** No translation, central authority, or dual criminality hurdles for basic subscriber info
- **Emergency responsiveness:** Life-threatening situations can be addressed in hours
- **Cost:** No central authority fees or extensive drafting requirements

## Limitations

1. **Content data barrier:** Without a CLOUD Act Executive Agreement (or future CETS 224 implementation), foreign law enforcement **cannot compel** content production from US providers — they must still use MLAT.
2. **Provider discretion:** Voluntary cooperation is not guaranteed; providers assess requests against internal policies.
3. **Blocking statutes:** GDPR Art. 48 and similar laws can create legal exposure for providers that disclose data in response to third-country legal process without a proper instrument.
4. **Evidentiary admissibility:** Direct provider disclosures may face challenges in trial courts that expect formal MLA channels for foreign evidence.
5. **Transparency gaps:** Limited information about request outcomes, refusal reasons, and user notice policies.
6. **Asymmetry:** Non-US providers face different and often less developed frameworks for receiving foreign requests.

## Notable Uses

Direct provider cooperation — especially emergency disclosures and subscriber information requests — has *likely* been used in the majority of documented cybercrime operations involving social media or cloud-hosted infrastructure. Specific case citations are rarely published because providers and law enforcement treat the mechanism as operationally sensitive.

## Comparison with Alternatives

See the comparison table in [[mlat-process]] for a direct side-by-side view of MLAT, 24/7 Network, Direct Provider Request, and JIT mechanisms.

## Korean Usage (한국의 활용)

Korean investigators routinely make direct requests to US providers for voice phishing and CSAM cases, typically through the providers' law enforcement portals. The main pathway for obtaining **content data** on US platforms remains the [[mlat-process|Korea-US MLAT (2000)]] channel, as Korea does not currently have a CLOUD Act Executive Agreement with the United States. Korea's 2024 accession to the [[budapest-convention]] positions it to potentially sign and ratify the [[second-additional-protocol|Second Additional Protocol]] in the future, which would expand direct cooperation options.

> [!warning] Legal status check needed
> Verify whether Korea has signed the Second Additional Protocol (CETS 224) and its current position on CLOUD Act Executive Agreement negotiations with the US.

## Contradictions & Open Questions

- What percentage of Korean cross-border digital evidence requests go through direct provider channels vs. MLAT?
- Are CLOUD Act Executive Agreements scaling as anticipated, or has progress stalled?
- How will the EU e-Evidence Regulation interact with CETS 224 implementation inside the EU?
- What safeguards exist against abuse of the mechanism by authoritarian regimes?

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | CLOUD Act (H.R. 4943, 115th Congress) | US Congress | 2018 | [원본](https://www.congress.gov/bill/115th-congress/house-bill/4943) |
| [2] | CLOUD Act — Wikipedia | Wikipedia | n.d. | [원본](https://en.wikipedia.org/wiki/CLOUD_Act) |
| [3] | The CLOUD Act, Explained | Orrick | 2018-04 | [원본](https://www.orrick.com/en/Insights/2018/04/The-CLOUD-Act-Explained) |
| [4] | Second Additional Protocol to the Convention on Cybercrime (CETS No. 224) | Council of Europe | 2022-05-12 | [원본](https://www.coe.int/en/web/cybercrime/second-additional-protocol) |
| [5] | Frequently Asked Questions about the U.S. CLOUD Act | Cross-Border Data Forum | n.d. | [원본](https://www.crossborderdataforum.org/cloudactfaqs/) |
| [6] | Government Requests for Customer Data Report | Microsoft | continuous | [원본](https://www.microsoft.com/en-us/corporate-responsibility/reports/government-requests/customer-data) |
