---
type: concept
title: "Nationality Principle (Active Personality)"
title_ko: "속인주의"
aliases: ["active personality principle", "nationality jurisdiction", "active nationality principle"]
aliases_ko: ["적극적 속인주의", "국적주의"]
concept_category: "jurisdictional-doctrine"
domain: "international-law"
definition: "The principle that a state has jurisdiction over criminal offenses committed by its nationals regardless of where the offense was committed. It extends a state's criminal law to the conduct of its citizens abroad."
legal_basis:
  - "Budapest Convention Art. 22(1)(d) — jurisdiction when offense committed by national"
  - "General principle of public international law"
  - "형법 (Korean Criminal Act) Art. 3 — 속인주의 (Offenses by Nationals Abroad)"
  - "UN Cybercrime Convention (2024) Art. 56(2)(b) — nationality jurisdiction"
relevance_to_ic: "Provides jurisdiction over nationals committing cybercrime abroad, particularly relevant for Korean nationals in overseas scam centres. Creates the legal basis for requesting repatriation, extradition, and prosecution of nationals who operate from jurisdictions with limited enforcement capacity."
related_concepts:
  - "[[territoriality-principle]]"
  - "[[dual-criminality]]"
  - "[[ne-bis-in-idem]]"
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

**Plain language:** A country can prosecute its own citizens for crimes they commit in other countries. If a Korean national operates a voice phishing call center in Cambodia, Korea has the right to prosecute that person under Korean law — even though the crime happened entirely on Cambodian soil.

**Legal definition:** The principle of criminal jurisdiction (also known as "active personality" or "active nationality") under which a state asserts jurisdiction over offenses committed by its nationals outside its territory. It is based on the bond of nationality between the state and the offender, rather than the location of the criminal conduct.

## Legal Basis

### In International Law

The nationality principle is universally recognized as a valid basis for criminal jurisdiction under customary international law (ICJ, *Nottebohm Case*, 1955, on the genuine link requirement for nationality). Its application varies:

- **Civil law systems:** Broadly apply the nationality principle, often as a matter of constitutional or statutory law. Most civil law countries assert jurisdiction over *all* crimes committed by nationals abroad.
- **Common law systems:** Traditionally more restrained, asserting nationality jurisdiction only for specific categories of serious offenses (e.g., murder, terrorism, sexual offenses against children, treason).

### Budapest Convention

Art. 22(1) provides that each Party shall establish jurisdiction over offenses when:
- **(d)** the offense is committed by one of its nationals, "if the offence is punishable under criminal law where it was committed or if the offence is committed outside the territorial jurisdiction of any State."

This formulation links nationality jurisdiction to a modified [[dual-criminality]] requirement or to cases where the offense occurs outside any state's territory (e.g., on the high seas or in cyberspace — though the latter interpretation is debated).

Art. 22(3) allows states to make reservations not to apply, or to apply only in specific conditions, the nationality jurisdiction basis.

### UN Cybercrime Convention (2024)

Art. 56(2)(b) similarly provides for nationality-based jurisdiction as an optional basis that parties may establish.

## Relevance to International Cooperation on Cybercrime

### Cybercrime Abroad by Nationals

The nationality principle is increasingly relevant as cybercriminals operate from countries that offer:
- Weak or absent cybercrime enforcement
- Safe havens for criminal operations
- Low cost of living and operational costs
- Proximity to victims or money laundering networks

Examples:
- **Korean nationals in Southeast Asian scam centres:** The [[korea-cambodia-scam-repatriation]] operation (2025) revealed approximately 1,000 Korean nationals working in Cambodian scam centres, many conducting [[voice-phishing-ic|voice phishing]] targeting Korean victims. Korea's jurisdiction under 형법 Art. 3 provides the legal basis for prosecution upon repatriation.
- **Nigerian nationals conducting BEC from multiple countries:** Nigeria can assert jurisdiction over its nationals involved in [[bec-ic|BEC]] operations regardless of their location.
- **Russian nationals operating ransomware from various countries:** Russia's failure to exercise nationality jurisdiction over its cyber criminals is a major obstacle to global [[ransomware-ic]] enforcement.

### Interaction with Other Jurisdictional Bases

