---
name: "Kanzo"
genre: "agent-framework"
url: "https://github.com/emanuele-em/kanzo"
repo: "emanuele-em/kanzo"
stars: 1195
forks: 99
open_issues: 13
size_kb: 20321
language: "Rust"
created: "2026-10-25"
updated: "2026-11-11"
archived: false
license: "AGPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/AIExplorerTim/status/2118910064606233060"]
fetched_at: "2026-11-15T00:17:28.872334+00:00"
---

# Kanzo

## 出来ること

- ブラウザー上のボード、MCP、CLIからタスクを扱えます。エージェントはタスクの取得、カードの移動、コメントを行えます。タスクの検索・絞り込み、依存タスクの設定、複数コンピューター間でのボード共有にも対応するとREADMEに記載されています。

## 目的・背景

- 人とコーディングエージェントが同じタスクを扱うためのカンバンボード兼MCPサーバーです。READMEでは、1台のコンピューター上でも、複数台で共有するボードでも利用できると説明されています。

## 依存関係

- READMEには、MCPクライアントとの接続例としてClaude CodeとCodexが記載されています。その他の依存関係は、この資料からは確認できません。

## 実行条件

- READMEでは、`kanzo`コマンドを実行してボードを起動する手順が示されています。macOS・Linux・Raspberry Pi向けインストーラー、Windows向けインストーラーとZIP、Cargoによるインストール方法が記載されています。

## 最短手順

- README記載の手順では、インストール後に`kanzo`を実行して起動します。MCP接続では、Claude Codeは`claude mcp add kanzo --scope user -- kanzo mcp`、Codexは`codex mcp add kanzo -- kanzo mcp`を実行し、クライアントを再起動します。

## 変更履歴

- 2026-11-15: 初回登録
