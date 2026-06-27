# AGENTS.md｜営業OS 共通AIエージェント規約

このファイルは、Claude Code / Codex / その他のコーディングエージェントが `rancorder/sales_os` で作業するための共通ルールである。

Claude Codeは `CLAUDE.md` からこのファイルを参照する。Codexはこの `AGENTS.md` を共通コンテキストとして扱う。

---

## 0. このリポジトリの正体

このリポジトリは、営業支援案件の **案件カルテ母艦** である。

単なる資料置き場ではなく、以下を蓄積する。

```txt
案件カルテ
商談分析
架電分析
商談台本
スライド設計
見積り判断
改善履歴
Drive参照ID
判断理由
再利用できる型
```

営業OSの基本思想：

```txt
Drive   = 原本置き場
GitHub  = 正本・判断・型・分析履歴
AI      = 分析・構成・実装エージェント
Vercel  = HTMLスライド確認・公開環境
Word/PDF/PPT = 現場配布・提出用
```

---

## 1. 最重要ルール

### 1.1 捏造禁止

情報がない場合は、必ず `{未確認}` と書く。

```txt
不明な会社情報
不明な商談日時
不明な担当者名
不明な価格
不明なVercel URL
不明なDrive ID
```

これらを推測で埋めない。

### 1.2 原本をGitHubに置かない

GitHubに置くのは、要約・判断・構成・参照IDだけ。

置いてはいけないもの：

```txt
商談動画
商談文字起こしの全文
電話番号入りリスト
メールアドレス一覧
顧客内部資料の原本
契約書
SCデータCSV
個人情報
重い画像・動画素材
```

### 1.3 判断履歴を残す

成果物だけを作らない。

必ず、なぜそう判断したかを残す。

```txt
decision_log.md
clients/{client}.md の進捗ログ
outputs/{analysis}.md
slides/projects/{project}/decision_log.md
```

### 1.4 既存ファイルを壊さない

既存カルテは原則として全面上書きしない。

更新する場合は、以下を優先する。

```txt
4章 進捗ログ
5章 次の一手
6章 資料原本
7章 スライド開発履歴
```

---

## 2. まず読むファイル

作業開始時は、対象に応じて以下を読む。

### 営業OS全体を扱う場合

```txt
README.md
INDEX.md
CLAUDE.md
AGENTS.md
docs/claude_sales_os_structure_guide.md
```

### 案件作業の場合

```txt
clients/{client}.md
outputs/{related_output}.md
DRIVE_REFERENCES.md
```

### スライド作業の場合

```txt
slides/README.md
slides/SLIDE_OS_POLICY.md
slides/SOURCE_REPOS.md
slides/templates/PROJECT_TEMPLATE.md
slides/patterns/README.md
prompts/slide_development_prompt.md
prompts/dual_agent_slide_development_prompt.md
```

### Claude Code / Codex 両対応作業の場合

```txt
AGENTS.md
docs/dual_agent_ops_guide.md
prompts/dual_agent_slide_development_prompt.md
```

---

## 3. Claude Code と Codex の役割分担

### Claude Codeが得意な作業

```txt
営業文脈の整理
案件カルテの読み解き
複数ファイルの構成整理
商談ストーリー設計
slide_spec / storyboard / talk_script 作成
長文ドキュメント整備
既存OSルールの再編
```

### Codexが得意な作業

```txt
HTML/CSS/JS実装
静的スライドの作成
Vercel向け構成調整
表示崩れ修正
ファイル差分の実装
レビュー指摘対応
軽いテスト・検証
```

### 両方に共通する作業

```txt
GitHub上のMarkdown更新
案件カルテ更新
スライド案件フォルダ作成
レビュー チェックリスト更新
判断ログの追記
```

---

## 4. スライド開発ルール

スライドはPowerPoint作業ではない。

営業OSでは、スライドを **営業判断を実装したプロダクト** として扱う。

標準フロー：

```txt
商談ログ / 商談分析
↓
slide_spec.md
↓
storyboard.md
↓
talk_script.md
↓
index.html / style.css / main.js
↓
GitHub push
↓
Vercel確認
↓
商談で使用
↓
反応を案件カルテへ戻す
```

スライド案件には原則として以下を作る。

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

---

## 5. スライド品質基準

```txt
1スライド1メッセージ
商談ログから始める
相手の課題整理を先に置く
サービス説明を早く出しすぎない
社内共有されても意味が通じる表現にする
決裁者が読んでも判断材料になる構成にする
スマホ/PCの両方で読める文字サイズにする
```

禁止：

```txt
見た目だけ良いが勝ち筋がない
HTMLだけ作って設計がない
商談ログにない事実を足す
顧客提出資料に内部向けメモを残す
```

---

## 6. ファイル命名

### clients

```txt
clients/{番号}_{社名}.md
```

### outputs

```txt
outputs/{client}_{theme}_{YYYYMMDD}.md
```

### slides projects

```txt
slides/projects/{client}_{theme}_{YYYYMMDD}/
```

### prompts

```txt
prompts/{purpose}_prompt.md
```

社名・テーマは英小文字・数字・アンダースコアを基本とする。

---

## 7. 文章ルール

営業スクリプト・メール・顧客向け資料では、基本的に以下を守る。

```txt
御社 → 貴社
断定しすぎない
相手の既存体制を否定しない
提案前に課題整理を置く
判断材料として整理する
```

社内向け分析では、温度感・勝ち筋・懸念を明確に書く。

---

## 8. コミット方針

1コミット1目的を基本にする。

例：

```txt
Add dual agent workflow guide
Add SlideOps project template
Update README with dual agent operations
Update Claude instructions to import AGENTS
```

大きな変更では、更新内容を `docs/` または対象ファイル内に明記する。

---

## 9. 完了条件

作業完了時は、以下を確認する。

```txt
必要なファイルを作成/更新した
既存の正本ルールを壊していない
捏造がない
Drive原本の直置きがない
判断理由が残っている
READMEや関連ガイドに導線がある
Claude Code / Codex のどちらから見ても作業ルールが分かる
```

---

## 10. 一言要約

```txt
営業OSでは、AIに成果物だけを作らせない。
判断・構成・実装・検証・反応まで残して、次回の精度を上げる。
```
