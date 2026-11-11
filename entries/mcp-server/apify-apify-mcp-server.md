---
name: "Apify MCP server"
genre: "mcp-server"
url: "https://github.com/apify/apify-mcp-server"
repo: "apify/apify-mcp-server"
flags: ["unverified"]
risk_notes: "Actorの料金や実行条件は個々のActorによって異なる可能性があるが、READMEから一律の条件や費用は確認できない。記載された効果はREADME上の説明であり、独立検証していない。"
stars: 15564
forks: 444
open_issues: 253
size_kb: 10980
language: "TypeScript"
created: "2025-01-02"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Y0urDumble/status/2116341413755453670"]
fetched_at: "2026-11-10T13:38:35.474660+00:00"
---

# Apify MCP server

## 出来ること

- Apify StoreのActorsを通じて、エージェントにウェブスクレイピング、データ抽出、ブラウザ自動化の機能を提供する。エージェントはActorを検索し、入力と料金を確認して実行し、構造化された結果を受け取る。

## 目的・背景

- サイトごとに別々のMCPサーバーを導入せずに、Apify MCPサーバーへの接続から必要なActorを利用する構成として説明されている。

## 依存関係

- ローカルstdio版はNode.js 22以降が必要。ローカルパッケージはnpmの`@apify/actors-mcp-server`。ホスト型は`https://mcp.apify.com`。

## 実行条件

- ホスト型はOAuthで接続する方法が案内されている。OAuthを利用できないクライアントでは、AuthorizationヘッダーにApify APIトークンを渡す方法が記載されている。ローカル版はstdioで実行し、APIトークンまたはApify CLIに保存したトークンを利用できる。

## 最短手順

- ホスト型はMCP configuratorでクライアントと利用するツールを選び、生成された設定をクライアントに登録して、ブラウザーでApifyにサインインする。ローカル版はクライアント設定に`npx -y @apify/actors-mcp-server`を登録し、`APIFY_TOKEN`を設定する。

## 変更履歴

- 2026-11-11: 初回登録
