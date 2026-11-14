---
name: "Moodle-MCP"
genre: "mcp-server"
url: "https://github.com/Faixiang/Moodle-MCP"
repo: "Faixiang/Moodle-MCP"
flags: ["unverified"]
risk_notes: "利用にはWeb ServicesとREST protocolが有効なMoodle 3.x/4.xサイト、およびwebservice/rest:use capabilityを持つアカウントが必要。ファイルのローカル保存機能を使う場合は保存先を指定する。"
stars: 206
forks: 0
open_issues: 0
size_kb: 265
language: "Python"
created: "2026-10-26"
updated: "2026-11-01"
archived: false
license: "MIT"
commits_30d: 20
commits_90d: 20
commit_cadence: "daily"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/Ryrenz/status/2118707230270763082"]
fetched_at: "2026-11-13T19:10:39.944066+00:00"
---

# Moodle-MCP

## 出来ること

- MoodleのWeb Service APIから、登録コース、最近の更新、未提出課題と期限、クイズの受験状態、コース内ファイル情報を取得するMCPツールを提供する。週次ダイジェストも生成できる。READMEでは10個の読み取り系ツールを説明し、別途、moodle_download_weekによる週単位のファイル保存機能も記載している。

## 目的・背景

- READMEによると、Moodleには汎用MCPサーバーがなく、ブラウザー操作による取得は遅く壊れやすいとして、Moodle標準のREST APIを利用するラッパーとして作られた。

## 依存関係

- Python 3.8以上。READMEではPython標準ライブラリのみを使い、追加依存関係はないとしている。MCP protocolは2024-11-05。

## 実行条件

- Moodle 3.x/4.xでWeb ServicesとREST protocolが有効であること、アカウントがwebservice/rest:use capabilityを持つことが必要。URLと個人アクセストークンを環境変数またはconfig.jsonで設定する。READMEではMoodle 4.3.6、435個の関数許可で検証したと報告している。

## 最短手順

- READMEの手順では、Moodleで個人アクセストークンを作成し、MOODLE_URLとMOODLE_TOKENを環境変数に設定するか、server.pyの隣にconfig.jsonを用意する。MCPクライアントの設定にpythonとserver.pyの絶対パスを登録し、moodle_site_infoを呼び出して接続を確認する。

## 変更履歴

- 2026-11-14: 初回登録
