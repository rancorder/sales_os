# CHECK_BEFORE_DELETE｜GPTプロジェクト削除前チェック

GPTプロジェクトを消す前に、GitHub上で以下を確認する。

## 1. ルート直下の構造

ルート直下に案件カルテが散っていないこと。

OK:

```txt
README.md
INDEX.md
CLAUDE.md
clients/
docs/
patterns/
prompts/
outputs/
tools/
```

NG:

```txt
21_ast.md
20_food_surprise.md
08_t2_laboratory.md
call_kpi_analysis_format.md
architecture.md
```

## 2. 案件ファイルの対応確認

GitHubで以下を開いて、先頭行が一致すること。

| パス | 先頭行 |
|---|---|
| clients/18_wse.md | # 案件カルテ｜ワールドシステムエンジニアリング有限会社（WSE） |
| clients/19_reegle.md | # 案件カルテ｜Reegle株式会社 |
| clients/20_food_surprise.md | # 案件カルテ｜株式会社フードサプライズ |
| clients/21_ast.md | # 案件カルテ｜株式会社アスト |
| clients/25_hanayuki.md | # 案件カルテ｜株式会社花雪 |

## 3. Drive原本

Google Drive側に以下が残っていること。

- 商談動画
- 文字起こし原本
- SU定例資料
- SCデータ
- 顧客提供資料

この3点がOKなら、GPTプロジェクトは削除してよい。
