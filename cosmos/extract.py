#!/usr/bin/env python
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    for candidate in ("vendor37_build", "vendor_build2", ".vendor_build"):
        path = Path(candidate)
        if path.exists():
            sys.path.insert(0, str(path.resolve()))
            try:
                import yaml  # type: ignore
                break
            except ModuleNotFoundError:
                continue
    else:
        raise


LINK_FIELDS = {
    "related_frameworks", "related_mechanisms", "related_procedures",
    "related_concepts", "related_challenges", "related_cases",
    "related_operation", "related_operations",
    "implementing_mechanisms", "operations_enabled", "sponsoring_body",
    "parent_org", "country", "successor", "predecessor",
    "cooperation_partners", "frameworks_administered", "mechanisms_operated",
    "operations_participated", "notable_cases",
    "key_agencies", "bilateral_agreements",
    "lead_agency", "coordinating_body", "participating_countries",
    "participating_agencies", "legal_basis", "mechanisms_used",
    "challenges_encountered", "crime_type",
    "jurisdiction_country", "cooperating_agencies",
    "legal_frameworks_invoked", "key_legal_issues", "crime_charged",
    "administered_by", "mechanisms_involved",
    "typical_ic_challenges", "relevant_legal_frameworks",
    "typical_mechanisms", "key_organizations", "notable_operations",
    "affected_mechanisms", "affected_crime_types",
    "applied_in_cases", "pages_updated",
}

