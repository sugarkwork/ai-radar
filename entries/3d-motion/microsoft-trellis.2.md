---
name: "TRELLIS.2"
genre: "3d-motion"
url: "https://github.com/microsoft/TRELLIS.2"
repo: "microsoft/TRELLIS.2"
stars: 12950
forks: 1575
open_issues: 162
size_kb: 676187
language: "Python"
created: "2025-11-26"
updated: "2026-07-10"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/Vlixsi/status/2121631327036318061"]
fetched_at: "2026-11-16T21:33:58Z"
last_release: ""
last_release_at: ""
---

# TRELLIS.2

## 出来ること

- 4Bパラメータのモデルを用いて画像から3Dアセットを生成し、形状条件付きのPBRテクスチャ生成や学習を行うコードを提供する。READMEではO-Voxel表現、Base Color・Roughness・Metallic・Opacityの属性を説明している。出典: https://github.com/microsoft/TRELLIS.2

## 目的・背景

- 複雑なトポロジーや鋭い形状、PBR素材を含む3Dアセットの生成を目的とする。READMEはオープンサーフェス、非多様体ジオメトリ、内部構造への対応を説明している。出典: https://github.com/microsoft/TRELLIS.2

## 依存関係

- README記載: Linuxでテスト。NVIDIA GPUはVRAM 24GB以上が必要で、A100およびH100で確認済み。CUDA Toolkit（推奨12.4）、Python 3.8以上、Condaを推奨。セットアップ例ではPyTorch 2.6.0/CUDA 12.4、flash-attn等を導入する。出典: https://github.com/microsoft/TRELLIS.2

## 実行条件

- READMEの前提条件はLinux、NVIDIA GPUのVRAM 24GB以上、CUDA Toolkit、Python 3.8以上。flash-attn非対応GPUではxformersを手動導入してATTN_BACKENDを設定する手順が記載されている。出典: https://github.com/microsoft/TRELLIS.2

## 最短手順

- READMEの手順は、リポジトリをrecursive cloneし、Conda環境と依存関係をsetup.shで導入する。その後、example.pyの例に従ってmicrosoft/TRELLIS.2-4Bを読み込み、画像をpipeline.runへ渡して生成し、O-VoxelユーティリティでGLBへ書き出す。出典: https://github.com/microsoft/TRELLIS.2

## 変更履歴

- 2026-11-14: 初回登録
