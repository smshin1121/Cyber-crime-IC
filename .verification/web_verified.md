# participating_countries — web primary-source verification (curl_cffi)

_Run: 2026-04-21 10:05_

Fetched via curl_cffi with Chrome TLS fingerprint impersonation (bypasses Cloudflare on most static press releases). For each op in the verification queue, every country in its `participating_countries` is checked against the rendered text of all cited source URLs.

- **verified_union** — country explicitly named in ≥1 source page
- **still_missing** — country NOT found in any reachable source
- Fetch errors (Cloudflare challenge still unsolved, 403, 404 etc.) are recorded per URL

## Summary

- Operations processed: 100
- Fully verified (every frontmatter country named in a source): 23
- Partially verified: 1
- Nothing verified (all sources failed): 76

## Results

### operation-haechi-vi

**Title**: Operation HAECHI VI

**Participating (frontmatter, 32)**: south-korea, portugal, thailand, united-arab-emirates, japan, albania, argentina, armenia, australia, brazil, bulgaria, cambodia, canada, china, germany, ghana, india, indonesia, ireland, kazakhstan, malaysia, nigeria, philippines, poland, romania, singapore, south-africa, spain, sweden, united-kingdom, united-states, vietnam

**Verified via web (32)**: albania, argentina, armenia, australia, brazil, bulgaria, cambodia, canada, china, germany, ghana, india, indonesia, ireland, japan, kazakhstan, malaysia, nigeria, philippines, poland, portugal, romania, singapore, south-africa, south-korea, spain, sweden, thailand, united-arab-emirates, united-kingdom, united-states, vietnam

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.interpol.int/en/News-and-Events/News/2025/USD-439-million-recovered- | INTERPOL | 6792 | south-korea, portugal, thailand, united-arab-emirates, japan, albania, argentina, armenia, australia, brazil, bulgaria,  |  |

### operation-eur-300m-global-credit-card-fraud-2025

**Title**: EUR 300 Million Global Credit Card Fraud Operation (2025)

**Participating (frontmatter, 10)**: germany, cyprus, italy, luxembourg, netherlands, spain, united-kingdom, united-states, canada, singapore

**Verified via web (10)**: canada, cyprus, germany, italy, luxembourg, netherlands, singapore, spain, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.eurojust.europa.eu/news/eurojust-coordinates-major-operation-against | Eurojust | 15550 | germany, cyprus, italy, luxembourg, netherlands, spain, united-kingdom, united-states, canada, singapore |  |

### darkmarket-takedown

**Title**: DarkMarket Marketplace Takedown

**Participating (frontmatter, 7)**: germany, australia, united-kingdom, united-states, ukraine, moldova, denmark

**Verified via web (7)**: australia, denmark, germany, moldova, ukraine, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/darkmarket-worlds-larges | Europol | 36600 | germany, australia, united-kingdom, united-states, ukraine, moldova, denmark |  |
| https://thehackernews.com/2021/01/authorities-take-down-worlds-largest.html | The Hacker News | 7326 | germany, australia, ukraine, moldova, denmark |  |
| https://www.rferl.org/a/ukraine-moldova-servers-seized-germany-busts-darknet-ope | RFE/RL | 0 |  | http_403 |
| https://www.sbs.com.au/news/article/australian-man-arrested-in-germany-accused-o | SBS News | 4224 | germany, australia, ukraine, moldova |  |
| https://www.dea.gov/press-releases/2021/10/26/department-justice-announces-resul | US DOJ/DEA | 18545 | germany, australia, united-kingdom, united-states |  |

### operation-us-v-parsarad-nemesis

**Title**: Behrouz Parsarad Enforcement Action

**Participating (frontmatter, 3)**: united-states, germany, lithuania

**Verified via web (3)**: germany, lithuania, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/administrator-nemesis-market-charged-role-operati | U.S. Department of Justice | 0 |  | http_404 |
| https://www.justice.gov/usao-ndoh/pr/iranian-national-indicted-operating-online- | US DOJ USAO | 0 |  | empty_body |
| https://home.treasury.gov/news/press-releases/sb0040 | U.S. Department of the Treasury | 17311 | united-states, germany, lithuania |  |
| https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2024/Presse2024/2403 | Bundeskriminalamt / ZIT Frankfurt | 5215 | lithuania |  |
| https://www.justice.gov/opa/pr/iranian-national-indicted-operating-online-market | US DOJ (Office of Public Affairs) | 9701 | united-states, germany, lithuania |  |

### doublevpn-takedown

**Title**: DoubleVPN Takedown

**Participating (frontmatter, 9)**: netherlands, united-states, canada, germany, united-kingdom, sweden, italy, bulgaria, switzerland

