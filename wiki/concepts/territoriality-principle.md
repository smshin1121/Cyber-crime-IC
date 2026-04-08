---
type: concept
title: "Territoriality Principle"
title_ko: "영토주의"
aliases: ["territorial jurisdiction", "territorial principle"]
aliases_ko: ["속지주의"]
concept_category: "jurisdictional-doctrine"
domain: "international-law"
definition: "The principle that a state has jurisdiction over crimes committed within its territory. In cybercrime, this raises fundamental challenges because cyber offenses routinely span multiple territories simultaneously."
legal_basis:
  - "Budapest Convention Art. 22(1)(a) — jurisdiction over offenses committed in territory"
  - "General principle of public international law"
  - "형법 (Korean Criminal Act) Art. 2 — Domestic Offenses"
relevance_to_ic: "The foundational basis for jurisdiction in criminal law, but deeply challenged by the borderless nature of cybercrime. Determines which state(s) can investigate/prosecute and whether international cooperation is needed."
related_concepts: ["[[dual-criminality]]", "[[nationality-principle]]", "[[effects-doctrine]]", "[[ne-bis-in-idem]]"]
related_challenges: ["[[jurisdictional-conflicts]]"]
applied_in_cases: []
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Definition

**Plain language:** A country has the right to prosecute crimes that happen on its soil. For cybercrime, "its soil" becomes complicated — the attacker is in Country A, the server is in Country B, the victim is in Country C, and the data passes through Country D.

**Legal definition:** The principle of public international law under which a state exercises criminal jurisdiction over offenses committed within its geographic territory, including offenses where a constituent element (act or effect) occurs within its territory.

## Legal Basis

### Budapest Convention

Art. 22(1) establishes jurisdiction when the offense is committed:
- **(a)** in the territory of the Party (territorial jurisdiction)
- **(b)** on board a ship or aircraft of the Party (flag state)
- **(c)** by a national of the Party (nationality principle, if domestic law recognizes it)
- **(d)** the offense is committed against a national (passive personality, if domestic law recognizes it)

Art. 22(5) requires consultation when multiple parties claim jurisdiction, to determine the "most appropriate" jurisdiction.

### Extensions of Territoriality

Two extensions are particularly relevant to cybercrime:

1. **Subjective territoriality:** Jurisdiction where the criminal *act* was initiated (e.g., where the attacker typed the commands).
2. **Objective territoriality / effects doctrine:** Jurisdiction where the criminal *effect* was felt (e.g., where the victim's system was compromised or data was stolen).

Most states accept both extensions, meaning cybercrime routinely falls under the jurisdiction of multiple states simultaneously.

## Relevance to International Cooperation on Cybercrime

The territoriality principle is both the **foundation** and the **primary challenge** for IC:

**Foundation:** It determines which state has jurisdiction and can legitimately investigate and prosecute. Without territorial (or other) jurisdiction, a state has no legal basis to act.

**Challenge:** A single cybercrime incident typically involves multiple territories:

```
Attacker (Country A) → C2 Server (Country B) → Victim (Country C)
    ↓                      ↓                      ↓
  Evidence in            Evidence in            Evidence in
  Country A              Country B              Country C
  + Cloud provider       + Hosting provider     + Victim logs
    (Country D)            (Country E)
```

Each country may claim jurisdiction. Evidence is scattered across borders. No single country has all the evidence. This makes international cooperation not optional but **structurally necessary** for effective prosecution.

## How It Works in Practice

### Concurrent Jurisdiction

In most cybercrime cases, multiple states have legitimate jurisdiction. This creates both an opportunity (any of them can investigate) and a problem (coordination needed to avoid:
- Duplicated efforts
- Conflicting proceedings
- Double jeopardy / ne bis in idem issues
- Evidence races (one country seizing evidence another needs)

### Jurisdiction Selection

In practice, jurisdiction is often determined by pragmatic factors:
- Where is the **most evidence** accessible?
- Where can the suspect be **arrested**?
- Which country's **laws** provide the best tools for prosecution?
- Which country has the **strongest interest** (most victims, greatest harm)?
- Which country has the **capacity** to handle the case?

The Budapest Convention Art. 22(5) encourages but does not mandate consultation. In practice, coordination often happens through INTERPOL, Europol, or bilateral channels.

## Variations Across Jurisdictions

### Common Law

Common law jurisdictions tend to interpret territorial jurisdiction broadly, recognizing jurisdiction over any offense with a "substantial connection" to the territory. The US in particular has asserted very broad jurisdiction based on minimal territorial contacts (e.g., data transiting through US servers).

### Civil Law

Civil law jurisdictions (including Korea) tend to have more codified jurisdiction rules. Korean Criminal Act Art. 2: "This Act shall apply to both Korean nationals and aliens who commit crimes within the territory of the Republic of Korea." Courts have interpreted "within the territory" to include cases where the *effect* of a cybercrime is felt in Korea.

## Korean Law (한국법)

- **형법 Art. 2 (속지주의):** 대한민국 영역 내에서 죄를 범한 내국인과 외국인에게 적용
- **형법 Art. 3 (속인주의):** 대한민국 영역 외에서 죄를 범한 내국인에게 적용
- **형법 Art. 5, 6:** 특정 범죄에 대한 보편적/보호적 관할

사이버범죄의 경우, 한국 법원은 범죄의 **행위지** 또는 **결과발생지**가 한국인 경우 관할을 인정하는 경향이 있다.

## Debates and Controversies

1. **Unilateral extraterritorial jurisdiction.** Some states (particularly the US) assert jurisdiction based on minimal territorial contacts (e.g., the use of US dollar transactions, data stored on US-based cloud services). This is controversial as it may encroach on other states' sovereignty.

2. **Cloud data and territoriality.** Where is data "located" when it is stored in a cloud data center? The physical location of the server? The location of the data controller? The nationality of the data subject? This question is at the heart of the [[data-sovereignty]] challenge.

3. **Loss of location.** The concept of "data location" may be becoming meaningless as cloud providers use distributed storage, replication, and CDNs. Some scholars argue this requires moving beyond territorial jurisdiction entirely for digital evidence.

## Multi-Language Terminology

| Language | Term | Notes |
|----------|------|-------|
| English | territoriality principle | Also: territorial jurisdiction |
| Korean | 영토주의 / 속지주의 | 속지주의 is the more common legal term |
| French | principe de territorialité | |
| German | Territorialitätsprinzip | |
| Spanish | principio de territorialidad | |
| Japanese | 属地主義 (zokuchishugi) | |

## Contradictions & Open Questions

- How do Korean courts determine territorial jurisdiction when a cybercrime involves distributed cloud infrastructure with no clear single location?
- Is there emerging consensus on whether "data location" should remain relevant for jurisdictional purposes?
- How does the Budapest Convention's Second Additional Protocol affect territorial jurisdiction analysis?

## References

> [!note] This page is based on Budapest Convention Art. 22, Korean Criminal Act (형법) Art. 2-6, and general legal scholarship on jurisdictional principles in international law. No specific collected sources from this wiki were used, as the 20 collected sources cover operational matters rather than jurisdictional doctrine.
