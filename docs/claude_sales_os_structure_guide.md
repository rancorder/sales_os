# Claude向け｜営業OS 構造理解ガイド

詳細な営業OS構造は `docs/claude_sales_os_structure_guide.md` を参照する。

## 0. この資料の目的

この資料は、Claude / Claude Code が `rancorder/sales_os` を正しく理解し、営業支援案件の分析・台本作成・報告書作成・GitHub更新を行うための運用ガイドである。

この営業OSは、単なる資料置き場ではない。  
案件ごとの営業知見・架電ログ分析・商談台本・改善パターン・判断履歴をGitHub上に蓄積し、Drive原本と連携させながら、AIが継続的に営業支援を行うための仕組みである。

---

## 1. 全体思想

営業OSの基本思想は以下。

```txt
Drive   = 原本置き場
GitHub  = 正本・判断・型・分析履歴
ChatGPT / Claude / Codex = 分析・更新エージェント
Word / PDF = 現場配布用
GitHub Actions = 構造監査
```

重要なのは、チャットやAIツールを「資料倉庫」にしないこと。

- 原本はDriveに置く
- GitHubには要約・判断・台本・分析・Drive参照IDを置く
- AIには「案件名＋やりたいこと」だけを渡す
- AIはGitHubの営業OS文脈を読み、必要なDrive原本を参照して作業する

---

## 2. なぜこの構造にしたか

従来の営業支援では、案件ごとに以下の問題が起きる。

```txt
過去資料がどこにあるか分からない
前回の判断がチャットに埋もれる
商談台本と実ログ分析が分離する
成功/失敗パターンが再利用されない
スマホでは重い作業ができない
```

営業OSでは、これを以下に変える。

```txt
Driveにログを入れる
↓
GitHubの案件カルテを読む
↓
_analysis_protocol / patterns に沿って分析する
↓
台本・報告・更新候補を作る
↓
GitHubにMD正本として蓄積する
↓
必要なものだけWord/PDF化して現場配布する
```

これにより、営業支援が「単発作業」ではなく「学習する営業資産」になる。

---

## 3. 正本と原本の分離

### 3.1 Driveに置くもの

Driveは原本置き場。

```txt
架電ログ原本
商談文字起こし
動画
VTT
CSV
Excel
PDF
Word
営業資料
顧客資料
個人情報を含む可能性があるもの
```

Driveには生データを置いてよい。

### 3.2 GitHubに置くもの

GitHubは正本置き場。

```txt
案件カルテ
分析結果MD
商談台本MD
架電フォロー台本MD
報告書MD
patterns
protocol
Drive参照ID
更新候補
判断履歴
```

GitHubには、生ログ・個人情報・電話番号・メールアドレス・顧客の機密原本を置かない。

### 3.3 Word / PDFにするもの

Word / PDFは現場配布用。

```txt
架電者に渡す台本
商談者に渡す台本
PM報告書
顧客提出用レポート
定例資料
```

WordやPDFは原則Driveに置き、GitHubにはMarkdown版またはDrive IDだけを残す。

---

## 4. sales_os リポジトリ構造

想定リポジトリ：

```txt
rancorder/sales_os
```

代表的な構造：

```txt
.
├── README.md
├── INDEX.md
├── CLAUDE.md
├── MANIFEST.md
├── DRIVE_REFERENCES.md
├── DRIVE_ID_EXPANSION_POLICY.md
├── CHECK_BEFORE_DELETE.md
├── SECURITY.md
├── FILENAME_POLICY.md
├── _research_protocol.md
├── _analysis_protocol.md
├── clients/
├── docs/
├── patterns/
├── prompts/
├── outputs/
├── tools/
└── .github/
```

---

## 5. 重要ファイルの役割

### README.md

営業OS全体の入口。  
リポジトリの目的、運用方針、基本構造を説明する。

### INDEX.md

案件一覧。  
各クライアントの入口として使う。  
Claudeはまず `INDEX.md` を見て対象案件を特定する。

### CLAUDE.md

Claude / Claude Code 向けの作業ルール。  
Claudeがこのリポジトリで作業する際の前提・禁止事項・更新方針を確認する。

### DRIVE_REFERENCES.md

全案件の代表Drive参照一覧。  
各案件につき、代表となるDrive file / folderを1件だけ管理する。

### clients/

案件カルテ置き場。  
各案件の正本はここにある。

例：

```txt
clients/27_generate_one.md
clients/08_t2_laboratory.md
clients/studio_tram/client_card.md
```

### patterns/

案件横断で再利用できる営業パターン置き場。

例：

```txt
patterns/followup_call_script_after_material_request.md
```

