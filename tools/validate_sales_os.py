#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

# 1. no non-ascii paths
for p in ROOT.rglob('*'):
    rel = p.relative_to(ROOT).as_posix()
    try:
        rel.encode('ascii')
    except UnicodeEncodeError:
        errors.append(f'NON_ASCII_PATH: {rel}')

# 2. no loose client-like files at root
for p in ROOT.glob('*.md'):
    name = p.name
    if name[:2].isdigit() and name[2] == '_':
        errors.append(f'LOOSE_CLIENT_FILE_AT_ROOT: {name}')
    if name.endswith('_update_candidate.md'):
        errors.append(f'LOOSE_UPDATE_CANDIDATE_AT_ROOT: {name}')

# 3. expected title mapping
expected = {
    'clients/18_wse.md': '# 案件カルテ｜ワールドシステムエンジニアリング有限会社（WSE）',
    'clients/19_reegle.md': '# 案件カルテ｜Reegle株式会社',
    'clients/20_food_surprise.md': '# 案件カルテ｜株式会社フードサプライズ',
    'clients/21_ast.md': '# 案件カルテ｜株式会社アスト',
    'clients/25_hanayuki.md': '# 案件カルテ｜株式会社花雪',
}
for rel, title in expected.items():
    p = ROOT / rel
    if not p.exists():
        errors.append(f'MISSING: {rel}')
        continue
    first = p.read_text(encoding='utf-8').splitlines()[0].strip()
    if first != title:
        errors.append(f'TITLE_MISMATCH: {rel}: expected {title!r}, got {first!r}')

if errors:
    print('VALIDATION FAILED')
    for e in errors:
        print('-', e)
    sys.exit(1)

print('VALIDATION OK')
print('All paths are ASCII, client files are under clients/, and key title mappings are correct.')
