---
type: case
title: "United States v. Buchanan, Urban, Elbadawy, Osiebo, Evans (Scattered Spider)"
case_number: "Press Release No. 24-289 (USAO-CDCA, 2024-11-20). Specific docket number not stated in the press release; indictment + companion complaint unsealed in the U.S. District Court for the Central District of California."
jurisdiction: "U.S. District Court for the Central District of California"
jurisdiction_country: "[[united-states]]"
jurisdictions:
  - "[[united-states]]"
  - "[[united-kingdom]]"
  - "[[spain]]"
case_type: prosecution
status: indicted
crime_charged:
  - "[[hacking-ic]]"
  - "[[identity-theft]]"
  - "[[online-fraud-ic]]"
defendants:
  - name: "Tyler Robert Buchanan (a/k/a 'Tylerb')"
    nationality: "British / United Kingdom national (Dundee, Scotland — per secondary reporting)"
    age: 22
    status: "Charged by federal criminal complaint in C.D. Cal. (unsealed 2024-11-20). Per secondary reporting, arrested by Spanish authorities in June 2024 attempting to board a flight at Palma de Mallorca to Italy; Spain-arrest fact NOT in DOJ release. Extradition status not announced in this release."
    location_at_arrest: "Spain (June 2024 — secondary reporting; not stated in DOJ release)"
  - name: "Ahmed Hossam Eldin Elbadawy (a/k/a 'AD')"
    nationality: "United States (resident of College Station, Texas)"
    age: 23
    status: "Charged by federal grand jury indictment (C.D. Cal., unsealed 2024-11-20)."
    location_at_arrest: "United States (Texas) — specific arrest details not in release"
  - name: "Noah Michael Urban (a/k/a 'Sosa', 'Elijah'; per secondary reporting also 'Kingbob')"
    nationality: "United States (resident of Palm Coast, Florida)"
    age: 20
    status: "Charged by federal grand jury indictment (C.D. Cal., unsealed 2024-11-20). Already faces and has pleaded not guilty to several fraud charges in a separate criminal case in M.D. Fla. (Jacksonville)."
    location_at_arrest: "United States (Florida) — already in U.S. custody on separate M.D. Fla. case"
  - name: "Evans Onyeaka Osiebo"
    nationality: "United States (resident of Dallas, Texas)"
    age: 20
    status: "Charged by federal grand jury indictment (C.D. Cal., unsealed 2024-11-20)."
    location_at_arrest: "United States (Texas) — specific arrest details not in release"
  - name: "Joel Martin Evans (a/k/a 'joeleoli')"
    nationality: "United States (resident of Jacksonville, North Carolina)"
    age: 25
    status: "Arrested by FBI in North Carolina on Tuesday 2024-11-19 (the day before unsealing). Charged by federal grand jury indictment (C.D. Cal., unsealed 2024-11-20). Initial appearance scheduled for 2024-11-20."
    location_at_arrest: "North Carolina, United States (2024-11-19)"
related_operation: ""
ic_elements:
  mlat_requests: []
  extradition: "Not announced in the DOJ press release. Buchanan, a UK national, was arrested in Spain in June 2024 (per secondary reporting); whether the United States has filed a formal extradition request to Spain (or to the United Kingdom) under the U.S.-Spain or U.S.-UK extradition treaties is not stated in the November 2024 release. Subsequent reporting (KrebsOnSecurity April 2025) indicates Buchanan was extradited to the United States in early 2025 — confirmation pending tier-1 source ingestion."
  evidence_from_abroad:
    - "United Kingdom / Scotland (per Police Scotland assistance named in release)"
  foreign_arrests:
    - "Spain (Buchanan, June 2024 — secondary reporting; not in DOJ release)"
  asset_freezing: []
cooperating_agencies:
  - "[[fbi]]"
  - "[[us-doj]]"
key_legal_issues:
  - "[[dual-criminality]]"
  - "[[extradition-practice]]"
  - "[[extraterritorial-jurisdiction]]"