### prompts/

Claude / Codex / GPT に投げるためのプロンプト置き場。

### outputs/

個別案件の分析結果、台本、報告書、更新候補置き場。

例：

```txt
outputs/generate_one_material_request_followup_analysis_20260626.md
outputs/generate_one_material_request_followup_script_20260626.md
outputs/chat_extraction_updates/update_27_generate_one_material_request_followup_candidate.md
```

### tools/

検証スクリプト置き場。

例：

```txt
tools/validate_sales_os.py
```

### .github/

GitHub Actionsなどの自動検証設定。

---

## 6. 案件カルテの読み方

各 `clients/*.md` は、案件ごとの正本である。

典型構成：

```txt
## 0. AI起動プロンプト
## 1. 基本情報
## 2. 商材の核 / USP
## 3. 商談設計
## 4. 進捗ログ
## 5. 次の一手
## 6. 資料原本（Drive参照・増設可能）
```

Claudeは案件作業を開始する前に、必ず対象案件のカルテを読む。

### 6.1 代表Drive参照

案件の入口となるDrive参照。  
`DRIVE_REFERENCES.md` と整合している必要がある。

### 6.2 追加資料ID一覧

案件内の個別資料IDを管理する表。  
商談台本、架電ログフォルダ、SU定例資料、分析資料、台本MDなどをここに追記する。

---

## 7. 分析時の基本フロー

Claudeが案件分析を行うときは、以下の順で進める。

```txt
1. INDEX.mdで対象案件を確認
2. clients/{対象案件}.md を読む
3. 6章のDrive参照を確認
4. 必要なDrive原本を読む
5. _analysis_protocol.md または該当patternsに沿って分析
6. outputs/ に分析MD・台本MD・更新候補MDを作成
7. 必要なら clients/{対象案件}.md への追記候補を作成
8. validate_sales_os.py のルールに反しないか確認
```

---

## 8. 立ち上げ時の基本フロー

新規案件や情報が薄い案件は、`_research_protocol.md` を使う。

```txt
1. 顧客HP・資料・取材ログ・商談ログを読む
2. 商材の核を整理
3. ターゲット仮説を作る
4. 商談ストーリーを作る
5. 架電・商談で検証する論点を決める
6. clients/ にカルテ化する
```

---

## 9. 改善・分析時の基本フロー

既存案件の架電ログ・商談ログ・拒否ログ・資料請求ログを読む場合は、`_analysis_protocol.md` と `patterns/` を使う。

分析観点：

```txt
定量：
- 電話数
- 着電率
- 受付拒否率
- 対象者通話率
- 本人拒否率
- 本人資料請求率
- アポ率
- 不通率

定性：
- 何に反応しているか
- どこで落ちているか
- 誤認されているか
- 誰に刺さっているか
- 次回台本に入れるべき言い換え
```

出力形式：

```txt
■定性的な報告
■乖離している場合
原因：
改善：
対策：
```

---

## 10. ジェネレートワンで確立した最新運用例

### 10.1 背景

ジェネレートワン案件では、Driveに本人資料請求ログが格納された。

Claude/GPTは以下を行った。

```txt
Driveフォルダ確認
↓
架電ログ > 本人資料請求フォルダを確認
↓
9件のログを分析
↓
A/B/C/D分類
↓
勝ち筋・NGトークを抽出
↓
フォロー架電台本を作成
↓
Word化して現場配布
↓
Markdown版をGitHubに正本化
↓
汎用patternsへ横展開
```

### 10.2 生成されたMD

```txt
outputs/generate_one_material_request_followup_analysis_20260626.md
outputs/generate_one_material_request_followup_script_20260626.md
outputs/chat_extraction_updates/update_27_generate_one_material_request_followup_candidate.md
```

### 10.3 汎用化されたパターン

```txt
patterns/followup_call_script_after_material_request.md
```

### 10.4 得られた重要学習

```txt
本人資料請求者 = 高温リードとは限らない
資料請求 = 社内共有・判断保留・営業回避の可能性がある
「資料をご覧いただけましたか？」で入らない
「御社の場合、どの用途で見るのが近そうか」で入る
YouTube広告・動画制作などの誤認は即座に修正する
二次商談は一般説明ではなく「御社向け企画骨子案」の場にする
```

---

## 11. Claudeがやってよいこと

Claudeは以下を行ってよい。

```txt
案件カルテを読む
Drive参照IDをもとに必要資料を読む
架電ログを分析する
商談文字起こしを分析する
台本MDを作る
報告MDを作る
clients更新候補を作る
patternsへ横展開する
promptsを作る
Word/PDF化用の原稿を作る
```

