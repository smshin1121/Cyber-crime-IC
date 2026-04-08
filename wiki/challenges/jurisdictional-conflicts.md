---
type: challenge
title: "Jurisdictional Conflicts in Cybercrime"
title_ko: "사이버범죄 관할권 충돌"
aliases: ["jurisdiction conflicts", "concurrent jurisdiction", "positive conflict of jurisdiction"]
challenge_category: "legal"
severity: "critical"
affected_mechanisms:
  - "[[mlat-process]]"
  - "[[europol-jit]]"
affected_crime_types:
  - "[[ransomware-ic]]"
  - "[[bec-ic]]"
  - "[[online-fraud-ic]]"
  - "[[hacking-ic]]"
affected_regions:
  - "Global"
proposed_solutions:
  - "Budapest Convention Art. 22(5) consultation"
  - "Eurojust case coordination"
  - "INTERPOL operational coordination"
  - "Binding jurisdiction allocation mechanism (proposed)"
  - "Forum selection criteria framework"
active_debates:
  - "Whether a binding conflict resolution mechanism is needed"
  - "Priority criteria for jurisdiction selection"
  - "Role of victim location vs. perpetrator location"
  - "Ne bis in idem as a check on concurrent prosecutions"
related_concepts:
  - "[[territoriality-principle]]"
  - "[[dual-criminality]]"
  - "[[ne-bis-in-idem]]"
  - "[[nationality-principle]]"
related_challenges:
  - "[[data-sovereignty]]"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

Jurisdictional conflicts arise when two or more states simultaneously claim the right to investigate and prosecute the same cybercrime. This is not an edge case — it is the *default condition* for transnational cybercrime. The borderless nature of cyber offenses means that the attacker's location, the server infrastructure, the victim, and the evidence are typically distributed across multiple countries, each of which has a legitimate basis for asserting jurisdiction under the [[territoriality-principle]], the [[nationality-principle]], or other jurisdictional doctrines.

Unlike some other areas of international law, there is **no binding mechanism** for resolving jurisdictional conflicts in cybercrime. The Budapest Convention's consultation requirement (Art. 22(5)) is non-binding, and no global framework assigns priority among competing jurisdictions. The result is a combination of duplicated investigations, uncoordinated prosecutions, forum shopping, and — in the worst cases — violations of the [[ne-bis-in-idem]] principle (double jeopardy).

## Nature of the Problem

### Multiple States Claiming Jurisdiction

A typical ransomware attack illustrates the problem:

```
Attacker (Russia) → C2 servers (Netherlands, Germany)
    → Encrypts victim networks (US company, UK subsidiary, Korean contractor)
    → Ransom payment (cryptocurrency, mixers in multiple jurisdictions)
    → Proceeds laundered (UAE, Singapore)
```

In this scenario, *at least* six or seven countries could plausibly claim jurisdiction:
- **Russia:** Nationality of attacker ([[nationality-principle]])
- **Netherlands / Germany:** Location of criminal infrastructure ([[territoriality-principle]])
- **United States:** Location of primary victim (effects doctrine / objective territoriality)
- **United Kingdom:** Location of affected subsidiary
- **South Korea:** Location of affected contractor
- **UAE / Singapore:** Location of money laundering

Each state's claim is legitimate under its own domestic law and general international law. No rule of international law gives priority to any of them.

### Concurrent Proceedings

When multiple states investigate the same conduct independently, several problems emerge:

1. **Duplicated effort.** Scarce law enforcement resources are spent redundantly investigating the same targets.
2. **Evidence conflicts.** One state's seizure of evidence (servers, cryptocurrency) may deprive another state of access to the same evidence.
3. **Witness/defendant conflicts.** An arrested suspect cannot be simultaneously tried in two countries. Extradition to one state means the other loses access.
4. **Inconsistent outcomes.** Different legal systems may reach different conclusions about the same conduct — acquittal in one jurisdiction and conviction in another.

### Ne Bis In Idem Risk

The principle of [[ne-bis-in-idem]] (double jeopardy) prohibits prosecuting a person twice for the same offense. However:
- The principle applies *within* most national legal systems, but its *international* application is uncertain and inconsistent.
- Within the EU, the Charter of Fundamental Rights Art. 50 and the CISA Art. 54 provide transnational ne bis in idem protection.
- Globally, there is no binding prohibition on successive prosecutions in different countries for the same conduct.
- The risk: a person convicted and sentenced in one country could face prosecution for the same cybercrime in another.

### Forum Shopping

In the absence of clear jurisdiction allocation rules, prosecuting authorities may engage in "forum shopping" — selecting the jurisdiction that offers:
- The most favorable legal framework (broadest offenses, heaviest penalties)
- The strongest procedural tools (wiretapping, search powers)
- The most favorable evidence rules
- The best chance of conviction

