# Cosmos of IC

`Cosmos of IC` is a static 3D knowledge graph for the Cyber Crime IC wiki. It turns `wiki/**/*.md` into nodes and edges so you can browse international-cooperation structure spatially instead of reading pages one by one.

## What is this

This is a GitHub Pages subsite under `/cosmos/`. It reads compiled wiki pages, extracts structured graph data into `data.json`, and renders a Three.js view with search, filters, path finding, and node detail panels.

## Live site

`https://<user>.github.io/<repo>/cosmos/`

## Local development

```bash
pip install -r cosmos/requirements.txt
python cosmos/extract.py
python -m http.server -d cosmos 8000
# open http://localhost:8000
```

## How it works

1. `wiki/**/*.md` is the source graph.
2. `cosmos/extract.py` parses frontmatter and body wikilinks into `cosmos/data.json`.
3. `cosmos/index.html` loads `data.json` and renders the 3D scene.

## Data freshness

GitHub Actions rebuilds `cosmos/data.json` whenever `wiki/**` or `cosmos/**` changes and republishes the Pages artifact with `/cosmos/` included.

## Enabling Pages

1. Open repository `Settings`.
2. Go to `Pages`.
3. Set `Source` to `GitHub Actions`.
4. Push a change under `wiki/**`, `cosmos/**`, or the workflow file.

## Known limitations

- The initial render only shows the root node plus its 1-hop neighborhood.
- Larger expansions can still become visually dense.
- The local markdown button opens the GitHub blob URL on Pages and `../wiki/...` in local fallback mode.
- Mobile works, but the side panels are more comfortable on desktop.

## License / attribution

See the repository root `LICENSE`. Three.js is loaded from a CDN, and typography uses Pretendard, Fraunces, JetBrains Mono, and Noto Serif KR.
