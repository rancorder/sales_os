# DRIVE_ID_EXPANSION_POLICY｜Drive ID増加時の運用ルール

## 基本方針
Drive IDは増えて問題ない。営業OSでは、Drive IDを2階層で管理する。

```txt
DRIVE_REFERENCES.md
→ 全社の代表Drive参照一覧

clients/{client}.md 6章
→ 代表Drive参照 + 個別資料ID一覧
```

## 1. 代表Drive参照
各社につき1件だけ持つ入口ID。

- 会社別Driveフォルダ
- 案件の母艦ファイル
- 参照すべき代表資料

代表Drive参照を変更した場合は、以下を同時に更新する。

```txt
DRIVE_REFERENCES.md
clients/{client}.md の 6.1
```

## 2. 追加資料ID
商談動画、文字起こし、SU定例、SCデータ、商談資料、台本、リード管理表などは、各社カルテの6.2へ追記する。

| 種別 | 資料名 | Drive参照種別 | Drive ID / URL | 用途 | 更新日 | 状態 |
|---|---|---|---|---|---|---|
| 商談動画 | 2026-06-24 定例 | file | `xxxxx` | 商談分析 | 2026-06-26 | active |

## 3. 状態管理
- `active`: 現在参照する資料
- `archived`: 過去資料として保管
- `deprecated`: 古く、原則参照しない
- `unverified`: IDや用途が未確認

## 4. 禁止事項
- 顧客リストや電話番号をGitHub本文に貼らない
- 原本ファイルをGitHubに置かない
- 個別資料IDを `DRIVE_REFERENCES.md` に大量追加しない
- file ID と folder ID を区別せず「フォルダID」と呼ばない

## 5. 判断基準
```txt
全社一覧で見たいID → DRIVE_REFERENCES.md
案件内で使う資料ID → clients/{client}.md 6章
重い原本ファイル → Google Drive
営業判断・台本・分析結果 → GitHub
```
