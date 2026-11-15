---
name: "Whisper Flow"
genre: "other"
url: "https://github.com/dimastatz/whisper-flow"
repo: "dimastatz/whisper-flow"
license: "MIT"
stars: 1011
language: "Python"
created: "2024-06-03"
updated: "2026-11-15"
forks: 139
open_issues: 1
commits_30d: 18
commit_cadence: "weekly"
commits_90d: 47
size_kb: 75994
archived: false
flags: ["unverified"]
risk_notes: "The README reports benchmark results of latency below 500 ms and a word error rate around 7% on an M1 MacBook Air with 16 GB RAM; these are author-reported results, not independent measurements. The attached README ends during the development setup instructions, so later setup details are unavailable."
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/ruyi3699/status/2118990841880465621"]
fetched_at: "2026-11-15T17:09:38.773933+00:00"
---

# Whisper Flow

## 出来ること

- ストリーミング音声をリアルタイムに文字起こしするサービス。音声を16 kHz、モノラル、int16 PCMのバイナリフレームとして`/ws`へ送り、JSON形式の部分結果・確定結果を受け取ります。READMEは、ストリーミングは処理速度が上がる一方、精度が低下する場合があると説明しています。

## 目的・背景

- OpenAI Whisperによるファイル単位のバッチ文字起こしに対し、音声を逐次送信して文字起こし結果を返す仕組みを提供します。READMEにはLibriSpeechを用いたベンチマーク方法と、M1 MacBook Air・16 GB RAMでの作者報告として、レイテンシが500 ms未満、単語誤り率が約7%と記載されています。これらは独立実測ではありません。

## 依存関係

- READMEの前提条件はPython 3.8以上（Python 3.12でテスト済み）と、PyAudioの音声入出力に必要なPortAudioです。

## 実行条件

- READMEではサーバーをポート8181で起動する手順を示しています。クライアント音声は16 kHz、モノラル、int16 PCM形式です。利用可能なモデルは`GET /ready`で確認できます。

## 最短手順

- READMEのQuick Startでは、リポジトリをcloneして`./run.sh -local`を実行し、仮想環境を有効化してから`./run.sh -run-server`を実行します。サーバーはポート8181で起動します。

## 変更履歴

- 2026-11-15: 初回登録
