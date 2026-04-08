---
type: mechanism
title: "Mutual Legal Assistance Treaty (MLAT) Process"
aliases: ["MLAT", "MLA", "사법공조", "Mutual Legal Assistance"]
mechanism_type: "formal-mlat"
formality: "formal"
legal_basis:
  - "[[budapest-convention]]"
  - "Bilateral MLATs between states"
  - "UNTOC (Palermo Convention) Art. 18"
  - "UNCAC Art. 46"
administered_by: "Central authorities of each state"
participants:
  type: "states"
  count: 0
  notable_members: []
purpose: "The formal legal channel through which states request and provide assistance in criminal investigations and proceedings, including evidence collection, witness testimony, and asset tracing across borders."
speed: "months"
scope:
  evidence_preservation: true
  evidence_production: true
  real_time_data: false
  subscriber_info: true
  content_data: true
  traffic_data: true
  arrest_coordination: false
  asset_tracing: true
  intelligence_sharing: false
limitations:
  - "Slow: 6-18 months average, sometimes years"
  - "Volume: central authorities overwhelmed with requests"
  - "Dual criminality may be required"
  - "Translation requirements add delay"
  - "Different legal standards between common/civil law"
operations_using: []
cases_using: []
related_mechanisms:
  - "[[24-7-network]]"
  - "[[europol-jit]]"
  - "[[direct-provider-request]]"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

The Mutual Legal Assistance Treaty (MLAT) process is the **primary formal mechanism** for international cooperation in criminal matters. It enables one state to request another to collect evidence, take witness statements, execute searches, seize assets, and transfer proceedings across borders. For cybercrime, MLATs are essential but widely criticized for being too slow relative to the pace of digital evidence lifecycle.

## Legal Basis

MLATs derive from:
1. **Bilateral treaties** between specific state pairs (e.g., Korea-US MLAT, 2000)
2. **Multilateral conventions:** [[budapest-convention]] Art. 25-31, UNTOC Art. 18, UNCAC Art. 46
3. **Domestic legislation:** Each state's MLA implementing law (e.g., Korea's 국제형사사법 공조법)

In the absence of a treaty, states may still cooperate based on **reciprocity** or **comity**, but this is less reliable and typically slower.

## How It Works

### Standard MLAT Flow

```
Requesting State                              Requested State
                                              
1. Investigator identifies need    
   for foreign evidence            
                                              
2. Prosecutor prepares MLA         
   request (formal letter)         
                                              
3. Central Authority reviews       
   and transmits                   
                ──────────────────►           
                                    4. Central Authority receives
                                       and reviews for compliance
                                              
                                    5. Routes to executing agency
                                       (prosecutor/judge)
                                              
                                    6. Executes request under
                                       domestic law (may need
                                       court order)
                                              
                                    7. Returns evidence through
                ◄──────────────────    Central Authority
                                              
8. Receives evidence;              
   uses in proceedings             
```

### Central Authorities

Each state designates a **central authority** responsible for transmitting and receiving MLAT requests. This is typically:
- **Korea:** 법무부 국제형사과 (Ministry of Justice, International Criminal Affairs Division)
- **US:** Department of Justice, Office of International Affairs (OIA)
- **UK:** Home Office
- **Germany:** Federal Office of Justice (Bundesamt fur Justiz)

## Scope and Capabilities

MLATs can request a wide range of assistance:
- Execution of searches and seizures (including digital evidence)
- Compelled production of documents, records, and data
- Taking witness statements and depositions
- Service of judicial documents
- Transfer of persons in custody for testimony
- Asset identification, tracing, freezing, and confiscation
- Any other form of assistance not contrary to domestic law

## Practical Usage

### Typical Timelines

| Stage | Duration | Notes |
|-------|----------|-------|
| Drafting request | 1-4 weeks | Quality matters — poor drafts cause delays |
| Central authority review (requesting) | 1-4 weeks | |
| Transmission | Days | Electronic transmission increasingly common |
| Central authority review (requested) | 2-8 weeks | Backlog varies dramatically by country |
| Execution | 2-12 weeks | May require court order; depends on complexity |
| Return of evidence | 1-4 weeks | |
| **Total typical** | **6-18 months** | Some requests take years |

### Quality Factors

A well-drafted MLAT request should include:
- Clear identification of the investigation/proceeding
- Specific description of evidence sought (not fishing)
- Legal basis (applicable treaty, offenses, penalties)
- Dual criminality analysis (if required)
- Urgency indication with justification
- Any special handling requirements

## Advantages

- **Legally binding** — treaty obligation to assist, subject to limited refusal grounds
- **Broad scope** — can compel production of any type of evidence
- **Court-admissible** — evidence obtained through MLAT is generally admissible
- **Content data** — can obtain actual communications content (unlike many informal channels)

## Limitations

1. **Speed:** 6-18 months is too slow for volatile digital evidence that can be deleted in seconds
2. **Volume:** Central authorities (especially US DOJ/OIA) are overwhelmed
3. **Quality variance:** Poorly drafted requests cause rejections and rework cycles
4. **Legal system mismatches:** Different evidentiary standards between common/civil law
5. **[[dual-criminality]]:** May be required, creating barriers for novel cybercrimes
6. **Translation:** Legal documents must be translated, adding cost and delay
7. **Capacity disparities:** Some countries lack capacity to execute complex digital evidence requests

## Notable Uses

The MLAT process is used in virtually every significant cybercrime prosecution with cross-border elements. It is the only formal channel for obtaining **content data** across borders in most jurisdictions.

## Comparison with Alternatives

| Feature | MLAT | [[24-7-network]] | [[direct-provider-request]] | [[europol-jit]] |
|---------|------|-----------------|---------------------------|----------------|
| Speed | Months | Hours-days | Days-weeks | Ongoing |
| Formality | Formal | Semi-formal | Informal | Formal |
| Content data | Yes | No (preservation only) | Varies | Yes |
| Compelled | Yes | No | No | Within JIT scope |
| Admissible | Yes | N/A | Varies | Yes |
| Scope | Broad | Narrow (preservation) | Subscriber/traffic | Broad within JIT |

## Korean Usage (한국의 활용)

Korea's MLAT process is governed by 국제형사사법 공조법:
- **Central authority:** 법무부 국제형사과
- **Incoming requests:** MOJ reviews → assigns to regional prosecutor → execution → return
- **Outgoing requests:** Investigating prosecutor → MOJ → transmission to foreign central authority
- **30+ bilateral MLATs** in force

Common Korean MLAT scenarios:
- Requesting user data from US tech companies (via US DOJ)
- Requesting evidence from China in voice phishing (보이스피싱) cases
- Responding to foreign requests for Korean financial data

## Contradictions & Open Questions

- What is Korea's average MLAT processing time for incoming vs. outgoing requests?
- How has the Budapest Convention accession changed Korea's MLAT practice?
- Are there statistics on MLAT rejection rates by country?

## References

> [!note] This page is primarily based on treaty texts (Budapest Convention Art. 25-31, UNTOC Art. 18, bilateral MLATs), Korean legislation (국제형사사법 공조법), and general legal scholarship on mutual legal assistance. No specific collected sources from this wiki were used for this page's content, as the 20 collected sources cover operational matters rather than MLAT process descriptions. Timelines and procedural descriptions reflect widely reported practitioner estimates.
