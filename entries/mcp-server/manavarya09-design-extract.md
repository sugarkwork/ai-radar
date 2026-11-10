---
repo: "Manavarya09/design-extract"
name: "designlang"
genre: "mcp-server"
url: "https://github.com/Manavarya09/design-extract"
stars: 5003
forks: 415
open_issues: 19
size_kb: 15954
language: "HTML"
created: "2026-04-15"
updated: "2026-11-05"
archived: false
license: "MIT"
commits_30d: 24
commits_90d: 86
commit_cadence: "daily"
last_release: "v13.3.2"
flags: ["unverified"]
risk_notes: "最新リリースの公開日時は未確認。抽出精度、サイト間での再現性、CLI・MCP の実動作は未検証。README の出力例は作者による掲載例。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117324109478507007"]
fetched_at: "2026-11-10T08:41:43+00:00"
---

# designlang — Webページからデザイントークンを抽出する CLI・MCP

## 出来ること

- 公開ページから配色、書体、余白などを抽出し、DTCG トークン、Tailwind 設定、Figma 変数用 JSON、AI に渡せる Markdown を生成する。

## 目的・背景

- Playwright でページを描画し、ライブ DOM の計算済みスタイルを集めて再利用可能な形式に整理する。README は出力例を掲載している。

## 依存関係

- パッケージ定義上は Node.js 20 以上。主な依存は Playwright と MCP SDK。

## 実行条件

- 対象 URL にアクセスできる環境と Chromium または Google Chrome が必要。README では `designlang install-browser` で対応する Chromium を準備できる。リポジトリは MIT。抽出元サイトの素材を再利用する条件は、その素材の権利に従う。

## 最短手順

- CLI ではブラウザを準備し、`npx designlang <公開URL>` を実行して `design-extract-output/` のトークンや Markdown を読む。
- Claude Code では `claude mcp add designlang -- npx -y designlang mcp` で登録し、エージェントから `extract_design` に公開 URL を渡す。返ったジョブ ID で `get_job_status` を確認し、完了後に `get_tokens` で結果を取得する。

## 変更履歴

- 2026-11-10: 初回登録