The nationality principle creates a **concurrent jurisdiction** with the [[territoriality-principle]] of the state where the crime occurs:

```
Korean national → operates scam centre in Cambodia → targets Korean victims

Korea has jurisdiction based on:
  - Nationality principle (형법 Art. 3) — offender is Korean
  - Territoriality/effects doctrine — victims are in Korea

Cambodia has jurisdiction based on:
  - Territoriality principle — criminal conduct occurs on Cambodian soil

Both have legitimate jurisdiction → potential [[jurisdictional-conflicts]]
```

### The "Haven" Problem

The nationality principle is sometimes the *only* available basis for jurisdiction when:
- The territorial state (where the crime occurs) lacks the capacity or willingness to prosecute
- The victim state has no extradition treaty with the territorial state
- The suspect cannot be located in a cooperative jurisdiction

In these cases, repatriation of the national (through diplomatic channels or consular assistance) combined with prosecution under nationality jurisdiction may be the only viable path to justice.

## How It Works in Practice

### Prosecution Process

1. **Detection:** Home state learns that its national is committing crimes abroad (through intelligence, victim reports, INTERPOL notices, or foreign LEA notifications)
2. **Evidence gathering:** Home state requests evidence from the territorial state through [[mlat-process|MLAT]], police-to-police channels, or international organizations
3. **Return of the national:** Through:
   - **Voluntary return** — the national returns on their own
   - **Repatriation** — diplomatic arrangements (not formal extradition)
   - **Extradition from a third state** — if the national travels to a cooperative jurisdiction
   - **Deportation** — the territorial state deports the foreign national
4. **Prosecution at home:** Under domestic criminal law, the home state prosecutes for the offense committed abroad

### Dual Criminality Limitation

Many national implementations of the nationality principle require [[dual-criminality]] — the act must also be criminal where it was committed. This limitation exists because:
- It would be unfair to punish a national for conduct that is legal where they are
- It prevents overreach by the home state's criminal law
- It is required by some treaty frameworks (Budapest Convention Art. 22(1)(d))

However, some states assert nationality jurisdiction even without dual criminality for the most serious offenses (e.g., child sexual exploitation, terrorism, genocide).

## Variations Across Jurisdictions

### Civil Law (Broad Application)

- **France (Code pénal Art. 113-6):** French criminal law applies to any felony committed by a French national outside France. For misdemeanors, dual criminality is required.
- **Germany (StGB § 7):** German criminal law applies to offenses committed abroad by German nationals, subject to dual criminality.
- **South Korea (형법 Art. 3):** Korean criminal law applies to all offenses committed by Korean nationals outside Korean territory (no dual criminality limitation in the statutory text).
- **Japan (刑法 Art. 3):** Japanese criminal law applies to Japanese nationals who commit certain enumerated offenses abroad.

### Common Law (Selective Application)

- **United States:** The US generally does not assert nationality jurisdiction as a general principle, but does so for specific statutory offenses (e.g., 18 USC § 2423 — sex tourism; 18 USC § 2332 — killing of US nationals abroad; FCPA — foreign bribery).
- **United Kingdom:** Similar selective approach — nationality jurisdiction for murder, manslaughter, and specific statutory offenses committed abroad.
- **Australia:** Criminal Code Act 1995 Part 2.7 — nationality jurisdiction for specific offenses (child exploitation, terrorism, bribery).

## Key Case Law

*To be populated as relevant cases are ingested.*

## Debates and Controversies

1. **Selective enforcement.** When states *can* but *choose not to* exercise nationality jurisdiction over their cybercriminal nationals — notably Russia — the principle becomes a shield rather than a sword. Russia's assertion of nationality jurisdiction without actual prosecution creates a safe haven effect.

2. **Dual criminality gap for cybercrime.** If the territorial state has no cybercrime law, nationality jurisdiction with a dual criminality requirement fails. This gap is narrowing as more countries enact cybercrime legislation, but remains relevant in some developing regions.

3. **Extraterritorial evidence challenges.** Exercising nationality jurisdiction requires *evidence* of what the national did abroad. If the territorial state is uncooperative or lacks digital forensic capacity, gathering evidence for prosecution at home is extremely difficult.

