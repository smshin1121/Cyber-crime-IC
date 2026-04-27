---
type: operation
title: "Cryptex and PM2BTC Coordinated Sanctions and Seizure Action"
title_ko: "Cryptex 및 PM2BTC 제재·압수 공조 조치"
aliases:
  - "Cryptex sanctions"
  - "PM2BTC sanctions"
  - "Cryptex PM2BTC action"
case_id: CYB-2024-052
period: 3
operation_type: infrastructure-seizure
status: completed
enforcement_type:
  - sanction
  - seizure
  - indictment
outcome: success
timeframe:
  announced: 2024-09-26
  start: 2024-09-26
  end: 2024-09-26
  ongoing: false
crime_type: "[[money-laundering-ic]]"
target_entity: "Cryptex exchange, PM2BTC, and the operators behind a cybercrime-linked virtual-currency laundering network"
lead_agency: "[[us-treasury]]"
coordinating_body: ""
participating_countries:
  - "[[united-states]]"
  - "[[netherlands]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[us-doj]]"
  - "[[netherlands-politie]]"
legal_basis: []
mechanisms_used: []
results:
  arrests: 0
  indictments: 2
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: "More than USD 7 million"
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "FinCEN designated PM2BTC as a primary money laundering concern."
    - "OFAC sanctioned Cryptex and related infrastructure."
    - "Dutch authorities seized servers associated with Cryptex and PM2BTC."
edges:
  - source_actor: "U.S. Treasury"
    target_actor: "Dutch authorities"
    cooperation_type: parallel_enforcement
    legal_basis: unknown
    direction: undirected
  - source_actor: "U.S. Department of Justice"
    target_actor: "Dutch authorities"
    cooperation_type: joint_investigation
    legal_basis: unknown
    direction: undirected
credibility_index: 4.33
source_tier: 1
missing_fields:
  - legal_basis
  - mechanisms_used
related_cases: []
related_operations: []
challenges_encountered: []
lessons_learned:
  - "Financial sanctions are more disruptive when synchronized with criminal charging and infrastructure seizure."
  - "Crypto-laundering services often require both regulatory and law-enforcement tools to create durable impact."
source_count: 6
sources:
  - "[[2024-09-26_treasury_cryptex-pm2btc-coordinated-actions]]"
  - "[[2024-09-26_justice-gov_two-russian-nationals-charged-money-laundering-services]]"
  - "[[2024-09-26_fincen_treasury-takes-coordinated-actions-against-illicit-russian-virtual-currency]]"
  - "[[2024-09-26_fincen_imposition-special-measure-prohibiting-the-transmittal-of-funds-involving-pm2btc]]"
  - "[[2024-09-26_usao-edva_two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering]]"
  - "[[2024-09-26_chainalysis_ofac-designates-russian-exchange-cryptex-fincen-names-pm2btc]]"
created: 2026-04-08
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "The September 2024 Cryptex and PM2BTC action combined U.S. sanctions, FinCEN special measures, criminal charging, and Dutch server seizures against a cybercrime-linked Russian virtual-currency laundering ecosystem."
organizations:
  - "[[us-treasury]]"
  - "[[us-doj]]"
  - "[[netherlands-politie]]"
crime_types:
  - "[[money-laundering-ic]]"
  - "[[ransomware-ic]]"
  - "[[dark-web-ic]]"
---
> [!note] Source basis
> This page now separates the Treasury press release, the FinCEN anti-money-laundering action, the DOJ criminal announcement, the EDVA case announcement, and independent technical analysis instead of collapsing them into one generic "sanctions" entry.

## Summary

The September 2024 Cryptex and PM2BTC action combined U.S. sanctions, anti-money-laundering regulation, criminal charging, and Dutch infrastructure seizure. Together, the measures targeted a Russian virtual-currency laundering ecosystem that U.S. authorities linked to ransomware payments, darknet activity, and wider cybercrime finance.

## Audit Note

