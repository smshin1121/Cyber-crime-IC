---
aliases:

case_id: CYB-2019-001
challenges_encountered:

coordinating_body: "[[europol-ec3]]"
created: 2026-04-08
credibility_index: 4.2
crime_type: "[[malware-ic]]"
edges:

enforcement_type:

lead_agency: "[[europol-ec3]]"
legal_basis:
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[search-seizure]]"
  - "[[electronic-evidence]]"
lessons_learned:

mechanisms_used:
  - "[[mutual-legal-assistance]]"
  - "[[extradition]]"
  - "[[search-seizure]]"
  - "[[electronic-evidence]]"
  - "[[public-private-cooperation]]"
missing_fields:
  - final_status_for_all_fugitives
  - complete_foreign_sentencing_outcomes
operation_type: joint-investigation
outcome: success
participating_agencies:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
  - "[[office-of-international-affairs]]"
  - "[[us-secret-service]]"
  - "[[ncfta]]"
  - "[[shadowserver]]"
  - "U.S. Attorney's Office for the Western District of Pennsylvania"
  - "Office of the Prosecutor General of Georgia"
  - "Prosecutor General's Office of Ukraine"
  - "Office of the Prosecutor General of the Republic of Moldova"
  - "Public Prosecutor's Office Verden, Germany"
  - "Supreme Prosecutor's Office of Cassation of Bulgaria"
  - "Ministry of Internal Affairs of Georgia"
  - "National Police of Ukraine"
  - "General Police Inspectorate of Moldova"
  - "Lueneburg Police, Germany"
  - "Bulgaria General Directorate for Combatting Organized Crime"
participating_countries:
  - "[[united-states]]"
  - "[[bulgaria]]"
  - "[[germany]]"
  - "[[georgia]]"
  - "[[moldova]]"
  - "[[ukraine]]"
period: 2
related_cases:
  - "[[us-v-konovolov-goznym]]"
related_operations:
  - "[[operation-us-v-konovolov-goznym]]"
results:
  arrests: 10
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  domains_seized: 0
  indictments: 10
  other:
    - "Estimated USD 100 million in attempted theft"
    - "More than 41,000 victim computers were controlled by the network leader"
    - "Parallel prosecutions were initiated in the United States, Georgia, Ukraine, Moldova, and Bulgaria"
    - "Evidence was acquired through coordinated searches in Georgia, Ukraine, Moldova, and Bulgaria"
    - "Nikolov was extradited from Bulgaria to the United States and pleaded guilty in April 2019"
  servers_seized: 0
  victims_notified: 0
source_count: 5
source_tier: 2
sources:
  - "[[2019-05-01_europol-europa-eu_goznym-malware-cybercriminal-network-dismantled-in-international-operation]]"
  - "[[2019-05-16_justice-gov_goznym-cyber-criminal-network-operating-out-of-europe-targeting-american-entitie]]"
  - "[[2019-12-20_justice-gov_three-members-of-goznym-cybercrime-network-sentenced-in-parallel-multi-national]]"
  - "[[bbc-goznym-malware-network-dismantling]]"
  - "[[2019-05-16_bleepingcomputer-com_goznym-cybercrime-group-behind-100-million-damages-dismantled]]"
status: completed
target_entity: "GozNym malware network"
timeframe:
  announced: 2019-05
  end: 2019-05
  ongoing: false
  start: 2016
title: "GozNym Malware Network Dismantling"
title_ko: "GozNym 악성코드 네트워크 해체"
type: operation
updated: 2026-04-27
operation_role: umbrella
parent_operation: ""
summary: "The GozNym action dismantled a transnational malware-and-online-banking-fraud network through coordinated prosecutions and evidence sharing among the United States, Georgia, Ukraine, Moldova, Germany, Bulgaria, Europol, and Eurojust. DOJ described the operation as an unprecedented multi-country prosecution model: the United States indicted ten defendants while partner states pursued parallel domestic prosecutions and supplied evidence through searches, extradition, and MLAT channels."
organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi-cyber-division]]"
  - "[[office-of-international-affairs]]"
  - "[[us-secret-service]]"
  - "[[ncfta]]"
  - "[[shadowserver]]"
