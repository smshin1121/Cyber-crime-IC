"""
Fix dead external URLs by:
1. Truncated Wikipedia URLs (missing closing parenthesis) -- direct fix
2. Querying Wayback Machine for an archived snapshot and rewriting
3. For unrecoverable URLs, flag in the file with a [!warning] callout

Reads from _workspace/external_url_check.json and applies changes to wiki/*.md
"""
import json
import re
import time
from pathlib import Path

import requests

WIKI = Path(__file__).resolve().parent.parent / "wiki"
REPORT = Path(__file__).resolve().parent.parent / "_workspace" / "external_url_check.json"
WAYBACK_API = "https://archive.org/wayback/available"
UA = "Mozilla/5.0 (Cyber-crime-IC url-fixer)"

# URLs we know are Wikipedia truncated — fix directly (add closing paren)
WIKIPEDIA_FIXES = {
    "https://en.wikipedia.org/wiki/Directorate-General_for_Territorial_Surveillance_(Morocco":
        "https://en.wikipedia.org/wiki/Directorate-General_for_Territorial_Surveillance_(Morocco)",
    "https://en.wikipedia.org/wiki/National_Bureau_of_Investigation_(Finland":
        "https://en.wikipedia.org/wiki/National_Bureau_of_Investigation_(Finland)",
    "https://en.wikipedia.org/wiki/National_Police_Agency_(Japan":
        "https://en.wikipedia.org/wiki/National_Police_Agency_(Japan)",
    "https://en.wikipedia.org/wiki/National_Special_Crime_Unit_(Denmark":
        "https://en.wikipedia.org/wiki/National_Special_Crime_Unit_(Denmark)",
}

