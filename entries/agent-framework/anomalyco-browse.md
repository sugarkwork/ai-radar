---
name: "browse"
genre: "agent-framework"
url: "https://github.com/anomalyco/browse"
flags: ["unverified"]
risk_notes: "README記載の導入方法には、ダウンロードしたインストーラーを実行する手順（curl | bash、PowerShellのirm | iex、npx install）が含まれます。この候補では実行していません。"
repo: "anomalyco/browse"
stars: 669
forks: 51
open_issues: 28
size_kb: 4878
language: "TypeScript"
created: "2026-10-27"
updated: "2026-11-16"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/NFT_Chen/status/2118934674533978517"]
fetched_at: "2026-11-16T21:36:07Z"
last_release: "v0.1.0"
last_release_at: "2026-11-16"
---

# browse

## 出来ること

- browse MCPサーバーとChromium拡張機能を提供する。エージェントはPlaywrightでタブを開いて操作し、スクリーンショット取得、ネットワーク通信の記録、画面録画ができる。ログイン、二要素認証、支払いなど利用者の操作が必要な場面ではタブを利用者に引き渡し、利用者がContinueを押した後に続行する。README記載の対応ブラウザーはChrome、Edge、Brave、Arc、Helium、Vivaldi、Opera、Chromium。

## 目的・背景

- 利用者の実ブラウザー、タブ、ログイン状態、拡張機能をAIエージェントから利用できるようにする。

## 依存関係

- Chromium系ブラウザーとopencodeまたは別のMCPクライアントが必要。npxで導入する場合はNode.js 22.19以上が必要。ソースからセットアップする場合はBunも必要。

## 実行条件

- READMEには、シェルインストーラー、PowerShellインストーラー、npx、またはソースからのセットアップ方法が記載されている。導入時にはCLIバイナリの取得・インストールや拡張機能とのペアリングが行われる。ソースからのセットアップは拡張機能とCLIをビルドする。

## 最短手順

- README記載の例は `npx @opencode/browse install`。この方法にはNode.js 22.19以上が必要で、インストーラーがパッケージを導入する。導入後にブラウザー拡張機能を追加してペアリングする。実行はしていない。

## 変更履歴

- 2026-11-15: 初回登録
