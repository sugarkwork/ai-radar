---
name: "OOOSplat"
genre: "3d-motion"
url: "https://github.com/ooolabdev/ooosplat"
repo: "ooolabdev/ooosplat"
license: "Apache-2.0"
stars: 2545
language: "Rust"
created: "2026-08-15"
updated: "2026-11-15"
forks: 302
open_issues: 23
commits_30d: 35
commit_cadence: "daily"
commits_90d: 100
size_kb: 16159
archived: false
flags: ["unverified"]
risk_notes: "READMEの記述に基づく紹介。実機での動作や生成品質は独立検証していない。LinuxはUbuntu 24.04 LTS x86_64のAlphaで、CPU-onlyソフトウェア描画は未検証。macOSはApple Silicon向け未署名・未公証Alpha。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/awe0_io/status/2119268269979025464"]
fetched_at: "2026-11-18T13:25:20.746260+00:00"
---

# OOOSplat

## 出来ること

- 普通・全景動画や画像系列から、ローカルで3D Gaussian Splattingを生成する。結果はプレビュー、編集でき、PLY、圧縮PLY、SPZ、SOG、MP4、オフラインHTMLにエクスポートできる。外部Gaussianモデルの読み込みにも対応するとREADMEに記載されている。

## 目的・背景

- 素材選択、プロジェクト先、品質档位を指定して生成を進めるデスクトップアプリ。画面準備、COLMAPによるカメラ再構成、Brushによる学習、final.plyの公開を自動化し、手動でコマンドを組み立てたりエンジンを設定したりせずに使えるとREADMEは説明している。

## 依存関係

- READMEによると、Windows版とApple Silicon macOS AlphaにはFFmpeg、FFprobe、COLMAP、Brushが同梱される。Ubuntu版はシステムのFFmpeg/FFprobeを使い、COLMAPとBrushはアプリに含まれる。

## 実行条件

- Windows 11 x64とWebView2 Runtimeが必要。Brush学習には利用可能なGPUグラフィックバックエンドが必要。COLMAPのNVIDIA CUDA加速にはWindowsドライバー580.00以上、Compute Capability 7.5以上が必要で、満たさない場合はCPUを使用する。macOSは15以降のApple Silicon限定Alpha。LinuxはUbuntu 24.04 LTS x86_64 Alphaで、対応GPUドライバーが必要。

## 最短手順

- GitHub Releasesから対象OSの配布物を取得してインストールし、起動後に素材、プロジェクトディレクトリ、品質档位を選んで「開始生成」を実行する。画像集が100枚を超える場合は撮影順を確認する。完了後はプレビューで編集し、エクスポート形式を選ぶ。

## 変更履歴

- 2026-11-23: 初回登録
