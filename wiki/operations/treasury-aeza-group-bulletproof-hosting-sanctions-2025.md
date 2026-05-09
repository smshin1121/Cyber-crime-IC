---
type: operation
title: "Treasury–UK NCA Sanctions on Aeza Group Russian Bulletproof Hosting (2025)"
aliases:
  - "Aeza Group sanctions"
  - "Aeza Group OFAC designation"
  - "Treasury SB-0185"
  - "US-UK Aeza bulletproof hosting sanctions 2025"
case_id: CYB-2025-115
period: 3
operation_type: takedown
status: completed
enforcement_type:
  - asset-freeze
outcome: success
timeframe:
  announced: 2025-07-01
  start: 2025-07-01
  end: 2025-07-01
  ongoing: false
crime_types:
  - "[[ransomware-ic]]"
  - "[[cybercrime-infrastructure-ic]]"
  - "[[malware-ic]]"
target_entity: "Aeza Group (St. Petersburg, Russia bulletproof hosting provider) plus three affiliated companies — Aeza International Ltd. (UK branch), Aeza Logistic LLC (Russia, 100% Aeza-owned subsidiary), and Cloud Solutions LLC (Russia, 100% Aeza-owned subsidiary) — and four Aeza Group leaders: Arsenii Aleksandrovich Penzev (CEO and 33% owner), Yurii Meruzhanovich Bozoyan (general director and 33% owner), Vladimir Vyacheslavovich Gast (technical director), and Igor Anatolyevich Knyazev (33% owner). The cybercriminal nexus targeted by the action comprises the Meduza infostealer, Lumma infostealer, BianLian ransomware, RedLine infostealer panel hosting, and BlackSprut Russian-language darknet drug marketplace."
lead_agency: "[[us-treasury]]"
coordinating_body: "[[us-treasury]]"
participating_countries:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[russia]]"
participating_agencies:
  - "[[us-treasury]]"
  - "[[uk-nca]]"
legal_basis:
  []
mechanisms_used:
  []
results:
  arrests: 0
  indictments: 0
  servers_seized: 0
  domains_seized: 0
  cryptocurrency_seized: ""
  decryption_keys_recovered: 0
  victims_notified: 0
  other:
    - "4 entities designated by OFAC under E.O. 13694, as further amended by E.O. 14144 and E.O. 14306: Aeza Group, Aeza International Ltd. (UK), Aeza Logistic LLC, Cloud Solutions LLC."
    - "4 individuals designated under the same authority: Arsenii Aleksandrovich Penzev (CEO, 33% owner); Yurii Meruzhanovich Bozoyan (general director, 33% owner); Vladimir Vyacheslavovich Gast (technical director); Igor Anatolyevich Knyazev (33% owner)."
    - "Bilateral U.S.–UK coordination: OFAC designated the Aeza UK front company (Aeza International Ltd.) in coordination with the UK National Crime Agency."
    - "On-record acknowledgment that Penzev and Bozoyan had been arrested by Russian law enforcement in connection with placing the BlackSprut illicit-drug marketplace on Aeza infrastructure (host-state enforcement parallel to U.S. designations)."
edges:
  - source_actor: us-treasury
    target_actor: uk-nca
    cooperation_type: info_sharing
    legal_basis: informal
    direction: undirected
credibility_index: 4.5
source_tier: 1
missing_fields:
  - "specific SDN-list identifiers for designated persons (DOB, passport, residential address)"
  - "specific bilateral MLAT, MOU, or Five Eyes information-sharing instrument cited as the basis for the US-UK coordination"
  - "specific victim-company identities and aggregate financial losses attributable to Aeza-hosted operations"
related_cases:
  []
related_operations:
  - "[[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025]]"
  - "[[treasury-evil-corp-tri-lateral-us-uk-au-sanctions-2024]]"
challenges_encountered:
  []
