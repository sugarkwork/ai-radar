---
name: "FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing"
genre: "article"
url: "https://arxiv.org/abs/2611.04303"
published: "2026-11-03"
flags: ["unverified"]
risk_notes: "論文の評価値は記載されたEasyOCR read-back protocolおよびScenePairの条件に基づく。別条件での性能は未確認。投稿文の説明は論文要約と一致するが、一般の写真で周囲が常に完全保持されることは確認していない。"
type: "article"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Machinedelusion/status/2118155587875942772"]
fetched_at: "2026-11-10T20:06:17Z"
---

# FlowTranslator: Training-Free In-Image Machine Translation with Flow-Based Editing

## テーマ

- 画像内機械翻訳（IIMT）において、画像中の文字を訳文に置き換え、周囲の視覚的文脈を保つ方法。

## 著者の主張

- FlowTranslatorはOCRモデルとLLMで翻訳プロンプトを作り、テキスト画像生成に基づく拡散モデルへ入力する学習不要の枠組み。文字領域のノイズ相関を軌道の初期に部分的に解き、途中で編集変位を増幅するRegion Coupling Release（RCR）とCoupling Expansion（CE）を導入する。論文はEasyOCR read-back protocolでPRIM BLEU 20.6、COMET 57.2、ScenePair写真の中国語訳で完全一致率40.1%を報告する。

## 裏取り・注意点

- arXivの論文要旨と投稿履歴を確認。記載のスコアはそれぞれ指定された評価条件での論文報告値であり、一般環境での性能保証ではない。

## 出典

- arXiv:2611.04303。Zhixian Li、Xingsong Ye、Yongkun Du、Yunyan Xiao、Yanglin Huang、Pinxuan Chen、Jiyu Zhuang、Cong Xu、Zhineng Chen。2026年11月3日投稿。

## 変更履歴

- 2026-11-11: 初回登録