precedent_value: "First U.S. multi-defendant federal indictment publicly charging members of the Scattered Spider / Octo Tempest / UNC3944 / 0ktapus social-engineering ecosystem (group attribution per secondary reporting; not asserted in the DOJ release itself). Demonstrates the **U.S.-domestic-indictment + UK-national-by-complaint + foreign-arrest-in-third-country (Spain)** prosecutorial pattern for transnational SMS-phishing-to-cryptocurrency-drain schemes. Sister cases [[us-v-jubair-scattered-spider-2025]] (D.N.J. complaint) and [[uk-jubair-flowers-tfl-cyber-attack-2025]] (UK NCA / Westminster Magistrates Court) extend the Scattered Spider prosecution chain."
source_count: 1
sources:
  - "[[2024-11-20_justice-gov_five-members-scattered-spider-charged-cybercrime-attacks]]"
created: 2026-05-09
updated: 2026-05-09
---

> [!info] Provisional case page (source_count = 1)
> Below the preferred publication threshold of source_count >= 5. Published as a provisional record because the DOJ-USAO-CDCA press release is a tier-1 primary source and the case has clear durable IC value: it is the first U.S. multi-defendant federal indictment charging individuals subsequently identified by all major secondary reporting as Scattered Spider members, and it sits at the head of a multi-year U.S. + UK Scattered Spider prosecution chain alongside [[us-v-jubair-scattered-spider-2025]] and [[uk-jubair-flowers-tfl-cyber-attack-2025]]. Should be promoted to a full case page once additional tier-1 filings (the actual indictment + complaint, any subsequent superseding indictment, the Spain extradition record, plea / verdict) are ingested.

> [!note] Group attribution caveat
> The DOJ press release does **not** use the name "Scattered Spider," "Octo Tempest," "UNC3944," or "0ktapus." The Scattered Spider attribution to these five defendants is sourced from secondary tier-2/3 reporting and is **highly likely** (80–95%) correct on the basis of (i) modus operandi (SMS-phishing → MFA bypass → cryptocurrency drains), (ii) named victim companies in secondary reporting (LastPass, MailChimp, Okta, T-Mobile, Twilio, MGM Resorts), and (iii) the September 2021 – April 2023 conduct period overlapping the publicly reported Scattered Spider campaign window. The attribution should be re-asserted with higher confidence once a tier-1 superseding indictment or DOJ release explicitly names the group.

## Summary

On **Wednesday, 20 November 2024**, the U.S. Attorney's Office for the Central District of California (USAO-CDCA) and the FBI Los Angeles Field Office unsealed (a) a **federal grand jury indictment** in the U.S. District Court for the Central District of California charging four U.S.-resident defendants — **Ahmed Hossam Eldin Elbadawy** (23, College Station TX), **Noah Michael Urban** (20, Palm Coast FL), **Evans Onyeaka Osiebo** (20, Dallas TX), and **Joel Martin Evans** (25, Jacksonville NC) — and (b) a companion **federal criminal complaint** in the same court charging UK national **Tyler Robert Buchanan** (22, of the United Kingdom). The four U.S.-defendants are charged by indictment with conspiracy to commit wire fraud (18 U.S.C. § 1349), conspiracy (18 U.S.C. § 371), and aggravated identity theft (18 U.S.C. § 1028A); Buchanan is charged by complaint with the same three offences plus substantive wire fraud (18 U.S.C. § 1343).

The DOJ release alleges that, from at least **September 2021 to April 2023**, the defendants conducted SMS-phishing ("smishing") attacks against employees of numerous victim companies, sending texts purporting to be from the victim company or a contracted IT / business-services supplier announcing imminent account deactivation and linking to phishing sites that harvested credentials and two-factor authentication responses. The defendants then used the stolen credentials to (i) access victim companies' computer systems and exfiltrate confidential work product, intellectual property, and personal identifying information; and (ii) drain individual cryptocurrency accounts and wallets of "millions of dollars' worth of virtual currency." U.S. Attorney Martin Estrada quantified intellectual-property and proprietary information losses at "tens of millions of dollars" and personal-information victims at "hundreds of thousands of individuals."

The release names **Police Scotland** as a foreign LE cooperator and identifies Joel Martin Evans's arrest by the FBI in North Carolina on Tuesday, 19 November 2024 — the only arrest event documented in the press release itself. The release does **not** name "Scattered Spider," does **not** mention Spain or Tyler Buchanan's arrest in Spain, and does **not** announce an extradition request. AUSAs Lauren Restrepo (CCIPS / Cyber and IP Crimes Section) and Sue J. Bai (Terrorism and Export Crimes Section) are prosecuting.

## Facts

### Conduct Period and Modus Operandi

