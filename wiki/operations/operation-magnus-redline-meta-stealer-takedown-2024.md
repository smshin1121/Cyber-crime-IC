---
type: operation
title: "Operation Magnus — RedLine and META Infostealer Takedown (October 2024)"
aliases:
  - "Operation Magnus"
  - "RedLine takedown 2024"
  - "META infostealer takedown 2024"
  - "RedLine/META infostealer takedown"
case_id: CYB-2024-100
period: 2
operation_type: takedown
status: completed
enforcement_type:
  - arrest
  - seizure
  - takedown
  - indictment
outcome: success
timeframe:
  announced: 2024-10-29
  start: 2024-10-28
  end: 2024-10-28
  ongoing: false
crime_types:
  - "[[malware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[identity-theft]]"
crime_type: "[[malware-ic]]"
target_entity: "RedLine Infostealer and META Infostealer (malware-as-a-service)"
lead_agency: "[[netherlands-politie]]"
coordinating_body: "[[eurojust]]"
participating_countries:
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[belgium]]"
  - "[[portugal]]"
  - "[[united-kingdom]]"
  - "[[australia]]"
participating_agencies:
  - "[[eurojust]]"
  - "[[netherlands-politie]]"
  - "[[netherlands-om]]"
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[us-ncis]]"
  - "[[us-dcis]]"
  - "[[belgium-federal-police]]"
  - "[[portugal-policia-judiciaria]]"
  - "[[uk-nca]]"
  - "[[australia-afp]]"
legal_basis: ""
mechanisms_used:
  - "[[eurojust-coordination-meeting]]"
results:
  arrests: 2
  indictments: 1
  servers_seized: 3
  domains_seized: 2
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "Client database from RedLine and META platforms retrieved by investigators"
    - "Over 1,200 infected servers across dozens of countries identified during investigation"
    - "Charges unsealed in the United States against Maxim Rudometov (developer/administrator of RedLine Infostealer)"
    - "Public victim-check resource published at operation-magnus.com (with ESET-provided RedLine/META scanner)"
related_cases:
  []
related_operations:
  - "[[us-v-sokolovsky-raccoon-infostealer]]"
  - "[[us-netherlands-belgium-minasyan-redline-infostealer-extradition-2026]]"
challenges_encountered:
  []
lessons_learned:
  - "Private-sector tip (unnamed security company) seeded a Dutch investigation that scaled to a six-country coordinated takedown — confirms the value of public-private intake channels for MaaS infrastructure mapping."
  - "Eurojust coordination allowed simultaneous Dutch infrastructure seizure, Belgian arrest action, and US indictment unsealing on the same day — single-day multi-jurisdiction synchronization remains the operational signature of EU-coordinated MaaS takedowns."
source_count: 1
sources:
  - "[[2024-10-29_eurojust-europa-eu_operation-magnus-redline-meta-infostealer-takedown]]"
created: 2026-05-09
updated: 2026-05-16
last_verified: 2026-05-09
---
> [!info] Provisional page
> This operation page is published below the preferred 5-source threshold (CLAUDE.md "Entity creation threshold"). It rests on a single tier-1 primary source (Eurojust press release, 2024-10-29). Additional companion sources (DOJ unsealing, IRS-CI page, Dutch police press release) should be ingested to lift the page to standard publication state.

## Summary

**Operation Magnus** was a coordinated international law-enforcement action that, on **28 October 2024**, dismantled the operational infrastructure of two prolific malware-as-a-service infostealers — **RedLine** and **META** — and unsealed criminal charges in the United States against one of RedLine's developers. The action was coordinated by **[[eurojust|Eurojust]]** and brought together authorities from six jurisdictions: the Netherlands, the United States, Belgium, Portugal, the United Kingdom, and Australia. The operation produced three server seizures in the Netherlands, two domain seizures, two arrests in Belgium, US indictments unsealed, and the recovery of a database of paying RedLine/META clients (Source: [[2024-10-29_eurojust-europa-eu_operation-magnus-redline-meta-infostealer-takedown|Eurojust press release, 29 Oct 2024]]).

It is *almost certain* (>95% confidence, single tier-1 primary source plus open companion victim site) that the action took place on 28 October 2024 and that the six countries listed were the named participating jurisdictions. The "Operation Magnus" codename appears on the public victim-facing site operation-magnus.com but is not used in the Eurojust release headline; it is recorded as an alias.

