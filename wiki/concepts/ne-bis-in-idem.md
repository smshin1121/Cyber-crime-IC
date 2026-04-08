---
type: concept
title: "Ne Bis In Idem (Double Jeopardy)"
title_ko: "일사부재리"
aliases: ["double jeopardy", "non bis in idem", "ne bis in idem principle"]
aliases_ko: ["이중처벌금지", "일사부재리 원칙"]
concept_category: "human-rights-safeguard"
domain: "criminal-law"
definition: "The principle that no person shall be tried or punished twice for the same offense. In the context of international cooperation on cybercrime, it addresses whether a person prosecuted in one state can be prosecuted again in another state for the same conduct."
legal_basis:
  - "ICCPR Art. 14(7) — limited to within same state"
  - "EU Charter of Fundamental Rights Art. 50 — transnational within EU"
  - "Convention Implementing the Schengen Agreement (CISA) Art. 54 — transnational within Schengen"
  - "Protocol No. 7 to the ECHR Art. 4 — within same state"
  - "헌법 (Korean Constitution) Art. 13(1) — 일사부재리"
  - "형사소송법 (Korean Criminal Procedure Act) Art. 326(1) — 확정판결이 있는 때"
relevance_to_ic: "When multiple countries have jurisdiction over the same cybercrime (the default for transnational cyber offenses), ne bis in idem determines whether a defendant convicted or acquitted in one state can face prosecution in another. The absence of a globally binding transnational ne bis in idem rule means this protection is incomplete."
related_concepts:
  - "[[territoriality-principle]]"
  - "[[dual-criminality]]"
  - "[[specialty-principle]]"
related_challenges:
  - "[[jurisdictional-conflicts]]"
applied_in_cases: []
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Definition

**Plain language:** Once a person has been tried and either convicted or acquitted of a crime, they cannot be tried again for the same crime. In international cybercrime cooperation, the question is: does a conviction or acquittal in Country A prevent Country B from prosecuting the same person for the same conduct?

**Legal definition:** The procedural safeguard prohibiting the repeated prosecution or punishment of a natural person for the same offense (idem) after a final decision (bis) by a competent judicial authority. The scope of the principle — whether it applies only within a single state or across states — is one of the most contested questions in international criminal law.

## Legal Basis

### International Instruments

| Instrument | Article | Scope | Binding? |
|-----------|---------|-------|----------|
| ICCPR | Art. 14(7) | Within same state only | Yes (treaty parties) |
| ECHR Protocol 7 | Art. 4 | Within same state only | Yes (ratifying parties) |
| EU Charter of Fundamental Rights | Art. 50 | Transnational (within EU) | Yes (EU member states) |
| CISA (Schengen) | Art. 54 | Transnational (within Schengen) | Yes (Schengen states) |
| Budapest Convention | No explicit provision | - | - |
| UN Cybercrime Convention (2024) | No explicit provision | - | - |

**Critical gap:** Neither the Budapest Convention nor the UN Cybercrime Convention contains an explicit ne bis in idem provision addressing transnational application. The Budapest Convention's Art. 22(5) (jurisdictional consultation) is meant to *prevent* concurrent proceedings, but provides no remedy if they occur.

### Domestic Law

Most national legal systems recognize ne bis in idem domestically. The question is whether they extend it to foreign judgments:

- **United States:** The "dual sovereignty" doctrine means federal and state prosecutions for the same conduct are permitted. Foreign prosecutions do *not* bar US prosecution (*Gamble v. United States*, 2019).
- **EU Member States:** Bound by CISA Art. 54 and the Charter Art. 50 to recognize other EU states' final judgments.
- **South Korea:** 헌법 Art. 13(1) protects against double jeopardy domestically. The effect of foreign judgments is addressed by 형법 Art. 7.

## Relevance to International Cooperation on Cybercrime

Ne bis in idem is directly relevant to the [[jurisdictional-conflicts]] challenge. When multiple countries have jurisdiction over the same cybercrime (which is the norm, not the exception), the following risks arise:

