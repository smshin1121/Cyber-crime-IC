---
type: procedure
title: "Emergency Data Preservation Request (Budapest Convention Art. 29)"
aliases: ["Art. 29 Preservation Request", "Expedited Preservation", "긴급 데이터 보전 요청"]
procedure_type: "evidence-preservation"
legal_basis:
  - "[[budapest-convention]] Art. 29"
  - "[[budapest-convention]] Art. 30 (expedited disclosure of preserved traffic data)"
mechanisms_involved:
  - "[[24-7-network]]"
typical_participants:
  requesting: "Law enforcement investigator/prosecutor in requesting state"
  requested: "24/7 Network contact point in requested state → domestic ISP/service provider"
prerequisites:
  - "Both states must be parties to the Budapest Convention (or have bilateral arrangement)"
  - "Requesting state has ongoing criminal investigation involving electronic evidence"
  - "Data at risk of deletion, modification, or loss (urgency must be demonstrated)"
  - "Requesting state must intend to submit a formal MLA request for production within the preservation period"
average_duration: "24-72 hours (initial preservation action); 60-day preservation hold (renewable)"
steps:
  - step: 1
    actor: "Investigating officer/prosecutor"
    action: "Identify at-risk electronic evidence stored in a foreign jurisdiction — e.g., server logs, email content, subscriber data held by a foreign ISP"
    documents: []
    notes: "Time-critical: data retention periods vary; some providers delete logs within days"
  - step: 2
    actor: "Investigating officer"
    action: "Contact the national 24/7 contact point designated under Budapest Convention Art. 35"
    documents: ["Art. 29 preservation request form (if available)", "Summary of investigation", "Description of data to be preserved"]
    notes: "In Korea, the 24/7 contact point is designated within the Supreme Prosecutors' Office (대검찰청) / KNPA (경찰청)"
  - step: 3
    actor: "National 24/7 contact point (requesting state)"
    action: "Transmit the preservation request to the 24/7 contact point of the state where data is stored, via the 24/7 Network (secure channels)"
    documents: ["Art. 29 request specifying: authority requesting, offense under investigation, data to be preserved, connection between data and offense, necessity and urgency"]
    notes: "Art. 29(2) requires: identity of requesting authority; offense summary; data description; necessity showing"
  - step: 4
    actor: "24/7 contact point (requested state)"
    action: "Receive the request and route it to the competent domestic authority for execution"
    documents: []
    notes: "The requested state must take measures under its domestic law to preserve the specified data"
  - step: 5
    actor: "Domestic authority (requested state)"
    action: "Execute a domestic preservation order against the service provider holding the data — provider must preserve the specified data for at least 60 days"
    documents: ["Domestic preservation order (form varies by jurisdiction)"]
    notes: "Art. 29(7): preservation shall be for at least 60 days, to permit the requesting state to submit a formal MLA request. Dual criminality may NOT be required for preservation (Art. 29(4))"
  - step: 6
    actor: "24/7 contact point (requested state)"
    action: "Confirm preservation to the requesting state's 24/7 contact point, including any conditions or partial refusals"
    documents: ["Confirmation communication"]
    notes: "Confirmation should be provided within hours where possible. Art. 29(5) allows refusal only if preservation is not possible under domestic law, or if the request relates to a political or military offense"
  - step: 7
    actor: "Requesting state"
    action: "Submit a formal MLA request (through MLAT or Budapest Convention Art. 31) for production of the preserved data within the 60-day preservation period"
    documents: ["Formal MLA request", "Supporting documents required by requested state"]
    notes: "Failure to submit MLA within 60 days may result in the preservation being lifted. See [[mlat-process]] for MLA procedure"
success_factors:
  - "Speed of initial identification and request submission — delay reduces preservation value"
  - "Quality and specificity of the preservation request — vague requests may be refused"
  - "24/7 contact point responsiveness in both states"
  - "Strong working relationships between 24/7 contact points"
  - "Timely follow-up with formal MLA request within the 60-day window"
common_pitfalls:
  - "Overly broad preservation requests that are rejected for lack of specificity"
  - "Failure to submit formal MLA request within the 60-day preservation period"
  - "Inadequate description of the urgency or connection between data and investigation"
  - "Requesting data from a non-Budapest party (Art. 29 only applies between parties)"
  - "Confusing preservation (Art. 29) with production (Art. 31) — preservation does NOT provide access to the data, only prevents its deletion"
  - "Insufficient domestic legal authority in the requested state for emergency preservation"
template_available: false
related_procedures:
  - "[[extradition-request]]"
source_count: 0
sources: []
created: 2026-04-08
updated: 2026-04-08
---

## Summary

The Emergency Data Preservation Request under Budapest Convention Art. 29 is the **primary mechanism** for preventing the deletion or loss of electronic evidence stored in a foreign jurisdiction while formal mutual legal assistance procedures are prepared. It leverages the [[24-7-network]] established under Art. 35 to transmit urgent preservation requests between Budapest Convention parties.