**Verified via web (9)**: bulgaria, canada, germany, italy, netherlands, sweden, switzerland, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.eurojust.europa.eu/news/coordinated-action-cuts-access-vpn-service-u | Eurojust | 13554 | netherlands, united-states, canada, germany, united-kingdom, sweden, italy, bulgaria, switzerland |  |
| https://www.eurojust.europa.eu/annual-report-2021/cybercrime/case-examples | Eurojust | 17004 | netherlands, united-states, canada, germany, united-kingdom, sweden, italy, bulgaria |  |
| https://www.nationalcrimeagency.gov.uk/news/doublevpn-takedown-nca-takes-uk-serv | UK NCA | 4855 | netherlands, united-states, canada, united-kingdom |  |
| https://therecord.media/dutch-police-takes-down-doublevpn-a-service-used-by-cybe | The Record | 3454 | netherlands, united-states, canada, germany, united-kingdom, sweden, italy, bulgaria, switzerland |  |

### operation-dark-huntor

**Title**: Operation Dark HunTOR

**Participating (frontmatter, 9)**: australia, bulgaria, france, germany, italy, netherlands, switzerland, united-kingdom, united-states

**Verified via web (9)**: australia, bulgaria, france, germany, italy, netherlands, switzerland, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/150-arrested-in-dark-web | Europol | 39536 | australia, bulgaria, france, germany, italy, netherlands, switzerland, united-kingdom, united-states |  |
| https://www.dea.gov/press-releases/2021/10/26/department-justice-announces-resul | US DOJ/DEA | 18545 | australia, bulgaria, france, germany, italy, netherlands, switzerland, united-kingdom, united-states |  |
| https://www.justice.gov/archives/opa/speech/deputy-attorney-general-lisa-o-monac | US DOJ | 0 |  | empty_body |
| https://www.nationalcrimeagency.gov.uk/news/international-operation-targets-dark | UK NCA | 5285 | australia, bulgaria, france, germany, italy, netherlands, switzerland, united-kingdom, united-states |  |
| https://www.europol.europa.eu/media-press/newsroom/news/darkmarket-worlds-larges | Europol | 36600 | australia, bulgaria, france, germany, italy, netherlands, united-kingdom, united-states |  |

### operation-eur-3m-online-investment-fraud-2025

**Title**: EUR 3 Million Online Investment Fraud Coalition Action (2025)

**Participating (frontmatter, 7)**: germany, cyprus, albania, united-kingdom, israel, belgium, latvia

**Verified via web (7)**: albania, belgium, cyprus, germany, israel, latvia, united-kingdom

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.eurojust.europa.eu/news/international-coalition-uncovers-eur-3-milli | Eurojust | 12931 | germany, cyprus, albania, united-kingdom, israel, belgium, latvia |  |

### operation-eur-600m-crypto-scam-network-2025

**Title**: EUR 600 Million Crypto Scam Network Takedown (2025)

**Participating (frontmatter, 5)**: belgium, cyprus, france, germany, spain

**Verified via web (5)**: belgium, cyprus, france, germany, spain

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.eurojust.europa.eu/news/decisive-actions-against-cryptocurrency-scam | Eurojust | 11522 | belgium, cyprus, france, germany, spain |  |

### operation-europol-105-arrested-for-stealing-over-12-million-from-us-based-banks-operation-secreto

**Title**: Europol: 105 Arrested for Stealing Over €12 Million from US-Based Banks (Operation Secreto) Enforcement Action

**Participating (frontmatter, 6)**: austria, denmark, greece, spain, united-kingdom, united-states

**Verified via web (6)**: austria, denmark, greece, spain, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/105-arrested-for-stealin | Europol | 41047 | austria, denmark, greece, spain, united-kingdom, united-states |  |

### operation-europol-french-coder-who-helped-extort-british-company-arrested-in-thailand

**Title**: Europol: French coder who helped extort British company arrested in Thailand Enforcement Action

**Participating (frontmatter, 4)**: belgium, france, thailand, united-kingdom

**Verified via web (4)**: belgium, france, thailand, united-kingdom

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/french-coder-who-helped- | Europol | 33351 | belgium, france, thailand, united-kingdom |  |

### alphabay-takedown

**Title**: Operation Bayonet -- AlphaBay & Hansa Takedown

**Participating (frontmatter, 8)**: united-states, thailand, netherlands, lithuania, canada, united-kingdom, france, germany

**Verified via web (0)**: —

**Still missing (8)**: canada, france, germany, lithuania, netherlands, thailand, united-kingdom, united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|

### bidencash-takedown

**Title**: BidenCash Marketplace Seizure

**Participating (frontmatter, 6)**: united-states, netherlands, finland, germany, france, denmark

**Verified via web (0)**: —

**Still missing (6)**: denmark, finland, france, germany, netherlands, united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|

### carbanak-cobalt-takedown

**Title**: Carbanak/Cobalt Mastermind Arrest

**Participating (frontmatter, 6)**: spain, united-states, romania, moldova, belarus, taiwan

**Verified via web (3)**: romania, spain, united-states

**Still missing (3)**: belarus, moldova, taiwan

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1- | Europol | 35870 | spain, united-states, romania |  |
| https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ | Kaspersky Securelist | 23200 | spain, united-states |  |
| https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.p | Europol | 1137912 | united-states |  |
| https://www.fbi.gov/contact-us/field-offices/seattle/news/stories/how-cyber-crim | FBI | 8008 | united-states |  |