1. **Successive prosecutions:** Country A convicts and sentences a cybercriminal. Country B, whose victims were also affected, then initiates its own prosecution for the same conduct. The defendant faces a second trial and potentially cumulative punishment.

2. **Acquittal followed by prosecution:** Country A acquits a defendant (insufficient evidence, legal deficiency). Country B, with stronger evidence or broader criminal laws, then prosecutes the same person. The acquittal provides no protection.

3. **Extradition complications:** A person extradited from Country C to Country A may, after serving the sentence, face an extradition request from Country B for the same conduct. The [[specialty-principle]] limits prosecution in Country A, but provides no protection against Country B.

4. **Chilling effect on cooperation:** If defendants know they may face multiple prosecutions, they may resist extradition more vigorously, and states may be reluctant to transfer proceedings or share evidence if doing so enables a second prosecution elsewhere.

## How It Works in Practice

### The "Idem" Question: What Constitutes the "Same Offense"?

The most contested aspect is defining "same offense":

- **Same legal classification (idem factum juridicum):** The offense must be the same crime in both jurisdictions. Under this test, Country A's prosecution for "computer fraud" does not bar Country B's prosecution for "money laundering" arising from the same conduct.
- **Same facts (idem factum):** The test is whether the material facts are substantially the same, regardless of legal classification. This is the approach adopted by the CJEU for EU ne bis in idem (*Van Esbroeck*, 2006).

The idem factum approach is more protective of defendants but harder to apply in cybercrime cases where a single course of conduct may simultaneously constitute multiple distinct offenses under different legal systems.

### The "Bis" Question: What Constitutes a Final Decision?

A ne bis in idem bar typically requires a *final* decision — a judgment that can no longer be appealed. Questions arise about:
- Plea agreements — are they "final decisions"?
- Settlements or deferred prosecution agreements
- Prosecutorial decisions not to prosecute (classement sans suite)
- Administrative penalties (e.g., regulatory fines for data breaches)

### Enforcement Conditions

Within the EU (CISA Art. 54), the ne bis in idem bar applies only if the penalty "has been enforced, is actually in the process of being enforced, or can no longer be enforced" under the sentencing state's laws. This prevents a person from obtaining impunity by being convicted abroad but never actually serving the sentence.

## Variations Across Jurisdictions

### Common Law

Common law jurisdictions generally recognize double jeopardy within the same jurisdiction but do not extend it to foreign judgments. The US "dual sovereignty" doctrine (*Gamble v. United States*, 2019) is the most prominent example — even two US sovereigns (federal and state) can prosecute the same conduct without violating double jeopardy.

### Civil Law

Civil law jurisdictions vary significantly:
- **Germany (StGB § 51):** Foreign judgments may be credited against domestic sentences (Anrechnungsprinzip), but do not create a procedural bar.
- **France:** The Cour de cassation has recognized a limited ne bis in idem effect of foreign judgments in some contexts.
- **Netherlands:** CISA Art. 54 is directly applicable; Dutch courts have broadly interpreted the transnational ne bis in idem principle.

## Key Case Law

### CJEU — Van Esbroeck (C-436/04, 2006)

The Court of Justice held that "same acts" under CISA Art. 54 means the *material facts* are the same, not the legal classification. This is the leading case on the idem factum approach within the EU.

### CJEU — Mantello (C-261/09, 2010)

Clarified that ne bis in idem under CISA Art. 54 requires a "final" decision, and courts in the executing member state must recognize the finality assessment of the issuing member state.

### US — Gamble v. United States (2019)

The US Supreme Court reaffirmed the "separate sovereigns" doctrine, holding that successive federal and state prosecutions for the same conduct do not violate the Fifth Amendment's double jeopardy clause. By extension, foreign sovereign prosecutions do not bar US prosecution.

## Debates and Controversies

1. **Global ne bis in idem for cybercrime?** Some scholars argue that a binding transnational ne bis in idem rule is necessary for cybercrime, given the routine concurrent jurisdiction of multiple states. Others counter that this would create impunity risks (e.g., sham trials in non-cooperative states creating a bar to genuine prosecution elsewhere).

