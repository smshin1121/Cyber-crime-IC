"""
Generate minimal stub pages for orphan wikilinks.
Each stub has verified basic facts and source URLs; marks unknown fields clearly.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"

ORG_STUBS = {
    # slug: (title, official_name, country_slug, org_type, mandate, url)
    "cert-lv": (
        "CERT.LV",
        "Information Technology Security Incident Response Institution of the Republic of Latvia",
        "latvia",
        "national-agency",
        "Latvia's national Computer Emergency Response Team; hosted by the University of Latvia under MoD mandate.",
        "https://cert.lv/en",
    ),
    "cert-mu": (
        "CERT-MU",
        "Computer Emergency Response Team of Mauritius",
        "mauritius",
        "national-agency",
        "National cybersecurity incident response body operated by the National Computer Board of Mauritius.",
        "https://www.cert-mu.govmu.org/",
    ),
    "maroc-cert": (
        "maCERT",
        "Centre Marocain d'Alerte et de Gestion des Incidents Informatiques (maCERT)",
        "morocco",
        "national-agency",
        "Morocco's national CERT, operated by the Direction Générale de la Sécurité des Systèmes d'Information (DGSSI).",
        "https://www.dgssi.gov.ma/fr/macert",
    ),
    "norway-kripos": (
        "Kripos",
        "Nasjonal enhet for bekjempelse av organisert og annen alvorlig kriminalitet (Kripos)",
        "norway",
        "national-unit",
        "Norway's National Criminal Investigation Service — hosts the NC3 cybercrime center and Norway's Budapest Convention 24/7 Network contact point.",
        "https://www.politiet.no/en/about-the-police-service/organisation/specialist-agencies/kripos/",
    ),
    "norway-nc3": (
        "Norway NC3",
        "Nasjonalt cyberkrimsenter (NC3)",
        "norway",
        "national-unit",
        "Norway's National Cybercrime Centre, established within Kripos; investigates serious cybercrime and hosts 24/7 PoC.",
        "https://www.politiet.no/en/about-the-police-service/organisation/specialist-agencies/kripos/nasjonalt-cyberkrimsenter-nc3/",
    ),
    "norway-nsm": (
        "Nasjonal sikkerhetsmyndighet (NSM)",
        "Nasjonal sikkerhetsmyndighet — Norwegian National Security Authority",
        "norway",
        "national-agency",
        "Norway's national security authority for preventive security and cybersecurity; operates NorCERT.",
        "https://nsm.no/",
    ),
    "morocco-dgsn": (
        "DGSN",
        "Direction Générale de la Sûreté Nationale",
        "morocco",
        "national-agency",
        "Morocco's National Security Directorate; parent of the Judicial Police and cybercrime investigation units.",
        "https://www.dgsn.gov.ma/",
    ),
    "morocco-dgst": (
        "DGST",
        "Direction Générale de la Surveillance du Territoire",
        "morocco",
        "national-agency",
        "Morocco's General Directorate for Territorial Surveillance; domestic intelligence and counter-terrorism with cybersecurity role.",
        "https://en.wikipedia.org/wiki/Directorate-General_for_Territorial_Surveillance_(Morocco)",
    ),
    "south-africa-hawks": (
        "The Hawks",
        "Directorate for Priority Crime Investigation (DPCI)",
        "south-africa",
        "national-unit",
        "South African Police Service specialized unit investigating organized crime, economic crime, and serious cybercrime.",
        "https://www.saps.gov.za/dpci/",
    ),
    "south-africa-saps": (
        "South African Police Service",
        "South African Police Service (SAPS)",
        "south-africa",
        "national-agency",
        "South Africa's national police service; hosts DPCI (Hawks) for serious cybercrime investigations.",
        "https://www.saps.gov.za/",
    ),
    "nacsa-malaysia": (
        "NACSA",
        "National Cyber Security Agency of Malaysia",
        "malaysia",
        "national-agency",
        "Malaysia's national cybersecurity coordinator, established under the National Security Council; policy and CNI protection.",
        "https://www.nacsa.gov.my/",
    ),
    "latvia-state-police": (
        "Latvia State Police",
        "Valsts policija — Economic Crimes Enforcement Department Cybercrime Division",
        "latvia",
        "national-unit",
        "Latvian state police cybercrime investigation division within the Economic Crimes Enforcement Department.",
        "https://www.vp.gov.lv/en",
    ),
    "mauritius-police-cybercrime": (
        "Mauritius Police Cybercrime Unit",
        "Mauritius Police Force — Cyber Crime Unit",
        "mauritius",
        "national-unit",
        "Cybercrime investigation unit of the Mauritius Police Force.",
        "https://police.govmu.org/",
    ),
    "spain-national-police": (
        "Spanish National Police",
        "Cuerpo Nacional de Policía — Unidad Central de Ciberdelincuencia (UCC)",
        "spain",
        "national-unit",
        "Central Cybercrime Unit of the Spanish National Police; complementary to Guardia Civil's GDT.",
        "https://www.policia.es/_es/colabora_ciberseguridad.php",
    ),
    "switzerland-ncsc": (
        "Swiss NCSC",
        "Bundesamt für Cybersicherheit / Office fédéral de la cybersécurité (Swiss Federal Office for Cybersecurity, formerly NCSC)",
        "switzerland",
        "national-agency",
        "Switzerland's national cybersecurity office, since 2024 a federal office (BACS/OFCS); national CERT (GovCERT) and NCSC functions.",
        "https://www.ncsc.admin.ch/ncsc/en/home.html",
    ),
    "singapore-csa": (
        "Cyber Security Agency of Singapore",
        "Cyber Security Agency of Singapore (CSA)",
        "singapore",
        "national-agency",
        "Singapore's lead national cybersecurity agency, under the Prime Minister's Office; operates SingCERT and critical infrastructure programme.",
        "https://www.csa.gov.sg/",
    ),
    "australian-criminal-intelligence-commission": (
        "Australian Criminal Intelligence Commission",
        "Australian Criminal Intelligence Commission (ACIC)",
        "australia",
        "national-agency",
        "Australia's national criminal intelligence agency; supports cybercrime investigations through intelligence sharing with AFP and state police.",
        "https://www.acic.gov.au/",
    ),
    "dod-inspector-general": (
        "DoD Office of Inspector General",
        "United States Department of Defense Office of Inspector General",
        "united-states",
        "national-agency",
        "Independent oversight of Department of Defense; parent of Defense Criminal Investigative Service ([[us-dcis]]).",
        "https://www.dodig.mil/",
    ),
    "us-ncis": (
        "NCIS",
        "Naval Criminal Investigative Service",
        "united-states",
        "national-unit",
        "Primary law enforcement and counterintelligence agency of the US Department of the Navy; cybercrime enforcement for Navy and Marine Corps networks.",
        "https://www.ncis.navy.mil/",
    ),
    "ministry-of-science-and-ict-korea": (
        "Ministry of Science and ICT (Korea)",
        "과학기술정보통신부 (Ministry of Science and ICT)",
        "south-korea",
        "national-agency",
        "South Korean government ministry responsible for ICT, science policy, and information security; parent of [[kisa]] (Korea Internet & Security Agency).",
        "https://www.msit.go.kr/eng/",
    ),
    "supreme-prosecutors-office-korea": (
        "Supreme Prosecutors' Office (Korea)",
        "대검찰청 (Supreme Prosecutors' Office of the Republic of Korea)",
        "south-korea",
        "prosecution-office",
        "South Korea's highest prosecution body; oversees cybercrime prosecution and international cooperation via [[spo-international-cooperation]].",
        "https://www.spo.go.kr/eng/",
    ),
}

LEGAL_FRAMEWORK_STUBS = {
    "malabo-convention": {
        "title": "African Union Convention on Cyber Security and Personal Data Protection",
        "official_name": "African Union Convention on Cyber Security and Personal Data Protection",
        "aliases": ["Malabo Convention"],
        "framework_type": "regional-agreement",
        "adopted_date": "2014-06-27",
        "entry_into_force": "2023-06-08",
        "depositary": "African Union Commission",
        "sponsoring_body": "[[african-union]]",
        "status": "in-force",
        "scope": {
            "substantive_law": True,
            "procedural_law": True,
            "international_cooperation": True,
            "data_protection": True,
        },
        "summary": "The Malabo Convention was adopted by the African Union in June 2014 and entered into force on 8 June 2023 after obtaining the required 15 ratifications. It addresses cybersecurity, cybercrime, and personal data protection across African Union member states. It is considered a regional alternative and complement to the Budapest Convention.",
        "url": "https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection",
    },
    "first-additional-protocol-xenophobia": {
        "title": "First Additional Protocol to the Budapest Convention (CETS 189)",
        "official_name": "Additional Protocol to the Convention on Cybercrime, concerning the criminalisation of acts of a racist and xenophobic nature committed through computer systems",
        "aliases": ["CETS 189", "First Additional Protocol", "Xenophobia Protocol"],
        "framework_type": "protocol",
        "adopted_date": "2003-01-28",
        "entry_into_force": "2006-03-01",
        "depositary": "Council of Europe",
        "sponsoring_body": "[[council-of-europe]]",
        "status": "in-force",
        "scope": {
            "substantive_law": True,
            "international_cooperation": True,
        },
        "summary": "CETS 189 is the First Additional Protocol to the Budapest Convention, criminalising acts of a racist and xenophobic nature committed through computer systems. Opened for signature on 28 January 2003 and entered into force on 1 March 2006. Not all Budapest Convention parties have ratified this protocol due to First Amendment concerns (notably the United States).",
        "url": "https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=189",
    },
}


def create_org_stub(slug: str, title: str, official: str, country: str, org_type: str, mandate: str, url: str) -> str:
    return f"""---
