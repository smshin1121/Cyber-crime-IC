---
type: mechanism
title: "INTERPOL I-GRIP (Global Rapid Intervention of Payments)"
aliases: ["I-GRIP", "Global Rapid Intervention of Payments", "INTERPOL Anti-Money Laundering Rapid Response Protocol"]
mechanism_type: "information-sharing-platform"
formality: "semi-formal"
legal_basis:
  - "INTERPOL Constitution Art. 2 (mutual assistance)"
  - "National anti-money laundering / proceeds of crime legislation"
administered_by: "[[interpol-igci]]"
participants:
  type: "agencies"
  count: 0
  notable_members:
    - "[[knpa-cyber-bureau]]"
    - "[[interpol-igci]]"
purpose: "A rapid payment interception mechanism that enables INTERPOL member countries to request the freezing or interception of fraudulently obtained funds as they move across borders through the banking system, before the funds are withdrawn or laundered beyond recovery."
speed: "hours-days"
scope:
  evidence_preservation: false
  evidence_production: false
  real_time_data: false
  subscriber_info: false
  content_data: false
  traffic_data: false
  arrest_coordination: false
  asset_tracing: true
  intelligence_sharing: true
limitations:
  - "Depends on speed of financial institution response — banking hours and processes vary"
  - "Limited to funds still in the banking system — cryptocurrency and cash withdrawals not covered"
  - "Requires rapid identification of recipient accounts and financial intermediaries"
  - "Effectiveness diminishes rapidly with time — funds must be intercepted before they are moved or withdrawn"
  - "No independent legal authority — relies on domestic laws in each country"
  - "Not all INTERPOL member countries have integrated I-GRIP into their NCB workflows"
operations_using:
  - "[[operation-haechi-v]]"
  - "[[operation-haechi-vi]]"
  - "[[operation-first-light-2024]]"
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

INTERPOL's I-GRIP (Global Rapid Intervention of Payments) is a **rapid financial interception mechanism** that enables law enforcement agencies in INTERPOL member countries to request the freezing or interception of fraudulent cross-border payments before the funds are withdrawn or laundered. Operating through INTERPOL's I-24/7 secure communications network and National Central Bureaus (NCBs), I-GRIP provides a semi-formal channel that is *significantly faster* than traditional MLAT-based asset freezing procedures.

I-GRIP has become a **critical tool** in INTERPOL's financial crime operations, particularly the HAECHI and First Light series, where it has contributed to the recovery of hundreds of millions of dollars in stolen funds.

## Legal Basis

I-GRIP operates under:
1. **INTERPOL Constitution Art. 2:** Mandate for the widest possible mutual assistance between criminal police authorities
2. **Domestic AML/proceeds of crime legislation:** Each country's ability to freeze funds depends on its domestic legal framework (e.g., Korean "범죄수익 은닉의 규제 및 처벌 등에 관한 법률")
3. **Banking regulations:** Financial institutions' obligations to cooperate with law enforcement under domestic law

I-GRIP does **not** have independent treaty-based legal authority. It functions as a **communication and coordination channel** that enables countries to invoke their domestic authorities rapidly.

## How It Works

### Standard I-GRIP Flow

```
Victim country                INTERPOL               Recipient country
                                                     
1. Fraud detected;                                   
   funds traced to            
   foreign account            
                                                     
2. NCB sends I-GRIP   ──────►                        
   request via I-24/7         3. INTERPOL routes     
                              ──────────────────────► 4. NCB receives request
                                                     
                                                      5. NCB contacts domestic
                                                         financial institution
                                                     
                                                      6. Bank freezes account
                                                         (domestic legal basis)
                                                     
                              ◄──────────────────────  7. Confirmation sent
                                                     
◄──────────────────────                               
8. Victim country                                     
   initiates formal                                   
   MLA/asset recovery                                
```

### Speed Advantage

| Mechanism | Typical timeline for asset freeze |
|-----------|----------------------------------|
| I-GRIP | Hours to days |
| [[24-7-network]] + MLAT | Days to weeks (preservation), months (formal freeze) |
| Standard [[mlat-process]] | 6-18 months |

The speed advantage is critical because fraudulent funds are typically moved through **multiple accounts and jurisdictions** within 24-72 hours. Without rapid interception, the funds become irrecoverable.

### Key Success Factors

1. **Speed of detection:** The victim country must identify the fraud and trace funds quickly
2. **Banking system access:** The recipient country's NCB must have an established relationship with domestic financial institutions
3. **Domestic legal authority:** The recipient country must have legal grounds to freeze funds on an emergency basis
4. **I-24/7 availability:** Both NCBs must be operationally responsive (24/7 staffing is ideal but not universal)

## Scope and Capabilities

**I-GRIP can do:**
- Rapid freezing of funds in bank accounts across borders
- Tracing of multi-hop fund movements through correspondent banking
- Coordination of simultaneous freezes in multiple countries
- Provide intelligence on account holders and transaction patterns

**I-GRIP cannot do:**
- Freeze cryptocurrency (different mechanisms needed)
- Intercept cash withdrawals already completed
- Compel banks to disclose account information without domestic authority
- Substitute for formal mutual legal assistance for evidentiary purposes
- Function as a legal basis for long-term asset seizure (domestic orders needed)

## Practical Usage

### HAECHI Series

I-GRIP has been deployed extensively in the HAECHI operations:

| Operation | Recovery | Countries | I-GRIP Role |
|-----------|---------|-----------|-------------|
| [[operation-haechi-v]] (2024) | USD 400M+ | 40 | Key mechanism for cross-border fund interception |
| [[operation-haechi-vi]] (2025) | USD 439M | 40 | Korea-UAE sub-operation used I-GRIP to recover funds |

