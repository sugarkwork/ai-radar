---
name: "AutoSubs"
genre: "other"
url: "https://github.com/tmoroney/auto-subs"
repo: "tmoroney/auto-subs"
stars: 4575
forks: 332
open_issues: 168
size_kb: 123787
language: "TypeScript"
created: "2023-03-15"
updated: "2026-11-11"
archived: false
license: "MIT"
commits_30d: 14
commits_90d: 100
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:13:23.080886+00:00"
---

# AutoSubs

## 出来ること

- 音声または動画からタイムスタンプ付き字幕を作成し、話者を検出してラベル付けできます。READMEによると、複数のローカル文字起こしモデルを選べ、字幕の編集、翻訳、SRTやテキストへの書き出しに対応します。DaVinci Resolve、Adobe Premiere Pro、After Effectsとの連携手順も案内されています。

## 目的・背景

- READMEでは、クラウドを使わず端末上で処理する字幕作成アプリとして説明されています。

## 依存関係

- READMEには複数のモデル実装としてwhisper-rs（GGML）とONNX Runtimeが記載されています。完全な依存関係一覧はここでは確認できません。

## 実行条件

- READMEによると、macOS（Apple Silicon・Intel）、Windows、Linuxに対応し、処理はオフラインで行うとされています。モデルはアプリ内のModel Managerから必要に応じてダウンロードします。

## 最短手順

- 単体利用では、AutoSubsを起動して音声または動画を選択し、モデルと言語・翻訳設定を選んでTranscribeを実行します。必要に応じて字幕や話者を編集し、SRT・テキストに書き出すかクリップボードにコピーします。

## 変更履歴

- 2026-11-23: 初回登録
