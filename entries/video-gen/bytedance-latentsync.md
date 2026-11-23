---
name: "LatentSync"
genre: "video-gen"
url: "https://github.com/bytedance/LatentSync"
repo: "bytedance/LatentSync"
license: "Apache-2.0"
stars: 6290
language: "Python"
created: "2024-12-11"
updated: "2025-06-20"
forks: 1012
open_issues: 229
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 9641
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:19:28.336268+00:00"
---

# LatentSync

## 出来ること

- 音声条件付き潜在拡散モデルで音声と映像の対応を学習し、映像のリップシンクを生成する。READMEはLatentSync 1.5の推論に最低8 GB、1.6に最低18 GBのVRAMが必要と記載している。

## 目的・背景

- READMEによると、LatentSyncは中間的なモーション表現を介さず、音声条件付き潜在拡散モデルを用いるエンドツーエンドのリップシンク手法。Whisperで得た音声埋め込みをU-Netに統合する構成を説明している。

## 依存関係

- READMEが明示する構成要素はWhisperによる音声埋め込み生成、Stable Diffusionの利用、データ処理でのPySceneDetectとInsightFace。セットアップには必要パッケージの導入とチェックポイント取得が含まれる。

## 実行条件

- README記載の推論VRAM目安はLatentSync 1.5が8 GB、1.6が18 GB。学習設定ごとのVRAM目安はstage1が23 GB、stage2が30 GB、stage2_efficientが20 GB、stage1_512が30 GB、stage2_512が55 GB。これらはREADME記載値であり、独立した実機検証ではない。

## 最短手順

- READMEの手順では、まず `source setup_env.sh` で必要パッケージとチェックポイントを準備する。推論はGradioなら `python gradio_app.py`、CLIなら `./inference.sh` を実行する。READMEは `inference_steps` を20〜50、`guidance_scale` を1.0〜3.0の調整範囲として案内している。

## 変更履歴

- 2026-11-23: 初回登録
