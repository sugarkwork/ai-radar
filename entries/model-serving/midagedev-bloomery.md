---
repo: "midagedev/bloomery"
name: "bloomery"
genre: model-serving
url: "https://github.com/midagedev/bloomery"
license: "MIT"
stars: 60
language: "Rust"
created: "2026-09-19"
updated: 2026-11-04
added: "2026-11-04"
first_seen: "2026-11-04"
source_post: "https://x.com/dextune/status/2117900921984401793"
sources: []
flags: []
risk_notes: ""
forks: 7
open_issues: 51
size_kb: 90109
archived: false
last_release: v0.3.12
commits_30d: 100
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-04T22:53:31Z"
last_release_at: 2026-11-03
---

# bloomery

## 出来ること

- GPU に載りきらない MoE モデルを、GPU とホスト RAM に分割して推論するサーバー。**使用頻度の高いエキスパートを実行中に GPU へ移す**ため、全エキスパートを VRAM に置く必要がない。
- 例として README は、合計 72 GB の2枚のカードで 225.6 GB の Muse Spark Open 816B-A42B や、250.1 GB の MiniMax-M3.1-Flash（Unsloth の 2bit GGUF なら 143.9 GB）を動かせるとしている。
- v0.3.12 で **Mistral Large 4**（1T パラメータ、52B アクティブ）に対応。`--place a` で UD-IQ1_S を RTX 3090 1枚に載せ、ルーティングされたエキスパートをホストメモリから流す構成を挙げている。
- 同じく v0.3.12 で、`--parallel auto` と `--slot-ctx`、スロットの保存・復元、系列長に応じて伸びる KV メモリ、FP4 / NVFP4 のカード・ホスト・ドライブ分割ロードが入った。
- **llama-server 互換**。OpenAI / Anthropic 形式の HTTP API、GGUF、同じフラグ名を受け付けるので、既存のクライアント設定をそのまま流用できる。
- ベンダー配布のフォルダをそのまま読める（MiniMax の NVFP4 safetensors、Qwen3.8 の NVFP4/FP4 など、変換も再量子化も不要）。
- プロンプトキャッシュをホスト RAM に保持し、他のリクエストを跨いで再利用する。
- NVIDIA（DGX Spark / GB10 含む）と Apple Silicon（Metal バックエンド、mlx-community の4bitフォルダ）に対応。HTTP サーバーから CUDA カーネルまで Rust 実装。

## 目的・背景

MoE を「VRAM に収まる範囲」で諦めるのではなく、エキスパートの配置を実行時に調整して安いハードで回すための推論サーバー。llama.cpp のサーバーを置き換える形で使うことを狙っている。2026-09-19 作成、直近30日のコミットは100以上。

## 依存関係

- ビルド済みバイナリ（インストーラ / Homebrew / Docker / tarball）が配布されている。ソースから建てる場合は `docs/BUILD.md`（Linux）または `docs/mac.md`（Mac）。
- NVIDIA 経路は CUDA。Docker を使う場合はホスト側に NVIDIA Container Toolkit が必要。
- Apple Silicon 経路は Metal バックエンド（`bloomery-serve-metal`）。

## 実行条件

- ライセンスは MIT。★59、fork 7、issue 50（2026-11-04 時点）。**作成から1か月半の新しいプロジェクト**で、issue が多めに開いている点は導入前に見ておく。
- v0.3.12 の高速化数値は各変更の作成者による計測で、カードと条件が個別に示されている。前提を揃えないと比較にならない。
- 「RTX 3090 1枚で Qwen3.8-Flash-Next が 83.36 tok/s」は投稿と README の主張。条件（量子化、プロンプト長）を揃えないと比較にならない。
- ホスト RAM を大量に使う構成が前提。モデルによっては数百 GB のダウンロードが必要。
- 読み込みはモデルごとに検証済み／未検証が分かれている（Apple Silicon の Q4_K_M GGUF は「動くが未検証」と README に明記）。

## 最短手順

```bash
# インストーラ（Linux x86-64 + NVIDIA、または WSL2 内）
curl -fsSL https://raw.githubusercontent.com/midagedev/bloomery/main/tools/release/install.sh | sh
~/.local/bin/bloomery-serve --hf unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF:Q4_K_M

# または Homebrew（Apple Silicon は Metal 版バイナリ）
brew install midagedev/tap/bloomery
bloomery-serve-metal -m PATH/Qwen3.6-35B-A3B-Q4_K_M.gguf

# または Docker（NVIDIA Container Toolkit 必須）
docker run --gpus all -p 8080:8080 -v bloomery-cache:/root/.cache/bloomery \
  ghcr.io/midagedev/bloomery --hf unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF:Q4_K_M

# 起動確認: GET /health が 200 / 待受は 127.0.0.1:8080
```

## 変更履歴

- 2026-11-04: 初回登録（★57 / MIT / v0.3.12 / 最終push 2026-11-04）、Mistral Large 4 対応と並列・スロット系フラグ（v0.3.12）
