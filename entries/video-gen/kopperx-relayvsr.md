---
name: "RelayVSR"
genre: "video-gen"
url: "https://github.com/kopperx/RelayVSR"
repo: "kopperx/RelayVSR"
license: "Apache-2.0"
stars: 315
language: "Python"
created: "2026-09-29"
updated: "2026-10-05"
forks: 26
open_issues: 3
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 18
size_kb: 192563
archived: false
flags: ["unverified"]
risk_notes: "GPUメモリ要件と実行速度はREADMEに記載がありません。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/superfang119/status/2118692694662987940"]
fetched_at: "2026-11-13T18:11:57.652789+00:00"
---

# RelayVSR

## 出来ること

- 疎なWan参照と小型条件付きデコーダーを用いて、動画をストリーミング方式で4倍超解像します。入力動画のFPSを維持し、出力解像度は入力の4倍です。音声はコピーされません。READMEのデモ説明では、出力領域をリサイズせず、MP4は3544×1832、24fps、265フレームとされています。出典: https://github.com/kopperx/RelayVSR

## 目的・背景

- 大規模モデルと小規模モデルの協調による、実世界動画向けの効率的な超解像を目的とするプロジェクトです。READMEは推論コードとプロジェクトウェブサイトのソースを含むと説明しています。

## 依存関係

- Linux、Python 3.11〜3.13、NVIDIA GPUが必要です。セットアップ手順は `uv sync --locked --extra cu128` です。依存パッケージや必要GPUメモリ量の詳細はREADME本文に記載されていません。

## 実行条件

- README記載の実行環境はLinux、Python 3.11〜3.13、NVIDIA GPUです。推論にはHugging Faceの `kopper/RelayVSR` から `flash.safetensors` と `wan.safetensors` を取得し、`weights/` に配置します。デフォルトのFlashチェックポイントはS、step 60000、EMAです。

## 最短手順

- 1. `uv sync --locked --extra cu128` を実行し、仮想環境を有効化します。2. `uvx hf download kopper/RelayVSR flash.safetensors wan.safetensors --local-dir weights` でチェックポイントを取得します。3. `python inference.py --output output_x4.mp4` を実行します。別の動画には `--input`、画像ディレクトリには `--fps` を指定します。README記載の手順であり、実機での動作確認結果ではありません。

## 変更履歴

- 2026-11-13: 初回登録
