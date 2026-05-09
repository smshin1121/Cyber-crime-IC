from pathlib import Path
import frontmatter
ROOT = Path(r"C:\Users\forenshin\Desktop\Cyber-crime-IC")

OP = "[[seoul-eastern-clark-philippines-voice-phishing-arrest-extradition-2026]]"
SRC = "[[2026-04-30_spo-go-kr_seoul-eastern-clark-philippines-voice-phishing-arrest-extradition]]"

EDITS = [
    ("wiki/countries/south-korea.md", "operations_participated", OP),
    ("wiki/countries/philippines.md", "operations_participated", OP),
    ("wiki/organizations/supreme-prosecutors-office-korea.md", "operations_participated", OP),
    ("wiki/organizations/ministry-of-justice-korea.md", "operations_participated", OP),
    ("wiki/organizations/philippine-national-police.md", "operations_participated", OP),
    ("wiki/organizations/interpol.md", "operations_participated", OP),
    ("wiki/crime-types/voice-phishing-ic.md", "notable_operations", OP),
    ("wiki/crime-types/voice-phishing-ic.md", "sources", SRC),
    ("wiki/crime-types/online-fraud-ic.md", "notable_operations", OP),
    ("wiki/crime-types/online-fraud-ic.md", "sources", SRC),
    ("wiki/crime-types/organized-crime-ic.md", "notable_operations", OP),
    ("wiki/crime-types/organized-crime-ic.md", "sources", SRC),
    ("wiki/mechanisms/extradition.md", "operations_using", OP),
    ("wiki/operations/korea-cambodia-philippines-73-extradition-2026.md", "related_operations", OP),
]

changed = 0
for path, field, link in EDITS:
    fp = ROOT / path
    if not fp.exists():
        print(f"SKIP MISSING: {path}")
        continue
    post = frontmatter.load(fp)
    cur = post.metadata.get(field) or []
    if isinstance(cur, str):
        cur = [cur]
    if link in cur:
        print(f"already: {path}/{field}")
        continue
    cur.append(link)
    post.metadata[field] = cur
    if field == "sources":
        post.metadata["source_count"] = int(post.metadata.get("source_count", 0)) + 1
    fp.write_text(frontmatter.dumps(post), encoding="utf-8")
    changed += 1
    print(f"OK: {path}/{field}")
print(f"\nChanged: {changed}/{len(EDITS)}")
