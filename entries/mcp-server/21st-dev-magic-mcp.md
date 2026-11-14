---
name: "21st MCP compatibility proxy (formerly Magic MCP)"
genre: "mcp-server"
url: "https://github.com/21st-dev/magic-mcp"
repo: "21st-dev/magic-mcp"
license: "ISC"
stars: 6482
language: "TypeScript"
created: "2025-02-19"
updated: "2026-09-09"
forks: 531
open_issues: 9
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 5
size_kb: 1548
archived: false
flags: ["unverified"]
risk_notes: "旧Magic APIキーは無効で、新しいAPIキーが必要です。AI生成ツールはアカウントでAIアクセスが有効な場合に限り一覧に表示され、利用可能なAIクレジット残量はREADMEから確認できません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/thegreatest_sv/status/2118770137646162218"]
fetched_at: "2026-11-14T04:13:04.640182+00:00"
---

# 21st MCP compatibility proxy (formerly Magic MCP)

## 出来ること

- 既存の`@21st-dev/magic`設定からMCPメッセージを21st MCPへ転送するstdio互換プロキシとして動作します。21st MCPでは、アカウントで利用可能なツールが提供され、READMEにはコンポーネント等の検索、コード取得、ブックマーク、チームライブラリ、UI生成などが記載されています。AI生成ツールの表示にはAIアクセスの有効化が必要です。

## 目的・背景

- Magic MCPは21st MCPに置き換えられ、このパッケージは旧設定を維持するための互換プロキシとして公開されています。READMEは新規設定では21st CLIによる初期化を推奨しています。旧Magic APIキーはリセットされ、利用できません。

## 依存関係

- 接続先として21st MCP（`https://21st.dev/api/mcp`）と、利用者の新しいAPIキーが必要です。READMEはstdioプロキシ方式とHTTP MCPサーバー方式を記載しています。

## 実行条件

- README記載の手順では、21st CLIを使う場合にNode.jsの`npx`と対応クライアント（Cursor、Claude、VS Code、Windsurf、Codex）が必要です。互換プロキシ利用時はAPIキーを引数または`TWENTY_FIRST_API_KEY`／`API_KEY_21ST`環境変数で渡します。AI生成機能の利用にはアカウントのAIアクセス有効化が必要です。

## 最短手順

- READMEの推奨手順は`npx @21st-dev/cli@latest init --client cursor`です（`cursor`は利用クライアントに合わせて変更）。手動設定ではMCP URLを`https://21st.dev/api/mcp`にし、21st MCPで発行したAPIキーをヘッダーに設定します。

## 変更履歴

- 2026-11-14: 初回登録
