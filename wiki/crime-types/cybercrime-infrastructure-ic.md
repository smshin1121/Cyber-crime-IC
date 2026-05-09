---
type: crime-type
title: "Cybercrime Infrastructure Disruption"
aliases:
  - "criminal infrastructure"
  - "cybercrime service infrastructure"
crime_category: cyber-dependent
typical_ic_challenges:
  - "service migration"
  - "domain and server control"
  - "customer attribution"
  - "parallel victim notification"
relevant_legal_frameworks:
  - "[[budapest-convention]]"
typical_mechanisms:
  - "[[domain-seizure]]"
  - "[[search-seizure]]"
  - "[[sinkholing]]"
  - "[[asset-freezing]]"
key_organizations:
  - "[[europol-ec3]]"
  - "[[eurojust]]"
  - "[[fbi]]"
  - "[[usdoj]]"
notable_operations:
  - "[[doublevpn-takedown]]"
  - "[[operation-nova]]"
  - "[[operation-kraken-ghost-platform]]"
  - "[[matrix-encrypted-messaging-takedown-2024]]"
  - "[[operation-alice-csam-fraud-2026]]"
  - "[[w3ll-phishing-kit-takedown-2026]]"
  - "[[treasury-us-au-uk-sanctions-media-land-russian-bulletproof-hosting-2025]]"
  - "[[treasury-us-au-uk-zservers-sanctions-2025]]"
  - "[[treasury-aeza-group-bulletproof-hosting-sanctions-2025]]"
notable_cases:

criminalization_status:
  broadly_criminalized: true
  definition_varies: true
  problem_jurisdictions:

estimated_annual_loss: ""
source_count: 10
sources:
  - "[[2024-05-30_europol-europa-eu_largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem]]"
  - "[[2022-01-18_europol-europa-eu_unhappy-new-year-for-cybercriminals-as-vpnlab-net-goes-offline]]"
  - "[[2021-06-30_eurojust_coordinated-action-cuts-access-vpn-service-used-ransomware-groups]]"
  - "[[2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet]]"
  - "[[2024-12-03_europol_matrix-encrypted-messaging-service-takedown]]"
  - "[[2026-03-21_europol_global-cybercrime-crackdown-373000-dark-web-sites-operation-alice]]"
  - "[[2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll]]"
  - "[[2025-11-19_treasury_us-au-uk-sanctions-russian-cybercrime-infrastructure-media-land]]"
  - "[[2025-02-11_treasury_us-au-uk-zservers-sanctions-lockbit-ransomware]]"
  - "[[2025-07-01_treasury_aeza-group-bulletproof-hosting-cybercriminal-technology-theft-sanctions]]"
created: 2026-04-17
updated: 2026-05-09
status: active
---
## Summary

Cybercrime infrastructure disruption covers actions against the services that make other crimes scalable: botnet loaders, proxy networks, bulletproof VPNs, credential shops, hosting clusters, malware-delivery domains, and command-and-control systems. The target is often not a single criminal group. It is an enabling service used by many customers, affiliates, or downstream actors.

## Cooperation Pattern

Operation Endgame, VPNLab, DoubleVPN, and the 911 S5 botnet action show the common sequence. Investigators map the infrastructure, identify legal control points, prepare seizure or disruption orders in several jurisdictions, and coordinate an action day that prevents administrators from moving domains, servers, or customer data. Evidence value is high because seized customer records can generate follow-on cases against ransomware groups, fraud actors, malware operators, or access brokers.

## Menu Use

Use this page when the source is mainly about infrastructure-as-a-service for cybercrime. If the source is about a specific malware family, use [[malware-ic]]. If it is about DDoS-for-hire, use [[ddos-ic]]. If it is about a forum where criminals trade services, use [[cybercrime-forum-ic]]. The infrastructure page should remain the cross-cutting menu node for services that support multiple criminal markets.

## Analytical Use

Within this wiki, **Cybercrime Infrastructure Disruption** is a control node for comparing records that describe the offense pattern, evidence sources, and cross-border investigative pressure points. Use the page to separate three questions that often become mixed in operation narratives: what conduct or authority is being discussed, which agency or state actor exercised it, and where the cross-border dependency appears in the evidence chain. That separation makes the menu more useful for comparing takedowns, prosecutions, extradition matters, and assistance requests without treating every related record as the same kind of cooperation event.

