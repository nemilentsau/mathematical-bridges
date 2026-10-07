# Adding a paper or updating a review

[Home](README.md)

1. Choose a stable lowercase, hyphenated ID.
2. Copy [templates/review.md](templates/review.md) to `reviews/<id>.md` and [templates/bridge.md](templates/bridge.md) to `bridges/<id>.md`.
3. Record the source URL, revision when available, reading scope, provenance, and proof-validation status. Do not fill unknown dates or conclusions by inference.
4. Keep the review and bridge separate. The review supports the assessment; the bridge should be readable in under a minute.
5. Update both indexes, `catalog.json`, and the reading queue. If downloading a new source, add its identity and SHA-256 to `sources/manifest.json` without committing the PDF.
6. Add a dated entry to `CHANGELOG.md`. Run `python3 tools/check_repo.py`, inspect the diff, and commit.

A queue hypothesis becomes a confirmed description only after reading the relevant construction. If the title led us to the wrong expectation, preserve that correction explicitly.
