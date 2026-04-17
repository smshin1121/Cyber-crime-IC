---
type: case
title: "United States v. Dariy Pankov (xDedic / NLBrute)"
case_number: "M.D. Fla. xDedic-related prosecution"
jurisdiction: "U.S. District Court, Middle District of Florida"
jurisdiction_country: "[[united-states]]"
case_type: "prosecution"
status: "sentenced"
crime_charged:
  - "[[malware-ic]]"
  - "[[cybercrime-forum-ic]]"
defendants:
  - name: "Dariy Pankov"
    nationality: "Russian"
    status: "sentenced"
    sentence: "60 months"
    location_at_arrest: "Republic of Georgia"
related_operation: "[[xdedic-marketplace-takedown]]"
ic_elements:
  mlat_requests:
    - "Georgia"
  extradition: "Pankov was arrested in Georgia and extradited to the United States."
  evidence_from_abroad:
    - "Georgia"
    - "Belgium"
    - "Ukraine"
  foreign_arrests:
    - "Georgia"
  asset_freezing:
    - "USD 358,437 forfeiture sought"
cooperating_agencies:
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
  - "[[office-of-international-affairs]]"
legal_frameworks_invoked:
  - "[[computer-fraud-and-abuse-act]]"
  - "[[access-device-fraud]]"
mechanisms_used:
  - "[[mutual-legal-assistance]]"
  - "[[extradition-request]]"
key_legal_issues:
  - "[[data-sovereignty]]"
  - "[[jurisdictional-conflicts]]"
precedent_value: "High - the case expands xDedic beyond marketplace administration by showing how a malware supplier feeding credentials into the market could be extradited and sentenced in the same enforcement ecosystem."
source_count: 1
sources:
  - "[[2023-02-22_mdfl_pankov-xdedic-extradition]]"
created: 2026-04-17
updated: 2026-04-17
---

## Summary

United States v. Pankov is an xDedic-related prosecution focused on a major seller-side actor rather than a marketplace administrator or buyer. That makes it one of the more analytically useful cases in the xDedic cluster.

## Facts

DOJ alleged that Pankov developed `NLBrute`, malware capable of decrypting login credentials and compromising protected computers around the world. He allegedly used the tool to obtain tens of thousands of credentials and sold those credentials, including through the xDedic Marketplace, earning more than USD 358,000 in proceeds.

Unlike the core administrator cases, this prosecution shows how the xDedic ecosystem depended on upstream malware-enabled credential supply.

## International Cooperation Elements

### Evidence Gathering

The prosecution sits within the same broad xDedic investigation that involved Belgium, Ukraine, Europol, and other foreign partners. Even where the Pankov case is more individualized, the evidence picture is still inherently multinational.

### Arrest and Extradition

Pankov was taken into custody in the Republic of Georgia on 4 October 2022 and extradited to the United States. DOJ later stated that he pleaded guilty and was sentenced to 60 months in prison.

### Asset Recovery

The indictment notified Pankov that the United States sought forfeiture of USD 358,437, alleged to be traceable to the offense proceeds.

## Legal Analysis

### Jurisdiction

The Middle District of Florida asserted jurisdiction because the xDedic ecosystem sold unauthorized access devices and facilitated fraud affecting U.S. victims and infrastructure, including Florida-linked victims.

### Key Legal Issues

- **Supplier-side cybercrime liability:** The case shows that providing credential-harvesting malware can be prosecuted as part of a broader marketplace ecosystem even when the defendant is not the platform operator.
- **Marketplace-enabled fraud chain:** It also illustrates how malware development, credential theft, and criminal resale markets can be treated as one integrated criminal enterprise.

### Precedent Value

The case has *high* value because it captures the supply chain behind access marketplaces and shows that extradition can reach not only admins but also key technical enablers.

## Proceedings Timeline

| Date | Event |
|------|-------|
| Pre-2019 | Pankov allegedly develops and uses NLBrute in the xDedic ecosystem |
| 2019-01 | xDedic infrastructure seized |
| 2022-10-04 | Pankov arrested in Georgia |
| 2023-02-22 | DOJ announces extradition to the United States |
| 2023-09-14 | DOJ announces guilty plea |
| 2024-01-04 | DOJ roundup lists 60-month sentence |

## Cooperation Effectiveness

The case suggests that the xDedic operation achieved more than site takedown. It reached a technical enabler in a third country, secured extradition, and converted that into conviction and sentence.

## Korean Relevance

No South Korean role is identified. The case remains relevant because access-broker ecosystems and brute-force tooling often underpin attacks against globally exposed RDP and enterprise infrastructure, including in Asia.

## Contradictions & Open Questions

1. The public source does not provide the full case number in the extradition release.
2. The exact overlap between Pankov's credential inventory and xDedic's total listings is not quantified.
3. Public materials do not fully describe which jurisdictions hosted the most affected systems.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | Russian Malware Developer Arrested and Extradited to the United States | DOJ M.D. Fla. | 2023-02-22 | https://www.justice.gov/usao-mdfl/pr/russian-malware-developer-arrested-and-extradited-united-states |