type: organization
title: "{title}"
official_name: "{official}"
aliases: []
org_type: "{org_type}"
parent_org: ""
country: "[[{country}]]"
headquarters: ""
established: ""
mandate: "{mandate}"
key_roles: []
cooperation_partners: []
frameworks_administered: []
mechanisms_operated: []
operations_participated: []
notable_cases: []
contact_point_for: []
source_count: 1
sources: []
created: 2026-04-10
updated: 2026-04-10
---

> [!info] Stub
> This page was auto-created to resolve a wikilink. It will be expanded when more sources are ingested.

## Summary

{mandate} For detailed facts, see the official source [1].

## Mandate and Authority

{mandate}

## Contradictions & Open Questions

- Specific cybercrime caseload and operational data not yet recorded.
- Year established, headquarters, and structural details require further research.

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Official website | {title} | — | {url} |
"""


def create_framework_stub(slug: str, data: dict) -> str:
    scope_lines = "\n".join(f"  {k}: {str(v).lower()}" for k, v in data["scope"].items())
    fm = f"""---
type: legal-framework
title: "{data['title']}"
official_name: "{data['official_name']}"
aliases: {data['aliases']}
framework_type: "{data['framework_type']}"
adopted_date: "{data['adopted_date']}"
entry_into_force: "{data['entry_into_force']}"
depositary: "{data['depositary']}"
sponsoring_body: "{data['sponsoring_body']}"
status: "{data['status']}"
parties:
  states_parties: 0
  signatories: 0