While this may serve prosecutorial efficiency, it raises due process concerns and can undermine the legitimacy of proceedings.

## Impact on Cooperation

Jurisdictional conflicts paradoxically both **impede** and **motivate** international cooperation:

**Impediment:** States reluctant to cooperate if they believe the other state is "taking" their case. Competing investigations may lead to refusal of MLA requests, extradition disputes, or parallel proceedings that waste resources.

**Motivation:** The recognition that no single state can effectively investigate transnational cybercrime drives states toward joint investigation teams ([[europol-jit]]), coordinated operations (through [[europol-ec3]] or [[interpol-igci]]), and informal police-to-police cooperation.

## Root Causes

### Borderless Nature of Cybercrime

The fundamental root cause is that cybercrime does not respect territorial boundaries. Jurisdictional rules developed for physical-world crime assume a clear connection between a criminal act and a specific territory. This assumption breaks down for conduct that is inherently distributed across networks spanning the globe.

### Multiple Territorial Connections

Each jurisdictional basis — the location of the act, the location of the effect, the nationality of the offender, the nationality of the victim — produces a different answer. All are recognized in international law, and none has priority.

### No Binding Conflict Resolution Mechanism

The Budapest Convention Art. 22(5) is the closest thing to a conflict resolution mechanism:

> "When more than one Party claims jurisdiction over an alleged offence established in accordance with this Convention, the Parties involved shall, where appropriate, consult with a view to determining the most appropriate jurisdiction for prosecution."

However, this provision is:
- **Non-binding** ("shall, where appropriate, consult" — not "shall resolve")
- **Offers no criteria** for what makes a jurisdiction "most appropriate"
- **Has no enforcement mechanism** if states fail to consult or disagree

The UN Cybercrime Convention (2024, not yet in force) Art. 58 contains a similar but slightly strengthened consultation provision. However, it also remains non-binding in outcome.

## Proposed Solutions

### Budapest Convention Art. 22(5) Consultation

The existing consultation requirement, while non-binding, provides a legal basis for dialogue. In practice, consultations happen informally between prosecutors and through Eurojust (within the EU) or INTERPOL (globally). The effectiveness depends entirely on the willingness of the parties.

### Eurojust Case Coordination

Within the EU, [[eurojust|Eurojust]] plays a critical role in resolving jurisdictional conflicts:

- **Council Framework Decision 2009/948/JHA** requires EU member states to consult when parallel proceedings exist, with Eurojust as the default mediator.
- Eurojust maintains a Case Management System that can detect parallel proceedings.
- Eurojust can issue **written opinions** recommending which member state should exercise jurisdiction.
- Eurojust can facilitate **transfer of proceedings** from one member state to another.

**Limitation:** This mechanism applies only within the EU. It has no application to conflicts involving non-EU states.

### INTERPOL Operational Coordination

For non-EU operations, [[interpol-igci|INTERPOL]] provides operational coordination that can help *de facto* resolve jurisdictional conflicts through practical collaboration. When an INTERPOL-coordinated operation designates a lead country, other participating countries implicitly accept a supporting role. However, this operational coordination does not resolve the *legal* question of which state has primary jurisdiction.

### Proposed Binding Mechanisms

Academic and policy proposals for binding jurisdiction allocation include:

1. **Priority criteria framework:** Establishing a hierarchy of jurisdictional bases (e.g., territory of the act > territory of the effect > nationality of offender) to determine which state has the strongest claim.
2. **Forum selection agreement:** A multilateral treaty provision allowing states to agree on jurisdiction allocation in individual cases, with binding effect.
3. **International cybercrime court:** A specialized tribunal with jurisdiction over the most serious transnational cybercrimes (highly aspirational; no active negotiations).
4. **Transfer of proceedings:** Formalizing the ability to transfer a criminal case from one state to another, preserving evidence and avoiding duplication.

## Current State of Debate

The debate centers on whether the current consultative approach is sufficient or whether binding rules are needed:

- **Status quo defenders:** The current flexible approach allows pragmatic case-by-case resolution. Binding rules would be difficult to negotiate and could produce perverse outcomes (e.g., assigning jurisdiction to a state with no capacity or willingness to prosecute).
- **Reform advocates:** The absence of binding rules leads to inefficiency, unfairness, and impunity. States with strong cybercrime capacity (US, UK, EU) dominate case selection, while developing countries are marginalized.
- **Middle ground:** Develop non-binding guidelines or best practices for jurisdiction selection, building on the Budapest Convention Art. 22(5) framework.

## Case Studies

### Operation Cronos (LockBit)

