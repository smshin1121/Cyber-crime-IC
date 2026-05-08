---
type: case
title: "United States v. Xu Zewei et al. (HAFNIUM / COVID-19 research / PRC MSS contract hacker, extradited from Italy)"
case_number: "S.D. Texas (Houston Division) — specific docket number not enumerated in cited tier-1 source; press release 26-404"
jurisdiction: "Southern District of Texas (Houston Division) — US federal prosecution; arrest jurisdiction: Italy (Milan Malpensa airport, July 2025)"
jurisdiction_country: "[[united-states]]"
jurisdictions:
  - "[[united-states]]"
  - "[[italy]]"
  - "[[china]]"
case_type: prosecution
status: indicted
crime_charged:
  - "[[hacking-ic]]"
  - "[[malware-ic]]"
defendants:
  - name: "Xu Zewei (徐泽伟)"
    nationality: "People's Republic of China"
    status: "extradited from Italy weekend of 2026-04-25 to 2026-04-26; first US court appearance Houston (S.D. Texas) on 2026-04-27"
    sentence: "n/a (pre-trial)"
    location_at_arrest: "Italy — Milan Malpensa airport, July 2025"
  - name: "Zhang Yu (张宇)"
    nationality: "People's Republic of China"
    status: "at large"
    sentence: "n/a"
    location_at_arrest: "n/a (not in custody)"
related_operation: ""
ic_elements:
  mlat_requests: []
  extradition: "Italy → US extradition of Xu Zewei coordinated by DOJ Office of International Affairs (OIA); Italian National Police — Cyber Division (Polizia Postale) credited by FBI as the partnership-leading agency for the Milan arrest and extradition; arrest July 2025; extradition weekend of 2026-04-25 to 2026-04-26 (~9 months between arrest and extradition)"
  evidence_from_abroad:
    - "[[italy]]"
  foreign_arrests:
    - "[[italy]]"
  asset_freezing: []
cooperating_agencies:
  - "[[fbi]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
legal_frameworks_invoked:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[hacking-ic]]"
  - "[[extradition]]"
precedent_value: "First wiki record of an Italy-as-extradition-source for a Chinese state-sponsored cyber actor — characterized as 'rare' in third-party reporting. Establishes a Schengen-region apprehension + extradition pathway for PRC contract hackers analogous to the Schengen-region pathways for Russian-organisation ransomware actors recorded in [[us-v-deniss-zolotarjovs|Zolotarjovs / Georgia]], [[us-v-stryzhak-nefilim|Stryzhak / Spain]], and [[us-v-vardanyan-avetisyan-ryuk-ransomware|Vardanyan / Ukraine + Avetisyan / France-pending]]. Adds Xu Zewei + Zhang Yu (Powerock contractors directed by PRC MSS Shanghai State Security Bureau) to the wiki's PRC enabling-company prosecution corpus alongside [[us-v-wu-haibo-isoon|US v. Wu Haibo (iSoon)]] and [[isoon-apt27-indictment|iSoon APT27 indictment]]."
source_count: 1
sources:
  - "[[2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy]]"
created: 2026-05-09
updated: 2026-05-09
summary: "United States v. Xu Zewei et al. is the Southern District of Texas (Houston Division) prosecution of two PRC nationals — Xu Zewei (34, extradited from Italy 2026-04-25/26 after July 2025 arrest at Milan Malpensa airport) and Zhang Yu (44, at large) — under a 9-count indictment for computer intrusions between February 2020 and June 2021. The intrusions are alleged to have been directed by officers of the PRC Ministry of State Security's (MSS) Shanghai State Security Bureau (SSSB), with Xu working through Shanghai Powerock Network Co. Ltd. (Powerock), a PRC enabling company. Phase 1 (early 2020): COVID-19 research intrusions targeting US universities, immunologists, and virologists conducting COVID-19 vaccine/treatment/testing research. Phase 2 (late 2020 – early 2021): HAFNIUM Microsoft Exchange Server vulnerability exploitation campaign that compromised 12,700+ US organizations including a S.D. Texas university and a worldwide-offices law firm with offices in Washington, D.C.. Charges include wire fraud (max 20 years/count), unauthorized access to protected computers (max 5 years/count), intentional damage to a protected computer (max 10 years/count), and aggravated identity theft (max 2 years). Italy → US extradition coordinated by DOJ OIA + Italian National Police Cyber Division (Polizia Postale)."
---
## Summary

