# Drive / GitHub 運用ルール

## 役割分担

| 場所 | 役割 | 置くもの | 編集するもの |
|---|---|---|---|
| Google Drive | 原本倉庫 | 商談動画、文字起こし、SU定例、SCデータ、顧客資料、納品用Docs/Slides | 原本・配布物 |
| GitHub | 営業OS正本 | カルテ、戦略、台本、分析結果、横断テンプレ、AIプロンプト | 正本md |
| ChatGPT/Claude/Codex | 編集エンジン | なし | GitHub更新、Drive原本分析 |
| Vercel/HTML | 共有ビュー | Webスライド、プロンプトUI、案件ダッシュボード | 表示用成果物 |

## Driveで編集しないもの
- README
- INDEX
- 各社カルテ
- 分析プロトコル
- 新規立ち上げプロトコル
- 勝ちパターン辞書

これらはGitHubを正本とする。

## Driveに残すもの
- 商談動画
- vtt/txt文字起こし原本
- SU定例資料
- SCデータ
- コックピット
- 顧客から受領した原本資料
- Google Docs/Slidesの納品物
- Word/PDF/PPTX成果物

## GitHubに置くもの
- `clients/{社名}.md`
- `patterns/*.md`
- `docs/*.md`
- `prompts/*.md`
- `README.md`
- `CLAUDE.md`
- `_research_protocol.md`
- `_analysis_protocol.md`

## 移行時の判断
DriveにあるmdがGitHubと重複したら、Drive側は `移行済み/` に退避する。
削除はしない。1〜2週間運用し、GitHub正本で問題がないと確認してから削除判断する。

## AIへの指示
Drive原本を読むときは必ず6章のfileIdを参照する。GitHubに原本文字起こしを貼り付けず、要約・判断・次アクションだけを保存する。
