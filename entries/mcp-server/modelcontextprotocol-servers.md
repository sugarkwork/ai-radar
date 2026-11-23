---
name: "Model Context Protocol servers"
genre: "mcp-server"
url: "https://github.com/modelcontextprotocol/servers"
repo: "modelcontextprotocol/servers"
license: "unknown"
stars: 92077
language: "TypeScript"
created: "2024-11-19"
updated: "2026-11-18"
forks: 11978
open_issues: 38
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 34304
archived: false
flags: ["unverified"]
risk_notes: "READMEによると、これらは教育・開発向けのリファレンス実装で、本番環境向けではありません。利用時は用途に応じてセキュリティ要件と保護策を評価してください。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/cc_lab_jp/status/2119195718661374413"]
fetched_at: "2026-11-18T07:12:02.270608+00:00"
---

# Model Context Protocol servers

## 出来ること

- MCPの機能とSDKの利用例を示すリファレンスサーバー群です。READMEでは、Everything（プロンプト・リソース・ツールを含むテストサーバー）、Fetch（Webコンテンツ取得と変換）、Filesystem（アクセス制御付きファイル操作）、Git（Gitリポジトリの読み取り・検索・操作）、Memory（知識グラフ型の永続メモリ）、Sequential Thinking、Timeを紹介しています。

## 目的・背景

- MCPの機能や公式SDKを示すための参照実装です。READMEは、教育用の開発者向け例であり、本番環境向けのソリューションではないと説明しています。

## 依存関係

- READMEは、各サーバーが通常MCP SDKで実装されると説明し、C#、Go、Java、Kotlin、PHP、Python、Ruby、Rust、Swift、TypeScriptのSDKを列挙しています。個別サーバーの依存関係はここでは確認していません。

## 実行条件

- READMEの例では、TypeScriptサーバーはnpx、Pythonサーバーはuvxまたはpipで起動します。例としてMemoryは `npx -y @modelcontextprotocol/server-memory`、Gitは `uvx mcp-server-git` またはpipでインストール後に `python -m mcp_server_git` で起動します。クライアント設定に登録して使用する例もあります。READMEによると、全サーバーがstdioに対応し、EverythingのみStreamable HTTPにも対応します。

## 最短手順

- Claude Desktopの設定例では、`mcpServers`にサーバー名、起動コマンド、引数を登録します。Memoryの場合は `command` を `npx`、`args` を `["-y", "@modelcontextprotocol/server-memory"]` とします。WindowsではREADMEの例に従い、npxの `command` を `cmd` にして `args` の先頭に `/c`, `npx` を加えます。

## 変更履歴

- 2026-11-23: 初回登録
