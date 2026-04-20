# participating_countries — local-text verification audit

_Run: 2026-04-21 08:21_

This report cross-checks every operation's `participating_countries` frontmatter entries against local text (operation body + cited `wiki/sources/*.md` summaries + their `raw_path` raw files). It does NOT fetch the web.

- **verified**: country name was found in at least one local text file
- **unverified**: country in frontmatter but NOT found in any local text — candidate for primary-source re-verification
- `missing_sources`: count of source references with no matching file

Unverified ≠ wrong. For operations whose primary sources are only reachable on the web (e.g., Europol press releases behind Cloudflare), the real text is not on disk. Treat large `unverified` lists as a prompt to recover the full source, not as evidence of non-participation.

## Summary

- Operations scanned: 1085
- With participating_countries: 1066
- Fully verified (every country found in local text): 272
- With ≥1 unverified country: 794

## Operations with unverified countries

| Op | Total | Verified | Unverified | Missing src files | Unverified list |
|---|---:|---:|---:|---:|---|
| [[operation-haechi-vi]] | 32 | 3 | 27 | 0 | japan, albania, argentina, armenia, australia, brazil, bulgaria, cambodia, canada, china, germany, ghana, … (+15) |
| [[operation-eur-300m-global-credit-card-fraud-2025]] | 10 | 4 | 6 | 0 | cyprus, italy, netherlands, spain, canada, singapore |
| [[darkmarket-takedown]] | 7 | 3 | 4 | 0 | australia, united-kingdom, united-states, denmark |
| [[operation-us-v-parsarad-nemesis]] | 3 | 0 | 3 | 0 | united-states, germany, lithuania |
| [[doublevpn-takedown]] | 9 | 7 | 2 | 0 | united-states, united-kingdom |
| [[operation-dark-huntor]] | 9 | 7 | 2 | 0 | united-kingdom, united-states |
| [[operation-eur-3m-online-investment-fraud-2025]] | 7 | 5 | 2 | 0 | belgium, latvia |
| [[operation-eur-600m-crypto-scam-network-2025]] | 5 | 3 | 2 | 0 | belgium, france |
| [[operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto]] | 6 | 4 | 2 | 0 | united-kingdom, united-states |
| [[operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | 4 | 2 | 2 | 0 | belgium, united-kingdom |
| [[alphabay-takedown]] | 8 | 7 | 1 | 0 | united-kingdom |
| [[bidencash-takedown]] | 6 | 5 | 1 | 5 | united-states |
| [[carbanak-cobalt-takedown]] | 6 | 5 | 1 | 0 | united-states |
| [[cryptex-pm2btc-sanctions]] | 2 | 1 | 1 | 0 | united-states |
| [[dridex-operations]] | 5 | 4 | 1 | 8 | united-kingdom |
| [[isoon-apt27-indictment]] | 2 | 1 | 1 | 0 | united-states |
| [[lumma-stealer-takedown]] | 2 | 1 | 1 | 0 | united-states |
| [[nemesis-market-takedown]] | 3 | 2 | 1 | 0 | united-states |
| [[operation-16-defendants-federally-charged-in-connection-with-danabot-malware-scheme-that-infected-computers-worldwide]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-2]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-3]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-4]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-5]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-6]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-7]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace]] | 4 | 3 | 1 | 0 | australia |
| [[operation-avalanche]] | 28 | 27 | 1 | 0 | united-kingdom |
| [[operation-ceres-man-pleads-guilty-cyberstalking-two-victims]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-chinese-national-sentenced-prison-role-crypto-scam-targeting-americans]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-contender-2]] | 4 | 3 | 1 | 0 | cote-divoire |
| [[operation-culpeper-woman-arrested-in-dark-web-murder-for-hire-plot]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-darknet-drug-vendor-arrested-for-distributing-illicit-prescription-drugs]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-darknet-vendor-arrested-on-distribution-and-money-laundering-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-deepdotweb-administrator-pleads-guilty-money-laundering-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-estonian-national-extradited-from-estonia-to-face-charges-of-illegal-procurement-of-u-s-electronics]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-euclid-ohio-man-pleads-guilty-distribution-fentanyl-he-ordered-china-and-sold]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-fayette-county-man-admits-making-hoax-emergency-phone-calls-to-elicit-an-armed-police-response-practice-is-kno]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-florida-computer-programmer-arrested-for-hacking]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-florida-man-pleads-guilty-production-images-child-sexual-abuse-and-traveling-sexually]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-foreign-national-indicted-in-wire-fraud-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-foreign-national-pleads-guilty-to-role-in-cybercrime-schemes-involving-tens-of-millions-of-dollars-in-losses]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-childcare-provider-sentenced-to-15-years-in-federal-prison-for-the-production-of-child-sexual-abuse-mat]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-commander-and-adjutant-of-nonprofit-veterans-organization-indicted-for-wire-fraud-and-tax-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-company-chief-financial-officer-indicted-for-using-35-million-in-company-cash-to-invest-in-cryptocurren]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-emergency-physician-pleads-guilty-to-possessing-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-employee-of-house-member-sentenced-to-prison-term-on-charges-in-cyberstalking-case]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-employee-of-silicon-valley-company-pleads-guilty-to-damaging-ex-employers-computers]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-owner-of-t-mobile-retail-store-in-eagle-rock-found-guilty-of-committing-25-million-scheme-to-illegally-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-former-teaching-assistant-in-st-louis-admits-blackmailing-student]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-french-coder-who-helped-extort-british-company-arrested-in-thailand]] | 2 | 1 | 1 | 0 | united-kingdom |
| [[operation-ghost-cybercrime-platform-dismantled-in-global-operation-51-arrested]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-grand-jury-indicts-knoxville-woman-previously-arrested-in-murder-for-hire-plot]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-greene-county-man-indicted-cyberstalking-and-interstate-threats]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-illinois-man-sentenced-2-years-federal-prison-operating-subscription-based-computer]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-in-re-bidencash-marketplace-seizure]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-in-re-heartsender-seizure]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-independence-pair-indicted-for-drug-and-firearms-offenses]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-individual-arrested-and-charged-with-operating-notorious-darknet-cryptocurrency-mixer]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-international-crypto-vendor-sentenced-for-money-laundering-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-international-hacker-for-hire-who-conspired-with-and-aided-russian-fsb-officers-sentenced-to-five-years-in-pri]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-international-money-launderer-sentenced-to-over-11-years-in-federal-prison-for-laundering-millions-from-cyber-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-internet-stalker-sentenced-to-more-than-14-years-in-federal-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-iranian-man-pleaded-guilty-to-role-in-robbinhood-ransomware]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-and-money-laundering-services]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-other-drugs-and-money-laundering-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-irish-man-who-helped-operate-the-silk-road-website-sentenced-in-manhattan-federal-court-to-over-six-years-in-p]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-issaquah-washington-man-sentenced-to-7-years-in-prison-for-dealing-fentanyl-and-other-drugs-on-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-jefferson-county-man-sentenced-to-6-12-years-in-prison-for-possession-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-jordanian-man-admits-selling-unauthorized-access-to-computer-networks-of-50-companies]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-jumbotron-hacker-and-prolific-child-molester-sentenced-to-220-years-in-federal-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-justice-department-secures-forfeiture-of-over-5m-of-funds-traceable-to-business-email-compromise-scheme-target]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-justice-department-seeks-forfeiture-of-848-247-in-cryptocurrency-from-confidence-scams]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-justice-department-seeks-forfeiture-of-over-5-million-in-bitcoin-stolen-in-sim-swapping-scams]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-justice-dept-seizes-over-112m-in-funds-linked-to-cryptocurrency-investment-schemes-with-over-half-seized-in-lo]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kansas-city-woman-indicted-for-fraudulent-tax-returns]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kansas-farmer-indicted-for-insurance-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kansas-man-pleads-guilty-to-child-pornography-possession]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kansas-woman-indicted-for-defrauding-elderly-victims]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kc-man-sentenced-for-selling-meth-heroin-on-the-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kent-washington-resident-indicted-for-dealing-fentanyl-while-illegally-possessing-firearm]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kentucky-man-pleads-guilty-advertising-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kentucky-man-pleads-guilty-to-advertising-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kentucky-man-sentenced-to-15-years-in-prison-for-advertising-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-key-member-of-drug-ring-associated-with-aryan-prison-gang-sentenced-to-7-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-king-county-couple-indicted-for-drug-and-illegal-weapons-possession]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-king-county-man-who-dealt-narcotics-on-the-dark-web-and-kept-a-cache-of-weapons-at-his-rv-sentenced-to-8-years]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kirkwood-resident-pleads-guilty-for-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-knox-county-man-sentenced-to-60-years-imprisonment-for-two-counts-of-production-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-kosovo-national-pleads-guilty-to-operating-an-online-criminal-marketplace]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-lakeland-man-pleads-guilty-to-receiving-child-sex-abuse-videos-from-the-largest-darknet-child-pornography-webs]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-lakeland-man-sentenced-to-more-than-9-years-in-federal-prison-for-downloading-and-possessing-child-sex-abuse-v]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-laredo-professor-charged-with-distribution-and-production-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-latvian-national-charged-for-alleged-role-in-transnational-cybercrime-organization]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-law-enforcement-seize-record-amounts-of-illegal-drugs-firearms-and-drug-trafficking-proceeds-in-international-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-leader-of-darknet-drug-distribution-conspiracy-sentenced-to-federal-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-leader-of-darknet-italianmafiabrussels-drug-trafficking-organization-sentenced-to-11-years-imprisonment]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-leader-of-international-malvertising-and-ransomware-schemes-extradited-from-poland-to-face-cybercrime-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-leader-of-international-steroids-distribution-scheme-sentenced-to-eight-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-leader-of-transnational-cybercrime-group-noirs-luxury-refunds-charged-with-conspiracy-to-commit-mail-and-wire-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ledyard-man-charged-with-child-exploitation-offense]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ledyard-man-pleads-guilty-child-exploitation-offense]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ledyard-man-pleads-guilty-to-child-exploitation-offense]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-lewis-county-man-charged-federally-with-unlawful-weapons-possession]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-lone-american-indicted-in-international-drug-trafficking-investigation-sentenced-to-five-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-long-beach-man-pleads-guilty-to-production-and-distribution-of-images-of-minors-engaging-in-sexually-explicit-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-long-beach-man-sentenced-to-110-years-in-prison-for-production-of-images-of-minors-engaging-in-sexually-explic]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-los-angeles-county-woman-pleads-guilty-to-conspiring-to-distribute-heroin-methamphetamine-and-cocaine-on-the-d]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-madison-county-sex-offender-indicted-for-failure-to-register]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-caught-three-times-with-dealer-quantities-of-fentanyl-indicted-federally]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-charged-with-threatening-and-cyberstalking-congressman]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-from-grays-harbor-county-washington-pleads-guilty-to-possession-of-narcotics-with-intent-to-distribute]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-pleads-guilty-to-charges-of-stealing-senate-information-illegally-posting-restricted-personal-information-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-pleads-guilty-to-conspiracy-to-distribute-meth-on-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-sentenced-for-conspiracy-to-distribute-meth-on-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-sentenced-for-stalking-and-threatening-congressman-kevin-hern-and-his-wife]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-sentenced-for-stealing-over-712-bitcoin-subject-to-forfeiture]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-sentenced-for-transnational-cybercrime-enterprise]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-sentenced-stalking-and-threatening-congressman-kevin-hern-and-his-wife]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-man-who-served-in-army-under-an-assumed-name-sentenced-to-time-served-and-community-service-for-passport-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-marine-based-at-camp-pendleton-arrested-on-federal-charges-alleging-cyberstalking-of-young-women-in-sextortion]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-marion-county-man-arrested-for-possession-of-child-sex-abuse-material]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-marion-county-man-pleads-guilty-to-production-of-child-sex-abuse-material]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-maryland-man-sentenced-to-30-months-in-prison-for-cyberstalking-former-girlfriend-and-threatening-workplace-vi]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-maryland-men-indicted-on-charges-relating-to-dark-web-drug-distribution-and-money-laudering-government-seized-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-massachusetts-man-pleads-guilty-knowingly-concealing-source-material-support-or]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-massachusetts-man-pleads-guilty-to-knowingly-concealing-the-source-of-material-support-or-resources-to-isis]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-massachusetts-man-sentenced-for-knowingly-concealing-the-source-of-material-support-or-resources-to-isis]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-member-of-darknet-drug-trafficking-organization-italianmafiabrussels-sentenced-to-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-member-of-lummi-nation-indicted-for-distributing-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-member-of-russian-cybercrime-group-charged-in-ohio]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-member-of-the-dark-overlord-hacking-group-extradited-from-united-kingdom-to-face-charges-in-st-louis]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-members-of-seattle-drug-trafficking-organization-indicted-for-distribution-of-heroin]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-men-indicted-for-crimes-related-to-securities-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-mexican-national-sentenced-to-prison-for-role-as-drug-ring-courier]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-michigan-man-indicted-on-wire-fraud-and-aggravated-identity-theft-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-michigan-man-sentenced-to-312-years-in-prison-for-role-in-sim-swapping-that-led-to-account-takeovers-and-122-0]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-michigan-man-sentenced-to-five-years-in-prison-for-possessing-child-sexual-abuse-material-on-a-military-base]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-middlesex-county-man-charged-with-production-and-possession-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-minnesota-man-pleads-guilty-to-stalking-and-interstate-communications]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-mississippi-county-sheriff-indicted-on-charges-of-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-missouri-man-sentenced-for-advertising-child-pornography-on-the-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-moldovan-national-and-technical-mastermind-of-xdedic-marketplace-extradited-from-spain]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-moldovan-sentenced-for-distributing-multifunction-malware-package]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-monroe-washington-man-sentenced-to-10-years-in-prison-for-role-as-right-hand-man-in-deadly-drug-distribution-r]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-monroeville-man-sentenced-to-24-months-for-purchasing-hundreds-of-stolen-log-in-credentials-off-the-darkweb]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-montgomery-county-doctor-charged-with-illegally-prescribing-opioids]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-monticello-man-indicted-for-attempted-enticement-of-a-minor]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-mountain-view-resident-charged-with-production-of-child-pornography-and-cyberstalking]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-and-conti]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti-ransomware-conspiracies-2]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-natchitoches-man-sentenced-for-possession-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nebraska-businessman-indicted-for-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nebraska-man-pleads-guilty-in-multi-million-dollar-cryptojacking-case]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nervone]] | 1 | 0 | 1 | 0 | cote-divoire |
| [[operation-nevada-woman-sentenced-to-5-years-prison-for-hiring-hitman-on-dark-web-to-kill-her-ex-husband]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-britain-man-sentenced-to-10-years-in-prison-for-distributing-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-britain-man-sentenced-to-66-months-in-prison-for-distributing-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-jersey-man-sentenced-for-prescription-opioid-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-jersey-man-sentenced-to-prison-after-pleading-guilty-to-posting-restricted-information-to-social-media]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-york-man-admits-continuing-to-sell-counterfeit-xanax-on-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-york-man-indicted-in-st-louis-accused-of-selling-counterfeit-xanax-on-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-york-man-sentenced-to-24-months-in-prison-for-internet-offenses-including-doxing-swatting-making-a-false-b]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-york-man-sentenced-to-54-months-in-prison-for-selling-counterfeit-xanax-on-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-new-york-man-sentenced-to-84-months-in-prison-for-conspiring-to-engage-in-multimillion-dollar-wire-fraud-schem]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-newport-news-man-sentenced-for-prolific-card-swiping-operation]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nicaraguan-national-pleads-guilty-to-conspiring-to-distribute-cocaine-and-marijuana-on-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-citizen-extradited-from-the-u-k-arraigned-on-indictment-for-wire-fraud-involving-stolen-tax-informati]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-national-pleads-guilty-to-1-25-million-business-email-compromise-scam-impacting-u-s-company]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-national-pleads-guilty-to-multi-million-dollar-cyber-fraud-scheme-targeting-tulsa-company-and-four-ot]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-national-sentenced-to-more-than-12-years-in-federal-prison-for-cyber-scams]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-national-sentenced-to-more-than-six-years-in-federal-prison-for-international-tax-fraud-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-nationals-charged-with-operating-business-compromise-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-scammer-arrested-for-60-million-email-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nigerian-state-official-sentenced-to-5-years-in-prison-for-stealing-u-s-disaster-aid-and-taxpayer-refunds]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-north-carolina-man-sentenced-to-federal-prison-for-distributing-opioids-through-the-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-north-philadelphia-pill-mill-doctor-sentenced-to-five-years-in-prison-for-illegal-opioid-distribution]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-north-reading-man-indicted-for-possession-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-notorious-hacker-sentenced-to-18-months-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nurse-admits-tampering-vials-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nurse-admits-tampering-with-vials-of-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-nurse-charged-with-tampering-with-vials-of-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-o-c-and-houston-men-sentenced-to-decades-in-prison-for-supplying-fentanyl-and-other-drugs-sold-on-darknet-and-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-o-c-man-admits-operating-unlicensed-atm-network-that-laundered-millions-of-dollars-of-bitcoin-and-cash-for-cri]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ocala-man-sentenced-to-federal-prison-for-attempting-to-meet-a-13-year-old-to-engage-in-sexual-activity]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-odessa-man-indicted-for-stealing-more-than-250-000-in-ppp-funds]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ohio-man-pleads-guilty-for-unlawfully-stealing-over-712-seized-bitcoin-subject-to-forfeiture-in-brothers-pendi]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ohio-resident-pleads-guilty-to-operating-darknet-based-bitcoin-mixer-that-laundered-over-300-million]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-oklahoma-man-sentenced-to-30-years-in-prison-for-sexually-exploiting-children]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-oldsmar-man-charged-with-producing-and-distributing-child-sexual-abuse-material]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-one-defendant-sentenced-to-prison-and-another-ordered-detained-pretrial-this-week-in-separate-cyberstalking-ca]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-operation-haechi-iii-interpol-arrested-1000-cyber-criminals-seized-130-million]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-operation-orion-international-144-arrested-in-major-child-abuse-operation-across-south-america]] | 2 | 1 | 1 | 0 | united-states |
| [[operation-operator-of-helix-darknet-cryptocurrency-mixer-sentenced-in-money-laundering-conspiracy-involving-hundreds-of-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-operator-of-silk-road-2-0-website-charged-in-manhattan-federal-court]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-orange-county-man-arrested-on-federal-stalking-charge-alleging-multiyear-harassment-campaign-against-prominent]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-orange-county-man-pleads-guilty-stalking-charge-harassment-campaign-against]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-orange-county-man-pleads-guilty-to-stalking-charge-for-harassment-campaign-against-professional-online-gamer]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-orange-county-man-sentenced-to-75-months-for-distributing-methamphetamine-and-selling-illegal-pills-on-the-dar]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-overland-park-men-indicted-for-investment-fraud-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-owners-of-empire-market-charged-in-chicago-with-operating-430-million-dark-web-marketplace]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-palm-beach-county-man-sentenced-for-cyberstalking-two-victims]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-parma-men-among-those-charged-as-part-of-crackdown-on-darknet-vendors]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-parolee-indicted-for-illegal-possession-of-a-firearm]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pasadena-man-who-cyberstalked-and-made-threats-to-injure-rape-and-kill-sentenced-to-more-than-3-years-in-feder]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pennsylvania-family-pleads-guilty-to-fentanyl-trafficking]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pennsylvania-man-convicted-of-distributing-fentanyl-analogue-that-killed-orlando-woman]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pernicious-cyberstalker-sentenced-to-9-years-in-prison-for-unrelenting-harassment-of-former-roommate-and-other]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-philadelphia-man-sentenced-for-cyberstalking-and-wire-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-phobos-ransomware-administrator-extradited-from-south-korea-to-face-cybercrime-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-phobos-ransomware-affiliates-arrested-in-coordinated-international-disruption]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-physician-sentenced-to-18-years-in-prison-for-operating-a-pill-mill-from-his-northwest-d-c-medical-practice]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pierce-county-based-drug-trafficking-organization-indicted-for-distributing-cocaine-fentanyl-and-marijuana]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pilots-indicted-for-wire-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pineville-man-sentenced-to-five-years-in-prison-for-accessing-child-pornography-online]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pittsburg-resident-pleads-guilty-to-stolen-identity-tax-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pittsburgh-felon-sentenced-to-9-5-years-in-prison-for-identity-theft-and-firearms-crimes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pittsburgh-man-charged-threatening-communications-and-impeding-fbi-investigation-1]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pittsburgh-man-charged-with-threatening-communications-and-impeding-fbi-investigation]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pittsburgh-man-indicted-on-cyberstalking-charge]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pittsburgh-woman-pleads-guilty-to-credit-card-fraud-and-aggravated-identity-theft-charges-in-car-rental-scam]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-post-falls-man-indicted-for-sexual-exploitation-of-a-child-distribution-of-child-sexual-abuse-materials-and-po]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-previously-convicted-felon-sentenced-to-more-than-26-years-in-federal-prison-for-possessing-a-firearm-in-conne]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-prince-georges-county-man-sentenced-to-seven-years-in-federal-prison-for-a-heroin-distribution-conspiracy-cond]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-prior-felon-pleads-guilty-to-cyberstalking]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-prolific-dark-web-dealer-of-carfentanil-and-fentanyl-sentenced-to-1712-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-prolific-fentanyl-distributor-sentenced-to-six-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-prominent-global-cryptocurrency-exchange-kucoin-and-two-of-its-founders-criminally-charged-with-bank-secrecy-a]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pulaski-county-man-indicted-for-cyber-intrusion-identity-theft-and-bank-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pulaski-county-man-sentenced-cyber-intrusion-and-aggravated-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-pulaski-county-man-sentenced-for-cyber-intrusion-and-aggravated-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-puyallup-man-caught-with-nearly-100-000-fentanyl-pills-and-five-firearms-sentenced-to-six-and-a-half-years-in-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-queens-woman-charged-with-using-a-hitman-for-hire-website-on-the-dark-web-to-order-murder-of-her-lovers-wife]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-red-card]] | 7 | 6 | 1 | 0 | cote-divoire |
| [[operation-registered-sex-offender-admits-possessing-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-registered-sex-offender-admits-possessing-child-pornography-0]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-registered-sex-offender-charged-with-new-child-pornography-offense]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-registered-sex-offender-sentenced-to-35-years-in-prison-for-exchanging-videos-images-of-child-torture-for-chil]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-renton-washington-man-who-worked-with-his-son-to-deal-drugs-and-launder-proceeds-sentenced-to-5-years-in-priso]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-repeat-drug-trafficker-caught-twice-with-kilos-of-drugs-and-firearms-sentenced-to-10-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-repeat-offender-sentenced-to-10-years-for-possession-of-child-sexual-abuse-material]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-repeat-sex-offender-pleads-guilty-to-sexual-exploitation-of-a-child]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-resident-of-tacoma-hotel-indicted-for-drug-and-gun-crimes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-revere-massachusetts-man-sentenced-in-nationwide-rideshare-and-delivery-account-fraud-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-rewired]] | 10 | 9 | 1 | 4 | united-kingdom |
| [[operation-rico-conspirator-convicted-at-trial]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-rico-conspirators-responsible-for-nationwide-computer-intrusions-and-tax-fraud-sentenced-to-federal-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-robinson-twp-man-pleads-guilty-in-international-investigation-into-darknet-sale-of-child-exploitation-videos-a]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-romanian-national-pleads-guilty-selling-access-networks-oregon-state-government-office]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-romanian-national-pleads-guilty-to-selling-access-to-networks-of-oregon-state-government-office-and-other-u-s-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-romanian-national-pleads-guilty-to-selling-access-to-networks-of-oregon-state-government-office-and-other-u-s--2]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-romanian-woman-pleads-guilty-to-federal-charges-in-hacking-of-metropolitan-police-department-surveillance-came]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ross-ulbricht-a-k-a-dread-pirate-roberts-sentenced-in-manhattan-federal-court-to-life-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ross-ulbricht-found-guilty-on-all-counts]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ross-ulbricht-sentenced-to-life-in-federal-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ross-ulbricht-sentenced-to-life-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-hacker-sentenced-to-over-7-years-in-prison-for-hacking-into-three-bay-area-tech-companies]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-malware-developer-pleads-guilty-to-conspiracy-to-commit-wire-and-computer-fraud]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-man-found-guilty-of-hacking-into-three-bay-area-tech-companies]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-national-and-bitcoin-exchange-charged-in-21-count-indictment-for-operating-alleged-international-money]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-national-charged-in-hacking-scheme-targeting-pittsburgh-national-golf-course]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-national-charged-with-decade-long-series-of-hacking-and-bank-fraud-offenses-resulting-in-tens-of-milli]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-national-indicted-in-east-texas-for-cyber-hacking-enterprise]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-national-sentenced-for-involvement-in-development-and-deployment-of-trickbot-malware]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-nationals-charged-with-hacking-one-cryptocurrency-exchange-and-illicitly-operating-another]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-russian-trickbot-malware-dev-sentenced-to-64-months-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sacramento-man-indicted-for-drug-distribution-via-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sacramento-sex-offender-pleads-guilty-to-distributing-child-pornography-on-the-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sacramento-woman-pleads-guilty-to-conspiracy-to-distribute-fentanyl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-salinas-man-charged-in-embezzlement-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-salinas-resident-sentenced-to-54-months-in-prison-for-identity-theft-and-preparing-false-tax-returns]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-salinas-residents-charged-in-tax-and-mortgage-fraud-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-antonio-man-sentenced-for-january-2018-threats-made-against-players-and-fans-at-nfl-playoff-game-at-heinz-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-francisco-man-sentenced-to-100-months-imprisonment-in-credit-card-fraud-and-identity-theft-case]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-francisco-man-sentenced-to-84-months-in-prison-for-possession-of-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-francisco-resident-charged-in-alleged-identity-theft-bank-fraud-and-aggravated-identity-theft-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-francisco-resident-sentenced-to-over-three-years-in-prison-for-aggravated-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-francisco-resident-sentenced-to-seven-years-in-prison-for-stealing-prisoner-identities-and-filing-fraudule]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-gabriel-valley-man-admits-cyberstalking-two-teenage-girls]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-gabriel-valley-man-admits-to-cyberstalking-two-teenage-girls]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-gabriel-valley-man-sentenced-to-more-than-4-years-in-federal-prison-for-role-in-36-9-million-global-digita]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-jose-man-pleads-guilty-to-damaging-ciscos-network]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-jose-man-sentenced-to-27-months-imprisonment-for-money-laundering]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-jose-resident-pleads-guilty-to-stealing-homeless-individuals-ids-and-using-them-to-seek-fraudulent-tax-ref]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-san-jose-resident-sentenced-to-a-year-in-custody-for-damaging-computers-of-silicon-valley-company]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sanford-spam-king-wallace-sentenced-to-two-and-a-half-years-in-custody-for-spamming-facebook-users]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-santa-clarita-man-found-guilty-of-producing-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-santa-clarita-man-who-led-organization-that-trafficked-drugs-to-darknet-customers-nationwide-sentenced-to-8-ye]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-seattle-man-sentenced-for-buying-630-000-counterfeit-pills-on-the-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-seattle-man-who-trafficked-drugs-and-fired-gun-in-international-district-drive-by-sentenced-to-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-second-canadian-resident-pleads-guilty-to-massive-covid-19-benefit-fraud-scheme]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-second-defendant-sentenced-to-7-years-in-prison-for-drug-trafficking-from-rvs-near-a-state-park]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-senior-adviser-to-the-operator-of-the-silk-road-online-black-market-sentenced-to-20-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-senior-advisor-arrested-in-thailand]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-serbian-citizen-pleads-guilty-to-running-monopoly-drug-market-on-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-serengeti]] | 1 | 0 | 1 | 0 | united-kingdom |
| [[operation-servers-seized-in-ukraine-moldova-as-germany-takes-down-world-s-largest-illegal-darknet-marketplace]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-seven-georgians-indicted-for-operating-online-fentanyl-meth-marketplace]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-seven-indicted-in-seattle-in-connection-with-coast-to-coast-drug-trafficking-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sex-offender-pleads-guilty-to-child-exploitation-offense-admits-violating-supervised-release]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-shiprock-man-indicted-on-federal-sexual-assault-and-kidnapping-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-siemens-contract-employee-intentionally-damaged-computers-planting-logic-bombs-programs]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-significant-member-of-a-whatcom-county-fentanyl-trafficking-ring-sentenced-to-4-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-silk-road-dark-web-fraud-defendant-sentenced-following-seizure-and-forfeiture-of-over-3-4-billion-in-cryptocur]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-silk-road-drug-vendor-who-claimed-to-commit-murders-for-hire-for-silk-road-founder-ross-ulbricht-charged-with-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-silk-road-vendor-sentenced-to-two-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-six-defendants-charged-with-selling-millions-of-dollars-worth-of-psychedelic-mushrooms-online]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-six-indicted-as-part-of-whatcom-county-fentanyl-trafficking-organization]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-six-russian-gru-officers-charged-in-connection-with-worldwide-deployment-of-destructive-malware-and-other-disr]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-skiatook-man-indicted-for-threatening-to-kill-federal-agents]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-slovakian-man-admits-aiding-darknet-market-sold-drugs-and-stolen-personal-information]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-slovakian-man-admits-aiding-darknet-market-that-sold-drugs-and-stolen-personal-information]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-socal-man-arrested-on-federal-charges-alleging-he-schemed-to-advertise-and-sell-hive-computer-intrusion-malwar]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-social-services-director-of-a-nursing-home-charged-with-id-theft-from-elderly-residents]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sonoma-county-resident-sentenced-to-30-months-in-prison-for-passport-fraud-and-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-south-carolina-man-charged-with-interstate-stalking-and-aggravated-id-theft-targeting-pennsylvania-resident]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-south-carolina-man-sentenced-to-30-months-in-prison-for-interstate-stalking]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-south-korean-national-and-hundreds-of-others-charged-worldwide-in-the-takedown-of-the-largest-darknet-child-po]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-southern-california-man-pleads-guilty-to-fentanyl-and-methamphetamine-distribution-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-southern-california-resident-sentenced-to-34-months-in-prison-for-role-in-bank-fraud-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-southern-california-woman-pleads-guilty-to-fentanyl-distribution-and-money-laundering-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ssndob-marketplace-administrator-pleads-guilty-to-charges-related-to-his-operation-of-a-series-of-websites-tha]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-st-augustine-serial-child-molester-convicted-of-hacking-jumbotron-child-exploitation-offenses-sex-offender-reg]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-st-lawrence-county-man-pleads-guilty-to-receiving-and-possessing-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-st-louis-man-admits-making-rape-threats-to-five-women]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-st-louis-man-indicted-on-cyberstalking-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-st-louis-man-sentenced-on-aggravated-id-theft-other-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-st-louis-man-sentenced-to-71-months-for-making-rape-threats-to-five-women]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-stanwood-washington-repeat-offender-sentenced-to-10-years-in-prison-for-selling-heroin-and-fentanyl-over-the-d]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sturgis-man-charged-with-selling-counterfeit-drugs-on-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sturgis-man-sentenced-to-70-months-for-selling-drugs-on-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-sumter-man-pleads-guilty-to-destruction-of-an-energy-facility-and-possession-of-child-sexual-abuse-material]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tacoma-man-who-persisted-in-drug-trafficking-despite-being-stopped-with-more-than-25-pounds-of-meth-sentenced-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tacoma-man-with-lengthy-criminal-history-pleads-guilty-to-gun-and-drug-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tattoo-shop-owner-pleads-guilty-to-distributing-heroin-and-methamphetamine-on-the-darknet]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tattoo-shop-owner-sentenced-to-more-than-7-years-in-prison-for-distributing-heroin-and-methamphetamine-on-the-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-ten-members-of-international-cyber-fraud-ring-indicted-for-refund-fraud-scheme-targeting-online-retailers]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tennessee-man-indicted-on-federal-charges-in-cyberstalking-and-identity-theft-case]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-texas-man-sentenced-to-15-years-in-prison-for-advertising-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-texas-man-sentenced-to-9-months-in-federal-prison-for-operating-website-that-offered-computer-attack-services]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-texas-residents-sentenced-for-their-involvement-in-a-counterfeit-prescription-drug-distribution-operation]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-the-drug-llama-pleads-guilty-to-distributing-fentanyl-on-the-dark-web]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-theodore-man-sentenced-to-prison-for-fraud-schemes-and-aggravated-identity-theft]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-third-defendant-pleads-guilty-to-hacking-fantasy-sports-and-betting-website]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-thirteen-people-indicted-in-drug-trafficking-conspiracy-involving-fentanyl-methamphetamine-and-cocaine]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-thompson-man-who-downloaded-child-sex-abuse-images-from-the-internet-is-sentenced]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-allegedly-responsible-for-distributing-thousands-of-fentanyl-pills-in-whatcom-county-indicted-for-drug-d]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-bay-area-defendants-charged-in-false-tax-refund-schemes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-defendants-in-significant-gun-and-drug-involved-cases-sentenced-to-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-defendants-indicted-on-federal-firearms-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-individuals-arrested-for-involvement-in-darknet-narcotics-trafficking-involving-pills-pressed-with-fenta]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-l-a-residents-charged-in-darknet-drug-ring-that-allegedly-shipped-methamphetamine-to-buyers-around-the-w]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-mexican-nationals-arrested-with-14-kilograms-of-crystal-methamphetamine]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-people-sentenced-to-prison-for-distributing-methamphetamine-fentanyl-and-nitazenes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-three-snohomish-county-men-indicted-for-drug-trafficking-conspiracy-involving-cocaine-fentanyl-and-firearms]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-thurston-county-man-caught-twice-with-drugs-and-firearms-sentenced-to-7-years-in-prison]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tohatchi-man-indicted-on-federal-assault-charges]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tulsa-man-sentenced-to-30-months-in-prison-for-sending-emails-threatening-to-kill-president-biden]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-tulsa-man-who-fled-from-smuggling-charge-pleads-guilty]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-twelve-defendants-convicted-in-cross-state-social-media-drug-trafficking-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-twelve-people-charged-in-two-indictments-following-investigation-of-drug-trafficking-ring]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-arrested-for-alleged-conspiracy-to-launder-4-5-billion-in-stolen-cryptocurrency]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-drug-traffickers-sentenced-to-lengthy-prison-terms-in-case-arising-from-investigation-of-aryan-family-pris]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-everett-residents-charged-federally-for-drug-distribution-activities-involving-multiple-kilos-of-fentanyl-]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-former-employees-of-house-member-indicted-on-federal-charges-in-cyberstalking-case]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-indicted-accused-of-harboring-aliens]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-indicted-for-drug-trafficking-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-individuals-sentenced-for-conspiracy-charges-involving-the-sale-of-fraudulent-identity-documents-on-the-da]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-members-of-multi-state-drug-trafficking-rings-linked-to-aryan-prison-gangs-sentenced-to-lengthy-prison-ter]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-men-charged-in-multi-million-dollar-darknet-drug-distribution-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-men-indicted-in-sim-swapping-scheme-to-steal-cryptocurrency]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-romanian-suspects-charged-with-hacking-of-metropolitan-police-department-surveillance-cameras-in-connectio]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-russian-nationals-charged-in-connection-with-operating-billion-dollar-money-laundering-services-justice-de]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-sacramento-men-indicted-for-distributing-cocaine-and-marijuana-on-dark-web-marketplaces]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-sentenced-in-dark-web-identity-theft-and-retail-fraud-conspiracy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-stockton-residents-charged-with-sexual-exploitation-of-a-minor]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-sudanese-nationals-indicted-for-alleged-role-in-anonymous-sudan-cyberattacks-on-hospitals-government-facil]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-texas-men-charged-in-stealing-over-a-million-dollars-in-a-romance-scam]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-tulsans-sentenced-for-running-illegal-dark-web-cryptocurrency-pharmacy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-two-virginia-men-arrested-for-conspiring-to-destroy-government-databases]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-u-k-citizen-sentenced-to-five-years-for-cybercrime-offenses]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-u-k-citizen-sentenced-to-five-years-in-prison-for-cybercrime-offenses]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-u-s-attorney-heap-announces-forfeiture-of-cryptocurrency-and-return-of-fraud-proceeds-to-victim]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-union-county-man-admits-to-possessing-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-union-county-new-jersey-man-charged-with-receiving-child-pornography]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-united-kingdom-national-pleads-guilty-to-hacking-securities-fraud-and-other-cybercrimes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-university-student-indicted-for-initiating-distributed-denial-of-service-attacks-on-bay-area-computers]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-charges-dual-russian-and-israeli-national-developer-lockbit-ransomware-group]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-aaron-michael-thomas]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-across-four-continents]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-adam-sloan]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-ahmed-salah-yousif-omer-and-alaa-salah-yusuuf-omer]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-alan-bill]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-aleksandr-stepanov-and-artem-aleksandrovich-kalinkin]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-alex-scott-roberts]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-alexander-aiello]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-alexander-james-rosell]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-alexey-bilyuchenko-and-aleksandr-verner]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-alexey-viktorovich-chertkov-kirill-vladimirovich-morozov-aleksandr-aleksandrovich-shi]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-amanda-rutherford]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-amir-hossein-golshan]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-amitoj-kapoor-and-siddharth-lillaney]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-and-prolific-child-molester]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-andrew-charles-nicholls]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-andrew-chu]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-andrew-shenkosky]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-andy-peter-vongdala]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-annie-nicole-ritenour]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-anthony-bellisario]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-anthony-dalton-wolff]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-anthony-joseph-carlson]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-anthony-raymond-dodd]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-antoin-austin]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-antonio-barner]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-anurag-pramod-murarka]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-april-henderson-and-donnell-timley]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-arbi-setaghaian-sangbarani]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-argishti-khudaverdyan]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-argishti-khudaverdyan-and-eagle-rock]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-ashton-connor-garcia]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-at-trial]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-auburn-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-austin-genay]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-baha-ibrahim-and-jawad-albadawi]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-beresford-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-bradley-lefebvre]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-brandon-robinson]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-brandon-spann]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-brought-against-bay-area]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-bryson-whiteside]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-bugat-botnet-administrator]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-carl-de-vera-bennington]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-catalin-dragomir]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-celeste-santifer]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-chandler-bennett]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-charges-hartford-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-charges-stamford-men]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-charges-waterbury-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-charles-thomas-abrahamson]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-charlestown-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-chris-ruediger]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-christerfer-frick]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-christhian-castillo]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-christopher-aaron-stanfield]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-christopher-lynn-driskill]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-christopher-scott-crawford]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-ciara-clutario]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-clayton-harker]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-colin-andrew-shapard]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-conor-brian-fitzpatrick]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-conway-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-corey-brossette]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-cory-hutcheson]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-cryptocurrency-exchange]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-daniel-faix]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-daniel-marsico]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-daniel-richter]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-dark-web-drug-trafficker]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-dark-web-marketplace]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-darkweb-drug-trafficker]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-david-brian-pate-and-jose-luis-fung-hou]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-david-mark-bartels]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-david-tinley]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-davit-avalyan]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-defendant-nicole-dunlap-and-marcus-smith]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-demario-sorrells]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-deniss-zolotarjovs]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-dequan-lamar-mitchell]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-devlin-hosner-and-holly-adams]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-district-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-dmitry-aleksandrovich-dokuchaev-and-igor-anatolyevich-sushchin]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-donald-ryan-austin]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-donjuan-murphy]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-dustin-carl-wurges-and-jonathan-mayhall]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-dutch-national]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-east-hartford-man]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-eddy-steven-sandoval-lopez]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-edmond-chakhmakhchyan]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-edward-shia]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-elizabeth-calderon]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-emerson-hayes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-ephraim-rosenberg]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-eric-caleb-carlson]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-eric-council]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-eric-scholl]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-eric-smith-and-sara-thompson]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-evan-baltierra]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-evan-hayes]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-evan-tangeman]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-evgenii-ptitsyn]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-fatiu-ismaila-lawal-and-sakiru-olanrewaju-ambali]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-felon-sentenced-and-previously-convicted-felon]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-filip-lucian-simion]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-firas-bashiti]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-following-seizure-and-forfeiture-and-dark-web-fraud-defendant]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-for-hacking]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-for-initiating-distributed-denial]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-for-operating-alleged-international-and-national-and-bitcoin-exchange]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-for-possessing-child-sexual]] | 1 | 0 | 1 | 0 | united-states |
| [[operation-us-v-for-possession-of-child-and-marion-county-man]] | 1 | 0 | 1 | 0 | united-states |

