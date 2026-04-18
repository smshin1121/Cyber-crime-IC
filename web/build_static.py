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

from app import app, WIKI_DIR, CATEGORIES, get_all_pages

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "docs"


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
