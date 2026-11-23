---
name: "Persian ASR: Nemotron streaming, fine-tuned for Persian (Farsi)"
genre: "tts-audio"
url: "https://github.com/mallahyari/nemotron-asr-streaming-farsi"
repo: "mallahyari/nemotron-asr-streaming-farsi"
license: "Apache-2.0"
stars: 96
language: "Python"
created: "2026-10-03"
updated: "2026-10-03"
forks: 9
open_issues: 2
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 6
size_kb: 676
archived: false
flags: ["unverified"]
risk_notes: "評価値はREADMEに記載された作者報告であり、独立に再測定していない。モデル重みはApache-2.0ではなく、README記載のOpenMDW-1.1。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/itsjooyan/status/2122779831557394859"]
fetched_at: "2026-11-18T04:16:10.866329+00:00"
---

# Persian ASR: Nemotron streaming, fine-tuned for Persian (Farsi)

## 出来ること

- ペルシャ語音声のストリーミング認識と音声・動画ファイルの文字起こしに対応するモデルの学習、評価、推論用コードを提供する。README記載の評価では、FLEURS fa testのWER 8.8%、会話音声testのWER 26.0%、Common Voice 22 fa testのWER 19.1%。作者は0.32秒look-ahead時のFLEURS WER 9.0%、会話音声test WER 28.0%も報告している。これらはREADME記載値で独立測定ではない。

## 目的・背景

- NVIDIA nemotron-3.5-asr-streaming-0.6bを、1,181時間のオープンライセンスのペルシャ語音声でファインチューニングしたモデル。READMEの説明では、ライブ音声をチャンク単位で認識し、ファイル全体の認識にも利用できる。

## 依存関係

- README記載のTransformers版の試用にはuvとffmpegが必要で、モデルはHugging Faceからダウンロードする。NeMo版はuv sync --extra trainで環境を同期して利用する。

## 実行条件

- READMEによればTransformers版はApple Silicon（MPS）、CUDA、CPUで実行可能。M1 Proではリアルタイムの約10倍の速度と作者が記載しているが、実行環境による差があり得る。NeMo版はREADME記載の手順で実行する。

## 最短手順

- ローカルWebアプリは `uv run scripts/gradio_app.py`、音声・動画ファイルの文字起こしは `uv run scripts/hf_transcribe_file.py audio.m4a`、マイクのライブ文字起こしは `uv run scripts/hf_stream_mic.py`。コードから使う場合はモデルカードを参照し、language promptを `fa-IR` に設定する。

## 変更履歴

- 2026-11-23: 初回登録
