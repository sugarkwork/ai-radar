---
repo: "TKY-27/iris-3b-metal"
name: "Iris-3B Metal"
genre: image-gen
url: "https://github.com/TKY-27/iris-3b-metal"
license: "Apache-2.0"
stars: 58
language: "Python"
created: "2026-10-09"
updated: "2026-10-19"
added: "2026-11-04"
first_seen: "2026-11-04"
source_post: "https://x.com/dextune/status/2117894618360508907"
sources: []
flags: []
risk_notes: ""
forks: 2
open_issues: 1
size_kb: 16697
archived: false
last_release: "v0.6.1"
commits_30d: 36
commits_90d: 78
commit_cadence: "daily"
fetched_at: "2026-11-09T21:38:41Z"
last_release_at: "2026-10-19"
---

# Iris-3B Metal

## 出来ること

- Apple Silicon 上で **Iris-3B のテキスト→画像生成をローカル実行**する推論エンジン。PyTorch MPS と自作の Metal カーネルで実装している。
- **VAE を使わない pixel-space diffusion**。RGB ピクセルを直接ノイズから復元するため、VAE のデコード往復がない。Iris-3B の設計をそのまま活かす実装。
- ネイティブ macOS アプリ（SwiftUI）、CLI（`iris-metal`）、Python API（`IrisPipeline`）、localhost の HTTP API の4経路が同梱されている。
- テキストエンコーダ（Qwen 系）はストリーミングで読む省メモリ実装。プロンプト・画像は Mac 上で処理され、外部に出ない（初回のモデル取得のみ Hugging Face から）。
- 相対深度推定・画像修復のファインチューンも同じアーキテクチャで動く（重みは使うときだけ追加ダウンロード）。

## 目的・背景

Speridlabs の Iris-3B（アーキテクチャ・学習コード・重み）を、Mac の GPU で実用的な速度で動かすための独立実装。重みは上流のものをそのまま使い、ファインチューンも蒸留もしていないと明記されている。Mac で画像生成を完結させたい場合の選択肢。

## 依存関係

- Apple Silicon、macOS 15 以降、Python 3.11 以降（CLI / Python API を使う場合）。
- 初回利用時にチェックポイントを取得する: Original 12.0 GB または公式 Turbo 6.0 GB（BF16）＋ 共有テキストエンコーダ 8.9 GB。
- ネイティブアプリ版は Python と重みを含まない（別途取得）。

## 実行条件

- ライセンスは Apache-2.0。★56、fork 2、issue 1（2026-11-04 時点）。
- **Apple Silicon 専用**。NVIDIA / CPU では動かない。
- README は「16 GB の Mac は未検証」と明記している。Turbo でも 6 GB ＋ 8.9 GB のテキストエンコーダがあるため、メモリの余裕は必要。
- Turbo 版はステップ数・CFG・ネガティブプロンプトが重みに固定されており、調整できない。
- 速度の数値（同一プロンプトのパイプライン遅延 21.6% 削減など）は作者側の計測で、比較条件は README の該当節を参照。

## 最短手順

```bash
# ネイティブアプリ（releases の macOS ビルド）
# CLI / Python をソースから使う場合
git clone https://github.com/TKY-27/iris-3b-metal.git && cd iris-3b-metal
uv sync   # もしくは README の development 手順
iris-metal "a glass of water on a wooden table"
```

## 変更履歴

- 2026-11-04: 初回登録（★56 / Apache-2.0 / v0.6.1 / 最終push 2026-10-19）
