---
name: "Video Subtitle Remover (VSR)"
genre: "other"
url: "https://github.com/YaoFANGUK/video-subtitle-remover"
repo: "YaoFANGUK/video-subtitle-remover"
license: "Apache-2.0"
stars: 13798
language: "Python"
created: "2023-10-25"
updated: "2026-06-30"
forks: 1713
open_issues: 196
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 1505343
archived: false
flags: ["unverified"]
risk_notes: "READMEが示す機能・アルゴリズム別の効果は作者の説明であり、独立した実測結果は確認していない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:18:15.241774+00:00"
---

# Video Subtitle Remover (VSR)

## 出来ること

- 動画のハード字幕を除去し、字幕領域をAIベースのインペインティングで補完するソフトウェア。字幕の位置を指定した除去、位置指定なしで動画内テキストを自動除去、複数画像の透かし・テキスト除去に対応するとREADMEは説明しています。字幕抽出機能もあり、READMEではvideo-subtitle-extractorとの併用を案内しています。CLIでは入力・出力パス、字幕領域座標、インペイント方式（sttn-auto、sttn-det、lama、propainter、opencv）を指定できます。

## 目的・背景

- 動画中のハード字幕やテキストを除去するためのツールです。READMEによれば、除去領域を非隣接ピクセルの単純な埋め合わせではなくAIモデルで補完することを目的としています。各方式の画質・速度に関する説明は作者による案内で、独立検証済みの結果ではありません。

## 依存関係

- ソースから実行する場合、READMEはPython 3.12以上とrequirements.txtのインストールを案内しています。実行方式に応じてPaddlePaddle、PyTorch、CUDA/cuDNN、onnxruntime-gpu、torch-directmlなどの導入手順が異なります。

## 実行条件

- Windows、macOS、Linuxに対応するとREADMEに記載されています。CUDA対応NVIDIA GPU、WindowsのDirectML対応GPU、CPUでの実行手順があり、macOSはApple Silicon向け手順も掲載されています。CUDAや各GPU向けの条件は利用する環境・配布パッケージに依存します。

## 最短手順

- 配布済みアーカイブはGitHub Releasesから取得して展開し、実行します。Dockerの例では、GPU別またはCPU用イメージを使い、`python backend/main.py -i test/test.mp4 -o test/test_no_sub.mp4`を実行します。ソースから使う場合は、Python環境と実行方式に応じた依存関係を用意し、GUIは`python gui.py`、CLIは`python ./backend/main.py`で起動します。READMEにはCLIの`--subtitle-area-coords`や`--inpaint-mode`などの引数も記載されています。

## 変更履歴

- 2026-11-23: 初回登録
