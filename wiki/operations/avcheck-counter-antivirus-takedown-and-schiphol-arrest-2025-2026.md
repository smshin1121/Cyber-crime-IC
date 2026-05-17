---
type: operation
title: "AvCheck Counter-Antivirus Takedown & Schiphol Follow-up Arrest (NL/US/FI, 2025–2026)"
aliases:
  - "AvCheck takedown"
  - "AvCheck.net seizure"
  - "Operation Endgame — AvCheck (CAV/crypter sub-operation)"
  - "OM.nl Schiphol cybercrime arrest 12 Jan 2026"
  - "Counter Antivirus service takedown 27 May 2025"
case_id: CYB-2025-447
period: 3
operation_type: infrastructure-seizure
status: ongoing
enforcement_type:
  - seizure
  - takedown
  - arrest
outcome: partial
timeframe:
  announced: 2025-05-27
  start: 2025-05-27
  end: 2026-01-11
  ongoing: true
crime_types:
  - "[[malware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[ransomware-ic]]"
crime_type: malware-ic
target_entity: "Counter-Antivirus (CAV) testing service avcheck.net and associated crypter domains (Cryptor.biz, Cryptor.live, Crypt.guru per external reporting); Amsterdam-based operator and his two companies"
lead_agency: ""
coordinating_body: ""
participating_countries:
  - "[[netherlands]]"
  - "[[united-states]]"
  - "[[finland]]"
participating_agencies:
  - "[[netherlands-om]]"
  - "[[netherlands-politie]]"
  - "[[dutch-nhtcu]]"
  - "[[us-doj]]"
  - "[[fbi]]"
  - "[[us-secret-service]]"
  - "[[finland-nbi]]"
legal_basis:
  - "[[budapest-convention]]"
  - "Dutch Wetboek van Strafvordering (computer-evidence and seizure provisions)"
  - "U.S. domain seizure authority"
mechanisms_used:
  - "[[mlat-process]]"
  - "informal multi-agency coordination (NL-US-FI)"
  - "international wanted-person flagging (signalering)"
results:
  arrests: 1
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "1 international suspect arrested at Schiphol airport on 11 January 2026 (announced 12 January)"
    - "Two companies (in Amsterdam) controlled by the suspect identified as part of the CAV service operation"
    - "Data carriers (gegevensdragers) seized from the suspect for forensic analysis"
    - "Underlying May 2025 operation (NL/US/FI) dismantled the CAV/crypter testing service used by malware developers — externally identified as AvCheck.net + Cryptor.biz + Cryptor.live + Crypt.guru (4 domains seized by U.S. DOJ on 27 May 2025)"
edges:
  - source_actor: Netherlands
    target_actor: "United States"
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: Netherlands
    target_actor: Finland
    cooperation_type: joint_investigation
    legal_basis: Budapest_Convention
    direction: undirected
  - source_actor: "United States"
    target_actor: Finland
    cooperation_type: info_sharing
    legal_basis: Budapest_Convention
    direction: undirected
credibility_index: 3.0
source_tier: 1
missing_fields:
  - "exact servers/domains count in OM.nl tier-1 source (only externally reported as 4 domains)"
  - "details of UAE cooperation (or absence thereof) regarding the suspect's relocation"
  - "MLAT request specifics (NL→US, NL→FI) not disclosed"
  - "links to specific malware families whose operators relied on the service"
related_cases:
  []
related_operations:
  - "[[operation-endgame]]"
  - "[[operation-endgame-phase2]]"
challenges_encountered:
  []
lessons_learned:
  - "Counter-Antivirus / crypter services are an upstream chokepoint for malware delivery — disrupting them creates downstream visibility into the operators of the malware that used them."
  - "Tri-lateral coordination (NL-US-FI) on a single CAV service produced both immediate infrastructure takedown (May 2025) and a follow-up arrest at a non-extraditing transit point (Schiphol, January 2026) — illustrating the value of international wanted-person flagging when the suspect attempts to relocate to a non-cooperating jurisdiction (UAE)."
  - "Border-stop arrest is a viable backup pathway when extradition from the suspect's chosen safe haven is uncertain."
source_count: 2
sources:
  - "[[2026-01-12_om-nl_avcheck-amsterdam-schiphol-arrest-cybercrime]]"
  - "[[2025-05-29_justice-gov-usao-sdtx_websites-selling-hacking-tools-cybercriminals-seized]]"
created: 2026-05-10
updated: 2026-05-17
---
# AvCheck Counter-Antivirus Takedown & Schiphol Follow-up Arrest (NL/US/FI, 2025–2026)

> [!info] Provisional / single-source page
> This page is published below the preferred source-count threshold (≥5) because the underlying operation is documented in only one tier-1 source we hold (OM.nl 12 Jan 2026), with the AvCheck identification asserted by tier-2 reporting (The Register, Infosecurity Magazine, SC Media). Treat the AvCheck attribution and the May 2025 4-domain seizure detail as *highly likely* but not directly confirmed by the tier-1 source until further DOJ / FBI / Politie primary statements are ingested.

