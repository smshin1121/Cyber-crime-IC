---
type: procedure
title: "Extradition Request Procedure"
aliases: ["Extradition", "범죄인 인도", "International Extradition"]
procedure_type: "extradition-request"
legal_basis:
  - "Bilateral extradition treaties"
  - "[[budapest-convention]] Art. 24"
  - "European Arrest Warrant (EU Council Framework Decision 2002/584/JHA)"
  - "UNTOC (Palermo Convention) Art. 16"
  - "Domestic extradition legislation"
mechanisms_involved:
  - "[[mlat-process]]"
  - "[[24-7-network]]"
typical_participants:
  requesting: "Requesting state: prosecution authority → central authority (Ministry of Justice/Foreign Affairs) → diplomatic channel"
  requested: "Requested state: diplomatic channel → central authority → judiciary → executive"
prerequisites:
  - "Valid arrest warrant or conviction in the requesting state"
  - "Extradition treaty or other legal basis between the two states"
  - "Dual criminality — the offense must be criminal in both states (with exceptions)"
  - "The offense must meet the minimum severity threshold (typically 1+ year imprisonment)"
  - "The person must be located in the requested state's territory"
  - "No applicable bars to extradition (political offense, nationality, double jeopardy, death penalty risk)"
average_duration: "6-24 months"
steps:
  - step: 1
    actor: "Requesting state prosecution authority"
    action: "Prepare extradition request package: diplomatic note, arrest warrant, statement of facts, applicable law, evidence of identity, assurances (if needed)"
    documents: ["Diplomatic note", "Certified copy of arrest warrant or judgment", "Statement of the offense and applicable law", "Evidence of identity (photos, fingerprints)", "Assurances regarding specialty, death penalty, or detention conditions (if required)"]
    notes: "Document requirements vary significantly by treaty and requested state. Translation into the requested state's language is typically required."
  - step: 2
    actor: "Requesting state central authority"
    action: "Review the request for completeness and legal sufficiency, then transmit through diplomatic channel to the requested state"
    documents: ["Formal extradition request with all supporting documents"]
    notes: "Central authority is typically the Ministry of Justice (법무부 in Korea) or Attorney General's office. Some bilateral treaties allow direct authority-to-authority transmission."
  - step: 3
    actor: "Requested state central authority"
    action: "Receive the request, review for formal compliance with treaty requirements, and transmit to the competent judicial authority"
    documents: []
    notes: "Central authority screens for basic legal sufficiency. Some states (US, UK) have extensive central authority review; others route quickly to courts."
  - step: 4
    actor: "Requested state judiciary"
    action: "Conduct judicial hearing: review dual criminality, identity, treaty compliance, bars to extradition, human rights considerations. The fugitive has the right to legal representation and to contest extradition."
    documents: ["Judicial extradition order or decision"]
    notes: "Judicial review varies significantly: common law systems (US, UK) hold adversarial hearings; civil law systems (Germany, France, Korea) may involve a different procedural format. Human rights review (ECHR Art. 3 in Europe) is increasingly important."
  - step: 5
    actor: "Requested state executive authority"
    action: "Ministerial decision on whether to surrender the person. In many systems, the executive has final discretion even after judicial approval."
    documents: ["Executive surrender order"]
    notes: "In some systems (Korea: 법무부장관 결정), the executive can refuse extradition on policy grounds even after judicial approval. In others (UK), the Home Secretary's role is more limited after judicial approval. In EU EAW cases, there is no executive stage."
  - step: 6
    actor: "Both states"
    action: "Physical surrender: coordinate transfer logistics, including escort, transportation, and documentation. The person is transferred to custody of the requesting state."
    documents: ["Surrender documentation", "Transfer of custody records"]
    notes: "The rule of specialty applies: the requesting state may only prosecute for the offenses specified in the extradition request (unless the requested state consents to additional charges)."
success_factors:
  - "Strong bilateral extradition treaty with clear terms"
  - "Early engagement with the requested state through diplomatic and LEA channels"
  - "Complete and well-prepared request package (reduces back-and-forth)"
  - "Provisional arrest (if available under the treaty) to prevent flight while the full request is prepared"
  - "Effective legal representation in the requested state to anticipate and address objections"
  - "Political will and diplomatic cooperation"
