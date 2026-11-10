---
repo: "stripe/ai"
name: "stripe/ai"
genre: "agent-framework"
url: "https://github.com/stripe/ai"
author: "stripe"
license: "MIT"
stars: 2052
language: "TypeScript"
created: "2024-11-11"
updated: "2026-11-09"
forks: 386
open_issues: 43
commits_30d: 56
commits_90d: 100
commit_cadence: "daily"
size_kb: 15295
archived: false
last_release: ""
last_release_at: ""
sources: ["https://github.com/stripe/ai", "https://api.github.com/repos/stripe/ai", "https://raw.githubusercontent.com/stripe/ai/main/README.md", "https://raw.githubusercontent.com/stripe/ai/main/benchmarks/README.md", "https://docs.stripe.com/mcp", "https://x.com/Y0urDumble/status/2114428470168334365"]
first_seen: "2026-10-25"
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "投稿が『Stripe agent toolkit』と呼ぶ @stripe/agent-toolkit は、READMEで『今後の更新・セキュリティ修正なし』と明記され、ホスト型MCP（https://mcp.stripe.com）への移行が推奨されている。新規導入では非推奨パッケージを選ばないこと。ベンチマークはStripe自身が3回の最良値を採る社内評価で、独立再現ではない。投稿の請求書・決済リンクの即時発行、$3,000–6,000、48 leads / 12 pitches / 1 signed は動作確認していない。当方でプラグイン導入・MCP接続・決済試験はしていない。"
fetched_at: "2026-11-09T21:34:56Z"
type: "repo"
---

# stripe/ai — Stripe公式のAIプラグイン・スキルとMCP、連携ベンチマーク

## 出来ること

- Stripe公式のAI向けリポジトリ。エージェントプラグイン/スキル（skills/ に stripe-pay、stripe-best-practices、stripe-docs、stripe-projects、stripe-apps、stripe-directory、metronome、upgrade-stripe など10種）と、Stripe連携タスクのベンチマーク（benchmarks/）を同梱する。
- ホスト型MCPサーバー https://mcp.stripe.com を案内し、OAuthでMCPクライアントからStripe APIへ接続する。請求・Checkout・サブスクリプション等の操作はMCP側のツールが担う。
- 重要: READMEは @stripe/agent-toolkit / stripe-agent-toolkit / @stripe/mcp / @stripe/ai-sdk / @stripe/token-meter を『今後の更新・セキュリティ修正なし』と明記し、ホスト型MCPへの移行を促している。投稿の『Stripe agent toolkit』はこの非推奨パッケージを指す可能性が高く、新規導入ではMCPを使う。

## 目的・背景

- Stripe上でAIプロダクトを作る際の、実装ガイド（skills）・接続（MCP）・評価（benchmarks）を1か所にまとめる公式リポジトリ。
- benchmarksはgooseベースのエージェントハーネスでStripe統合タスクを実行し、backend / full-stack / gymの3カテゴリで採点する。タスクにはCheckout、サブスクリプション、SDKアップグレード、請求書などが含まれる。
- 2026-11-09時点でstars 2,052、forks 386、最終push 2026-11-09、直近30日56コミット。TypeScript、MIT、アーカイブなし。最新リリースは未取得（releases/latestは404）。

## 依存関係

- プラグイン導入はClaude Code / Codex / Cursor / Grok Buildの各CLI。手動導入はNode.jsの npx skills。
- ホスト型MCPはOAuth認証。ベンチマーク実行は自分のStripeアカウント（testmode/sandbox）のSecret key/Public keyと、各evalの依存・Dockerが必要。
- Stripe APIの利用自体はStripeの契約・手数料・利用規約に従う。

## 実行条件

- リポジトリのコードはMIT。Stripeアカウント、APIキー、MCPクライアント、Node.js環境が必要。
- ベンチマークのスコアはStripe自身が3回の最良値を採用した社内評価で、独立再現ではない。数値は配布元の報告として扱う。
- 投稿の請求書・決済リンクの即時発行や$3,000–6,000の案件単価は動作確認していない。

## 最短手順

- Claude Codeならプロジェクトで `claude plugin install stripe@claude-plugins-official` を実行する。
- 他クライアントはCodex `codex plugin add stripe@openai-curated`、Cursor `/add-plugin stripe`、Grok `grok plugin install stripe --trust`、または `npx skills add https://docs.stripe.com` を使う。
- StripeアカウントでMCPクライアントを https://mcp.stripe.com にOAuth接続し、テストモードで請求・Checkoutを試す。
- ベンチマークを再現する場合は benchmarks/ の各eval READMEに従い、testmodeのキーとDockerを用意する。

## 変更履歴

- 2026-11-09: 初回登録
