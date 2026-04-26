from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import frontmatter

from source_canonical_map import score_source, word_count


ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "wiki" / "sources"
WORKSPACE = ROOT / "_workspace"
REPORT_PATH = ROOT / "wiki" / "analysis" / "source-duplicate-normalization-2026-04-26.md"


@dataclass
class SourceCandidate:
    slug: str
    path: Path
    title: str
    publisher: str
    publish_date: str
    collection_url: str
    content_hash: str
    duplicate_of: str
    score: int
    word_count_value: int
    body_words: int
    post: frontmatter.Post


@dataclass(frozen=True)
class SourceAlias:
    slug: str
    canonical_slug: str
    reason: str
    key: str
    title: str
    canonical_title: str


def wikilink_slug(value: Any) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def int_value(value: Any) -> int:
    try:
        return int(value)
    except Exception:
        return 0


def scalar_text(value: Any) -> str:
    if isinstance(value, dt.datetime):
        return value.date().isoformat()
    if isinstance(value, dt.date):
        return value.isoformat()
    return str(value or "").strip()


def load_sources() -> list[SourceCandidate]:
    rows: list[SourceCandidate] = []
    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        post = frontmatter.load(path)
        meta = post.metadata
        body_words = word_count(post.content or "")
        score, _ = score_source(path.stem, meta, body_words)
        rows.append(
            SourceCandidate(
                slug=path.stem,
                path=path,
                title=str(meta.get("title") or path.stem),
                publisher=str(meta.get("publisher") or ""),
                publish_date=str(meta.get("publish_date") or ""),
                collection_url=str(meta.get("collection_url") or "").strip(),
                content_hash=str(meta.get("content_hash") or "").strip(),
                duplicate_of=wikilink_slug(meta.get("duplicate_of")),
                score=score,
                word_count_value=int_value(meta.get("word_count")),
                body_words=body_words,
                post=post,
            )
        )
    return rows


def grouped(rows: list[SourceCandidate], field: str) -> list[tuple[str, list[SourceCandidate]]]:
    buckets: dict[str, list[SourceCandidate]] = defaultdict(list)
    for row in rows:
        value = getattr(row, field)
        if value:
            buckets[value].append(row)
    return sorted(
        ((value, members) for value, members in buckets.items() if len(members) > 1),
        key=lambda item: (-len(item[1]), item[0]),
    )


def choose_canonical(members: list[SourceCandidate], alias_slugs: set[str]) -> SourceCandidate:
    active = [row for row in members if not row.duplicate_of and row.slug not in alias_slugs]
    pool = active or members
    return sorted(pool, key=lambda row: (-row.score, -row.word_count_value, -row.body_words, row.slug))[0]


def mark_alias(row: SourceCandidate, canonical: SourceCandidate, reason: str, key: str, apply: bool) -> SourceAlias | None:
    meta = row.post.metadata
    expected = {
        "duplicate_of": wikilink(canonical.slug),
        "duplicate_reason": reason,
        "duplicate_key": key,
        "duplicate_normalized_at": "2026-04-26",
    }

    changed = any(scalar_text(meta.get(field)) != value for field, value in expected.items())

    if not changed:
        return None

    if apply:
        update_frontmatter_fields(row.path, expected)

    return SourceAlias(
        slug=row.slug,
        canonical_slug=canonical.slug,
        reason=reason,
        key=key,
        title=row.title,
        canonical_title=canonical.title,
    )


