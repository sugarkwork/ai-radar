---
name: "LoopVQ: Sub 1-bit KV Cache Quantization for Looped Transformers"
genre: "model-serving"
url: "https://arxiv.org/abs/2611.05304"
author: "Minsoo Cheong, Sungjoo Yoo"
published: "2026-11-03"
flags: ["unverified"]
risk_notes: "評価値は著者の報告。独立再現、評価対象外のモデルや実行環境への一般化、依存コンポーネントとモデル重みの個別利用条件は未検証。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/mscheong01/status/2117295415062401324"]
fetched_at: "2026-11-10T05:56:35Z"
---

# LoopVQ — ループ型TransformerのKVキャッシュを1ビット未満に量子化

## テーマ

- 同じ層を繰り返し使うループ型Transformerでは、各ループ段が個別にKVを保持する。LoopVQは複数の連続するループ段のチャネルをまとめ、16または32要素を1つの8ビット索引で表す。モデル重みを固定し、量子化前後の出力分布のKLダイバージェンスを最小化するよう、モデルごとにコードブックを調整する。

## 著者の主張

- 著者の評価では、0.5ビット/要素のLoopVQが比較対象のCQとTaSQを上回った。0.25ビットではLoopVQ単独の長い推論で精度低下が目立ち、TaSQ併用で改善した。
- SGLangの専用カーネルを使った著者の測定では、RTX 6000 Ada 1枚でOuro-1.4B-Thinkingの32Kトークン時のデコード遅延がBF16の約半分になった。ピーク配信スループットはBF16比でOuro-1.4B-Thinkingが最大4.3倍、Ouro-2.6B-Thinkingが最大6.1倍だった。

## 裏取り・注意点

- 論文の第5.3節と付録D.2で測定条件を確認した。32～64倍はBF16と量子化索引の公称ビット幅の比。実装ではコードブックを使い、先頭8トークンと直近64トークンをBF16で保持する。TaSQ併用ではキーのスケール情報も保持する。
- Ouro-2.6B-ThinkingではプリフィルがBF16比で5～9%遅かった。ピーク値はGPUとリクエスト条件に依存し、独立再現は行っていない。
- 公式コードはApache-2.0で公開され、第三者コンポーネントには元の条件が適用される。論文とコードは公開閲覧できる。GPU実行費用とモデル重みの個別条件は未確認。

## 出典

- arXiv書誌・初回投稿日 https://arxiv.org/abs/2611.05304
- 著者の論文本文・実験条件 https://arxiv.org/html/2611.05304v1
- 著者のプロジェクトページ https://mscheong01.github.io/loopvq/
- 公式実装・README・ライセンス https://github.com/mscheong01/LoopVQ

## 変更履歴

- 2026-11-10: 初回登録
