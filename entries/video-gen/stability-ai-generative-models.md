---
name: "Generative Models by Stability AI"
genre: "video-gen"
url: "https://github.com/Stability-AI/generative-models"
repo: "Stability-AI/generative-models"
license: "MIT"
stars: 27343
language: "Python"
created: "2023-06-22"
updated: "2025-12-16"
forks: 3091
open_issues: 337
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 88668
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/AIExplorerTim/status/2118242415219982564"]
fetched_at: "2026-11-11T08:19:03.895625+00:00"
---

# Generative Models by Stability AI

## 出来ること

- READMEによると、SV4D 2.0は入力動画から新規視点の動画と4Dアセットを生成する。SV3Dは単一画像から新規視点の動画を生成する。いずれも研究目的での公開として説明されている。

## 目的・背景

- Stability AIの生成モデル実装をまとめたリポジトリ。READMEは、SV4D 2.0について自己遮蔽への頑健性や実動画への汎化向上を作者の説明として挙げている。これらはREADME記載の主張であり、独立検証ではない。

## 依存関係

- README記載のSV4D 2.0セットアップはPython 3.10、PyTorch・torchvision・torchaudio（CUDA 11.8用のインデックスを例示）、requirements/pt2.txt、リポジトリ本体、Stability-AI/datapipelinesのsdataを使用する。

## 実行条件

- モデル重みをHugging Faceから取得してcheckpoints/に置く必要がある。SV4D 2.0の例は入力動画を使用し、READMEは低VRAM時にencoding_t=1、decoding_t=1またはimg_size=512を試す方法を記載している。必要なGPU性能の具体値はREADME抜粋に記載されていない。

## 最短手順

- README記載のSV4D 2.0手順: 1) Python 3.10の仮想環境を作る。2) README記載のPyTorch、pt2要件、リポジトリ、sdataをインストールする。3) stabilityai/sv4d2.0からsv4d2.safetensorsをcheckpoints/へ取得する。4) `python scripts/sampling/simple_video_sample_4d2.py --input_path <path/to/video>`を実行する。

## 変更履歴

- 2026-11-11: 初回登録
