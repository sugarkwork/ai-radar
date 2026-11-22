---
name: "TripoSR"
genre: "3d-motion"
url: "https://github.com/VAST-AI-Research/TripoSR"
repo: "VAST-AI-Research/TripoSR"
license: "MIT"
language: "Python"
created: "2024-02-07"
updated: "2026-06-04"
commit_cadence: "stale"
archived: false
stars: 7409
forks: 959
open_issues: 109
size_kb: 37566
commits_30d: 0
commits_90d: 0
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/thegreatest_sv/status/2119129564047982889"]
fetched_at: "2026-11-17T02:19:55.514071+00:00"
---

# TripoSR

## 出来ること

- 単一画像から3Dモデルを再構成する公式コードベース。READMEでは、`run.py`による推論結果の保存、複数画像の入力、`--bake-texture`によるテクスチャ出力、`--texture-resolution`による解像度指定、およびGradioアプリを案内している。README記載ではNVIDIA A100で0.5秒未満、デフォルト設定で単一画像あたり約6GB VRAM。速度・性能の記述は作者による報告で、独立実測ではない。

## 目的・背景

- Tripo AIとStability AIが共同開発した、単一画像からの高速なフィードフォワード3D再構成モデル。READMEはLarge Reconstruction Model（LRM）の原理を活用すると説明し、研究者・開発者・クリエイターによる3D生成AIとコンテンツ制作を目的として挙げている。

## 依存関係

- Python 3.8以上、PyTorch、`requirements.txt`記載の依存パッケージが必要。CUDAは利用可能な場合に導入する。READMEは、ローカルCUDAとPyTorchに同梱されたCUDAのメジャーバージョンを一致させるよう記載している。

## 実行条件

- 推論時のデフォルト設定は単一画像あたり約6GB VRAMとREADMEに記載。CUDA利用時はローカルCUDAとPyTorch側CUDAのメジャーバージョンを合わせる。

## 最短手順

- READMEの手順に従い、Python 3.8以上、必要に応じてCUDA、環境に合ったPyTorchを用意し、`pip install --upgrade setuptools`と`pip install -r requirements.txt`を実行する。推論は`python run.py examples/chair.png --output-dir output/`。ローカルGradioアプリは`python gradio_app.py`で起動する。

## 変更履歴

- 2026-11-22: 初回登録
