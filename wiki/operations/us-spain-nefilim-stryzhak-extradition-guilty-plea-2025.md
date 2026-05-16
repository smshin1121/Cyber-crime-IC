---
type: operation
title: "US-Spain Nefilim Ransomware Affiliate Extradition + EDNY Guilty Plea — Artem Stryzhak (2024-2025)"
title_ko: "US-스페인 Nefilim 랜섬웨어 affiliate 송환 + EDNY 유죄 인정 — Artem Stryzhak (2024-2025)"
aliases:
  - "US v. Stryzhak (Nefilim) — Spain extradition"
  - "Stryzhak Nefilim affiliate plea"
  - "USAO-EDNY Stryzhak guilty plea"
case_id: CYB-2025-219
period: 3
operation_type: arrest-sweep
status: completed
enforcement_type:
  - arrest
  - extradition
  - indictment
outcome: success
timeframe:
  announced: 2025-12-19
  start: 2024-06
  end: 2025-12-19
  ongoing: false
crime_type: "[[ransomware-ic]]"
crime_types:
  - "[[ransomware-ic]]"
  - "[[extortion-ic]]"
  - "[[hacking-ic]]"
target_entity: "Artem Aleksandrovych Stryzhak, 35, Ukrainian citizen resident in Barcelona, Spain; Nefilim ransomware affiliate operating June 2021 onward, receiving Nefilim code via the Nefilim administrator-operated affiliate panel in exchange for a 20% revenue share of paid ransoms, targeting US/Canada/Australia-based companies with annual revenues exceeding USD 100 million (later USD 200 million); leak-site brand 'Corporate Leaks'"
lead_agency: "[[us-doj]]"
coordinating_body: "[[office-of-international-affairs]]"
participating_countries:
  - "[[united-states]]"
  - "[[spain]]"
participating_agencies:
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[office-of-international-affairs]]"
  - "[[spain-national-police]]"
legal_basis:
  - "[[extradition]]"
  - "[[budapest-convention]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[mlat-process]]"
  - "[[european-arrest-warrant]]"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Stryzhak arrested in Spain June 2024 on US provisional arrest request"
    - "Extradited US 2025-04-30"
    - "Guilty plea entered 2025-12-19 (EDNY federal court, Brooklyn) to conspiracy to commit fraud and related extortion-in-connection-with-computers; max 10 years"
    - "Sentencing scheduled 2026-05-06"
    - "Co-defendant Volodymyr Tymoshchuk (Nefilim administrator) at-large; State Department Rewards For Justice TOC bounty up to USD 11 million"
edges:
  - source_actor: "[[fbi]]"
    target_actor: "[[spain-national-police]]"
    cooperation_type: extradition
    legal_basis: bilateral_MOU
    direction: directed
  - source_actor: "[[us-doj]]"
    target_actor: "[[spain-national-police]]"
    cooperation_type: extradition
    legal_basis: MLAT
    direction: directed
  - source_actor: "[[office-of-international-affairs]]"
    target_actor: "[[spain-national-police]]"
    cooperation_type: evidence_transfer
    legal_basis: MLAT
    direction: directed
credibility_index: 4.0
source_tier: 1
missing_fields:
  - "Spanish prosecuting/extraditing tribunal (Audiencia Nacional vs. lower-court extradition chamber) is not named in the EDNY release"
  - "Specific victim companies count and aggregate ransom dollar figure for Stryzhak-attributed attacks not disclosed"
related_cases:
  - "[[us-v-stryzhak-nefilim]]"
  - "[[us-v-tymoshchuk-nefilim-megacortex-lockergoga]]"
related_operations:
  - "[[us-v-volkov-yanluowang-sentencing]]"
  - "[[operation-us-v-deniss-zolotarjovs]]"
challenges_encountered: []
lessons_learned:
  - "EU-resident ransomware affiliates (Stryzhak in Spain, Volkov in Italy, Zolotarjovs originally arrested in Georgia) are reachable through US-led extradition requests channeled via DOJ Office of International Affairs to the EU/EU-adjacent host state's central authority — a 2024-2025 IC pattern that has now delivered three Russian/Ukrainian ransomware affiliate or initial-access-broker defendants to EDNY/SDIN/SDOH federal-court guilty pleas"
  - "EDNY-led ransomware prosecutions appear to consistently leverage FBI Springfield Illinois Field Office as the field-office investigator-of-record, even when the defendant is arrested overseas — suggesting a victim-jurisdiction-based field assignment model rather than the foreign-arrest jurisdiction's local FBI Legat office leading"
source_count: 1
sources:
  - "[[2025-12-19_justice-gov-usao-edny_ukrainian-national-pleads-guilty-conspiracy-nefilim-ransomware]]"
