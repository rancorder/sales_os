# 追記候補｜営業OS 一気通貫ワークフロー

## 種別
OS設計。`docs/architecture.md` または `docs/chat_cleanup_protocol.md` に統合候補。

## 核
商談ログ→分析→FB→資料→台本→定例報告を毎回ゼロから考えず、一気通貫で吐き出す営業OSを作る。

## 出力物
- 商談判断ログMD
- 商談者FB
- 架電者FB
- 顧客提示レポート
- 定例報告文
- 次回商談台本
- Mermaid分岐図
- Word/PDF/PPT出力
- GitHub/Vercelの案件別ページ

## GitHubの役割
GitHubは「資料置き場」ではなく、**検証知の倉庫**。
商談ログそのものではなく、仮説検証ログを蓄積する。

## 保存ルール
- 人名・電話番号・顧客名は必要に応じて匿名化
- Private repo一択
- AGENTS.md / CLAUDE.md には FACT / ANALYSIS / HYPOTHESIS の分離を明記
- 仮説は仮説として保存する

## 出力安定化の原則
自由入力→自由出力はブレる。
以下の3段階に分ける。

```text
案件カード
↓
分析テンプレ
↓
出力テンプレ
```

必須分離：
- 事実
- 推測
- 仮説
- 確認事項
- 次アクション