- **Period charged**: ~September 2021 to April 2023.
- **Method**: Mass SMS ("smishing") campaigns targeting employees of victim companies. Texts impersonated the victim company itself or a contracted IT / business-services supplier, claimed accounts were about to be deactivated, and provided links to spoofed login pages. Victims who entered credentials sometimes also approved push-based two-factor authentication prompts, allowing the attackers to bypass MFA.
- **Post-credential-theft activity**: unauthorized access to corporate networks → exfiltration of work product, IP, and PII → use of stolen PII (combined with stolen data sets and other sources) to access individual cryptocurrency exchange accounts and wallets → drain of "millions of dollars' worth of virtual currency."
- **Scale (per DOJ release)**: "numerous" victim companies; "hundreds of thousands of individuals" with PII exposed; "tens of millions of dollars" of IP / proprietary information; "millions of dollars" of stolen cryptocurrency. The DOJ release does not give victim-by-victim figures.
- **Scale (per secondary reporting, **highly likely** 80–95% reliable but not asserted in this DOJ release)**: at least 45 victim companies; at least 29 cryptocurrency-victim individuals; ~USD 11 million stolen cryptocurrency. Named victim companies include LastPass, MailChimp, Okta, T-Mobile, Twilio (and 163+ Twilio downstream customers), and MGM Resorts.

### Charges

| Defendant | Count 1 | Count 2 | Count 3 | Count 4 (Buchanan only) |
|---|---|---|---|---|
| Elbadawy | Conspiracy to commit wire fraud (§ 1349) | Conspiracy (§ 371) | Aggravated identity theft (§ 1028A) | — |
| Urban | Conspiracy to commit wire fraud (§ 1349) | Conspiracy (§ 371) | Aggravated identity theft (§ 1028A) | — |
| Osiebo | Conspiracy to commit wire fraud (§ 1349) | Conspiracy (§ 371) | Aggravated identity theft (§ 1028A) | — |
| Evans | Conspiracy to commit wire fraud (§ 1349) | Conspiracy (§ 371) | Aggravated identity theft (§ 1028A) | — |
| Buchanan (by complaint) | Conspiracy to commit wire fraud | Conspiracy | Aggravated identity theft | Wire fraud (§ 1343) |

**Statutory maximum exposure (per DOJ release):**
- Conspiracy to commit wire fraud: up to 20 years.
- Conspiracy: up to 5 years.
- Aggravated identity theft: mandatory **2 years consecutive**.
- Wire fraud (Buchanan only): up to 20 years.
- **Total ceiling**: 27 years for U.S.-defendants (indictment); up to 47 years for Buchanan (complaint).

### Arrests Documented in the Release

- **Joel Martin Evans**: arrested by the FBI in North Carolina on **Tuesday, 19 November 2024** (the day before unsealing). Initial appearance scheduled for 2024-11-20.
- **Noah Michael Urban**: already in custody on a separate criminal case in the U.S. District Court for the Middle District of Florida (Jacksonville), where he has pleaded not guilty.
- **Elbadawy, Osiebo, Buchanan**: arrest details not specified in the DOJ release.

> [!warning] Spain arrest of Buchanan — secondary-source only
> Per all major secondary reporting (KrebsOnSecurity, Bloomberg, The Record, Bank Info Security, etc.) — but **not** mentioned in this DOJ press release — Tyler Buchanan was arrested by Spanish authorities in **June 2024 at Palma de Mallorca airport** while attempting to board a flight to Italy, on the basis of a U.S. arrest warrant. KrebsOnSecurity reporting from April 2025 indicates Buchanan was subsequently extradited to the United States. Both facts await tier-1 confirmation in the wiki (Spanish judicial decision; U.S. extradition / first-appearance docket entry).

## International Cooperation Elements

### Evidence Gathering

The DOJ release explicitly names two foreign / cross-border evidence-cooperation streams:

1. **Police Scotland** (United Kingdom — Scottish national police force). Named as a contributing agency. **Likely** (55–80%) reflects (i) Buchanan's reported residence ties to Dundee, Scotland and (ii) Scotland-side evidence collection on his communications, infrastructure, and cryptocurrency flows. The release does not specify the legal vehicle — formal MLAT, [[budapest-convention]] preservation/production order, or informal LE-to-LE channel.
2. **Spanish authorities** (not named in the DOJ release; documented in secondary reporting). **Highly likely** (80–95%) involved in Buchanan's June 2024 arrest at Palma de Mallorca airport on a U.S. warrant. Likely vehicle: U.S. provisional-arrest request under the U.S.-Spain extradition treaty (1970, with 1995 supplementary treaty); subsequent extradition proceedings before the Spanish Audiencia Nacional.

