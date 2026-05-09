---
type: case
title: "United States v. Jalili, Aghamiri, and Balaghi (IRGC Hack-and-Leak 2024)"
case_number: "Sealed indictment unsealed 2024-09-27 (D.D.C.)"
jurisdiction: "U.S. District Court for the District of Columbia"
jurisdiction_country: "[[united-states]]"
jurisdictions:
  - "[[united-states]]"
  - "[[iran]]"
case_type: prosecution
status: indicted
crime_charged:
  - "[[hacking-ic]]"
  - "[[identity-theft]]"
defendants:
  - name: "Masoud Jalili"
    nationality: Iranian
    age: 36
    affiliation: "Islamic Revolutionary Guard Corps (IRGC) employee"
    status: "indicted-fugitive (resides in Iran); separately designated by US Treasury OFAC under E.O. 13694 (as amended) and E.O. 13848 on 2024-09-27"
    sentence: ""
    location_at_arrest: "Not arrested — believed to reside in Iran"
  - name: "Seyyed Ali Aghamiri"
    nationality: Iranian
    age: 34
    affiliation: "Islamic Revolutionary Guard Corps (IRGC) employee"
    status: "indicted-fugitive (resides in Iran)"
    sentence: ""
    location_at_arrest: "Not arrested — believed to reside in Iran"
  - name: "Yaser Balaghi"
    nationality: Iranian
    age: 37
    affiliation: "Islamic Revolutionary Guard Corps (IRGC) employee"
    status: "indicted-fugitive (resides in Iran)"
    sentence: ""
    location_at_arrest: "Not arrested — believed to reside in Iran"
related_operation: ""
ic_elements:
  mlat_requests: []
  extradition: "No extradition treaty with Iran; defendants reside in Iran. Custodial enforcement is *highly unlikely* in the near term and the U.S. response is built on indictment, sanctions designation, and Rewards for Justice."
  evidence_from_abroad: []
  foreign_arrests: []
  asset_freezing:
    - "United States — Treasury OFAC designation of Masoud Jalili pursuant to E.O. 13694 (as amended) and E.O. 13848 on 2024-09-27 freezes any U.S.-jurisdiction property of the designated person and prohibits U.S. persons from dealings."
cooperating_agencies:
  - "[[fbi]]"
  - "[[fbi-cyber-division]]"
  - "[[us-doj]]"
legal_frameworks_invoked: []
mechanisms_used:
  - "[[informal-cooperation]]"
key_legal_issues:
  - "[[extraterritorial-jurisdiction]]"
  - "Conspiracy framework (commonly 18 U.S.C. § 371) used to capture the cross-border tradecraft as a single charged agreement rather than discrete intrusions."
  - "Computer Fraud and Abuse Act (commonly 18 U.S.C. § 1030) extraterritorial application to spearphishing of U.S. persons from Iran-based infrastructure."
  - "Aggravated identity theft (commonly 18 U.S.C. § 1028A) — eight counts — used to convert credential-harvesting into mandatory-minimum exposure."
  - "Wire fraud (commonly 18 U.S.C. § 1343) — eight counts — and the false-domain-registration wire fraud variant, attaching the spoofed-login-page tradecraft."
  - "Material support to a designated foreign terrorist organization (commonly 18 U.S.C. § 2339B) — overlay of counterterrorism statute on cyber conduct because IRGC is FTO-designated."
  - "Election-interference framing as direct assault on U.S. democratic processes (per AAG Olsen)."
  - "IEEPA / E.O. 13694 (as amended) and E.O. 13848 sanctions overlap — Jalili individually designated by OFAC the same day, layering sanctions enforcement on top of criminal indictment."
precedent_value: "Medium-high. The case is *likely* to be cited as a template for stacking criminal indictment, OFAC sanctions, and Rewards for Justice into a coordinated single-day denial-and-deterrence action against state-directed election-interference cyber actors. Custodial precedent value is *unlikely* to develop unless a defendant travels to a cooperating jurisdiction."
source_count: 1
sources:
  - "[[2024-09-27_justice-gov_three-irgc-cyber-actors-indicted-hack-and-leak-2024-election]]"
created: 2026-05-09
updated: 2026-05-09
---
## Summary