crime_types:
  - "[[malware-ic]]"
---
## Summary

The GozNym action was a coordinated multinational malware case, not a one-paragraph takedown. DOJ described the network as a transnational organized cybercrime group that used GozNym malware to capture online-banking credentials, access victim bank accounts, and launder stolen funds through U.S. and foreign beneficiary accounts. The estimated intended loss was **USD 100 million**, with tens of thousands of infected computers worldwide and a victim base concentrated in the United States and Europe.

The operational significance is the prosecution model. The United States unsealed charges against ten members of the network in the Western District of Pennsylvania, while partner jurisdictions pursued parallel domestic cases or supplied evidence against defendants who could not all be brought into U.S. custody.

## Participating Parties

### Coordinating and Judicial Bodies
- [[europol-ec3|Europol EC3]]
- [[eurojust|Eurojust]]
- U.S. Attorney's Office for the Western District of Pennsylvania
- [[office-of-international-affairs|DOJ Office of International Affairs]]

### Law-Enforcement and Prosecutorial Participants
- [[fbi-cyber-division|FBI Pittsburgh Field Office]]
- [[us-secret-service|U.S. Secret Service]]
- Georgia Prosecutor General and Ministry of Internal Affairs
- Ukraine Prosecutor General and National Police
- Moldova Prosecutor General and General Police Inspectorate
- Public Prosecutor's Office Verden and Lueneburg Police, Germany
- Bulgaria Supreme Prosecutor's Office of Cassation and General Directorate for Combatting Organized Crime
- [[ncfta|National Cyber-Forensics and Training Alliance]]
- [[shadowserver|Shadowserver Foundation]]

### Participating Countries
The core participating jurisdictions were [[united-states|United States]], [[bulgaria|Bulgaria]], [[germany|Germany]], [[georgia|Georgia]], [[moldova|Moldova]], and [[ukraine|Ukraine]]. Russia appears mainly as a defendant-residence and fugitive jurisdiction; it is not listed as a cooperating participant in the current source set.

## Cooperation Architecture

The case combined several cooperation channels. Bulgarian authorities searched and arrested Krasimir Nikolov at the request of the United States, then extradited him to Pittsburgh in December 2016. The DOJ Office of International Affairs coordinated foreign searches, arrests, extradition requests, and evidence-sharing through Mutual Legal Assistance Treaty requests.

For defendants who could not be extradited, the model shifted to evidence sharing and parallel domestic prosecution. DOJ says evidence came from coordinated searches in Georgia, Ukraine, Moldova, and Bulgaria, plus evidence shared by U.S. and German investigations. Georgia prosecuted Alexander Konovolov and Marat Kazandjian domestically; Ukraine pursued Gennady Kapkanov; Moldova pursued Eduard Malanici and associates.

## Defendant and Role Map

| Defendant / actor | Jurisdictional status | Alleged role |
|---|---|---|
| Alexander Konovolov | Prosecuted in Georgia | Organizer who controlled more than 41,000 infected victim computers |
| Marat Kazandjian | Prosecuted in Georgia | Technical administrator and primary assistant |
| Krasimir Nikolov | Extradited from Bulgaria to the United States; guilty plea entered in April 2019 | Account-takeover specialist / casher |
| Gennady Kapkanov | Prosecuted in Ukraine | Avalanche bulletproof-hosting administrator tied to GozNym infrastructure |
| Eduard Malanici | Prosecuted in Moldova | Crypting-service provider used to evade antivirus detection |
| Farkhad Manokhin | Arrested in Sri Lanka at U.S. request, then absconded to Russia | Cash-out / drop-master role |
| Five Russian nationals | Fugitives in the DOJ record | Malware development, spam distribution, cashing, and cash-out functions |

## Evidence and Infrastructure

The indictment described a cybercrime-as-a-service structure recruited from Russian-language criminal forums. Members supplied malware development, spam distribution, crypting, account takeover, cash-out, and bulletproof-hosting services. Kapkanov's alleged role linked GozNym to the Avalanche hosting infrastructure, which German-led action had already targeted in 2016.

Victim examples included U.S. businesses, a law firm, a church, an association serving people with disabilities, a casino, and a German medical-equipment distributor with a U.S. subsidiary. This mix matters for jurisdiction: the Western District of Pennsylvania case was not based only on abstract U.S. victimization, but on named U.S. entities and banking effects.

