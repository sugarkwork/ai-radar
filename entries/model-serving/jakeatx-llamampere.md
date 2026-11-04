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
stars: 216
forks: 30
open_issues: 13
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 391373
archived: false
fetched_at: "2026-11-04T01:23:51Z"
last_release: v0.6.2
last_release_at: 2026-11-01
---

# llamAmpere

## 出来ること

- **Ampere 世代の NVIDIA GPU（RTX 3090 / 3090 Ti など）向けに最適化した llama.cpp のフォーク**。
- 独自の量子化形式「AmperInteger+」を実装し、約2.3bpw まで圧縮しながら BF16 相当の精度を保つとしている。
- 埋め込みテーブルをメインメモリに逃がすことで、**12GB VRAM でも 200K トークン超のコンテキスト**を扱える構成を用意している。
- 例として、Qwen3.8 の 100K トークン生成で 110+ tok/s（temperature 1）という測定値を挙げている。

## 目的・背景

2026-09 公開、★216、v0.6.2。llama.cpp の量子化は世代ごとのGPU特性（Ampere の INT8/FP8 周り）を活かしきれていない部分があり、RTX 30 系のユーザー向けに KV キャッシュ量子化とメモリ配置を振り直したもの。

## 依存関係

- CUDA（Ampere 世代のGPU）
- GGUF 形式のモデル
- Linux / Windows（ビルド手順は README 参照）

## 実行条件

- **Ampere 世代（RTX 30 系）向け**。Ada / Blackwell では恩恵が限られる可能性がある。
- 12GB VRAM 構成はメインメモリ側の余裕が必要（埋め込みテーブルを逃がすため）。
- リポジトリは約391MB（ビルド成果物を含む）。

## 最短手順

```bash
git clone https://github.com/JakeATX/llamAmpere
# README の CUDA ビルド手順に従う
```

## 変更履歴

- 2026-11-04: 初回登録（★216 / v0.6.2 / MIT / 30日100+コミット）