### cryptex-pm2btc-sanctions

**Title**: Cryptex and PM2BTC Coordinated Sanctions and Seizure Action

**Participating (frontmatter, 2)**: united-states, netherlands

**Verified via web (2)**: netherlands, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://home.treasury.gov/news/press-releases/jy2616 | U.S. Department of the Treasury | 20310 | united-states, netherlands |  |
| https://www.justice.gov/archives/opa/pr/two-russian-nationals-charged-connection | US Department of Justice | 0 |  | empty_body |
| https://www.fincen.gov/news/news-releases/treasury-takes-coordinated-actions-aga | Financial Crimes Enforcement Network | 11380 | united-states, netherlands |  |
| https://www.fincen.gov/resources/statutes-regulations/federal-register-notices/i | Financial Crimes Enforcement Network | 2092 | united-states |  |
| https://www.justice.gov/usao-edva/pr/two-russian-nationals-charged-connection-op | U.S. Attorney's Office, Eastern District of Virginia | 0 |  | empty_body |
| https://www.chainalysis.com/blog/ofac-sanctions-russian-exchange-cryptex-uaps-fr | Chainalysis | 12397 | united-states, netherlands |  |

### dridex-operations

**Title**: Dridex/Evil Corp Disruption and Prosecution

**Participating (frontmatter, 5)**: united-states, united-kingdom, germany, moldova, cyprus

**Verified via web (0)**: —

**Still missing (5)**: cyprus, germany, moldova, united-kingdom, united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|

### isoon-apt27-indictment

**Title**: i-Soon/APT27 Indictment (Chinese Contract Hackers)

**Participating (frontmatter, 2)**: united-states, china

**Verified via web (2)**: china, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/justice-department-charges-12-chinese-contract-ha | US Department of Justice | 17645 | united-states, china |  |

### lumma-stealer-takedown

**Title**: Lumma Stealer Takedown

**Participating (frontmatter, 2)**: united-states, japan

**Verified via web (2)**: japan, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://blogs.microsoft.com/on-the-issues/2025/05/21/microsoft-leads-global-acti | Microsoft | 10170 | united-states, japan |  |
| https://www.justice.gov/opa/pr/justice-department-seizes-domains-behind-major-in | U.S. Department of Justice | 9147 | united-states |  |
| https://www.microsoft.com/en-us/security/blog/2025/05/21/lumma-stealer-breaking- | Microsoft Security Blog | 34761 | united-states |  |

### nemesis-market-takedown

**Title**: Nemesis Market Takedown

**Participating (frontmatter, 3)**: germany, united-states, lithuania

**Verified via web (3)**: germany, lithuania, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2024/Presse2024/2403 | Bundeskriminalamt / ZIT Frankfurt | 5215 | lithuania |  |
| https://www.justice.gov/opa/pr/administrator-nemesis-market-charged-role-operati | U.S. Department of Justice | 0 |  | http_404 |
| https://www.justice.gov/usao-ndoh/pr/iranian-national-indicted-operating-online- | US DOJ USAO | 0 |  | empty_body |
| https://home.treasury.gov/news/press-releases/sb0040 | U.S. Department of the Treasury | 17311 | germany, united-states, lithuania |  |

### operation-16-defendants-federally-charged-in-connection-with-danabot-malware-scheme-that-infected-computers-worldwide

**Title**: 16 Defendants Federally Charged in Connection with DanaBot Malware Scheme That Infected Computers Worldwide Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-cdca/pr/16-defendants-federally-charged-connection- | US DOJ USAO | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-2

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-3

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-4

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-5

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-6

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-19-individuals-worldwide-charged-in-transnational-cybercrime-investigation-of-the-xdedic-marketplace-7

**Title**: 19 Individuals Worldwide Charged In Transnational Cybercrime Investigation Of The xDedic Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/19-individuals-worldwide-charged-transnatio | US DOJ (Middle District of Florida) | 0 |  | empty_body |

### operation-australian-man-arrested-in-germany-accused-of-running-world-s-largest-darknet-marketplace

**Title**: Australian DarkMarket Operator Arrest Enforcement Action

**Participating (frontmatter, 4)**: germany, australia, moldova, ukraine

**Verified via web (4)**: australia, germany, moldova, ukraine

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/darkmarket-worlds-larges | Europol | 36600 | germany, australia, moldova, ukraine |  |
| https://thehackernews.com/2021/01/authorities-take-down-worlds-largest.html | The Hacker News | 7326 | germany, australia, moldova, ukraine |  |
| https://www.rferl.org/a/ukraine-moldova-servers-seized-germany-busts-darknet-ope | RFE/RL | 0 |  | http_403 |
| https://www.sbs.com.au/news/article/australian-man-arrested-in-germany-accused-o | SBS News | 4224 | germany, australia, moldova, ukraine |  |
| https://www.dea.gov/press-releases/2021/10/26/department-justice-announces-resul | US DOJ/DEA | 18545 | germany, australia |  |

### operation-avalanche

**Title**: Operation Avalanche

