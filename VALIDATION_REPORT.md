# VALIDATION_REPORT｜sales_os clean v5

## 判定

OK: sales_os validation passed

## v5で追加された検証

- ルート直下の許可リスト完全一致チェック
- `PUSH_CLEAN_WINDOWS.bat` / `push_clean.sh` は `tools/` 配下
- `PUSH_GUIDE.md` は `docs/` 配下
- `DRIVE_REFERENCES.md` と各client 6.1のDrive ID・file/folder種別の完全照合
- Drive ID重複チェック
- 28社以外の余剰clientカルテ検出
- `### 6.1 代表Drive参照` 見出しの存在チェック
- 危険拡張子スキャン
- 日本語ファイル名・半角スペース・括弧付きファイル名チェック
- 主要カルテの会社名一致チェック

## 監査で指摘された軽微問題への対応

| 指摘 | 対応 |
|---|---|
| `PUSH_CLEAN_WINDOWS.bat` がルート直下 | `tools/` へ移動 |
| `push_clean.sh` がルート直下 | `tools/` へ移動 |
| `PUSH_GUIDE.md` がルート直下 | `docs/` へ移動 |
| validateの監査範囲不足 | v5で強化 |

## GPTプロジェクト削除可否

v5をGitHubへ反映し、`python tools/validate_sales_os.py` がOKなら削除可能。
