---
name: "SAM 2"
genre: "other"
url: "https://github.com/facebookresearch/sam2"
repo: "facebookresearch/sam2"
license: "Apache-2.0"
stars: 20155
language: "Jupyter Notebook"
created: "2024-07-29"
updated: "2026-05-30"
forks: 2592
open_issues: 487
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 138255
archived: false
flags: []
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/flxrnc/status/2119041226909372919"]
fetched_at: "2026-11-16T01:43:44.291840+00:00"
---

# SAM 2

## 出来ること

- SAM 2は、画像と動画を対象とするプロンプト可能な視覚セグメンテーション用モデルです。画像予測、画像の自動マスク生成、動画内の複数オブジェクトのセグメンテーションと追跡に対応するAPIを提供します。READMEは、動画推論でプロンプトを追加し、動画フレームへマスクを伝播できると説明しています。

## 目的・背景

- 画像を単一フレームの動画として扱うことでSAMを動画へ拡張し、ストリーミングメモリを用いたリアルタイム動画処理向けのTransformer構成を採用しています。作者は、モデルとデータをユーザー操作で改善するデータエンジンを構築し、SA-Vデータセットを収集したと説明しています。

## 依存関係

- README記載の要件はPython 3.10以上、PyTorch 2.5.1以上、TorchVision 0.20.1以上です。ノートブック例の利用にはJupyterとmatplotlibが必要です。

## 実行条件

- READMEはGPUマシンへのインストールを案内し、インストール時にカスタムCUDAカーネルのコンパイルが必要と説明しています。CUDA拡張のビルドに失敗しても利用できる場合がありますが、一部の後処理機能が制限される可能性があります。WindowsではWSLとUbuntuの利用を推奨しています。

## 最短手順

- README記載の手順は、リポジトリを取得して `pip install -e .` を実行し、チェックポイントを用意して、画像または動画のpredictor APIを呼び出すことです。チェックポイント取得には `checkpoints/download_ckpts.sh` を実行する方法も記載されています。

## 変更履歴

- 2026-11-16: 初回登録
