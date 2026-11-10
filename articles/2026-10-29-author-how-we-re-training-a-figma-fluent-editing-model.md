---
name: "How we’re training a Figma-fluent editing model"
genre: "article"
url: "https://www.figma.com/blog/training-a-figma-fluent-editing-model/"
published: "2026-10-29"
flags: ["unverified"]
risk_notes: "比較結果はFigmaの社内評価で、独立した再現性は未確認。学習データに含まれる顧客コンテンツの具体的な範囲と利用条件、学習済みモデルやデータの入手・再利用条件、モデル単体の速度と費用は未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/neuronxwhite/status/2117856064104489123"]
fetched_at: "2026-11-10T10:49:12Z"
---

# Figmaのキャンバス編集モデルをどう訓練・評価するか

## テーマ

- 既存デザインの余白や色などを編集するモデルの事後学習。元のデザイン、合成した編集指示、成功した編集結果を組にし、Figmaのネイティブ形式で学習させる。

## 著者の主張

- Josh Clemmによると、大規模な教師モデルで編集案を作り、決定的な検証と視覚モデルによる判定で選別する。評価のフィードバックを使って編集案を修正できるようにした。
- Figmaは、25万件を超える例で学習した初期のLlama 3.3 70Bが、同社の編集タスクで当時の上位モデルに匹敵したと報告している。その後はQwenなどのベースモデルも採用し、教師あり微調整の汎化やサンプル効率の限界を踏まえて強化学習にも取り組んでいる。

## 裏取り・注意点

- 応用できるのは、出力構造の妥当性と見た目や指示への適合を分けて評価し、専門家の判断で評価器を調整する設計。性能比較はFigmaの社内評価に基づく。
- 記事は顧客のプライバシーと設定を尊重する方針に触れている。個々の顧客ファイルが実際に学習に使われたかは本文から確認できず、発見投稿の断定は裏付けられない。

## 出典

- [Figma公式ブログ、Josh Clemm、2026年10月29日](https://www.figma.com/blog/training-a-figma-fluent-editing-model/)

## 変更履歴

- 2026-11-10: 初回登録