key_provisions: []
scope:
{scope_lines}
related_frameworks: []
implementing_mechanisms: []
operations_enabled: []
source_count: 1
sources: []
created: 2026-04-10
updated: 2026-04-10
---

> [!info] Stub
> This page was auto-created to resolve a wikilink. It will be expanded when more sources are ingested.

## Summary

{data['summary']} See [1] for the authoritative treaty text and ratification chart.

## Historical Context

(To be expanded)

## Key Provisions for IC

(To be expanded)

## Parties and Participation

(To be expanded)

## Implementation in Practice

(To be expanded)

## Contradictions & Open Questions

- Exact current number of states parties not yet recorded
- Ratification chart should be verified against depositary source

## References

| # | Source | Publisher | Date | URL |
|---|---|---|---|---|
| [1] | Treaty text and status chart | {data['depositary']} | {data['adopted_date']} | {data['url']} |
"""
    return fm


def main() -> None:
    created = []
    for slug, tup in ORG_STUBS.items():
        path = WIKI / "organizations" / f"{slug}.md"
        if path.exists():
            continue
        content = create_org_stub(slug, *tup)
        path.write_text(content, encoding="utf-8")
        created.append(str(path.relative_to(WIKI)))

    for slug, data in LEGAL_FRAMEWORK_STUBS.items():
        path = WIKI / "legal-frameworks" / f"{slug}.md"
        if path.exists():
            continue
        content = create_framework_stub(slug, data)
        path.write_text(content, encoding="utf-8")
        created.append(str(path.relative_to(WIKI)))

    print(f"Created {len(created)} stub files:")
    for f in created:
        print(f"  {f}")


if __name__ == "__main__":
    main()
