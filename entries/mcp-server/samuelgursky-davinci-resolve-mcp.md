---
name: "DaVinci Resolve MCP Server"
genre: "mcp-server"
url: "https://github.com/samuelgursky/davinci-resolve-mcp"
repo: "samuelgursky/davinci-resolve-mcp"
license: "MIT"
stars: 4187
language: "Python"
created: "2025-03-18"
updated: "2026-11-18"
forks: 484
open_issues: 3
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 64026
archived: false
flags: ["unverified"]
risk_notes: "無料版向けブリッジはResolve 21.0.xまでの経路として扱うようREADMEが記載。無料版21.1でConsoleからPythonを実行できるかは未確認。Windows・Linuxの確認根拠は作者が紹介する利用者報告で、独立検証ではない。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RoundtableSpace/status/2123027189276778909"]
fetched_at: "2026-11-18T15:09:07.343350+00:00"
---

# DaVinci Resolve MCP Server

## 出来ること

- DaVinci Resolve Studioを公式Scripting API経由で操作するMCPサーバー。編集、メディアプール整理、レンダー設定、レビュー用マーカー、カラーグレーディング、Fusion、Fairlight、プロジェクト管理などの操作を提供する。README記載では標準モードは37ツール、全APIメソッド単位のモードは390ツール。ローカルのブラウザー操作パネルも同梱する。

## 目的・背景

- AIアシスタントからResolveの操作を行うためのサーバー。READMEによるとStudio版では外部スクリプティングを使用する。無料版ではResolve内でスクリプトを実行して認証付きループバック接続に再公開するブリッジ経路が説明されている。

## 依存関係

- README記載の主な前提はDaVinci ResolveとPython 3.10以降。無料版ブリッジではResolve内でPythonスクリプトを実行できる環境が必要。

## 実行条件

- セットアップ例は `npx davinci-resolve-mcp setup`。接続前にResolve Studioの Preferences > General > External scripting using を Local に設定する。無料版ブリッジはREADMEではResolve 21.0.x向けの経路として説明され、21.1ではScriptsメニューにPythonファイルが表示されないとの報告があり、Consoleからの実行可否は未確認。

## 最短手順

- README記載のセットアップコマンド `npx davinci-resolve-mcp setup` を実行し、Resolve Studioで外部スクリプティングをLocalに設定する。ソースからの場合はリポジトリをcloneして `python install.py` を実行する。無料版ブリッジを使う場合は `python scripts/install_resolve_bridge.py` の後、Resolveを再起動し、プロジェクトを開いて Workspace > Scripts > resolve_bridge を実行する。

## 変更履歴

- 2026-11-23: 初回登録
