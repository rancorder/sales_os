from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

ALLOWED_ROOT_FILES = {
    ".gitattributes",
    ".gitignore",
    "README.md",
    "INDEX.md",
    "CLAUDE.md",
    "MANIFEST.md",
    "SECURITY.md",
    "FILENAME_POLICY.md",
    "DRIVE_REFERENCES.md",
    "DRIVE_ID_EXPANSION_POLICY.md",
    "CHECK_BEFORE_DELETE.md",
    "CLEANUP_OLD_UPLOAD.md",
    "UPLOAD_INSTRUCTIONS.md",
    "VALIDATION_REPORT.md",
    "_research_protocol.md",
    "_analysis_protocol.md",
    "filename_mapping.md",
}

ALLOWED_ROOT_DIRS = {
    "clients",
    "docs",
    "patterns",
    "prompts",
    "outputs",
    "tools",
    ".github",
    ".git",
}

EXPECTED = {
    "clients/01_firstfan_ageru_care.md": ("FirstFan", "file", "1F80wHcgB7cg7fbD2S_N1dQHl12CxzkQ9"),
    "clients/02_at_design.md": ("株式会社ATデザイン", "file", "1rgFiTnhxnH_6U3YWk0W8dOj1JzzT5pUd"),
    "clients/03_jct.md": ("有限会社ジェイシーティー", "file", "1ZNiZLI0YSQRw0yH02TdmM8X498G6X6Za"),
    "clients/studio_tram/client_card.md": ("STUDIO TRAM", "folder", "1JmnQokba1zp7RHBpilgwdBjuFI93bbaq"),
    "clients/05_kyoei_data_center.md": ("株式会社共栄データセンター", "file", "1NKnTuwL7h05-C469idOSXxPkwsWQQBNz"),
    "clients/06_hiwell.md": ("株式会社ハイウェル", "file", "1ZnGPCrhR1gCzaRG8BIoDWC9NekhzDY_U"),
    "clients/07_aidec_management.md": ("エイデックマネジメント", "file", "1nKqe_OXcItaQ2zRlGWXrd4BtoXNQwtDL"),
    "clients/08_t2_laboratory.md": ("株式会社ティーツー・ラボラトリ", "file", "1HQIjqlkqc77UiihNe5JEbnSKh6ciyiAu"),
    "clients/09_laura_office.md": ("ラウラオフィス", "file", "1nlD7ufeSaHbMEn6x6TLi_lFowWLjVgzR"),
    "clients/10_aile.md": ("株式会社AILE", "file", "1X5G6Uddy76F9wWFtyCWmzraxV1zmSRAF"),
    "clients/11_sozo_gijutsu_sozo.md": ("想像技術創造株式会社", "file", "1r-wc4p9g0nWU9ZvKfqVYlzRnu_Cbad-0"),
    "clients/12_hito_film.md": ("HITO Film株式会社", "file", "1a2MqZEKD8Cx6BWizXSM5wjkXG42pErx_"),
    "clients/13_asahien.md": ("有限会社旭園", "file", "1u0NLZ1suDpslqzuDI2donXy0bAsT6II6"),
    "clients/14_aim_rose.md": ("株式会社aim-rose", "file", "1-3hzXOOTvzf1fZgV5-L0JqIpDL-PTKtj"),
    "clients/15_sanko.md": ("参鋼株式会社", "file", "1kgb3i0uxWP-L07D4fX4dovRWOd0ehIiV"),
    "clients/16_kotonoha_marketing.md": ("株式会社kotonohaマーケティング", "file", "1StPvsJg1i-kQGz0bs0I95daclUmOWhfq"),
    "clients/17_sm_tech.md": ("株式会社SM TECH", "file", "12oaxt5YTvEdylTYpx3CklT64tTJy3Sk0"),
    "clients/18_wse.md": ("ワールドシステムエンジニアリング", "file", "1KPhRO5dWQBp3QWcVUlDzAVOF3xw-Irgf"),
    "clients/19_reegle.md": ("Reegle株式会社", "file", "1tHXnyxomP7hG9fZde5dnx0lcthFF-FVR"),
    "clients/20_food_surprise.md": ("株式会社フードサプライズ", "file", "1Zcq0PR1ATTCCoJ8bfn1T4bMc8-MtfIlB"),
    "clients/21_ast.md": ("株式会社アスト", "file", "15ez44jIAClPxXA3KjJ0_HlPLsqnyYpIC"),
    "clients/22_kansha.md": ("株式会社KANSHA", "file", "1S2yfMFEeNe5vkw03O8V5gLgLJAjs2q4O"),
    "clients/23_nihon_shin_kikaku.md": ("合同会社日本真企画", "file", "18Mc-KwsIcBLfo7IRyK45JFoaZKu-JO7Q"),
    "clients/24_ikko_industry.md": ("有限会社一光工業", "file", "1ukcJTDGpF2azdgaquHo-UAxANRjnVKQZ"),
    "clients/25_hanayuki.md": ("株式会社花雪", "file", "192hX_NXmiwZQlOvCIBu1d6QUTrqAjyfl"),
    "clients/26_vista.md": ("株式会社ビスタ", "file", "1HHb1CXwp-Hzl6eqOQ5pCZ3hnnYNR-hcQ"),
    "clients/27_generate_one.md": ("株式会社ジェネレートワン", "file", "1I14IWTzVAKAkYfPN2f_0hYXkNNaNmETY"),
    "clients/28_inet_technologies.md": ("株式会社アイネットテクノロジーズ", "file", "1kSRsr-Ttd5gqHqSxjzgtzhU30ae1TQQw"),
}