created: 2026-05-16
updated: 2026-05-16
---

## Summary

The US-Spain bilateral cooperation that brought Nefilim ransomware affiliate Artem Aleksandrovych Stryzhak — a 35-year-old Ukrainian national resident in Barcelona, Spain — from his Spanish residence to a Brooklyn federal-court guilty plea is the third in a 2024-2025 series of European-arrest US-extradition pathways closing out Nefilim-, Yanluowang-, and Conti/Karakurt-affiliated ransomware-affiliate-tier defendants. Stryzhak was arrested in Spain in June 2024 on a US provisional arrest request, extradited to the United States on 2025-04-30, and pleaded guilty on 2025-12-19 in the U.S. District Court for the Eastern District of New York (Brooklyn) to a single count of conspiracy to commit fraud and related activity, including extortion, in connection with computers, with a maximum statutory penalty of 10 years and sentencing scheduled for 2026-05-06.

The case is delivered jointly by U.S. Attorney for the Eastern District of New York Joseph Nocella, Jr., Acting Assistant Attorney General Matthew R. Galeotti of the DOJ Criminal Division, and FBI Special Agent in Charge Christopher J.S. Johnson of the FBI Springfield Illinois Field Office. The EDNY USAO press release explicitly thanks the Justice Department's Office of International Affairs and Computer Crime and Intellectual Property Section, as well as Spanish law enforcement authorities, for their assistance in the capture of Stryzhak, providing the L24-required verbatim acknowledgement of the foreign cooperating-LE jurisdiction.

## Background

Nefilim ransomware emerged as a successor lineage descended from the Nemty/Nefilim/Karma malware family with continuity-of-administrators traceable to the at-large co-defendant Volodymyr Tymoshchuk, who is named in the EDNY release as a Nefilim administrator and the subject of a State Department Rewards For Justice TOC bounty of up to USD 11 million for arrest or conviction information. Tymoshchuk was previously indicted in September 2025 in a separate USAO-EDNY indictment naming him as an administrator of Lockergoga, MegaCortex, and Nefilim — see [[us-v-tymoshchuk-nefilim-megacortex-lockergoga]] and the parallel September 2025 source pages.

The Nefilim affiliate-tier compensation structure documented in the EDNY release works as follows: in June 2021, Nefilim administrators (Tymoshchuk-tier) gave Stryzhak access to the Nefilim ransomware code via an online affiliate panel in exchange for 20% of his ransom proceeds. Affiliates operate the ransomware through individual accounts on the operator-panel platform; the Nefilim administrators customize the ransomware executable file for each victim, creating a unique decryption key and customized ransom note. Affiliate-tier targeting per the EDNY release was specifically configured for US/Canada/Australia-based companies with annual revenues exceeding USD 100 million (with a later EDNY-recorded raise to USD 200 million). Victim research used commercial online net-worth and contact databases. Post-encryption double-extortion leak threats published stolen data on Nefilim-administrator-controlled "Corporate Leaks" websites.

## Participating Parties

Cooperating jurisdictions per the EDNY release:
- **[[united-states]]**: USAO-EDNY (prosecutor of record, lead), DOJ Criminal Division Computer Crime and Intellectual Property Section (CCIPS) (co-prosecutor — Trial Attorney Brian Mund), DOJ [[office-of-international-affairs]] (OIA — extradition channel), [[fbi]] Springfield Illinois Field Office (investigating field office), FBI New York Field Office ("significant contributions to the investigation"), U.S. Department of State (Rewards For Justice TOC bounty operator for Tymoshchuk)
- **[[spain]]**: [[spain-national-police|"Spanish law enforcement authorities"]] — explicitly thanked in the EDNY USAO release for assistance in the capture of Stryzhak; the EDNY release does not name a specific Spanish agency or extraditing tribunal, leaving the Spanish counterpart agency as a missing-field item for cross-verification

Defendant nationality: [[ukraine]] (Stryzhak is a Ukrainian citizen, residence in Barcelona, Spain). Ukraine is the defendant's nationality jurisdiction, not a cooperating-LE jurisdiction per the L24 strict interpretation; Spain is the cooperating-LE jurisdiction because Spanish LE arrested Stryzhak on the US provisional arrest request and Spanish judicial authorities executed the 2025-04-30 extradition.

## Legal Framework

