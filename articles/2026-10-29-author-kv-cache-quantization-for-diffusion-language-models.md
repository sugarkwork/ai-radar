---
name: "KV Cache Quantization for Diffusion Language Models"
genre: "article"
url: "https://arxiv.org/abs/2610.39853"
published: "2026-10-29"
flags: ["unverified"]
risk_notes: "ベンチマーク結果は著者報告で、独立再現は未実施。実装コードの公開状況と利用条件、実環境での速度・メモリ削減量は未確認。"
type: "article"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/HEI/status/2117341227368497627"]
fetched_at: "2026-11-10T08:48:26Z"
---

# KV Cache Quantization for Diffusion Language Models

## テーマ

- 拡散言語モデルでは、マスクされたトークンが確定するたびに双方向の表現が変わり得る。そのため、前の復号ステップから再利用したKVキャッシュは、量子化前から全再計算の結果とずれることがある。

## 著者の主張

- TRACEでプロンプトと回答の組からトークンが順次確定する軌跡を再構成し、量子化の較正に使う。dLLM-KVQは、その軌跡をもとに各層で高精度のまま保持するキーを選び、値は低ビットで量子化する。
- 著者はLLaDAとDreamをGSM8K、HumanEval、MATH、MBPPで評価し、報告された4ビット・2ビットのprefix／dual cache設定で、比較した量子化手法の中で最高の平均スコアを得たと報告している。

## 裏取り・注意点

- 本文の付録に、Fast-dLLMのキャッシュ再利用を前提としたKIVI・KVQuantの適応方法と、TRACEの較正手順が記載されている。スコアは著者報告で、独立再現や実環境での速度・メモリ削減量の確認は行っていない。
- arXivのHTML本文にはCC BY 4.0と表示されている。実装コードの公開状況・利用条件は未確認で、較正素材を再配布する場合は元データの利用条件を確認する必要がある。

## 出典

- [arXivの要旨と投稿履歴](https://arxiv.org/abs/2610.39853)
- [arXivのv1本文と付録](https://arxiv.org/html/2610.39853v1)

## 変更履歴

- 2026-11-10: 初回登録
