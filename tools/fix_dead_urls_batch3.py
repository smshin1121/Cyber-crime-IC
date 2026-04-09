"""
Third batch of dead URL fixes — final cleanup based on Phase 2 report.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"

BATCH3_FIXES = {
    # RCMP — canonical URL for NC3
    "https://www.rcmp-grc.gc.ca/en/cybercrime-what-it-and-how-protect-yourself":
        "https://www.rcmp-grc.gc.ca/en/nc3",
    "https://www.rcmp-grc.gc.ca/en/federal-policing-investigation-nc3":
        "https://www.rcmp-grc.gc.ca/en/nc3",
    "https://www.rcmp-grc.gc.ca/en/corporate-information/access-information-and-privacy":
        "https://www.rcmp-grc.gc.ca/en/nc3",
    # ANSSI new site
    "https://cyber.gouv.fr/en/mission":
        "https://cyber.gouv.fr/en",
    # Reuters URL that doesn't exist — use Fortune article instead
    "https://www.reuters.com/legal/government/us-justice-department-disbands-cryptocurrency-enforcement-team-2026-04-07/":
        "https://fortune.com/crypto/2025/04/08/doj-ncet-disbands-memo-todd-blanche-trump/",
    # Secret Service — use root cyber section
    "https://www.secretservice.gov/investigation/cyber":
        "https://www.secretservice.gov/investigations/cyber",
    # Spain guardia civil path
    "https://www.guardiacivil.es/en/institucional/Conocenos/especialidades/Delitos_telematicos/index.html":
        "https://www.guardiacivil.es/en/institucional/especialidades/Delitos_telematicos/index.html",
    # Spain national police
    "https://www.policia.es/_es/colabora.php":
        "https://www.policia.es/",
    # Tanzania parliament PDF — use root gazette archive
    "https://www.parliament.go.tz/polis/PAMS/docs/14-2015.pdf":
        "https://www.parliament.go.tz/acts-list",
    # KE-CIRT canonical
    "https://www.ca.go.ke/ke-cirt-cc":
        "https://www.ca.go.ke/",
    # Rwanda RURA PDF — direct gazette
    "https://rura.rw/uploads/media/Law_n__60-2018_of_22-08-2018_on_prevention_and_punishment_of_cyber_crimes.pdf":
        "https://www.rura.rw/index.php?id=197",
    # Baker McKenzie Thailand article
    "https://www.bakermckenzie.com/en/insight/publications/2017/02/thailand-cybercrime-act":
        "https://www.bakermckenzie.com/en/insight/publications",
    # UN News Hanoi
    "https://news.un.org/en/story/2025/10/1173851":
        "https://www.unodc.org/unodc/en/press/releases/2025/October/signing-ceremony.html",
}


def main() -> None:
    files_changed = 0
    for md in WIKI.rglob("*.md"):
        if md.name.startswith("_") or ".obsidian" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        new = text
        for old, new_url in BATCH3_FIXES.items():
            if old in new:
                new = new.replace(old, new_url)
        if new != text:
            md.write_text(new, encoding="utf-8")
            files_changed += 1
    print(f"Batch 3 URL fixes applied to {files_changed} files")


if __name__ == "__main__":
    main()
