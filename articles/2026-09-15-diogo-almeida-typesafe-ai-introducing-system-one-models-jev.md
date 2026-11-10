---
name: "Introducing System One Models & Jev"
genre: "article"
url: "https://typesafe.ai/blog/introducing-system-one-models-and-jev"
author: "Diogo Almeida（TypeSafe AI）"
published: "2026-09-15"
flags: ["unverified"]
risk_notes: "速度・精度・確率の較正は独立に実測していない。候補投稿のPokémon Red以外のデモ、現行の利用条件およびモデル重みの配布条件は未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T05:49:02Z"
---

# Jevの公式技術解説：型付きの判断をアプリケーションに組み込む

## テーマ

- アプリケーションの状態と質問を入力し、あらかじめ定義した型の値と確率を受け取る。分類・採点・処理の振り分けを、受け取った値に応じてコードで分岐させる設計を紹介している。

## 著者の主張

- TypeSafe AIは、確率を並列に出力する方式と、判断の確率を較正するための学習法RLCDを採用したと説明している。公開時の掲載価格は入力100万トークンあたり0.042米ドルで、出力トークンは無料。

## 裏取り・注意点

- 公式記事のワークフロー評価は、同じ処理フローを各モデルに与え、参照モデルの出力確率の平均との一致を比較したもの。著者は評価課題を自社チームが作成したことと、公開した速度評価が主にサービスに近い米国西海岸からの計測だったことを明記している。
- Christian Mathiesenのプロジェクトページは、Pokémon Redで殿堂入りまで37時間40分、16,150回の判断、Jevの費用は約1.65米ドルだったと報告している。同ページは進行ガイドの利用も明記している。数値は実装者の報告であり、再実行による検証は行っていない。

## 出典

- TypeSafe AIの公式技術記事 https://typesafe.ai/blog/introducing-system-one-models-and-jev
- Christian Mathiesenのデモ記録 https://jev-pokemon.vercel.app/

## 変更履歴

- 2026-11-10: 初回登録