lessons_learned:
  - "Cross-jurisdictional shell exposure: the Aeza UK branch (Aeza International Ltd.) demonstrates that Russian BPH providers actively use UK corporate registrations to lease IP addresses to cybercriminals. A US-UK bilateral designation pairing was needed to reach the UK shell with simultaneous legal effect in both jurisdictions."
  - "Sanctions-evasion-by-rebranding pattern: Treasury's subsequent November 2025 designation of Hypercore Ltd. (UK) and enabler entities in Serbia and Uzbekistan, framed on the record as a response to Aeza's post-designation rebranding strategy, demonstrates that single-shot BPH sanctions actions are typically insufficient against Russia-headquartered providers and require maintenance-of-pressure follow-on cycles."
  - "Convergence of host-state enforcement and U.S. sanctions: Penzev and Bozoyan's arrests by Russian authorities for the BlackSprut drug-marketplace nexus, occurring in parallel with their OFAC designation, illustrates that BPH actors can simultaneously face host-state criminal liability (for domestically-defined offenses such as drug trafficking) and U.S. sanctions liability (for cyber-enabled misappropriation), even where the host state does not cooperate on the cyber dimension itself."
source_count: 1
sources:
  - "[[2025-07-01_treasury_aeza-group-bulletproof-hosting-cybercriminal-technology-theft-sanctions]]"
created: 2026-05-09
updated: 2026-05-09
---
# Treasury–UK NCA Sanctions on Aeza Group Russian Bulletproof Hosting (2025)

## Summary

On 1 July 2025, the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC), acting in coordination with the United Kingdom's [[uk-nca|National Crime Agency]], designated **Aeza Group** — a St. Petersburg, Russia bulletproof hosting (BPH) services provider — together with three Aeza-affiliated companies (Aeza International Ltd. in the UK, Aeza Logistic LLC, and Cloud Solutions LLC) and four Aeza Group leaders (Arsenii Aleksandrovich Penzev, Yurii Meruzhanovich Bozoyan, Vladimir Vyacheslavovich Gast, and Igor Anatolyevich Knyazev) (Treasury press release SB-0185; reliability: high; credibility: confirmed). All designations were issued under Executive Order 13694, as further amended by E.O. 14144 and E.O. 14306.

The action is described on the record as building on [[us-treasury|OFAC]]'s February 2025 designation of the ZServers BPH provider, establishing a documented Treasury campaign against the Russian-aligned BPH ecosystem in 2025. The action is **almost certainly** the most consequential bilateral U.S.–UK cyber-sanctions designation of a Russian BPH provider in mid-2025 (high confidence, based on the on-the-record framing in the Treasury release and the subsequent November 2025 follow-on action against Aeza's rebranded successor). The cybercriminal customer portfolio identified by Treasury — Meduza and Lumma infostealers, BianLian ransomware, RedLine infostealer panels, and the BlackSprut darknet drug marketplace — places the operation squarely at the intersection of [[ransomware-ic]], [[malware-ic]], and [[cybercrime-infrastructure-ic]] cooperation.

## Background

Bulletproof hosting providers sell access to specialized servers and other computer infrastructure designed to help cybercriminals — ransomware actors, infostealer operators, and darknet marketplace operators — evade detection and resist law enforcement attempts to disrupt their malicious activities. By design, BPH providers offer high resistance to abuse-complaint takedowns, accept anonymous or laundered payment, and concentrate risk in jurisdictions where law-enforcement disruption of the underlying infrastructure is operationally difficult.

[[united-states|U.S.]] Treasury treats BPH providers as a high-priority enabler layer of the cybercrime ecosystem. The Aeza Group designation is the second of three documented 2025 OFAC sanctions actions against the Russian-aligned BPH ecosystem:

1. **February 2025**: OFAC designation of ZServers BPH (referenced on the record in the SB-0185 release; not itself in scope of this operation page).
2. **1 July 2025 (this operation)**: OFAC + UK NCA designation of Aeza Group, three affiliates, and four leaders.
3. **19 November 2025**: trilateral OFAC + Australia DFAT + UK FCDO designation of Media Land LLC and the [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|Aeza sanctions-evasion network (Hypercore Ltd. / Smart Digital Ideas DOO / Datavice MCHJ)]], explicitly framed as a response to Aeza's post-July 2025 rebranding strategy.

This three-action sequence over nine months is **likely** the clearest 2025 illustration of the Treasury "maintenance-of-pressure" approach to Russian BPH (medium-high confidence).

## Participating Parties

**Lead jurisdiction**:
- [[united-states|United States]] — Department of the Treasury, [[us-treasury|Office of Foreign Assets Control (OFAC)]], with FinCEN supplemental advisory linkage on the BlackSprut darknet-drug-trafficking dimension.