2. **"Enforcement condition" fairness.** The CISA Art. 54 enforcement condition means that a conviction in one EU state only bars re-prosecution if the sentence is actually enforced. This raises concerns about conditional ne bis in idem protection.

3. **Cybercrime and multiple victims.** A ransomware attack affecting victims in 50 countries — does a prosecution in one country for the domestic victims bar prosecution in another country for different victims of the same attack? Under the idem factum approach, likely yes; under the idem juridicum approach, potentially not.

4. **Ne bis in idem and plea bargains.** If a cybercriminal pleads guilty to reduced charges in one jurisdiction (common in US practice), can another jurisdiction prosecute the same conduct under the more serious charges that were dropped in the plea?

## Korean Law (한국법)

### Constitutional Protection

**헌법 제13조 제1항:** "모든 국민은 동일한 범죄에 대하여 거듭 처벌받지 아니한다."
(All citizens shall not be punished repeatedly for the same crime.)

This is an absolute constitutional guarantee within the Korean legal system.

### Criminal Procedure Act

**형사소송법 제326조 제1호:** A judgment of not guilty (면소) must be entered when a final judgment (확정판결) already exists for the same offense. This codifies the domestic ne bis in idem bar.

### Effect of Foreign Judgments

**형법 제7조:** "범죄에 의하여 외국에서 형의 전부 또는 일부의 집행을 받은 자에 대하여는 형을 감경 또는 면제할 수 있다."
(For a person who has received enforcement of all or part of a sentence abroad for a crime, the sentence may be reduced or remitted.)

This provision does **not** create a procedural bar to prosecution in Korea. It only allows for *reduction or remission* of the Korean sentence, taking the foreign punishment into account. Korea can still prosecute a person already convicted abroad for the same conduct — the foreign sentence is a *mitigating factor*, not a bar.

### Implications for Cybercrime IC

- If a Korean national is convicted abroad for a cybercrime (e.g., ransomware operation), Korea can still prosecute under 형법 Art. 3 ([[nationality-principle]]) when the person returns to Korea.
- If a foreign national is convicted in their home country for a cybercrime that also affected Korean victims, Korea can technically pursue a separate prosecution, though in practice this is unlikely.
- The gap between Korean constitutional protection (absolute domestic ne bis in idem) and the limited recognition of foreign judgments (형법 Art. 7, mitigation only) is a notable feature of the Korean system.

> [!note] Translation note
> "일사부재리" (ilsa-bujaeri) literally translates as "one matter not to be retried" and is used in Korean law specifically for the domestic constitutional guarantee. "이중처벌금지" (ijung-cheobolgeunji) — "prohibition of double punishment" — is used more broadly, including in discussions of the international dimension.

## Multi-Language Terminology

| Language | Term | Notes |
|----------|------|-------|
| Latin | ne bis in idem | Literally: "not twice in the same [matter]" |
| English | double jeopardy | US constitutional term; broader: ne bis in idem |
| Korean | 일사부재리 (ilsa-bujaeri) | Constitutional term (헌법 Art. 13) |
| Korean | 이중처벌금지 | Broader term including international dimension |
| French | non bis in idem | Also: autorité de la chose jugée |
| German | Doppelbestrafungsverbot | Literally: "prohibition of double punishment" |
| Spanish | non bis in idem | |
| Japanese | 二重の危険 (nijū no kiken) | Also: 一事不再理 (ichiji fusairi) |

## Contradictions & Open Questions

- Should a binding transnational ne bis in idem rule be established for cybercrime, or does this create unacceptable impunity risks?
- How should the "same offense" be defined for cybercrime that produces victims and effects across dozens of countries simultaneously?
- Does Korea's 형법 Art. 7 (mitigation only, not bar) adequately protect the rights of persons already convicted abroad, or should Korea adopt a stronger transnational ne bis in idem protection?
- How does the absence of ne bis in idem provisions in both the Budapest Convention and the UN Cybercrime Convention affect their legitimacy as human rights-compliant frameworks?
- Can pre-trial coordination (through Eurojust or INTERPOL) effectively prevent concurrent prosecutions, making a formal ne bis in idem rule unnecessary?
