---
name: "gsplat"
genre: "3d-motion"
url: "https://github.com/nerfstudio-project/gsplat"
repo: "nerfstudio-project/gsplat"
license: "Apache-2.0"
stars: 5930
language: "Python"
created: "2023-08-25"
updated: "2026-09-19"
forks: 1023
open_issues: 405
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 4
size_kb: 165567
archived: false
flags: ["unverified"]
risk_notes: "READMEの評価欄は最大4倍のGPUメモリ削減、最大15%の所要時間短縮を報告しているが、ここでは独立実測していない。PyTorch、CUDA、Pythonの対応組み合わせは配布先の案内で確認が必要。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xCarrera/status/2123762450935771202"]
fetched_at: "2026-11-22T04:47:14.395834+00:00"
---

# gsplat

## 出来ること

- Pythonバインディング付きのCUDA高速Gaussian Splattingラスタライズライブラリ。READMEは、3DGS/3DGUTのラスタライズ、疎なラスタライズ、複数GPU対応、各種カメラ・センサー、学習および事前学習済みGaussianシーンの推論レンダリング機能を挙げている。推論レンダリングはexperimentalで、学習勾配を必要としない用途向けと説明されている。

## 目的・背景

- SIGGRAPH論文「3D Gaussian Splatting for Real-Time Rendering of Radiance Fields」に着想を得たオープンソース実装。READMEは、元実装に対して高速化・省メモリ化と機能追加を行ったと述べている。

## 依存関係

- PyTorchを先にインストールする。READMEはソースからの導入例と、追加依存パッケージ（ninja、numpy、jaxtyping、rich）の例を記載している。

## 実行条件

- CUDAコードはPyPI導入時に初回実行時のJITでビルドされ、ソース導入時はインストール中にビルドされる。Windows/Linux向けの事前ビルドwheelは特定のPython・PyTorch・CUDAの組み合わせに限られる。Windowsでソースビルドする場合はREADME記載の専用手順を参照。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- PyTorchを導入後、`pip install gsplat` を実行する。Windowsでソースビルドする場合はREADME記載のWindowsインストール手順を確認する。

## 変更履歴

- 2026-11-23: 初回登録