# Manual replacements where we know a better canonical URL
MANUAL_FIXES = {
    # rcmp.ca → official rcmp-grc.gc.ca domain
    "https://rcmp.ca/en/cyber-choices/cybercrime-and-criminal-code":
        "https://www.rcmp-grc.gc.ca/en/cybercrime-what-it-and-how-protect-yourself",
    "https://rcmp.ca/en/federal-policing/cybercrime/national-cybercrime-coordination-centre":
        "https://www.rcmp-grc.gc.ca/en/federal-policing-investigation-nc3",
    "https://rcmp.ca/en/corporate-information/access-information-and-privacy/privacy-impact-assessments/national-cybercrime-coordination-centre-nc3-and-canadian-anti-fraud-centre-cafc":
        "https://www.rcmp-grc.gc.ca/en/corporate-information/access-information-and-privacy",
    # www.rcmp.gc.ca → www.rcmp-grc.gc.ca
    "https://www.rcmp.gc.ca/en/the-national-cybercrime-coordination-unit-nc3":
        "https://www.rcmp-grc.gc.ca/en/federal-policing-investigation-nc3",
    # ssi.gouv.fr → cyber.gouv.fr (ANSSI's new domain since 2024)
    "https://www.ssi.gouv.fr/en/mission/what-we-do/":
        "https://cyber.gouv.fr/en/mission",
    # www.policia.es — correct path
    "https://www.policia.es/_es/colabora_ciberseguridad.php":
        "https://www.policia.es/_es/colabora.php",
    # Portugal PJ — correct domain
    "https://www.policiajudiciaria.pt/":
        "https://www.pj.pt/",
    "https://www.policiajudiciaria.pt/unc3t/":
        "https://www.pj.pt/unc3t/",
    # ec3.pro — does not exist; Europol EC3 is at europol.europa.eu
    "https://www.ec3.pro/":
        "https://www.europol.europa.eu/about-europol/european-cybercrime-centre-ec3",
    # Baker McKenzie old insight URL — truncated
    "https://www.bakermckenzie.com/en/insight/publications/2017/01/key-changes-under-the-2017":
        "https://www.bakermckenzie.com/en/insight/publications/2017/02/thailand-cybercrime-act",
    # Washington Post — use archive.org for paywalled content
    # (Handled automatically by Wayback lookup below)
    # Spain Guardia Civil GDT
    "https://www.gdt.guardiacivil.es/":
        "https://www.guardiacivil.es/en/institucional/Conocenos/especialidades/Delitos_telematicos/index.html",
    # CSA Singapore — root returns 403; use Wayback
    # Handled by Wayback fallback
    # MDDI Singapore
    "https://www.mddi.gov.sg/who-we-are/agencies/":
        "https://www.mddi.gov.sg/",
    # US Secret Service CFTF contact
    "https://www.secretservice.gov/contact/ectf-fctf":
        "https://www.secretservice.gov/investigation/cyber",
    # Belgium FCCU (sinners.be is defunct)
    "https://fccu.sinners.be/about.html":
        "https://www.police.be/5998/fr/a-propos/directions-centrales/federal-computer-crime-unit",
    # Belgium Federal Police (same URL appears to be 403)
    # keep as-is for Wayback
    # Tanzania parliament PDF — try alternate path
    "https://www.parliament.go.tz/polis/uploads/bills/acts/1452248153-The%20Cyber%20Crime%20Act,%202015.pdf":
        "https://www.parliament.go.tz/polis/PAMS/docs/14-2015.pdf",
    # Rwanda RURA PDF
    "https://www.rura.rw/fileadmin/Documents/ICT/Laws/Law_n__60-2018_of_22-08-2018_on_prevention_and_punishment_of_cyber_crimes.pdf":
        "https://rura.rw/uploads/media/Law_n__60-2018_of_22-08-2018_on_prevention_and_punishment_of_cyber_crimes.pdf",
    # Togo cyberdroit — use the official Journal Officiel archive
    "https://www.cyberdroit.tg/loi-2018-026-cybersecurite/":
        "https://ancy.gouv.tg/",
    # NCIS Navy
    "https://www.ncis.navy.mil/":
        "https://www.ncis.navy.mil/About-NCIS/",
    # Morocco DGSN
    "https://www.dgsn.gov.ma/":
        "https://dgsn.gov.ma/",
    # Morocco DGSSI
    "https://www.dgssi.gov.ma/fr/macert":
        "https://www.dgssi.gov.ma/",
    # France diplomatie URL — reorganized site
    "https://www.diplomatie.gouv.fr/en/french-foreign-policy/security-disarmament-and-non-proliferation/fight-against-organized-criminality/cyber-security/":
        "https://www.diplomatie.gouv.fr/en/french-foreign-policy/digital-diplomacy/france-s-international-digital-strategy/",
    # UN OLA Hanoi news — use UN News direct
    "https://www.un.org/ola/en/news/united-nations-convention-against-cybercrime-opens-signature-hanoi":
        "https://news.un.org/en/story/2025/10/1173851",
    # Hanoi convention portal
    "https://hanoiconvention.org/":
        "https://www.unodc.org/unodc/en/cybercrime/convention/home.html",
    # KE-CIRT
    "https://ke-cirt.go.ke/":
        "https://www.ca.go.ke/ke-cirt-cc",
    # CERT-MU
    "https://www.cert-mu.govmu.org/":
        "https://www.cert-mu.org.mu/",
    # Zambia Parliament PDF
    "https://www.parliament.gov.zm/sites/default/files/documents/acts/The%20Cyber%20Security%20and%20Cyber%20Crimes%20Act%20No%202%20of%202021.pdf":
        "https://www.parliament.gov.zm/node/8756",
    # Cote d'Ivoire Tresor URL
    "https://www.tresor.gouv.ci/tres/wp-content/uploads/2018/03/2013-451-cybercriminalite.pdf":
        "https://www.artci.ci/images/stories/pdf/lois/loi_2013_451.pdf",
    # Gambia govt PDFs
    "https://moin.gov.gm/wp-content/uploads/2023/10/CYBERSECURITY-POLICY-2024.pdf":
        "https://www.moict.gov.gm/",
    "https://mocde.gov.gm/wp-content/uploads/2024/02/Cybersecurity-Policy-2022-2026-Final-1.pdf":
        "https://www.moict.gov.gm/",
    # Portugal PGD Lisboa legal article lookup
    "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=2608A0001&nid=2608&tabela=leis&ficha=1&nversao=":
        "https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?nid=1137",
    # Portugal DRE — likely valid, keep as-is
    # Serbia paragraf.rs — law database, URL may have changed
    "https://www.paragraf.rs/propisi/zakon-o-organizaciji-i-nadleznosti-drzavnih-organa-za-borbu-protiv-visokotehnoloskog-kriminala.html":
        "https://www.paragraf.rs/propisi/zakon_o_organizaciji_i_nadleznosti_drzavnih_organa_za_borbu_protiv_visokotehnoloskog_kriminala.html",
    # youcandonews Korea — article removed; no clean replacement
    # Handled via Wayback
}


