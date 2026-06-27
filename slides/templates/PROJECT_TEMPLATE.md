# PROJECT_TEMPLATE｜スライド案件テンプレート

新しいスライド案件を作るときは、以下の構成で `slides/projects/{client}_{theme}_{date}/` を作成する。

---

## 1. フォルダ命名

```txt
slides/projects/{client}_{theme}_{YYYYMMDD}/
```

例：

```txt
slides/projects/hanayuki_arao_20260703/
slides/projects/dadway_second_meeting_20260609/
slides/projects/t2_kpi_report_20260610/
```

---

## 2. 必須ファイル

```txt
slide_spec.md
storyboard.md
talk_script.md
decision_log.md
review_checklist.md
index.html
style.css
main.js
vercel_url.md
```

---

## 3. slide_spec.md テンプレ

```md
# slide_spec

## 用途
{商談プレゼン / 役員判断 / 商談FB / デモ導入 / インフォグラフィック}

## 対象
{誰に見せるか}

## 目的
{この資料で相手に何を判断・理解・行動してほしいか}

## 入力情報
- clients: {clients/xx_client.md}
- outputs: {outputs/xxx.md}
- Drive原本: {Drive ID / 未確認}
- 参照スライド: {GitHub path / Drive ID / 未確認}

## 前回商談の要点
- {要点1}
- {要点2}
- {要点3}

## 今回の勝ち筋
{商談ログから抽出した勝ち筋}

## 必ず伝えること
- {論点1}
- {論点2}
- {論点3}

## 避けること
- {誤解されやすい表現}
- {不要な深掘り}
- {商談上マイナスになる見せ方}

## 最終CTA
{次回商談 / 決裁者同席 / デモ確認 / 対象資料共有 / 見積依頼 など}
```

---

## 4. storyboard.md テンプレ

```md
# storyboard

## 1. 表紙
- 見出し：
- 伝えること：

## 2. 前回整理
- 見出し：
- 伝えること：

## 3. 課題整理
- 見出し：
- 伝えること：

## 4. 見えていない論点
- 見出し：
- 伝えること：

## 5. 提案の位置付け
- 見出し：
- 伝えること：

## 6. 具体イメージ
- 見出し：
- 伝えること：

## 7. 判断材料
- 見出し：
- 伝えること：

## 8. 次回アクション
- 見出し：
- 伝えること：
```

---

## 5. talk_script.md テンプレ

```md
# talk_script

## 1. 表紙
話すこと：

## 2. 前回整理
話すこと：

## 3. 課題整理
話すこと：

## 4. 見えていない論点
話すこと：

## 5. 提案の位置付け
話すこと：

## 6. 具体イメージ
話すこと：

## 7. 判断材料
話すこと：

## 8. 次回アクション
話すこと：
```

---

## 6. decision_log.md テンプレ

```md
# decision_log

## YYYY-MM-DD

### 判断
{今回のスライドで採用した方針}

### 理由
{商談ログ・案件状況・相手の温度感から見た理由}

### 採用した表現
{採用した言い回し}

### 捨てた表現
{捨てた表現と理由}

### 実装上の判断
{HTML/CSS/構成/画面遷移などの判断}

### 次回改善候補
{商談後に見るべき点}
```

---

## 7. review_checklist.md テンプレ

```md
# review_checklist

## 商談目的
- [ ] このスライドで相手に何を判断してほしいか明確
- [ ] 次回アクションにつながる

## 勝ち筋
- [ ] 商談ログから抽出した勝ち筋が入っている
- [ ] 汎用説明になっていない

## 構成
- [ ] サービス説明が早すぎない
- [ ] 相手の課題整理が先にある
- [ ] 1スライド1メッセージになっている

## 表現
- [ ] 社内共有に使える言い方になっている
- [ ] 決裁者が読んでも理解できる
- [ ] 誇張・断定が強すぎない

## 実装
- [ ] Vercelで表示確認済み
- [ ] PC/スマホで読める
- [ ] URL共有できる

## 資産化
- [ ] decision_logを記入した
- [ ] 案件カルテ7章へ追記した
- [ ] 再利用パターンがあればpatternsへ抽出した
```

---

## 8. vercel_url.md テンプレ

```md
# vercel_url

## Production URL
{URL}

## Preview URL
{URL}

## 最終確認日
YYYY-MM-DD

## 確認内容
- [ ] PC表示
- [ ] スマホ表示
- [ ] 文字崩れ
- [ ] 画像表示
- [ ] リンク動作

## 案件カルテ追記
- [ ] clients/{client}.md 7章へ追記済み
```

---

## 9. index.html 最小構成方針

- まずは静的HTMLでよい。
- 複雑なフレームワークは不要。
- スライド送りはキーボード操作・ボタン操作に対応する。
- 文字サイズは商談画面共有でも読めるサイズにする。
- 1スライド1メッセージを守る。

---

## 10. 完了条件

```txt
slide_specがある
storyboardがある
talk_scriptがある
decision_logがある
review_checklistが埋まっている
HTMLスライドが表示できる
Vercel URLが記録されている
案件カルテに履歴が残っている
```
