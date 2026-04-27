"""
Static site generator for GitHub Pages.
Converts the Flask wiki app into static HTML files.
"""
import os
import sys
import shutil
from pathlib import Path

# Add parent and tools to path
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from app import (
    app,
    WIKI_DIR,
    CATEGORIES,
    get_all_pages,
    parse_page,
    get_category_for_file,
)
from operation_scope import operation_scope

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "docs"
COSMOS_DIR = Path(__file__).resolve().parent.parent / "cosmos"


def build() -> None:
    """Generate static HTML site in docs/ directory."""
    # Rebuild category indexes from the wiki tree before any derived outputs.
    try:
        from reconcile_indexes import main as reconcile_main
        print("Reconciling indexes...")
        reconcile_main()
    except Exception as e:
        print(f"  Warning: index reconcile skipped ({e})")

    # Sync statistics before building
    try:
        from sync_stats import main as sync_main
        print("Syncing statistics...")
        sync_main()
    except Exception as e:
        print(f"  Warning: stats sync skipped ({e})")

    # Clean output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Copy static assets
    static_src = Path(__file__).parent / "static"
    static_dst = OUTPUT_DIR / "static"
    shutil.copytree(static_src, static_dst)

    if COSMOS_DIR.exists():
        try:
            import subprocess
            extract_script = COSMOS_DIR / "extract.py"
            if extract_script.exists():
                print("Building cosmos graph...")
                subprocess.run([sys.executable, str(extract_script)], check=True)
            cosmos_dst = OUTPUT_DIR / "cosmos"
            if cosmos_dst.exists():
                shutil.rmtree(cosmos_dst)
            shutil.copytree(COSMOS_DIR, cosmos_dst)
        except Exception as e:
            print(f"  Warning: cosmos build skipped ({e})")

    routes_built = 0

    with app.test_client() as client:
        # Home redirect -> build index directly
        _save(client, "/wiki/index", "index.html")
        routes_built += 1

        # Stats page
        _save(client, "/stats", "stats.html")
        routes_built += 1

        # Search page (empty)
        _save(client, "/search", "search.html")
        routes_built += 1

        # Category pages
        for cat in CATEGORIES:
            cat_dir = WIKI_DIR / cat
            if cat_dir.is_dir():
                _save(client, f"/category/{cat}", f"category/{cat}.html")
                routes_built += 1

                # Individual pages in category
                for md_file in cat_dir.glob("*.md"):
                    if md_file.name.startswith("_"):
                        continue
                    slug = md_file.stem
                    _save(
                        client,
                        f"/wiki/{cat}/{slug}",
                        f"wiki/{cat}/{slug}.html",
                    )
                    routes_built += 1

        # Top-level wiki pages (index, overview, log)
        for md_file in WIKI_DIR.glob("*.md"):
            slug = md_file.stem
            if slug.startswith("_"):
                continue
            _save(client, f"/wiki/{slug}", f"wiki/{slug}.html")
            routes_built += 1

    # Build client-side search index consumed by search.html
    print("Building search index...")
    import json
    search_index = []
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        try:
            meta, content = parse_page(md_file)
        except Exception:
            continue
        cat = get_category_for_file(md_file) or ""
        op_scope = operation_scope(meta) if cat == "operations" or meta.get("type") == "operation" else ""
        search_index.append({
            "slug": md_file.stem,
            "category": cat,
            "title": str(meta.get("title") or md_file.stem),
            "title_ko": str(meta.get("title_ko") or meta.get("official_name_ko") or ""),
            "type": str(meta.get("type") or ""),
            "status": str(meta.get("status") or ""),
            "operation_scope": op_scope,
            "text": str(content or "")[:4000],
        })
    (OUTPUT_DIR / "search-index.json").write_text(
        json.dumps(search_index, ensure_ascii=False),
        encoding="utf-8",
    )

    # Create redirect index.html at root
    root_index = OUTPUT_DIR / "index.html"
    root_index.write_text(
        '<!DOCTYPE html><html><head>'
        '<meta http-equiv="refresh" content="0;url=wiki/index.html">'
        '</head><body></body></html>',
        encoding="utf-8",
    )

    # Create generic 404 page for GitHub Pages (use _save for consistent links)
    with app.test_client() as client:
        _save(client, "/wiki/_missing/placeholder", "404.html")

    # Create .nojekyll for GitHub Pages
    (OUTPUT_DIR / ".nojekyll").touch()

    print(f"Built {routes_built} pages to {OUTPUT_DIR}")


def _save(client, route: str, filepath: str) -> None:
    """Fetch a route and save the HTML."""
    import re

    resp = client.get(route)
    if resp.status_code in (200, 404):
        out_path = OUTPUT_DIR / filepath
        out_path.parent.mkdir(parents=True, exist_ok=True)
        html = resp.data.decode("utf-8")

        depth = filepath.count("/")
        prefix = "../" * depth

        # Step 1: Add .html extension WHILE links are still absolute
        html = re.sub(r'href="/wiki/([^"#]+?)"', r'href="/wiki/\1.html"', html)
        html = re.sub(r'href="/category/([^"#]+?)"', r'href="/category/\1.html"', html)
        html = re.sub(r'href="/stats"', r'href="/stats.html"', html)
        html = re.sub(r'href="/search"', r'href="/search.html"', html)
        html = re.sub(r'action="/search"', r'action="/search.html"', html)

        # Step 1.5: keep root links usable after absolute-to-relative conversion
        home_href = f'{prefix}index.html' if prefix else 'index.html'
        html = html.replace('href="/"', f'href="{home_href}"')

        # Step 2: Convert absolute paths to relative
        html = html.replace('href="/', f'href="{prefix}')
        html = html.replace('action="/', f'action="{prefix}')
        html = html.replace('src="/', f'src="{prefix}')

        # Step 3: Fix double .html.html if any
        html = html.replace('.html.html"', '.html"')

        out_path.write_text(html, encoding="utf-8")
    else:
        print(f"  SKIP {route} (status {resp.status_code})")


if __name__ == "__main__":
    build()