**Participating (frontmatter, 29)**: armenia, australia, austria, azerbaijan, belgium, belize, bulgaria, canada, colombia, finland, france, germany, hungary, india, italy, lithuania, luxembourg, moldova, montenegro, netherlands, norway, poland, romania, singapore, sweden, taiwan, ukraine, united-kingdom, united-states

**Verified via web (29)**: armenia, australia, austria, azerbaijan, belgium, belize, bulgaria, canada, colombia, finland, france, germany, hungary, india, italy, lithuania, luxembourg, moldova, montenegro, netherlands, norway, poland, romania, singapore, sweden, taiwan, ukraine, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/%E2%80%98avalanche%E2%80 | Europol | 45093 | armenia, australia, austria, azerbaijan, belgium, belize, bulgaria, canada, colombia, finland, france, germany, hungary, |  |
| https://www.justice.gov/usao-wdpa/pr/avalanche-network-dismantled-international- | US DOJ USAO | 0 |  | empty_body |
| https://www.eurojust.europa.eu/publication/operation-avalanche-closer-look | Eurojust | 9752 | austria, belgium, bulgaria, finland, france, germany, hungary, italy, lithuania, luxembourg, netherlands, poland, romani |  |
| https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Cyber-Sicherh | Federal Office for Information Security (BSI) | 5829 | germany |  |
| https://www.bbc.com/news/technology-30849172 | BBC | 5237 | india, united-kingdom, united-states |  |
| https://www.reuters.com/technology/cybersecurity/ghost-cybercrime-platform-disma | Reuters | 0 |  | http_401 |
| https://www.kaspersky.com/about/press-releases/kaspersky-shares-cyberthreat-data | Kaspersky | 13664 | australia, bulgaria, canada, france, india, luxembourg, singapore, taiwan, ukraine, united-kingdom, united-states |  |

### operation-ceres-man-pleads-guilty-cyberstalking-two-victims

**Title**: Kevin James Strutz Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edca/pr/ceres-man-pleads-guilty-cyberstalking-two-v | US DOJ USAO | 0 |  | empty_body |

### operation-chinese-national-sentenced-prison-role-crypto-scam-targeting-americans

**Title**: Jingliang Su Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (1)**: united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/chinese-national-sentenced-prison-role-crypto-sca | US DOJ (Office of Public Affairs) | 9216 | united-states |  |

### operation-contender-2

**Title**: Operation Contender 2.0

**Participating (frontmatter, 4)**: cote-divoire, nigeria, switzerland, finland

**Verified via web (4)**: cote-divoire, finland, nigeria, switzerland

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.interpol.int/en/News-and-Events/News/2024/Arrests-in-international-o | INTERPOL | 5885 | cote-divoire, nigeria, switzerland, finland |  |
| https://www.group-ib.com/th/media-center/press-releases/operation-contender/ | Group-IB | 0 |  | http_403 |

### operation-culpeper-woman-arrested-in-dark-web-murder-for-hire-plot

**Title**: Culpeper Woman Arrested in Dark Web Murder-for-Hire Plot Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdva/pr/culpeper-woman-arrested-dark-web-murder-hir | US DOJ USAO | 0 |  | empty_body |

### operation-darknet-drug-vendor-arrested-for-distributing-illicit-prescription-drugs

**Title**: Darknet Drug Vendor Arrested for Distributing Illicit Prescription Drugs Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edva/pr/darknet-drug-vendor-arrested-distributing-i | US DOJ USAO | 0 |  | empty_body |

### operation-darknet-vendor-arrested-on-distribution-and-money-laundering-charges

**Title**: Darknet Vendor Arrested on Distribution and Money Laundering Charges Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edva/pr/darknet-vendor-arrested-distribution-and-mo | US DOJ USAO | 0 |  | empty_body |

### operation-deepdotweb-administrator-pleads-guilty-money-laundering-conspiracy

**Title**: Tal Prihar and Michael Phan Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdpa/pr/deepdotweb-administrator-pleads-guilty-mone | US DOJ USAO | 0 |  | empty_body |

### operation-estonian-national-extradited-from-estonia-to-face-charges-of-illegal-procurement-of-u-s-electronics

**Title**: Estonian National Extradited From Estonia To Face Charges Of Illegal Procurement Of U.S. Electronics Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndca/pr/estonian-national-extradited-estonia-face-c | US DOJ USAO | 0 |  | empty_body |

### operation-euclid-ohio-man-pleads-guilty-distribution-fentanyl-he-ordered-china-and-sold

**Title**: Antoin Austin Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdpa/pr/euclid-ohio-man-pleads-guilty-distribution- | US DOJ USAO | 0 |  | empty_body |

### operation-fayette-county-man-admits-making-hoax-emergency-phone-calls-to-elicit-an-armed-police-response-practice-is-kno

**Title**: Fayette County Man Admits Making Hoax Emergency Phone Calls to Elicit an Armed Police Response: Practice is Known as “Swatting” Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdpa/pr/fayette-county-man-admits-making-hoax-emerg | US DOJ USAO | 0 |  | empty_body |

### operation-florida-computer-programmer-arrested-for-hacking

