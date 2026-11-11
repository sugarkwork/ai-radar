---
repo: "shadcn-ui/ui"
name: "shadcn/ui"
genre: "mcp-server"
url: "https://github.com/shadcn-ui/ui"
last_release: "shadcn@4.23.0"
flags: ["unverified"]
risk_notes: "MCP の接続とコンポーネント追加は公式手順で確認した。実行時の互換性、生成結果の品質、作業時間の短縮効果は実測していない。最新リリースの公開日時は未確認。"
stars: 127807
forks: 11332
open_issues: 1776
size_kb: 75193
language: "TypeScript"
created: "2023-01-04"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 84
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116190137948254226"]
fetched_at: "2026-11-10T13:00:07+00:00"
---

# shadcn/ui の公式 MCP で UI コンポーネントを探して追加する

## 出来ること

- Claude Code などの MCP 対応クライアントから、設定済みレジストリのコンポーネントやテンプレートを一覧表示・検索し、自然言語でプロジェクトへの追加を依頼できる。[公式 MCP ドキュメント](https://ui.shadcn.com/docs/mcp)

## 目的・背景

- コンポーネントを編集可能なソースコードとして配布し、プロジェクト側で見た目や挙動を調整できるようにする。[公式 README](https://raw.githubusercontent.com/shadcn-ui/ui/main/README.md)

## 依存関係

- Claude Code などの MCP クライアントと、shadcn CLI を起動する pnpm や npx が必要。標準レジストリは追加設定なしで使え、外部レジストリは components.json で指定する。[公式 MCP ドキュメント](https://ui.shadcn.com/docs/mcp)

## 実行条件

- Claude Code ではプロジェクトの .mcp.json からサーバーを起動し、再起動後に /mcp で接続状態を確認できる。リポジトリは MIT ライセンス。外部レジストリの素材の利用条件や、利用する AI クライアントの料金は個別に確認が必要。[公式 MCP ドキュメント](https://ui.shadcn.com/docs/mcp)、[公式 README](https://raw.githubusercontent.com/shadcn-ui/ui/main/README.md)

## 最短手順

- 対象プロジェクトで `pnpm dlx shadcn@latest mcp init --client claude` を実行する。
- Claude Code を再起動し、`/mcp` で shadcn の接続を確認する。
- Claude Code に「shadcn レジストリでボタンを探して、このプロジェクトに追加して」と依頼する。[公式クイックスタート](https://ui.shadcn.com/docs/mcp#quick-start)

## 変更履歴

- 2026-11-11: 初回登録
