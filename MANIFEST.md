# MANIFEST｜sales_os clean package v2

このパッケージは、GitHub 正本化用に整理した営業OSです。

## 方針
- ファイル名・フォルダ名はASCIIのみ
- 本文は日本語UTF-8
- 案件カルテはすべて `clients/` 配下
- ルート直下に案件別カルテを置かない
- Google Driveは原本置き場、GitHubは営業OSの正本

## ルート直下に置くもの
- README.md
- INDEX.md
- CLAUDE.md
- _research_protocol.md
- _analysis_protocol.md
- SECURITY.md
- FILENAME_POLICY.md
- filename_mapping.md
- MANIFEST.md
- CHECK_BEFORE_DELETE.md
- UPLOAD_INSTRUCTIONS.md
- CLEANUP_OLD_UPLOAD.md
- clients/
- docs/
- patterns/
- prompts/
- outputs/
- tools/

## 絶対にルート直下へ散らさないもの
- `01_*.md` 〜 `28_*.md` の案件カルテ
- `*_update_candidate.md`
- pattern系テンプレート
- prompt系テンプレート

これらは必ず該当フォルダ配下に置く。