**Title**: Florida Computer Programmer Arrested For Hacking Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndca/pr/florida-computer-programmer-arrested-hackin | US DOJ USAO | 0 |  | empty_body |

### operation-florida-man-pleads-guilty-production-images-child-sexual-abuse-and-traveling-sexually

**Title**: Samuel Aaron Leonard Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/florida-man-pleads-guilty-production-images | US DOJ USAO | 0 |  | empty_body |

### operation-foreign-national-indicted-in-wire-fraud-scheme

**Title**: Foreign National Indicted In Wire Fraud Scheme Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/foreign-national-indicted-wire-fraud-scheme | US DOJ USAO | 0 |  | empty_body |

### operation-foreign-national-pleads-guilty-to-role-in-cybercrime-schemes-involving-tens-of-millions-of-dollars-in-losses

**Title**: Foreign National Pleads Guilty to Role in Cybercrime Schemes Involving Tens of Millions of Dollars in Losses Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ne/pr/foreign-national-pleads-guilty-role-cybercrim | US DOJ USAO | 0 |  | empty_body |

### operation-former-childcare-provider-sentenced-to-15-years-in-federal-prison-for-the-production-of-child-sexual-abuse-mat

**Title**: Former Childcare Provider Sentenced to 15 Years in Federal Prison for the Production of Child Sexual Abuse Material Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-nh/pr/former-childcare-provider-sentenced-15-years- | US DOJ USAO | 0 |  | empty_body |

### operation-former-commander-and-adjutant-of-nonprofit-veterans-organization-indicted-for-wire-fraud-and-tax-fraud

**Title**: Former Commander and Adjutant of Nonprofit Veteran’s Organization Indicted for Wire Fraud and Tax Fraud Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-id/pr/former-commander-and-adjutant-nonprofit-veter | US DOJ USAO | 0 |  | empty_body |

### operation-former-company-chief-financial-officer-indicted-for-using-35-million-in-company-cash-to-invest-in-cryptocurren

**Title**: Former company Chief Financial Officer indicted for using $35 million in company cash to invest in cryptocurrency venture Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/former-company-chief-financial-officer-indi | US DOJ USAO | 0 |  | empty_body |

### operation-former-emergency-physician-pleads-guilty-to-possessing-child-pornography

**Title**: Former emergency physician pleads guilty to possessing child pornography Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-sdoh/pr/former-emergency-physician-pleads-guilty-po | US DOJ USAO | 0 |  | empty_body |

### operation-former-employee-of-house-member-sentenced-to-prison-term-on-charges-in-cyberstalking-case

**Title**: Former Employee of House Member Sentenced to Prison Term on Charges in Cyberstalking Case Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-dc/pr/former-employee-house-member-sentenced-prison | US DOJ USAO | 0 |  | empty_body |

### operation-former-employee-of-silicon-valley-company-pleads-guilty-to-damaging-ex-employers-computers

**Title**: Former Employee Of Silicon Valley Company Pleads Guilty To Damaging Ex-Employer’s Computers Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndca/pr/former-employee-silicon-valley-company-plea | US DOJ USAO | 0 |  | empty_body |

### operation-former-owner-of-t-mobile-retail-store-in-eagle-rock-found-guilty-of-committing-25-million-scheme-to-illegally-

**Title**: Former Owner of T-Mobile Retail Store in Eagle Rock Found Guilty of Committing $25 Million Scheme to Illegally Unlock Cellphones Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-cdca/pr/former-owner-t-mobile-retail-store-eagle-ro | US DOJ USAO | 0 |  | empty_body |

### operation-former-teaching-assistant-in-st-louis-admits-blackmailing-student

**Title**: Former Teaching Assistant in St. Louis Admits Blackmailing Student Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edmo/pr/former-teaching-assistant-st-louis-admits-b | US DOJ USAO | 0 |  | empty_body |

### operation-french-coder-who-helped-extort-british-company-arrested-in-thailand

**Title**: French Coder Who Helped Extort British Company Arrested in Thailand Enforcement Action

**Participating (frontmatter, 2)**: thailand, united-kingdom

**Verified via web (2)**: thailand, united-kingdom

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/french-coder-who-helped- | Europol | 33351 | thailand, united-kingdom |  |

### operation-ghost-cybercrime-platform-dismantled-in-global-operation-51-arrested

**Title**: Ghost cybercrime platform dismantled in global operation, 51 arrested Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.reuters.com/technology/cybersecurity/ghost-cybercrime-platform-disma | Reuters | 0 |  | http_401 |

### operation-grand-jury-indicts-knoxville-woman-previously-arrested-in-murder-for-hire-plot

**Title**: Grand Jury Indicts Knoxville Woman Previously Arrested In Murder-For-Hire Plot Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edtn/pr/grand-jury-indicts-knoxville-woman-previous | US DOJ USAO | 0 |  | empty_body |

### operation-greene-county-man-indicted-cyberstalking-and-interstate-threats

**Title**: Kaleb Levicky Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdpa/pr/greene-county-man-indicted-cyberstalking-an | US DOJ USAO | 0 |  | empty_body |

### operation-illinois-man-sentenced-2-years-federal-prison-operating-subscription-based-computer

