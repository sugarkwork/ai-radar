---
name: "D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding"
genre: "article"
url: "https://arxiv.org/abs/2611.06425"
published: "2026-11-04"
flags: ["unverified"]
risk_notes: "速度向上の数値は論文の著者らが記載した評価結果であり、独立した再現確認ではない。評価はQwen3-8B／32B、7ベンチマーク、greedy decodingなど論文記載の条件に基づく。"
type: "article"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119264905119285734"]
fetched_at: "2026-11-18T10:09:53.186011+00:00"
---

# D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding

## テーマ

- 投機的デコーディングで、ターゲットモデルの隠れ状態を使わずに候補トークンを生成する独立型拡散ドラフターD3Dを提案する論文。ドラフト生成とターゲットモデルの検証を並行させる非同期推論を扱う。

## 著者の主張

- 著者らは、ブロック単位の拡散学習と補助的な自己回帰学習でドラフターを訓練し、受理長への影響を基準にレイヤーを段階的に枝刈りすると説明している。論文の評価では、Qwen3-8BおよびQwen3-32Bをターゲットとした7ベンチマークで平均5.00倍／5.71倍のデコード速度向上を報告し、Qwen3-32BのGSM8Kでは7.48倍としている。これらは論文内の著者報告値。

## 裏取り・注意点

- arXiv本文の実験設定では、Qwen3-8B／32Bを対象に数学・コード生成・対話の7ベンチマークを評価し、Transformersバックエンド、greedy decoding、non-thinking modeを使用。推論実験にはH800 GPUを使用したと記載されている。本文には、ドラフト計算が検証時間内に隠れない場合や、準備済み候補のキャッシュがヒットしない場合には同期生成が必要になる旨も説明されている。ここで示した性能値は独立検証ではない。

## 出典

- arXiv論文ページ（要旨・公開日）: https://arxiv.org/abs/2611.06425
論文本文（手法・実験条件）: https://arxiv.org/html/2611.06425

## 変更履歴

- 2026-11-23: 初回登録