## Integrity Notes

The page groups terminology; it is not independent proof that the concept, crime type, mechanism, or framework applied in every linked matter. Operation and case pages remain the controlling records for arrests, seizures, requests, treaty use, and participating agencies. When adding future links, keep the distinction between direct source evidence, inferred analytical classification, and catalog navigation visible in the target page.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | [[2024-05-30_europol-europa-eu_largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem|Largest ever operation against botnets hits dropper malware ecosystem]] | Europol | 2024-05-30 | https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem |
| [2] | [[2022-01-18_europol-europa-eu_unhappy-new-year-for-cybercriminals-as-vpnlab-net-goes-offline|Unhappy New Year for cybercriminals as VPNLab.net goes offline]] | Europol | 2022-01-18 | https://www.europol.europa.eu/media-press/newsroom/news/unhappy-new-year-for-cybercriminals-vpnlabnet-goes-offline |
| [3] | [[2021-06-30_eurojust_coordinated-action-cuts-access-vpn-service-used-ransomware-groups|Coordinated action cuts off access to VPN service used by ransomware groups]] | Eurojust | 2021-06-30 | https://www.eurojust.europa.eu/news/coordinated-action-cuts-access-vpn-service-used-ransomware-groups |
| [4] | [[2024-05-29_justice-gov_justice-department-leads-effort-to-dismantle-911-s5-botnet|911 S5 Botnet Dismantled and Its Administrator Arrested in Coordinated International Operation]] | U.S. Department of Justice | 2024-05-29 | https://www.justice.gov/archives/opa/pr/911-s5-botnet-dismantled-and-its-administrator-arrested-coordinated-international-operation |
| [5] | [[2024-12-03_europol_matrix-encrypted-messaging-service-takedown\|International operation takes down another encrypted messaging service used by criminals (MATRIX)]] | Europol | 2024-12-03 | https://www.europol.europa.eu/media-press/newsroom/news/international-operation-takes-down-another-encrypted-messaging-service-used-criminals |
| [6] | [[2026-03-21_europol_global-cybercrime-crackdown-373000-dark-web-sites-operation-alice\|Global cybercrime crackdown: over 373 000 dark web sites shut down (Operation Alice)]] | Europol | 2026-03-21 | https://www.europol.europa.eu/media-press/newsroom/news/global-cybercrime-crackdown-over-373-000-dark-web-sites-shut-down |
| [7] | [[2026-04-10_fbi-atlanta_global-phishing-network-takedown-w3ll\|FBI Atlanta, Indonesian Authorities Take Down Global Phishing Network Behind Millions in Fraud Attempts (W3LL phishing kit)]] | FBI Atlanta Field Office | 2026-04-10 | https://www.fbi.gov/contact-us/field-offices/atlanta/news/fbi-atlanta-indonesian-authorities-take-down-global-phishing-network-behind-millions-in-fraud-attempts |
| [8] | [[2025-11-19_treasury_us-au-uk-sanctions-russian-cybercrime-infrastructure-media-land\|United States, Australia, and United Kingdom Sanction Russian Cybercrime Infrastructure Supporting Ransomware]] | US Department of the Treasury (OFAC), Press Release SB-0319 | 2025-11-19 | https://home.treasury.gov/news/press-releases/sb0319 |
| [9] | [[2025-02-11_treasury_us-au-uk-zservers-sanctions-lockbit-ransomware\|US/AU/UK Jointly Sanction Key Infrastructure that Enables Ransomware Attacks (Zservers)]] | US Department of the Treasury (OFAC), Press Release SB-0018 | 2025-02-11 | https://home.treasury.gov/news/press-releases/sb0018 |
| [10] | [[2025-07-01_treasury_aeza-group-bulletproof-hosting-cybercriminal-technology-theft-sanctions\|Treasury Sanctions Global Bulletproof Hosting Service Enabling Cybercriminals and Technology Theft (Aeza Group)]] | US Department of the Treasury (OFAC), Press Release SB-0185 | 2025-07-01 | https://home.treasury.gov/news/press-releases/sb0185 |