**Bilateral coordination partner**:
- [[united-kingdom|United Kingdom]] — [[uk-nca|National Crime Agency (NCA)]]. The release describes OFAC as acting "in coordination with" the NCA specifically for the designation of the Aeza UK front company (Aeza International Ltd.).

**Designated-target jurisdiction**:
- [[russia|Russia]] — host state of Aeza Group, Aeza Logistic LLC, Cloud Solutions LLC, and the four designated individuals. Russia is named on the record as having domestically arrested two of the designated individuals (Penzev and Bozoyan) in connection with the BlackSprut drug-marketplace nexus, but the Treasury release does not characterize Russia as a cooperating partner on the cyber-sanctions action itself.

**Designated entities** (4):
- Aeza Group LLC (Russia) — primary target; St. Petersburg-headquartered BPH provider.
- Aeza International Ltd. (United Kingdom) — UK branch / front company; leases IP addresses to cybercriminals including Meduza infostealer operators.
- Aeza Logistic LLC (Russia) — 100%-owned Aeza Group subsidiary.
- Cloud Solutions LLC (Russia) — 100%-owned Aeza Group subsidiary.

**Designated individuals** (4):
- **Arsenii Aleksandrovich Penzev** — CEO and 33% owner; previously involved in multiple BPH and illicit-drug-marketplace businesses; arrested by Russian law enforcement for placing BlackSprut on Aeza infrastructure.
- **Yurii Meruzhanovich Bozoyan** — general director and 33% owner; managed Aeza Group finances; similarly arrested by Russian law enforcement for the BlackSprut nexus.
- **Vladimir Vyacheslavovich Gast** — technical director; managed Aeza Group's internal network and oversaw the technical placement of BlackSprut on Aeza infrastructure.
- **Igor Anatolyevich Knyazev** — 33% owner; managing the company during the absence of Penzev and Bozoyan.

## Legal Framework

All designations were issued under **Executive Order 13694** ("Blocking the Property of Certain Persons Engaging in Significant Malicious Cyber-Enabled Activities", April 1, 2015), **as further amended by Executive Order 14144** and **Executive Order 14306**.

- **Aeza Group** was designated under the substantive cyber-sanctions prong of E.O. 13694 as amended — being responsible for or having engaged in cyber-enabled activities, originating from or directed by persons located outside the United States, that are reasonably likely to result in or have materially contributed to a threat to U.S. national security, foreign policy, or economic / financial stability, and that have the purpose of or involve causing a misappropriation of funds or economic resources, intellectual property, proprietary information, personal identifiers, or financial information for commercial or competitive advantage or private financial gain.
- **Aeza International Ltd., Aeza Logistic LLC, and Cloud Solutions LLC** were designated under the owned-or-controlled-by-blocked-person prong — for being owned or controlled by, or having acted or purported to act for or on behalf of, Aeza Group.
- **Penzev, Bozoyan, Gast, and Knyazev** were designated under the leader-or-officer prong — for being or having been leaders, officials, senior executives, or members of the board of directors of Aeza Group.

The release does not invoke a bilateral MLAT, the [[budapest-convention|Budapest Convention]], or any specific information-sharing instrument as the legal basis for the U.S.–UK coordination. The coordination is described in unspecified narrative terms ("in coordination with the United Kingdom's National Crime Agency"), which is **likely** to reflect informal bilateral law-enforcement-and-financial-intelligence cooperation rather than a treaty-based mechanism (medium confidence).

> [!note] Translation note
> The Treasury press release uses "bulletproof hosting" / "bulletproof hosting (BPH) services provider" as a translation of the Russian-language criminal-marketplace term. There is no single Korean equivalent in formal use; the closest descriptive rendering in current Korean cybersecurity literature is "방탄 호스팅" (bangtan hosting), used in technical-trade press but not in Korean prosecutor- or police-issued documents.

## Operational Timeline

- **February 2025** — Predicate action: OFAC designates ZServers bulletproof hosting (referenced on the record in SB-0185; not separately catalogued here).
- **1 July 2025** — OFAC issues press release SB-0185; Aeza Group, three affiliates, and four leaders are added to the SDN List with immediate legal effect. UK NCA's coordination role is acknowledged on the record.
- **Post-July 2025 (per subsequent SB-0319 release)** — Aeza leadership initiates a rebranding strategy, routing IP infrastructure through Hypercore Ltd. (UK) and establishing enabler entities in Serbia and Uzbekistan.
- **19 November 2025** — Follow-on trilateral action ([[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|SB-0319]]) designates Hypercore Ltd., Smart Digital Ideas DOO, Datavice MCHJ, and two further Aeza-affiliated individuals (Maksim Makarov, Ilya Zakirov), explicitly framed as a maintenance-of-pressure response to the Aeza rebranding pattern that emerged after the present July 2025 action.