This page is kept because the action is multinational, but the sanctions, criminal charging, and Dutch seizure pieces are separate legal layers. They are intentionally not collapsed into one generic enforcement story.

## Background

Cryptex and PM2BTC were described by U.S. authorities as key financial services for illicit Russian virtual-currency flows. Treasury and FinCEN focused on the financial-risk side of the ecosystem, while DOJ tied the same action to two Russian defendants and to Dutch seizure activity against the services' infrastructure.

## Participating Parties

### U.S. Authorities
- [[us-treasury|U.S. Department of the Treasury]]
- FinCEN
- OFAC
- [[us-doj|U.S. Department of Justice]]

### Foreign Partner
- [[netherlands-politie|Dutch National Police]]

## Legal Framework

The public action combined sanctions and anti-money-laundering authorities with criminal prosecution. FinCEN's PM2BTC measure is analytically distinct from OFAC's Cryptex sanctions, and the DOJ/EDVA releases show how those financial controls were paired with charges and foreign seizure support.

## Operational Timeline

| Date | Event |
|------|-------|
| 2024-09-26 | Treasury announces coordinated action targeting Cryptex, PM2BTC, and related cybercrime finance infrastructure. |
| 2024-09-26 | FinCEN identifies PM2BTC as a primary money laundering concern and proposes a special measure. |
| 2024-09-26 | DOJ and USAO EDVA announce charges against two Russian nationals and state that Dutch authorities seized related servers. |

## Results and Impact

| Metric | Detail |
|--------|--------|
| Criminal defendants publicly named | 2 |
| Countries with public action disclosed | 2 |
| Cryptocurrency seized | More than USD 7 million |
| Enforcement tools combined | Sanctions, AML special measure, charging, and server seizure |

## Cooperation Mechanisms Used

This action is a strong example of layered financial disruption. Treasury and FinCEN attacked the laundering channels, DOJ added a criminal case narrative, and Dutch partners imposed direct infrastructure costs. The combination matters because cybercrime exchanges often adapt quickly if only one enforcement layer is used.

## Contradictions & Open Questions

- Treasury and DOJ releases describe the same overall action from different institutional angles, so exact operator attribution should be read across documents rather than from one release alone.
- Public releases did not fully disclose how long Dutch-seized infrastructure had supported Cryptex and PM2BTC operations.
- The long-term displacement effect on Russian cybercrime cash-out routes remains unclear.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- U.S. Department of the Treasury, 2024-09-26: Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitator.
- US Department of Justice, 2024-09-26: Two Russian Nationals Charged in Connection with Operating Billion Dollar Money Laundering Services.
- Financial Crimes Enforcement Network, 2024-09-26: Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitator.
- Financial Crimes Enforcement Network, 2024-09-26: Imposition of Special Measure Prohibiting the Transmittal of Funds Involving PM2BTC.
- U.S. Attorney's Office, Eastern District of Virginia, 2024-09-26: Two Russian nationals charged in connection with operating billion-dollar money laundering services; Justice Department seizes web domains for..
- Chainalysis, 2024-09-26: OFAC Designates Russian Exchange Cryptex, FinCEN names PM2BTC.

## Evidence and Attribution Notes

