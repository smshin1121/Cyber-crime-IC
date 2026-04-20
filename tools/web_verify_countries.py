"""
Batch web verification of participating_countries using a real Chromium
(via browser-use / Playwright) to bypass Cloudflare.

Reads `.verification/verify_queue.json` (produced by
`collect_verify_queue.py`), walks each op's source URLs, dumps rendered
page text, scans for country names, and appends findings to
`.verification/web_verified.md`.

This script does NOT modify any wiki pages — output is a human-review
artefact. Apply L19 three-bucket policy manually afterwards.

Install (one-time):
    uv add browser-use playwright beautifulsoup4
    uvx browser-use install   # chromium

Run:
    python tools/web_verify_countries.py --limit 10
"""
from __future__ import annotations
import argparse
import asyncio
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from browser_use import Browser  # type: ignore
except Exception:  # noqa: BLE001
    Browser = None  # sentinel; script warns if unavailable
try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # noqa: BLE001
    BeautifulSoup = None

import yaml  # from existing project deps


ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / ".verification" / "verify_queue.json"
COUNTRIES_DIR = ROOT / "wiki" / "countries"
OUT = ROOT / ".verification" / "web_verified.md"
RAW_CACHE = ROOT / ".verification" / "web_cache"
RAW_CACHE.mkdir(parents=True, exist_ok=True)


@dataclass
class CountryProfile:
    slug: str
    title: str
    aliases: list[str]

    def patterns(self) -> list[re.Pattern[str]]:
        needles = {self.title, *self.aliases, self.slug.replace("-", " ")}
        needles.discard("")
        return [re.compile(r"\b" + re.escape(n) + r"\b", re.IGNORECASE)
                for n in sorted(needles, key=len, reverse=True) if len(n) >= 3]


def _fm(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def build_country_index() -> dict[str, CountryProfile]:
    out: dict[str, CountryProfile] = {}
    # common abbreviations that often appear in press releases
    alias_overrides = {
        "united-states": ["US", "USA", "U.S.", "U.S.A.", "America"],
        "united-kingdom": ["UK", "U.K.", "Britain", "British"],
        "netherlands": ["Dutch", "Holland"],
        "germany": ["German"],
        "france": ["French"],
        "italy": ["Italian"],
        "spain": ["Spanish"],
        "russia": ["Russian"],
        "china": ["Chinese", "PRC"],
        "japan": ["Japanese"],
        "south-korea": ["Korea", "Korean", "Republic of Korea", "ROK"],
        "united-arab-emirates": ["UAE"],
    }
    for md in COUNTRIES_DIR.glob("*.md"):
        if md.name.startswith("_"):
            continue
        fm = _fm(md)
        slug = md.stem
        title = str(fm.get("title") or slug).strip()
        aliases_raw = fm.get("aliases") or []
        if isinstance(aliases_raw, str):
            aliases_raw = [aliases_raw]
        aliases = [str(a).strip() for a in aliases_raw if a]
        aliases.extend(alias_overrides.get(slug, []))
        out[slug] = CountryProfile(slug=slug, title=title, aliases=aliases)
    return out


async def fetch_page(url: str, timeout_s: float = 25.0) -> str:
    if Browser is None:
        raise RuntimeError(
            "browser-use not installed. Run: uv add browser-use "
            "playwright beautifulsoup4 && uvx browser-use install"
        )
    browser = Browser()
    try:
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded", timeout=int(timeout_s * 1000))
        # Give Cloudflare a moment to run challenge + any JS renderers
        await page.wait_for_timeout(3500)
        html = await page.content()
        return html
    finally:
        await browser.close()


def extract_text(html: str) -> str:
    if BeautifulSoup is None:
        # naive strip
        return re.sub(r"<[^>]+>", " ", html)
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)


def scan_countries(text: str, countries: dict[str, CountryProfile],
                   candidates: list[str]) -> dict[str, bool]:
    out: dict[str, bool] = {}
    for slug in candidates:
        profile = countries.get(slug)
        if not profile:
            out[slug] = False
            continue
        found = any(p.search(text) for p in profile.patterns())
        out[slug] = found
    return out


def cache_path(url: str) -> Path:
    h = re.sub(r"[^a-z0-9]+", "-", url.lower())[:120]
    return RAW_CACHE / f"{h}.txt"