### Arrest and Extradition

- **Single domestic arrest documented**: Joel Martin Evans (FBI, North Carolina, 2024-11-19).
- **Pre-existing federal custody**: Noah Michael Urban (M.D. Fla., separate case).
- **Foreign arrest (per secondary reporting only)**: Tyler Buchanan (Spain, Palma de Mallorca, June 2024).
- **No extradition announcement in the DOJ release**. Per [[extradition-practice|extradition practice]], Buchanan's situation as a UK national arrested in Spain triggers a **U.S.-Spain bilateral extradition track** (rather than a U.S.-UK track), because the requested state is the state of detention, not nationality. Spain does not refuse extradition of foreign nationals, and the U.S.-Spain treaty does not include a "no extradition of own nationals" reservation that would block a UK-national subject; this case is therefore expected to proceed cleanly on dual-criminality + standard treaty grounds.
- **[[dual-criminality|Dual criminality]] readily satisfied** (>95%): SMS phishing, unauthorised access to computer systems, and credential theft are criminal under U.S. law (18 U.S.C. §§ 1030, 1343, 1349, 1028A) and Spanish law (Código Penal arts. 248 (estafa informática), 197 bis (acceso ilícito a sistemas informáticos), 264 (daños informáticos), 264 bis–ter), as well as UK law (Computer Misuse Act 1990, ss. 1, 3; Fraud Act 2006).

### Asset Recovery

- The DOJ release does **not** specify any cryptocurrency seizures, wallet seizures, or victim-restitution figures attributable to this case. Secondary reporting indicates Buchanan was alleged to have controlled wallets holding ~USD 27 million in Bitcoin at the time of his Spanish arrest; this is not asserted in the DOJ release and is recorded here only as an open-question fact.

## Legal Analysis

### Jurisdiction

- **U.S. extraterritorial jurisdiction over CFAA-adjacent wire-fraud-via-SMS conduct**: the case theory rests on U.S. wires (SMS messages routed through U.S. carriers; phishing sites hosted on U.S. infrastructure; cryptocurrency exchanges with U.S. operations). Wire fraud (18 U.S.C. § 1343) reaches any scheme using U.S. wires, regardless of the defendant's physical location at the time of the act. With at least four U.S.-resident co-conspirators and victim companies headquartered in or operating from the United States, U.S. jurisdiction over Buchanan's conduct is **almost certain** (>95%).
- **Venue (C.D. Cal.)**: not explicitly justified in the press release. **Likely** (55–80%) anchored on (i) at least one C.D. Cal.-based victim company in the indictment (LastPass and Okta have California ties; both are publicly named in secondary reporting), and/or (ii) the situs of the cryptocurrency exchange where the drained accounts were maintained.

### Key Legal Issues

- **Aggravated identity theft (18 U.S.C. § 1028A)**: charged against all five defendants. Carries a mandatory 2-year consecutive sentence on top of the predicate offence (here, wire-fraud conspiracy). Requires the government to prove that the identity used was an actual person's, not a fabricated one.
- **Conspiracy + substantive wire fraud (Buchanan only)**: the substantive wire-fraud count appears in the **complaint**, not the indictment, **likely** (55–80%) because (i) the complaint is the vehicle used to support the U.S. extradition request to Spain (where a complaint + sworn affidavit is sufficient) and (ii) a substantive count strengthens the dual-criminality showing for Spain.
- **[[dual-criminality]]**: not contested at the press-release stage but operationally engaged for the U.S.-Spain extradition track on Buchanan.
- **[[extraterritorial-jurisdiction]]**: U.S. wire-fraud jurisdiction over Buchanan's UK-resident conduct rests on the use of U.S. wires and U.S.-based victims.
- **Group-criminal-organisation theory NOT charged**: no RICO, continuing criminal enterprise, or 18 U.S.C. § 371 conspiracy-to-violate-multiple-offences theory is alleged in the press release. The charges are squarely individual-defendant fraud and identity-theft counts. Compare [[us-v-jubair-scattered-spider-2025]] (which adds money-laundering conspiracy under § 1956(h)) and [[uk-jubair-flowers-tfl-cyber-attack-2025]] (UK Computer Misuse Act).

