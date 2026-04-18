from __future__ import annotations

import argparse
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"
ORGS_DIR = ROOT / "wiki" / "organizations"


def wikilink_slug(value: object) -> str:
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        return text[2:-2].split("|", 1)[0].strip()
    return text


def wikilink(slug: str) -> str:
    return f"[[{slug}]]"


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        text = str(item or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        output.append(text)
    return output


def operation_org_slugs(meta: dict) -> list[str]:
    values: list[str] = []
    for key in ("lead_agency", "coordinating_body"):
        slug = wikilink_slug(meta.get(key))
        if slug:
            values.append(slug)
    for key in ("participating_agencies", "organizations"):
        for value in meta.get(key) or []:
            slug = wikilink_slug(value)
            if slug:
                values.append(slug)
    return unique(values)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--org", help="Restrict to a single organization slug")
    args = parser.parse_args()

    org_to_ops: dict[str, list[str]] = {}
    for op_path in sorted(OPS_DIR.glob("*.md")):
        if op_path.name.startswith("_"):
            continue
        meta = frontmatter.load(op_path).metadata
        for org_slug in operation_org_slugs(meta):
            if args.org and org_slug != args.org:
                continue
            org_to_ops.setdefault(org_slug, []).append(wikilink(op_path.stem))

    changed = 0
    for org_slug, op_links in org_to_ops.items():
        org_path = ORGS_DIR / f"{org_slug}.md"
        if not org_path.exists():
            continue
        post = frontmatter.load(org_path)
        meta = post.metadata
        current = [str(v) for v in (meta.get("operations_participated") or [])]
        merged = unique(current + sorted(op_links))
        if merged == current:
            continue
        meta["operations_participated"] = merged
        org_path.write_text(frontmatter.dumps(post), encoding="utf-8")
        changed += 1

    print(f"Updated {changed} organization pages.")


if __name__ == "__main__":
    main()
