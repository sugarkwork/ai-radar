---
repo: JakeATX/llamAmpere
name: llamAmpere
genre: model-serving
url: https://github.com/JakeATX/llamAmpere
license: MIT
language: C++
created: 2026-09-07
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/ai_hakase_/status/2117527965277773956
flags: []
risk_notes: ""
stars: 221
forks: 30
open_issues: 13
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 391373
archived: false
fetched_at: "2026-11-04T22:50:48Z"
last_release: v0.6.2
last_release_at: 2026-11-01
---

# llamAmpere

## 出来ること

- **Ampere 世代の NVIDIA GPU（RTX 3090 / 3090 Ti など）向けに最適化した llama.cpp のフォーク**。
- 独自の量子化形式「AmperInteger+」を実装し、約2.3bpw まで圧縮しながら BF16 相当の精度を保つとしている。v0.6.2 で2.5bit の小数型（type 118、`aif25_u`）が加わり、公開されている 2.3bpw の 27B モデルを読み込める。
- 埋め込みテーブルをメインメモリに逃がすことで、**12GB VRAM でも 200K トークン超のコンテキスト**を扱える構成を用意している。
- 例として、Qwen3.8 の 100K トークン生成で 110+ tok/s（temperature 1）という測定値を挙げている。

## 目的・背景

2026-09 公開、★216、v0.6.2。llama.cpp の量子化は世代ごとのGPU特性（Ampere の INT8/FP8 周り）を活かしきれていない部分があり、RTX 30 系のユーザー向けに KV キャッシュ量子化とメモリ配置を振り直したもの。

## 依存関係

- CUDA 12 以降の NVIDIA ドライバとツールキット（`nvcc`）、CMake、git、C++ コンパイラ
- GGUF 形式のモデル（初回起動時に取得する構成では約9.1GB）
- Linux（v0.6.2 のクイックスタートは Linux 前提）

## 実行条件

- **Ampere 世代（RTX 30 系）向け**。Ada / Blackwell では恩恵が限られる可能性がある。v0.6.2 の推奨構成は 24GB の RTX 30 系1枚・200K コンテキスト（Swift 1.5 27B を 2.3bpw で）。他の世代は `CMAKE_CUDA_ARCHITECTURES` を変える（未検証）。
- 12GB VRAM 構成はメインメモリ側の余裕が必要（埋め込みテーブルを逃がすため）。
- リポジトリは約391MB（ビルド成果物を含む）。

## 最短手順

```bash
git clone -b v0.6.2 https://github.com/JakeATX/llamAmpere.git
cd llamAmpere
cmake -S . -B build-sm86 -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON \
  -DCMAKE_CUDA_ARCHITECTURES=86 -DLLAMA_BUILD_BORINGSSL=ON
cmake --build build-sm86 -j8 --target llama-server
./build-sm86/bin/llama-server \
  -hf jakeatx/qwen3.8-27b-Swift1.5-Uncensored-ATX-AI2 \
  -c 204800 -ngl 99 -fa on -b 4096 -ub 1024 --parallel 1 --jinja --no-context-shift \
  -ctk sjkvarn3 -ctv sjkvarn2 --sjkvarn-body-type auto \
  --spec-type draft-mtp-adaptive --spec-draft-n-min-adaptive 3 --spec-draft-n-max 4 \
  --spec-draft-p-min 0 --spec-mb-mtp
# http://127.0.0.1:8080 で待受（OpenAI 互換 API）
```

Flash-Next 用の `scripts/flash-next-server.sh` は `--moe-skip`（ルーター重みの15%を上限に、カード外の低重みエキスパートを間引き、最初の5経路は保護）が既定で、**出力が変わる**。`--exact` を付けると間引きと mb-MTP をまとめて切る。

## 変更履歴

- 2026-11-04: 初回登録（★216 / v0.6.2 / MIT / 30日100+コミット）、ビルド・起動コマンドと --moe-skip の注意を追記（v0.6.2）