## Results and Impact

- **4 entities and 4 individuals** added to the SDN List with immediate legal effect on 2025-07-01.
- All property and interests in property of the designated persons in the United States or in the possession or control of U.S. persons are blocked. Entities owned 50% or more (individually or in aggregate) by one or more blocked persons are also blocked under OFAC's 50 Percent Rule.
- The designation captures the UK shell layer of the Aeza network (Aeza International Ltd.) within the same legal action as the Russian parent and Russian subsidiaries — **likely** materially increasing transaction-screening exposure for any UK-correspondent banking flows tied to the entity (medium-high confidence).
- The release does not quantify victim losses, decryption-key recoveries, server seizures, or arrests attributable directly to the SB-0185 designation. Penzev and Bozoyan were already in Russian custody on the BlackSprut domestic-drug nexus at the time of the OFAC designation; the U.S. designations are administrative-record, not extradition-driven.

## Cooperation Mechanisms Used

The Treasury release names **bilateral coordination with the UK National Crime Agency** as the operative cooperation mechanism. The release does not invoke a formal mutual legal assistance request or a treaty-based information-sharing instrument; the coordination architecture is **likely** informal bilateral cooperation between [[us-treasury|OFAC]] / Treasury Terrorism and Financial Intelligence and the [[uk-nca|UK NCA]] (medium confidence).

The action also touches a parallel domestic-Russian enforcement track (the Penzev/Bozoyan arrests on the BlackSprut drug nexus). However, no Russian law-enforcement coordination on the cyber-sanctions side is claimed in the press release, and Russia is **highly unlikely** to be a willing cooperation partner on cyber-enabled-misappropriation matters under E.O. 13694 (high confidence).

## Challenges and Friction Points

1. **Host-state non-cooperation on the cyber dimension** — Although Russian law enforcement had arrested two of the same individuals on a domestic drug-trafficking theory, the Russian state does not cooperate with U.S. cyber-sanctions enforcement against Russia-headquartered BPH providers. The U.S. action is therefore confined to administrative blocking of property rather than physical disruption of the underlying infrastructure or extradition.
2. **Cross-jurisdictional shell layering** — The Aeza UK branch (Aeza International Ltd.) demonstrates that Russian BPH providers actively use third-country corporate registrations (UK, and subsequently — per the Nov 2025 follow-on — Serbia and Uzbekistan) to lease IP addresses and to position payment flows outside Russian jurisdiction. This requires multi-jurisdiction sanctions coordination to capture.
3. **Sanctions evasion via rebranding** — The most significant challenge documented in the broader operation arc is the Aeza-to-Hypercore rebranding pattern that emerged immediately after this July 2025 designation. Per the subsequent SB-0319 release (19 November 2025), Aeza leadership initiated a rebranding strategy "focusing on removing any connections between Aeza and their new technical infrastructure" — most notably by routing IP infrastructure through Hypercore Ltd., a UK-registered shell, and by establishing enabler entities in Serbia (Smart Digital Ideas DOO) and Uzbekistan (Datavice MCHJ). The 19 November 2025 follow-on trilateral action was needed to maintain pressure on the same target ecosystem under the rebranded structure. This is **almost certainly** the canonical 2025 case study of post-designation BPH rebranding (high confidence).

## Lessons Learned

1. **Single-shot OFAC designations are typically insufficient against Russia-headquartered BPH providers** — the Aeza → Hypercore rebranding cycle, completed within four months of the original designation, demonstrates that BPH actors with Russia-state risk tolerance can quickly relocate corporate identity across cooperative third-country jurisdictions. Maintenance-of-pressure follow-on designations are required.
2. **Bilateral U.S.–UK pairing is operationally significant for capturing UK shell layers** — designating the Aeza UK branch (Aeza International Ltd.) in coordination with the UK NCA on the same date as the parent gives the action immediate legal effect across both jurisdictions and forecloses a window during which the UK shell could otherwise be quietly liquidated or transferred.
3. **Treasury's BPH campaign uses a portfolio approach** — the documented February 2025 (ZServers) → July 2025 (Aeza) → November 2025 (Media Land + Hypercore/Aeza-network) sequence is **likely** a deliberate, sustained campaign against the Russian BPH ecosystem rather than three independent ad-hoc actions (medium-high confidence, based on the explicit cross-references in successive press releases).

