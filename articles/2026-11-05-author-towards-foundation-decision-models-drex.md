---
name: "Towards Foundation Decision Models: Drex"
genre: "article"
url: "https://arxiv.org/pdf/2611.07854"
published: "2026-11-05"
flags: ["unverified"]
risk_notes: "ベンチマークスコアと183 msの応答時間は論文の報告値であり、ここでは独立再現していない。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119327568226636054"]
fetched_at: "2026-11-19T07:14:09.708336+00:00"
---

# Towards Foundation Decision Models: Drex

## テーマ

- 選択肢、はい・いいえ判定、順序尺度の採点に対して、テキストを逐次生成せず選択肢上の確率分布を返す「decision model」ファミリー Drex の技術報告。

## 著者の主張

- 著者らは、8B、9B、35B（3B active）、27Bパラメータの4モデルを報告し、教師ありファインチューニングと adjusted feedback による強化学習（RLAF）を組み合わせたと述べる。論文記載の評価では、Drex Max は Decision Index 0.4.1 の公開スイートで67.52、典型的なリクエストの応答時間は183 ms。これらは論文中の著者報告値。

## 裏取り・注意点

- 論文本文では、モデル群の仕様、評価設定、アブレーション、比較結果を確認できる。arXiv要旨は評価結果を示すが、ここではベンチマークや応答時間の独立再現をしていない。モデル重みと推論コードの案内も論文に記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 出典

- arXiv論文: https://arxiv.org/pdf/2611.07854
arXiv書誌ページ: https://arxiv.org/abs/2611.07854

## 変更履歴

- 2026-11-23: 初回登録
