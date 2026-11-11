---
name: "Pedalboard"
genre: "other"
url: "https://github.com/spotify/pedalboard"
repo: "spotify/pedalboard"
license: "GPL-3.0"
stars: 6475
language: "C++"
created: "2021-07-06"
updated: "2026-11-09"
forks: 376
open_issues: 150
commits_30d: 11
commit_cadence: "weekly"
commits_90d: 46
size_kb: 29926
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/RealMarvelX/status/2118330503040221345"]
fetched_at: "2026-11-11T20:10:39.081667+00:00"
---

# Pedalboard

## 出来ること

- Pythonで音声ファイルの読み書き、レンダリング、エフェクト処理ができる。AIFF、FLAC、MP3、OGG、WAVの読み書きに対応し、Chorus、Reverb、Compressor、PitchShiftなどのエフェクトを内蔵する。VST3プラグインはmacOS、Windows、Linuxで、Audio UnitはmacOSで利用できる。

## 目的・背景

- SpotifyのAudio Intelligence Labが、PythonとTensorFlowからスタジオ品質の音声エフェクトを利用するために開発。READMEでは、Spotify社内のデータ拡張やコンテンツ制作での利用例を挙げている。

## 依存関係

- READMEによると、AIFF、FLAC、MP3、OGG、WAVの読み書きは全プラットフォームで追加依存なし。その他の形式への対応はプラットフォームに依存する。

## 実行条件

- READMEではPython 3.10〜3.15との互換性を記載。Linuxのx86_64ホイールにはAVXが必要で、Linuxの多くのVSTにはglibc 2.27より新しい環境が必要。Windowsのホイールはamd64向け。

## 最短手順

- `pip install pedalboard`でインストール。`Pedalboard`にエフェクトを指定し、`pedalboard.io.AudioFile`で音声ファイルを読み込み、ボードを適用して出力ファイルへ書き込む。READMEにはChorusとReverbを使った処理例がある。

## 変更履歴

- 2026-11-11: 初回登録
