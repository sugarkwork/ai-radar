---
name: "zlib"
genre: "coding-agent"
url: "https://github.com/heartleo/zlib"
flags: ["unverified"]
risk_notes: "利用にはZ-Libraryアカウントが必要とREADMEに記載されています。利用可能なドメインやダウンロード条件の詳細はREADME本文では確認できません。"
repo: "heartleo/zlib"
stars: 1860
forks: 135
open_issues: 0
size_kb: 10621
language: "Go"
created: "2026-04-10"
updated: "2026-11-13"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118716534314897487"]
fetched_at: "2026-11-13T20:14:25.538843+00:00"
---

# zlib

## 出来ること

- ターミナルから書籍を検索し、結果の閲覧、ダウンロード、Kindleへの送信、WeReadへの取り込みができます。Claude CodeとCodex向けのエージェントプラグイン、およびローカルstdioのMCPサーバー連携もREADMEに記載されています。出典: https://github.com/heartleo/zlib#features

## 目的・背景

- READMEでは「A Z-Library CLI for you and your AI agents.」と説明されています。出典: https://github.com/heartleo/zlib

## 依存関係

- READMEはGoのCLIとして案内しています。MCPサーバーの利用にはzlibをPATH上で利用可能にし、サインインしておく必要があります。具体的な依存パッケージ一覧は添付READMEからは確認できません。出典: https://github.com/heartleo/zlib#agent-setup

## 実行条件

- クイックスタートにはZ-Libraryアカウントが必要と記載されています。利用するドメインはネットワークから到達可能なものを確認する手順です。出典: https://github.com/heartleo/zlib#quick-start

## 最短手順

- README記載のCodexプラグイン手順は `codex plugin marketplace add heartleo/zlib`、続いて `codex plugin add zlib@zlib` です。MCPを使う場合は `codex mcp add zlib -- zlib mcp` と記載されています。いずれもREADME上の手順で、ここでは実行確認していません。出典: https://github.com/heartleo/zlib#agent-setup

## 変更履歴

- 2026-11-14: 初回登録
