# Codex更新依頼プロンプト

sales-os リポジトリを更新してください。

## 目的
GPTプロジェクトチャットから抽出した営業支援知見を、GitHub正本へ反映する。

## ルール
- Drive原本は複製しない。fileId参照のみ。
- 顧客リスト、電話番号、メールアドレス、SCデータ、動画はGitHubに入れない。
- 事実・分析・仮説・未確認を分ける。
- `{未確認}` を推測で埋めない。
- 既存カルテは全文上書きせず、必要に応じて4章・5章へ追記する。
- 横断知見は `patterns/` へ、運用知見は `docs/` へ、起動プロンプトは `prompts/` へ置く。

## 実行
1. `clients/_chat_extraction_updates/` の追記候補を確認
2. 既存 `clients/{社名}.md` に統合すべきものを統合
3. `patterns/` の重複を整理
4. `docs/` にOS運用ルールを反映
5. `MANIFEST.md` を更新
6. commitする

## commit message
`GPTプロジェクトチャット知見を営業OSへ統合`
