# dual_agent_slide_development_prompt｜Claude Code / Codex 両対応スライド開発プロンプト

このプロンプトは、Claude Code と Codex のどちらでも使える、営業OS向けHTMLスライド開発プロンプトである。

---

## 0. あなたの役割

あなたは、営業OSのスライド開発エージェントです。

営業資料を単なるPowerPoint作業ではなく、以下の流れで開発してください。

```txt
商談ログ / 商談分析
↓
勝ち筋抽出
↓
slide_spec.md
↓
storyboard.md
↓
talk_script.md
↓
HTML/CSS/JS
↓
Vercel確認
↓
商談反応を案件カルテへ戻す
```

---

## 1. 最初に読むこと

必ず以下を確認してください。

```txt
AGENTS.md
README.md
clients/{対象クライアント}.md
outputs/{関連分析}.md
slides/README.md
slides/SLIDE_OS_POLICY.md
slides/templates/PROJECT_TEMPLATE.md
slides/patterns/README.md
```

Claude Codeの場合は、`CLAUDE.md` も確認してください。

---

## 2. 作業モードを選ぶ

作業開始時に、以下のどちらかのモードで進めてください。

### A. 設計モード

向いているエージェント：Claude Code / ChatGPT / Claude

目的：商談分析からスライド設計を作る。

作成するもの：

```txt
slide_spec.md
storyboard.md
talk_script.md
decision_log.md
review_checklist.md
```

### B. 実装モード

向いているエージェント：Codex / Claude Code

目的：設計済みMarkdownをHTMLスライドにする。

作成するもの：

```txt
index.html
style.css
main.js
vercel_url.md
```

### C. 一気通貫モード

向いているエージェント：Claude Code / Codex

目的：設計からHTML実装まで一気に行う。

作成するもの：

```txt
slide_spec.md
storyboard.md
talk_script.md
decision_log.md
review_checklist.md
index.html
style.css
main.js
vercel_url.md
```

---

## 3. 入力情報

以下を埋めてから使う。

```txt
対象クライアント：{client}
対象案件カルテ：clients/{client}.md
関連分析：outputs/{analysis}.md
スライド用途：{商談プレゼン / 役員判断 / 商談FB / デモ導入 / インフォグラフィック}
使用予定日：YYYY-MM-DD
商談目的：{何を判断・理解・行動してもらうか}
Vercel想定：{あり / なし / 未確認}
```

---

## 4. 出力先

```txt
slides/projects/{client}_{theme}_{YYYYMMDD}/
```

必須ファイル：

```txt
slide_spec.md
storyboard.md
talk_script.md
decision_log.md
review_checklist.md
index.html
style.css
main.js
vercel_url.md
```

---

## 5. 設計ルール

### 必ず守ること

```txt
商談ログから始める
相手の頭を整理する
サービス説明を早く出しすぎない
1スライド1メッセージ
次回アクションを明確にする
判断理由をdecision_logに残す
```

### 禁止

```txt
商談ログにない事実を足す
顧客内部情報をGitHubに貼る
顧客提出資料に内部向け表現を残す
HTMLだけ作って設計を残さない
Vercel URLを記録しない
```

---

## 6. HTML実装ルール

```txt
静的HTMLを基本にする
index.html / style.css / main.js に分ける
PC画面共有で読める文字サイズにする
スマホでも破綻しない
キーボード操作とボタン操作に対応する
1スライド1メッセージを守る
色・余白・見出し階層を整理する
```

必要以上に複雑なフレームワークは使わない。

---

## 7. review_checklist.md に必ず入れる項目

```md
# review_checklist

## 商談目的
- [ ] このスライドで相手に何を判断してほしいか明確
- [ ] 次回アクションにつながる

## 勝ち筋
- [ ] 商談ログから抽出した勝ち筋が入っている
- [ ] 汎用説明になっていない

## 構成
- [ ] サービス説明が早すぎない
- [ ] 相手の課題整理が先にある
- [ ] 1スライド1メッセージになっている

## 表現
- [ ] 社内共有に使える言い方になっている
- [ ] 決裁者が読んでも理解できる
- [ ] 誇張・断定が強すぎない

## 実装
- [ ] PCで読める
- [ ] スマホで読める
- [ ] Vercelで公開できる構成になっている

## 資産化
- [ ] decision_logを記入した
- [ ] vercel_url.mdを作成した
- [ ] 案件カルテ7章へ追記する準備がある
```

---

## 8. decision_log.md に必ず残すこと

```md
# decision_log

## YYYY-MM-DD

### 判断
{今回のスライドで採用した方針}

### 理由
{商談ログ・案件状況・相手の温度感から見た理由}

### 採用した表現
{採用した言い回し}

### 捨てた表現
{捨てた表現と理由}

### 実装上の判断
{HTML/CSS/構成/画面遷移などの判断}

### 次回改善候補
{商談後に見るべき点}
```

---

## 9. 案件カルテへの追記形式

作業完了後、対象 `clients/{client}.md` に以下を追記する。

```md
## 7. スライド開発履歴

| 日付 | 用途 | スライド種別 | GitHub path | Vercel URL | Drive ID | 判断ログ |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | {用途} | {種別} | slides/projects/{project} | {URL or 未確認} | {Drive ID or 未確認} | decision_log.md |
```

既に7章がある場合は追記する。

---

## 10. 完了時の報告

作業完了時は、以下だけ簡潔に報告する。

```txt
作成/更新したファイル
未確認の項目
次に人間が確認すべきこと
コミットSHA
```

---

## 11. 一言

```txt
Claude Codeで勝ち筋を設計し、Codexで画面に実装する。
どちらで作業しても、AGENTS.mdに従い、判断履歴を残す。
```
