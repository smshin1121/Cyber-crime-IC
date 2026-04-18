from __future__ import annotations

import argparse
import re

from doj_fetch import DOJClient


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="https://www.justice.gov/news/press-releases")
    args = parser.parse_args()

    client = DOJClient()
    if args.url != "https://www.justice.gov/news/press-releases":
        client.fetch("https://www.justice.gov/news/press-releases")
    html = client.fetch(args.url)
    print("length", len(html))

    for match in re.finditer(r'href="([^"]+)"', html):
        href = match.group(1)
        if "press-releases" in href or "/pr/" in href or "?page=" in href or "facet_topics" in href:
            print(href)


if __name__ == "__main__":
    main()
