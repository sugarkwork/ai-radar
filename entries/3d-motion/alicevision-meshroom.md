---
type: "repo"
repo: "alicevision/Meshroom"
name: "Meshroom"
genre: "3d-motion"
url: "https://github.com/alicevision/Meshroom"
license: "MPL-2.0"
stars: 13076
language: "Python"
created: "2015-04-22"
updated: "2026-11-09"
forks: 1243
open_issues: 550
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 13824
archived: false
added: "2026-11-09"
fetched_at: "2026-11-09T21:30:24Z"
flags: ["unverified"]
risk_notes: "Meshroom本体はMPL-2.0。AliceVisionや追加プラグイン、AIモデルの条件は個別に確認。公式マニュアルによると密な深度推定にはCUDA対応NVIDIA GPUが必要で、非CUDA環境は粗いdraft meshingを利用。実行・再構築品質は未検証。"
sources: ["https://x.com/i/status/2119475041402257767", "https://github.com/alicevision/Meshroom", "https://meshroom-manual.readthedocs.io/en/latest/first-steps/install/requirements.html", "https://raw.githubusercontent.com/alicevision/Meshroom/develop/COPYING.md"]
last_release: "v2025.1.0"
last_release_at: "2025-08-19"
---

# Meshroom — 写真からの3D再構築ワークフロー

## 出来ること

複数の写真からカメラ位置と形状を推定し、メッシュやテクスチャを生成するノードベースの視覚的ワークフロー。AliceVisionプラグインでフォトグラメトリー、カメラ追跡、パノラマ等を扱う。独自Pythonノードや外部コマンドで拡張できる。

## 目的・背景

ノードごとに処理を分離し、入力や設定を変更した場合は影響を受ける下流だけ再計算して中間キャッシュを再利用する。ローカルまたはレンダーファームで実行可能。単なる画像生成AIではなく、多視点写真からの3D再構築を中心とする。

## 依存関係

GUIはPythonとQt/PySide、再構築にはAliceVisionを利用する。公式はビルド済みリリースを提供。プラグインごとの依存・モデルやライセンスは別に確認する。

## 実行条件

公式マニュアルはWindowsとLinuxの配布版を案内。密な深度推定にはCUDA対応NVIDIA GPUを要する一方、GPUなしの粗いdraft meshingもある。撮影枚数・写真品質・対象表面などで結果やリソース要件は変わる。

## 最短手順

公式ReleasesからOSに合うビルドを取得し、展開して起動。重なりを持つ複数写真を取り込み、再構築パイプラインを実行する。詳細は公式マニュアル参照。

## 注意点

本体はMPL-2.0。AliceVisionや追加プラグイン、モデル・同梱ライブラリは別途条件確認。手元での実行・品質検証はしていない。
