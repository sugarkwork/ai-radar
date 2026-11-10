---
repo: "GLips/Figma-Context-MCP"
name: "Framelink MCP for Figma"
genre: "mcp-server"
url: "https://github.com/GLips/Figma-Context-MCP"
license: "MIT"
stars: 16187
language: "TypeScript"
created: "2025-02-13"
updated: "2026-10-27"
forks: 1282
open_issues: 29
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 8185
archived: false
last_release: "v0.13.2"
last_release_at: "2026-06-18"
flags: ["unverified"]
risk_notes: "スクリーンショット入力に対する再現精度の優位性は作者の主張。実行による再現、Claude Code固有の設定と互換性、Figmaのプラン別料金・API利用条件は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2114739076796428729"]
fetched_at: "2026-11-10T11:34:45+00:00"
---

# Framelink MCP for Figmaでデザイン情報をAIエージェントに渡す

## 出来ること

- Figmaのファイル、フレーム、グループのリンクをもとにレイアウトやスタイルを取得し、UI実装の文脈としてエージェントに渡せる。

## 目的・背景

- Figma APIの応答を簡略化し、実装に関係するレイアウトとスタイルをモデルに渡す。READMEはスクリーンショットを貼る方法より正確に一度で実装できると述べている。比較精度は未検証。

## 依存関係

- MCP対応クライアント、Node.js 20.20.0以上、npx、対象デザインを参照できるFigmaアクセストークンが必要。

## 実行条件

- READMEのローカル構成ではstdioで接続し、クライアント設定の環境変数FIGMA_API_KEYにトークンを設定できる。リポジトリはMITライセンス。Figma側の料金とプラン別API利用条件は未確認。

## 最短手順

- MCPクライアントに起動コマンドとして npx -y figma-developer-mcp --stdio を登録し、環境変数FIGMA_API_KEYを設定する。WindowsではREADMEに従いcmd /c経由で起動する。
- Cursorなどのエージェントチャットに対象のFigmaリンクを貼り、MCPツールget_figma_dataでデザイン情報を取得してUIを実装するよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