common_pitfalls:
  - "Incomplete or poorly translated documentation — causes delays of months for supplementation"
  - "Dual criminality failure — the offense is not criminal in the requested state (particularly for newer cyber offenses)"
  - "Nationality bar — many civil law countries (Germany, Japan, Korea) do not extradite their own nationals"
  - "Political offense exception — rarely applies to cybercrime but may be raised"
  - "Human rights challenges — claims of unfair trial, torture risk, or disproportionate sentencing in the requesting state"
  - "Competing extradition requests from multiple states"
  - "Fugitive flight during prolonged proceedings"
  - "Death penalty bar — many states refuse extradition unless the requesting state provides assurances that the death penalty will not be imposed"
template_available: false
related_procedures:
  - "[[emergency-data-preservation]]"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

Extradition is the **formal legal process** by which one state requests another to surrender a person accused or convicted of a criminal offense so that the person may face trial or serve a sentence in the requesting state. For cybercrime, extradition is critical when key suspects are located outside the investigating state's jurisdiction — a common scenario given the borderless nature of cyber offenses.

Extradition proceedings are *almost certainly* the **most complex and time-consuming** IC procedure, typically taking 6-24 months and sometimes years. They involve diplomatic, executive, and judicial stages, and are subject to numerous legal bars and human rights considerations.

## Legal Basis

Extradition is governed by a layered framework:

### Treaty Basis

1. **Bilateral extradition treaties:** The primary legal basis between specific state pairs (e.g., US-Korea Extradition Treaty, 1998)
2. **Multilateral conventions:** The [[budapest-convention]] Art. 24 provides an extradition basis for cybercrime offenses between parties. UNTOC Art. 16 covers transnational organized crime
3. **European Arrest Warrant (EAW):** Within the EU, the EAW replaces traditional extradition with a simplified judicial surrender procedure (EU Council Framework Decision 2002/584/JHA)

### Domestic Legislation

Each state has domestic extradition law:
- **South Korea:** 범죄인 인도법 (Extradition Act)
- **United States:** 18 U.S.C. Chapter 209 (Extradition)
- **United Kingdom:** Extradition Act 2003
- **Germany:** Gesetz uber die internationale Rechtshilfe in Strafsachen (IRG)

### Key Legal Principles

- **Dual criminality (쌍방가벌성):** The offense must be criminal in both the requesting and requested states. See [[dual-criminality]] for detailed analysis.
- **Specialty rule:** The extradited person may only be tried for the offense(s) specified in the extradition request
- **Non bis in idem (double jeopardy):** Extradition may be refused if the person has already been tried for the same offense
- **Political offense exception:** Traditionally bars extradition for political offenses (rarely applicable to cybercrime)
- **Nationality exception:** Many civil law states do not extradite their own nationals (aut dedere aut judicare — extradite or prosecute)

## Prerequisites

Before initiating an extradition request:

1. **Valid legal basis:** Arrest warrant (pre-trial) or judgment (post-conviction) in the requesting state
2. **Treaty relationship:** Extradition treaty or convention between the states (some states extradite on reciprocity without a treaty, but this is uncommon)
3. **Dual criminality:** Verified that the offense is criminal in both states
4. **Minimum severity:** The offense typically must carry a potential sentence of at least 1 year imprisonment
5. **Location confirmed:** The fugitive has been located in the requested state's territory
6. **No absolute bars:** No death penalty risk (or assurances available), no political offense, no prior adjudication

## Step-by-Step Process

### Step 1: Prepare Request Package

The requesting state's prosecution authority prepares a comprehensive extradition request containing:

- **Diplomatic note:** Formal request from the requesting state's government
- **Arrest warrant/judgment:** Certified copy of the domestic warrant or conviction
- **Statement of facts:** Detailed description of the criminal conduct
- **Applicable law:** Text of the relevant criminal statutes, showing dual criminality
- **Evidence of identity:** Photographs, fingerprints, physical description
- **Assurances:** If required, regarding specialty, death penalty, detention conditions
- **Translation:** All documents translated into the requested state's official language

**Cybercrime-specific documentation:**
- Technical evidence summary (server logs, IP addresses, cryptocurrency traces)
- Explanation of the cyber offense in non-technical terms for judicial review
- Mapping of cyber offense to both states' criminal codes (dual criminality analysis)

### Step 2: Central Authority Transmission

The requesting state's central authority (typically Ministry of Justice) reviews the request for completeness and transmits it through the diplomatic channel. Some modern treaties allow direct authority-to-authority transmission.

### Step 3: Requested State Review

The requested state's central authority receives the request and conducts an initial review for:
- Treaty compliance
- Formal document requirements
- Potential bars to extradition
- Need for supplemental information

The request is then routed to the competent judicial authority.

### Step 4: Judicial Hearing

