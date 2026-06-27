# SOURCE_REPOS｜既存GitHubスライド資産の吸収元

このファイルは、営業OSのスライド開発レイヤーへ吸収する既存GitHub資産のメモである。

## 確認済みリポジトリ

### rancorder/wse_presentation

用途：WSE向けHTMLプレゼン資料の既存資産。

吸収する観点：

- HTMLプレゼンをGitHub管理する運用
- Vercel公開を前提とした静的スライド構成
- 商談資料をWebスライド化する発想
- 画像・動画・スライドを組み合わせたプレゼン表現

営業OSへの取り込み方：

```txt
個別コードをそのまま移植するのではなく、
「HTMLスライドを営業資料として開発する型」として吸収する。
```

---

### rancorder/cba

用途：CBA系HTMLスライド/プレゼン資産。

確認された特徴：

- `present.html` 更新履歴あり
- `index.html` 更新履歴あり
- Vercel設定更新履歴あり
- 静的HTMLを公開資料として扱う運用に近い

吸収する観点：

- `present.html` のような商談用単体HTML
- `index.html` を入口にする構成
- Vercel設定調整の実務知見
- GitHub更新 → 公開確認 の短い制作サイクル

営業OSへの取り込み方：

```txt
営業OSでは、present.html単体運用を発展させ、
slide_spec / storyboard / decision_log まで含めた
「判断履歴つきスライド開発」に拡張する。
```

---

### rancorder/cba_new

用途：CBA系の新構成候補。

吸収する観点：

- 既存CBA資料の再構築・新設計
- 旧資料と新資料の差分管理
- スライド構成の作り直しパターン

営業OSへの取り込み方：

```txt
既存資料のリニューアル案件では、
old/current/new の差分を decision_log に残す。
```

---

## 吸収方針

営業OSには、既存リポジトリの完成物を丸ごと混ぜない。

代わりに、以下を吸収する。

```txt
1. GitHubでHTMLスライドを管理する型
2. VercelでURL確認する型
3. index.html / present.html を入口にする型
4. 商談資料をWebプロダクトとして改善する型
5. 実装履歴を判断履歴へ昇格させる型
```

## 吸収しないもの

```txt
顧客固有の素材
重い画像/動画
商談ごとの機密情報
古いHTMLの細部デザイン
使い捨ての実装断片
```

## 営業OSでの標準化

今後のスライド案件は、既存リポジトリのようにHTMLを作るだけで終わらせず、必ず以下をセットにする。

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

## 一言

```txt
既存GitHubスライド資産は、完成物としてではなく、
「スライドを高速に開発して公開する作法」として営業OSへ吸収する。
```
