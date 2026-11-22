---
type: "repo"
repo: "vercel-labs/agent-browser"
name: "agent-browser"
genre: "agent"
url: "https://github.com/vercel-labs/agent-browser"
license: "Apache-2.0"
stars: 51976
language: "Rust"
created: "2026-01-11"
updated: "2026-11-16"
forks: 3629
open_issues: 589
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 36539
archived: false
added: "2026-11-09"
fetched_at: "2026-11-16T21:35:41Z"
flags: ["unverified"]
risk_notes: "Apache-2.0。要素が隠れている等でクリック失敗する場合がある。更新された画面の古いrefを再利用しない。 実行・品質は未検証。"
sources: ["https://x.com/i/status/2119588334615802105", "https://github.com/vercel-labs/agent-browser"]
last_release: "v0.43.0"
last_release_at: "2026-11-12"
---

# agent-browser

## 出来ること

アクセシビリティツリーの要素にrefを付け、エージェントがCLIから開く・読む・クリックする。CDP接続やMCPにも対応。

## 目的・背景

Vercel Labs製ブラウザ自動操作CLI。refは取得時点の画面に対応する。

## 依存関係

配布版はnpmまたはHomebrew、ブラウザのインストールが必要。

## 実行条件

Windows / macOS / Linux対応。ログイン情報や外部サイトの操作権限を扱う。

## 最短手順

`npm install -g agent-browser`、`agent-browser install`。操作後は再度snapshotを取得する。

## 注意点

Apache-2.0。要素が隠れている等でクリック失敗する場合がある。更新された画面の古いrefを再利用しない。 実行・品質は未検証。

## 出典

- [公式リポジトリ](https://github.com/vercel-labs/agent-browser)
- [紹介投稿](https://x.com/i/status/2119588334615802105)