## Background

RedLine and META are infostealer malware families operated as **malware-as-a-service** — criminal customers paid to use the infrastructure to deploy the stealer against victims and harvest credentials. Per the Eurojust release, the malware exfiltrated saved usernames and passwords, automatically saved form data (addresses, email addresses, phone numbers), cryptocurrency wallet contents, and browser cookies. Eurojust characterizes the victim scale as "millions" worldwide.

The investigation began after victims came forward and an unnamed private-sector security company notified authorities about possible RedLine/META servers hosted in the Netherlands. Investigators subsequently mapped over 1,200 infected/operating servers across dozens of countries — the scope that justified the multi-jurisdictional coordination.

## Participating Parties

### Coordinating body

- **[[eurojust|Eurojust (European Union Agency for Criminal Justice Cooperation)]]** — coordinated information exchange and synchronized action across all six jurisdictions.

### Lead investigative agency

- **[[netherlands-politie|Netherlands National Police, Team Cybercrime Limburg]]**, with the Dutch **[[netherlands-om|Public Prosecution Service (Openbaar Ministerie)]]**.

### Participating jurisdictions and authorities (as named in the Eurojust release)

| Country | Authorities |
|---|---|
| [[netherlands\|Netherlands]] | National Police (Team Cybercrime Limburg); Public Prosecution Service |
| [[united-states\|United States]] | [[fbi\|FBI]]; [[us-ncis\|Naval Criminal Investigative Service (NCIS)]]; Internal Revenue Service Criminal Investigations (IRS-CI); [[us-dcis\|Department of Defense Criminal Investigative Service (DCIS)]]; Army Criminal Investigation Division (Army CID); prosecution coordinated by [[us-doj\|US Department of Justice]] |
| [[belgium\|Belgium]] | [[belgium-federal-police\|Federal Police]]; Federal Prosecutor's Office |
| [[portugal\|Portugal]] | [[portugal-policia-judiciaria\|Polícia Judiciária]] |
| [[united-kingdom\|United Kingdom]] | [[uk-nca\|National Crime Agency (NCA)]] |
| [[australia\|Australia]] | [[australia-afp\|Australian Federal Police (AFP)]] |

### Private-sector touchpoints

- An unnamed security company supplied the initial tip identifying servers in the Netherlands (mentioned in the Eurojust release without attribution).
- ESET provided a free RedLine/META detection scanner published via operation-magnus.com (companion source — the Eurojust release does not name the vendor).

## Legal Framework

The Eurojust release does not cite specific treaty articles or legal-cooperation instruments by name. Eurojust coordination of multi-jurisdiction cybercrime takedowns is *typically* (~80% confidence based on prior comparable Eurojust-coordinated operations such as [[operation-cronos-phase1|Cronos Phase 1]] and [[us-v-sokolovsky-raccoon-infostealer|Raccoon Infostealer]]) anchored in the **Eurojust Regulation (EU) 2018/1727** for coordination, the **Budapest Convention on Cybercrime** for cross-border procedural authority among parties, and bilateral **Mutual Legal Assistance** channels for the US-EU evidence chain. None of these are explicitly cited in the present source — flagging accordingly.

> [!warning] Legal status check needed
> The specific statutory and treaty bases used are not enumerated in the Eurojust press release. The DOJ unsealing reportedly cites 18 U.S.C. §§ 1029 (access device fraud), 1030 and 371 (computer-intrusion conspiracy), and 1956 (money laundering) for the Maxim Rudometov indictment, per the IRS Criminal Investigation companion page; this awaits confirmation against the unsealed indictment text directly. Adding those citations to `legal_basis` is deferred until that source is ingested.

## Operational Timeline

| Date | Event |
|---|---|
| (pre-2024) | Victim reports plus private-sector tip flag possible RedLine/META servers in the Netherlands. |
| 2024 (date not in source) | Investigators map >1,200 infected servers across dozens of countries; cooperation channel established under Eurojust coordination. |
| **2024-10-28** | Worldwide operational day: 3 Dutch servers shut down; 2 domains seized; 2 arrests executed in Belgium; charges unsealed in the United States. |
| **2024-10-29** | Eurojust publishes coordinated press release; Dutch police launches public victim-check resource at operation-magnus.com. |

## Results and Impact