## Follow-Up Actions

- **19 November 2025**: [[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025|Treasury SB-0319 trilateral action]] — designates Hypercore Ltd. (UK rebrand of Aeza Group), Smart Digital Ideas DOO (Serbia enabler), Datavice MCHJ (Uzbekistan enabler), and two further Aeza-affiliated individuals (Maksim Makarov, Ilya Zakirov). This follow-on is the operational consequence of the Aeza rebranding pattern that emerged AFTER the present July 2025 designation, and it confirms — as a matter of on-the-record Treasury narrative — that the Aeza Group leadership pivoted to Hypercore as the rebranded successor entity.

> [!note] Naming continuity
> The "Aeza Group → Hypercore Ltd." rebranding linkage is established not in the present 1 July 2025 release (where Hypercore is not named) but in the subsequent 19 November 2025 release (SB-0319), which retroactively documents the rebrand. The SB-0185 action should therefore be read as the **trigger** of, not the **target** of, the Aeza-to-Hypercore pivot.

## Korean Involvement (한국의 참여)

The 1 July 2025 Treasury press release does not name [[south-korea|South Korea]], any Korean agency, or any Korean victim entity. The release's victim characterization is generic ("U.S. defense industrial base and technology companies, among other victims globally"), and the bilateral coordination is exclusively U.S.–UK.

There is **no on-the-record Korean involvement** in this operation (high confidence, based on a complete reading of the press-release text). Indirect Korean exposure is **likely** present in two narrow forms:

1. **Infostealer victim exposure** — Lumma and Meduza infostealer operations have a globally-distributed victim pool, and Korean enterprises and government users are **likely** to be among the affected populations of any large-scale infostealer campaign (medium confidence; the press release does not enumerate Korean victims).
2. **SDN-list compliance obligation** — Korean financial institutions and Korean-headquartered multinationals with U.S.-nexus operations or USD correspondent banking relationships are required, as a matter of U.S. secondary-sanctions exposure, to screen counterparties against the post-1-July-2025 SDN List, which now includes the eight Aeza designations. This is a routine compliance consequence rather than an active cooperation dimension.

No Korean participation in the underlying U.S.–UK coordination, and no direct Korean operational role, is documented in this source.

## Contradictions & Open Questions

1. **Specific information-sharing instrument unclear** — The Treasury release describes the U.S.–UK coordination only as "in coordination with the United Kingdom's National Crime Agency" without identifying a specific MLAT, MOU, or Five Eyes channel. Is the coordination architecture better characterized as informal financial-intelligence cooperation or as a formal MLA channel? The release does not say.
2. **Russian domestic prosecution status** — Treasury notes Penzev and Bozoyan were arrested by Russian law enforcement on the BlackSprut nexus, but does not specify charging status, anticipated trial timing, or whether the BlackSprut-related Russian case will be pursued to conviction or quietly dropped. This is a meaningful open question for assessing whether the U.S. designations will ever be operationally complemented by host-state prosecutorial action.
3. **Victim quantification** — The release does not quantify the financial impact of Aeza-hosted ransomware (BianLian) and infostealer (Meduza, Lumma, RedLine) operations on U.S. victims. Aggregate-loss attribution to a BPH provider is methodologically difficult, but the absence of any victim-count or loss figure leaves the action's announced rationale ("disruptive ransomware attacks, steal U.S. technology, sell black-market drugs") empirically unsupported in this source.
4. **Effective disruption assessment** — Whether the SDN-listing of Aeza Group materially reduced the operational availability of Aeza-hosted infrastructure to its cybercriminal customers between 1 July 2025 and the 19 November 2025 follow-on action is not addressed in this source. The fact that Treasury found it necessary to designate Hypercore Ltd. only four months later **likely** suggests that the underlying technical infrastructure migrated to rebranded hosts rather than being effectively dismantled (medium confidence).
