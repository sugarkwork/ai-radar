---
name: "ProPainter"
genre: "video-gen"
url: "https://github.com/sczhou/ProPainter"
repo: "sczhou/ProPainter"
license: "unknown"
stars: 7079
language: "Python"
created: "2023-09-01"
updated: "2026-10-27"
forks: 823
open_issues: 82
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 5
size_kb: 71468
archived: false
flags: ["unverified"]
risk_notes: "リポジトリのライセンス情報は取得値が unknown。README記載のGPUメモリ値は推定値で、この環境での実機検証はしていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:17:32.515276+00:00"
---

# ProPainter

## 出来ること

- 動画の物体除去と動画補完を行う動画インペインティング。READMEでは、入力として動画または分割フレームとフレームごとのマスクを用意する手順を案内している。

## 目的・背景

- ProPainterは、動画インペインティング向けの伝播・Transformer手法を扱うICCV 2023の研究実装。READMEによると、2023年9月にコードとモデルを公開した。

## 依存関係

- README記載の条件はPython 3.8、CUDA 9.2以上、PyTorch 1.7.1以上、Torchvision 0.8.2以上。その他のPythonパッケージはrequirements.txtからインストールする。

## 実行条件

- READMEの例では、動画またはフレームとフレーム単位のマスクを入力し、推論結果をresultsフォルダに保存する。GPUメモリを抑える設定として、neighbor_lengthの縮小、ref_strideの拡大、resize_ratioや動画サイズの縮小、fp16、subvideo_lengthの縮小が挙げられている。必要メモリの表はREADME記載の推定値。

## 最短手順

- READMEの手順は、リポジトリを取得し、Python 3.8のConda環境を作成してrequirements.txtを導入、Releases V0.1.0の事前学習済みモデルをweightsフォルダに用意してから、例として `python inference_propainter.py --video inputs/video_completion/running_car.mp4 --mask inputs/video_completion/mask_square.png --height 240 --width 432` を実行する。READMEでは初回推論時にモデルを自動ダウンロードする方法も記載している。

## 変更履歴

- 2026-11-23: 初回登録
