---
type: operation
title: "Operation RapTor"
aliases:
  - RapTor
  - "JCODE Operation RapTor"
case_id: CYB-2025-017
period: 3
operation_role: umbrella
parent_operation: ""
operation_type: coordinated-arrests
status: completed
enforcement_type:
  - arrest
  - search
  - seizure
  - asset-seizure
outcome: success
timeframe:
  announced: 2025-05-22
  start: 2025-04-01
  end: 2025-05-22
  ongoing: false
crime_type: "[[dark-web-ic]]"
crime_types:
  - "[[dark-web-ic]]"
  - "[[drug-trafficking]]"
  - "[[money-laundering-ic]]"
target_entity: "Darknet vendors, buyers, administrators, and trafficking networks selling fentanyl, opioids, firearms, counterfeit goods, and other illicit services"
lead_agency: "[[us-doj]]"
coordinating_body: "[[us-doj]]"
participating_countries:
  - "[[austria]]"
  - "[[brazil]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[south-korea]]"
  - "[[spain]]"
  - "[[switzerland]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
jurisdictions:
  - "[[austria]]"
  - "[[brazil]]"
  - "[[france]]"
  - "[[germany]]"
  - "[[netherlands]]"
  - "[[south-korea]]"
  - "[[spain]]"
  - "[[switzerland]]"
  - "[[united-kingdom]]"
  - "[[united-states]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[dea]]"
  - "[[europol-ec3]]"
  - "[[uk-nca]]"
organizations:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[dea]]"
  - "[[europol-ec3]]"
  - "[[uk-nca]]"
mechanisms_used:
  - "[[electronic-evidence]]"
  - "[[cryptocurrency-seizure]]"
  - "[[search-seizure]]"
  - "[[informal-cooperation]]"
legal_basis:
  - "[[informal-cooperation]]"
results:
  arrests: 270
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "More than USD 200 million in currency and digital assets"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "More than two metric tons of drugs seized."
    - "144 kilograms of fentanyl or fentanyl-laced narcotics seized."
    - "More than 180 firearms seized."
    - "Arrests included the United States, Germany, the United Kingdom, France, South Korea, Austria, Brazil, the Netherlands, Spain, and Switzerland."
credibility_index: 4.4
source_tier: 1
missing_fields: ""
related_cases: ""
related_operations:
  - "[[operation-dark-huntor]]"
  - "[[nemesis-market-takedown]]"
  - "[[darkmarket-takedown]]"
  - "[[archetyp-market-takedown-operation-deep-sentinel-2025]]"
challenges_encountered:
  - "Public sources describe a coordinated operation based on separate national investigations, so later defendant-specific filings should not be counted as separate operation-level actions unless they identify a new multinational operation."
lessons_learned:
  - "Darknet marketplace seizures can generate cross-border evidence packages that support later coordinated arrests across multiple continents."
source_count: 5
sources:
  - "[[2025-05-22_justice-gov_law-enforcement-seize-record-amounts-of-illegal-drugs-firearms-and-drug-traffick]]"
  - "[[2025-05-22_fbi-gov_global-operation-targets-darknet-drug-trafficking]]"
  - "[[2025-05-22_ice-gov_ice-europol-law-enforcement-partners-dismantle-major-illicit-drug-networks-global-darknet-crackdown]]"
  - "[[2025-05-22_hackread_com_operation-raptor-270-arrested-global-crackdown-on-dark-web-vendors]]"
  - "[[2025-05-22_occrp_org_massive-dark-web-sweep-leads-to-270-arrests-worldwide]]"
summary: "Operation RapTor was a 2025 global darknet-trafficking operation announced by DOJ JCODE and international partners. Authorities arrested 270 dark web vendors, buyers, and administrators across four continents and ten named countries, while seizing more than USD 200 million in currency and digital assets, over two metric tons of drugs, 144 kilograms of fentanyl or fentanyl-laced narcotics, and more than 180 firearms."
created: 2026-05-07
updated: 2026-05-17
---
# Operation RapTor

## Summary

Operation RapTor was a global coordinated operation against darknet trafficking of fentanyl, opioids, firearms, counterfeit goods, and related illicit services. DOJ announced the results on 22 May 2025 with JCODE and international law-enforcement partners.

The operation produced 270 arrests across four continents and ten named countries: Austria, Brazil, France, Germany, the Netherlands, South Korea, Spain, Switzerland, the United Kingdom, and the United States.

## Background

### Modus operandi

Per DOJ and FBI releases, the targets of Operation RapTor were vendors, buyers, and administrators operating on Tor-hidden-service darknet marketplaces — principally Nemesis, Tor2Door, Bohemia, and Kingdom Markets, the four markets DOJ named as evidence-source feeders for the coordinated arrest wave. Vendors used these markets to sell fentanyl, fentanyl-laced counterfeit pills (pressed to imitate oxycodone, Xanax, and Adderall), heroin, methamphetamine, cocaine, firearms, counterfeit currency, fraudulent identity documents, and stolen account data. Orders were placed through marketplace escrow, shipped via national postal services and private couriers (often disguised as innocuous packages with falsified return addresses), and paid in Bitcoin or Monero through marketplace-hosted wallets. After prior takedowns of Hydra (2022), Nemesis (March 2024), and other markets, RapTor exploited the resulting evidence packages — vendor PGP keys, shipping addresses, customer lists, and on-chain transaction histories — to identify individual vendors and high-volume buyers across jurisdictions.

