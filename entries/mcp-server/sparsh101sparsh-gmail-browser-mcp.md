---
name: "gmail-browser-mcp"
genre: "mcp-server"
url: "https://github.com/sparsh101sparsh/gmail-browser-mcp"
repo: "sparsh101sparsh/gmail-browser-mcp"
license: "unknown"
stars: 0
language: "TypeScript"
created: "2026-11-11"
updated: "2026-11-13"
forks: 0
open_issues: 0
commits_30d: 88
commit_cadence: "daily"
commits_90d: 88
size_kb: 984
archived: false
flags: ["low-quality", "unverified"]
risk_notes: "作者自身がX投稿で「not in production stage」「you need to configure multiple things by yourself」と説明。 作者の説明では本番利用段階ではなく、複数の設定を利用者が行う必要がある。必要な設定項目と本番利用条件は今回確認した資料だけでは特定できない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/issparssh/status/2121389152768008212"]
fetched_at: "2026-11-14T01:10:47Z"
---

# gmail-browser-mcp

## 出来ること

- GitHubの説明ではPlaywrightを使ったブラウザー自動化によるGmail MCPサーバー。package.jsonは製品説明として「Local browser-automated Gmail MCP server using Playwright and persistent user profile」と記載。機能の詳細な説明は今回確認した一次資料では不明。

## 目的・背景

- 作者のX投稿ではGmail MCPサーバーを仕上げた段階と説明し、別投稿ではChromeの永続ユーザープロファイルを使う方式へ変更したと述べている。これは作者の報告であり、独立した性能測定ではない。

## 依存関係

- package.jsonに記載された依存関係は@modelcontextprotocol/sdk ^1.18.1、playwright ^1.50.0。開発依存は@types/node ^24.5.2、typescript ^5.9.2。

## 実行条件

- package.jsonはNode.jsからdist/index.jsを起動するstartスクリプトと、TypeScriptをビルドするbuildスクリプトを記載。作者のX投稿によれば本番段階ではなく複数の設定が必要だが、設定内容や必要バージョンの詳細は確認できていない。

## 最短手順

- package.jsonで確認できる手順は、依存関係を用意しnpm run buildでビルド後、npm startでdist/index.jsを起動する方法。GmailやMCPクライアントの具体的な設定方法は、今回確認できた資料では不明。

## 変更履歴

- 2026-11-14: 初回登録
