# CHECK_BEFORE_DELETE｜GPTプロジェクト削除前チェック v5

GPTプロジェクトを削除してよいのは、以下をすべて満たした後。

## 1. GitHub構造

- `rancorder/sales_os` にv5が反映済み
- ルート直下に案件カルテがない
- `clients/` に28社分のカルテがある
- `docs/`, `patterns/`, `prompts/`, `tools/` がある

## 2. 検証

```bash
python tools/validate_sales_os.py
```

以下が出ること。

```txt
OK: sales_os validation passed
root allow-list: strict
drive reference consistency: strict
drive expansion table: v5
```

## 3. 重要カルテ

- `clients/18_wse.md` はWSE
- `clients/19_reegle.md` はReegle
- `clients/20_food_surprise.md` はフードサプライズ
- `clients/21_ast.md` はアスト
- `clients/25_hanayuki.md` は花雪

## 4. Drive

- 原本資料はGoogle Driveに残っている
- GitHubにはDrive ID / URL参照だけを置いている
- 追加資料IDは各社カルテ6.2へ追記する運用になっている

## 判定

上記がOKなら、GPTプロジェクトチャットは削除可能。