### Precedent Value

- **First U.S. multi-defendant federal indictment of alleged Scattered Spider members**: establishes the template for subsequent Scattered Spider charging documents (compare the September 2025 D.N.J. complaint against Jubair, [[us-v-jubair-scattered-spider-2025]]).
- **U.S.-Spain extradition track for a UK national**: documents the pattern in which the requested state for extradition is determined by the state of detention rather than nationality. Useful comparator for analysing third-country-arrest extradition mechanics on cybercrime cases.
- **Police Scotland as named cooperator**: rare instance of a Scottish-specific (rather than NCA / Met / City of London Police) UK-side cooperator on a U.S. cybercrime indictment. Reflects sub-state-level UK police forces' growing role in U.S. cybercrime investigations where the defendant has Scotland-specific residency.
- **MFA-bypass-via-push-fatigue conduct**: the indictment describes employees authenticating "two-factor authentication request[s] sent to their mobile phones," which describes the now-common push-fatigue / push-acceptance MFA bypass technique. One of the earliest tier-1 DOJ filings to put this technique in the conduct narrative.

## Proceedings Timeline

| Date | Event |
|---|---|
| ~2021-09 | Approximate start of conduct period charged. |
| ~2023-04 | Approximate end of conduct period charged. |
| 2024-06 | Tyler Buchanan reportedly arrested in Spain at Palma de Mallorca airport while attempting to board a flight to Italy (per secondary reporting; not in DOJ release). |
| 2024-11-19 (Tue) | FBI arrests Joel Martin Evans in North Carolina. |
| **2024-11-20 (Wed)** | **USAO-CDCA + FBI Los Angeles unseal the federal grand jury indictment against Elbadawy, Urban, Osiebo, Evans, plus a companion federal criminal complaint against Buchanan. Press Release No. 24-289. Evans's initial court appearance scheduled for the same day.** |
| 2024-11-25 | DOJ press release "Updated" notation. |
| (subsequent, per secondary reporting) | Reported extradition of Buchanan to the United States in early 2025 — pending tier-1 confirmation. |
| (pending) | Plea, trial, or pre-trial motions for any defendant. |

## Cooperation Effectiveness

- **Speed**: arrest of Evans (2024-11-19) and unsealing (2024-11-20) timed within 24 hours, consistent with deliberate domestic-arrest-then-unseal sequencing to avoid tipping co-defendants.
- **Breadth (per DOJ release)**: **two named external offices** — Police Scotland and USAO Eastern District of North Carolina — plus four FBI field offices. Modest external footprint compared with the eight-agency / six-country roster of [[us-v-jubair-scattered-spider-2025]].
- **Notable absences (per DOJ release)**: no named UK NCA, City of London Police, Met Police, or West Midlands Police cooperation. No named Spanish, Eurojust, Europol, or DOJ Office of International Affairs participation. The absence of OIA from the named-cooperators list is notable given that Buchanan's June 2024 Spanish arrest (per secondary reporting) would have required OIA-coordinated provisional-arrest request to Spain — **highly likely** (80–95%) that OIA was in fact involved but is simply not credited in this press release.
- **Group attribution NOT made by DOJ**: the absence of "Scattered Spider" / Octo Tempest / UNC3944 / 0ktapus naming in the DOJ release is a deliberate prosecutorial choice (to avoid charging-document attribution that would require additional evidentiary showing) and contrasts with [[us-v-jubair-scattered-spider-2025]] (D.N.J., September 2025), which explicitly names "Scattered Spider, also known as Octo Tempest, UNC3944, and 0ktapus" in the DOJ release body.

## Korean Relevance (한국 관련성)

The DOJ release does not identify Korean victims, Korean-resident defendants, Korean-based infrastructure, or Korean LE participation. Indirect relevance:

