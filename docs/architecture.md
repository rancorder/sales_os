# 営業支援OS アーキテクチャ

## 目的
GPTプロジェクトチャットに散らばった案件文脈・商談判断・架電分析・資料設計を、再利用できる営業支援資産としてGitHubへ正本化する。

## 基本思想
- **Drive = 原本倉庫**：動画、文字起こし、SU定例、SCデータ、顧客資料、Slides/Docs/PDFの原本を置く。
- **GitHub = 正本**：カルテ、戦略、台本、分析結果、横断パターン、AI起動プロンプトを置く。
- **GPT / Claude / Codex = 更新エンジン**：Drive原本を読み、GitHub正本を更新し、必要に応じてDocs/Slides/PDFを生成する。
- **Vercel / HTML = 共有ビュー**：商談資料、案件ダッシュボード、プロンプト呼び出しUIを表示する。

## 三層運用
```text
入力層: Google Drive / ChatGPT壁打ち / 商談文字起こし / 架電ログ
正本層: GitHub sales-os / clients / patterns / docs / prompts
出力層: Word / PDF / Slides / HTML / Vercel / 定例報告
```

## 情報の粒度
チャット全文は保存しない。保存するのは以下のみ。

1. 案件判断
   - 商材の再定義
   - ターゲットの歪み
   - 架電・商談の勝ち筋
   - NG訴求
   - 進捗ログ
   - 次の一手

2. 横断知見
   - 本人拒否の原因分類
   - 受付拒否の改善パターン
   - 一次商談から二次トスアップする型
   - 商談者/架電者/PM報告テンプレ
   - 課題確定済アポの定義

3. OS運用知見
   - GitHub/Driveの役割分担
   - Codex/Claude/GPTの起動ルール
   - 自動化構想
   - GitHub→Vercel運用

## 禁止事項
- 顧客リスト原本、電話番号、メールアドレス、個人情報をGitHubへ入れない。
- 商談動画・SCデータ・CSVをGitHubへ入れない。
- `{未確認}` を推測で埋めない。
- 古いカルテを正本として残さない。旧版は `deprecated` または `_archive` へ。

## 最終形
```text
sales-os/
├── clients/       # 各社カルテ
├── patterns/      # 横断勝ち筋・テンプレ
├── docs/          # OS運用設計
├── prompts/       # AI起動プロンプト
└── outputs/       # 週次総括・定例報告テンプレ
```