United States v. Jalili, Aghamiri, and Balaghi is the U.S. District Court for the District of Columbia prosecution unsealed on 27 September 2024 charging three Iranian nationals — all employees of the Islamic Revolutionary Guard Corps (IRGC) — with a multi-year spearphishing and social-engineering campaign culminating in a June 2024 hack-and-leak operation against a U.S. presidential campaign. It is *highly likely* one of the clearest U.S. examples of a "full-stack" denial-and-deterrence response to state-directed election-interference cyber activity: the indictment was announced the same day as a State Department Rewards for Justice offer of up to USD 10 million and a Treasury OFAC sanctions designation of defendant Jalili.

## Facts

According to the DOJ release, beginning in or around January 2020 the three defendants, working on behalf of the IRGC, conducted a wide-ranging hacking campaign using spearphishing and social engineering against U.S. government officials (current and former), members of the media, NGOs, and individuals associated with U.S. political campaigns. Tradecraft included the use of VPNs and VPS infrastructure to obscure location, fraudulent email accounts in the names of prominent U.S. persons and international institutions, spoofed login pages to harvest credentials, spearphishing from compromised victim accounts, and social-engineering capture of multi-factor authentication and recovery codes.

In May–June 2024 the conspirators successfully compromised accounts of individuals associated with U.S. Presidential Campaign 1 and exfiltrated non-public campaign material. Beginning in June 2024 they conducted a "hack-and-leak" operation, sharing stolen material with members of the U.S. media and with individuals associated with U.S. Presidential Campaign 2. Per the DOJ release, the conduct is part of Iran's continuing effort to "stoke discord, erode confidence in the U.S. electoral process, and unlawfully acquire information relating to current and former U.S. officials that could be used to advance the malign activities of the IRGC, including ongoing efforts to avenge the death of Qasem Soleimani."

## International Cooperation Elements

### Evidence Gathering

No formal mutual-legal-assistance partner is identified in the release. Iran is not a party to the Council of Europe's Budapest Convention and the United States has no extradition treaty with Iran, so the case is *almost certainly* built on U.S.-side technical evidence: provider records, infrastructure attribution, and victim-side digital evidence collected through domestic legal process. The investigating offices identified by DOJ — FBI Washington Field Office (lead), FBI Cyber Division, FBI Springfield Field Office, and FBI Minneapolis Field Office — reflect U.S. domestic geographic distribution of the victims rather than international cooperation.

### Arrest and Extradition

All three defendants are believed to reside in Iran. Custodial enforcement is *highly unlikely* in the near term. The U.S. response substitutes (1) public attribution through indictment, (2) financial denial through Treasury OFAC designation of defendant Jalili under E.O. 13694 (as amended) and E.O. 13848, and (3) a Department of State Rewards for Justice offer of up to USD 10 million for information leading to identification or location of the subjects or associated IRGC election-interference activity.

### Asset Recovery

No criminal forfeiture is documented in the release. The 2024-09-27 Treasury OFAC designation of Masoud Jalili functions as the principal financial-pressure mechanism, freezing any U.S.-jurisdiction property of the designated person and prohibiting U.S. persons from dealings.

## Legal Analysis

### Jurisdiction

U.S. jurisdiction is *almost certainly* grounded in (a) the targeting of U.S. persons, (b) use of U.S.-located computer systems and provider services in furtherance of the conduct, and (c) the inclusion of a material-support count for a foreign terrorist organization, which has explicit extraterritorial reach. The case is a routine fit for [[extraterritorial-jurisdiction]] application of the Computer Fraud and Abuse Act and the federal wire-fraud statute.

### Key Legal Issues

