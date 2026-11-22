---
name: "Taste — Design DNA Extractor"
genre: "coding-agent"
url: "https://github.com/senlindesign/taste-skill"
repo: "senlindesign/taste-skill"
license: "unknown"
stars: 493
language: "JavaScript"
created: "2026-05-24"
updated: "2026-07-07"
forks: 43
open_issues: 7
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 10130
archived: false
flags: ["unverified"]
risk_notes: "READMEのライセンスバッジはMITを示すが、ライセンス本文は確認できていない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/suraj_sharma14/status/2122585528906518837"]
fetched_at: "2026-11-18T00:44:35.716232+00:00"
---

# Taste — Design DNA Extractor

## 出来ること

- 任意のWebサイトを解析し、デザインマップと「Taste DNA」をMarkdownおよびJSONで出力する。背景色・書体・角丸などの計測値に加え、デザイン原則、その根拠、判断理由、トレードオフをまとめる。CursorやWindsurfなど9種類のビルドツール向け形式にも出力できる。

## 目的・背景

- READMEでは、色や余白などのトークンだけでなく、その選択理由やトレードオフも抽出し、未見のページにも適用できるデザインガイダンスを作ることを目的としている。

## 依存関係

- README記載の前提はClaude CodeまたはGemini CLIとPlaywright MCP。初回のブラウザー操作時にPlaywrightがChromiumをダウンロードすると説明されている。

## 実行条件

- ログイン後のページや自動アクセスをブロックするサイトは対象外とREADMEに記載。解析時に単一ページか同一サイト内のリンク先2〜3ページも調べるかを選択できる。

## 最短手順

- Claude Codeではリポジトリを`~/.claude/skills/taste`へcloneし、`claude mcp add playwright -s user -- npx -y @playwright/mcp@latest --isolated`でPlaywright MCPを設定して再起動する。Gemini CLIの導入手順と設定例もREADMEにある。セットアップ後、`/taste <url>`を実行する。

## 変更履歴

- 2026-11-22: 初回登録
