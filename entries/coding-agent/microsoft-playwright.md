---
name: "Playwright"
genre: "coding-agent"
url: "https://github.com/microsoft/playwright"
repo: "microsoft/playwright"
license: "Apache-2.0"
stars: 99952
language: "TypeScript"
created: "2019-11-15"
updated: "2026-11-12"
forks: 6855
open_issues: 30
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 246944
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/kursormaxx/status/2118673610722144590"]
fetched_at: "2026-11-12T11:11:07.075000+00:00"
---

# Playwright

## 出来ること

- 公式READMEによると、PlaywrightはChromium・Firefox・WebKitを共通APIで操作するWeb自動化・テスト用フレームワーク。Playwright TestはブラウザーをまたぐE2Eテスト、CLIはコーディングエージェント向けブラウザー操作、MCPサーバーはアクセシビリティスナップショットを用いたAIエージェント連携、ライブラリーはテストランナーを使わない自動化スクリプトに利用できる。Playwright Testには自動待機、再試行するアサーション、テストごとのブラウザーコンテキスト分離、失敗時のトレース等が記載されている。

## 目的・背景

- テスト、スクリプト、AIエージェントからブラウザーを操作するための共通APIを提供する。READMEでは用途に応じてPlaywright Test、CLI、MCP、Libraryを選ぶ構成を案内している。

## 依存関係

- READMEにある導入例はNode.js/npmを使用する。Playwright Testの手動導入例では@playwright/testとnpx playwright install、CLIでは@playwright/cli、MCPでは@playwright/mcpを利用する。ランタイムやブラウザーの詳細な対応条件はこのREADME抜粋からは確認できない。

## 実行条件

- READMEの例ではnpmによる導入後、テストはnpx playwright test、CLIはplaywright-cliコマンド、MCPは対応クライアントのMCP設定から利用する。例ではブラウザーの起動、ページへのアクセス、操作を行う。環境ごとの詳細な要件はREADME抜粋からは確認できない。

## 最短手順

- E2Eテストは `npm init playwright@latest` で開始し、テストを作成して `npx playwright test` を実行する。コーディングエージェント向けCLIは `npm install -g @playwright/cli@latest`、MCPサーバーはクライアント設定に `npx @playwright/mcp@latest` を指定する。ライブラリーは `npm i playwright` で導入する。これらはREADME記載の手順であり、ここで実行確認はしていない。

## 変更履歴

- 2026-11-12: 初回登録
