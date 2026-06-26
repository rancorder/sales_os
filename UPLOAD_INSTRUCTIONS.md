# UPLOAD_INSTRUCTIONS｜v4反映手順

このv4は、Drive IDが増える前提の6章テーブルへ更新済み。

## 推奨：force pushで正本化
既存GitHubにルート直下の散らばりがある場合、Webアップロードで上書きせず、以下でクリーン反映する。

```bash
cd sales_os_clean_v4
git init
git add -A
git commit -m "営業OS正本 v4: Drive ID増加対応テーブルへ更新"
git branch -M main
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
```

Windowsの場合は `PUSH_CLEAN_WINDOWS.bat` を使う。

## 反映後の確認
```txt
clients/21_ast.md
→ # 案件カルテ｜株式会社アスト
→ 6.2に追加資料ID一覧テーブルあり

DRIVE_REFERENCES.md
→ 28件の代表Drive参照あり

DRIVE_ID_EXPANSION_POLICY.md
→ Drive ID追加ルールあり
```
