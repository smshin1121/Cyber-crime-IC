---
type: operation
title: "OAG/fedpol Real-Time Phishing Joint Investigation - UK Conviction (2025)"
aliases:
  - "OAG fedpol UK phishing kit conviction"
  - "Swiss-UK real-time phishing case"
  - "English student Swiss phishing kit case"
case_id: CYB-2025-097
period: 3
operation_role: standalone
parent_operation: ""
operation_type: joint-investigation
status: completed
enforcement_type:
  - arrest
  - indictment
  - extradition
outcome: success
timeframe:
  announced: 2025-07-29
  start: 2022-07
  end: 2025-07-23
  ongoing: false
crime_type: "[[bank-fraud-ic]]"
crime_types:
  - "[[bank-fraud-ic]]"
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
target_entity: "British national who developed and distributed a real-time-phishing kit used against Swiss bank customers"
lead_agency: "[[switzerland-fedpol]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[switzerland]]"
  - "[[united-kingdom]]"
jurisdictions:
  - "[[switzerland]]"
  - "[[united-kingdom]]"
participating_agencies:
  - "[[switzerland-fedpol]]"
  - "Office of the Attorney General of Switzerland (OAG / Bundesanwaltschaft)"
  - "[[uk-nca]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
organizations:
  - "[[switzerland-fedpol]]"
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[uk-nca]]"
mechanisms_used:
  - "[[joint-investigation-team]]"
  - "[[eurojust-coordination-meeting]]"
  - "[[mutual-legal-assistance]]"
  - "[[electronic-evidence]]"
legal_basis:
  - "Article 147 Swiss Criminal Code (computer fraud)"
  - "Bilateral Switzerland-UK criminal-justice cooperation; transfer of proceedings to UK"
  - "Europol/Eurojust operational and judicial coordination support"
results:
  arrests: 1
  indictments: 1
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "British national arrested in England on 2023-10-26 (per fedpol Report 2024)."
    - "OAG consolidated approximately 30 cantonal Swiss fraud cases into a single proceeding opened in July 2022."
    - "Total losses to Swiss bank customers approximately CHF 2.4 million."
    - "On 2025-07-23 a UK court sentenced the perpetrator to seven years' imprisonment."
    - "OAG transferred / discontinued Swiss proceedings in favour of UK prosecution."
credibility_index: 4.2
source_tier: 1
missing_fields:
  - "defendant_name (not released by OAG)"
  - "specific UK court and case number"
related_cases:
  []
related_operations:
  []
challenges_encountered:
  - "Bypass of bank two-factor authentication via real-time SMS interception."
  - "Attribution of the phishing-kit developer required cross-border identification before arrest could be coordinated."
lessons_learned:
  - "Where the suspect, the harm, and the prosecuting authority sit in different countries, transfer of proceedings to the suspect's country can be an efficient cooperation outcome when bilateral coordination is sound."
  - "Real-time-phishing cases attacking cantonal-bank e-banking can require consolidation of many small cantonal proceedings into a federal file before international cooperation becomes effective."
source_count: 3
sources:
  - "[[2025-07-29_oag-fedpol_real-time-phishing-uk-conviction]]"
summary: "A joint Swiss federal investigation by the Office of the Attorney General of Switzerland (OAG) and the Federal Office of Police (fedpol) identified a British national as the developer and distributor of a real-time-phishing kit used against Swiss bank customers, consolidating approximately 30 cantonal cases representing about CHF 2.4 million in losses. The suspect was arrested in England in October 2023; after coordination with UK authorities, prosecution was transferred to the United Kingdom, where on 23 July 2025 a UK court sentenced the perpetrator to seven years' imprisonment. OAG announced the conviction on 29 July 2025."
created: 2026-05-09
updated: 2026-05-09
---

# OAG/fedpol Real-Time Phishing Joint Investigation - UK Conviction (2025)

