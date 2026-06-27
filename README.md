# sales-os

アイドマHD経由セールスユニット案件の「案件カルテ母艦」。

詳細な営業OS構造は `docs/claude_sales_os_structure_guide.md` を参照する。

クライアントごとにAIチャットが増えて文脈・成果物が散らばる問題を解決するための正本リポジトリ。各社カルテの0章「AI起動プロンプト」を新チャットに貼れば、その案件の文脈が即立ち上がる。

## 三層アーキテクチャ

- **入力**：Google Drive（各社フォルダに台本・スライド・商談文字起こし。フォルダ名＝会社名）＋ ChatGPT壁打ち
- **正本**：このGitHubリポジトリ（INDEX＋各社カルテ。資料はfileID参照で複製しない）
- **動力**：Claude Code / Codex（ドライブ読取→カルテ生成→INDEX更新→push）

## 構成

```txt
sales-os/
├── README.md
├── .gitignore
├── AGENTS.md        ← v6.1追加：Claude Code / Codex 共通AIエージェント規約
├── INDEX.md         ← 全社一覧（社名・商材・ステータス）
├── CLAUDE.md        ← Claude Code入口 / AGENTS.md参照 / カルテ生成規約
├── clients/
│   └── {番号}_{社名}.md   ← 各社カルテ（0章〜7章）
├── slides/          ← v6追加：HTMLスライド / Vercel公開 / スライド開発OS
├── prompts/         ← AIエージェント向けプロンプト
└── docs/
```

> Driveから移植した都合でカルテはフラット配置（`clients/{番号}_{社名}.md`）。
> お好みで `clients/{社名}/カルテ.md` 構造に展開してもよい。

## カルテ書式

0章 AI起動プロンプト / 1章 基本情報 / 2章 商材の核・USP / 3章 商談設計 / 4章 進捗ログ / 5章 次の一手 / 6章 資料原本（fileID一覧） / 7章 スライド開発履歴

情報が無い項目は捏造せず `{未確認}` で枠のみ残す。

## 初回push（private repo推奨）

```bash
cd sales-os
git init
git add -A
git commit -m "営業OS母艦：営業OS母艦：全28社カルテ初期構築"
git branch -M main
git remote add origin https://github.com/rancorder/sales-os.git
git push -u origin main
```


## 運用ルール

- **正本**：GitHub上のこのリポジトリ。
- **原本置き場**：Google Drive（動画・文字起こし・SCデータ・顧客資料）。
- **カルテ更新**：Drive原本を読み、カルテには判断・要約・fileId参照のみ残す。
- **禁止**：電話番号入りリスト、SCデータCSV、商談動画、契約書、顧客内部資料の直置き。
- **推奨**：private repositoryで運用する。


## v4 更新：Drive ID増加対応

Drive IDは増える前提で設計しています。

- `DRIVE_REFERENCES.md`：全社の代表Drive参照だけを管理
- `clients/{client}.md` 6章：個別資料IDを増設可能な表で管理
- `DRIVE_ID_EXPANSION_POLICY.md`：Drive ID追加時のルール

商談動画・文字起こし・SU定例・SCデータ・スライドなどのIDが増えた場合は、該当clientカルテの6.2へ追記してください。


## v5監査対応

Codex監査の指摘を受け、pushスクリプトを`tools/`へ、PUSHガイドを`docs/`へ移動し、`tools/validate_sales_os.py`の検証範囲を強化した。


## v6 SlideOps対応：GitHub → Vercel スライド開発OS

既存のGitHub/Vercelスライド資産を営業OSに吸収し、スライド制作を「単発資料作成」ではなく「営業判断を実装する開発工程」として扱う。

追加ファイル：

- `slides/README.md`：スライド開発レイヤーの入口
- `slides/SLIDE_OS_POLICY.md`：スライド正本・原本・品質・Vercel運用ルール
- `slides/SOURCE_REPOS.md`：既存GitHubスライド資産からの吸収メモ
- `slides/templates/PROJECT_TEMPLATE.md`：新規スライド案件テンプレート
- `slides/patterns/README.md`：案件横断のスライド構成パターン集
- `prompts/slide_development_prompt.md`：Claude / Codex / GPT向けスライド開発プロンプト
- `docs/slide_ops_sales_os_guide.md`：SlideOps運用ガイド

基本フロー：

```txt
商談ログ / 商談分析
↓
slide_spec.md
↓
storyboard.md
↓
talk_script.md
↓
HTML/CSS/JS
↓
GitHub push
↓
Vercel確認
↓
商談で使用
↓
反応を案件カルテへ戻す
```

このレイヤーにより、商談資料はPowerPoint作業ではなく、GitHub管理の営業プロダクト開発として運用する。


## v6.1 Claude Code / Codex 両対応

Claude Code と Codex の両方から同じ営業OSルールで作業できるよう、AIエージェント共通レイヤーを追加した。

追加・更新ファイル：

- `AGENTS.md`：Claude Code / Codex 共通AIエージェント規約
- `CLAUDE.md`：Claude Code入口。`@AGENTS.md` を参照し、Claude固有の補足を記載
- `docs/dual_agent_ops_guide.md`：Claude Code / Codex の役割分担と共同作業フロー
- `prompts/dual_agent_slide_development_prompt.md`：両対応スライド開発プロンプト

役割分担：

```txt
Claude Code
= 営業文脈整理 / 案件カルテ読解 / 商談分析 / slide_spec / storyboard / talk_script / decision_log

Codex
= HTML/CSS/JS実装 / Vercel向け調整 / 表示崩れ修正 / 差分実装 / レビュー指摘対応
```

最短フロー：

```txt
Claude Codeで勝ち筋を設計
↓
CodexでHTMLスライドとして実装
↓
Vercelで確認
↓
Claude CodeまたはCodexで判断ログと案件カルテを更新
```
