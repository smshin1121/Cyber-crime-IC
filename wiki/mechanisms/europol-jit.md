---
type: mechanism
title: "Europol Joint Investigation Team (JIT)"
aliases: ["JIT", "Joint Investigation Team", "Europol JIT", "공동수사팀"]
mechanism_type: "joint-investigation-team"
formality: "formal"
legal_basis:
  - "[[budapest-convention]]"
  - "EU Council Framework Decision 2002/465/JHA"
  - "EU Convention on Mutual Assistance in Criminal Matters (2000) Art. 13"
  - "[[second-additional-protocol]] Art. 9-12"
administered_by: "[[eurojust]]"
participants:
  type: "mixed"
  count: 0
  notable_members:
    - "[[europol-ec3]]"
    - "[[eurojust]]"
    - "[[fbi-cyber-division]]"
    - "[[uk-nca]]"
    - "[[germany-bka]]"
    - "[[netherlands-politie]]"
purpose: "A formal cooperation structure enabling investigators and prosecutors from multiple countries to work together as a single team, sharing evidence directly and coordinating operational activities in real time for cross-border cybercrime investigations."
speed: "weeks-months"
scope:
  evidence_preservation: true
  evidence_production: true
  real_time_data: true
  subscriber_info: true
  content_data: true
  traffic_data: true
  arrest_coordination: true
  asset_tracing: true
  intelligence_sharing: true
limitations:
  - "Setup requires weeks to months of negotiation and formal agreement"
  - "Primarily EU-focused; non-EU participation requires additional legal arrangements"
  - "Resource-intensive: requires dedicated personnel and coordination infrastructure"
  - "Effectiveness depends on participant commitment and domestic legal constraints"
  - "Evidence admissibility rules vary between participating jurisdictions"
operations_using:
  - "[[operation-cronos-phase1]]"
  - "[[operation-cronos-phase3]]"
  - "[[operation-endgame-phase1]]"
  - "[[operation-endgame-phase2]]"
  - "[[phobos-8base-crackdown]]"
  - "[[operation-stream-kidflix]]"
  - "[[operation-talent]]"
cases_using: []
related_mechanisms:
  - "[[mlat-process]]"
  - "[[24-7-network]]"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

