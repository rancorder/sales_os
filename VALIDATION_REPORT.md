# VALIDATION_REPORT｜sales_os_clean_v4

## 実行結果

```txt
OK: sales_os validation passed
client cards checked: 28
drive expansion table: v4
```

## v4検証内容
- 全28件のclientカルテに代表Drive IDが入っている
- 全28件のclientカルテに6.2「追加資料ID一覧」がある
- 6.2表は以下の拡張カラムに統一

```md
| 種別 | 資料名 | Drive参照種別 | Drive ID / URL | 用途 | 更新日 | 状態 |
```

- 旧式の `| 資料 | fileId |` テーブルが残っていない
- `DRIVE_REFERENCES.md` は代表Drive参照一覧として存在
- `DRIVE_ID_EXPANSION_POLICY.md` が存在
- ルート直下に案件カルテが散っていない
- 日本語ファイル名がない

## 重要確認済み
- `clients/18_wse.md` → WSE
- `clients/19_reegle.md` → Reegle株式会社
- `clients/20_food_surprise.md` → 株式会社フードサプライズ
- `clients/21_ast.md` → 株式会社アスト
- `clients/25_hanayuki.md` → 株式会社花雪
