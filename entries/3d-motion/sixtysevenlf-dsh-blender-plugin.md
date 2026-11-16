---
name: "DSH × Blender"
genre: "3d-motion"
url: "https://github.com/sixtysevenlf/dsh-blender-plugin"
repo: "sixtysevenlf/dsh-blender-plugin"
stars: 2147
forks: 94
open_issues: 9
size_kb: 10781
language: "Python"
created: "2026-09-13"
updated: "2026-11-12"
archived: false
license: "BSD-3-Clause"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: []
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/zhngzhom1/status/2119087220170932350"]
fetched_at: "2026-11-16T19:12:25.937604+00:00"
---

# DSH × Blender

## 出来ること

- DSHのエージェントをBlenderに接続し、シーンの確認・変更・検証・書き出しを行う。GUIでの対話操作のほか、GUIがない場合のheadlessジョブ、参照画像の計測、パラメトリック面の生成と検査、アセンブリの監査・修復、レンダー比較による受け入れ判定などをREADMEが説明している。

## 目的・背景

- エージェントが実際のBlenderセッションを確認しながら3Dシーンを作るワークフローを提供する。GUIでの逐次操作にはGUIセッションが必要で、長時間または新規シーンの処理向けにheadlessジョブ経路も用意されている。

## 依存関係

- DSHが必要。GUI経路では同梱のBlenderアドオンをインストールして有効化する。READMEは、Blender側のエージェントブリッジはこのアドオンのみを使い、旧MCP for Blender / blender_mcpなどを無効にするよう案内している。

## 実行条件

- README記載のテスト済みバージョンはBlender 4.2 LTS。Blender 4.xは動作する可能性があり、5.xは未検証。ソースからビルドする場合のみNode.js 24.9以降が必要で、npmからのインストールではDSHに同梱のランタイムを使う。GUI操作にはアドオンが必要。headless経路ではBlender実行ファイルが必要。

## 最短手順

- READMEの推奨手順は、GitHub Releasesから同梱アドオンのZIPを取得してBlenderのExtensions設定からインストール・有効化し、3DビューのNパネルからConnectする。その後、利用するDSHホストにnpmプラグインをインストールし、必要なホストではDSHを再起動する。READMEはGUI経路の確認条件をdoctor.kindがokであること、headless経路の確認条件をジョブと出力が返ることとしている。

## 変更履歴

- 2026-11-16: 初回登録