### First Light Series

| Operation | Recovery | Countries | I-GRIP Role |
|-----------|---------|-----------|-------------|
| [[operation-first-light-2024]] | USD 257M | 61 | Rapid interception of online scam proceeds |

### Notable Recoveries

- **HAECHI V (2024):** USD 400M+ intercepted across 40 countries, including a single Singaporean BEC case recovering USD 42.3M
- **HAECHI VI (2025):** USD 439M recovered; a Korea-UAE sub-operation used I-GRIP to intercept voice phishing proceeds routed through UAE bank accounts
- **First Light 2024:** USD 257M in assets seized/frozen across 61 countries

## Advantages

1. **Speed:** Hours instead of months — critical for catching funds in transit
2. **Global reach:** Available to all 196 INTERPOL member countries (in principle)
3. **Existing infrastructure:** Leverages the already-deployed I-24/7 network and NCB structure
4. **No treaty requirement:** Operates on domestic authority, not requiring a bilateral treaty between the specific countries
5. **Scalable:** Can handle high volumes during major operations
6. **Proven results:** Hundreds of millions of dollars recovered through HAECHI and First Light operations

## Limitations

1. **Time sensitivity:** Effectiveness drops sharply after 24-72 hours as funds are moved or withdrawn
2. **Banking system dependency:** Requires cooperative financial institutions; effectiveness varies by country
3. **Fiat currency only:** Does not cover cryptocurrency, which is increasingly used in cybercrime money laundering
4. **No formal legal authority:** I-GRIP is a coordination mechanism, not a legal instrument; domestic authority must exist
5. **Uneven coverage:** Not all INTERPOL NCBs have integrated I-GRIP workflows or maintain 24/7 financial crime response capacity
6. **Follow-up burden:** Rapid freeze is only the first step; formal MLA is still required for asset recovery, repatriation, and evidentiary use
7. **Jurisdictional limits:** Some countries' banking secrecy laws may limit the ability to freeze on an emergency basis

## Notable Uses

### Korea-UAE I-GRIP Sub-Operation (HAECHI VI, 2025)

A particularly notable use case: Korean voice phishing victims' funds were traced to UAE bank accounts. The Korean NCB ([[knpa-cyber-bureau]]) initiated an I-GRIP request through INTERPOL, and UAE authorities froze the accounts within days. This cross-continental interception demonstrates I-GRIP's value when traditional bilateral channels would have been too slow.

### Singaporean BEC Recovery (HAECHI V, 2024)

A Singapore-based company lost USD 42.3 million to a BEC attack. Through I-GRIP coordination, funds were traced and a significant portion recovered across multiple jurisdictions within days of the fraud being detected.

## Comparison with Alternatives

| Feature | I-GRIP | MLAT Asset Freeze | 24/7 Network |
|---------|--------|-------------------|--------------|
| Speed | Hours-days | 6-18 months | Hours (preservation only) |
| Scope | Bank account freeze | Full asset seizure | Data preservation |
| Legal authority | Domestic | Treaty-based | Budapest Convention |
| Follow-up needed | Yes (MLA) | No (self-sufficient) | Yes (MLA) |
| Crypto coverage | No | Possible | No |
| Global reach | 196 countries | Treaty partners only | 70+ countries |

## Korean Usage (한국의 활용)

### Lead Role in HAECHI

South Korea ([[knpa-cyber-bureau]]) has been a **driving force** behind I-GRIP development and deployment through the HAECHI operations, which Korea co-leads with INTERPOL:

- **HAECHI IV (2023):** USD 300M seized, 34 countries
- **HAECHI V (2024):** USD 400M+ seized, 40 countries
- **HAECHI VI (2025):** USD 439M recovered, 40 countries

Korea's *high IC capacity* and advanced financial monitoring systems make it a particularly effective I-GRIP user.

### Korea-UAE Partnership

The Korea-UAE I-GRIP sub-operation during HAECHI VI demonstrates Korea's ability to leverage I-GRIP for **bilateral cross-border recovery** within INTERPOL's multilateral framework.

### Domestic Legal Basis

Korean authorities can initiate I-GRIP requests based on:
- 범죄수익 은닉의 규제 및 처벌 등에 관한 법률 (Act on Regulation and Punishment of Criminal Proceeds Concealment)
- 전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법 (Special Act on Prevention of Telecommunications Financial Fraud and Refund of Damages)
- 국제형사사법 공조법 (International Criminal Justice Mutual Assistance Act)

### Capacity

Korean financial institutions are *highly likely* among the most responsive to LEA freeze requests due to well-established cooperation frameworks between the Korea Financial Intelligence Unit (KoFIU, 금융정보분석원) and law enforcement.

## Contradictions & Open Questions

1. **Cryptocurrency gap:** How will I-GRIP adapt to address cryptocurrency-based money laundering? Current capability is limited to traditional banking channels.
2. **Success rate:** What percentage of I-GRIP requests result in successful fund recovery? Aggregate statistics are not publicly available beyond operation-level announcements.
3. **Permanent recovery vs. temporary freeze:** What proportion of I-GRIP-frozen funds are eventually repatriated to victims versus released due to legal insufficiency?
4. **Coverage gaps:** Which INTERPOL member countries lack effective I-GRIP participation? No public assessment exists.
5. **Double-counting:** Are recovery figures in HAECHI and First Light announcements deduplicated? The same funds could potentially be counted in multiple operations.
