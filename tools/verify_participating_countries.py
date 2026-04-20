"""
Background audit: cross-check every operation's `participating_countries` list
against local text (op body + cited wiki/sources summaries + raw/ files).

Produces `.verification/participating_countries_audit.md` with three buckets
per operation:

  verified  — country name explicitly found in at least one local text
  unverified — country in frontmatter but not in any local text
  text_scan_failed — local source files missing / unreadable

This is a LOCAL-only pass (no web fetch). It complements the web-based Colombia
and Avalanche audits already in place. It is safe to run repeatedly.

Run:
    python tools/verify_participating_countries.py
"""
from __future__ import annotations
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parent.parent
OPS = ROOT / "wiki" / "operations"
COUNTRIES = ROOT / "wiki" / "countries"
SOURCES = ROOT / "wiki" / "sources"
RAW = ROOT / "raw"
OUT = ROOT / ".verification"
OUT.mkdir(exist_ok=True)


@dataclass
class CountryProfile:
    slug: str
    title: str
    aliases: list[str] = field(default_factory=list)

    @property
    def patterns(self) -> list[re.Pattern[str]]:
        needles = {self.title, *self.aliases}
        # crude fallback: turn slug into spaced form
        needles.add(self.slug.replace("-", " "))
        needles.discard("")
        pats: list[re.Pattern[str]] = []
        for n in sorted(needles, key=len, reverse=True):
            if len(n) < 3:
                continue
            pats.append(re.compile(r"\b" + re.escape(n) + r"\b", re.IGNORECASE))
        return pats


def load_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return {}
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}
    return fm if isinstance(fm, dict) else {}


