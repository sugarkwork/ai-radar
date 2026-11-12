---
name: "VidDub"
genre: "video-gen"
url: "https://github.com/LAW1223/VidDub"
repo: "LAW1223/VidDub"
license: "unknown"
stars: 64
language: "Python"
created: "2026-10-29"
updated: "2026-11-10"
forks: 0
open_issues: 2
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 8
size_kb: 2308
archived: false
flags: ["unverified"]
risk_notes: "リポジトリAPI上のライセンスはunknown。READMEのライセンス表示だけでは具体的な利用条件を確認できない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/Machinedelusion/status/2118436438614196297"]
fetched_at: "2026-11-12T03:50:04.466784+00:00"
---

# VidDub

## 出来ること

- 置換音声に合わせて動画の発話動作を編集する、音声駆動の動画吹き替えシステム。READMEでは、人物の外見・動き・シーンを保ちながら発話を置き換える設計、2ステップ推論、長尺動画向けの重複窓処理を説明している。

## 目的・背景

- READMEによると、音声を置き換えた後に元動画の口元を再構成対象にすると、置換後の発話動作と矛盾しうる。VidDubは置換音声での学習時に元の口元再構成をマスクし、顔や背景などの情報を保つことを狙う。

## 依存関係

- README記載の要件はLinux、Python 3.10以上、FFmpeg、NVIDIA CUDA GPU、およびWan/VACEスタックを動かすためのGPUメモリ。開発環境ではPyTorch 2.7.1を使用。モデル重みのほか、Wan/VACEの基盤アセットとWhisperは別途取得する手順が示されている。

## 実行条件

- 入力動画は検出可能でおおむね正面向きの顔を含み、81フレーム以上であること。音声は16 kHzにリサンプルされ、出力は入力動画のフレームレートと解像度を保つとREADMEに記載。長尺処理は81フレーム窓、64フレーム刻み、17フレーム重複。

## 最短手順

- README記載の流れは、リポジトリを取得してrequirements.txtをインストールし、VidDub・Wan/VACE・Whisperの重みを配置した後、scripts/infer.pyにモデル、入力動画、置換音声、出力先を指定して実行すること。例: `python scripts/infer.py --model weights/VidDub --weight-root weights --video input.mp4 --audio replacement.wav --output output.mp4`。

## 変更履歴

- 2026-11-12: 初回登録