## Summary

On the evening of Sunday 11 January 2026, the Royal Netherlands Marechaussee arrested a 33-year-old Dutch national at Amsterdam Schiphol Airport. The Public Prosecution Service's national office (Landelijk Parket) announced the arrest on 12 January 2026 and described the suspect as the operator of a service that allowed cybercriminals to test malware against antivirus engines so they could iteratively refine the obfuscation of malicious files until detection rates dropped. Two of the suspect's companies, based in Amsterdam, are part of the same investigation. The suspect had earlier deregistered from the Netherlands and relocated to the United Arab Emirates; he had been internationally flagged (internationaal gesignaleerd) for some time before the Schiphol stop. Data carriers were seized from him; Team High Tech Crime (THTC) of the National Unit for Investigation and Special Interventions of the Dutch police is conducting further investigation.

The arrest is the follow-up to a coordinated international operation in **May 2025** in which the Dutch THTC, together with the **United States** and **Finland**, dismantled what OM.nl describes as a "sleuteldienst voor ontwikkelaars van malware" (key service for malware developers). Independent reporting identifies that May 2025 operation as the **AvCheck.net** Counter-Antivirus (CAV) takedown — a 27 May 2025 U.S. DOJ seizure of four domains (avcheck.net, cryptor.biz, cryptor.live, crypt.guru), conducted in partnership with Dutch and Finnish authorities and announced by DOJ as part of the broader Operation Endgame umbrella.

## Background

A **Counter-Antivirus (CAV)** service — also called a "crypter check" or "scantime checker" — lets a malware developer upload a candidate payload and observe how many of a panel of antivirus engines (typically 20–30) flag it as malicious. By iterating, the developer narrows down which engines still detect the binary and tunes obfuscation, packing, or signing until detection drops to near-zero. This pre-deployment laundering step is, as OM.nl puts it, "een belangrijke schakel" (an important link in the chain) for any cybercriminal who wants to maximise the success rate of malware-borne attacks. CAV services therefore sit upstream of ransomware distribution, banking-trojan campaigns, info-stealer operations, and commodity loader infrastructure.

Disrupting one such service has cascading visibility benefits: investigators inherit the customer logs, the malware samples that were tested, and (where present) the payment metadata. That intelligence is what the OM.nl release implicitly relies on when it says "informatie uit dat onderzoek vormde de aanleiding voor een afzonderlijk onderzoek" (information from that investigation formed the basis for a separate investigation) into the Dutch operator and his two companies.

## Participating parties

- **Netherlands**
  - [[netherlands-om|Openbaar Ministerie — Landelijk Parket]] (lead prosecutor for the follow-up case)
  - [[netherlands-politie|Politie / National Unit (Eenheid Landelijke Opsporing en Interventies)]] — Team High Tech Crime (THTC) (lead investigator)
  - [[dutch-nhtcu|Dutch National High Tech Crime Unit (legacy label for THTC)]]
  - Koninklijke Marechaussee (Royal Marechaussee) — executed the Schiphol arrest (no dedicated wiki page yet; reference in prose only)
- **United States** (May 2025 takedown)
  - [[us-doj|U.S. Department of Justice]] (announced the 27 May 2025 four-domain seizure per external reporting)
  - [[fbi|FBI]] — operational role per external reporting
  - [[us-secret-service|U.S. Secret Service]] — operational role per external reporting
- **Finland** (May 2025 takedown)
  - [[finland-nbi|Finland National Bureau of Investigation (Keskusrikospoliisi)]]
- **United Arab Emirates** — country to which the suspect had relocated; OM.nl does not characterise UAE as a cooperating party. The arrest was effected at the suspect's transit through Schiphol, not at the suspect's residence in the UAE.

## Legal framework

The OM.nl release does not enumerate the specific statutory hooks. Plausibly applicable Dutch instruments include:

- **Wetboek van Strafvordering** — articles governing seizure of data carriers (gegevensdragers) and arrest based on international flagging.
- **Wetboek van Strafrecht** — computer-misuse provisions covering aiding and abetting (medeplichtigheid) the commission of computer crimes (artt. 138ab, 350a Sr.) by providing a service knowingly used for malware refinement.
- For the cross-border component: [[budapest-convention|Budapest Convention on Cybercrime]] (Netherlands, United States, and Finland are all parties) underpinned the NL/US/FI evidence sharing that led to the May 2025 seizures and to the identification of the Dutch operator.

The international flagging mechanism (signalering) is most likely an **Interpol Red/Blue Notice** or **Schengen Information System (SIS II)** alert; OM.nl does not specify which.

## Operational timeline

