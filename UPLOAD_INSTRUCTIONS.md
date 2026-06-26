# UPLOAD_INSTRUCTIONS｜GitHubへ正しく投入する手順

## 推奨：コマンドラインで投入

```bash
cd sales_os_clean_v2
git init
git add -A
git commit -m "営業OS正本をクリーン構造で再構築"
git branch -M main
git remote add origin https://github.com/rancorder/sales_os.git
git push -f origin main
```

既存の誤アップロードを一掃するため、今回は `git push -f` 推奨です。
Webアップロードで上書きすると、ルート直下に不要ファイルが残る可能性があります。

## Webアップロードしか使わない場合

1. 現在のGitHub上の不要ファイルを削除する
2. ZIPを展開する
3. `sales_os_clean_v2` フォルダの「中身」をアップロードする
4. `clients/21_ast.md` を開いて、先頭が `# 案件カルテ｜株式会社アスト` であることを確認する
5. ルート直下に `21_ast.md` など案件ファイルが出ていないことを確認する

## NG

- `clients` フォルダ内のファイルを、個別にルート直下へアップロードしない
- `patterns` フォルダ内のファイルを、個別にルート直下へアップロードしない
- `download` や `download (1)` というファイルをアップロードしない