---

## 12. Claudeが勝手にやってはいけないこと

Claudeは以下を勝手にやってはいけない。

```txt
Drive原本をGitHubへコピーする
電話番号・メールアドレス・個人名をGitHubに残す
CSV / Excel / PDF / Word / 動画 / VTTなどの原本をGitHubへ入れる
クライアントカードの代表Drive IDを根拠なく変更する
古いチャット情報だけで正本を上書きする
未確認情報を確定情報として書く
分析していないログを「分析済み」とする
```

不明点は `{未確認}` と明記する。

---

## 13. ファイル作成ルール

### 13.1 ファイル名

- ASCII
- 小文字
- スネークケース
- 日付を入れる
- スペース、全角、括弧を避ける

良い例：

```txt
outputs/generate_one_material_request_followup_analysis_20260626.md
outputs/generate_one_material_request_followup_script_20260626.md
```

悪い例：

```txt
ジェネレートワン 資料請求分析.md
本人資料請求（最新）.md
```

### 13.2 GitHubに置かない拡張子

原則として以下はGitHubに置かない。

```txt
.csv
.xlsx
.xls
.docx
.pdf
.mp4
.webm
.vtt
```

これらはDriveに置き、GitHubにはDrive IDと要約を置く。

---

## 14. GitHub更新候補の作り方

直接 `clients/*.md` を更新する前に、まず更新候補を作る。

置き場所：

```txt
outputs/chat_extraction_updates/
```

例：

```txt
outputs/chat_extraction_updates/update_27_generate_one_material_request_followup_candidate.md
```

中身：

```txt
## 4章 進捗ログ 追記候補
## 5章 次の一手 追記/修正候補
## 6.2 追加資料ID一覧 追記候補
## 注意
```

これにより、案件カルテに何を反映するかレビューできる。

---

## 15. 検証ルール

更新後は、可能なら以下を実行する。

```bash
python tools/validate_sales_os.py
```

GitHub Actionsの `Validate sales_os` が通れば、構造としてはOK。

validatorは主に以下を見る。

```txt
ルート直下に余計なファイルがないか
clientsの案件カードが揃っているか
Drive参照IDとDRIVE_REFERENCES.mdが整合しているか
危険な原本拡張子が混ざっていないか
ファイル名が安全か
```

---

## 16. スマホ運用

この営業OSは、スマホ運用を前提にできる。

スマホでやること：

```txt
Driveにログや資料を入れる
ChatGPT / Claudeに案件名と依頼を投げる
出てきた分析・台本・報告を確認する
必要ならGitHubへMD反映する
```

スマホでやらなくてよいこと：

```txt
大量ファイル整理
Word整形
GitHub構造整理
台本のゼロから作成
```

つまり、スマホでは素材投入と判断だけ行い、重い整形や分析はAIに任せる。

---

## 17. Claudeへの標準依頼文

### 17.1 架電ログ分析

```txt
sales_osの構造を前提に、{案件名} の案件カルテを読み、
Driveの架電ログを分析してください。

対象は {対象ログ} です。

以下を出してください。
1. 定量サマリー
2. 定性的な報告
3. 落ちている理由
4. 改善すべきトーク
5. 次回台本の修正案
6. clients更新候補
7. patternsへ横展開できる学び

GitHubには、個人名・電話番号・メールアドレス・架電ログ原文を残さないでください。
```

### 17.2 商談文字起こし分析

```txt
sales_osの構造を前提に、{案件名} の案件カルテを読み、
Driveの商談文字起こしを分析してください。

以下を出してください。
1. 商談要約
2. 顧客課題
3. 刺さった訴求
4. 落ちた訴求
5. 二次商談に進める条件
6. 商談者へのFB
7. 次回商談ストーリー
8. clients更新候補
```

### 17.3 台本作成

```txt
sales_osの構造を前提に、{案件名} の案件カルテと関連patternsを読み、
{用途} 向けの台本を作成してください。

現場配布用にWord化できる構成で、
冒頭、確認質問、分岐、切り返し、クロージング、NGトーク、架電者注意点まで作成してください。

GitHubに入れる場合はMarkdown版のみとし、Word本体はDrive保管前提にしてください。
```

---

## 18. 最重要ルール

Claudeは、営業OSを「ファイル置き場」ではなく「営業判断の正本」として扱うこと。

常に以下を守る。

```txt
原本はDrive
正本はGitHub
作業指示はチャット
現場配布はWord/PDF
構造監査はGitHub Actions
```

そして、各案件から得た学びを必ず `patterns/` に蒸留する。

これにより、営業OSは案件ごとに強くなり、次の案件で再利用できる。