def yaml_value(field: str, value: str) -> str:
    if field in {"duplicate_of", "duplicate_key"}:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def update_frontmatter_fields(path: Path, fields: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(?P<frontmatter>.*?)(?P<tail>\r?\n---\r?\n)", text, re.S)
    if not match:
        raise ValueError(f"Missing frontmatter block: {path}")

    frontmatter_text = match.group("frontmatter")
    tail = text[match.start("tail") :]
    lines = frontmatter_text.splitlines()
    seen: set[str] = set()
    updated_lines: list[str] = []

    for line in lines:
        field = line.split(":", 1)[0] if ":" in line and not line.startswith((" ", "\t")) else ""
        if field in fields:
            updated_lines.append(f"{field}: {yaml_value(field, fields[field])}")
            seen.add(field)
        else:
            updated_lines.append(line)

    for field, value in fields.items():
        if field not in seen:
            updated_lines.append(f"{field}: {yaml_value(field, value)}")

    path.write_text(text[: match.start("frontmatter")] + "\n".join(updated_lines) + tail, encoding="utf-8")


def normalize(rows: list[SourceCandidate], apply: bool, include_hash: bool) -> list[SourceAlias]:
    aliases: list[SourceAlias] = []
    alias_slugs = {row.slug for row in rows if row.duplicate_of}
    by_slug = {row.slug: row for row in rows}

    for url, members in grouped(rows, "collection_url"):
        canonical = choose_canonical(members, alias_slugs)
        for row in members:
            if row.slug == canonical.slug:
                continue
            alias = mark_alias(row, canonical, "same_collection_url", url, apply)
            alias_slugs.add(row.slug)
            if alias:
                aliases.append(alias)

    if not include_hash:
        return aliases

    # After URL aliases are assigned, resolve only the remaining active exact-content duplicates.
    active_rows = [row for row in rows if row.slug not in alias_slugs and not row.duplicate_of]
    for content_hash, members in grouped(active_rows, "content_hash"):
        canonical = choose_canonical(members, alias_slugs)
        for row in members:
            if row.slug == canonical.slug:
                continue
            alias = mark_alias(row, canonical, "same_content_hash", content_hash, apply)
            alias_slugs.add(row.slug)
            if alias:
                aliases.append(alias)

    # Avoid mypy/linters complaining about by_slug being unused when adding future checks.
    _ = by_slug
    return aliases


def write_csv(aliases: list[SourceAlias]) -> Path:
    path = WORKSPACE / "source_duplicate_normalization_2026-04-26.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["slug", "canonical_slug", "reason", "key", "title", "canonical_title"])
        for alias in aliases:
            writer.writerow(
                [
                    alias.slug,
                    alias.canonical_slug,
                    alias.reason,
                    alias.key,
                    alias.title,
                    alias.canonical_title,
                ]
            )
    return path


def render_report(rows: list[SourceCandidate], aliases: list[SourceAlias], apply: bool, include_hash: bool) -> str:
    url_groups = grouped(rows, "collection_url")
    hash_groups = grouped(rows, "content_hash")
    url_aliases = [alias for alias in aliases if alias.reason == "same_collection_url"]
    hash_aliases = [alias for alias in aliases if alias.reason == "same_content_hash"]
    all_aliases = {row.slug for row in rows if row.duplicate_of} | {alias.slug for alias in aliases}

    lines = [
        "---",
        "title: Source Duplicate Normalization (2026-04-26)",
        "type: analysis",
        "created: 2026-04-26",
        "updated: 2026-04-26",
        'summary: "Canonical/alias normalization of duplicate source records."',
        "source_count: 0",
        "---",
        "## Summary",
        "",
        "Duplicate source records were normalized without deleting pages. Canonical source pages remain the primary records, while alternates stay addressable and carry `duplicate_of` metadata so audits can distinguish active duplicate records from preserved aliases.",
        "",
        f"- Mode: **{'apply' if apply else 'dry-run'}**",
        f"- Source pages scanned: **{len(rows)}**",
        f"- Duplicate URL groups considered: **{len(url_groups)}**",
        f"- Duplicate content-hash groups considered: **{len(hash_groups)}**",
        f"- Content-hash normalization: **{'enabled' if include_hash else 'disabled'}**",
        f"- New/updated URL aliases: **{len(url_aliases)}**",
        f"- New/updated content-hash aliases: **{len(hash_aliases)}**",
        f"- Total alias-marked source pages after normalization: **{len(all_aliases)}**",
        "",
        "## Alias Changes",
        "",
        "| Rank | Alias | Canonical | Reason | Key |",
        "|---:|---|---|---|---|",
    ]

    for idx, alias in enumerate(aliases[:200], 1):
        key = alias.key
        if len(key) > 140:
            key = key[:137] + "..."
        lines.append(
            f"| {idx} | [[{alias.slug}]] | [[{alias.canonical_slug}]] | {alias.reason} | {key} |"
        )

    if len(aliases) > 200:
        lines.append(f"| ... | ... | ... | ... | +{len(aliases) - 200} more aliases in `_workspace/source_duplicate_normalization_2026-04-26.csv` |")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Mark duplicate wiki source pages as canonical aliases.")
    parser.add_argument("--apply", action="store_true", help="Write duplicate_of metadata. Omit for dry-run.")
    parser.add_argument(
        "--include-hash",
        action="store_true",
        help="Also normalize exact content_hash duplicates. Use only after reviewing cross-URL hash groups.",
    )
    args = parser.parse_args()

    rows = load_sources()
    aliases = normalize(rows, apply=args.apply, include_hash=args.include_hash)
    csv_path = write_csv(aliases)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(render_report(rows, aliases, apply=args.apply, include_hash=args.include_hash), encoding="utf-8")

    print(f"Mode: {'apply' if args.apply else 'dry-run'}")
    print(f"Sources scanned: {len(rows)}")
    print(f"Aliases new/updated: {len(aliases)}")
    print(f"CSV: {csv_path}")
    print(f"Report: {REPORT_PATH}")


if __name__ == "__main__":
    main()