REQUIRED_DRIVE_TABLE_HEADER = "| 種別 | 資料名 | Drive参照種別 | Drive ID / URL | 用途 | 更新日 | 状態 |"
DANGEROUS_EXTENSIONS = {".csv", ".mp4", ".webm", ".vtt", ".xlsx", ".xls", ".docx", ".pdf"}
BAD_FILENAME_PATTERNS = [
    re.compile(r"\s"),
    re.compile(r"\("),
    re.compile(r"\)"),
]
WARN_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

errors = []
warnings = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


# 1. Strict root allow list
for item in ROOT.iterdir():
    name = item.name
    if item.is_dir():
        if name not in ALLOWED_ROOT_DIRS:
            errors.append(f"root disallowed directory: {name}")
    else:
        if name not in ALLOWED_ROOT_FILES:
            errors.append(f"root disallowed file: {name}")

# 2. Path safety
for p in ROOT.rglob("*"):
    if ".git" in p.parts:
        continue
    r = rel(p)
    try:
        r.encode("ascii")
    except UnicodeEncodeError:
        errors.append(f"non-ascii path: {r}")
    name = p.name
    for pat in BAD_FILENAME_PATTERNS:
        if pat.search(name):
            errors.append(f"bad filename pattern: {r}")
            break

# 3. No client cards in root
for p in ROOT.glob("[0-9][0-9]_*.md"):
    errors.append(f"root client card leak: {p.name}")

# 4. Dangerous raw source extensions should not be in GitHub
for p in ROOT.rglob("*"):
    if ".git" in p.parts or not p.is_file():
        continue
    if p.suffix.lower() in DANGEROUS_EXTENSIONS:
        errors.append(f"dangerous raw-source file extension: {rel(p)}")

# 5. Expected client cards
expected_paths = set(EXPECTED.keys())
actual_existing_card_paths = {path for path in expected_paths if (ROOT / path).exists()}
if actual_existing_card_paths != expected_paths:
    missing = sorted(expected_paths - actual_existing_card_paths)
    for m in missing:
        errors.append(f"missing client card: {m}")

# Numeric client-card-like files under clients must be in EXPECTED.
for p in (ROOT / "clients").rglob("*.md"):
    r = rel(p)
    if re.search(r"(^|/)[0-9]{2}_[a-z0-9_]+\.md$", r) and r not in expected_paths:
        errors.append(f"unexpected numeric client-card-like file: {r}")