The [[operation-cronos-phase1|Operation Cronos]] series (2024-2025) targeted the LockBit ransomware group across 10+ countries. The question of which state would prosecute the primary defendants required coordination among:
- United States (DOJ/FBI — charging)
- United Kingdom (NCA — infrastructure seizure)
- France, Germany, Netherlands (Europol coordination)
- Multiple other participant countries

The operational coordination through Europol and Eurojust effectively managed the jurisdictional allocation, with the US taking the lead on prosecution and other countries focusing on infrastructure seizure and evidence gathering.

### Phobos/8Base Crackdown

The [[phobos-8base-crackdown|Phobos/8Base operation]] (2025) involved a suspect arrested in South Korea and extradited to the United States. Korea had jurisdiction based on the arrest location (and potentially the nationality principle or effects of the crime), but deferred to the US for prosecution. This pragmatic resolution avoided a jurisdictional conflict but raises the question: what if Korea had wanted to prosecute?

## Comparative Perspectives

### EU Approach

The EU has the most developed framework for resolving intra-EU jurisdictional conflicts:
- Framework Decision 2009/948/JHA (prevention and settlement of conflicts of jurisdiction)
- Eurojust coordination role
- Charter of Fundamental Rights Art. 50 (ne bis in idem)
- European Arrest Warrant system

### US Approach

The US frequently asserts broad extraterritorial jurisdiction and has the most extensive bilateral MLAT network. In practice, the US often takes the prosecution lead in multi-country cybercrime cases due to its capacity, legal tools, and the location of many major service providers on US soil.

### Asia-Pacific Approach

The Asia-Pacific region lacks a regional framework equivalent to the EU's. Jurisdictional conflicts are resolved through bilateral channels, INTERPOL coordination, or ad hoc arrangements. ASEAN's efforts on cybercrime cooperation remain at an early stage.

## Korean Perspective (한국 관점)

### Korean Courts' Approach to Cyber Jurisdiction

Korean courts have generally adopted a broad interpretation of territorial jurisdiction for cybercrime:

- **형법 Art. 2 (속지주의):** Korean courts recognize jurisdiction when either the criminal act or its effect occurs in Korea. For cybercrime, this includes cases where Korean victims are targeted from abroad or where Korean infrastructure is used.
- **대법원 판례:** The Supreme Court has held that jurisdiction exists when a "constituent element" (구성요건적 행위 또는 결과) of the offense occurs in Korean territory, including the location where data is accessed or where the harm materializes.

### Korea's Jurisdictional Conflicts in Practice

Korea has encountered jurisdictional conflicts in several contexts:

1. **Voice phishing (보이스피싱):** Perpetrators operating from China or Southeast Asia targeting Korean victims. Korea has jurisdiction based on the effect (victim location) and often the nationality of victims and sometimes perpetrators. China has jurisdiction based on the location of the act. The [[korea-china-voice-phishing-qingdao|Korea-China Qingdao operation]] demonstrates bilateral cooperation rather than conflict, but the underlying jurisdictional overlap exists.

2. **Overseas Korean cybercriminals:** Korean nationals committing cybercrime from abroad (e.g., Cambodia scam centres, as seen in [[korea-cambodia-scam-repatriation]]). Korea has jurisdiction under the [[nationality-principle]] (형법 Art. 3), while the host country has territorial jurisdiction. Resolution typically involves repatriation rather than prosecution in the host country.

3. **Ransomware extradition:** The Phobos admin arrested in Korea and extradited to the US illustrates Korea deferring prosecution to the requesting state. The [[specialty-principle]] constrains what the US can prosecute after extradition.

### Korea and Forum Selection

Korea, as a relatively recent Budapest Convention party (2024), is still developing its practice on jurisdictional consultation under Art. 22(5). The Korean approach is *likely* to favor:
- Prosecution in the state with the strongest evidentiary base
- Deference to the state leading the operation (especially the US for ransomware cases)
- Assertion of jurisdiction primarily when Korean victims or Korean nationals are directly involved

> [!warning] Legal status check needed
> Verify whether any Korean court decisions have specifically addressed the Budapest Convention Art. 22(5) consultation obligation since Korea's accession in 2024.

## Contradictions & Open Questions

- Is the Budapest Convention's non-binding consultation requirement (Art. 22(5)) sufficient, or does the cybercrime problem demand binding jurisdiction allocation rules?
- How should jurisdiction be allocated when a state with the strongest legal claim (e.g., Russia for Russia-based attackers) is unwilling to prosecute?
- Does the practice of US-led prosecution of global cybercrime cases create a de facto hierarchy of jurisdictions, and is this legitimate?
- How can developing countries assert jurisdiction over cybercrime affecting their citizens when the investigation requires resources and provider cooperation they lack?
- When Korea arrests a cybercrime suspect for extradition, under what circumstances should Korea assert its own jurisdiction instead of deferring to the requesting state?
