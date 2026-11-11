---
name: "Video Studio Skill"
genre: "coding-agent"
url: "https://github.com/aaitor/skill-video-studio"
repo: "aaitor/skill-video-studio"
license: "MIT"
stars: 390
language: "HTML"
created: "2026-08-26"
updated: "2026-11-04"
forks: 13
open_issues: 3
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 27
size_kb: 15579
archived: false
flags: ["unverified"]
risk_notes: "全工程の実行にはローカルのツール環境が必要。README記載の本番要件はNode.js 22以上、FFmpeg/ffprobe、Chromiumおよび補助ツール固有のPython依存関係。ナレーションやアバターには追加サービスまたはGPU環境が必要。効果や費用は確認できない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2117952254091145585"]
fetched_at: "2026-11-10T15:19:20.013402+00:00"
---

# Video Studio Skill

## 出来ること

- Claude Codeの`/devrel-video`スキルを使い、製品操作のブラウザー撮影、HyperFramesによるタイトル・章・CTAの合成、FFmpegによる動画の仕上げと検査を行う。音楽、ナレーション、字幕、持ち込みプレゼンター映像などは任意の追加レイヤー。ブランド、ブリーフ、テンプレートと作例を含む。

## 目的・背景

- 製品のワークフローをデモ動画にまとめるためのローカル動画制作ワークスペース。

## 依存関係

- 制作スタックにはNode.js 22以上、FFmpeg/ffprobe、Chromium、補助ツール固有のPython依存関係が必要。ナレーションやアバターは追加サービスまたはGPU環境を要する。

## 実行条件

- 計画にはGitと認証済みClaude Codeが必要。完全な撮影・レンダリングにはローカルの制作ツール一式が必要。READMEによればオフラインCIはソースと一部ローカルユーティリティを検査し、制作スタック全体は検証しない。

## 最短手順

- READMEの手順ではリポジトリをcloneしてディレクトリに移動し、`claude`を起動する。`/devrel-video`に動画ブリーフの作成を依頼する。完全な動画を作る場合は制作前提条件を導入し、作例の手順に従う。

## 変更履歴

- 2026-11-11: 初回登録
