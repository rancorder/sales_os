# sales-os

アイドマHD経由セールスユニット案件の「案件カルテ母艦」。

クライアントごとにAIチャットが増えて文脈・成果物が散らばる問題を解決するための正本リポジトリ。各社カルテの0章「AI起動プロンプト」を新チャットに貼れば、その案件の文脈が即立ち上がる。

## 三層アーキテクチャ

- **入力**：Google Drive（各社フォルダに台本・スライド・商談文字起こし。フォルダ名＝会社名）＋ ChatGPT壁打ち
- **正本**：このGitHubリポジトリ（INDEX＋各社カルテ。資料はfileID参照で複製しない）
- **動力**：Claude Code / Codex（ドライブ読取→カルテ生成→INDEX更新→push）

## 構成

```
sales-os/
├── README.md
├── .gitignore
├── INDEX.md          ← 全社一覧（社名・商材・ステータス）
├── CLAUDE.md         ← カルテ生成規約
└── clients/
    └── {番号}_{社名}.md   ← 各社カルテ（0章〜6章）
```

> Driveから移植した都合でカルテはフラット配置（`clients/{番号}_{社名}.md`）。
> お好みで `clients/{社名}/カルテ.md` 構造に展開してもよい。

## カルテ書式

0章 AI起動プロンプト / 1章 基本情報 / 2章 商材の核・USP / 3章 商談設計 / 4章 進捗ログ / 5章 次の一手 / 6章 資料原本（fileID一覧）

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
