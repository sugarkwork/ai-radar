---
repo: hao-ai-lab/FastVideo
name: FastVideo
genre: video-gen
url: https://github.com/hao-ai-lab/FastVideo
license: Apache-2.0
language: Python
created: 2024-10-24
updated: "2026-11-08"
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/haoailab/status/2117704073248174180
flags: []
risk_notes: ""
stars: 4799
forks: 520
open_issues: 141
commits_30d: 74
commits_90d: 100
commit_cadence: "daily"
size_kb: 440084
archived: false
fetched_at: "2026-11-09T21:44:50Z"
last_release: "v0.2.0"
last_release_at: "2026-06-04"
---

# FastVideo

## 出来ること

- 動画生成モデルの**推論高速化とポストトレーニング**をまとめたフレームワーク。distillation・量子化・並列化を同じインターフェースで扱う。
- MiniMax H3 Flex（Pika Labs がオープンソース化した H3 系）を FastVideo 上で動かせる。公式のオープンソース推論コードと比べて**最大7倍高速**とされ、480p・5秒の動画＋音声を NVIDIA GB200 1枚で 5.8 秒で生成したと報告している。
- 学習側のコードも同梱（ポストトレーニング、蒸留）。
- Cosmos 2.5 Text2World のパイプラインも用意されている。全 DiT 共通の Hooks API とレイヤー単位オフロードを備え、v0.2.0 で FSDP 推論は既定で無効になった。
- モデル実装は diffusers 系を土台にしており、H3 以外の動画モデルにも同じ最適化を適用できる構成。

## 目的・背景

hao-ai-lab（UCSD の Hao AI Lab）による動画生成の高速化研究リポジトリ。2024-10 作成、v0.2.0。元は動画拡散モデルの推論最適化が出発点で、現在は「推論＋ポストトレーニング」を一つの枠にまとめている。2026-11 に H3 Flex 対応を追加したことで、ローカル動画生成の実用速度に直結する選択肢になった。

## 依存関係

- Python、PyTorch、CUDA（GPU 必須）
- diffusers 系のモデル実装
- モデル重みは別途取得（Hugging Face）

## 実行条件

- NVIDIA GPU が必須。H3 Flex の測定値は GB200 1枚での数字で、コンシューマGPUではそのままの速度は出ない。
- 動画モデル用の VRAM とディスク（重みが大きい）。
- Linux 前提の構成（CUDA ドライバ、FlashAttention 系の依存）。
- マルチ GPU で FSDP 推論を使う場合は `use_fsdp_inference=True` を明示する（既定は無効）。

## 最短手順

```bash
git clone https://github.com/hao-ai-lab/FastVideo
# README の手順で CUDA 環境を用意し、H3 Flex の重みを取得
```

## 変更履歴

- 2026-11-04: 初回登録（★4,777 / v0.2.0 / Apache-2.0 / 30日100+コミット）。H3 Flex を FastVideo で動かし最大7倍高速・480p 5秒を5.8秒で生成という主張（GB200 1枚、著者計測）、Cosmos 2.5 Text2World と Hooks API・レイヤー単位オフロードを追記（v0.2.0）
