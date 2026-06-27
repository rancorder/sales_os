# dual_agent_ops_guide｜Claude Code / Codex 両対応運用ガイド

## 0. 目的

このガイドは、営業OSを Claude Code と Codex の両方で扱えるようにするための運用ルールである。

目的は、AIエージェントごとに依頼文やルールがズレることを防ぎ、同じ営業OS文脈で以下を実行できるようにすること。

```txt
案件カルテ更新
商談分析
台本作成
スライド設計
HTMLスライド実装
Vercel公開前提の修正
判断履歴の蓄積
```

---

## 1. 基本思想

```txt
AGENTS.md = 共通ルール
CLAUDE.md = Claude Code向け入口
prompts/ = 具体タスクの依頼文
slides/ = HTMLスライド開発レイヤー
clients/ = 案件カルテ正本
outputs/ = 分析・台本・報告書
```

Claude Code と Codex の両方が同じ思想で動くよう、共通ルールは `AGENTS.md` に置く。

---

## 2. なぜ AGENTS.md を中心にするか

複数AIエージェントを使う場合、ツールごとに指示ファイルを分けると、以下が起きる。

```txt
Claudeでは守られるがCodexでは守られない
Codexでは実装されるが営業文脈が抜ける
同じルールを二重更新してズレる
古い方のルールが残る
```

そのため、営業OSでは以下の構造にする。

```txt
AGENTS.md      = 共通ルール本体
CLAUDE.md      = Claude Code入口 + AGENTS.md参照
prompts/*.md   = タスク別プロンプト
```

---

## 3. 役割分担

## Claude Code

Claude Codeは、文脈理解・構成整理・長文Markdown編集に強い前提で使う。

主な担当：

```txt
案件カルテの読解
商談分析
勝ち筋抽出
商談ストーリー作成
slide_spec.md作成
storyboard.md作成
talk_script.md作成
decision_log.md作成
docs/やprompts/の整備
```

向いている依頼：

```txt
clients/25_hanayuki.md と outputs を読んで、アラオ様2次商談のスライド設計を作って
この商談ログから勝ち筋を抽出して、次回商談ストーリーにして
既存のSlideOpsルールに合わせて、スライド案件フォルダを設計して
```

---

## Codex

Codexは、実装・差分修正・HTML/CSS/JS・Vercel向け調整に強い前提で使う。

主な担当：

```txt
index.html作成
style.css作成
main.js作成
静的HTMLスライド実装
レスポンシブ調整
表示崩れ修正
Vercel向け設定
レビュー指摘対応
```

向いている依頼：

```txt
slides/projects/hanayuki_arao_20260703/ の slide_spec.md と storyboard.md を読み、静的HTMLスライドを実装して
PC/スマホで読みやすいCSSに調整して
Vercelで静的公開できるようにファイル構成を整えて
```

---

## 4. 共同作業フロー

最も安定する流れ：

```txt
1. Claude Codeで案件カルテと商談分析を整理
2. Claude Codeでslide_spec / storyboard / talk_scriptを作成
3. CodexでHTML/CSS/JSを実装
4. Codexで表示・構成の微修正
5. Claude Codeでdecision_logと案件カルテへの反映を確認
6. Vercel URLをvercel_url.mdとclientsカルテ7章に追記
```

---

## 5. 1エージェント完結の場合

### Claude Codeだけで進める場合

```txt
設計から実装まで可能。
ただしHTML/CSS/JSは簡潔にし、必ずreview_checklistで確認する。
```

### Codexだけで進める場合

```txt
実装前に必ずclients/outputs/slidesルールを読む。
slide_spec.mdが無い場合は、先に作る。
HTMLだけ作って完了にしない。
```

---

## 6. 共通プロンプトの使い分け

### スライド開発

```txt
prompts/dual_agent_slide_development_prompt.md
```

### 通常のスライド開発

```txt
prompts/slide_development_prompt.md
```

### OS全体理解

```txt
docs/claude_sales_os_structure_guide.md
docs/slide_ops_sales_os_guide.md
```

---

## 7. スライド開発の標準成果物

```txt
slides/projects/{client}_{theme}_{YYYYMMDD}/
├── slide_spec.md
├── storyboard.md
├── talk_script.md
├── decision_log.md
├── review_checklist.md
├── index.html
├── style.css
├── main.js
└── vercel_url.md
```

CodexがHTMLだけ作った場合でも、Claude CodeまたはCodex自身がMarkdown側を補完する。

---

## 8. 失敗パターン

```txt
Claude Codeが設計だけして実装導線がない
CodexがHTMLだけ作って商談文脈がない
Vercel URLが案件カルテに残らない
decision_logが空のまま
顧客原本をGitHubに貼ってしまう
```

---

## 9. 成功パターン

```txt
slide_specに勝ち筋がある
storyboardに商談の流れがある
talk_scriptに人間が話す補足がある
index.htmlが商談で見せられる
decision_logに判断理由がある
review_checklistで品質確認されている
Vercel URLが残っている
商談後の反応がclientsカルテに戻っている
```

---

## 10. 一言まとめ

```txt
Claude Codeで勝ち筋を設計し、Codexで画面に実装する。
両方をAGENTS.mdで束ね、営業OSの判断資産として残す。
```