This procedure is *almost certainly* the most time-sensitive IC tool available to cybercrime investigators. Electronic evidence is volatile — server logs may be overwritten, accounts deleted, and cloud data purged according to provider retention policies. Art. 29 preservation creates a **60-day bridge** between the detection of foreign-held evidence and the formal MLA process required to obtain it.

## Legal Basis

### Budapest Convention Art. 29: Expedited Preservation of Stored Computer Data

Art. 29(1): "A Party may request another Party to order or otherwise obtain the expeditious preservation of data stored by means of a computer system, located within the territory of that other Party and in respect of which the requesting Party intends to submit a request for mutual assistance for the search or similar access, seizure or similar securing, or disclosure of the data."

Key legal features:
- **No dual criminality requirement for preservation** (Art. 29(4)): A party may reserve the right to require dual criminality, but this reservation is exceptional. Most parties do not require it for mere preservation.
- **60-day minimum preservation** (Art. 29(7)): The requested party must preserve data for at least 60 days pending the formal MLA request.
- **Limited grounds for refusal** (Art. 29(5)): Only if the offense is political or military, or if domestic execution is impossible.
- **Traffic data disclosure** (Art. 30): If during preservation execution, traffic data reveals the involvement of a service provider in another state, the preserving party must expeditiously disclose enough traffic data to enable the requesting party to identify that other provider and the path of the communication.

### Budapest Convention Art. 35: 24/7 Network

The 24/7 Network is the **designated channel** for transmitting Art. 29 requests. Each party designates a point of contact available 24/7 to facilitate urgent preservation requests and other immediate assistance.

## Prerequisites

1. **Budapest Convention membership:** Both the requesting and requested states must be parties to the Convention (or have an equivalent bilateral arrangement)
2. **Active criminal investigation:** The requesting state must have an ongoing investigation concerning offenses related to computer systems or data
3. **Urgency/risk of loss:** The requesting state must demonstrate that the data is at risk of modification, loss, or deletion
4. **Intent to follow up:** The requesting state must intend to submit a formal MLA request for production of the preserved data

## Step-by-Step Process

### Step 1: Identify At-Risk Foreign Evidence

The investigator identifies electronic evidence stored in a foreign jurisdiction that is at risk of deletion:
- Server logs at a foreign hosting provider
- Email account content at a foreign email service
- Subscriber information at a foreign ISP
- Cloud-stored files at a provider in another country
- Traffic/connection data at a foreign telecommunications provider

**Urgency indicators:**
- Provider's data retention policy expires soon
- Suspect may delete account or data
- Service being shut down
- Routine log rotation imminent

### Step 2: Contact National 24/7 Point

The investigator contacts their own country's designated 24/7 contact point with:
- Summary of the investigation
- Description of the specific data to be preserved
- Location of the data (country, provider, if known)
- Explanation of urgency
- Statement of intent to follow up with formal MLA

### Step 3: 24/7 Network Transmission

The national 24/7 contact point transmits the request to the counterpart in the country where the data is located. The request must include (per Art. 29(2)):
- Identity of the authority seeking preservation
- The offense that is the subject of investigation and a brief summary of facts
- The data to be preserved and its relationship to the offense
- Any available information identifying the custodian or location of the data
- The necessity of preservation and that the requesting party intends to submit a formal MLA request

### Step 4: Foreign 24/7 Point Routes Request

