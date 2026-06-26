# GitHub / Vercel 営業資料ワークフロー

## 目的
営業資料・商談スライド・案件別プレゼンをGitHubで管理し、Vercelで即共有できる状態にする。

## 基本構成
```text
GitHub repo
├── index.html / present.html
├── data/*.json
├── docs/*.md
├── slides/*.md
└── assets/*
```

## 使いどころ
- 商談スライドを16:9 HTMLで作る
- Mermaidの分岐図を動的表示する
- 案件別ページとして成果物を共有する
- プロンプト保管庫をブックマーク化し、瞬時にコピペできるUIにする
- 案件ごとのFBサイトを生成する

## ユーザーの好み
- アクセス瞬時
- 瞬時にコピペ
- Keepのようなメモより「打つ→出る」呼び出し装置
- GitHub→Vercelでプロンプト/資料を運用

## 商談資料HTML化の意義
- PowerPointより即修正・即共有しやすい
- Vercel URLで商談者に渡せる
- スピーカーノート、分岐、クリック導線、Mermaidを組み込める
- Codex/Claudeで修正しやすい

## 注意
- 顧客名や電話番号入りリストは入れない。
- 公開Vercelに置く場合は匿名化・汎用化する。
- Private repoでもVercel公開URLになる可能性があるため、秘匿資料は公開しない。

## 標準フロー
```text
1. GitHubでHTML/MD作成
2. Vercelへデプロイ
3. 商談/社内確認で利用
4. FBをChatGPT/Claudeで修正指示化
5. Codexで修正
6. GitHubにcommit
7. Vercelで即反映
```
