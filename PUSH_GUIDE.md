# PUSH_GUIDE｜GitHub初回投入手順

## 前提
- GitHubリポジトリは **private** 推奨。
- このZIPには動画、SCデータCSV、顧客リスト原本は含めていない。
- Drive原本は6章のfileIdで参照する。

## 初回push

```bash
cd sales-os_github_ready
git init
git add -A
git commit -m "営業OS母艦：GitHub正本初期構築"
git branch -M main
git remote add origin https://github.com/rancorder/sales-os.git
git push -u origin main
```

## 以後の運用

```bash
# 変更確認
git status
git diff

# 更新
git add -A
git commit -m "{案件名}: カルテ更新"
git push
```

## 注意
- Driveから追加取得した素材をそのまま置かない。
- 個人情報・電話番号・顧客リスト・CSV・動画はGitHubに入れない。
- 迷ったら `clients/{社名}.md` には要約とfileIdだけ残す。