_…294 more rows truncated._

## Operations fully verified (every country in local text)

- [[2bagoldmule-qqaazz]] — 16 countries
- [[africa-cyber-surge-ii]] — 7 countries
- [[andromeda-botnet-takedown]] — 17 countries
- [[bali-villa-cybercrime-raid-2024]] — 1 countries
- [[bec-nigeria-2016]] — 2 countries
- [[belgium-netherlands-phishing-gang]] — 2 countries
- [[black-axe-bec-2021]] — 6 countries
- [[blackcat-lockeroga-kelvin-security-2023]] — 4 countries
- [[carding-action-2020]] — 3 countries
- [[cyber-fraud-international-2015]] — 6 countries
- [[cyberbunker-takedown]] — 2 countries
- [[de-ch-crypto-mixer-takedown-2025]] — 2 countries
- [[emotet-takedown]] — 8 countries
- [[fin7-takedown]] — 4 countries
- [[franco-israeli-ceo-fraud]] — 6 countries
- [[imminent-monitor-rat-takedown]] — 8 countries
- [[infraud-telusma-sentencing]] — 1 countries
- [[korea-cambodia-scam-repatriation]] — 2 countries
- [[korea-china-voice-phishing-qingdao]] — 2 countries
- [[marketplace-a-dekhtyarchuk-indictment]] — 2 countries
- [[myanmar-kokang-scam-compound-crackdown]] — 2 countries
- [[nigerian-bec-convictions-2023]] — 2 countries
- [[operation-105-arrested-for-stealing-over-eur-12-million-from-us-based-banks]] — 5 countries
- [[operation-12-members-of-an-irish-high-risk-criminal-network-arrested]] — 5 countries
- [[operation-150-arrested-in-dark-web-drug-bust-as-police-seize-eur-26-million]] — 1 countries
- [[operation-administrator-of-online-criminal-marketplace-extradited-from-kosovo-to-the-united-states]] — 1 countries
- [[operation-alleged-russian-cryptocurrency-money-launderer-extradited-to-united-states]] — 1 countries
- [[operation-almost-1-000-suspects-arrested-in-interpol-operation-which-seized-over-129-million]] — 1 countries
- [[operation-bakovia]] — 4 countries
- [[operation-brazilian-extradited-from-switzerland-to-the-united-states-to-face-indictment-charging-involvement-in-290m-cry]] — 1 countries
- [[operation-bremerton-washington-man-sentenced-to-3-years-in-prison-for-extensive-swatting-campaign-targeting-victims-in-u]] — 2 countries
- [[operation-chakra-iii]] — 2 countries
- [[operation-checkmate-blacksuit]] — 4 countries
- [[operation-cronos-phase1]] — 14 countries
- [[operation-cronos-phase3]] — 12 countries
- [[operation-cyber-guardian]] — 6 countries
- [[operation-dark-web-narcotics-trafficker-sentenced-to-96-months-in-prison-for-distributing-fentanyl-heroin-methamphetamin]] — 4 countries
- [[operation-de-fr-online-fraud-group-2026]] — 2 countries
- [[operation-destabilise]] — 2 countries
- [[operation-dual-russian-and-israeli-national-extradited-to-the-united-states-for-his-role-in-the-lockbit-ransomware-consp]] — 1 countries
- [[operation-emotet-disruption-ladybird]] — 1 countries
- [[operation-endgame]] — 15 countries
- [[operation-endgame-phase1]] — 13 countries
- [[operation-endgame-phase2]] — 7 countries
- [[operation-eur-100m-crypto-investment-fraud-2025]] — 6 countries
- [[operation-eur-100m-illegal-financial-service-laundering-2025]] — 4 countries
- [[operation-europol-mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain-carbanak-cobalt]] — 1 countries
- [[operation-first-light-2024]] — 1 countries
- [[operation-foreign-national-sentenced-for-victimizing-u-s-persons-through-cyber-enabled-fraud-schemes]] — 1 countries
- [[operation-foreign-nationals-sentenced-for-roles-in-transnational-cybercrime-enterprise]] — 1 countries
- [[operation-germany-romania-trusted-seller-fraud-2025]] — 3 countries
- [[operation-goldfish-alpha-night-fury]] — 7 countries
- [[operation-haechi-ii]] — 18 countries
- [[operation-haechi-iii]] — 30 countries
- [[operation-haechi-iv]] — 8 countries
- [[operation-haechi-v]] — 2 countries
- [[operation-heart-blocker]] — 3 countries
- [[operation-hook-line-and-sinker-cybercrime-network-phishing-bank-credentials-arrested-in-romania]] — 1 countries
- [[operation-hyperion]] — 1 countries
- [[operation-interpol-online-scamming-fraud-three-nigerians-arrested-in-operation-killer-bee]] — 1 countries
- [[operation-interpol-seized-130-million-from]] — 1 countries
- [[operation-interpol-seized-130-million-from-cybercriminals-in-global-haechi-iii-crackdown]] — 1 countries
- [[operation-interpol-seized-130-million-from-cybercriminals-worldwide]] — 1 countries
- [[operation-jackal]] — 21 countries
- [[operation-jackal-iii]] — 1 countries
- [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested]] — 1 countries
- [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown]] — 3 countries
- [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-2]] — 1 countries
- [[operation-key-figures-behind-phobos-and-8base-ransomware-arrested-in-international-cybercrime-crackdown-3]] — 3 countries
- [[operation-key-player-in-silk-road-2-0-sentenced-to-eight-years-in-prison]] — 1 countries
- [[operation-killer-bee]] — 11 countries
- [[operation-kokomo-resident-arrested-on-federal-animal-cruelty-charges]] — 1 countries
- [[operation-kraken-ghost-platform]] — 9 countries
- [[operation-massachusetts-man-pleads-guilty-to-firearm-offenses-and-unlawful-entry-into-the-u-s]] — 1 countries
- [[operation-mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain]] — 1 countries
- [[operation-moldovan-botnet-operator-indicted-for-role-in-conspiracy-to-unlawfully-access-thousands-of-infected-computers-]] — 1 countries
- [[operation-multiple-foreign-nationals-charged-in-connection-with-trickbot-malware-and-conti-ransomware-conspiracies]] — 1 countries
- [[operation-norton-shores-dark-web-drug-dealer-sentenced-to-30-months-in-prison]] — 1 countries
- [[operation-online-scamming-fraud-three-nigerians-arrested-in-interpol-operation-killer-bee]] — 1 countries
- [[operation-onymous]] — 17 countries
- [[operation-oregon-man-sentenced-to-federal-prison-for-attempting-to-sell-cocaine-purchased-from-the-dark-web]] — 1 countries
- [[operation-orion-international]] — 12 countries
- [[operation-pennsylvania-man-sentenced-to-life-in-federal-prison-for-dealing-fentanyl-analogue-that-caused-fatal-overdoses]] — 1 countries
- [[operation-pittsburgh-resident-and-darknet-drug-trafficker-sentenced-to-nearly-six-years-in-prison-on-federal-drug-traffi]] — 1 countries
- [[operation-pleiades]] — 10 countries
- [[operation-power-off]] — 15 countries
- [[operation-ransomware-administrator-charged-with-cybercrimes-for-deploying-lockergoga-nefilim-and-megacortex-ransomware-s]] — 1 countries
- [[operation-russian-malware-developer-arrested-and-extradited-to-the-united-states]] — 1 countries
- [[operation-russian-national-charged-with-decade-long-series-of-hacking-and-bank-fraud-offenses-resulting-in-tens-of-milli-2]] — 1 countries
- [[operation-rydox-cybercrime-marketplace-shut-down-and-three-administrators-arrested]] — 1 countries
- [[operation-secreto]] — 5 countries
- [[operation-sentinel-africa]] — 19 countries
- [[operation-seven-charged-after-federal-investigation-disrupts-massive-counterfeit-pill-manufacturing-operation]] — 1 countries
- [[operation-source]] — 3 countries
- [[operation-stream-kidflix]] — 2 countries
- [[operation-talent]] — 8 countries
- [[operation-texas-business-executive-sentenced-to-prison-for-illegally-selling-oxycodone-on-silk-road]] — 1 countries
- [[operation-thirty-six-defendants-indicted-for-alleged-roles-in-transnational-criminal-organization-responsible-for-more-t]] — 1 countries
- [[operation-three-arrested-as-interpol-group-ib-and-the-nigeria-police-force-disrupt-prol]] — 1 countries
- [[operation-three-darknet-fentanyl-vendors-sentenced-to-over-20-years-in-prison]] — 1 countries
- [[operation-three-former-department-of-homeland-security-employees-sentenced-in-scheme-to-defraud-the-united-states]] — 1 countries
- [[operation-three-individuals-sentenced-in-darknet-narcotics-trafficking-conspiracy-involving-distribution-of-pills-presse]] — 1 countries
- [[operation-three-members-of-goznym-cybercrime-network-sentenced-in-parallel-multi-national-prosecutions-in-pittsburgh-and]] — 1 countries
- [[operation-trojan-shield]] — 6 countries
- [[operation-two-estonian-citizens-arrested-in-575-million-cryptocurrency-fraud-and-money-laundering-scheme]] — 1 countries
- [[operation-two-men-charged-for-breaching-federal-law-enforcement-database-and-posing-as-police-officers-to-defraud-social]] — 1 countries
- [[operation-two-men-indicted-for-international-conspiracy-to-ship-fentanyl-other-drugs-into-united-states-through-dark-web]] — 1 countries
- [[operation-two-southern-california-men-who-supplied-fentanyl-sold-to-darknet-customers-in-all-50-states-sentenced-to-fede]] — 1 countries
- [[operation-u-k-citizen-extradited-and-pleads-guilty-to-cybercrime-offenses]] — 1 countries
- [[operation-u-s-based-conspirators-sentenced-to-prison-for-international-tax-scheme]] — 1 countries
- [[operation-ukrainian-cyber-criminal-extradited-for-decrypting-the-credentials-of-thousands-of-computers-across-the-world-]] — 1 countries
- [[operation-united-states-seized-and-files-forfeiture-action-to-recover-over-54-million-of-cryptocurrency-traceable-to-nar]] — 1 countries
- [[operation-us-v-adafin-xdedic]] — 1 countries
- [[operation-us-v-adam-lemar-miles]] — 1 countries
- [[operation-us-v-adam-miles-dark-web]] — 1 countries
- [[operation-us-v-adan-ruiz-and-omar-navia]] — 1 countries
- [[operation-us-v-adejumo-jinadu-xdedic]] — 1 countries
- [[operation-us-v-adetunji-adejumo-and-ibrahim-jinadu]] — 1 countries
- [[operation-us-v-aidan-curry-and-connor-brooke]] — 1 countries
- [[operation-us-v-akshay-ram-kancharla]] — 1 countries
- [[operation-us-v-alex-ogando-olatunji-dawodu-and-luis-spencer]] — 1 countries
- [[operation-us-v-alexander-vinnik]] — 1 countries
- [[operation-us-v-allen-d-lint]] — 1 countries
- [[operation-us-v-almashwali-alphabay]] — 1 countries
- [[operation-us-v-anom-distributors]] — 1 countries
- [[operation-us-v-aragon-dark-web]] — 1 countries
- [[operation-us-v-ardit-kutleshi-and-jetmir-kutleshi]] — 1 countries
- [[operation-us-v-astamirov-vasiliev-lockbit]] — 1 countries
- [[operation-us-v-banmeet-singh-dark-web]] — 1 countries
- [[operation-us-v-barraza-flores-dark-web]] — 1 countries
- [[operation-us-v-benthall-silk-road-2]] — 1 countries
- [[operation-us-v-bondarenko-infraud]] — 1 countries
- [[operation-us-v-bookman-dark-web]] — 1 countries
- [[operation-us-v-brandon-adams-dark-web]] — 1 countries
- [[operation-us-v-brandon-arias-dark-web]] — 1 countries
- [[operation-us-v-brewer-dark-web]] — 1 countries
- [[operation-us-v-brian-mcdonald-dark-web]] — 1 countries
- [[operation-us-v-brian-richard-farrell]] — 1 countries
- [[operation-us-v-bryan-connor-herrell]] — 1 countries
- [[operation-us-v-burgamy-wilson-dark-web]] — 1 countries
- [[operation-us-v-california-teenager]] — 1 countries
- [[operation-us-v-castillo-rosario-vasquez-roman-dark-web]] — 1 countries
- [[operation-us-v-castro-dark-web]] — 1 countries
- [[operation-us-v-catherine-stuckey-dark-web]] — 1 countries
- [[operation-us-v-cazes-alphabay]] — 1 countries
- [[operation-us-v-chaloner-saintillus-dark-web]] — 1 countries
- [[operation-us-v-charges-man]] — 1 countries
- [[operation-us-v-charging-involvement]] — 1 countries
- [[operation-us-v-cheerish-noel-taylor-and-robert-james-fischer]] — 1 countries
- [[operation-us-v-curry-brooke-dark-web]] — 1 countries
- [[operation-us-v-de-los-santos]] — 1 countries
- [[operation-us-v-dekhtyarchuk-marketplace-a]] — 1 countries
- [[operation-us-v-devin-shanahan]] — 1 countries
- [[operation-us-v-dittman-schiffner-langer-dark-web]] — 1 countries
- [[operation-us-v-dominick-jeffrey-aragon]] — 1 countries
- [[operation-us-v-easton-man]] — 1 countries
- [[operation-us-v-evan-hernandez-dark-web]] — 1 countries
- [[operation-us-v-evan-jaime-hernandez]] — 1 countries
- [[operation-us-v-farrell-silk-road-2]] — 1 countries
- [[operation-us-v-fatukala-cocaine-dark-web]] — 1 countries
- [[operation-us-v-fatukala-yamamoto-mina-and-hollis]] — 1 countries
- [[operation-us-v-for-receipt-of]] — 1 countries
- [[operation-us-v-foreign-nationals]] — 1 countries
- [[operation-us-v-galochkin-trickbot-conti]] — 1 countries
- [[operation-us-v-gary-davis-silk-road]] — 1 countries
- [[operation-us-v-george-sotiris-vlastos]] — 1 countries
- [[operation-us-v-ghinkul-dridex]] — 1 countries
- [[operation-us-v-glib-ivanov-tolpintsev]] — 1 countries
- [[operation-us-v-gregory-castillo-rosario-joseph-james-vasquez-joshua-william-vas]] — 1 countries
- [[operation-us-v-gudmunds-darkode]] — 1 countries
- [[operation-us-v-gutierrez-villasenor-dark-web]] — 1 countries
- [[operation-us-v-haahr-albert-dark-web]] — 1 countries
- [[operation-us-v-habasescu-xdedic]] — 1 countries
- [[operation-us-v-haney-silk-road]] — 1 countries
- [[operation-us-v-hardened-encrypted-devices]] — 1 countries
- [[operation-us-v-hernandez-dark-web]] — 1 countries
- [[operation-us-v-herrell-alphabay]] — 1 countries
- [[operation-us-v-holly-adams-dark-web]] — 1 countries
- [[operation-us-v-homeland-security-employees]] — 1 countries
- [[operation-us-v-hugh-brian-haney]] — 1 countries
- [[operation-us-v-ilya-lichtenstein-and-heather-morgan]] — 1 countries
- [[operation-us-v-indicted-for-role-in]] — 1 countries
- [[operation-us-v-ivanov-tolpintsev-xdedic]] — 1 countries
- [[operation-us-v-jason-arnold-dark-web]] — 1 countries
- [[operation-us-v-john-cruz-dark-web]] — 1 countries
- [[operation-us-v-john-mckernan-dark-web]] — 1 countries
- [[operation-us-v-jose-rodolfo-barraza-flores]] — 1 countries
- [[operation-us-v-kancharla-dark-web]] — 1 countries
- [[operation-us-v-kharmanskyi-xdedic]] — 1 countries
- [[operation-us-v-khlari-sirotkin-and-sean-deaver]] — 1 countries
- [[operation-us-v-konovolov-goznym]] — 1 countries
- [[operation-us-v-krasimir-nikolov]] — 1 countries
- [[operation-us-v-krystal-cherika-scott]] — 1 countries
- [[operation-us-v-kutleshi-rydox]] — 1 countries
- [[operation-us-v-levinson-xdedic]] — 1 countries
- [[operation-us-v-lint-dream-market]] — 1 countries
- [[operation-us-v-luis-teixeira-da-silva]] — 1 countries
- [[operation-us-v-madding-dark-web]] — 1 countries
- [[operation-us-v-matthew-jones-silk-road]] — 1 countries
- [[operation-us-v-mckinzie-xdedic]] — 1 countries
- [[operation-us-v-mcneely-xdedic]] — 1 countries
- [[operation-us-v-michael-carlton-paiva]] — 1 countries
- [[operation-us-v-miller-poweroff]] — 1 countries
- [[operation-us-v-nazarovi-qqaazz]] — 1 countries
- [[operation-us-v-nicholas-partlow-dark-web]] — 1 countries
- [[operation-us-v-odedeyi-davies-xdedic]] — 1 countries
- [[operation-us-v-odufuye-nwoke-bec]] — 1 countries
- [[operation-us-v-of-silk-road]] — 1 countries
- [[operation-us-v-ogando-dawodu-spencer-dark-web]] — 1 countries
- [[operation-us-v-ogunlana-xdedic]] — 1 countries
- [[operation-us-v-okparaeke-dark-web]] — 1 countries
- [[operation-us-v-okpe-obogo-bec]] — 1 countries
- [[operation-us-v-olivia-bolles-silk-road]] — 1 countries
- [[operation-us-v-olufemi-odedeyi-and-ibrahim-davies]] — 1 countries
- [[operation-us-v-omotosho-xdedic]] — 1 countries
- [[operation-us-v-orgil-dark-web]] — 1 countries
- [[operation-us-v-oyebanjo-xdedic]] — 1 countries
- [[operation-us-v-paiva-silk-road-2]] — 1 countries
- [[operation-us-v-pankov-xdedic]] — 1 countries
- [[operation-us-v-peck-dark-web]] — 1 countries
- [[operation-us-v-pedro-marquez-benetiz]] — 1 countries
- [[operation-us-v-ransomware-administrator]] — 1 countries
- [[operation-us-v-roberts-dark-web]] — 1 countries
- [[operation-us-v-roger-thomas-clark-silk-road]] — 1 countries
- [[operation-us-v-rostislav-panev]] — 1 countries
- [[operation-us-v-ruiz-navia-dark-web]] — 1 countries
- [[operation-us-v-ruslan-astamirov-and-mikhail-vasiliev]] — 1 countries
- [[operation-us-v-ryan-scott-cochran-dark-web]] — 1 countries
- [[operation-us-v-sabbagh-dark-web]] — 1 countries
- [[operation-us-v-scanlan-dark-web]] — 1 countries
- [[operation-us-v-shaughnessy-dark-web]] — 1 countries
- [[operation-us-v-sheldon-kennedy-silk-road]] — 1 countries
- [[operation-us-v-sirotkin-deaver-dark-web]] — 1 countries
- [[operation-us-v-solomon-ekunke-okpe-and-johnson-uke-obogo]] — 1 countries
- [[operation-us-v-spencer-xdedic]] — 1 countries
- [[operation-us-v-stepanov-danabot]] — 1 countries
- [[operation-us-v-t-andre-mcneely]] — 1 countries
- [[operation-us-v-tan-dark-web]] — 1 countries
- [[operation-us-v-taylor-fischer-dark-web]] — 1 countries
- [[operation-us-v-taylor-xdedic]] — 1 countries
- [[operation-us-v-telusma-infraud]] — 1 countries
- [[operation-us-v-timothy-dalton-vaughn]] — 1 countries
- [[operation-us-v-two-men]] — 1 countries
- [[operation-us-v-udvardi-dark-web]] — 1 countries
- [[operation-us-v-ulbricht]] — 1 countries
- [[operation-us-v-vallerius-dream-market]] — 1 countries
- [[operation-us-v-veronica-dittman-rick-schiffner-and-devin-langer]] — 1 countries
- [[operation-us-v-vlastos-dark-web]] — 1 countries
- [[operation-us-v-witters-dark-web]] — 1 countries
- [[operation-us-v-yakubets-dridex]] — 1 countries
- [[operation-us-v-yunhe-wang-911-s5]] — 1 countries
- [[operation-us-v-yutong-zhang]] — 1 countries
- [[operation-usd-257-million-seized-in-global-police-crackdown-against-online-scams-operation-first-light-2024]] — 1 countries
- [[operation-usd-257-million-seized-in-global-police-crackdown-against-online-scams-operation-first-light-2024-2]] — 1 countries
- [[operation-usd-257-million-seized-in-global-police-crackdown-against-online-scams-operation-first-light-2024-3]] — 1 countries
- [[operation-usd-300-million-seized-and-3-500-suspects-arrested-in-international-financial-crime-operation-operation-haechi]] — 1 countries
- [[operation-usd-300-million-seized-and-3-500-suspects-arrested-operation-haechi-iv]] — 1 countries
- [[operation-usps-employee-indicted-for-misappropriation-of-funds]] — 1 countries
- [[operation-wirewire]] — 5 countries
- [[phobos-8base-crackdown]] — 15 countries
- [[proxy-service-takedown-2026-03]] — 4 countries
- [[qqaazz-money-laundering-takedown]] — 7 countries
- [[rex-mundi-takedown]] — 3 countries
- [[romania-phishing-takedown-2024]] — 1 countries
- [[rydox-marketplace-takedown]] — 4 countries
- [[silk-road-takedown]] — 5 countries
- [[simda-botnet-takedown]] — 7 countries
- [[trickbot-operations]] — 2 countries
- [[vpnlab-takedown]] — 10 countries
- [[xdedic-marketplace-takedown]] — 3 countries
- [[zambia-golden-top-call-center]] — 2 countries
- [[zeus-spyeye-jit-takedown]] — 3 countries