The foreign 24/7 contact point receives the request and routes it to the competent domestic authority (police, prosecutor, or judge, depending on the jurisdiction's requirements for preservation orders).

### Step 5: Domestic Preservation Order Executed

The domestic authority in the requested state issues a preservation order to the service provider. The provider must preserve the specified data for **at least 60 days** (Art. 29(7)). Some jurisdictions allow longer periods.

### Step 6: Confirmation

The requested state's 24/7 point confirms preservation to the requesting state, including:
- Whether preservation was executed in full or partially
- Any conditions attached
- If refused, the grounds for refusal (Art. 29(5))

Confirmation should be provided **within hours** where operationally possible.

### Step 7: Formal MLA Follow-Up

The requesting state must submit a formal MLA request for **production** of the preserved data within the 60-day preservation period. This follows the standard [[mlat-process]] or Budapest Convention Art. 31 procedure.

> [!warning] Critical
> Preservation only prevents deletion — it does NOT provide access to the data. A formal MLA request is always required for actual production.

## Required Documents

| Document | Step | Prepared By |
|----------|------|-------------|
| Investigation summary | 2-3 | Investigating officer |
| Data specification (what to preserve) | 2-3 | Investigating officer |
| Art. 29 request form | 3 | 24/7 contact point |
| Domestic preservation order | 5 | Requested state authority |
| Preservation confirmation | 6 | Requested state 24/7 point |
| Formal MLA request (Art. 31) | 7 | Prosecutor/central authority |

## Timelines

| Phase | Typical Duration | Notes |
|-------|-----------------|-------|
| Internal preparation (Steps 1-2) | Hours | Depends on investigator preparedness |
| 24/7 Network transmission (Step 3) | Hours | Should be near-immediate via secure channels |
| Foreign routing and execution (Steps 4-5) | 24-72 hours | Varies significantly by country capacity |
| Confirmation (Step 6) | Hours after execution | |
| Preservation hold | 60 days minimum | Extendable by subsequent request |
| Formal MLA submission (Step 7) | Within 60 days | Often the bottleneck — MLA preparation is time-consuming |

**Total critical timeline:** 24-72 hours from request to preservation confirmed.

## Practical Tips

1. **Prepare MLA in parallel:** Begin drafting the formal MLA request simultaneously with the Art. 29 preservation request — do not wait for confirmation
2. **Be specific:** Specify exact data types, accounts, IP addresses, and date ranges. Vague requests are more likely to be refused or executed imperfectly
3. **Know your 24/7 point:** Maintain a current relationship with your national 24/7 contact. Response time depends partly on the quality of this working relationship
4. **Include provider information:** If you know the service provider (e.g., Google, Amazon AWS, OVH), include this in the request to speed routing
5. **Track retention policies:** Maintain awareness of major providers' data retention policies (some delete logs in 30 days or less)
6. **Use Art. 30 proactively:** If traffic data reveals involvement of additional jurisdictions, request expedited disclosure under Art. 30 immediately

## Country-Specific Variations

### United States

The US 24/7 contact point is the [[us-doj|Department of Justice, Computer Crime and Intellectual Property Section (CCIPS)]]. US domestic preservation is governed by 18 U.S.C. 2703(f), which allows LEA to request providers to preserve records for 90 days (renewable for an additional 90 days).

### United Kingdom

The UK 24/7 contact point is within the [[uk-nca|National Crime Agency]]. The UK Regulation of Investigatory Powers Act 2000 and the Investigatory Powers Act 2016 govern domestic preservation.

### Germany

Germany's 24/7 contact point is within the [[germany-bka|Bundeskriminalamt]]. German domestic law may impose additional requirements for preservation orders, and the judicial review process can add time.

## Common Pitfalls

1. **Confusing preservation with production:** Art. 29 preservation prevents deletion; it does NOT give the requesting state access to the data
2. **Missing the 60-day window:** If the formal MLA request is not submitted within 60 days, the preservation may be lifted and the data lost
3. **Overly broad requests:** Requests covering "all data" without specificity are likely to be narrowed or refused
4. **Non-Budapest parties:** Art. 29 only applies between Budapest Convention parties. For non-parties, alternative arrangements (bilateral, UNTOC, informal) must be used
5. **Weekend/holiday delays:** While the 24/7 Network is designed for round-the-clock operation, some contact points have reduced capacity outside business hours
6. **Language barriers:** Requests not in a common language may be delayed for translation

## Related Procedures

- **[[extradition-request]]** — May follow if investigation leads to an arrest warrant for a suspect abroad
- Standard [[mlat-process]] — Required follow-up for actual production of preserved data

## Korean Practice (한국 실무)

### Post-2024 Access

South Korea's accession to the [[budapest-convention]] in 2024 gave Korean investigators **direct access to Art. 29 preservation** for the first time. Prior to accession, Korean LEA relied on:
- Bilateral channels (limited coverage)
- INTERPOL police-to-police cooperation (informal, no preservation authority)
- Direct voluntary requests to service providers (inconsistent compliance)

### Designated 24/7 Contact Point

Korea's 24/7 contact point is designated within the **Supreme Prosecutors' Office (대검찰청)** and/or the **Korean National Police Agency (경찰청)**. The exact designation and operational protocols are *likely* still being refined post-accession.

> [!warning] Legal status check needed
> The exact designation of Korea's 24/7 contact point should be confirmed. The Budapest Convention requires parties to designate a point of contact, but the public designation for Korea may not yet be widely documented.

### Domestic Legal Basis

Korean domestic law supporting preservation includes:
- 형사소송법 (Criminal Procedure Act) — provisions for evidence preservation
- 통신비밀보호법 (Communications Privacy Protection Act) — telecommunications data
- 전기통신사업법 (Telecommunications Business Act) — provider cooperation obligations
- 정보통신망 이용촉진 및 정보보호 등에 관한 법률 (ICNA) — internet service providers

### Practical Considerations

Korean investigators seeking Art. 29 preservation should:
1. Coordinate with the designated 24/7 contact point early
2. Prepare bilingual (Korean/English) request documentation
3. Include specific technical details (IP addresses, account identifiers, date ranges)
4. Begin formal MLA preparation simultaneously to avoid missing the 60-day window
5. Maintain awareness that some requested states may have longer processing times

## Contradictions & Open Questions

1. **Renewal mechanism:** Can the 60-day preservation period be extended, and how often? Art. 29(7) is ambiguous about multiple extensions.
2. **Provider compliance rates:** What percentage of service providers comply fully with Art. 29 preservation orders? No systematic data is available.
3. **Korean 24/7 capacity:** How effectively is Korea's newly established 24/7 contact point operating? Post-accession operational experience is limited.
4. **Non-party data:** How should investigators handle data stored in non-Budapest party states (e.g., China, Russia)? Alternative mechanisms are less reliable and slower.
5. **Cloud complexity:** When data is distributed across multiple jurisdictions by a cloud provider, which state(s) should receive the Art. 29 request? The "loss of location" problem complicates this procedure.
