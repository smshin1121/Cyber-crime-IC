# Routes

- `GET` `/` [auth, db, cache]
- `GET` `/wiki/<slug>` params(slug) [auth, db, cache]
- `GET` `/wiki/<category>/<slug>` params(category, slug) [auth, db, cache]
- `GET` `/wiki/_missing/<slug>` params(slug) [auth, db, cache]
- `GET` `/category/<category>` params(category) [auth, db, cache]
- `GET` `/search` [auth, db, cache]
- `GET` `/stats` [auth, db, cache]
