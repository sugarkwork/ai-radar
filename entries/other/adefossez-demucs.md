---
name: "Demucs"
genre: "other"
url: "https://github.com/adefossez/demucs"
flags: ["unverified"]
risk_notes: "READMEではMUSDB HQテストセットでのSDR値を報告しています。これはREADME上の報告であり、この候補についての独立した実測ではありません。実験的な6音源モデルのピアノ分離には漏れやアーティファクトが多いとREADMEに記載されています。"
repo: "adefossez/demucs"
stars: 3564
forks: 333
open_issues: 6
size_kb: 78746
language: "Python"
created: "2023-11-16"
updated: "2026-10-26"
archived: false
license: "MIT"
commits_30d: 1
commits_90d: 2
commit_cadence: "monthly"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:14:54.756448+00:00"
---

# Demucs

## 出来ること

- 楽曲からドラム、ベース、ボーカルと伴奏などの音源を分離します。READMEでは、実験的な6音源モデルについてギターとピアノの音源追加を説明し、ピアノには漏れやアーティファクトが多いとしています。

## 目的・背景

- 音源分離を目的とするリポジトリです。READMEによると、v4はスペクトログラムと波形を組み合わせるHybrid Transformer Demucsで、Hybrid Demucsを基に、内側の層をクロスドメインTransformer Encoderに置き換えています。README記載の評価値は作者側の報告です。

## 依存関係

- READMEでは、通常の分離にはパッケージに必要なものが含まれると説明しています。学習用の追加依存関係は`train`、量子化モデル用は`quantized`です。ffmpegは任意ですが、flac出力と、sphnがデコードできない音声形式の読み込みに必要です。

## 実行条件

- README記載の必要条件はPython 3.10以上です。手順はuvの`uvx`を使いますが、pipでのインストールも可能です。Intel製（Apple Silicon以外）のMacでは、READMEはPython 3.12以下を使うよう案内しています。OS別の案内としてWindows、macOS、Linuxのサポート文書を挙げています。

## 最短手順

- 音源を分離する最短手順として、READMEは`uvx demucs MY_TRACK.mp3`を示しています。継続利用する場合は`uv tool install demucs`の後に`demucs MY_TRACK.mp3`を実行できます。

## 変更履歴

- 2026-11-23: 初回登録
