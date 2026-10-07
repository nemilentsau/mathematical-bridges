"""Validate this notebook's catalog, local navigation, and source records."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

root = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((root / 'catalog.json').read_text())
papers = catalog['papers']
ids = [p['id'] for p in papers]
if len(ids) != len(set(ids)):
    errors.append('Duplicate catalog IDs')
reviewed = [p for p in papers if p['status'] == 'reviewed']
queued = [p for p in papers if p['status'] == 'queued']
manifest = json.loads((root / 'sources/manifest.json').read_text())
sources = {s['id']: s for s in manifest['papers']}
for p in reviewed:
    for key in ['review', 'bridge']:
        if not (root / p[key]).is_file():
            errors.append(f"Missing {key}: {p['id']}")
    if p['id'] not in sources:
        errors.append(f"Missing source: {p['id']}")
    elif not re.fullmatch(r'[0-9a-f]{64}', sources[p['id']]['sha256']):
        errors.append(f"Invalid SHA-256: {p['id']}")
for p in queued:
    if p.get('selection_basis') != 'title-only':
        errors.append(f"Queue basis missing: {p['id']}")
for md in root.rglob('*.md'):
    if '.git' in md.parts or 'templates' in md.parts:
        continue
    for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', md.read_text()):
        if '://' in link or link.startswith('#') or link.startswith('mailto:'):
            continue
        target = unquote(link.split('#', 1)[0])
        if target and not (md.parent / target).exists():
            errors.append(f"Broken local link in {md.relative_to(root)}: {link}")
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(reviewed)} reviews, {len(reviewed)} bridge cards, {len(queued)} queued papers; catalog, sources, and local links valid.')