**Title**: Matthew Gatrel Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-cdca/pr/illinois-man-sentenced-2-years-federal-pris | US DOJ USAO | 0 |  | empty_body |

### operation-in-re-bidencash-marketplace-seizure

**Title**: Seizure of BidenCash Marketplace Domains Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edva/pr/us-government-seizes-approximately-145-crim | US DOJ (Eastern District of Virginia) | 0 |  | empty_body |

### operation-in-re-heartsender-seizure

**Title**: HeartSender / Saim Raza Seizure Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-sdtx/pr/international-operation-takes-down-cybercri | U.S. District Court for the Southern District of Texas | 0 |  | empty_body |

### operation-independence-pair-indicted-for-drug-and-firearms-offenses

**Title**: Independence Pair Indicted for Drug and Firearms Offenses Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdmo/pr/independence-pair-indicted-drug-and-firearm | US DOJ USAO | 0 |  | empty_body |

### operation-individual-arrested-and-charged-with-operating-notorious-darknet-cryptocurrency-mixer

**Title**: Individual Arrested and Charged with Operating Notorious Darknet Cryptocurrency "Mixer" Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-dc/pr/individual-arrested-and-charged-operating-not | US DOJ USAO | 0 |  | empty_body |

### operation-international-crypto-vendor-sentenced-for-money-laundering-conspiracy

**Title**: International Crypto Vendor Sentenced for Money Laundering Conspiracy Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edky/pr/international-crypto-vendor-sentenced-money | US DOJ USAO | 0 |  | empty_body |

### operation-international-hacker-for-hire-who-conspired-with-and-aided-russian-fsb-officers-sentenced-to-five-years-in-pri

**Title**: International Hacker-For-Hire Who Conspired With And Aided Russian FSB Officers Sentenced To Five Years In Prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndca/pr/international-hacker-hire-who-conspired-and | US DOJ USAO | 0 |  | empty_body |

### operation-international-money-launderer-sentenced-to-over-11-years-in-federal-prison-for-laundering-millions-from-cyber-

**Title**: International Money Launderer Sentenced to over 11 Years in Federal Prison for Laundering Millions from Cyber Crime Schemes Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-cdca/pr/international-money-launderer-sentenced-ove | US DOJ USAO | 0 |  | empty_body |

### operation-internet-stalker-sentenced-to-more-than-14-years-in-federal-prison

**Title**: Internet Stalker Sentenced to More than 14 Years in Federal Prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-co/pr/internet-stalker-sentenced-more-14-years-fede | US DOJ USAO | 0 |  | empty_body |

### operation-iranian-man-pleaded-guilty-to-role-in-robbinhood-ransomware

**Title**: Iranian Man Pleaded Guilty to Role in Robbinhood Ransomware Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (1)**: united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/iranian-man-pleaded-guilty-role-robbinhood-ransom | US DOJ (Office of Public Affairs) | 9433 | united-states |  |

### operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-and-money-laundering-services

**Title**: Iranian National Indicted for Operating Online Marketplace Offering Fentanyl and Money Laundering Services Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (1)**: united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/iranian-national-indicted-operating-online-market | US DOJ (Office of Public Affairs) | 9701 | united-states |  |

### operation-iranian-national-indicted-for-operating-online-marketplace-offering-fentanyl-other-drugs-and-money-laundering-

**Title**: Iranian National Indicted for Operating Online Marketplace Offering Fentanyl, Other Drugs, and Money Laundering Services Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndoh/pr/iranian-national-indicted-operating-online- | US DOJ USAO | 0 |  | empty_body |

### operation-irish-man-who-helped-operate-the-silk-road-website-sentenced-in-manhattan-federal-court-to-over-six-years-in-p

**Title**: Irish Man Who Helped Operate The “Silk Road” Website Sentenced In Manhattan Federal Court To Over Six Years In Prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-sdny/pr/irish-man-who-helped-operate-silk-road-webs | US DOJ (Southern District of New York) | 0 |  | empty_body |

### operation-issaquah-washington-man-sentenced-to-7-years-in-prison-for-dealing-fentanyl-and-other-drugs-on-the-darknet

**Title**: Issaquah, Washington man sentenced to 7 years in prison for dealing fentanyl and other drugs on the darknet Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/issaquah-washington-man-sentenced-7-years-p | US DOJ USAO | 0 |  | empty_body |

### operation-jefferson-county-man-sentenced-to-6-12-years-in-prison-for-possession-of-child-pornography

**Title**: Jefferson County Man Sentenced to 6 ½ Years in Prison for Possession of Child Pornography Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndal/pr/jefferson-county-man-sentenced-6-years-pris | US DOJ USAO | 0 |  | empty_body |

### operation-jordanian-man-admits-selling-unauthorized-access-to-computer-networks-of-50-companies

**Title**: Jordanian Man Admits Selling Unauthorized Access to Computer Networks of 50 Companies Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-nj/pr/jordanian-man-admits-selling-unauthorized-acc | US DOJ USAO | 0 |  | empty_body |

### operation-jumbotron-hacker-and-prolific-child-molester-sentenced-to-220-years-in-federal-prison

