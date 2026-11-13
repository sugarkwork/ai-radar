---
name: "VidBee"
genre: "other"
url: "https://github.com/nexmoe/VidBee"
repo: "nexmoe/VidBee"
stars: 11135
forks: 874
open_issues: 56
size_kb: 32375
language: "TypeScript"
created: "2025-10-22"
updated: "2026-11-08"
archived: false
license: "MIT"
commits_30d: 13
commits_90d: 63
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/bkdgiffug/status/2118637513862783231"]
fetched_at: "2026-11-13T06:25:29.472768+00:00"
---

# VidBee

## 出来ること

- 動画・音声を対応サイトからダウンロードするか、ローカルファイルを取り込み、文字起こしを検索可能なライブラリとして管理するデスクトップアプリ。READMEでは、ローカル音声認識、話者ラベル、タイムスタンプ再生、要約・翻訳・質問などのAI処理、ダウンロードキュー、RSS購読、形式やメタデータの設定を説明している。

## 目的・背景

- 動画・音声の取得から文字起こし、整理、検索、文字起こしへのAI処理までを一つのアプリで扱う用途。README記載の機能説明であり、独立した実機評価ではない。

## 依存関係

- READMEは、ローカル文字起こしにWhisper、SenseVoice、Parakeet、Qwen3-ASRのモデルファミリーを選べると説明している。ダウンロード機能の共有コアとしてyt-dlp/ffmpegを記載。AI処理は利用者が選んだプロバイダーに接続し、Ollama、LM Studioなどのローカルエンドポイントも選択肢として挙げている。

## 実行条件

- デスクトップアプリとして利用する。文字起こしはローカルで実行するとREADMEに記載。AIプロンプト実行時は、プロンプトと文字起こし内容が選択したプロバイダーに送られる。Web/API構成は別途、READMEにpnpmまたはDockerでの起動方法が記載されている。

## 最短手順

- READMEの「Download VidBee」からアプリを入手し、対応サイトのURLを貼り付けるかローカルの音声・動画ファイルを取り込む。文字起こしを作成し、必要に応じて設定からAIプロバイダーを選んで要約・翻訳・質問などのプロンプトを実行する。

## 変更履歴

- 2026-11-13: 初回登録
