# SlideOps for Sales OS｜営業OS スライド開発ガイド

## 0. この資料の目的

この資料は、営業OSに GitHub → Vercel のHTMLスライド開発システムを統合するための運用ガイドである。

従来の営業OSは、以下を中心にしていた。

```txt
Drive   = 原本置き場
GitHub  = 案件カルテ・分析・台本・判断履歴の正本
AI      = 分析・更新エージェント
Word/PDF = 現場配布用
```

ここに、以下を追加する。

```txt
Vercel = スライド公開・確認環境
slides/ = スライド開発レイヤー
```

---

## 1. なぜスライド開発をOSに入れるのか

営業支援では、商談分析や台本だけでは足りない。

実際の商談では、以下が必要になる。

```txt
見込み客に見せる資料
決裁者に回す資料
デモ前に論点を揃える資料
PMへ共有する商談FB資料
複雑な仕組みを一枚で説明する図解
```

これらを毎回ゼロから作ると、知見が残らない。

そこで、スライド制作を以下のように扱う。

```txt
資料作成ではなく、営業判断の実装
```

---

## 2. 全体構造

```txt
商談動画 / 文字起こし / 顧客資料
        ↓
Driveに原本保管
        ↓
clientsカルテ / outputs分析を読む
        ↓
slide_spec.mdで設計
        ↓
storyboard.mdで順番化
        ↓
talk_script.mdで話し方を補強
        ↓
HTML/CSS/JSでスライド化
        ↓
GitHubにpush
        ↓
VercelでURL確認
        ↓
商談で使用
        ↓
反応をclientsカルテへ戻す
```

---

## 3. 追加ディレクトリ

```txt
slides/
├── README.md
├── SLIDE_OS_POLICY.md
├── SOURCE_REPOS.md
├── templates/
├── projects/
└── patterns/
```

### slides/README.md

スライド開発レイヤーの入口。

### slides/SLIDE_OS_POLICY.md

正本・原本・禁止事項・品質基準・Vercel運用を定義する規約。

### slides/SOURCE_REPOS.md

既存GitHubスライド資産から何を吸収するかのメモ。

### slides/templates/

新規スライド案件を作るときのテンプレート。

### slides/projects/

個別スライド案件の正本。

### slides/patterns/

案件横断で再利用できるスライド構成パターン。

---

## 4. 既存GitHub資産から吸収した考え方

既存のHTMLスライド資産から吸収するのは、完成物そのものではない。

吸収するのは以下。

```txt
GitHubでHTMLスライドを管理する
VercelでURL確認する
index.html / present.html を入口にする
静的HTMLで高速に商談資料を作る
商談資料をWebプロダクトのように改善する
```

営業OSでは、これをさらに拡張する。

```txt
HTMLスライド
+
slide_spec
+
storyboard
+
talk_script
+
decision_log
+
review_checklist
+
案件カルテ更新
```

---

## 5. スライド案件の作り方

### Step 1. 案件カルテを読む

```txt
clients/{client}.md
```

確認すること：

- 商材の核
- 商談設計
- 進捗ログ
- 次の一手
- Drive参照ID

### Step 2. 商談分析を読む

```txt
outputs/{analysis}.md
```

確認すること：

- 商談結果
- 温度感
- 仮説とのズレ
- 勝ち筋
- 次回の論点

### Step 3. スライド案件を作る

```txt
slides/projects/{client}_{theme}_{YYYYMMDD}/
```

### Step 4. slide_spec.mdを作る

何を伝えるかを定義する。

### Step 5. storyboard.mdを作る

どの順番で伝えるかを定義する。

### Step 6. talk_script.mdを作る

どう話すかを補強する。

### Step 7. HTML実装する

```txt
index.html
style.css
main.js
```

### Step 8. decision_log.mdを書く

なぜこの構成・表現・見せ方にしたかを残す。

### Step 9. Vercel URLを記録する

```txt
vercel_url.md
```

### Step 10. 案件カルテに戻す

`clients/{client}.md` に7章「スライド開発履歴」を追加・更新する。

---

## 6. スライド制作の5分類

```txt
商談プレゼン型
役員判断型
商談FB型
デモ導入型
インフォグラフィック型
```

### 商談プレゼン型

見込み客に提示する外向き資料。

### 役員判断型

決裁者が短時間で判断するための資料。

### 商談FB型

PM・社内向けに商談結果を整理する資料。

### デモ導入型

操作画面を見る前に、見るポイントを揃える資料。

### インフォグラフィック型

複雑な仕組みを一枚で理解させる資料。

---

## 7. Codex / Claude への依頼方法

以下のプロンプトを使う。

```txt
prompts/slide_development_prompt.md
```

依頼例：

```txt
clients/25_hanayuki.md と直近のoutputsを読んで、
2026-07-03 アラオ様2次商談用のHTMLスライドを作成してください。
slides/SLIDE_OS_POLICY.md と prompts/slide_development_prompt.md に従って、
slide_spec / storyboard / talk_script / decision_log / review_checklist / index.html / style.css / main.js を作成してください。
```

---

## 8. 高品質最短化のポイント

### 速くなる理由

```txt
型がある
順番が決まっている
AIへの依頼文が固定される
GitHubで差分管理できる
Vercelですぐ確認できる
過去の勝ち筋を流用できる
```

### 品質が上がる理由

```txt
商談ログから始まる
勝ち筋がslide_specに残る
構成理由がdecision_logに残る
review_checklistで確認できる
商談後の反応が案件カルテに戻る
```

---

## 9. 最重要ルール

```txt
スライドHTMLだけを作って終わらない。
必ず、設計・話法・判断・確認・反応まで残す。
```

---

## 10. 一言まとめ

```txt
SlideOps for Sales OS は、営業資料をPowerPoint作業から、GitHub管理の営業プロダクト開発に昇格させる仕組みである。
```
