---
name: "IDA Pro MCP"
genre: "mcp-server"
url: "https://github.com/mrexodia/ida-pro-mcp"
repo: "mrexodia/ida-pro-mcp"
license: "MIT"
stars: 13525
language: "Python"
created: "2025-03-25"
updated: "2026-11-12"
forks: 1660
open_issues: 59
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 27
size_kb: 2447
archived: false
flags: ["unverified"]
risk_notes: "作者は公式Hex-Rays IDA MCP Serverの利用を推奨し、GUI向けMCPプラグインは非推奨化予定と記載しています。IDA Freeは非対応です。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:21:41.307599+00:00"
---

# IDA Pro MCP

## 出来ること

- IDA ProのデータベースをMCP経由でLLMクライアントから調査するサーバーです。READMEは、デコンパイル結果や逆アセンブルを確認し、コメント追加、変数名・型・関数名の整理、解析報告の作成といった使い方を例示しています。idalibを使うヘッドレス構成では、バイナリを指定して起動する方法と、後からidb_openでファイルを開く方法が記載されています。これらはREADME記載の機能・手順であり、独立した動作検証ではありません。

## 目的・背景

- IDA Proを使ったリバースエンジニアリングをMCPクライアントから支援することを目的としています。作者はREADME冒頭で公式Hex-Rays IDA MCP Serverの利用を推奨し、GUI向けプラグインについては非推奨化予定としています。

## 依存関係

- README記載の前提はPython 3.11以上、IDA Pro 8.3以上（9推奨。IDA Freeは非対応）、対応MCPクライアントです。idalibを利用する場合はidalibのグローバル有効化とuvのインストールが必要と記載されています。

## 実行条件

- GUIプラグイン方式ではpipでインストール後、ida-pro-mcp --installを実行し、IDAとMCPクライアントを再起動する手順です。ヘッドレス方式ではidalib-mcpをuv runで起動し、--host、--port、必要に応じてバイナリパスを指定します。stdioクライアント向けの起動例もあります。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- idalibを使う場合、まずIDA付属のpy-activate-idalib.pyをuv runで実行して有効化し、READMEの例に従ってuv run idalib-mcp --host 127.0.0.1 --port 8745 path/to/executableを起動します。MCPクライアントで接続して解析対象を調べます。READMEにはCodex向けプラグインの追加コマンドもありますが、作者は公式サーバーを推奨しています。

## 変更履歴

- 2026-11-23: 初回登録