**Title**: Jumbotron Hacker And Prolific Child Molester Sentenced To 220 Years In Federal Prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/jumbotron-hacker-and-prolific-child-moleste | US DOJ USAO | 0 |  | empty_body |

### operation-justice-department-secures-forfeiture-of-over-5m-of-funds-traceable-to-business-email-compromise-scheme-target

**Title**: Justice Department Secures Forfeiture of Over $5M of Funds Traceable to Business Email Compromise Scheme Targeting Massachusetts Workers Union Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (1)**: united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/justice-department-secures-forfeiture-over-5m-fun | US DOJ (Office of Public Affairs) | 5841 | united-states |  |

### operation-justice-department-seeks-forfeiture-of-848-247-in-cryptocurrency-from-confidence-scams

**Title**: Justice Department Seeks Forfeiture of $848,247 in Cryptocurrency from Confidence Scams Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-dc/pr/justice-department-seeks-forfeiture-848247-cr | US DOJ USAO | 0 |  | empty_body |

### operation-justice-department-seeks-forfeiture-of-over-5-million-in-bitcoin-stolen-in-sim-swapping-scams

**Title**: Justice Department Seeks Forfeiture of Over $5 Million in Bitcoin Stolen in SIM Swapping Scams Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-dc/pr/justice-department-seeks-forfeiture-over-5-mi | US DOJ USAO | 0 |  | empty_body |

### operation-justice-dept-seizes-over-112m-in-funds-linked-to-cryptocurrency-investment-schemes-with-over-half-seized-in-lo

**Title**: Justice Dept. Seizes Over $112M in Funds Linked to Cryptocurrency Investment Schemes, With Over Half Seized in Los Angeles Case Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-cdca/pr/justice-dept-seizes-over-112m-funds-linked- | US DOJ USAO | 0 |  | empty_body |

### operation-kansas-city-woman-indicted-for-fraudulent-tax-returns

**Title**: Kansas City Woman Indicted for Fraudulent Tax Returns Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdmo/pr/kansas-city-woman-indicted-fraudulent-tax-r | US DOJ USAO | 0 |  | empty_body |

### operation-kansas-farmer-indicted-for-insurance-fraud

**Title**: Kansas farmer indicted for insurance fraud Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ks/pr/kansas-farmer-indicted-insurance-fraud | US DOJ USAO | 0 |  | empty_body |

### operation-kansas-man-pleads-guilty-to-child-pornography-possession

**Title**: Kansas man pleads guilty to child pornography possession Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ks/pr/kansas-man-pleads-guilty-child-pornography-po | US DOJ USAO | 0 |  | empty_body |

### operation-kansas-woman-indicted-for-defrauding-elderly-victims

**Title**: Kansas Woman Indicted for Defrauding Elderly Victims Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdmo/pr/kansas-woman-indicted-defrauding-elderly-vi | US DOJ USAO | 0 |  | empty_body |

### operation-kc-man-sentenced-for-selling-meth-heroin-on-the-dark-web

**Title**: KC Man Sentenced for Selling Meth, Heroin on the Dark Web Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdmo/pr/kc-man-sentenced-selling-meth-heroin-dark-w | US DOJ USAO | 0 |  | empty_body |

### operation-kent-washington-resident-indicted-for-dealing-fentanyl-while-illegally-possessing-firearm

**Title**: Kent, Washington, resident indicted for dealing fentanyl while illegally possessing firearm Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/kent-washington-resident-indicted-dealing-f | US DOJ USAO | 0 |  | empty_body |

### operation-kentucky-man-pleads-guilty-advertising-child-pornography

**Title**: Scott Allison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ma/pr/kentucky-man-pleads-guilty-advertising-child- | US DOJ USAO | 0 |  | empty_body |

### operation-kentucky-man-pleads-guilty-to-advertising-child-pornography

**Title**: Kentucky Man Pleads Guilty to Advertising Child Pornography Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ma/pr/kentucky-man-pleads-guilty-advertising-child- | US DOJ USAO | 0 |  | empty_body |

### operation-kentucky-man-sentenced-to-15-years-in-prison-for-advertising-child-pornography

**Title**: Kentucky Man Sentenced to 15 Years in Prison for Advertising Child Pornography Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ma/pr/kentucky-man-sentenced-15-years-prison-advert | US DOJ USAO | 0 |  | empty_body |

### operation-key-member-of-drug-ring-associated-with-aryan-prison-gang-sentenced-to-7-years-in-prison

**Title**: Key member of drug ring associated with Aryan prison gang sentenced to 7+ years in prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/key-member-drug-ring-associated-aryan-priso | US DOJ USAO | 0 |  | empty_body |

### operation-king-county-couple-indicted-for-drug-and-illegal-weapons-possession

**Title**: King County couple indicted for drug and illegal weapons possession Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/king-county-couple-indicted-drug-and-illega | US DOJ USAO | 0 |  | empty_body |

### operation-king-county-man-who-dealt-narcotics-on-the-dark-web-and-kept-a-cache-of-weapons-at-his-rv-sentenced-to-8-years