for path, (title_token, drive_kind, drive_id) in EXPECTED.items():
    p = ROOT / path
    if not p.exists():
        continue
    txt = p.read_text(encoding="utf-8")
    if title_token not in txt:
        errors.append(f"title mismatch: {path} expected token {title_token}")
    if "### 6.1 代表Drive参照" not in txt:
        errors.append(f"missing 6.1 section: {path}")
    if "### 6.2 追加資料ID一覧" not in txt:
        errors.append(f"missing 6.2 section: {path}")
    if REQUIRED_DRIVE_TABLE_HEADER not in txt:
        errors.append(f"missing v4/v5 drive table header: {path}")
    if "| 資料 | fileId |" in txt:
        errors.append(f"old 2-column fileId table remains: {path}")
    if f"| Drive参照種別 | {drive_kind} |" not in txt:
        errors.append(f"drive kind mismatch in client: {path} expected {drive_kind}")
    if f"| Drive参照ID | `{drive_id}` |" not in txt:
        errors.append(f"drive id mismatch/missing in client: {path} expected {drive_id}")

    # Soft warning for email-like strings. Do not fail because official company contact can be valid.
    for match in WARN_EMAIL_RE.findall(txt):
        warnings.append(f"email-like string found in {path}: {match}")

# 6. DRIVE_REFERENCES full consistency
dr = ROOT / "DRIVE_REFERENCES.md"
if not dr.exists():
    errors.append("missing: DRIVE_REFERENCES.md")
else:
    dr_txt = dr.read_text(encoding="utf-8")
    rows = {}
    for line in dr_txt.splitlines():
        if not line.startswith("| "):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 6 or not parts[0].isdigit():
            continue
        idx, client_file, client_name, kind, drive_id, url = parts[:6]
        client_file = client_file.strip("`")
        drive_id = drive_id.strip("`")
        rows[client_file] = {"idx": int(idx), "name": client_name, "kind": kind, "drive_id": drive_id, "url": url}
    if len(rows) != 28:
        errors.append(f"DRIVE_REFERENCES row count mismatch: expected 28 got {len(rows)}")
    if set(rows.keys()) != expected_paths:
        missing = sorted(expected_paths - set(rows.keys()))
        extra = sorted(set(rows.keys()) - expected_paths)
        for m in missing:
            errors.append(f"DRIVE_REFERENCES missing client path: {m}")
        for e in extra:
            errors.append(f"DRIVE_REFERENCES extra client path: {e}")
    seen_ids = {}
    for path, (title_token, expected_kind, expected_drive_id) in EXPECTED.items():
        row = rows.get(path)
        if not row:
            continue
        if row["kind"] != expected_kind:
            errors.append(f"DRIVE_REFERENCES kind mismatch: {path} expected {expected_kind} got {row['kind']}")
        if row["drive_id"] != expected_drive_id:
            errors.append(f"DRIVE_REFERENCES ID mismatch: {path} expected {expected_drive_id} got {row['drive_id']}")
        if expected_kind == "folder" and "/drive/folders/" not in row["url"]:
            errors.append(f"DRIVE_REFERENCES URL kind mismatch for folder: {path}")
        if expected_kind == "file" and "/file/d/" not in row["url"]:
            errors.append(f"DRIVE_REFERENCES URL kind mismatch for file: {path}")
        if row["drive_id"] in seen_ids:
            errors.append(f"duplicate Drive ID: {row['drive_id']} in {seen_ids[row['drive_id']]} and {path}")
        seen_ids[row["drive_id"]] = path

# 7. Required policy files
for required in [
    "DRIVE_ID_EXPANSION_POLICY.md",
    "FILENAME_POLICY.md",
    "SECURITY.md",
    "CHECK_BEFORE_DELETE.md",
    "CLEANUP_OLD_UPLOAD.md",
]:
    if not (ROOT / required).exists():
        errors.append(f"missing policy file: {required}")

if warnings:
    print("WARNINGS:")
    for w in sorted(set(warnings)):
        print("-", w)
    print()

if errors:
    print("NG: sales_os validation failed")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("OK: sales_os validation passed")
print(f"client cards checked: {len(EXPECTED)}")
print("root allow-list: strict")
print("drive reference consistency: strict")
print("drive expansion table: v5")
if warnings:
    print(f"warnings: {len(set(warnings))} non-blocking")