**Victim profile + impact.** The defining victim class is users of opioids and counterfeit pharmaceuticals, particularly U.S. consumers exposed to fentanyl-laced counterfeit prescription tablets. DOJ framed RapTor as a fentanyl-poisoning response: 144 kilograms of fentanyl or fentanyl-laced narcotics seized in the operation represents lethal doses sufficient to kill millions, given the ~2 mg lethal-dose threshold widely cited by DEA. U.S. overdose-death statistics that motivated the JCODE initiative — over 100,000 annual U.S. overdose deaths in the years preceding 2025, with synthetic opioids accounting for the majority — provide the impact backdrop. Secondary victim categories include firearms-trafficking victims (recipients of weapons sold through darknet listings, often diverted into U.S. street markets) and counterfeit-document fraud victims.

### Financial flow

Darknet-market commerce on the targeted platforms ran on Bitcoin and Monero, with Monero adoption increasing as on-chain analytics matured. Marketplaces operated escrow wallets that held buyer funds until delivery confirmation, then released funds to vendor wallets (less a market commission of typically 2-5%). Vendor cash-out paths included no-KYC and weak-KYC cryptocurrency exchanges, peer-to-peer trades, prepaid debit cards, and conversion through privacy-coin swap services. The USD 200 million+ in currency and digital assets seized in Operation RapTor reflects on-chain vendor and administrator wallets traced through the prior marketplace seizures, plus cash and bank funds recovered during national search warrants.

### Criminal organization structure

Targets clustered in three roles: (1) **vendors** — typically small operations of 1-5 individuals running storefronts, often specialising in one product class (fentanyl analogues, firearms, counterfeit currency), with the most prolific vendors on Nemesis and Tor2Door identified by DOJ as having processed thousands of orders before takedown; (2) **administrators** — small teams (often 2-4 named individuals per market) operating the marketplace infrastructure, escrow wallets, and forum moderation; (3) **buyers** — individual consumers and resellers, with high-volume buyers (those purchasing in kilogram quantities for street-level redistribution) prioritised for arrest. Public DOJ releases do not describe targets as members of pre-existing hierarchical OCGs (cartels, mafias); rather, RapTor targeted the post-Hydra darknet vendor ecosystem of independent operators connected only through shared markets and forum identities.

## Cooperation Model

- **JCODE coordination:** DOJ framed RapTor as part of the Joint Criminal Opioid and Darknet Enforcement initiative.
- **Europol and national partners:** Public releases identify Europol EC3 and the U.K. National Crime Agency as key international partners, alongside national law-enforcement actions in Europe, South America, Asia, and the United States.
- **Evidence pipeline:** DOJ said prior darknet-market takedowns, including Nemesis, Tor2Door, Bohemia, and Kingdom Markets, generated leads and evidence that supported the coordinated arrests.
- **Asset and evidence actions:** Sources document searches, arrests, digital-asset seizures, drug seizures, and firearm seizures.

## Results and Impact

| Metric | Value |
|---|---:|
| Arrests | 270 |
| Countries with arrests named in official releases | 10 |
| Currency and digital assets seized | USD 200 million+ |
| Drugs seized | 2 metric tons+ |
| Fentanyl or fentanyl-laced narcotics | 144 kg |
| Firearms seized | 180+ |

The U.S. accounted for 130 arrests, while FBI and independent reporting identify Germany, the United Kingdom, France, and South Korea as other major arrest locations.

## Boundary and Non-Duplication Notes

This page is the operation-level aggregation point for Operation RapTor. The existing long-title enforcement wrapper is retained only for source-trace continuity and should not be counted as a separate international-cooperation operation. Later indictments, pleas, sentencings, or forfeiture cases should be attached as related case or absorbed follow-on records unless a source explicitly presents them as a new multinational operation.

## Evidence Notes

DOJ is the anchor source for the operation name, arrest total, participating-country list, and seizure totals. FBI and ICE provide parallel U.S. government confirmation. Hackread and OCCRP add external media confirmation of the operation name, ten-country scope, prior-marketplace evidence pipeline, and headline enforcement metrics.

## Contradictions & Open Questions

- Per-vendor revenue breakdowns and overall on-chain transaction volume on the feeder marketplaces (Nemesis, Tor2Door, Bohemia, Kingdom) are not disclosed in DOJ's public RapTor announcement; only the aggregate USD 200 million+ asset-seizure figure is reported.
- Defendant-level financial flows (laundering routes, exchange identities, cash-out infrastructure) are not enumerated in public sources for the 270 arrested individuals.
- Aggregate victim count and total user-poisoning impact from products sold through the targeted vendors are not quantified in tier-1 sources; only the 144 kg fentanyl seizure metric is provided.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Law Enforcement Seize Record Amounts of Illegal Drugs, Firearms, and Drug Trafficking Proceeds in International Operation Against Darknet Trafficking of Fentanyl and Opioids; 270 Arrested Across Four Continents | US DOJ | 2025-05-22 | https://www.justice.gov/opa/pr/law-enforcement-seize-record-amounts-illegal-drugs-firearms-and-drug-trafficking-proceeds |
| [2] | Global Operation Targets Darknet Drug Trafficking | FBI | 2025-05-22 | https://www.fbi.gov/news/stories/global-operation-targets-darknet-drug-trafficking |
| [3] | ICE, Europol, law enforcement partners, dismantle major illicit drug networks in global Darknet crackdown | ICE | 2025-05-22 | https://www.ice.gov/news/releases/ice-europol-law-enforcement-partners-dismantle-major-illicit-drug-networks-global |
| [4] | Operation RapTor: 270 Arrested in Global Crackdown on Dark Web Vendors | Hackread | 2025-05-22 | https://hackread.com/operation-raptor-police-arrests-270-dark-web-vendors/ |
| [5] | Massive Dark Web Sweep Leads to 270 Arrests Worldwide | OCCRP | 2025-05-22 | https://www.occrp.org/en/news/massive-dark-web-sweep-leads-to-270-arrests-worldwide |
