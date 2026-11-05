---
type: model
model: higa2515/Qwen3.8-27B-QSA-GGUF
name: Qwen3.8-27B QSA（Q8_0 GGUF + ネイティブランタイム）
genre: model-serving
url: https://huggingface.co/higa2515/Qwen3.8-27B-QSA-GGUF
author: higa2515（@_ryu15_）
license: Apache-2.0
base_model: [higa2515/Qwen3.8-27B-QSA-BF16, Qwen/Qwen3.8-27B]
format: gguf
size: "Q8_0 本体 29.3GB ＋ mmproj F16 0.93GB ＋ ランタイム同梱アーカイブ"
downloads: 14
likes: 7
created: 2026-11-04
updated: 2026-11-04
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/LiLensss/status/2118098612676952299
sources:
  - https://huggingface.co/higa2515/Qwen3.8-27B-QSA-BF16
  - https://github.com/kuraneko1/Qwen3.8-27B-QSA-llama.cpp
  - https://arxiv.org/abs/2608.30320
flags: [unverified]
risk_notes: "prefill約2倍・decode 45+ tok/s は作者のX投稿の数値で、モデルカードに計測条件の記載が無い。stock llama.cpp では動かず、同梱の改造ランタイム（Linux x86_64 / sm70）か自前ビルドが必須。"
pricing: free
pricing_detail: "重み無料（Apache-2.0）"
signup_required: false
---

# Qwen3.8-27B QSA（Q8_0 GGUF + ネイティブランタイム）

## 出来ること

- **Qwen3.8-27B に QSA（Qwen Sparse Attention）を後付けしたモデルの Q8_0 GGUF**。公式の Qwen4 系で使われる疎注意の仕組みを、先に 27B へ移植したもの。
- QSA は**学習済みの圧縮インデクサで、4トークン単位のブロックを選ぶ**方式。この27B移植では、16層の full-attention 層が固定 K=2,048＋現在ブロックを使い、残り48層の Gated DeltaNet は元の構成のまま。
- **KV キャッシュは圧縮しない**。全 KV エントリは確保されたままで、QSA が減らすのは注意の計算量と KV の読み出し量（この点は紹介投稿の「KVを粗く削っていない」という説明と整合するが、メモリが減るわけではない）。
- テキスト・画像・動画の QSA、M-RoPE、MTP（最大2ドラフトトークン）、prefix-cache の再利用に対応する**改造 llama.cpp エンジン**同梱。
- ランタイム同梱のアーカイブに、パッチ済みソース・サーバー・共有ライブラリ・起動スクリプト・ビルド手順が入る。
- BF16 の元重み（`higa2515/Qwen3.8-27B-QSA-BF16`）も別途公開。元の18シャードは byte-for-byte で Qwen3.8-27B と同一で、**FP32 インデクサ 52,434,944 パラメータ**だけを追加している。

## 目的・背景

Qwen4 の公式リリース前に、その中核とされる QSA を Qwen3.8-27B へ逆移植したコミュニティ研究。インデクサは長さ16,384・マルチモーダル混在50%・合成OCR/表/図形タスクで300ステップ学習。バックボーン・視覚エンコーダ・投影層・MTP の重みは学習で変えていない。作者は V100 32GB×2 環境（@_ryu15_）。2026-11-04 公開。

## 収録ファイル

- `Qwen3.8-27B-QSA-Q8_0.gguf` — 29.3GB（Q8_0 本体行列、FP32 インデクサ、MTP テンソル保持）
- `mmproj-Qwen3.8-27B-QSA-F16.gguf` — 0.93GB（視覚/投影層。未変更）
- `qsa27b-linux-x86_64-sm70.tar.gz` — 改造ランタイム（サーバー、共有ライブラリ、パッチ済みソース、launcher、ビルド手順）
- `SHA256SUMS` / `release-manifest.json` — 完全性ハッシュと来歴

## 実行条件

- **stock llama.cpp では動かない**。同梱ランタイムか、`kuraneko1/Qwen3.8-27B-QSA-llama.cpp` のソースビルドが必要
- 同梱バイナリは **Linux x86_64 / NVIDIA sm70** 向け。作者の検証構成は V100-PCIE 32GB＋PG500 32GB の2枚、driver 580.178.04、CUDA 12.9、layer split 1:1、FP16 KV、context 262,144、batch 2,048、ubatch 512、MTP max draft 2
- 他の GPU では自前ビルドとメモリ設計が必要。NVIDIA ドライバと CUDA 12 ライブラリは各自用意（アーカイブに含まれない）
- 既定の待受は `127.0.0.1:8091`。サービスは自動登録されない
- prefix 再利用は再起動をまたがない。MTP の lag/async は無効
- 品質確認（BF16 参照、Q8_0 ネイティブではない）: 32,766トークンの text PPL が dense 7.072960 → QSA 7.071384（比 0.99978）、自作50問の4択 DocVQA が 50/50 で同一
- **速度の数値（128K prefill 1,598→3,114 tok/s、decode 45+ tok/s）は作者のX投稿によるもので、モデルカードには計測条件が無い**。独立検証は未確認
- BF16 の Transformers 実装は**正しさの参照用**で、テキスト以外は dense attention に落ち、MTP も未実装。速度は出ない

## 使い方

```bash
sha256sum -c SHA256SUMS
tar -xzf qsa27b-linux-x86_64-sm70.tar.gz
QSA_MODEL_DIR="$PWD" ./qsa27b-runtime/launch.sh
# 既定: http://127.0.0.1:8091
```

## 変更履歴

- 2026-11-04: 初回登録（⚑ 速度数値は作者投稿のみ）
