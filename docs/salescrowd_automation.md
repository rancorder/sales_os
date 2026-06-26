# SalesCrowd / 架電業務 自動化構想

## 背景
SalesCrowdへ再ログインして案件・架電結果・リンクを確認する作業が面倒で、Playwrightによる自動化を検討している。

## 目的
- 営業支援担当が案件状況を毎回手動確認しなくてよい状態にする。
- 架電ログやコックピット情報をGitHub/Driveに同期し、分析プロトコルへ接続する。
- GPT/Claude/Codexが読むための材料を定型化する。

## 基本方針
Playwrightでログイン・画面遷移・CSV/表データ取得をレシピ化する。

```bash
playwright codegen https://sales-crowd.jp/
```

## 同一URL問題
SalesCrowdではどのページも同じリンクに見える場合がある。URLではなく以下をキーにする。

- ページ内の案件名
- DOM上の見出し
- 表の列名
- ボタン/タブのテキスト
- 遷移後の状態

## 取得したい情報
- 案件名
- 架電期間
- 電話数
- 着電率
- 受付拒否率
- 対象者通話率
- 対象者拒否率
- 資料請求数
- アポ数
- 本人拒否ログ
- 受付拒否ログ
- アポログ

## GitHub連携
取得結果は原則GitHubに直接置かず、Drive/CSV原本へ保存し、GitHubには分析結果だけを残す。

```text
SalesCrowd → CSV/ログ → Drive原本 → _analysis_protocol → clients/{社名}.md 4章追記
```

## 重要ルール
- 認証情報はGitHubへ入れない。
- `.env` / `.mcp.json` / cookie / token は `.gitignore` 対象。
- Playwrightの録画やスクショは個人情報を含む可能性があるためDrive保管。

## 将来像
1. 案件ごとのDrive IDをスプレッドシートで管理
2. PlaywrightでSalesCrowdを巡回
3. 新規ログのみDriveへ保存
4. Codexが未分析期間を検出
5. `clients/{社名}.md` 4章へ分析済みマーカー付きで追記
6. 週次総括を生成