- **Smishing-to-MFA-bypass-to-cryptocurrency-drain pattern**: the modus operandi is directly analogous to Korean voice-phishing → bank-account-credential-theft → cryptocurrency-drain schemes investigated by the [[knpa-cyber-bureau|KNPA cyber units]] and the Supreme Prosecutors' Office under domestic [[voice-phishing-ic|voice phishing]] statutes (전기통신금융사기 피해 방지 및 피해금 환급에 관한 특별법). The U.S. choice to charge wire fraud + aggravated identity theft + conspiracy (rather than a CFAA-only charging package) is a useful comparator for Korean prosecutors building outbound MLAT requests on Korean-victim smishing cases.
- **Sub-state UK police-force cooperation precedent**: Police Scotland's appearance as a named cooperator (rather than the UK central NCA) is a comparator for cases where Korean LE may seek to cooperate with a specific UK regional or sub-state force on a defendant with regional residency — a contrast model to the standard NCA-only cooperation channel.
- **U.S.-Spain extradition track for a UK national on cyber charges**: useful comparator for analysing extradition options when a Korean target is detained in a third country (e.g., Southeast Asia) where neither Korea nor the U.S. has a direct bilateral extradition treaty preference.

## Contradictions & Open Questions

> [!warning] Group attribution not in DOJ release
> The "Scattered Spider" attribution to these five defendants is **secondary-source only**. The DOJ release uses no group name. Tier-1 confirmation is **likely** (55–80%) to come from a future superseding indictment or related DOJ release; until then, the attribution is treated as **highly likely** (80–95%) based on modus-operandi and victim-set overlap with publicly reported Scattered Spider activity, but not asserted as a tier-1 fact on this page.

> [!warning] Spain-arrest fact not in DOJ release
> Tyler Buchanan's June 2024 arrest in Spain (Palma de Mallorca airport, attempting to board a flight to Italy) is documented in secondary reporting (KrebsOnSecurity, Bloomberg, The Record, etc.) but **not** in the DOJ release. Tier-1 confirmation pending: a Spanish Audiencia Nacional decision, a U.S. extradition filing, or a U.S. superseding indictment recording the foreign arrest.

> [!note] Specific docket number not in release
> The DOJ release identifies Press Release No. 24-289 but does not give the C.D. Cal. case number(s). To be filled in when the actual indictment / complaint document is ingested.

> [!note] Victim companies unnamed in release
> The DOJ release does not name any of the "numerous" victim companies. Secondary reporting names LastPass, MailChimp, Okta, T-Mobile, Twilio, and MGM Resorts; these names are **not** asserted on this page until tier-1 sources confirm specific victim-to-this-indictment mapping.

Open questions:

1. Specific C.D. Cal. case / docket number(s).
2. Victim companies named in the indictment / complaint (vs. those reported only in secondary press).
3. Tyler Buchanan's exact extradition path: Spanish Audiencia Nacional decision date, extradition order date, transfer date to U.S., date of first U.S. court appearance.
4. Whether a superseding indictment was returned post-extradition that explicitly names Scattered Spider / Octo Tempest / UNC3944 / 0ktapus as the group.
5. Cryptocurrency seizure / forfeiture amounts attributable to this prosecution (vs. to the parallel [[us-v-jubair-scattered-spider-2025]] forfeiture).
6. Whether the DOJ Office of International Affairs (OIA), UK NCA, or Eurojust assisted on the Spain arrest — strongly implied by the operational logistics but not credited in this DOJ release.
7. The relationship between this November 2024 indictment / complaint and the September 2025 D.N.J. complaint against Jubair — same investigative team? same underlying intelligence base? coordinated charging strategy?

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2024-11-20_justice-gov_five-members-scattered-spider-charged-cybercrime-attacks\|5 Defendants Charged Federally with Running Scheme that Targeted Victim Companies via Phishing Text Messages]] | U.S. Department of Justice — U.S. Attorney's Office, Central District of California (USAO-CDCA) | 2024-11-20 | https://www.justice.gov/usao-cdca/pr/5-defendants-charged-federally-running-scheme-targeted-victim-companies-phishing-text |

## Related Wiki Pages

- Sister Scattered Spider matter (US, 2025): [[us-v-jubair-scattered-spider-2025]]
- Sister Scattered Spider matter (UK, 2025): [[uk-jubair-flowers-tfl-cyber-attack-2025]]
- Concept: [[dual-criminality]], [[extradition-practice]], [[extraterritorial-jurisdiction]]
- Crime types: [[hacking-ic]], [[identity-theft]], [[online-fraud-ic]]
- Agencies: [[fbi]], [[us-doj]]
- Countries: [[united-states]], [[united-kingdom]], [[spain]]
