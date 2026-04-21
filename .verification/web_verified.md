# participating_countries — web primary-source verification (curl_cffi)

_Run: 2026-04-21 09:07_

Fetched via curl_cffi with Chrome TLS fingerprint impersonation (bypasses Cloudflare on most static press releases). For each op in the verification queue, every country in its `participating_countries` is checked against the rendered text of all cited source URLs.

- **verified_union** — country explicitly named in ≥1 source page
- **still_missing** — country NOT found in any reachable source
- Fetch errors (Cloudflare challenge still unsolved, 403, 404 etc.) are recorded per URL

## Summary

- Operations processed: 30
- Fully verified (every frontmatter country named in a source): 15
- Partially verified: 3
- Nothing verified (all sources failed): 12

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
| https://home.treasury.gov/news/press-releases/sb0040 | U.S. Department of the Treasury | 17311 | united-states, germany |  |
| https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2024/Presse2024/2403 | Bundeskriminalamt / ZIT Frankfurt | 5215 |  |  |
| https://www.justice.gov/opa/pr/iranian-national-indicted-operating-online-market | US DOJ (Office of Public Affairs) | 9701 | united-states, germany, lithuania |  |

### doublevpn-takedown

**Title**: DoubleVPN Takedown

**Participating (frontmatter, 9)**: netherlands, united-states, canada, germany, united-kingdom, sweden, italy, bulgaria, switzerland

**Verified via web (9)**: bulgaria, canada, germany, italy, netherlands, sweden, switzerland, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.eurojust.europa.eu/news/coordinated-action-cuts-access-vpn-service-u | Eurojust | 13554 | netherlands, united-states, canada, germany, united-kingdom, sweden, italy, bulgaria, switzerland |  |
| https://www.eurojust.europa.eu/annual-report-2021/cybercrime/case-examples | Eurojust | 17004 | netherlands, united-states, canada, germany, sweden, italy, bulgaria |  |
| https://www.nationalcrimeagency.gov.uk/news/doublevpn-takedown-nca-takes-uk-serv | UK NCA | 4855 | netherlands, canada |  |
| https://therecord.media/dutch-police-takes-down-doublevpn-a-service-used-by-cybe | The Record | 3454 | netherlands, united-states, canada, germany, sweden, italy, bulgaria, switzerland |  |

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
| https://www.nationalcrimeagency.gov.uk/news/international-operation-targets-dark | UK NCA | 5285 | australia, bulgaria, france, germany, italy, netherlands, switzerland, united-states |  |
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

**Verified via web (5)**: austria, denmark, greece, spain, united-states

**Still missing (1)**: united-kingdom

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/105-arrested-for-stealin | Europol | 41047 | austria, denmark, greece, spain, united-states |  |

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
| https://www.europol.europa.eu/media-press/newsroom/news/mastermind-behind-eur-1- | Europol | 35870 | spain, romania |  |
| https://securelist.com/the-great-bank-robbery-the-carbanak-apt/68732/ | Kaspersky Securelist | 23200 | spain, united-states |  |
| https://www.europol.europa.eu/cms/sites/default/files/documents/carbanakcobalt.p | Europol | 1137912 |  |  |
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
| https://www.chainalysis.com/blog/ofac-sanctions-russian-exchange-cryptex-uaps-fr | Chainalysis | 12397 | netherlands |  |

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

**Verified via web (2)**: germany, united-states

**Still missing (1)**: lithuania

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.bka.de/DE/Presse/Listenseite_Pressemitteilungen/2024/Presse2024/2403 | Bundeskriminalamt / ZIT Frankfurt | 5215 |  |  |
| https://www.justice.gov/opa/pr/administrator-nemesis-market-charged-role-operati | U.S. Department of Justice | 0 |  | http_404 |
| https://www.justice.gov/usao-ndoh/pr/iranian-national-indicted-operating-online- | US DOJ USAO | 0 |  | empty_body |
| https://home.treasury.gov/news/press-releases/sb0040 | U.S. Department of the Treasury | 17311 | germany, united-states |  |

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

**Participating (frontmatter, 28)**: armenia, australia, austria, azerbaijan, belgium, belize, bulgaria, canada, finland, france, germany, hungary, india, italy, lithuania, luxembourg, moldova, montenegro, netherlands, norway, poland, romania, singapore, sweden, taiwan, ukraine, united-kingdom, united-states

**Verified via web (28)**: armenia, australia, austria, azerbaijan, belgium, belize, bulgaria, canada, finland, france, germany, hungary, india, italy, lithuania, luxembourg, moldova, montenegro, netherlands, norway, poland, romania, singapore, sweden, taiwan, ukraine, united-kingdom, united-states

**Still missing (0)**: —

| URL | Publisher | Chars | Found | Error |
|---|---|---:|---|---|
| https://www.europol.europa.eu/media-press/newsroom/news/%E2%80%98avalanche%E2%80 | Europol | 45093 | armenia, australia, austria, azerbaijan, belgium, belize, bulgaria, canada, finland, france, germany, hungary, india, it |  |
| https://www.justice.gov/usao-wdpa/pr/avalanche-network-dismantled-international- | US DOJ USAO | 0 |  | empty_body |
| https://www.eurojust.europa.eu/publication/operation-avalanche-closer-look | Eurojust | 9752 | austria, belgium, bulgaria, finland, france, germany, hungary, italy, lithuania, luxembourg, netherlands, poland, romani |  |
| https://www.bsi.bund.de/EN/Themen/Verbraucherinnen-und-Verbraucher/Cyber-Sicherh | Federal Office for Information Security (BSI) | 5829 | germany |  |
| https://www.bbc.com/news/technology-30849172 | BBC | 5237 | india, united-states |  |
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
