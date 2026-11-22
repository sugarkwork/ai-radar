---
name: "Oxylabs Web API — MCP Server"
genre: "mcp-server"
url: "https://github.com/oxylabs/web-api-mcp"
repo: "oxylabs/web-api-mcp"
license: "MIT"
stars: 58
language: "Python"
created: "2026-08-23"
updated: "2026-11-09"
forks: 9
open_issues: 0
commits_30d: 28
commit_cadence: "daily"
commits_90d: 70
size_kb: 210
archived: false
flags: ["unverified"]
risk_notes: "利用にはOxylabs Web APIキーが必要です。APIの料金・利用枠はREADMEに記載がなく、費用は確認できません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/DivyanshT91162/status/2119134534134600107"]
fetched_at: "2026-11-17T07:15:57.547500+00:00"
---

# Oxylabs Web API — MCP Server

## 出来ること

- Oxylabs Web APIへのMCP接続を提供します。READMEによると、searchはライブWebの検索結果を返し、scrapeはURLをMarkdownまたは指定したJSON形式で取得します。list_scrapersで利用可能な専用スクレイパーとパラメーターを確認でき、run_scraperで実行できます。check_requestsはバックグラウンド処理の完了確認、read_resultは長いページの分割読み取りに使います。READMEでは6つのツールすべてにreadOnlyHintが付与されていると説明しています。

## 目的・背景

- MCP対応エージェントにOxylabs Web API経由のWeb検索・ページ取得機能を提供する、開発者向けの技術資料およびMCPサーバーです。Remote MCPはOxylabs側でホスト・保守され、self-hostedは利用者側でインストール・運用します。

## 依存関係

- Remote MCPには、カスタムヘッダーを扱えるリモートMCPクライアントとOxylabs Web APIキーが必要です。self-hostedにはPython 3.10以上、uv、およびOxylabs Web APIキーが必要です。

## 実行条件

- Remote MCPの接続先は https://mcp.oxylabs.io/web-api-mcp です。リクエストにWeb APIキーをAuthorizationヘッダーで渡します。self-hostedはstdioまたはHTTP transportで起動できます。HTTP transportではMCP_ALLOWED_HOSTSに接続先ホストを設定する必要があります。OAuthログインのみでカスタムヘッダーを送れないクライアントはRemote MCPに接続できず、READMEはself-hostedを案内しています。

## 最短手順

- Remote MCPを使う場合、Oxylabs Web APIキーを環境変数OXYLABS_WEB_API_KEYに設定し、MCPクライアントに https://mcp.oxylabs.io/web-api-mcp とキーを渡す設定を追加します。self-hostedの場合はREADMEの手順に従ってuv tool install git+https://github.com/oxylabs/web-api-mcpでインストールし、クライアントからoxylabs-web-api-mcpコマンドを起動する設定を行います。キーは環境変数または.envファイルで渡します。

## 変更履歴

- 2026-11-22: 初回登録