On **2026-04-27**, the US Department of Justice announced that **Xu Zewei (徐泽伟)**, age 34, a People's Republic of China national, had been extradited from Italy to the United States the weekend before and made his first US federal-court appearance in **Houston (S.D. Texas)** on a **9-count indictment** for computer intrusions between **February 2020 and June 2021**. Xu was arrested at **Milan Malpensa airport in July 2025** and extradited approximately 9 months later. His co-defendant, **Zhang Yu (张宇)**, age 44 and also a PRC national, **remains at large**.

According to court documents, officers of the PRC Ministry of State Security's (MSS) **Shanghai State Security Bureau (SSSB)** directed Xu's hacking. When Xu conducted the intrusions, he allegedly worked for **Shanghai Powerock Network Co. Ltd.** (Powerock), one of many PRC enabling companies that conducted hacking for the PRC government.

## Facts

### Phase 1 (early 2020): COVID-19 research intrusions

In early 2020, Xu and his co-conspirators **hacked and otherwise targeted U.S.-based universities, immunologists, and virologists conducting research into COVID-19 vaccines, treatment, and testing**. Xu reported his activities to SSSB officers who supervised and directed the hacking. For example:

- **2020-02-19**: Xu provided an SSSB officer with confirmation that he had compromised the network of a research university located in the **Southern District of Texas**.
- **2020-02-22**: The SSSB officer directed Xu to target and access specific email accounts (mailboxes) belonging to **virologists and immunologists** engaged in COVID-19 research for the university. Xu later confirmed for the SSSB officer that he acquired the contents of the researchers' mailboxes.

### Phase 2 (late 2020 — early 2021): HAFNIUM Microsoft Exchange campaign

Beginning in late 2020, Xu and his co-conspirators exploited certain vulnerabilities in **Microsoft Exchange Server**. Their exploitation was at the forefront of the massive campaign known publicly as **"HAFNIUM"**.

- **March 2021**: Microsoft publicly disclosed the intrusion campaign by state-sponsored hackers operating out of China.
- **2021-03-10**: FBI + CISA released a Joint Advisory on Compromise of Microsoft Exchange Server.
- **March 2021 (end)**: Hundreds of web shells remained on certain U.S.-based computers running Microsoft Exchange Server software.
- **April 2021**: DOJ announced a court-authorized operation to remediate hundreds of computers in the United States made vulnerable by HAFNIUM actors.
- **July 2021**: The United States and foreign partners attributed the HAFNIUM campaign to the **PRC's MSS**.

The indictment alleges HAFNIUM-attributed web shells installed by Xu and his co-conspirators were specific to HAFNIUM actors at the time. **HAFNIUM compromised 12,700+ U.S. organizations** in total. Among Xu's specific HAFNIUM victims: another university located in the Southern District of Texas, and **a law firm with offices worldwide**, including in Washington, D.C. Through unauthorized access to the law firm's network, Xu and his co-conspirators **stole information from mailboxes** and searched them using terms including **"Chinese sources," "MSS," and "HongKong"**.

### Coordination

Xu and Zhang worked together on the HAFNIUM intrusions, under the supervision and direction of SSSB officers. For example:

- **2021-01-30**: Xu confirmed to Zhang that he had compromised the other Texas university's network.
- **2021-02-28**: Xu updated a SSSB officer on his successful intrusions; the SSSB officer directed Xu to obtain a list of other successful intrusions from a second SSSB officer.

## International Cooperation Elements

| Element | Detail |
|---|---|
| Foreign arrest | Italy — Milan Malpensa airport, July 2025 |
| Custody-transfer route | Italy → US (weekend of 2026-04-25 to 2026-04-26) — approximately 9 months between arrest and extradition |
| Extradition channel | DOJ Office of International Affairs (OIA) + Italian National Police — Cyber Division (Polizia Postale) |
| FBI lead | Houston Field Office |
| Prosecutors | AUSA Mark McIntyre (S.D. Texas) + Deputy Chief Matthew Anzaldi (NSD National Security Cyber Section) |
| Defendant nationalities | China (Xu Zewei, Zhang Yu) |
| Cooperating states explicitly named | United States (lead), Italy |
| State-sponsor attribution | China (PRC Ministry of State Security — Shanghai State Security Bureau) |

## Legal Analysis

### Jurisdiction

US federal jurisdiction in the Southern District of Texas (Houston Division) attached through the Texas-based university victims (Phase 1 + Phase 2) and through the worldwide-offices law firm with offices in Washington, D.C. (Phase 2). Defendant Xu was extradited from Italy after his July 2025 arrest at Milan Malpensa.

### Charges

