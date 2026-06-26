# CHECK_BEFORE_DELETE｜GPTプロジェクト削除前チェック

GPTプロジェクトを削除する前に、GitHub上で以下を確認する。

## 1. 構造
```txt
sales_os/
├── README.md
├── INDEX.md
├── DRIVE_REFERENCES.md
├── DRIVE_ID_EXPANSION_POLICY.md
├── clients/
├── docs/
├── patterns/
├── prompts/
└── tools/
```

ルート直下に `21_ast.md` や `call_kpi_analysis_format.md` が散っていたらNG。

## 2. 代表Drive参照
- `DRIVE_REFERENCES.md` に28件の代表Drive参照がある
- `clients/21_ast.md` の6.1に `15ez44jIAClPxXA3KjJ0_HlPLsqnyYpIC` がある
- `clients/20_food_surprise.md` の6.1に `1Zcq0PR1ATTCCoJ8bfn1T4bMc8-MtfIlB` がある

## 3. 追加資料IDテーブル
各clientカルテの6章に次の表がある。

```md
| 種別 | 資料名 | Drive参照種別 | Drive ID / URL | 用途 | 更新日 | 状態 |
```

## 4. 本文整合
- `clients/21_ast.md` → `# 案件カルテ｜株式会社アスト`
- `clients/20_food_surprise.md` → `# 案件カルテ｜株式会社フードサプライズ`
- `clients/18_wse.md` → `# 案件カルテ｜ワールドシステムエンジニアリング有限会社（WSE）`

## 5. 検証コマンド
```bash
python tools/validate_sales_os.py
```

`OK: sales_os validation passed` が出れば、GPTプロジェクト削除可。