- Treasury identified PM2BTC as a primary money laundering concern and sanctioned Cryptex.
- The action was described as part of a coordinated international effort against Russian cybercrime services.
- Treasury linked Cryptex to ransomware-related and broader cybercriminal financial flows.
- This is the lead Treasury announcement for the September 2024 Cryptex and PM2BTC action.
- This DOJ release complements the Treasury sanctions announcement by documenting the related enforcement action.
- FinCEN identified PM2BTC as a primary money laundering concern and framed the move as part of a coordinated international action.
- The release tied PM2BTC to Russian illicit finance and cybercrime services.
- This FinCEN release is the cleanest U.S. financial-regulatory source for the PM2BTC portion of the September 2024 action.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- U.S. Department of the Treasury, 2024-09-26: Department of the Treasury About Treasury Enter Search Term(s): Advanced Search General Information Role of the Treasury Officials Organizational Chart Orders and Directives Offices Domestic Finance Economic Policy General Counsel International Affairs Management Public Affairs Tax Policy Terrorism and Financial Intelligence Tribal and.
- U.S. Department of Justice, 2024-09-26: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs Two Russian Nationals Charged In Connection With Operating Billion Dollar Money Laundering Services This is archived content from the U.S.
- U.S. Department of Justice, 2024-09-26: The actions involved the unsealing of an indictment charging a Russian national with his involvement in operating multiple money laundering services that catered to cybercriminals, as well as the seizure of websites associated with three illicit cryptocurrency exchanges.
- U.S. Attorney's Office, Eastern District of Virginia, 2024-09-26: Attorney Criminal Civil Services & Programs Victim Witness Assistance Project Safe Neighborhoods Reentry Program Report a Crime Find a Court Document Locate An Inmate Whistleblower Non-Prosecution Pilot Program ## Extraction Notes - parser: document - fetcher: doj_fetch - fetched_at: 2026-04-25T14:18:37+00:00 - final_url:

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a infrastructure-seizure against Cryptex exchange, PM2BTC, and the operators behind a cybercrime-linked virtual-currency laundering network, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Us Treasury and coordination to Us Treasury, with participating or affected jurisdictions recorded as United States and Netherlands.

The cooperation model is documented through named agencies and partners: Us Treasury, Us Doj, Netherlands Politie; enforcement posture: Sanction, Seizure, Indictment.

Operational results captured for the canonical record: 2 indictments; cryptocurrency/asset result recorded as More than USD 7 million; FinCEN designated PM2BTC as a primary money laundering concern.; OFAC sanctioned Cryptex and related infrastructure.; Dutch authorities seized servers associated with Cryptex and PM2BTC..

The canonical source set contains 6 reference(s): 2024 09 26 Treasury Cryptex Pm2btc Coordinated Actions, 2024 09 26 Justice Gov Two Russian Nationals Charged Money Laundering Services, 2024 09 26 Fincen Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency, 2024 09 26 Fincen Imposition Special Measure Prohibiting The Transmittal Of Funds Involving Pm2btc, 2024 09 26 Usao Edva Two Russian Nationals Charged Connection Operating Billion Dollar Money Laundering, 2024 09 26 Chainalysis Ofac Designates Russian Exchange Cryptex Fincen Names Pm2btc.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Legal Basis and Mechanisms Used.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|-------|----------|------|-----|
| [1] | Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency Exchanges and Cybercrime Facilitator | U.S. Department of the Treasury | 2024-09-26 | https://home.treasury.gov/news/press-releases/jy2616 |
| [2] | Two Russian Nationals Charged in Connection with Operating Billion Dollar Money Laundering Services | U.S. Department of Justice | 2024-09-26 | https://www.justice.gov/archives/opa/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering-1 |
| [3] | Treasury Takes Coordinated Actions Against Illicit Russian Virtual Currency | Financial Crimes Enforcement Network | 2024-09-26 | https://www.fincen.gov/news/news-releases/treasury-takes-coordinated-actions-against-illicit-russian-virtual-currency |
| [4] | Imposition of Special Measure Prohibiting the Transmittal of Funds Involving PM2BTC | Financial Crimes Enforcement Network | 2024-09-26 | https://www.fincen.gov/resources/statutes-regulations/federal-register-notices/imposition-special-measure-prohibiting-0 |
| [5] | Two Russian Nationals Charged in Connection with Operating Billion-Dollar Money Laundering Services | USAO Eastern District of Virginia | 2024-09-26 | https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-operating-billion-dollar-money-laundering |
| [6] | OFAC Designates Russian Exchange Cryptex and FinCEN Names PM2BTC | Chainalysis | 2024-09-26 | https://www.chainalysis.com/blog/ofac-sanctions-russian-exchange-cryptex-uaps-fraud-shop-2024/ |