> [!info] Provisional record
> This page rests on a single Swiss federal-government press release plus mirrored confirmations (Keystone-SDA / fedpol Report 2024). It is below the preferred 5-source threshold and is filed as a provisional case-cooperation record. It will be promoted when UK court documents or NCA/CPS releases identifying the defendant become available.

## Summary

A joint criminal investigation by the **Office of the Attorney General of Switzerland (OAG / Bundesanwaltschaft)** and the **Federal Office of Police ([[switzerland-fedpol|fedpol]])** identified a British national as the developer and distributor of a phishing kit used in a "real-time phishing" scheme that defrauded customers of Swiss banks. The OAG had opened criminal proceedings in **July 2022** and consolidated approximately **30 cantonal fraud cases** into a single federal file; total losses were approximately **CHF 2.4 million**. The developer/distributor was identified through joint OAG/fedpol investigation in **August 2023** and arrested in England on **26 October 2023**. After bilateral coordination with United Kingdom authorities, prosecution was transferred to the UK. On **23 July 2025**, a UK court sentenced the perpetrator to **seven years' imprisonment**. The OAG announced the conviction on **29 July 2025**.

This record qualifies for the IC corpus because the case was conducted as a Switzerland-UK cross-border cybercrime cooperation, with supporting roles for [[europol-ec3|Europol]] and [[eurojust|Eurojust]] (per the fedpol annual-report account), and resulted in transfer of proceedings to the country of the suspect.

## Background

Between approximately **May and October 2022**, a criminal network targeted customers of Swiss banks - in particular cantonal-bank e-banking customers - with a "real-time phishing" attack:

1. The attackers registered domain names that closely imitated the genuine domains of Swiss banks.
2. They placed paid Google Search advertisements so the fake e-banking login pages appeared at the top of search results when victims searched for their bank.
3. When victims attempted to log in, the page captured their credentials in real time.
4. Two-factor authentication was bypassed by inducing victims to enter their SMS one-time code on the phishing page; the code was forwarded to the fraudsters in real time and used to authenticate sessions and register the attackers' devices to the victim's account.
5. Funds were moved out through money mules and cryptocurrency exchanges.

The OAG opened criminal proceedings in **July 2022**. Approximately 30 fraud cases originally handled by Swiss cantons were transferred to the OAG and consolidated, given the cross-cantonal and cross-border dimension of the scheme.

## Participating Parties

| Role | Party |
|---|---|
| Swiss prosecuting authority | Office of the Attorney General of Switzerland (OAG / Bundesanwaltschaft) |
| Swiss investigating police authority | [[switzerland-fedpol\|fedpol]] |
| UK prosecuting / convicting authority | United Kingdom courts and prosecution service |
| EU operational support | [[europol-ec3\|Europol]] (per fedpol Report 2024 account) |
| EU judicial coordination support | [[eurojust\|Eurojust]] (per fedpol Report 2024 account) |
| Source-backed participating countries | [[switzerland\|Switzerland]], [[united-kingdom\|United Kingdom]] |

## Legal Framework

