---
name: "Doop"
genre: "mcp-server"
url: "https://github.com/kgoedecke/doop"
repo: "kgoedecke/doop"
license: "AGPL-3.0"
stars: 2078
language: "TypeScript"
created: "2026-08-22"
updated: "2026-11-16"
forks: 263
open_issues: 89
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 19644
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/awe0_io/status/2119067835708387501"]
fetched_at: "2026-11-16T21:54:33Z"
last_release: "desktop-v0.14.0"
last_release_at: "2026-11-16"
---

# Doop

## 出来ること

- 人とAIエージェントが共有するデザインキャンバスを提供する。フレームはサンドボックス化されたiframe内でHTMLを表示し、AIエージェントは組み込みMCPサーバーからデザインを編集できる。READMEによると、ライブカーソル、プレゼンス、フレーム編集、エージェントの状態、アクティビティフィードを共有する。

## 目的・背景

- Paper.designのオープンソース代替として紹介されている。Claude Code、Codex、ChatGPT、Cursor、OpenCodeなど、MCPクライアントから同じキャンバス上でデザインする用途を掲げている。

## 依存関係

- README記載の開発環境はBunで、サーバーはNode上で動作する。`bun run dev`および`bun run build`ではClaude Desktop拡張をNodeスクリプトでパッケージするため、NodeがPATH上に必要。標準構成は埋め込みPostgres（PGlite）を使い、外部サービスなしで動作すると説明されている。

## 実行条件

- 開発起動はREADME記載のQuickstartに従い、`git clone https://github.com/kgoedecke/doop && cd doop`、`bun install`、`bun run dev`を実行する。本番ビルドはDocker Compose、または`bun run build && bun run start`で起動できる。Docker Composeでは`BETTER_AUTH_SECRET`の設定例が示されている。

## 最短手順

- READMEのQuickstartは、`git clone https://github.com/kgoedecke/doop && cd doop`、`bun install`、`bun run dev`の順。

## 変更履歴

- 2026-11-16: 初回登録
