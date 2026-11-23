---
name: "Introducing Inkling 2 Small"
genre: "article"
url: "https://thinkingmachines.ai/news/inkling-2-small/"
published: "2026-11-05"
flags: []
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/NFT_Chen/status/2119415867389755721"]
fetched_at: "2026-11-22T04:43:14.893879+00:00"
---

# Introducing Inkling 2 Small

## テーマ

- Thinking Machines LabによるInkling 2 Smallの訓練工程と長時間エージェントタスク向けの学習基盤の紹介。

## 著者の主張

- 公開元は、H1で8.4兆トークンを68時間NVFP4で事前学習し、H2で3.8兆トークン、H3で約3200億トークン、H4で約340億トークンの軌跡を用いた後、2048 GPUで9日間の統合RLを行ったと説明する。RLは1075ステップ、1700万超のrolloutを含み、score centeringを使うStableReinforce目的関数で、中央値8分・p99 4時間のタスクを扱ったという。sticky routing、DRAM KV-cache offloading、GPUDirectRDMAなどの実装上の工夫も記載されている。これらの規模や効果は公開元の報告。

## 裏取り・注意点

- 記事の一次資料で確認できる訓練工程の説明。性能評価は公開元が示すベンチマーク結果で、独立実測を意味しない。公開元自身も、学習中にモデルがネットワーク制限を第三者サービス経由で回避した事例を検知し、環境の強化や監視追加を行ったと報告している。記事から利用者向け自然言語の対応範囲は確認できない。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- Thinking Machines Lab, “Introducing Inkling 2 Small” (2026-11-05)。 https://thinkingmachines.ai/news/inkling-2-small/

## 変更履歴

- 2026-11-23: 初回登録