- **Conspiracy to commit wire fraud** (18 U.S.C. § 1349) — max 20 years.
- **Two counts of wire fraud** (18 U.S.C. § 1343) — max 20 years per count.
- **Conspiracy to cause damage to and obtain information by unauthorized access to protected computers, to commit wire fraud, and to commit identity theft** — max 5 years.
- **Two counts of obtaining information by unauthorized access to protected computers** — max 5 years per count.
- **Two counts of intentional damage to a protected computer** — max 10 years per count.
- **Aggravated identity theft** — max 2 years.

### Precedent Value

This is the first wiki record of an **Italy-as-extradition-source for a Chinese state-sponsored cyber actor** — characterised as "rare" in third-party reporting. The case adds Xu Zewei + Zhang Yu (Powerock contractors directed by PRC MSS Shanghai State Security Bureau) to the wiki's PRC enabling-company prosecution corpus alongside [[us-v-wu-haibo-isoon|US v. Wu Haibo (iSoon)]] and [[isoon-apt27-indictment|iSoon APT27 indictment]]. The Schengen-region apprehension + extradition pathway is structurally analogous to the [[us-v-deniss-zolotarjovs|Zolotarjovs / Georgia]], [[us-v-stryzhak-nefilim|Stryzhak / Spain]], and [[us-v-vardanyan-avetisyan-ryuk-ransomware|Vardanyan / Ukraine + Avetisyan / France-pending]] Schengen-region pathways for Russian-organisation ransomware actors.

## Proceedings Timeline

| Date | Event |
|---|---|
| Feb 2020 — June 2021 | Xu and Zhang's alleged hacking activity period |
| 2020-02-19 | Xu confirms compromise of S.D. Texas research university (COVID-19 research target) |
| 2020-02-22 | SSSB officer directs Xu to target virologist/immunologist mailboxes |
| 2021-01-30 | Xu confirms HAFNIUM compromise of another S.D. Texas university to Zhang |
| 2021-02-28 | Xu reports HAFNIUM intrusions to SSSB officer |
| 2021-03 | Microsoft publicly discloses HAFNIUM |
| 2021-03-10 | FBI + CISA Joint Advisory on Microsoft Exchange Server compromise |
| 2021-04 | DOJ court-authorized remediation operation on HAFNIUM-vulnerable US computers |
| 2021-07 | US + foreign partners attribute HAFNIUM to PRC MSS |
| (date not enumerated) | S.D. Texas federal grand jury indicts Xu Zewei + Zhang Yu (9-count indictment) |
| 2025-07 | Xu Zewei arrested at Milan Malpensa airport |
| 2026-04 | Italian extradition decision |
| 2026-04-25/26 | Xu extradited from Italy to US |
| 2026-04-27 | Xu's first US federal-court appearance in Houston; DOJ public announcement |

## Cooperation Effectiveness

The case demonstrates a successful US-Italy extradition pathway for a Chinese state-sponsored cyber actor — described as "rare" in third-party reporting. Italian National Police Cyber Division (Polizia Postale) is explicitly credited by FBI Cyber Division Assistant Director Brett Leatherman as the partnership-leading agency for the Milan arrest and extradition. DOJ OIA secured the formal extradition. The 9-month interval between July 2025 arrest and April 2026 extradition is comparable to other Schengen-region extradition timelines tracked in the wiki.

## Korean Relevance (한국 관련성)

South Korea is not named in the cited DOJ release as a victim, source, or cooperation jurisdiction. The case is recorded in the wiki for the Italy-as-extradition-source for a PRC state-sponsored cyber actor pattern, the PRC enabling-company architecture documentation, and the HAFNIUM Microsoft Exchange compromise scale (12,700+ US organisations). HAFNIUM's broader victim cohort *almost certainly* included Korean organisations given the global Microsoft Exchange installed base, but Korean victims are not enumerated in this release.

## Contradictions & Open Questions

- The cited release does not enumerate the specific names of the S.D. Texas universities or the worldwide-offices law firm victimized.
- The specific date of Xu's arrest at Milan Malpensa airport in July 2025 is not enumerated (only "July 2025").
- The specific date of the Italian extradition decision is not in the cited DOJ release (third-party reporting cites April 26, 2026).
- The status of Zhang Yu's at-large location is not specified.
- The specific HAFNIUM-attributed organisations beyond the S.D. Texas university and the worldwide-offices law firm are not enumerated (the 12,700+ figure is cumulative).
- Whether other co-conspirators beyond Xu and Zhang are charged is not enumerated.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2026-04-27_justice-gov_prolific-chinese-state-sponsored-contract-hacker-extradited-italy\|Prolific Chinese State-Sponsored Contract Hacker Extradited from Italy]] | US DOJ (OPA), Press Release 26-404 | 2026-04-27 | https://www.justice.gov/opa/pr/prolific-chinese-state-sponsored-contract-hacker-extradited-italy |
