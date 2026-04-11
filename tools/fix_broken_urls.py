"""
Fix broken URLs by finding Wayback Machine snapshots or correct replacements.

Reads the external_url_check.json report, queries Wayback Machine API for
archived versions of 404 URLs, and produces a replacement mapping.

Usage:
  python tools/fix_broken_urls.py           # dry-run: show replacements
  python tools/fix_broken_urls.py --apply   # apply replacements to wiki files
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen, Request
from urllib.error import URLError

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORT = PROJECT_ROOT / "_workspace" / "external_url_check.json"
WIKI = PROJECT_ROOT / "wiki"

# Manual replacements for known URL pattern changes
MANUAL_REPLACEMENTS: dict[str, str] = {
    # justice.gov restructured URLs
    "https://www.justice.gov/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet":
        "https://www.justice.gov/archives/opa/pr/justice-department-leads-effort-among-multinational-partners-dismantle-worlds-largest-botnet",
    "https://www.justice.gov/opa/pr/leader-qakbot-malware-conspiracy-indictment-involvement-global-ransomware-scheme":
        "https://www.justice.gov/archives/opa/pr/leader-qakbot-malware-conspiracy-indictment-involvement-global-ransomware-scheme",
    "https://www.justice.gov/opa/pr/thirty-six-defendants-indicted-alleged-roles-transnational-criminal-organization":
        "https://www.justice.gov/archives/opa/pr/thirty-six-defendants-indicted-alleged-roles-transnational-criminal-organization",
    "https://www.justice.gov/opa/pr/fourteen-individuals-associated-qqaazz-charged-laundering-money-stolen-cybercriminals":
        "https://www.justice.gov/archives/opa/pr/fourteen-individuals-associated-qqaazz-charged-laundering-money-stolen-cybercriminals",
    "https://www.justice.gov/opa/pr/150-arrested-hit-against-dark-web-marketplaces":
        "https://www.justice.gov/archives/opa/pr/150-arrested-hit-against-dark-web-marketplaces",
}

# URLs to add to bot-protected whitelist (403 but actually accessible in browser)
BOT_PROTECTED_ADDITIONS: list[str] = [
    "group-ib.com",
    "www.group-ib.com",
    "moneylaunderingnews.com",
    "www.moneylaunderingnews.com",
    "techxplore.com",
]


def query_wayback(url: str) -> str | None:
    """Query Wayback Machine API for the latest available snapshot."""
    api_url = f"https://archive.org/wayback/available?url={quote(url, safe='')}"
    try:
        req = Request(api_url, headers={"User-Agent": "IC-Wiki-LinkChecker/1.0"})
        with urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        snapshot = data.get("archived_snapshots", {}).get("closest", {})
        if snapshot.get("available"):
            return snapshot["url"]
    except (URLError, json.JSONDecodeError, TimeoutError):
        pass
    return None


def load_broken_urls() -> list[dict]:
    """Load 404/not_found URLs from the check report."""
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    return [
        r for r in data["results"]
        if r["category"] in ("not_found", "server_error")
    ]


def find_replacements(broken: list[dict]) -> dict[str, dict]:
    """Find replacement URLs via manual map + Wayback Machine."""
    replacements: dict[str, dict] = {}

    for r in broken:
        url = r["url"]
        files = r.get("referenced_by", [])

        # Check manual replacements first
        if url in MANUAL_REPLACEMENTS:
            replacements[url] = {
                "new_url": MANUAL_REPLACEMENTS[url],
                "source": "manual",
                "files": files,
            }
            print(f"  [manual] {url[:70]}")
            continue

        # Query Wayback Machine
        wayback = query_wayback(url)
        if wayback:
            replacements[url] = {
                "new_url": wayback,
                "source": "wayback",
                "files": files,
            }
            print(f"  [wayback] {url[:70]}")
        else:
            print(f"  [no-archive] {url[:70]}")
        time.sleep(0.5)  # Rate limit Wayback API

    return replacements


def apply_replacements(replacements: dict[str, dict]) -> int:
    """Apply URL replacements to wiki markdown files."""
    count = 0
    for old_url, info in replacements.items():
        new_url = info["new_url"]
        for rel_path in info["files"]:
            fpath = WIKI / rel_path
            if not fpath.exists():
                continue
            text = fpath.read_text(encoding="utf-8")
            if old_url in text:
                text = text.replace(old_url, new_url)
                fpath.write_text(text, encoding="utf-8")
                count += 1
                print(f"  [OK] {rel_path}: replaced")
    return count


def main() -> None:
    apply = "--apply" in sys.argv

    print("=== Broken URL Fixer ===")
    print(f"  Mode: {'APPLY' if apply else 'DRY-RUN'}\n")

    broken = load_broken_urls()
    print(f"  404/503 URLs to fix: {len(broken)}\n")

    print("Finding replacements...")
    replacements = find_replacements(broken)

    print(f"\n  Found replacements: {len(replacements)}/{len(broken)}")
    print(f"    Manual: {sum(1 for v in replacements.values() if v['source'] == 'manual')}")
    print(f"    Wayback: {sum(1 for v in replacements.values() if v['source'] == 'wayback')}")

    if apply and replacements:
        print("\nApplying replacements...")
        count = apply_replacements(replacements)
        print(f"\n  {count} file(s) updated.")
    elif replacements:
        print("\nDry-run complete. Use --apply to apply replacements.")

    # Save replacement map for reference
    out = PROJECT_ROOT / "_workspace" / "url_replacements.json"
    out.write_text(json.dumps(replacements, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Replacement map: {out}")


if __name__ == "__main__":
    main()