| Result | Count | Source statement |
|---|---|---|
| Servers shut down (Netherlands) | 3 | "three servers taken down in the Netherlands" |
| Domains seized | 2 | "two domains seized" |
| Arrests (Belgium) | 2 | "two people taken into custody in Belgium" |
| US charges unsealed | 1 indictment (Maxim Rudometov) | "charges unsealed in the United States" |
| Client database retrieved | 1 | "a client database of RedLine and Meta was retrieved" (paraphrased from Eurojust) |
| Infected/affected servers identified | >1,200 | "over 1,200 servers in dozens of countries were running the malware" |
| Victim scale | "millions" | Eurojust framing |

The takedown rendered the RedLine and META infostealers non-functional for the immediate post-operation window and exposed the customer pool — both prerequisites for downstream investigations against MaaS *operators* and *customers* alike.

## Cooperation Mechanisms Used

- **Eurojust coordination** (information exchange + synchronized multi-jurisdiction action) is the only mechanism explicitly named in the Eurojust press release.
- The simultaneous (a) Dutch infrastructure seizure, (b) Belgian arrest, and (c) US indictment unsealing pattern is consistent with — but not explicitly attributed to — a **[[joint-investigation-team|joint investigation team (JIT)]]** structure. Whether a formal JIT was registered with Eurojust is not stated in the source.
- The **[[j-cat|Joint Cybercrime Action Taskforce (J-CAT)]]** at Europol is mentioned by the IRS-CI companion source as the coordinating taskforce for the US side; this is not echoed in the Eurojust release and is therefore not asserted in `mechanisms_used` pending direct confirmation.

## Challenges and Friction Points

The Eurojust release does not narrate friction points. Inferred from the operation's structure (not asserted as fact):

- Six-jurisdiction synchronization across two continents and four time zones implied non-trivial pre-action sequencing — managed via Eurojust coordination.
- The decision to execute the only physical arrests in Belgium (rather than the Netherlands, which hosted infrastructure, or the US, which led prosecution) suggests jurisdictional placement of the suspects rather than a strategic forum-shopping outcome — but this is not stated.

## Lessons Learned

- **Private-sector intake matters**: an unnamed security company's tip seeded the Dutch investigation that scaled to a six-country takedown, reinforcing the value of voluntary disclosure channels into national cybercrime units.
- **Eurojust coordination delivers same-day multi-jurisdiction synchronization**: the operation reproduced the [[operation-cronos-phase1|Operation Cronos Phase 1]] template (single-day, multi-country, infrastructure + arrests + indictments) for the MaaS-infostealer class.
- **MaaS client-database retrieval is a force-multiplier**: recovering the RedLine/META customer list converts a single takedown into a pipeline of follow-on investigations against subscribers worldwide.

## Follow-Up Actions

The Eurojust release does not enumerate follow-up actions beyond the takedown. Subsequent Maxim Rudometov prosecution proceedings (US) and possible client-database-driven actions in non-listed jurisdictions are *likely* (~70% confidence based on prior MaaS takedowns such as Raccoon Infostealer) but await documentation in further sources.

## Korean Involvement (한국의 참여)

The Eurojust press release does not name South Korea among the participating jurisdictions, nor does it list any Korean agency among the executing authorities. Korean victims are *plausibly* affected given Eurojust's "millions worldwide" framing and RedLine's known global distribution, but the source does not establish Korean operational participation. No assertion of Korean participation is made on this page.

## Contradictions & Open Questions

- **Operation codename**: "Operation Magnus" appears on the victim-facing site (operation-magnus.com) and in companion press, but not in the Eurojust release headline. Recorded as alias.
- **Formal JIT?**: Whether the multi-country coordination was formalized as a Joint Investigation Team (JIT) registered with Eurojust is not stated in the available source.
- **Statutory citations**: The Eurojust release does not enumerate the US statutes or treaty articles invoked. Pending DOJ unsealed-indictment ingestion.
- **Identity of the private-sector tip-source**: Eurojust's release does not name the security company that initially flagged Dutch-hosted RedLine/META servers; companion press indicates ESET supplied the post-takedown victim scanner, but pre-takedown attribution is unconfirmed.
- **Belgium-arrest identities**: The Eurojust release does not name the two suspects taken into custody in Belgium nor specify whether they are RedLine operators, META operators, or customers.
