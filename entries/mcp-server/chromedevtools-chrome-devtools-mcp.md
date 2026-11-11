---
name: "Chrome DevTools for agents"
genre: "mcp-server"
url: "https://github.com/ChromeDevTools/chrome-devtools-mcp"
repo: "ChromeDevTools/chrome-devtools-mcp"
flags: ["unverified"]
risk_notes: "使用統計は既定で有効。MCPクライアントはブラウザー内の情報を閲覧・変更できる。公式サポート対象はGoogle ChromeとChrome for Testing。"
stars: 55061
forks: 4579
open_issues: 129
size_kb: 21871
language: "TypeScript"
created: "2025-09-11"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/nuannuan_share/status/2119640438135242817"]
fetched_at: "2026-11-10T15:14:33.512147+00:00"
---

# Chrome DevTools for agents

## 出来ること

- MCPサーバーまたはCLIを通じて、エージェントから起動中のChromeを操作・調査する。READMEには、DevToolsによるトレース記録とパフォーマンス分析、ネットワークリクエスト・スクリーンショット・コンソールメッセージの確認、Puppeteerによるブラウザー操作が記載されている。

## 目的・背景

- コーディングエージェントにChrome DevToolsを利用させ、ブラウザーの自動化、デバッグ、パフォーマンス分析を行えるようにする。

## 依存関係

- README記載の要件はNode.jsのLTS版、Chromeの現行安定版以降、npm。

## 実行条件

- READMEではGoogle ChromeとChrome for Testingのみを公式サポート対象としている。MCPサーバーは、実行中のブラウザーを必要とするツールが初めて使われたときにブラウザーを自動起動する。

## 最短手順

- MCPクライアントに `command: "npx"`、`args: ["-y", "chrome-devtools-mcp@latest"]` を設定する。READMEの動作確認例は、クライアントから `Check the performance of https://developers.chrome.com` を入力すること。

## 変更履歴

- 2026-11-11: 初回登録
