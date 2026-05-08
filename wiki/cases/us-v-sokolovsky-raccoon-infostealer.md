---
type: case
title: "United States v. Mark Sokolovsky (Raccoon Infostealer)"
case_number: "Western District of Texas, Austin Division (specific docket number not enumerated in cited tier-1 source)"
jurisdiction: "Western District of Texas (Austin Division) — US federal prosecution; arrest jurisdiction: Netherlands"
jurisdiction_country: "[[united-states]]"
jurisdictions:
  - "[[united-states]]"
  - "[[netherlands]]"
  - "[[italy]]"
  - "[[ukraine]]"
case_type: prosecution
status: sentenced
crime_charged:
  - "[[malware-ic]]"
  - "[[online-fraud-ic]]"
  - "[[money-laundering-ic]]"
defendants:
  - name: "Mark Sokolovsky (alias Photix; raccoonstealer; black21jack77777)"
    nationality: "Ukraine"
    status: "sentenced (2024-12-18, 60 months)"
    sentence: "60 months in federal prison; plea on one count of conspiracy to commit computer intrusion (October 2024); forfeiture USD 23,975; restitution at least USD 910,844.61"
    location_at_arrest: "Netherlands (March 2022, arrested by Dutch authorities)"
related_operation: ""
ic_elements:
  mlat_requests: []
  extradition: "US-Netherlands extradition coordinated by DOJ (cooperating partner: Netherlands Ministry of Justice / Public Prosecution Service); arrest March 2022 by Dutch authorities, transfer to US custody February 2024 (24-month gap during contested extradition appeal)"
  evidence_from_abroad:
    - "[[netherlands]]"
    - "[[italy]]"
  foreign_arrests:
    - "[[netherlands]]"
  asset_freezing: []
cooperating_agencies:
  - "[[fbi]]"
  - "[[us-doj]]"
legal_frameworks_invoked:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
mechanisms_used:
  - "[[extradition]]"
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[malware-ic]]"
  - "[[extradition]]"
precedent_value: "First wiki record explicitly capturing a coordinated arrest-of-operator (Netherlands, March 2022) + concurrent multi-country infrastructure dismantle (FBI + Italy + Netherlands) for a malware-as-a-service operation, followed by ~24-month contested-extradition pathway (March 2022 arrest → February 2024 US custody) and ~10-month plea-to-sentencing pathway (October 2024 plea → December 2024 sentence). The 52M+ compromised credentials place Raccoon Infostealer among the larger MaaS infrastructure takedowns by absolute scale."
source_count: 1
sources:
  - "[[2024-12-18_doj-wdtx_ukrainian-national-sentenced-raccoon-infostealer]]"
created: 2026-05-09
updated: 2026-05-09
summary: "United States v. Mark Sokolovsky is the WDTX prosecution of a Ukrainian national Raccoon Infostealer operator. Arrested by Dutch authorities in March 2022 concurrent with an FBI + Italy + Netherlands infrastructure dismantle that took the Raccoon Infostealer offline; extradited from the Netherlands to the US in February 2024; pleaded guilty in October 2024 to one count of conspiracy to commit computer intrusion; sentenced 2024-12-18 to 60 months federal prison plus USD 23,975 forfeiture and at least USD 910,844.61 restitution. Raccoon Infostealer was a malware-as-a-service operation leased at ~USD 200/month in cryptocurrency that compromised 52M+ user credentials."
---
## Summary

On **2024-12-18**, the **US Attorney's Office for the Western District of Texas** (Austin Division) announced that **Mark Sokolovsky**, age 28, a Ukrainian national, was sentenced to **60 months in federal prison** on one count of **conspiracy to commit computer intrusion**, plus forfeiture of **USD 23,975** and restitution of at least **USD 910,844.61**, for operating the **Raccoon Infostealer** malware-as-a-service. Sokolovsky was arrested by **Dutch authorities** in March 2022 concurrent with an **FBI + Italy + Netherlands** dismantle of the Raccoon Infostealer digital infrastructure; extradited from the **Netherlands** in **February 2024**; and pleaded guilty in October 2024.

## Facts

The Raccoon Infostealer was a **malware-as-a-service (MaaS)** operation: individuals who deployed the malware to steal data from victims **leased access for approximately USD 200 per month**, paid for in cryptocurrency. Customers used **email phishing** ruses to install the malware on victim computers, after which it stole **log-in credentials, financial information, and other personal records**. The stolen data was used to commit financial crimes or sold to others on cybercrime forums. According to the FBI San Antonio field office, Raccoon Infostealer was responsible for compromising **more than 52 million user credentials**, used in furtherance of fraud, identity theft, and ransomware attacks affecting millions of victims worldwide.

## International Cooperation Elements

