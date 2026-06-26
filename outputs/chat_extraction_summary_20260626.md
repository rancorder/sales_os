# GPTプロジェクトチャット吸い上げサマリー｜2026-06-26

## 実施内容
GPTプロジェクトチャット・過去要約・営業OS設計メモから、GitHubに保存すべき情報を抽出し、以下に格納した。

## 追加した主なファイル

### docs/
- `architecture.md`：営業支援OS全体設計
- `drive_github_rule.md`：Drive/GitHub役割分担
- `chat_cleanup_protocol.md`：チャット削除前の吸い上げ手順
- `salescrowd_automation.md`：SalesCrowd/Playwright自動化構想
- `github_vercel_workflow.md`：GitHub→Vercel商談資料運用
- `sm_abc_operation.md`：受注後のA/B/C SM運用設計

### patterns/
- `架電KPI分析フォーマット.md`
- `本人拒否_原因分類.md`
- `受付拒否_冒頭改善.md`
- `二次トスアップ勝ち筋.md`
- `課題確定済アポ_定義.md`
- `リスト設計_痛みシグナル.md`
- `商談者FBテンプレ.md`
- `架電者FBテンプレ.md`
- `PM報告テンプレ.md`

### prompts/
- `gpt_project_chat_extraction.md`
- `codex_update_request.md`
- `claude_research_request.md`
- `gemini_deepresearch_request.md`

### clients/_chat_extraction_updates/
- `05_共栄データセンター_追記候補.md`
- `01_FirstFan_AGERUケア_追記候補.md`
- `08_T2_Laboratory_追記候補.md`
- `発注タイミング特定サービス_追記候補.md`
- `営業OS_一気通貫ワークフロー_追記候補.md`

## 重要判断
- チャット全文は保存しない。
- 案件判断は `clients/`、横断知見は `patterns/`、OS設計は `docs/`、AI起動文は `prompts/` に保存。
- 原本資料・動画・CSV・個人情報はDriveに残し、GitHubへ入れない。

## 未完了
- GitHubリポジトリ `rancorder/sales-os` が現時点でアクセス不可/未作成のため、実GitHubへのpushは未実行。
- repo作成後、このパッケージをそのままpushする。
