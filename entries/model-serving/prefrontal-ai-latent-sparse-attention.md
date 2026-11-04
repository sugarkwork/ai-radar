---
repo: Prefrontal-AI/latent-sparse-attention
name: Latent Sparse Attention (LSA)
genre: model-serving
url: https://github.com/Prefrontal-AI/latent-sparse-attention
author: Prefrontal AI
license: Apache-2.0
stars: 331
language: Python
created: 2026-10-27
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/_avichawla/status/2117578508918772134
sources:
  - https://arxiv.org/abs/2610.42147
  - https://x.com/QwenAIFans/status/2117537750689947650
forks: 39
open_issues: 5
commits_30d: 2
commits_90d: 2
commit_cadence: monthly
size_kb: 3761
archived: false
fetched_at: "2026-11-04T06:33:34Z"
---

# Latent Sparse Attention (LSA)

## 出来ること

- **超長文脈のための疎な注意機構**。キーを学習された潜在空間で階層的にクラスタリングし、各クエリは個々のキーではなく**クラスタの重心**を採点して、選んだ長距離キーだけを見る。FAISS を使ったクラスタベースのベクトル検索を attention の内側でやるイメージ。
- **D-LSA（蒸留）**: 学習済みモデルの indexer を蒸留して後付けする方式。GLM-5.3-Flash の 10M トークンで、そのモデル自身の疎な attention に対して **prefill 22.7倍・decode 4.6倍**。Qwen3.8-27B ではフル attention に対して **prefill 72.4倍・decode 42.5倍**（いずれも1層の計測）。
- **N-LSA（ネイティブ）**: next-token loss だけでゼロから学習する方式。フル attention と同等の精度で、128k トークン時の学習が1層あたり1.6倍速い。
- **attention カーネル自体は変えない**。LSA は「どのキーを読むか」だけを決める。
- 実装は SGLang のプラグイン。D-LSA（Flat / Tree / Training-Free の PCA 写像）、蒸留、N-LSA とベースライン（Full / SWA / NSA / PISA / Block Sparse）、精度・カーネル・end-to-end の評価を `lsa` コマンド1つで回せる。
- SGLang フォーク（`lsa-v0.1.0`）と Docker イメージ（`ghcr.io/sglang:lsa-v0.1.0`、Blackwell 用は `-b300`）を公開。

## 目的・背景

長文脈のコストは「KV キャッシュの保存量」と「注意の計算量」の両方で増える。LSA は後者を、学習された潜在空間でのクラスタ検索によって劣線形化する。論文 *Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention*（arXiv:2610.42147）の実装。2026-10-27 作成、11-03 時点で 331 star。

## 依存関係

- Python 3.12、`uv`
- SGLang フォーク（`Prefrontal-AI/sglang` の `lsa-v0.1.0` タグ）とその配布イメージ。10M トークン実行には context-parallel / long-context 対応が必要で、本家 SGLang では動かない
- CUDA 13.0.3 ベースのイメージ（B300 は専用タグ）
- 学習 extra は `causal-conv1d` をビルドするため CUDA ツールキット（nvcc）が必要

## 実行条件

- 論文の計測は **NVIDIA H200**。10M トークン級の実行には相応の GPU メモリとコンテナ環境が要る
- 公開されている倍率は**1層あたり**の値。モデル全体の高速化は層数・実装・バッチ条件で変わり、そのままは出ない（QwenAIFans の投稿も同じ注意をしている）
- 512k トークン未満ではほぼ損益分岐（フル attention と同等）で、長文脈で効く設計
- LSA はキーの「探し方」を安くするだけで、**KV キャッシュは文脈長に対して線形に増え続ける**。10M トークンではメモリ管理が次の課題になる
- 配布重み・蒸留マップの利用条件は各モデルのライセンスに従う

## 最短手順

```bash
git clone https://github.com/Prefrontal-AI/latent-sparse-attention.git
cd latent-sparse-attention
uv sync --locked --extra evaluation --extra training   # nvcc が無ければ --no-install-package causal-conv1d
uv run lsa --help

# 配信: SGLang フォークのイメージにこのリポジトリを入れ、
# 蒸留マップと HF キャッシュをマウントして起動する
```

## 変更履歴

- 2026-11-04: 初回登録（D-LSA / N-LSA、SGLang プラグイン時点）