- Swiss proceedings were opened on the basis of **Article 147 of the Swiss Criminal Code** (computer fraud / *betrügerischer Missbrauch einer Datenverarbeitungsanlage* / *abus de la dispositif d'identification informatique*).
- After the suspect was identified, located, and arrested in England, and after coordination with UK authorities, the OAG **transferred / discontinued** its proceedings in favour of UK prosecution, on the basis that parallel UK proceedings were already underway against the same individual.
- Operational and judicial cooperation was supported through Europol and Eurojust channels (per the fedpol annual-report account).

## Operational Timeline

- **May–October 2022:** Phishing campaign targeting Swiss bank customers.
- **July 2022:** OAG opens criminal proceedings; consolidates approximately 30 cantonal Swiss fraud cases.
- **August 2023:** Joint OAG/fedpol investigation identifies the developer and distributor of the phishing kit; defendant added to the proceedings.
- **26 October 2023:** Defendant arrested in England (per fedpol Report 2024).
- **23 July 2025:** UK court sentences the defendant to seven years' imprisonment.
- **29 July 2025:** OAG issues press release announcing the UK conviction.

## Results and Impact

- One identified suspect arrested, prosecuted, and sentenced to **seven years' imprisonment** in the UK.
- Approximately **CHF 2.4 million** in documented losses to Swiss bank customers (based on consolidated OAG file).
- Approximately **30 cantonal fraud cases** consolidated and resolved through a single federal proceeding plus UK prosecution.
- Establishment of a documented Swiss-UK cooperation precedent for transfer of cybercrime prosecution where the suspect is located and prosecuted in his country of nationality.

## Cooperation Mechanisms Used

- **Bilateral coordination Switzerland-United Kingdom**, including transfer of proceedings from OAG to UK prosecution.
- **fedpol** as Swiss police investigative authority feeding identification and location intelligence.
- **Europol** support (per fedpol Report 2024 account of the case as an "international network").
- **Eurojust** judicial coordination support (per fedpol Report 2024 account).

## Challenges and Friction Points

- **Two-factor-authentication bypass.** SMS-based 2FA was defeated in real time, demonstrating that 2FA alone is insufficient against real-time-phishing kits.
- **Cantonal-to-federal consolidation.** Approximately 30 individually-cantonal complaints had to be consolidated into a single OAG proceeding before meaningful international cooperation became feasible.
- **Cross-border attribution before arrest.** Identifying the kit's developer in England required joint OAG/fedpol investigative work over a period of more than a year before a UK arrest could occur.

## Lessons Learned

- Where the suspect, the harm, and the prosecuting authority sit in different countries, **transfer of proceedings to the suspect's country** can be an efficient cooperation outcome when bilateral coordination is sound.
- Cantonal-level cybercrime complaints can require **federal consolidation** before they can be carried into international cooperation channels at scale.
- Real-time-phishing kits represent a **commodity-level criminal product**: prosecuting the developer/distributor (rather than only the operators) materially disrupts the underlying capability.

## Follow-Up Actions

- Public Swiss communications (NCSC and fedpol) continue to warn about real-time phishing of Swiss cantonal-bank customers, including a 2025 NCSC focus article specifically on the same fraud pattern.

## Korean Involvement (한국의 참여)

No Korean involvement is reported in this case. The matter is filed in the wiki as a Swiss-UK bilateral precedent of interest for comparative analysis with Korean cantonal/federal-equivalent fraud-consolidation issues and with Korea-UK / Korea-EU cybercrime cooperation discussions.

## Contradictions & Open Questions

- The defendant's name has not been released by the OAG; UK court documents would be the source for that detail.
- The OAG release does not name the specific UK court or UK case number; this should be filled in when an NCA / CPS / UK court source becomes available.
- The fedpol Report 2024 account references Europol and Eurojust support; the OAG press release itself does not enumerate those channels in detail. The Europol/Eurojust attribution is therefore retained in this record but flagged as drawn from the fedpol annual-report account rather than from a formal Europol/Eurojust press release on this specific case.

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Cybercrime: International investigations by the OAG and fedpol result in conviction for real-time phishing in the UK | Office of the Attorney General of Switzerland (OAG) / fedpol | 2025-07-29 | https://www.bag.admin.ch/en/newnsb/b4yhFXHLpERSkhgNMVb89 |
| [2] | English student sentenced for defrauding Swiss bank customers | Keystone-SDA / SWI swissinfo.ch | 2025-07-29 | https://www.swissinfo.ch/eng/various/fedpol-investigation-into-phishing-leads-to-conviction-in-england/89752247 |
| [3] | Phishing scam by an international network uncovered | fedpol Report 2024 | 2024 | https://fedpol.report/en/report-2024-en/serious-crime/phishing-scam-by-an-international-network-uncovered/ |
