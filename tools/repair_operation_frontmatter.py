from __future__ import annotations

import tempfile
from pathlib import Path

import frontmatter


ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "wiki" / "operations"


def load_from_text(text: str):
    with tempfile.NamedTemporaryFile("w+", suffix=".md", encoding="utf-8", delete=False) as handle:
        temp_path = Path(handle.name)
        handle.write(text)
    try:
        return frontmatter.load(temp_path)
    finally:
        temp_path.unlink(missing_ok=True)


def main() -> None:
    repaired = 0

    for path in sorted(OPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue

        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) < 8 or lines[0] != "---":
            continue

        try:
            closing_idx = lines.index("---", 1)
        except ValueError:
            continue

        injected = frontmatter.load(path).metadata
        probe = "\n".join(lines[closing_idx + 1: closing_idx + 20])
        if "type: operation" not in probe:
            continue

        cleaned_lines = lines[closing_idx + 1:]
        while cleaned_lines and not cleaned_lines[0].strip():
            cleaned_lines.pop(0)
        if not cleaned_lines:
            continue

        if cleaned_lines[0].startswith("癤") or cleaned_lines[0].startswith("ï»¿"):
            cleaned_lines[0] = "---"
        elif cleaned_lines[0] != "---":
            cleaned_lines.insert(0, "---")

        cleaned_text = "\n".join(cleaned_lines) + "\n"
        post = load_from_text(cleaned_text)
        meta = post.metadata

        for key, value in injected.items():
            meta[key] = value

        path.write_text(frontmatter.dumps(post), encoding="utf-8")
        repaired += 1

    print(f"Repaired {repaired} operation pages.")


if __name__ == "__main__":
    main()
