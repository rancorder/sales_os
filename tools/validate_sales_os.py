from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]

expected = {
    "clients/01_firstfan_ageru_care.md": ("FirstFan", "1F80wHcgB7cg7fbD2S_N1dQHl12CxzkQ9"),
    "clients/02_at_design.md": ("株式会社ATデザイン", "1rgFiTnhxnH_6U3YWk0W8dOj1JzzT5pUd"),
    "clients/03_jct.md": ("有限会社ジェイシーティー", "1ZNiZLI0YSQRw0yH02TdmM8X498G6X6Za"),
    "clients/studio_tram/client_card.md": ("STUDIO TRAM", "1JmnQokba1zp7RHBpilgwdBjuFI93bbaq"),
    "clients/05_kyoei_data_center.md": ("株式会社共栄データセンター", "1NKnTuwL7h05-C469idOSXxPkwsWQQBNz"),
    "clients/06_hiwell.md": ("株式会社ハイウェル", "1ZnGPCrhR1gCzaRG8BIoDWC9NekhzDY_U"),
    "clients/07_aidec_management.md": ("エイデックマネジメント", "1nKqe_OXcItaQ2zRlGWXrd4BtoXNQwtDL"),
    "clients/08_t2_laboratory.md": ("株式会社ティーツー・ラボラトリ", "1HQIjqlkqc77UiihNe5JEbnSKh6ciyiAu"),
    "clients/09_laura_office.md": ("ラウラオフィス", "1nlD7ufeSaHbMEn6x6TLi_lFowWLjVgzR"),
    "clients/10_aile.md": ("株式会社AILE", "1X5G6Uddy76F9wWFtyCWmzraxV1zmSRAF"),
    "clients/11_sozo_gijutsu_sozo.md": ("想像技術創造株式会社", "1r-wc4p9g0nWU9ZvKfqVYlzRnu_Cbad-0"),
    "clients/12_hito_film.md": ("HITO Film株式会社", "1a2MqZEKD8Cx6BWizXSM5wjkXG42pErx_"),
    "clients/13_asahien.md": ("有限会社旭園", "1u0NLZ1suDpslqzuDI2donXy0bAsT6II6"),
    "clients/14_aim_rose.md": ("株式会社aim-rose", "1-3hzXOOTvzf1fZgV5-L0JqIpDL-PTKtj"),
    "clients/15_sanko.md": ("参鋼株式会社", "1kgb3i0uxWP-L07D4fX4dovRWOd0ehIiV"),
    "clients/16_kotonoha_marketing.md": ("株式会社kotonohaマーケティング", "1StPvsJg1i-kQGz0bs0I95daclUmOWhfq"),
    "clients/17_sm_tech.md": ("株式会社SM TECH", "12oaxt5YTvEdylTYpx3CklT64tTJy3Sk0"),
    "clients/18_wse.md": ("ワールドシステムエンジニアリング", "1KPhRO5dWQBp3QWcVUlDzAVOF3xw-Irgf"),
    "clients/19_reegle.md": ("Reegle株式会社", "1tHXnyxomP7hG9fZde5dnx0lcthFF-FVR"),
    "clients/20_food_surprise.md": ("株式会社フードサプライズ", "1Zcq0PR1ATTCCoJ8bfn1T4bMc8-MtfIlB"),
    "clients/21_ast.md": ("株式会社アスト", "15ez44jIAClPxXA3KjJ0_HlPLsqnyYpIC"),
    "clients/22_kansha.md": ("株式会社KANSHA", "1S2yfMFEeNe5vkw03O8V5gLgLJAjs2q4O"),
    "clients/23_nihon_shin_kikaku.md": ("合同会社日本真企画", "18Mc-KwsIcBLfo7IRyK45JFoaZKu-JO7Q"),
    "clients/24_ikko_industry.md": ("有限会社一光工業", "1ukcJTDGpF2azdgaquHo-UAxANRjnVKQZ"),
    "clients/25_hanayuki.md": ("株式会社花雪", "192hX_NXmiwZQlOvCIBu1d6QUTrqAjyfl"),
    "clients/26_vista.md": ("株式会社ビスタ", "1HHb1CXwp-Hzl6eqOQ5pCZ3hnnYNR-hcQ"),
    "clients/27_generate_one.md": ("株式会社ジェネレートワン", "1I14IWTzVAKAkYfPN2f_0hYXkNNaNmETY"),
    "clients/28_inet_technologies.md": ("株式会社アイネットテクノロジーズ", "1kSRsr-Ttd5gqHqSxjzgtzhU30ae1TQQw"),
}

errors=[]
required_header="| 種別 | 資料名 | Drive参照種別 | Drive ID / URL | 用途 | 更新日 | 状態 |"

for p in ROOT.glob("[0-9][0-9]_*.md"):
    errors.append(f"rootに案件ファイルが散っています: {p.name}")

for p in ROOT.rglob("*"):
    try:
        str(p.relative_to(ROOT)).encode("ascii")
    except UnicodeEncodeError:
        errors.append(f"non-ascii path: {p.relative_to(ROOT)}")

for rel,(title,drive_id) in expected.items():
    p=ROOT/rel
    if not p.exists():
        errors.append(f"missing: {rel}")
        continue
    txt=p.read_text(encoding="utf-8")
    if title not in txt:
        errors.append(f"title mismatch: {rel} expected title token {title}")
    if drive_id not in txt:
        errors.append(f"drive id missing: {rel} expected {drive_id}")
    if "### 6.2 追加資料ID一覧" not in txt:
        errors.append(f"missing 6.2 section: {rel}")
    if required_header not in txt:
        errors.append(f"missing v4 drive table header: {rel}")
    if "| 資料 | fileId |" in txt:
        errors.append(f"old 2-column fileId table remains: {rel}")

dr=ROOT/"DRIVE_REFERENCES.md"
if not dr.exists():
    errors.append("missing: DRIVE_REFERENCES.md")
else:
    txt=dr.read_text(encoding="utf-8")
    if txt.count("https://drive.google.com/") < 28:
        errors.append("DRIVE_REFERENCES.md has fewer than 28 drive URLs")

policy=ROOT/"DRIVE_ID_EXPANSION_POLICY.md"
if not policy.exists():
    errors.append("missing: DRIVE_ID_EXPANSION_POLICY.md")

if errors:
    print("NG")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("OK: sales_os validation passed")
print(f"client cards checked: {len(expected)}")
print("drive expansion table: v4")
