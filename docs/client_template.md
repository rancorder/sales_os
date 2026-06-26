# 案件カルテ｜{社名}

---
client_id: {slug}
client_name: {社名}
status: {未確認}
stage: pre_research
owner: SM
next_action: {未確認}
blocker: {未確認}
last_updated: YYYY-MM-DD
win_definition: 二次商談トスアップ
confidence: low
---

## 0. AI起動プロンプト
あなたは{社名}の営業案件を伴走するパートナー。以下のカルテが正本。
資料が要るときは6章のDrive参照IDを参照して読め。今日のタスクは「____」。

## 1. 基本情報
| 項目 | 内容 |
|---|---|
| クライアント名 | {社名} |
| 提供商材 | {未確認} |
| 自分の役割 | 営業支援 |
| 体制 | アイドマHD経由SU |
| ステータス | {未確認} |
| Drive参照種別 | {file/folder/url/unverified} |
| Drive参照ID | `{未確認}` |
| Drive参照URL | {未確認} |

## 2. 商材の核 / USP
- {未確認}

## 3. 商談設計
- {未確認}

## 4. 進捗ログ
- {未確認}

## 5. 次の一手
1. {未確認}

## 6. 資料原本（Drive参照・増設可能）

### 6.1 代表Drive参照
| 項目 | 内容 |
|---|---|
| 参照スコープ | representative |
| Drive参照種別 | {file/folder/url/unverified} |
| Drive参照ID | `{未確認}` |
| Drive参照URL | {未確認} |
| 管理方針 | この案件の入口。追加資料IDは6.2に追記する。 |

### 6.2 追加資料ID一覧
| 種別 | 資料名 | Drive参照種別 | Drive ID / URL | 用途 | 更新日 | 状態 |
|---|---|---|---|---|---|---|
| {追加資料} | {未確認} | unverified | {未確認} | {未確認} | {未確認} | unverified |

### 6.3 追加ルール
- Drive IDが増えたら、まずこの6.2表に追記する。
- `DRIVE_REFERENCES.md` は代表Drive参照の一覧として使い、個別資料IDを無制限に詰め込まない。
- `Drive参照種別` は `file` / `folder` / `url` / `multiple` / `unverified` のいずれか。
- `状態` は `active` / `archived` / `deprecated` / `unverified` のいずれか。
- 顧客リスト・電話番号・個人情報入り原本はGitHubに置かず、Drive ID参照に留める。
