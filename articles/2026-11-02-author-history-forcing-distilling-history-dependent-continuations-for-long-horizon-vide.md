---
name: "History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models"
genre: "video-gen"
url: "https://arxiv.org/abs/2611.02782"
published: "2026-11-02"
flags: ["unverified"]
risk_notes: "性能値は論文著者らの評価結果であり、独立検証は未確認。投稿文の「minute-long clips」は論文の60秒評価を指すが、実用環境で同様の一貫性が得られることまでは示さない。"
type: "article"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Machinedelusion/status/2118074050539122800"]
fetched_at: "2026-11-10T17:12:19Z"
---

# History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models

## テーマ

- 長時間の自己回帰動画生成において、画面外に出た対象や場面が再登場した際の一貫性を改善するための蒸留手法「History Forcing」を提案する研究。

## 著者の主張

- 履歴情報のある教師予測と履歴情報のない教師予測との差分を使い、蒸留時のスコアまたは速度予測を補正する。著者らは、1.3Bモデルで15秒動画のVBench品質スコア85.07、60秒動画のVBench-Long集約スコア79.82を報告している。画面外世界モデリングでは、PlayWorldのEvolution Qualityが2.35から2.70に、MemoBenchのObject Consistencyが58.43から62.18に改善したと報告している。

## 裏取り・注意点

- arXivの要旨で手法と評価値を確認。数値は著者らが報告した実験結果であり、独立検証や一般的な利用環境での効果はこの資料だけでは確認できない。

## 出典

- arXiv論文ページ。提出日：2026-11-02。

## 変更履歴

- 2026-11-11: 初回登録
