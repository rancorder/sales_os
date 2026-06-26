# CLEANUP_OLD_UPLOAD｜旧アップロード整理

旧アップロードでルート直下に案件カルテやテンプレが散った場合は、v5を正本としてforce pushする。

## 旧状態でありがちなNG

- ルート直下に `01_firstfan_ageru_care.md`
- ルート直下に `21_ast.md`
- ルート直下に `call_kpi_analysis_format.md`
- ルート直下に `download`
- ルート直下に `download (1)`
- ルート直下に `PUSH_CLEAN_WINDOWS.bat`
- ルート直下に `push_clean.sh`
- ルート直下に `PUSH_GUIDE.md`

## v5の正しい配置

- 案件カルテ：`clients/`
- 横断テンプレ：`patterns/`
- AI依頼文：`prompts/`
- 運用ドキュメント：`docs/`
- スクリプト：`tools/`

## 対処

v5を展開し、以下で反映。

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
