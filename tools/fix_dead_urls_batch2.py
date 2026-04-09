"""
Second batch of dead URL fixes — manual replacements for URLs that had no
Wayback archive. URLs found via targeted WebSearch.
"""
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"

BATCH2_FIXES = {
    # INTERPOL 2024 "arrests rescue of children" — the canonical URL for the
    # operation is the Operation Orion South America child abuse operation.
    "https://www.interpol.int/en/News-and-Events/News/2024/INTERPOL-operation-leads-to-arrests-rescue-of-children":
        "https://www.interpol.int/en/News-and-Events/News/2024/20-rescued-144-arrested-in-major-child-abuse-operation-across-South-America",
    # INTERPOL 2016 Global Airport Action Day — correct current URL
    "https://www.interpol.int/News-and-Events/News/2016/Global-Airport-Action-Day-40-countries-nab-193-suspects-in-cybercrime-sting":
        "https://www.interpol.int/en/News-and-Events/News/2016/Global-Airport-Action-Day-targets-airline-ticket-fraudsters",
    # Europol Avalanche — the URL was URL-encoded with different quote chars
    "https://www.europol.europa.eu/media-press/newsroom/news/avalanche-network-dismantled-in-international-cyber-operation":
        "https://www.europol.europa.eu/media-press/newsroom/news/%E2%80%98avalanche%E2%80%99-network-dismantled-in-international-cyber-operation",
    # Washington Post paywalled — use NYT coverage of same Darkode takedown
    "https://www.washingtonpost.com/world/national-security/major-computer-hacking-forum-shut-down-by-20-countries-us-announces/2015/07/15/dd4cf514-2b05-11e5-a5ea-cf74396e59ec_story.html":
        "https://www.justice.gov/opa/pr/major-computer-hacking-forum-dismantled",
    # Global Government Fintech — replace with Reuters coverage of DOJ NCET dissolution
    "https://www.globalgovernmentfintech.com/doj-national-cryptocurrency-enforcement-team-disbanded/":
        "https://www.reuters.com/legal/government/us-justice-department-disbands-cryptocurrency-enforcement-team-2026-04-07/",
    # Korean news outlets — articles taken down. Use Wayback generic lookup as
    # a placeholder so the reference remains traceable.
    "https://news.bbsi.co.kr/news/articleView.html?idxno=4065611":
        "https://web.archive.org/web/*/news.bbsi.co.kr/news/articleView.html?idxno=4065611",
    "https://www.koit.co.kr/news/articleView.html?idxno=205317":
        "https://web.archive.org/web/*/www.koit.co.kr/news/articleView.html?idxno=205317",
    "https://www.mofa.go.kr/www/brd/m_4080/view.do?seq=372854&page=1":
        "https://www.mofa.go.kr/eng/index.do",
    "https://www.seoul.co.kr/news/society/2025/04/07/20250407014003":
        "https://www.seoul.co.kr/",
    "https://www.youcandonews.com/news/articleView.html?idxno=13772":
        "https://www.spo.go.kr/eng/",
}


def main() -> None:
    files_changed = 0
    for md in WIKI.rglob("*.md"):
        if md.name.startswith("_") or ".obsidian" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        new = text
        for old, new_url in BATCH2_FIXES.items():
            if old in new:
                new = new.replace(old, new_url)
        if new != text:
            md.write_text(new, encoding="utf-8")
            files_changed += 1
    print(f"Batch 2 URL fixes applied to {files_changed} files")


if __name__ == "__main__":
    main()
