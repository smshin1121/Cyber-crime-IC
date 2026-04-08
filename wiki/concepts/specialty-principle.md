---
type: concept
title: "Specialty Principle (Rule of Specialty)"
title_ko: "특정성의 원칙"
aliases: ["rule of specialty", "principle of speciality", "doctrine of specialty"]
aliases_ko: ["특정주의", "특별성의 원칙"]
concept_category: "legal-principle"
domain: "international-law"
definition: "The principle that a person extradited from one state to another may only be tried or punished for the specific offense(s) for which extradition was granted, unless the surrendering state consents to prosecution for additional offenses."
legal_basis:
  - "Budapest Convention Art. 24(1)(c) — incorporation of existing extradition treaties"
  - "European Convention on Extradition (1957) Art. 14 — rule of speciality"
  - "범죄인 인도법 (Korean Extradition Act) Art. 15 — 특정성의 원칙"
  - "US-Korea Extradition Treaty Art. 15 — rule of speciality"
  - "Model Treaty on Extradition (UN, 1990) Art. 14"
relevance_to_ic: "Prevents prosecution scope creep after extradition. Ensures the surrendering state's sovereignty is respected and the extradited person's rights are protected. Particularly relevant in cybercrime cases where a single actor may have committed multiple offenses across jurisdictions."
related_concepts:
  - "[[dual-criminality]]"
  - "[[ne-bis-in-idem]]"
  - "[[territoriality-principle]]"
  - "[[nationality-principle]]"
related_challenges:
  - "[[jurisdictional-conflicts]]"
applied_in_cases: []
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Definition

**Plain language:** If Country A extradites a suspect to Country B to be tried for ransomware, Country B cannot then also prosecute the suspect for unrelated hacking or money laundering unless Country A agrees. The extradited person can only be tried for the specific crime that was the basis for the extradition.

**Legal definition:** The rule of international extradition law that restricts the requesting state from prosecuting, sentencing, or detaining an extradited person for any offense committed prior to surrender other than the offense for which extradition was granted, unless the surrendering state provides its consent or the extradited person has had the opportunity to leave the requesting state and has not done so.

## Legal Basis

### Treaty Sources

The specialty principle is codified in virtually all extradition treaties and conventions:

**European Convention on Extradition (1957) Art. 14:**
> "A person who has been extradited shall not be prosecuted, sentenced or detained with a view to the carrying out of a sentence or detention order for any offence committed prior to his surrender other than that for which he was extradited..."

**Budapest Convention Art. 24:** The Budapest Convention does not contain its own specialty provision but references extradition under existing bilateral/multilateral treaties and domestic law. Art. 24(1) provides that the existing extradition framework between the parties applies, including any specialty protections therein.

**Exceptions (typical in most treaties):**
1. The surrendering state consents to prosecution for additional offenses
2. The extradited person, having had the opportunity to leave, voluntarily remains in the requesting state for more than a specified period (usually 30-45 days)
3. The extradited person voluntarily returns to the requesting state after leaving

### Rationale

The specialty principle serves three functions:
1. **Sovereignty protection:** The surrendering state's decision to extradite was based on a specific offense. Allowing prosecution for other offenses would circumvent the surrendering state's extradition decision-making process.
2. **Individual rights protection:** The extradited person agreed to (or was subjected to) transfer for a specific charge. Expanding the prosecution undermines legal certainty and due process.
3. **Treaty compliance:** Extradition depends on trust between states. If requesting states routinely expanded charges after extradition, surrendering states would become reluctant to grant future requests.

## Relevance to International Cooperation on Cybercrime

### Prosecution Scope Creep

Cybercriminals often engage in *multiple* types of criminal conduct:
- A ransomware operator may also be involved in money laundering, wire fraud, identity theft, conspiracy, and computer intrusion
- A BEC syndicate member may be involved in bank fraud, aggravated identity theft, and money mule recruitment
- A hacker may have conducted espionage, data theft, and sabotage across multiple victim organizations

When extradition is sought for one offense (e.g., computer fraud), prosecutors may discover evidence of additional offenses after the suspect is surrendered. The specialty principle prevents the requesting state from simply adding charges without the surrendering state's consent.

### Practical Impact on Cybercrime Cases

1. **Charge selection before extradition:** Prosecutors must carefully craft the extradition request to cover all offenses they intend to prosecute. Under-inclusive requests may prevent prosecution of serious charges.
2. **Consent requests:** After extradition, prosecutors may request the surrendering state's consent to prosecute additional offenses. This adds time and creates diplomatic overhead.
3. **Superseding indictments:** In US practice, a superseding indictment adding new charges after extradition requires the surrendering state's consent, unless the new charges arise from the "same facts" as the extradited offenses (subject to treaty-specific interpretation).

## How It Works in Practice

### Standard Process

1. Requesting state submits extradition request specifying offense(s)
2. Surrendering state evaluates the request (including [[dual-criminality]])
3. Extradition is granted for the specified offense(s)
4. Requesting state may only prosecute for those offense(s)
5. If additional prosecution desired → formal request for consent to surrendering state
6. Surrendering state evaluates consent request (applying same standards as original extradition)

### "Same Conduct" Interpretation

A key question is whether the requesting state can charge *different legal offenses* arising from the *same factual conduct* described in the extradition request:

- **Broad interpretation (US, UK):** Charges arising from the same factual conduct described in the extradition request are generally permitted, even if the legal characterization changes (e.g., upgrading from fraud to RICO conspiracy based on the same underlying facts).
- **Narrow interpretation (some civil law states):** Only the specific offense listed in the extradition order may be prosecuted.

