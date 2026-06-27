# Slides｜営業OS スライド開発レイヤー

このディレクトリは、営業OSにおける **HTMLスライド / Vercel公開 / 商談資料開発** の正本置き場です。

営業OSの基本思想はそのまま維持します。

```txt
Drive   = 原本置き場
GitHub  = 正本・判断・型・分析履歴
AI      = 分析・構成・実装エージェント
Vercel  = スライド確認・公開環境
Word/PDF/PPT = 現場配布・提出用
```

## 目的

スライド制作を「毎回ゼロから作る作業」ではなく、

```txt
商談分析 → スライド設計 → HTML実装 → Vercel確認 → 商談反応 → 改善履歴
```

として蓄積し、案件横断で再利用できる営業資産にする。

## 基本フロー

```txt
1. clients/{client}.md を読む
2. outputs/ の商談分析・次の一手を読む
3. slides/projects/{project}/slide_spec.md を作る
4. storyboard.md でスライド順を設計する
5. talk_script.md で補足トークを作る
6. index.html / style.css / main.js でHTMLスライド化する
7. GitHubへpushしてVercelで確認する
8. decision_log.md に判断理由を残す
9. 商談後の反応をclientsカルテへ戻す
```

## ディレクトリ構成

```txt
slides/
├── README.md
├── SLIDE_OS_POLICY.md
├── SOURCE_REPOS.md
├── templates/
│   └── PROJECT_TEMPLATE.md
├── projects/
│   └── {client}_{theme}_{date}/
│       ├── slide_spec.md
│       ├── storyboard.md
│       ├── talk_script.md
│       ├── decision_log.md
│       ├── review_checklist.md
│       ├── index.html
│       ├── style.css
│       ├── main.js
│       └── vercel_url.md
└── patterns/
    ├── README.md
    ├── pain_to_solution_flow.md
    ├── executive_decision_flow.md
    ├── demo_bridge_flow.md
    └── meeting_feedback_flow.md
```

## 重要ルール

- スライドHTMLだけを正本にしない。
- 必ず `slide_spec.md` と `decision_log.md` を残す。
- 商談ログにない事実を盛らない。
- 顧客機密・個人情報・生ログはGitHubに直置きしない。
- Vercel URLは `vercel_url.md` と案件カルテ7章に残す。

## 使い分け

```txt
slide_spec.md     = 何を伝えるか
storyboard.md     = どの順番で伝えるか
talk_script.md    = どう話すか
index.html        = 見せるもの
decision_log.md   = なぜそう作ったか
review_checklist.md = 品質確認
vercel_url.md     = どこで見られるか
```

## このレイヤーの本質

スライドを成果物で終わらせず、

```txt
勝ち筋の設計図
判断履歴
再利用できる型
商談反応の学習データ
```

として残す。

つまり、スライド制作を **営業資料作成** から **営業プロダクト開発** に昇格させる。