4. **Repatriation vs. extradition.** Many states refuse to extradite their own nationals (e.g., Germany, France, many civil law countries). Instead, they exercise nationality jurisdiction and prosecute at home. This can result in more lenient outcomes if the home state has lighter penalties or less expertise in the specific type of cybercrime.

5. **Forced labor/trafficking context.** Some nationals abroad are not voluntary cybercriminals but victims of trafficking forced into scam operations (as documented in the Cambodia scam centre context). The nationality principle must account for this — prosecution should target organizers, not trafficked persons.

## Korean Law (한국법)

### 형법 제3조 (속인주의)

**형법 Art. 3:** "본법은 대한민국 영역 외에서 죄를 범한 내국인에게 적용한다."
(This Act shall apply to Korean nationals who commit offenses outside the territory of the Republic of Korea.)

This is one of the broadest nationality jurisdiction provisions in the world:
- Applies to **all** criminal offenses, not just enumerated ones
- **No dual criminality requirement** in the statutory text
- Applies to all Korean nationals regardless of whether they also hold another nationality

### Practical Application to Cybercrime

**Voice phishing / scam centres:**
- Korean nationals operating voice phishing call centers in China, Cambodia, Philippines, and other countries are subject to Korean criminal law under Art. 3
- The [[korea-cambodia-scam-repatriation]] operation (2025) resulted in 107+ Korean nationals being repatriated from Cambodia, with prosecution in Korea under this principle
- HAECHI series operations have identified Korean nationals involved in transnational fraud operations

**Challenges in Korean practice:**
1. **Evidence gathering:** Korean police need evidence from the territorial state (e.g., call center records, financial records from Cambodia/China). This requires international cooperation from countries with varying levels of capacity and willingness.
2. **Repatriation logistics:** Returning nationals from states without formal extradition treaties requires diplomatic coordination (as demonstrated in the Cambodia operation).
3. **Trafficking victims vs. criminals:** Many Koreans in Cambodian scam centres were lured by false job offers. Korean law enforcement must distinguish between willing participants and trafficking victims.
4. **Sentencing parity:** Korean sentences for cybercrime may be lighter than those in victim countries (especially the US), raising questions about whether nationality jurisdiction produces adequate deterrence.

### Related Korean Provisions

- **형법 Art. 2 (속지주의):** Territorial jurisdiction — see [[territoriality-principle]]
- **형법 Art. 5 (외국인의 국외범):** Universal jurisdiction for certain offenses by foreigners abroad
- **형법 Art. 6 (대한민국과 대한민국 국민에 대한 국외범):** Protective principle — jurisdiction over foreigners' offenses abroad that target Korea or Korean nationals

## Multi-Language Terminology

| Language | Term | Notes |
|----------|------|-------|
| English | nationality principle | Also: active personality principle |
| Korean | 속인주의 (sogin-juui) | Also: 적극적 속인주의, 국적주의 |
| French | compétence personnelle active | Also: principe de personnalité active |
| German | aktives Personalitätsprinzip | Also: Täterprinzip |
| Spanish | principio de personalidad activa | Also: principio de nacionalidad |
| Japanese | 属人主義 (zokujinshugi) | Also: 積極的属人主義 |

> [!note] Translation note
> "속인주의" (sogin-juui) literally means "principle of personal affiliation" and is the standard Korean legal term. "적극적 속인주의" (active personality principle) distinguishes it from "소극적 속인주의" (passive personality principle), which covers jurisdiction based on the *victim's* nationality rather than the *offender's* nationality.

## Contradictions & Open Questions

- Should the nationality principle carry a dual criminality requirement for cybercrime, or should Korea's broad Art. 3 approach (no such requirement) be the model?
- When Russia refuses to extradite its nationals and also refuses to prosecute them for ransomware, is there a basis under international law for other states to intervene?
- How should Korea handle the repatriation-prosecution pipeline for nationals in Southeast Asian scam centres who are both perpetrators and victims of trafficking?
- Does the practical difficulty of evidence gathering abroad undermine the effectiveness of nationality jurisdiction, making it a "paper jurisdiction" in many cases?
- Should Korea negotiate specific agreements with Cambodia, Vietnam, and Philippines for evidence sharing in nationality-based cybercrime prosecutions?