A Joint Investigation Team (JIT) is a **formal cooperation structure** that enables investigators and prosecutors from multiple countries to work together as a unified team for a defined period and purpose. In the cybercrime context, JITs coordinated through [[europol-ec3|Europol's European Cybercrime Centre (EC3)]] and [[eurojust]] have become the **primary operational mechanism** for major cross-border cybercrime investigations in Europe and beyond.

JITs are *almost certainly* the most effective IC mechanism for complex, multi-country cybercrime operations. They enable direct evidence sharing between participants (bypassing formal MLAT channels within the JIT scope), real-time coordination of takedowns and arrests, and combined analytical capabilities.

## Legal Basis

JITs derive authority from multiple legal instruments:

1. **EU Convention on Mutual Assistance in Criminal Matters (2000), Art. 13:** The foundational EU legal basis for JITs between EU member states
2. **EU Council Framework Decision 2002/465/JHA:** Standardized JIT implementation across EU member states
3. **[[budapest-convention]] Art. 30:** Provides a legal basis for JITs between Budapest Convention parties (including non-EU states)
4. **[[second-additional-protocol]] Art. 9-12:** Enhanced JIT provisions specifically for cybercrime, once the Protocol enters into force
5. **Bilateral MLA treaties:** May provide supplementary legal basis for non-EU state participation

For each JIT, a **JIT Agreement** is signed by all participating states, defining:
- Scope and duration
- Participating authorities
- Leadership and coordination
- Evidence sharing rules
- Applicable law
- Funding arrangements

## How It Works

### Setup Phase (Weeks to Months)

1. **Initiation:** Lead state (usually the most affected or best-positioned) proposes a JIT
2. **Coordination request:** Through [[eurojust]] (judicial) and [[europol-ec3]] (operational)
3. **Negotiation:** Participating states agree on scope, duration, and terms
4. **JIT Agreement signing:** Formal document signed by all parties
5. **Eurojust funding:** Financial support for operational costs (travel, interpretation, technical support)

### Operational Phase

Once established, a JIT operates as an integrated team:

```
                 ┌─────────────────────────┐
                 │     EUROPOL EC3         │
                 │  (Operational Hub)       │
                 │  - Analytical support    │
                 │  - Cross-matching        │
                 │  - Coordination centre   │
                 └───────────┬─────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼─────┐       ┌─────▼────┐        ┌─────▼────┐
   │ Country A │       │ Country B │        │ Country C│
   │ (Lead)    │       │           │        │          │
   │ Police    │◄─────►│ Police    │◄──────►│ Police   │
   │ Prosecutor│       │ Prosecutor│        │Prosecutor│
   └───────────┘       └──────────┘        └──────────┘
        ▲                    ▲                    ▲
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                 ┌───────────▼─────────────┐
                 │       EUROJUST          │
                 │  (Judicial Support)      │
                 │  - MLA coordination      │
                 │  - Legal advice          │
                 │  - Evidence admissibility│
                 └─────────────────────────┘
```

**Key operational features:**
- **Direct evidence sharing:** JIT members can share evidence directly without formal MLA requests — the JIT Agreement pre-authorizes this
- **Real-time coordination:** Europol provides a secure coordination center for simultaneous actions (Action Days)
- **Seconded members:** Officers from one country work temporarily in another country's territory
- **Joint analytical products:** Europol analysts process data from all JIT members collectively
- **Coordinated arrests:** Simultaneous arrest warrants executed across multiple jurisdictions on a single "Action Day"

### Dissolution

JITs are **time-limited** (typically 1-3 years, renewable). Upon conclusion:
- Final report produced
- Evidence formally transferred for domestic prosecutions
- JIT Agreement terminates
- Follow-up actions continue through normal channels

## Scope and Capabilities

**JITs can accomplish what no single mechanism can alone:**

| Capability | JIT | Standard MLAT | 24/7 Network |
|-----------|-----|---------------|--------------|
| Evidence preservation | Yes | Yes | Yes |
| Evidence production | Yes (direct) | Yes (months) | No |
| Real-time data access | Yes | No | No |
| Arrest coordination | Yes (Action Day) | Possible | Limited |
| Asset tracing/freezing | Yes (parallel) | Yes (slow) | No |
| Intelligence sharing | Yes (ongoing) | No | Limited |
| Joint analysis | Yes | No | No |
| Speed | Fast (within JIT) | 6-18 months | Hours |

## Practical Usage

### Role of Europol EC3

[[europol-ec3]] provides:
- **Analytical support:** Cross-matching data from all JIT members using Europol databases
- **Operational coordination center:** Physical and virtual coordination for Action Days
- **Technical support:** Malware analysis, cryptocurrency tracing, digital forensics
- **Financial support:** Operational meetings funding

### Role of Eurojust

[[eurojust]] provides:
- **Judicial coordination:** Ensuring MLA requests, European Arrest Warrants, and evidence transfers comply with all participating jurisdictions' laws
- **Legal advice:** On admissibility, dual criminality, and procedural requirements
- **Funding:** JIT operational grants
- **Coordination meetings:** Hosting and facilitating

### Non-EU Participation

Non-EU states (e.g., US, UK post-Brexit, Australia, South Korea) can participate in JITs through:
- Cooperation agreements between Europol and third countries
- Operational agreements with Eurojust
- Budapest Convention Art. 30 provisions
- Bilateral MLA treaty arrangements

The [[fbi-cyber-division]] and [[uk-nca]] regularly participate in Europol-coordinated JITs.

## Advantages

1. **Speed within JIT:** Once established, evidence sharing is immediate — no per-request MLA needed
2. **Comprehensive scope:** All IC capabilities in one mechanism
3. **Institutional support:** Europol and Eurojust provide analytical, logistical, and legal infrastructure
4. **Coordinated action:** Simultaneous multi-country operations prevent target flight
5. **Admissibility guidance:** Eurojust's involvement helps ensure evidence is admissible in all jurisdictions
6. **Funding:** EU co-finances JIT operations through Eurojust grants

## Limitations

1. **Setup time:** Weeks to months to negotiate and establish a JIT
2. **EU-centric:** Primarily designed for EU member states; third-country participation requires additional arrangements
3. **Resource demand:** Requires significant personnel commitment from all participants
4. **Legal complexity:** Evidence admissibility rules still vary between jurisdictions despite JIT framework
5. **Scope limitation:** The JIT Agreement defines scope; evidence discovered outside scope may require separate authorization
6. **Not suitable for urgent single-country requests:** Overkill for simple data requests; better suited for complex multi-country operations

## Notable Uses

JITs have been used in *almost certainly* all major Europol cybercrime operations:

| Operation | Crime Type | Countries | Key Results |
|-----------|-----------|-----------|-------------|
| [[operation-cronos-phase1]] | Ransomware (LockBit) | 10 | 2 arrests, 34 servers seized |
| [[operation-cronos-phase3]] | Ransomware (LockBit) | 12 | 4 arrests, 9 servers, sanctions |
| [[operation-endgame-phase1]] | Botnets | 13 | 4 arrests, 100+ servers, 2,000+ domains |
| [[operation-endgame-phase2]] | Ransomware supply chain | 7 | 300 servers, 650 domains, EUR 3.5M |
| [[phobos-8base-crackdown]] | Ransomware (Phobos/8Base) | 14 | 4 arrests, 27 servers |
| [[operation-stream-kidflix]] | CSAM | 35 | 79 arrests, 1.8M users identified |
| [[operation-talent]] | Criminal marketplace | 8 | Cracked/Nulled forums seized |

## Comparison with Alternatives

### JIT vs. Parallel National Investigations

Without a JIT, the same investigation would require:
- Separate MLAT requests between each country pair
- No direct evidence sharing
- Sequential rather than simultaneous actions
- No unified analytical picture
- Significantly longer timelines

### JIT vs. INTERPOL Coordination

INTERPOL operations (HAECHI, Jackal, etc.) use a different model:
- **INTERPOL model:** Information sharing and coordination without formal legal authority; each country conducts domestic operations
- **JIT model:** Formal legal authority for direct evidence sharing and joint operations

The JIT model is more legally robust but more resource-intensive and EU-focused.

## Korean Usage (한국의 활용)

South Korea's participation in Europol JITs is limited but growing:

### Current Status

- Korea has a **Strategic Agreement** with Europol (signed 2014) enabling information sharing but not full operational participation
- Korean officers have participated in JIT-related coordination meetings for operations involving Korean victims or suspects
- The [[phobos-8base-crackdown]] (2025) involved a suspect arrested in South Korea and extradited to the US, demonstrating Korean integration into JIT-linked operations

### Potential for Enhanced Participation

Korea's 2024 accession to the [[budapest-convention]] provides a legal basis (Art. 30) for Korean participation in Budapest-based JITs. Combined with a potential [[second-additional-protocol]] ratification, Korea could formalize its participation in future cyber JITs.

### Practical Barriers

- Geographic distance from Europol headquarters (The Hague)
- Time zone differences complicate real-time coordination
- Korean domestic legal requirements for evidence sharing may require legislative updates
- Language barriers (Korean is not a Europol working language)

> [!note] Translation note
> "Joint Investigation Team" is rendered in Korean as "공동수사팀" (gongdong-susa-tim). In Korean legal practice, the concept is also related to "합동수사단" used for domestic joint investigations.

## Contradictions & Open Questions

1. **Evidence admissibility:** Do all JIT member states consistently accept evidence gathered by other JIT members? Anecdotal reports suggest some courts still require formal MLA-like documentation.
2. **Non-EU equality:** Are non-EU JIT participants treated as full equals, or do they face information-sharing restrictions?
3. **Korea's JIT future:** Will Korea pursue an Operational Agreement with Europol to enable full JIT participation? Timeline is unknown.
4. **Post-Brexit UK:** How has the UK's exit from the EU affected its JIT participation? The UK-EU Trade and Cooperation Agreement provides a framework, but practical impacts are still emerging.
5. **Scale limits:** Are JITs scalable to operations involving 30+ countries, or do they work best for smaller coalitions? Operations like Kidflix (35 countries) push the model's limits.