## Legal Basis

The collected sources identify three concrete procedural mechanisms: extradition, search and seizure, and MLAT-enabled evidence sharing. The record does not show a single joint court, but a distributed model in which each state used its own criminal procedure while sharing evidence and coordinating public enforcement action through Europol and Eurojust. This is why the page treats the operation as a joint investigation and parallel-prosecution matter rather than as a conventional single-country indictment.

## Results

- **10 defendants** charged in the newly unsealed U.S. indictment, with an eleventh member charged separately.
- **More than 41,000 infected victim computers** allegedly controlled by Konovolov.
- **USD 100 million** in estimated attempted theft.
- Parallel prosecutions and evidence sharing across the United States, Georgia, Ukraine, Moldova, Germany, and Bulgaria.
- Nikolov extradited from Bulgaria to the United States and pleaded guilty before sentencing.

## Open Questions

- The current page does not yet resolve the final status of every Russian fugitive.
- Some foreign prosecution outcomes are covered by the 2019 follow-up DOJ sentencing source, but the full docket histories for Georgia, Ukraine, Moldova, and Bulgaria need separate case-level reconciliation.
- The Europol source in the corpus is summary-level; the DOJ source carries most of the operational detail and should remain the principal source for mechanisms.

## Source Coverage

Reference [2], the DOJ release, is the primary mechanism source. Reference [1] confirms Europol's public framing of the dismantling. Reference [3] supplies later prosecution outcome data for three members. References [4] and [5] are media corroboration and should not override the official DOJ/Europol records where details conflict.

<!-- SOURCE_ENRICHMENT_START -->

## Source Coverage

- Europol, 2019-05-01: Goznym Malware Cybercriminal Network Dismantled In International Operation.
- US DOJ (W.D. Pa.), 2019-05-16: GozNym Cyber-Criminal Network Operating out of Europe Targeting American Entities Dismantled in International Operation.
- US DOJ USAO, 2019-12-20: Three Members of GozNym Cybercrime Network Sentenced in Parallel Multi-National Prosecutions in Pittsburgh and Tbilisi, Georgia.
- BBC News, 2019-05-16: BBC: GozNym cyber-crime gang which stole millions busted.
- BleepingComputer, 2019-05-16: GozNym Cybercrime Group Behind $100 Million Damages Dismantled.

## Operational Timeline

- 2016: activity or investigation start.
- 2019-05: public announcement.
- 2019-05: reported enforcement endpoint.
- 2019-05-01: public source coverage from Europol.
- 2019-05-16: public source coverage from BBC News, BleepingComputer, US DOJ (W.D. Pa.).
- 2019-12-20: public source coverage from US DOJ USAO.

<!-- SOURCE_ENRICHMENT_END -->

<!-- RAW_TEXT_HIGHLIGHTS_START -->

## Raw Source Highlights

- US DOJ (W.D. Pa.), 2019-05-16: Department of Justice title="About" title="News" title="Guidance & Resources" Justice.gov Office of Public Affairs GozNym Cyber-Criminal Network Operating Out of Europe Targeting American Entities Dismantled In International Operation This is archived content from the U.S.
- US DOJ (W.D. Pa.), 2019-05-16: The operation was highlighted by the unprecedented initiation of criminal prosecutions against members of the network in four different countries as a result of cooperation between the United States, Georgia, Ukraine, Moldova, Germany, Bulgaria, Europol and Eurojust.
- US DOJ USAO, 2019-12-20: Attorney's Office, Western District of Pennsylvania PITTSBURGH - A resident of Varna, Bulgaria, was sentenced on December 16, 2019, in federal court in Pittsburgh to a period of time served after having served more than 39 months in prison following his conviction on charges of criminal conspiracy, computer fraud, and bank fraud for his.
- US DOJ USAO, 2019-12-20: At the request of the United States, Nikolov was arrested in September 2016 by Bulgarian authorities and extradited to Pittsburgh in December 2016 to face prosecution in the Western District of Pennsylvania.

<!-- RAW_TEXT_HIGHLIGHTS_END -->