The US-Spain extradition pathway employed for Stryzhak combines (a) bilateral extradition under the long-standing US-Spain extradition treaty and bilateral instruments, (b) Spain's domestic implementation of the [[budapest-convention]] (Convention on Cybercrime ETS 185, of which Spain is a party), supplying substantive-law dual-criminality coverage for ransomware/extortion-in-connection-with-computers offenses, and (c) the DOJ Office of International Affairs as the US central-authority channel transmitting the provisional arrest request and the formal extradition request to the Spanish Ministry of Justice. The EDNY release does not invoke the EU European Arrest Warrant explicitly because the EAW is an intra-EU instrument and the requesting state is the US; the EAW is included in `mechanisms_used` only as a related Spanish-domestic procedural reference and may be removed at next-pass enrichment if it is determined not to have been the operative legal instrument.

## Operational Timeline

- **June 2021**: Stryzhak gains access to the Nefilim affiliate panel for a 20% revenue share
- **late 2018 – late 2021 (Nefilim global activity window)**: ransomware attacks on US/Canada/Australia-based companies with annual revenues exceeding USD 100-200 million; leak-site brand "Corporate Leaks"
- **June 2024**: Spanish LE arrest Stryzhak in Spain on a US provisional arrest request
- **2025-04-30**: Spain executes formal extradition; Stryzhak is transferred to US custody
- **2025-09-09**: Co-defendant Tymoshchuk separately charged in EDNY indictment as Nefilim/MegaCortex/Lockergoga administrator (see related case)
- **2025-12-18**: DOJ Office of Public Affairs (OPA) issues national parallel announcement of Stryzhak's plea
- **2025-12-19**: USAO-EDNY issues regional press release; Stryzhak pleads guilty in Brooklyn federal court to conspiracy to commit fraud and related computer activity including extortion; max 10 years
- **2026-05-06**: Sentencing scheduled (EDNY Docket 23-CR-324 (PKC))
- **Tymoshchuk at-large**: Rewards For Justice TOC bounty up to USD 11 million via FBI tip line +1-917-242-1407, email TymoTips@fbi.gov

## Results and Impact

- 1 arrest (Spain, June 2024)
- 1 extradition (Spain → US, 2025-04-30)
- 1 guilty plea (EDNY, 2025-12-19)
- Co-defendant administrator (Tymoshchuk) named publicly with $11 million Rewards For Justice TOC bounty offer
- EDNY victim-impact and aggregate dollar figures not disclosed in the regional release

## Cooperation Mechanisms Used

- **[[extradition]]** — US-Spain bilateral extradition treaty pathway
- **[[mlat-process]]** — DOJ OIA channel for the provisional arrest request and the formal extradition documentation transmission to the Spanish central authority
- **[[european-arrest-warrant]]** — see note under Legal Framework; included as a related Spanish-domestic procedural reference, may be reclassified at enrichment

## Challenges and Friction Points

The EDNY release does not name a specific Spanish agency (Policía Nacional, Guardia Civil, Audiencia Nacional vs. lower extradition chamber), only "Spanish law enforcement authorities" generically. This is a minor opacity in cooperation attribution but not a defect of the L24 ≥2-country requirement — Spain is unambiguously named as a cooperating LE jurisdiction.

## Lessons Learned

Recorded under `lessons_learned` in the frontmatter:
1. EU-resident ransomware affiliates are reachable through US-led extradition requests via DOJ OIA — the 2024-2025 Stryzhak (Spain) / Volkov (Italy) / Zolotarjovs (Georgia) triad demonstrates a consistent pattern.
2. EDNY-led ransomware prosecutions appear to use FBI Springfield Illinois Field Office as the field-office investigator-of-record across geographically dispersed defendant cases, suggesting a victim-jurisdiction-based field-assignment model.

## Follow-Up Actions

- Sentencing 2026-05-06 will close the Stryzhak prosecution leg of this US-Spain pathway
- Tymoshchuk (administrator-tier) remains at-large; the US$11M Rewards For Justice TOC bounty remains the primary US instrument for follow-up

## Korean Involvement (한국의 참여)

No Korean LE or prosecutorial involvement is named in the EDNY release. Nefilim's documented target profile per the release is US/Canada/Australia, with no Korean-victim attribution.

## Contradictions & Open Questions

> [!note] Source-attribution ambiguity
> The EDNY release names "Spanish law enforcement authorities" generically without specifying the Policía Nacional vs. Guardia Civil vs. Audiencia Nacional chain. This is recorded in `missing_fields` for next-pass enrichment.

> [!note] Parallel OPA vs. regional EDNY release
> A parallel DOJ OPA national release dated 2025-12-18 covers the same Stryzhak plea ([[2025-12-18_justice-gov_ukrainian-national-pleads-guilty-conspiracy-nefilim-ransomware]]); the EDNY regional release dated 2025-12-19 used here is the prosecutor-of-record's own-domain version. Both are tier-1 own-domain US federal-government releases; the EDNY version is preferred for the L24 verbatim quote on Spanish-LE cooperation because the EDNY USAO is the actual prosecuting office.
