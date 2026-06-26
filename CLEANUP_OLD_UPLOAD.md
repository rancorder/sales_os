# CLEANUP_OLD_UPLOAD｜前回アップロードの掃除

前回のGitHubには、案件カルテやテンプレートがルート直下に散っていました。
この状態ではAIが誤読するため、以下のどちらかで修正します。

## 推奨

ローカルでこのパッケージを展開し、以下で強制反映します。

```bash
git push -f origin main
```

## Webで直す場合

ルート直下から以下を削除してください。

- `01_*.md` 〜 `28_*.md`
- `*_update_candidate.md`
- `call_kpi_analysis_format.md` などpatterns配下にあるべきファイル
- `claude_research_request.md` などprompts配下にあるべきファイル
- `architecture.md` などdocs配下にあるべきファイル
- `client_card.md`, `strategy_v2_team.md`, `operation_design.md`, `gpt_feedback_review.md`
- `download`, `download (1)`

削除後、正しいフォルダ構造のファイルだけをアップロードしてください。
