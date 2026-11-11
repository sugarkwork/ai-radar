---
repo: "every-app/open-seo"
name: "OpenSEO"
genre: "mcp-server"
url: "https://github.com/every-app/open-seo"
stars: 27127
forks: 3759
open_issues: 109
size_kb: 38925
language: "TypeScript"
created: "2026-02-27"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "MCP接続とセルフホストは公式手順の確認まで。検索データの精度、他製品との比較、最新リリース、Cloudflare無料枠での稼働は未確認。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/opensourcelab9/status/2115934204165062890"]
fetched_at: "2026-11-10T12:48:03+00:00"
---

# OpenSEO — CodexやClaude CodeからSEOデータを調べるMCP

## 出来ること

- キーワード調査、順位追跡、競合分析、被リンク調査、サイト監査、AI検索での可視性調査を扱う。公式MCPガイドでは、検索量・難易度・CPCやGoogleのオーガニック検索結果をAIクライアントから取得できるとしている。

## 目的・背景

- SEOデータをAIの調査に取り込めるよう、MCPがデータ取得を担い、スキルがキーワード調査や競合分析の進め方を定義する。MITライセンス。

## 依存関係

- セルフホストのSEOデータ取得にはDataForSEOのAPIキーが必要で、利用料は同社へ直接支払う。Docker版では一部のAI調査・生成機能にOpenRouterのキーも使う。

## 実行条件

- 公式READMEにはDockerとCloudflareのセルフホスト手順がある。Docker版はDocker ComposeとDocker用メモリ4 GiB以上が必要。ホスト版MCPは初回接続時にOpenSEOで認可する。

## 最短手順

- Codex CLIで `codex mcp add openseo --url https://app.openseo.so/mcp` を実行し、表示されるOpenSEOの認可を完了する。
- Codexに『OpenSEOで対象キーワードの検索量・難易度・CPCを調べて』と依頼する。スキルも使う場合は、公式ガイドに沿ってOpenSEOプラグインを導入する。

## 変更履歴

- 2026-11-11: 初回登録