The requested state's judiciary holds an extradition hearing. The fugitive has the right to:
- Legal representation
- Contest the request on legal grounds
- Challenge identity
- Raise human rights objections
- Invoke bars to extradition

**Common judicial issues in cybercrime extraditions:**
- Dual criminality analysis for novel cyber offenses
- Jurisdiction challenges (where did the crime "occur"?)
- Proportionality of the request relative to the offense
- Human rights review (particularly regarding US sentencing)

### Step 5: Executive Decision

In most systems, after judicial approval, the executive authority (Minister of Justice) makes the final surrender decision. The executive may consider:
- Diplomatic and political factors
- Humanitarian considerations
- Competing requests from other states
- Policy implications

### Step 6: Physical Surrender

Upon all approvals, the person is physically transferred to the custody of the requesting state. Logistics include:
- Escort arrangements
- Air transportation
- Transit country clearances (if needed)
- Transfer of personal property
- Documentation

### Provisional Arrest

Many extradition treaties provide for **provisional arrest** pending the full extradition request:
- Requested through INTERPOL (Red Notice) or direct diplomatic channel
- Person arrested and held for a limited period (typically 40-60 days)
- Full extradition request must be submitted within this period
- Critical for preventing flight when the full request is still being prepared

## Required Documents

| Document | Prepared By | Notes |
|----------|-------------|-------|
| Diplomatic note | Foreign ministry | Formal government-to-government request |
| Arrest warrant (certified) | Court | Must be currently valid |
| Statement of facts | Prosecutor | Detailed, non-technical summary |
| Applicable law texts | Prosecutor | Both states' relevant statutes |
| Identity evidence | Police | Photos, fingerprints, description |
| Dual criminality analysis | Prosecutor | Mapping offenses across both legal systems |
| Assurances (if needed) | Government | Death penalty, specialty, conditions |
| Translations | Certified translator | Into requested state's language |

## Timelines

| Phase | Typical Duration | Notes |
|-------|-----------------|-------|
| Request preparation | 1-3 months | Gathering documents, translations |
| Diplomatic transmission | 2-4 weeks | Through foreign ministries |
| Central authority review | 1-3 months | Both states |
| Judicial hearing | 2-6 months | Depends on court schedule, complexity, appeals |
| Executive decision | 1-3 months | Political considerations |
| Physical surrender | 1-4 weeks | Logistics |
| **Total** | **6-24 months** | Can be longer if contested vigorously |

### European Arrest Warrant (Comparison)

Within the EU, the EAW dramatically compresses timelines:
- **Decision deadline:** 60 days (extendable to 90)
- **No executive stage:** Purely judicial
- **No dual criminality for 32 listed offenses** (including cybercrime)
- **Practical:** 1-3 months typical

## Practical Tips

