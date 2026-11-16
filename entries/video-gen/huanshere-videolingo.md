---
name: "VideoLingo"
genre: "video-gen"
url: "https://github.com/Huanshere/VideoLingo"
repo: "Huanshere/VideoLingo"
stars: 19271
forks: 2130
open_issues: 25
size_kb: 21457
language: "Python"
created: "2024-08-09"
updated: "2026-11-13"
archived: false
license: "Apache-2.0"
commits_30d: 6
commits_90d: 100
commit_cadence: "weekly"
flags: []
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/flxrnc/status/2119041226909372919"]
fetched_at: "2026-11-16T01:45:21.344103+00:00"
---

# VideoLingo

## 出来ること

- 音声認識、字幕翻訳、字幕分割、吹き替えをStreamlitの画面で扱い、字幕ファイルや、任意で字幕・吹き替え付きの動画を作成するとREADMEに記載されています。品質は元音声、言語、選択したモデルに依存します。出典: https://github.com/Huanshere/VideoLingo/blob/main/README.md

## 目的・背景

- 「The workflow combines transcription, translation, subtitle layout and dubbing in one project.」文字起こし、翻訳、字幕レイアウト、吹き替えを一つのプロジェクトで扱う構成です。出典: https://github.com/Huanshere/VideoLingo/blob/main/README.md

## 依存関係

- READMEには、YouTube動画取得にyt-dlp、既定の音声認識にQwen3-ASRとQwen3-ForcedAligner、吹き替えに複数のTTS方式が記載されています。LLMは構造化JSONを返せるOpenAI互換Chat Completionsプロバイダーを選ぶ必要があります。出典: https://github.com/Huanshere/VideoLingo/blob/main/README.md

## 実行条件

- Windows、macOS（Apple Silicon / Intel）、Linuxに対応するとREADMEに記載されています。初回起動にはインターネット接続が必要で、Windowsのワンクリック手順ではPython 3.12などを自動セットアップします。Linux NVIDIA向けDocker構成も説明されています。出典: https://github.com/Huanshere/VideoLingo/blob/main/README.md

## 最短手順

- ソースからの手順として、READMEは `git clone https://github.com/Huanshere/VideoLingo.git && cd VideoLingo` の後に `uv run start.py` を実行する方法を記載しています。起動後、サイドバーでAPI URL、キー、モデルを設定します。出典: https://github.com/Huanshere/VideoLingo/blob/main/README.md

## 変更履歴

- 2026-11-16: 初回登録
