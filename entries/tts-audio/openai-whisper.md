---
repo: "openai/whisper"
name: "Whisper"
genre: "tts-audio"
url: "https://github.com/openai/whisper"
license: "MIT"
stars: 111860
language: "Python"
created: "2022-09-16"
updated: 2026-08-31
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 13560
open_issues: 179
commits_30d: 0
commits_90d: 1
commit_cadence: stale
size_kb: 12797
archived: false
fetched_at: "2026-11-03T15:42:52Z"
last_release: v20250625
last_release_at: 2025-06-26
---

# Whisper

## 出来ること

- 多言語の音声認識（書き起こし）、音声→英語翻訳、言語識別をまとめて行うモデルと CLI。
- モデルは tiny / base / small / medium / large の5サイズ。速度と精度のトレードオフで選ぶ。
- タイムスタンプ付きの単語／セグメント出力、VAD による無音除去、初期プロンプト指定に対応。

## 目的・背景

OpenAI が 2022-09 に公開した音声認識モデル。派生実装（faster-whisper、whisper.cpp、Groq 等のホスト版）が多数あり、ローカル文字起こしの事実上の標準。本リポジトリは原典実装で、学習コードと重み変換スクリプトも含む。

## 依存関係

- Python 3.8〜3.11（README は 3.9.9 / PyTorch 1.10.1 で検証、その後も対応と記載）。
- `ffmpeg` が必須（PATH 上に必要）。
- `pip install -U openai-whisper`。tiktoken の wheel が無い環境では Rust ツールチェーンが必要になる場合がある。

## 実行条件

- GPU があると大幅に速い。large モデルは VRAM 約 10GB 級、medium 以下なら数 GB（モデルサイズ依存）。
- モデル重みは初回実行時に `~/.cache/whisper` へダウンロード。
- 日本語の書き起こしは `--language ja` を明示すると安定する。

## 最短手順

```bash
pip install -U openai-whisper
whisper audio.mp3 --model medium --language ja --output_format srt
```

## 変更履歴

- 2026-11-03: 初回登録（star 111,858 / pushed 2026-08-31 / MIT）