META_MAP = {
    "legal-framework": [("status", "status"), ("entry_into_force", "entry_into_force"), ("parties_states_parties", "parties.states_parties")],
    "country": [("legal_system", "legal_system"), ("region", "region"), ("ic_capacity_rating", "ic_capacity.rating")],
    "organization": [("org_type", "org_type"), ("status", "status"), ("established", "established"), ("headquarters", "headquarters")],
    "operation": [("status", "status"), ("operation_type", "operation_type"), ("outcome", "outcome"), ("results_arrests", "results.arrests")],
    "case": [("status", "status"), ("case_type", "case_type"), ("jurisdiction", "jurisdiction")],
    "mechanism": [("mechanism_type", "mechanism_type"), ("formality", "formality"), ("speed", "speed")],
    "procedure": [("procedure_type", "procedure_type"), ("average_duration", "average_duration")],
    "crime-type": [("crime_category", "crime_category")],
    "challenge": [("challenge_category", "challenge_category"), ("severity", "severity")],
    "concept": [("concept_category", "concept_category"), ("domain", "domain")],
}

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
SUMMARY_RE = re.compile(r"^##\s+Summary\s*$", re.MULTILINE)
SECTION_RE = re.compile(r"^##\s+", re.MULTILINE)
BODY_LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
EXCLUDED_NAMES = {"index.md", "log.md", "overview.md"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiki-dir", default="wiki")
    parser.add_argument("--out", default="cosmos/data.json")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def jsonable(value: Any) -> Any:
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [jsonable(v) for v in value]
    return value


def nested_get(data: Any, path: str) -> Any:
    cur = data
    for part in path.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
    return cur


def clean_markdown(text: str) -> str:
    text = re.sub(r"^\s*>\s*\[![^\]]+\].*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_summary(body: str) -> str:
    match = SUMMARY_RE.search(body)
    if match:
        start = match.end()
        next_section = SECTION_RE.search(body, start)
        body = body[start:next_section.start() if next_section else None]
    text = clean_markdown(body)
    if len(text) <= 250:
        return text
    return f"{text[:249].rsplit(' ', 1)[0].strip()}…"


def is_excluded(path: Path) -> bool:
    return path.name in EXCLUDED_NAMES or path.name == "_index.md"


def parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except Exception:
        print(f"[warn] yaml_parse_fail: {path.as_posix()}", file=sys.stderr)
        return None, text
    return data, text[match.end():]


def normalize_aliases(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def extract_link_targets(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(extract_link_targets(item))
        return out
    if isinstance(value, dict):
        out: list[str] = []
        for key in ("framework", "page", "target", "operation", "case", "organization", "country"):
            if key in value:
                out.extend(extract_link_targets(value[key]))
        return out
    text = str(value).strip()
    if not text:
        return []
    match = BODY_LINK_RE.search(text)
    if match:
        text = match.group(1)
    text = text.replace("\\", "/").split("/")[-1].replace(".md", "")
    return [text] if text else []


def build_meta(page_type: str, frontmatter: dict[str, Any]) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    for out_key, source_key in META_MAP.get(page_type, []):
        value = nested_get(frontmatter, source_key)
        if value not in (None, "", [], {}):
            meta[out_key] = jsonable(value)
    return meta


def collect_pages(wiki_dir: Path) -> tuple[list[dict[str, Any]], dict[str, str]]:
    collisions: dict[str, list[str]] = defaultdict(list)
    staged: list[dict[str, Any]] = []

    for path in sorted(wiki_dir.rglob("*.md")):
        if is_excluded(path):
            continue
        frontmatter, body = parse_frontmatter(path)
        if frontmatter is None:
            continue
        page_type = str(frontmatter.get("type", "")).strip()
        if not page_type:
            continue
        slug = path.stem
        collisions[slug].append(path.as_posix())
        title = frontmatter.get("title") or frontmatter.get("official_name") or slug.replace("-", " ").title()
        staged.append({
            "slug": slug,
            "path": path.as_posix(),
            "type": page_type,
            "title": str(title),
            "title_ko": jsonable(frontmatter.get("title_ko") or frontmatter.get("official_name_ko")),
            "aliases": normalize_aliases(frontmatter.get("aliases")),
            "summary": extract_summary(body),
            "source_count": int(frontmatter.get("source_count", 0) or 0),
            "created": jsonable(frontmatter.get("created")),
            "updated": jsonable(frontmatter.get("updated")),
            "frontmatter": frontmatter,
            "body": body,
            "meta": build_meta(page_type, frontmatter),
        })

    pages: list[dict[str, Any]] = []
    slug_to_id: dict[str, str] = {}
    for page in staged:
        slug = page["slug"]
        if len(collisions[slug]) > 1:
            print(f"[warn] id_collision: {slug} in {', '.join(collisions[slug][:2])}", file=sys.stderr)
            page["id"] = f"{page['type']}:{slug}"
        else:
            page["id"] = slug
            slug_to_id[slug] = slug
        pages.append(page)
    return pages, slug_to_id


def resolve_target(raw_target: str, slug_to_id: dict[str, str]) -> str | None:
    slug = raw_target.strip().replace("\\", "/").split("/")[-1].replace(".md", "")
    return slug_to_id.get(slug)


def build_graph(
    pages: list[dict[str, Any]], slug_to_id: dict[str, str], verbose: bool
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], Counter[str], int]:
    edges: list[dict[str, Any]] = []
    broken: list[dict[str, Any]] = []
    degree = Counter()
    seen: set[tuple[str, str, str]] = set()

    for page in pages:
        source = page["id"]
        for field in LINK_FIELDS:
            for raw_target in extract_link_targets(page["frontmatter"].get(field)):
                target = resolve_target(raw_target, slug_to_id)
                if not target:
                    broken.append({"source": source, "target_slug": raw_target, "kind": field})
                    if verbose:
                        print(f"[broken] {source} -> {raw_target} (kind={field})", file=sys.stderr)
                    continue
                if target == source:
                    continue
                key = (source, target, field)
                if key in seen:
                    continue
                seen.add(key)
                edges.append({"source": source, "target": target, "kind": field, "directed": True})
                degree[source] += 1
                degree[target] += 1

        for match in BODY_LINK_RE.finditer(page["body"]):
            raw_target = match.group(1)
            target = resolve_target(raw_target, slug_to_id)
            if not target:
                broken.append({"source": source, "target_slug": raw_target, "kind": "body"})
                if verbose:
                    print(f"[broken] {source} -> {raw_target} (kind=body)", file=sys.stderr)
                continue
            if target == source:
                continue
            key = (source, target, "body")
            if key in seen:
                continue
            seen.add(key)
            edges.append({"source": source, "target": target, "kind": "body", "directed": False})
            degree[source] += 1
            degree[target] += 1

    orphan_count = 0
    for page in pages:
        if degree[page["id"]] == 0:
            orphan_count += 1
            if verbose:
                print(f"[orphan] {page['id']} ({page['path']})", file=sys.stderr)

    return edges, broken, degree, orphan_count


def main() -> None:
    args = parse_args()
    pages, slug_to_id = collect_pages(Path(args.wiki_dir))
    edges, broken, degree, orphan_count = build_graph(pages, slug_to_id, args.verbose)

    broken_ratio = (len(broken) / len(edges)) if edges else 0.0
    if broken_ratio > 0.10:
        raise SystemExit("broken_links exceed 10% of edges; inspect extraction logic")

    nodes = [{
        "id": page["id"],
        "type": page["type"],
        "title": page["title"],
        "title_ko": page["title_ko"],
        "aliases": page["aliases"],
        "summary": page["summary"],
        "source_count": page["source_count"],
        "created": page["created"],
        "updated": page["updated"],
        "degree": degree.get(page["id"], 0),
        "path": page["path"],
        "meta": jsonable(page["meta"]),
    } for page in pages]

    payload = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "root": None,
        "stats": {
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "broken_links": len(broken),
            "orphans": orphan_count,
            "by_type": dict(sorted(Counter(page["type"] for page in pages).items())),
        },
        "nodes": nodes,
        "edges": edges,
        "broken_links": broken,
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    size_kb = max(1, round(out_path.stat().st_size / 1024))

    print("cosmos/extract.py")
    print(f"  scanned: {len(pages)} files")
    print(f"  nodes:   {len(nodes)}")
    print(f"  edges:   {len(edges)}")
    print(f"  orphans: {orphan_count} (see stderr)")
    print(f"  broken:  {len(broken)} (see stderr)")
    print(f"  output:  {out_path.as_posix()} ({size_kb} KB)")


if __name__ == "__main__":
    main()