1. **Use provisional arrest:** If the fugitive may flee, seek provisional arrest through INTERPOL Red Notice simultaneously with preparing the full request
2. **Engage early informally:** Contact the requested state's central authority informally to understand documentation requirements before the formal submission
3. **Dual criminality mapping:** Prepare a detailed mapping of the cyber offense to the requested state's criminal code — this is the most common challenge point
4. **Anticipate human rights objections:** Prepare assurances regarding detention conditions, fair trial, and sentencing proportionality proactively
5. **Coordinate with INTERPOL:** Issue a Red Notice through INTERPOL for fugitives whose location is unknown
6. **Consider alternatives:** If extradition is blocked (e.g., nationality bar), explore alternatives: aut dedere aut judicare (request prosecution in the fugitive's home state), transfer of proceedings, or conviction in absentia

## Country-Specific Variations

### United States

- **Central authority:** US Department of Justice, Office of International Affairs (OIA)
- **Treaty network:** 100+ bilateral extradition treaties
- **Judicial hearing:** Federal magistrate or district judge conducts certification hearing under 18 U.S.C. 3184
- **Executive decision:** Secretary of State has final discretion
- **No nationality bar:** The US extradites its own nationals
- **Sentencing concerns:** US sentencing guidelines often trigger human rights challenges from requested states (particularly EU)

### European Union (EAW)

- **Simplified judicial surrender:** No diplomatic channel, no executive stage
- **Issuing judicial authority** sends EAW directly to **executing judicial authority**
- **32 listed offenses** (including cybercrime) exempt from dual criminality check
- **60-90 day decision deadline**
- **Brexit impact:** UK no longer participates in the EAW; uses the UK-EU Trade and Cooperation Agreement's Part Three surrender mechanism (similar to EAW but with some additional safeguards)

### Civil Law Countries (Germany, Japan, Korea)

- **Nationality exception:** Most civil law countries do not extradite their own nationals. Instead, they may prosecute the person domestically (aut dedere aut judicare)
- **Judicial review format:** May differ from common law adversarial hearing

## Common Pitfalls

1. **Incomplete documentation:** The #1 cause of delay. Requests returned for supplementation can add 3-6 months
2. **Dual criminality for novel cyber offenses:** Crimes like DDoS attacks, ransomware distribution, or cryptocurrency theft may not have exact equivalents in both legal systems
3. **Nationality bar:** Attempting to extradite a national of the requested state without awareness of the nationality exception
4. **Fugitive flight:** Prolonged proceedings allow fugitives to flee to third countries
5. **Multiple competing requests:** If multiple states seek the same person, complex priority decisions arise
6. **Human rights litigation:** Particularly in European courts, challenges under ECHR Art. 3 (prohibition of torture/inhuman treatment) can add years
7. **Political interference:** High-profile cases may face political obstacles

## Related Procedures

- **[[emergency-data-preservation]]** — Often precedes or runs parallel to extradition in cybercrime cases; preserving digital evidence while seeking the suspect
- Standard [[mlat-process]] — MLA for evidence is typically separate from extradition but may run in parallel

## Korean Practice (한국 실무)

### Domestic Legal Framework

Korea's extradition practice is governed by:
- **범죄인 인도법 (Extradition Act):** Primary domestic legislation governing extradition requests to and from Korea
- **대한민국 범죄인인도조약 (Bilateral extradition treaties):** Korea has extradition treaties with approximately 30+ countries, including the US (1998), Japan, Australia, and multiple EU member states

### Korean Extradition Procedure (Incoming Request)

When a foreign state requests extradition from Korea:

1. **Receipt:** Ministry of Foreign Affairs (외교부) receives diplomatic note
2. **Central authority review:** Ministry of Justice (법무부) reviews for treaty compliance
3. **Judicial review:** Seoul High Court (서울고등법원) conducts the extradition hearing
4. **Judicial decision:** Court issues a ruling (인도심사결정) on whether extradition is legally permissible
5. **Executive decision:** Minister of Justice (법무부장관) makes the final surrender decision
6. **Physical surrender:** Coordinated through Ministry of Justice and police

### Korean Extradition Procedure (Outgoing Request)

When Korea seeks extradition of a person from abroad:

1. **Prosecution prepares request:** Supreme Prosecutors' Office (대검찰청)
2. **Ministry of Justice review:** 법무부 국제법무과 reviews and approves
3. **Diplomatic transmission:** Through Ministry of Foreign Affairs
4. **Follow-up:** Korean embassy coordinates with requested state

### Nationality Exception

Korea generally **does not extradite its own nationals** under the 범죄인 인도법, consistent with civil law tradition. However, Korea will prosecute its nationals domestically for offenses committed abroad under the principle of aut dedere aut judicare.

### Cybercrime Extradition Example: Phobos/8Base (2025)

The most notable recent cybercrime extradition involving Korea:
- A Phobos ransomware administrator was **arrested in South Korea** during the [[phobos-8base-crackdown]] (2025)
- The individual was **extradited to the United States** within approximately 6 months
- This case demonstrates Korea's operational capability and willingness to execute cybercrime extraditions
- Legal basis: Korea-US Extradition Treaty (1998) and [[budapest-convention]] Art. 24

> [!note] Translation note
> "범죄인 인도" (beomjoein indo) is the Korean legal term for extradition. The 범죄인 인도법 is the primary enabling legislation. "인도심사" (indo-simsa) refers to the judicial extradition review proceeding.

## Contradictions & Open Questions

1. **Nationality bar workarounds:** How effectively does the aut dedere aut judicare principle work in cybercrime cases? Are domestic prosecutions of nationals adequate substitutes for extradition?
2. **US sentencing concerns:** Does the increasing length of US cybercrime sentences (sometimes 20+ years) create human rights objections from requested states that may slow or block extradition?
3. **Cryptocurrency tracing and extradition:** As cryptocurrency-related offenses increase, how will dual criminality analysis adapt to offenses that may not have clear equivalents in all jurisdictions?
4. **Korea extradition capacity:** What is Korea's track record for processing incoming extradition requests? Limited public data is available.
5. **Phobos precedent:** Will the successful Phobos/8Base extradition establish a routine path for cybercrime extraditions from Korea, or was it exceptional?
6. **EAW post-Brexit:** How effectively is the UK-EU surrender mechanism working compared to the pre-Brexit EAW? Early indications suggest some friction.
