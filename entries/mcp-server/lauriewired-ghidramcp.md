---
name: "ghidraMCP"
genre: "mcp-server"
url: "https://github.com/LaurieWired/GhidraMCP"
repo: "LaurieWired/GhidraMCP"
license: "Apache-2.0"
stars: 11978
language: "Java"
created: "2025-03-23"
updated: "2026-10-10"
forks: 1319
open_issues: 96
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 3
size_kb: 414
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:21:36.810148+00:00"
---

# ghidraMCP

## 出来ること

- README では、Ghidra のバイナリ解析・デコンパイル、メソッドやデータの自動リネーム、メソッド・クラス・インポート・エクスポートの一覧取得を MCP ツールとして提供すると説明されています。

## 目的・背景

- LLM が MCP クライアント経由で Ghidra の機能を利用し、アプリケーションを自律的にリバースエンジニアリングできるようにするサーバーとプラグインです。

## 依存関係

- README 記載の通常利用では Ghidra 12.1.4 と uv（または Python 3.10 以上）が必要です。ヘッドレス実行には PyGhidra、GhidraMCP 拡張機能、Python 3.10〜3.13、Ghidra 12.1.4、および GHIDRA_INSTALL_DIR の設定が必要です。

## 実行条件

- Ghidra GUI を使う場合は、リリースの拡張 ZIP を Ghidra にインストールして再起動し、GhidraMCPPlugin を有効にします。MCP クライアントの接続先 IP とポートを設定でき、README 記載の既定値は localhost:8080 です。GUI なしでは --headless と --binary を指定して実行できます。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README に従い、Ghidra 12.1.4 と uv を用意し、GitHub Releases から拡張 ZIP を取得します。Ghidra の File → Install Extensions で ZIP を追加して再起動し、GhidraMCPPlugin を有効にした後、MCP クライアントの設定に README の ghidra-mcp 起動コマンドを登録します。

## 変更履歴

- 2026-11-23: 初回登録