- **Pre-2025**: Suspect (33-year-old Dutch national, based in Amsterdam) operates a CAV testing service and two related companies; service is used by malware developers worldwide.
- **2024–early 2025**: Suspect deregisters from the Netherlands and relocates to the UAE.
- **27 May 2025**: Coordinated NL-US-FI takedown of the CAV/crypter service. External reporting names AvCheck.net, Cryptor.biz, Cryptor.live, and Crypt.guru as the four seized domains; OM.nl tier-1 source describes it generically as "een sleuteldienst voor ontwikkelaars van malware".
- **Mid-to-late 2025**: Intelligence from the seized infrastructure leads to a separate Dutch investigation by THTC into the suspect's two Amsterdam companies. International flagging is issued.
- **11 January 2026 (Sunday evening)**: Suspect transits through Schiphol; Koninklijke Marechaussee arrests him on the basis of the existing international signalering. Data carriers are seized.
- **12 January 2026 (Monday)**: Landelijk Parket publicly announces the arrest in a brief Nieuwsbericht.
- **Post-12 January 2026**: THTC continues forensic analysis of the seized data carriers; case has not yet entered public court phase as of this page's creation.

## Results and impact

- **1 arrest** of a named-but-unidentified 33-year-old Dutch national.
- **Two Dutch companies** identified as suspected vehicles for the CAV service (located in Amsterdam).
- **Data carriers seized** for forensic exploitation.
- **Predicate effect**: extends the May 2025 takedown beyond pure infrastructure seizure into individual accountability — a pattern characteristic of [[operation-endgame|Operation Endgame]]'s multi-phase model.
- **No** monetary forfeiture, decryption-key recovery, or victim-notification figures disclosed in the OM.nl release.

## Cooperation mechanisms used

- **NL ↔ US ↔ FI tri-lateral joint investigation** for the May 2025 takedown — type, formality, and coordinating body not specified by OM.nl.
- **International flagging (signalering)** as the operative tool that converted the suspect's transit through Schiphol into an arrestable event.
- **THTC ↔ Marechaussee handover** at the border for execution of the arrest.

## Challenges and friction points

- **UAE as relocation jurisdiction**: The suspect's move to the UAE is a textbook example of relocation to a state with limited mutual-legal-assistance practice on cybercrime — the Netherlands evidently did not pursue (or could not effect) extradition from the UAE, and instead waited for the suspect to transit through a cooperating jurisdiction. This pattern recurs in many post-Endgame arrests.
- **Tier-1 attribution gap**: The OM.nl release does not name the underlying takedown ("AvCheck") or specify the four seized domains, leaving observers reliant on tier-2 reporting for the substantive linkage. Wiki integration must therefore flag the AvCheck identification as inferential.

## Lessons learned

- Counter-Antivirus / crypter services are an upstream chokepoint for malware delivery — disrupting them creates downstream visibility into the operators of the malware that used them.
- Tri-lateral coordination (NL-US-FI) on a single CAV service produced both immediate infrastructure takedown (May 2025) and a follow-up arrest at a non-extraditing transit point (Schiphol, January 2026) — illustrating the value of international wanted-person flagging when the suspect attempts to relocate to a non-cooperating jurisdiction (UAE).
- Border-stop arrest is a viable backup pathway when extradition from the suspect's chosen safe haven is uncertain.

## Follow-up actions

- Awaiting public court phase / charging instrument from Landelijk Parket.
- Awaiting any U.S. or Finnish public statement identifying the suspect or charging parallel offences.
- Awaiting forensic analysis of the seized data carriers (likely to surface customer lists of malware developers who used the service — potential basis for further arrests in third countries).

## Korean Involvement (한국의 참여)

OM.nl 보도자료는 한국 관련 협력을 언급하지 않는다. AvCheck/CAV 서비스 사용자 가운데 한국 IP 또는 한국 사업자가 포함되어 있었는지 여부는 외부 보도에서도 확인되지 않았으며, 본 사건 단계에서는 한국 관련성은 없는 것으로 평가된다 (highly unlikely). 향후 데이터 캐리어 포렌식 결과가 공개되면 재평가 필요.

## Contradictions & Open Questions

- **Did the OM.nl-described May 2025 operation correspond to AvCheck.net, or to a different CAV/crypter service?** External tier-2 reporting (The Register 2026-01-13, Infosecurity Magazine, SC Media) treats the linkage as established. OM.nl tier-1 source does not name the service. Likely AvCheck (highly likely) but flagged here pending further tier-1 corroboration.
- **What was the U.S. charging vehicle?** U.S. DOJ may have its own indictment for the suspect (separate from the Dutch case) given that the May 2025 seizure was DOJ-announced; this is unconfirmed.
- **Was the UAE asked for extradition before the Schiphol stop?** OM.nl is silent. The pattern is consistent with NL having relied on the international signalering as the primary mechanism, treating UAE as non-cooperating.
- **Other CAV operators**: how many additional individuals (developers / resellers / customers) does the seized infrastructure expose? Not disclosed.

## See also

- [[operation-endgame]] — broader Operation Endgame umbrella (NL/US/FR/DE/DK/UK/PT/UA + others), of which the May 2025 CAV/crypter takedown is reportedly part.
- [[operation-endgame-phase2]] — May 2025 ransomware-kill-chain wave (Bumblebee, Lactrodectus, Qakbot, etc.); same operational window and partly overlapping agencies, but distinct target set.