def load_body(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    body = re.sub(r"^---\n.*?\n---\n?", "", text, count=1, flags=re.DOTALL)
    return body


def wikilink_to_slug(val: str) -> str:
    m = re.match(r"\[\[([^\|\]]+)", val.strip())
    return m.group(1).strip().lower() if m else val.strip().lower()


def build_country_index() -> dict[str, CountryProfile]:
    out: dict[str, CountryProfile] = {}
    for md in COUNTRIES.glob("*.md"):
        if md.name.startswith("_"):
            continue
        fm = load_frontmatter(md)
        slug = md.stem
        title = str(fm.get("title") or slug).strip()
        aliases_raw = fm.get("aliases") or []
        if isinstance(aliases_raw, str):
            aliases_raw = [aliases_raw]
        aliases = [str(a).strip() for a in aliases_raw if a]
        out[slug] = CountryProfile(slug=slug, title=title, aliases=aliases)
    return out


def resolve_source_text(source_ref: str) -> str:
    """Gather text for a cited source (summary + raw file if linked)."""
    slug = wikilink_to_slug(source_ref)
    chunks: list[str] = []
    summary_path = SOURCES / f"{slug}.md"
    if summary_path.exists():
        chunks.append(load_body(summary_path))
        fm = load_frontmatter(summary_path)
        raw_rel = fm.get("raw_path") or ""
        if raw_rel:
            raw_path = (ROOT / raw_rel).resolve()
            if raw_path.exists():
                chunks.append(load_body(raw_path))
    return "\n\n".join(c for c in chunks if c)


def iter_operations() -> Iterable[Path]:
    for md in OPS.glob("*.md"):
        if md.name.startswith("_"):
            continue
        yield md


def verify_one(op_path: Path, countries: dict[str, CountryProfile]) -> dict:
    fm = load_frontmatter(op_path)
    op_slug = op_path.stem
    pc_raw = fm.get("participating_countries") or []
    if not pc_raw:
        return {"slug": op_slug, "skip": "no_participating_countries"}

    op_body = load_body(op_path)
    source_texts: list[str] = [op_body]
    sources = fm.get("sources") or []
    missing_sources = 0
    for src in sources:
        if not src:
            continue
        txt = resolve_source_text(str(src))
        if txt:
            source_texts.append(txt)
        else:
            missing_sources += 1

    combined = "\n\n".join(source_texts)

    verified: list[str] = []
    unverified: list[str] = []
    unknown: list[str] = []

    for entry in pc_raw:
        country_slug = wikilink_to_slug(str(entry))
        profile = countries.get(country_slug)
        if not profile:
            unknown.append(country_slug)
            continue
        if any(p.search(combined) for p in profile.patterns):
            verified.append(country_slug)
        else:
            unverified.append(country_slug)

    return {
        "slug": op_slug,
        "title": str(fm.get("title") or op_slug),
        "pc_total": len(pc_raw),
        "verified": verified,
        "unverified": unverified,
        "unknown": unknown,
        "source_count": len(sources),
        "missing_sources": missing_sources,
    }


def write_report(results: list[dict]) -> Path:
    results.sort(key=lambda r: (-(len(r.get("unverified") or [])), r["slug"]))
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines: list[str] = [
        "# participating_countries — local-text verification audit",
        "",
        f"_Run: {now}_",
        "",
        "This report cross-checks every operation's `participating_countries` "
        "frontmatter entries against local text (operation body + cited "
        "`wiki/sources/*.md` summaries + their `raw_path` raw files). It does "
        "NOT fetch the web.",
        "",
        "- **verified**: country name was found in at least one local text file",
        "- **unverified**: country in frontmatter but NOT found in any local "
        "text — candidate for primary-source re-verification",
        "- `missing_sources`: count of source references with no matching file",
        "",
        "Unverified ≠ wrong. For operations whose primary sources are only "
        "reachable on the web (e.g., Europol press releases behind Cloudflare), "
        "the real text is not on disk. Treat large `unverified` lists as a "
        "prompt to recover the full source, not as evidence of non-participation.",
        "",
        "## Summary",
        "",
    ]

    total = len(results)
    with_pc = [r for r in results if "skip" not in r]
    any_unverified = [r for r in with_pc if r["unverified"]]
    fully_verified = [r for r in with_pc if not r["unverified"]]

    lines.append(f"- Operations scanned: {total}")
    lines.append(f"- With participating_countries: {len(with_pc)}")
    lines.append(f"- Fully verified (every country found in local text): {len(fully_verified)}")
    lines.append(f"- With ≥1 unverified country: {len(any_unverified)}")
    lines.append("")
    lines.append("## Operations with unverified countries")
    lines.append("")
    lines.append("| Op | Total | Verified | Unverified | Missing src files | Unverified list |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for r in any_unverified[:500]:
        unv = ", ".join(r["unverified"][:12])
        if len(r["unverified"]) > 12:
            unv += f", … (+{len(r['unverified']) - 12})"
        lines.append(
            f"| [[{r['slug']}]] | {r['pc_total']} | {len(r['verified'])} | "
            f"{len(r['unverified'])} | {r['missing_sources']} | {unv} |"
        )
    if len(any_unverified) > 500:
        lines.append("")
        lines.append(f"_…{len(any_unverified) - 500} more rows truncated._")

    lines.append("")
    lines.append("## Operations fully verified (every country in local text)")
    lines.append("")
    for r in fully_verified[:300]:
        lines.append(f"- [[{r['slug']}]] — {r['pc_total']} countries")
    if len(fully_verified) > 300:
        lines.append(f"- _…{len(fully_verified) - 300} more truncated._")

    out_path = OUT / "participating_countries_audit.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main() -> int:
    countries = build_country_index()
    print(f"[verify] country index: {len(countries)} profiles", flush=True)

    results: list[dict] = []
    ops = list(iter_operations())
    total = len(ops)
    for i, op in enumerate(ops, 1):
        try:
            r = verify_one(op, countries)
        except Exception as exc:  # noqa: BLE001
            r = {"slug": op.stem, "error": str(exc)}
        results.append(r)
        if i % 50 == 0 or i == total:
            print(f"[verify] {i}/{total}", flush=True)

    out = write_report(results)
    print(f"[verify] report -> {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