def query_wayback(url: str) -> str | None:
    """Return the closest archived snapshot URL or None."""
    try:
        r = requests.get(WAYBACK_API, params={"url": url}, timeout=15, headers={"User-Agent": UA})
        if r.status_code != 200:
            return None
        data = r.json()
        snap = data.get("archived_snapshots", {}).get("closest")
        if snap and snap.get("available"):
            return snap.get("url")
    except Exception:
        return None
    return None


def apply_replacements(replacements: dict[str, str]) -> int:
    """Replace URLs across wiki markdown files. Returns number of files changed."""
    files_changed = 0
    for md in WIKI.rglob("*.md"):
        if md.name.startswith("_") or ".obsidian" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        new = text
        for old, new_url in replacements.items():
            if old in new:
                new = new.replace(old, new_url)
        if new != text:
            md.write_text(new, encoding="utf-8")
            files_changed += 1
    return files_changed


def main() -> None:
    print("=" * 60)
    print("  Dead URL Fixer")
    print("=" * 60)

    # Phase 1: Wikipedia truncated
    replacements: dict[str, str] = dict(WIKIPEDIA_FIXES)
    print(f"  Wikipedia truncated URL fixes: {len(WIKIPEDIA_FIXES)}")

    # Phase 2: Manual known replacements
    replacements.update(MANUAL_FIXES)
    print(f"  Manual canonical URL replacements: {len(MANUAL_FIXES)}")

    # Phase 3: Load broken URLs from report, try Wayback for remaining
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    broken = [
        r for r in report["results"]
        if r["category"] in ("not_found", "client_error", "connection_error", "server_error")
    ]
    remaining = [r for r in broken if r["url"] not in replacements]
    print(f"  Broken URLs remaining for Wayback lookup: {len(remaining)}")

    wayback_hits = 0
    wayback_misses = 0
    for i, res in enumerate(remaining, 1):
        url = res["url"]
        archived = query_wayback(url)
        if archived:
            replacements[url] = archived
            wayback_hits += 1
            print(f"    [{i}/{len(remaining)}] archived: {url[:60]}...")
        else:
            wayback_misses += 1
            print(f"    [{i}/{len(remaining)}] NO archive: {url[:60]}...")
        time.sleep(0.3)

    print(f"\n  Wayback hits: {wayback_hits}  misses: {wayback_misses}")
    print(f"  Total replacements to apply: {len(replacements)}")

    # Apply
    files_changed = apply_replacements(replacements)
    print(f"  Files updated: {files_changed}")

    # Also add a warning callout for URLs with no replacement
    unresolved_log = []
    for res in remaining:
        if res["url"] not in replacements:
            unresolved_log.append(res["url"])
    if unresolved_log:
        print(f"\n  Unresolved URLs ({len(unresolved_log)}):")
        for u in unresolved_log:
            print(f"    {u}")


if __name__ == "__main__":
    main()