### Waiver

In some jurisdictions, the extradited person may waive specialty protections. This is common in US practice, where defendants may waive specialty as part of a plea agreement.

## Variations Across Jurisdictions

### Common Law

Common law jurisdictions (US, UK, Australia, Canada) generally apply the specialty principle as a treaty obligation but allow flexible interpretation of "same offense." US courts have held that specialty is primarily a right of the surrendering state, not the individual (*United States v. Rauscher*, 1886, established the principle; subsequent cases have narrowed individual standing).

### Civil Law

Civil law jurisdictions tend to apply the specialty principle more strictly, viewing it as both a state right and an individual right. European Convention on Extradition Art. 14 is interpreted as creating an individual right enforceable by the extradited person.

### European Arrest Warrant

The EU's European Arrest Warrant (EAW) Framework Decision has significantly relaxed the specialty rule within the EU. Art. 27(1) presumes member states have given consent to prosecution for offenses other than the one for which surrender was granted, unless the executing member state has made a specific notification to the contrary.

## Key Case Law

### United States v. Rauscher (US, 1886)

The foundational US case establishing the specialty principle. The Supreme Court held that a person extradited under a treaty may only be tried for the offense for which extradition was granted.

### United States v. Andonian (9th Cir., 1994)

The Ninth Circuit held that specialty protections are for the benefit of the surrendering state, and the defendant has standing to raise the issue only insofar as the surrendering state has not waived or consented.

## Debates and Controversies

1. **Standing to invoke specialty.** Disagreement over whether the extradited person has independent standing to invoke the specialty principle, or whether it is exclusively a right of the surrendering state. This matters because surrendering states may consent to additional prosecution without consulting the defendant.

2. **Breadth of "same offense."** How broadly should "same offense" be interpreted? A narrow interpretation (strict specialty) may let cybercriminals escape prosecution for serious charges due to technical drafting errors in the extradition request. A broad interpretation may undermine the protective purpose of the principle.

3. **Cybercrime-specific challenges.** The multi-offense nature of cybercrime means extradition requests may fail to anticipate all relevant charges. Should specialty rules be relaxed for cybercrime to allow more flexible prosecution?

4. **Consent delays.** Requests for consent to prosecute additional offenses add months or years to proceedings. Some argue the consent process should be streamlined for cybercrime cases.

## Example: Phobos Admin Extradited from Korea to US

The [[phobos-8base-crackdown|Phobos/8Base crackdown]] (2025) involved the arrest of a suspect in South Korea who was subsequently extradited to the United States. The specialty principle applies to this case:

- The suspect was likely extradited for specific charges in the US indictment (e.g., wire fraud conspiracy, computer fraud, extortion)
- The US may only prosecute for those charges (and closely related ones arising from the same facts)
- If US prosecutors discover evidence of additional, unrelated offenses (e.g., separate hacking campaigns not covered by the extradition request), they would need Korea's consent to add those charges
- The US-Korea Extradition Treaty Art. 15 governs the specialty obligation

This is a significant practical constraint. Korean authorities, having made a sovereign decision to surrender the suspect for specific offenses, retain a degree of control over the scope of prosecution.

> [!warning] Legal status check needed
> Verify the specific charges in the Phobos admin extradition request and whether any consent requests for additional charges have been made.

## Korean Law (한국법)

### 범죄인 인도법 (Extradition Act)

**Art. 15 (특정성의 원칙):** Korea's Extradition Act codifies the specialty principle. When Korea surrenders a person to a requesting state:

- The requesting state may not prosecute for offenses other than those for which extradition was granted
- Consent for additional prosecution must be sought through diplomatic channels (외교 경로)
- Korea evaluates consent requests applying the same standards as the original extradition (including [[dual-criminality]], political offense exception, etc.)

**Art. 39:** When Korea *receives* an extradited person from another state, Korean prosecutors are similarly bound by the specialty principle — they may only prosecute for the offenses listed in the extradition request.

### Korean Practice

Korea has been both a surrendering and requesting state in cybercrime extraditions:

- **As surrendering state:** The Phobos admin extradition (2025, to US) is the most prominent recent example. Korea's consent would be required for any expansion of charges beyond the original request.
- **As requesting state:** Korea may request extradition of cybercriminals (especially voice phishing organizers in Southeast Asia) under the [[nationality-principle]] and bilateral extradition treaties. Korean prosecutors must carefully define the scope of charges in the request.

## Multi-Language Terminology

| Language | Term | Notes |
|----------|------|-------|
| English | specialty principle | Also: rule of specialty, principle of speciality |
| Korean | 특정성의 원칙 (teukjeongseong-ui wonchik) | Also: 특정주의 |
| French | principe de spécialité | Also: règle de la spécialité |
| German | Grundsatz der Spezialität | Also: Spezialitätsprinzip |
| Spanish | principio de especialidad | |
| Japanese | 特定性の原則 (tokuteise no gensoku) | |

## Contradictions & Open Questions

- Should the specialty principle be relaxed for cybercrime cases given the multi-offense nature of cyber conduct, or would this undermine the trust framework that extradition depends on?
- Does the extradited person have independent standing to invoke specialty under Korean law (범죄인 인도법), or is it solely a state right?
- How should "same offense" be interpreted when the requesting state discovers additional cybercrime offenses during prosecution that arise from the same criminal operation but target different victims or use different techniques?
- What was the specific scope of charges in the Korea-to-US Phobos admin extradition, and has any consent request been made for additional charges?
