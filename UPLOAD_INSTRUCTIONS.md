# UPLOAD_INSTRUCTIONS｜sales_os clean v5

## 方針

v5はCodex監査で指摘された軽微問題を修正した版。

- `PUSH_CLEAN_WINDOWS.bat` は `tools/` 配下へ移動
- `push_clean.sh` は `tools/` 配下へ移動
- `PUSH_GUIDE.md` は `docs/` 配下へ移動
- `tools/validate_sales_os.py` を強化
- ルート直下は許可リストで厳密管理

## GitHubへの反映

既存リポジトリに旧アップロードが残っている場合は、v5を正本としてforce pushする。

```bash
python tools/validate_sales_os.py
git init
git add -A
git commit -m "営業OS正本 v5: audit-ready clean structure"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
```

Windowsの場合：

```bat
tools\PUSH_CLEAN_WINDOWS.bat
```

## 反映後チェック

GitHub上で以下を確認する。

- ルート直下に `01_*.md` などの案件カルテがない
- `clients/21_ast.md` が株式会社アスト
- `clients/20_food_surprise.md` が株式会社フードサプライズ
- `DRIVE_REFERENCES.md` が28件
- `tools/validate_sales_os.py` がOK