- **Conspiracy as the governing framework.** Charging the multi-year tradecraft chain as a single conspiracy is *likely* important because it lets DOJ aggregate spearphishing, credential-harvesting, infrastructure registration, and the June 2024 leak distribution into one charged agreement.
- **Statute stacking.** CFAA + wire fraud + aggravated identity theft + material support to an FTO is a statute stack that *likely* maximises both deterrent messaging and exposure if any defendant ever enters U.S. or allied custody.
- **Election-interference framing.** Per AAG Olsen, the conduct is framed as a "direct assault on the integrity of our democratic processes." That framing is *likely* to recur in future state-actor election-interference indictments and *likely* shapes the OFAC E.O. 13848 designation pathway.
- **IEEPA / sanctions overlap.** OFAC's same-day designation of Jalili under E.O. 13694 (as amended) and E.O. 13848 is grounded in the IEEPA authority underlying both executive orders. Sanctions designation runs in parallel to, not in place of, the criminal indictment, which is the "full-stack" pattern increasingly used against state-directed cyber actors.
- **Material support overlay.** Charging material support to a designated FTO (the IRGC) is *likely* one of the more novel features of this case versus purely financially motivated cyber prosecutions.

### Precedent Value

*Medium-high.* The case is *likely* to be cited as a template for coordinating indictment, sanctions designation, and Rewards for Justice into a single-day denial-and-deterrence package. Its custodial precedent value is *unlikely* to develop unless a defendant travels to a jurisdiction willing to extradite to the United States, which is *highly unlikely* for serving IRGC personnel.

## Proceedings Timeline

| Date | Event |
|------|-------|
| ~2020-01 | Per DOJ, conspiracy commences; spearphishing and social-engineering campaign begins. |
| 2024-05 to 2024-06 | Successful compromise of accounts associated with U.S. Presidential Campaign 1; non-public campaign material exfiltrated. |
| 2024-06 | Hack-and-leak distribution to U.S. media and to individuals associated with U.S. Presidential Campaign 2 begins. |
| 2024-09-27 | Indictment unsealed in D.D.C.; State Department Rewards for Justice offers up to USD 10M; Treasury OFAC designates Masoud Jalili under E.O. 13694 (as amended) and E.O. 13848. |

## Cooperation Effectiveness

The case is *likely* effective as a public-attribution and financial-denial tool but *highly unlikely* to produce custody of the named defendants. That asymmetry is the central international-cooperation lesson: when the suspect state is not a treaty partner and shelters the actors, U.S. prosecutors substitute coordinated multi-instrument response (indictment + OFAC + Rewards for Justice) for the custodial outcome they would normally pursue. The case is *likely* to be useful for partner states as a public attribution they can rely on for their own administrative measures, even without a formal mutual-legal-assistance vehicle.

## Korean Relevance (한국 관련성)

South Korea is not identified as a participant or victim in this matter. The case is still *likely* relevant to Korean practice in two ways. First, ROK officials and political figures have been targeted by state-directed spearphishing tradecraft of the same family in recent years, so the U.S. charging template is *likely* useful as a comparative reference for how Korean prosecutors might frame analogous cross-border state-actor intrusion conduct under [[extraterritorial-jurisdiction]] principles. Second, the "indictment + sanctions + reward" stack is *likely* to inform how Korean agencies coordinate with allied financial-sanctions authorities when custodial cooperation is unavailable.

## Contradictions & Open Questions

1. The release does not identify Campaign 1 or Campaign 2 by name; secondary reporting *likely* identifies Campaign 1 as the Trump campaign and Campaign 2 as another presidential campaign, but the DOJ release itself uses neutral labels.
2. The release describes charges in narrative form; the precise count structure, statute citations, and per-count maxima above are *highly likely* the conventional citations for the conduct described, but the unsealed indictment text is the controlling document.
3. The release does not document any specific MLAT request, foreign arrest, or evidence transfer, so the international-cooperation footprint of the case is *almost certainly* asymmetric: U.S.-built evidence, no foreign-state assistance.
4. Whether OFAC will designate Aghamiri and Balaghi in subsequent tranches is not addressed in the 2024-09-27 release.

## References

| # | Source | Publisher | Date | URL |
|---|--------|-----------|------|-----|
| 1 | [[2024-09-27_justice-gov_three-irgc-cyber-actors-indicted-hack-and-leak-2024-election\|Three IRGC Cyber Actors Indicted for 'Hack-and-Leak' Operation Designed to Influence the 2024 U.S. Presidential Election]] | US DOJ (OPA) | 2024-09-27 | https://www.justice.gov/archives/opa/pr/three-irgc-cyber-actors-indicted-hack-and-leak-operation-designed-influence-2024-us |
