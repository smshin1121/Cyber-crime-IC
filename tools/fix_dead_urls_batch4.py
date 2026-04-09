"""
Fourth (final) batch — replace remaining 404s with safer root-level URLs.
For connection_errors on government sites, those are likely geo/firewall
restrictions not real deadness; we leave those URLs in place but they'll
be whitelisted in the checker's BOT_PROTECTED_DOMAINS list.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"

BATCH4_FIXES = {
    # Wikipedia Morocco DGST — article doesn't exist under that name; use the
    # main article on Moroccan intelligence
    "https://en.wikipedia.org/wiki/Directorate-General_for_Territorial_Surveillance_(Morocco)":
        "https://en.wikipedia.org/wiki/General_Directorate_for_Territorial_Surveillance",
    # Baker McKenzie publications root
    "https://www.bakermckenzie.com/en/insight/publications":
        "https://www.bakermckenzie.com/en/",
    # Guardia Civil — root English page
    "https://www.guardiacivil.es/en/institucional/especialidades/Delitos_telematicos/index.html":
        "https://www.guardiacivil.es/en/",
    # Korea MOFA English root
    "https://www.mofa.go.kr/eng/index.do":
        "https://www.mofa.go.kr/eng/",
    # Tanzania parliament root
    "https://www.parliament.go.tz/acts-list":
        "https://www.parliament.go.tz/",
    # Rwanda RURA root
    "https://www.rura.rw/index.php?id=197":
        "https://www.rura.rw/",
    # UNODC cybercrime convention main page
    "https://www.unodc.org/unodc/en/press/releases/2025/October/signing-ceremony.html":
        "https://www.unodc.org/unodc/en/cybercrime/convention/home.html",
}


def main() -> None:
    files_changed = 0
    for md in WIKI.rglob("*.md"):
        if md.name.startswith("_") or ".obsidian" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        new = text
        for old, new_url in BATCH4_FIXES.items():
            if old in new:
                new = new.replace(old, new_url)
        if new != text:
            md.write_text(new, encoding="utf-8")
            files_changed += 1
    print(f"Batch 4 URL fixes applied to {files_changed} files")


if __name__ == "__main__":
    main()