<!-- CANONICAL_ASSESSMENT_START -->

## Canonical Operation Assessment

This page is retained as a canonical operation because it describes a joint-investigation against GozNym malware network, rather than a defendant-specific follow-on action. The record attributes lead responsibility to Europol Ec3 and coordination to Europol Ec3, with participating or affected jurisdictions recorded as United States, Bulgaria, Germany, Georgia, Moldova, Ukraine.

The cooperation model is documented through named agencies and partners: Europol Ec3, Eurojust, Fbi Cyber Division, Office Of International Affairs, Us Secret Service, Ncfta, Shadowserver, U.s. Attorney's Office For The Western District Of Pennsylvania, Office Of The Prosecutor General Of Georgia, Prosecutor General's Office Of Ukraine; mechanisms: mutual legal assistance, Extradition, Search Seizure, Electronic Evidence, Public Private Cooperation; legal basis: mutual legal assistance, Extradition, Search Seizure, Electronic Evidence.

Operational results captured for the canonical record: 10 arrests; 10 indictments; Estimated USD 100 million in attempted theft; More than 41,000 victim computers were controlled by the network leader; Parallel prosecutions were initiated in the United States, Georgia, Ukraine, Moldova, and Bulgaria; Evidence was acquired through coordinated searches in Georgia, Ukraine, Moldova, and Bulgaria.

The canonical source set contains 5 reference(s): 2019 05 01 Europol Europa Eu Goznym Malware Cybercriminal Network Dismantled In International Operation, 2019 05 16 Justice Gov Goznym Cyber Criminal Network Operating Out Of Europe Targeting American Entitie, 2019 12 20 Justice Gov Three Members Of Goznym Cybercrime Network Sentenced In Parallel Multi National, Bbc Goznym Malware Network Dismantling, 2019 05 16 Bleepingcomputer Com Goznym Cybercrime Group Behind 100 Million Damages Dismantled.
The source floor is met for a canonical operation, but source breadth does not by itself prove that every downstream arrest or sentencing is part of this operation; follow-on records should remain linked separately.
Known metadata gaps still carried by this page: Final Status For All Fugitives and Complete Foreign Sentencing Outcomes.
For dataset use, this page should be treated as the operation-level aggregation point: country, agency, mechanism and outcome fields describe the coordinated enforcement action as a whole. Later indictments, pleas, sentencings, extraditions or forfeiture actions should be attached as related case or absorbed follow-on records unless the source explicitly presents them as a new multinational operation.
When source records contain broader background, repeated wire-service republications, or topic-page material, this assessment gives priority to facts that are directly tied to the named operation, its participating authorities, its target infrastructure or criminal service, and its measurable enforcement outcome. Peripheral source titles are not treated as independent taxonomy or result evidence.
This keeps the canonical record analytically bounded and reproducible.

<!-- CANONICAL_ASSESSMENT_END -->

## References

| # | Title | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Goznym Malware Cybercriminal Network Dismantled In International Operation | Europol | 2019-05-01 | https://www.europol.europa.eu/media-press/newsroom/news/goznym-malware-cybercriminal-network-dismantled-in-international-operation |
| [2] | GozNym Cyber-Criminal Network Operating out of Europe Targeting American Entities Dismantled in International Operation | US DOJ (W.D. Pa.) | 2019-05-16 | https://www.justice.gov/archives/opa/pr/goznym-cyber-criminal-network-operating-out-europe-targeting-american-entities-dismantled |
| [3] | Three Members of GozNym Cybercrime Network Sentenced in Parallel Multi-National Prosecutions in Pittsburgh and Tbilisi, Georgia | US DOJ USAO | 2019-12-20 | https://www.justice.gov/usao-wdpa/pr/three-members-goznym-cybercrime-network-sentenced-parallel-multi-national-prosecutions |
| [4] | BBC: GozNym cyber-crime gang which stole millions busted | BBC News | 2019-05-16 | https://www.bbc.com/news/technology-48294788 |
| [5] | GozNym Cybercrime Group Behind $100 Million Damages Dismantled | BleepingComputer | 2019-05-16 | https://www.bleepingcomputer.com/news/security/goznym-cybercrime-group-behind-100-million-damages-dismantled/ |
