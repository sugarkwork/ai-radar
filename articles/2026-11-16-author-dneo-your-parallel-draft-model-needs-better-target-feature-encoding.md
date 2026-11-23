---
name: "DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding"
genre: "article"
url: "https://www.alphaxiv.org/pdf/2611.21925"
published: "2026-11-16"
flags: ["unverified"]
risk_notes: "最大30%の高速化は著者らがQwen3-4B、H100、記載されたベンチマークと推論設定で報告した結果。別のモデルや環境で同じ効果が得られるかは未確認。対応言語について論文に明記が見当たらず不明。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/NeuralArch1tect/status/2123117414690718100"]
fetched_at: "2026-11-19T03:07:45.312773+00:00"
---

# DNeo: Your Parallel Draft Model Needs Better Target Feature Encoding

## テーマ

- 並列ドラフターを用いる speculative-diffusion decoding の設計。

## 著者の主張

- 著者らは、既存方式の特徴エンコーディングにおける表現の混合、過去の棄却提案を使わないこと、対象モデルの層を一様に選ぶことを課題として挙げ、Mixture-of-Features Attention（MoFA）、棄却メモリ、非一様な層選択などを備えるDNeoを提案している。論文はQwen3-4Bを使った評価で、DFlash-2より最大30%速い生成と、バッチサイズ32で16%高いスループットを報告している。これらは論文の実験条件での著者報告。

## 裏取り・注意点

- arXiv掲載の論文本文で手法と評価の記述を確認。比較結果はQwen3-4Bを用いた評価であり、他の対象モデルや実運用環境への一般化はこの資料だけでは確認できない。論文は、speculative decodingの検証が対象モデルの分布を保つ理論的性質を説明している。対応言語は論文に明記されていないため不明。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- 論文PDF（一次資料）: https://www.alphaxiv.org/pdf/2611.21925

## 変更履歴

- 2026-11-23: 初回登録