async def verify_op(op: dict, countries: dict[str, CountryProfile]) -> dict:
    op_slug = op["op_slug"]
    pc = op["participating_countries"]
    results: list[dict[str, Any]] = []
    hits_union: set[str] = set()
    for src in op["source_urls"]:
        url = src["url"]
        cache = cache_path(url)
        text = ""
        fetched = False
        err: str | None = None
        if cache.exists():
            text = cache.read_text(encoding="utf-8", errors="replace")
        else:
            try:
                html = await fetch_page(url)
                text = extract_text(html)
                cache.write_text(text, encoding="utf-8")
                fetched = True
            except Exception as exc:  # noqa: BLE001
                err = str(exc)[:200]

        if text:
            found = scan_countries(text, countries, pc)
            hits = [c for c, f in found.items() if f]
            hits_union.update(hits)
            results.append({
                "url": url,
                "publisher": src.get("publisher", ""),
                "fetched_now": fetched,
                "char_count": len(text),
                "found": hits,
                "missing": [c for c, f in found.items() if not f],
                "error": err,
            })
        else:
            results.append({
                "url": url,
                "publisher": src.get("publisher", ""),
                "error": err or "no_text",
                "found": [],
                "missing": list(pc),
            })
    return {
        "op_slug": op_slug,
        "op_title": op["op_title"],
        "pc": pc,
        "verified_union": sorted(hits_union),
        "still_missing": sorted(set(pc) - hits_union),
        "sources": results,
    }


def render_report(entries: list[dict]) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        "# participating_countries — web-rendered primary-source verification",
        "",
        f"_Run: {now}_",
        "",
        "This report fetches each cited source URL through a real Chromium "
        "instance (browser-use / Playwright) to get past Cloudflare-protected "
        "pages that `WebFetch` cannot reach. For every operation in the "
        "verification queue, each country in its `participating_countries` "
        "list is checked against the rendered page text.",
        "",
        "- **verified_union**: country was explicitly named in at least one "
        "source page",
        "- **still_missing**: country NOT found in any accessible source page",
        "",
        "Still-missing ≠ wrong. It means the accessible primary sources do "
        "not explicitly name the country. Treat it as an input to L19 policy "
        "(verified / removed / pending), not an automatic delete signal.",
        "",
        "## Summary",
        "",
    ]
    total = len(entries)
    fully = [e for e in entries if not e["still_missing"]]
    partial = [e for e in entries if e["still_missing"] and e["verified_union"]]
    none = [e for e in entries if not e["verified_union"]]
    lines += [
        f"- Operations processed: {total}",
        f"- Fully verified via web: {len(fully)}",
        f"- Partially verified: {len(partial)}",
        f"- No countries verified (source fetch failed or empty): {len(none)}",
        "",
        "## Results",
        "",
    ]
    for e in entries:
        lines += [f"### {e['op_slug']}", ""]
        lines.append(f"**Title**: {e['op_title']}  ")
        lines.append(f"**Participating (frontmatter, {len(e['pc'])})**: "
                     f"{', '.join(e['pc']) or '—'}  ")
        lines.append(f"**Verified via web ({len(e['verified_union'])})**: "
                     f"{', '.join(e['verified_union']) or '—'}  ")
        lines.append(f"**Still missing ({len(e['still_missing'])})**: "
                     f"{', '.join(e['still_missing']) or '—'}")
        lines.append("")
        lines.append("| Source | Publisher | Chars | Found | Missing | Error |")
        lines.append("|---|---|---:|---|---|---|")
        for s in e["sources"]:
            lines.append(
                f"| {s['url']} | {s.get('publisher','')} | "
                f"{s.get('char_count',0)} | {', '.join(s.get('found',[]))} | "
                f"{', '.join(s.get('missing',[]))[:80]} | {s.get('error') or ''} |"
            )
        lines.append("")
    return "\n".join(lines)


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None,
                    help="Process at most N ops from queue")
    ap.add_argument("--op", type=str, default=None,
                    help="Process a single op slug (overrides --limit)")
    args = ap.parse_args()

    if not QUEUE.exists():
        print(f"[web-verify] missing {QUEUE}; run collect_verify_queue.py first",
              file=sys.stderr)
        return 1

    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    if args.op:
        queue = [q for q in queue if q["op_slug"] == args.op]
    elif args.limit:
        queue = queue[: args.limit]

    countries = build_country_index()
    print(f"[web-verify] ops to process: {len(queue)}", flush=True)

    entries: list[dict] = []
    for i, op in enumerate(queue, 1):
        print(f"[web-verify] ({i}/{len(queue)}) {op['op_slug']} — "
              f"{len(op['source_urls'])} URL(s)", flush=True)
        try:
            result = await verify_op(op, countries)
        except Exception as exc:  # noqa: BLE001
            print(f"[web-verify] FAILED {op['op_slug']}: {exc}", flush=True)
            continue
        entries.append(result)
        # incremental save so background runs aren't lost on interrupt
        OUT.write_text(render_report(entries), encoding="utf-8")

    print(f"[web-verify] report -> {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
