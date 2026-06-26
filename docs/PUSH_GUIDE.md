# PUSH_GUIDE｜GitHub反映手順

このリポジトリは `rancorder/sales_os` の正本として運用する。

## 推奨：検証してからpush

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

## Windows

ルート直下ではなく、以下を実行する。

```bat
tools\PUSH_CLEAN_WINDOWS.bat
```

## macOS / Linux

```bash
bash tools/push_clean.sh
```

## 注意

- ルート直下に案件カルテを置かない。
- `clients/` 配下に28社分のカルテを置く。
- Drive原本はGitHubに置かない。
- 追加資料IDは各社カルテの6.2へ追記する。
