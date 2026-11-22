---
name: "boss-agent-cli"
genre: "coding-agent"
url: "https://github.com/can4hou6joeng4/boss-agent-cli"
repo: "can4hou6joeng4/boss-agent-cli"
license: "MIT"
stars: 2225
language: "Python"
created: "2026-03-20"
updated: "2026-11-16"
forks: 194
open_issues: 8
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 64222
archived: false
flags: []
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
risk_notes: ""
sources: ["https://x.com/bkdgiffug/status/2118983795194069108"]
fetched_at: "2026-11-16T21:42:52Z"
last_release: "v3.4.72"
last_release_at: "2026-11-16"
---

# boss-agent-cli

## 出来ること

- READMEによると、BOSS直聘向けに求職者の求人検索、福利厚生条件による絞り込み、候補求人の整理、AIによる求人票・履歴書関連の支援、応募者と採用者のワークフローを提供する。CLI、JSON、MCP、Python APIから利用できる。

## 目的・背景

- READMEは、求人発見、福利厚生による絞り込み、ローカルの履歴書とAI、応募時のやり取り、採用者の候補者処理、再開可能な収集を一つのCLIにまとめると説明している。

## 依存関係

- READMEにはPython ≥3.11と記載されている。MCP連携は boss-agent-cli[mcp]、一括収集は追加の crawl extra が必要。

## 実行条件

- READMEに記載された登録プラットフォームはBOSS直聘（zhipin）。ログインが必要な操作があり、収集機能は独立したChromeプロファイルを使う。ブラウザー操作やプラットフォーム上の動作はこの資料から独立検証されていない。

## 最短手順

- README記載の手順は `uv tool install boss-agent-cli` の後に `boss` を起動する。環境確認には `boss doctor` を使う。ログインや求人操作はこの確認では実行していない。

## 変更履歴

- 2026-11-15: 初回登録
