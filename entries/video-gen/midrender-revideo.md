---
name: "Revideo"
genre: "video-gen"
url: "https://github.com/midrender/revideo"
repo: "midrender/revideo"
stars: 4205
forks: 220
open_issues: 63
size_kb: 22463
language: "TypeScript"
created: "2024-03-11"
updated: "2026-07-15"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/RealMarvelX/status/2118525010088251781"]
fetched_at: "2026-11-12T11:15:34.259153+00:00"
---

# Revideo

## 出来ること

- TypeScriptでシーンを記述し、動画ファイルにレンダリングする。READMEには、プログラムから利用するヘッドレスレンダリングAPI、Reactプレイヤーでのブラウザプレビュー、動画・音声コンポーネント、音声出力とフレーム単位の同期が記載されている。

## 目的・背景

- コードで動画を作成するためのレンダリングエンジン。READMEによると、シーンはTypeScriptで記述し、ClaudeやCodexがプロンプトからシーンを生成する用途も想定している。

## 依存関係

- READMEではコアは「zero dep」と説明されている。レンダリングにはNodeとヘッドレスブラウザが動作する環境が必要と記載されている。個別の依存パッケージ一覧はREADMEにない。

## 実行条件

- Nodeとヘッドレスブラウザが動作する環境。READMEではGoogle Cloud Runなどのサーバーレス環境での実行例にも言及している。

## 最短手順

- README記載の作成コマンドは `npm init @revideo@latest`。シーンはTypeScriptのgenerator関数として作成し、コマンドラインから `renderVideo()` でレンダリングする。詳細はREADMEから案内される公式ドキュメントを参照。

## 変更履歴

- 2026-11-12: 初回登録