**Title**: King County man who dealt narcotics on the dark web and kept a cache of weapons at his RV sentenced to 8 years in prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-wdwa/pr/king-county-man-who-dealt-narcotics-dark-we | US DOJ USAO | 0 |  | empty_body |

### operation-kirkwood-resident-pleads-guilty-for-identity-theft

**Title**: Kirkwood resident pleads guilty for identity theft Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edmo/pr/kirkwood-resident-pleads-guilty-identity-th | US DOJ USAO | 0 |  | empty_body |

### operation-knox-county-man-sentenced-to-60-years-imprisonment-for-two-counts-of-production-of-child-pornography

**Title**: Knox County Man Sentenced To 60 Years Imprisonment For Two Counts Of Production Of Child Pornography Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-edtn/pr/knox-county-man-sentenced-60-years-imprison | US DOJ USAO | 0 |  | empty_body |

### operation-kosovo-national-pleads-guilty-to-operating-an-online-criminal-marketplace

**Title**: Kosovo National Pleads Guilty To Operating An Online Criminal Marketplace Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/kosovo-national-pleads-guilty-operating-onl | US DOJ USAO | 0 |  | empty_body |

### operation-lakeland-man-pleads-guilty-to-receiving-child-sex-abuse-videos-from-the-largest-darknet-child-pornography-webs

**Title**: Lakeland Man Pleads Guilty To Receiving Child Sex Abuse Videos From The Largest Darknet Child Pornography Website, Which Was Funded By Bitcoin Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/lakeland-man-pleads-guilty-receiving-child- | US DOJ USAO | 0 |  | empty_body |

### operation-lakeland-man-sentenced-to-more-than-9-years-in-federal-prison-for-downloading-and-possessing-child-sex-abuse-v

**Title**: Lakeland Man Sentenced To More Than 9 Years In Federal Prison For Downloading And Possessing Child Sex Abuse Videos From The Darkweb Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-mdfl/pr/lakeland-man-sentenced-more-9-years-federal | US DOJ USAO | 0 |  | empty_body |

### operation-laredo-professor-charged-with-distribution-and-production-of-child-pornography

**Title**: Laredo professor charged with distribution and production of child pornography Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-sdtx/pr/laredo-professor-charged-distribution-and-p | US DOJ USAO | 0 |  | empty_body |

### operation-latvian-national-charged-for-alleged-role-in-transnational-cybercrime-organization

**Title**: Latvian National Charged for Alleged Role in Transnational Cybercrime Organization Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndoh/pr/latvian-national-charged-alleged-role-trans | US DOJ USAO | 0 |  | empty_body |

### operation-law-enforcement-seize-record-amounts-of-illegal-drugs-firearms-and-drug-trafficking-proceeds-in-international-

**Title**: Law Enforcement Seize Record Amounts of Illegal Drugs, Firearms, and Drug Trafficking Proceeds in International Operation Against Darknet Trafficking of Fentanyl and Opioids; 270 Arrested Across Four Continents Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (1)**: united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/opa/pr/law-enforcement-seize-record-amounts-illegal-drug | US DOJ (Office of Public Affairs) | 23385 | united-states |  |

### operation-leader-of-darknet-drug-distribution-conspiracy-sentenced-to-federal-prison

**Title**: Leader of Darknet Drug Distribution Conspiracy Sentenced to Federal Prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-or/pr/leader-darknet-drug-distribution-conspiracy-s | US DOJ USAO | 0 |  | empty_body |

### operation-leader-of-darknet-italianmafiabrussels-drug-trafficking-organization-sentenced-to-11-years-imprisonment

**Title**: Leader Of Darknet ItalianMafiaBrussels Drug Trafficking Organization Sentenced To 11 Years’ Imprisonment Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-co/pr/leader-darknet-italianmafiabrussels-drug-traf | US DOJ USAO | 0 |  | empty_body |

### operation-leader-of-international-malvertising-and-ransomware-schemes-extradited-from-poland-to-face-cybercrime-charges

**Title**: Leader of International Malvertising and Ransomware Schemes Extradited from Poland to Face Cybercrime Charges Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-nj/pr/leader-international-malvertising-and-ransomw | US DOJ USAO | 0 |  | empty_body |

### operation-leader-of-international-steroids-distribution-scheme-sentenced-to-eight-years-in-prison

**Title**: Leader of International Steroids Distribution Scheme Sentenced to Eight Years in Prison Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-sdca/pr/leader-international-steroids-distribution- | US DOJ USAO | 0 |  | empty_body |

### operation-leader-of-transnational-cybercrime-group-noirs-luxury-refunds-charged-with-conspiracy-to-commit-mail-and-wire-

**Title**: Leader of Transnational Cybercrime Group “Noir’s Luxury Refunds” Charged with Conspiracy to Commit Mail and Wire Fraud Enforcement Action

**Participating (frontmatter, 1)**: united-states

**Verified via web (0)**: —

**Still missing (1)**: united-states

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.justice.gov/usao-ndal/pr/leader-transnational-cybercrime-group-noirs | US DOJ USAO | 0 |  | empty_body |