| Element | Detail |
|---|---|
| Foreign arrest | Netherlands, March 2022 (Dutch authorities) |
| Concurrent infrastructure dismantle | March 2022 — joint FBI + Italy + Netherlands action took the Raccoon Infostealer infrastructure offline |
| Custody-transfer route | Netherlands → US custody (February 2024) after Sokolovsky's contested extradition appeal |
| Extradition channel | DOJ (USAO-WDTX) coordinated with Netherlands judiciary |
| Defendant nationality | Ukraine |
| Cooperating states explicitly named | United States, Netherlands, Italy |

## Legal Analysis

### Jurisdiction

US federal jurisdiction in the Western District of Texas (Austin Division) attached through the conspiracy to commit computer intrusion, the underlying victim cohort being US persons among the 52M+ compromised credential-holders. Defendant was extradited from the Netherlands following an appeal of the September 2022 Amsterdam District Court extradition decision (referenced in earlier DOJ filings). Italy was a co-action party in the March 2022 infrastructure dismantle but not the arrest jurisdiction.

### Key Legal Issues

- **Conspiracy to commit computer intrusion** (18 U.S.C. § 371 / 1030(a) — final plea offence; lower-tier than the original indictment's slate of fraud, money laundering, and aggravated identity theft).
- **Contested extradition under US-Netherlands bilateral arrangements** — defendant's appeal contributed to the ~24-month gap between March 2022 arrest and February 2024 US-custody transfer.
- **Malware-as-a-service liability** — a structural prosecutorial theory in which the operator is held responsible for downstream criminal use by paying customers.

### Precedent Value

This is the first wiki-recorded prosecution of a malware-as-a-service operator with explicit FBI + Italy + Netherlands joint infrastructure-dismantle cooperation alongside the arrest. The 52M+ compromised credentials place Raccoon Infostealer among the larger MaaS infrastructure takedowns by absolute scale. The 24-month contested-extradition window from the Netherlands provides a comparison-point to other Schengen-region US-extradition cases tracked in the wiki ([[us-v-volkov-yanluowang-sentencing|Volkov / Italy ~12 months]]; [[us-v-deniss-zolotarjovs|Zolotarjovs / Georgia ~8 months]]; [[us-v-stryzhak-nefilim|Stryzhak / Spain]]).

## Proceedings Timeline

| Date | Event |
|---|---|
| 2022-03 | Sokolovsky arrested by Dutch authorities; FBI + Italy + Netherlands dismantle Raccoon Infostealer infrastructure |
| 2022-09 (background) | Amsterdam District Court grants extradition to the US (defendant appeals) |
| 2022-10-25 (background) | WDTX federal grand jury indictment unsealed (fraud, money laundering, aggravated identity theft) |
| 2024-02 | Sokolovsky extradited from the Netherlands to US custody |
| 2024-10 | Plea entered: one count of conspiracy to commit computer intrusion; agreed to forfeit USD 23,975 and pay at least USD 910,844.61 in restitution |
| 2024-12-18 | Sentenced to 60 months in federal prison (USAO-WDTX press release) |

## Cooperation Effectiveness

The case demonstrates a successful three-country IC pattern: (a) **Netherlands** as both the arrest jurisdiction and the extradition jurisdiction; (b) **Italy** as a co-action partner for infrastructure dismantle but not for arrest or extradition; (c) **United States** as the lead investigator (FBI Austin Cyber Task Force) and ultimate prosecution venue. The 24-month arrest-to-extradition window — partly attributable to the defendant's appeal of the September 2022 Amsterdam District Court extradition decision — is longer than comparable Schengen-region pathways but still effective. The simultaneous arrest-of-operator + infrastructure-dismantle is a discrete IC mechanism class that complements the traditional sequential indictment → arrest → seizure pattern.

## Korean Relevance (한국 관련성)

South Korea is not named in the cited DOJ release as a victim, source, or cooperation jurisdiction. The case is recorded in the wiki for the malware-as-a-service prosecution model and the FBI + Italy + Netherlands joint infrastructure-dismantle mechanism class. Korean exposure to Raccoon Infostealer victim-credential cohorts is *likely* present given the global 52M+ credential scale but is not enumerated in this source.

## Contradictions & Open Questions

- The cited release does not enumerate the specific Italian or Dutch agencies that participated in the March 2022 infrastructure dismantle (only "the FBI and law enforcement partners in Italy and the Netherlands").
- The specific WDTX docket number is not enumerated in the cited release.
- Whether any non-US-jurisdiction victims among the 52M+ credential cohort received restitution is not specified.
- The extent of Korean (or other Asian) victim exposure to Raccoon Infostealer is not enumerated.
- The Italian arrest / extradition track for any Italy-resident customer of the MaaS service is not described in this release; the Italian role appears confined to the infrastructure dismantle.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2024-12-18_doj-wdtx_ukrainian-national-sentenced-raccoon-infostealer\|Ukrainian National Sentenced to Federal Prison in 'Raccoon Infostealer' Cybercrime Case]] | USAO-WDTX | 2024-12-18 | https://www.justice.gov/usao-wdtx/pr/ukrainian-national-sentenced-federal-prison-raccoon-infostealer-cybercrime-case |
