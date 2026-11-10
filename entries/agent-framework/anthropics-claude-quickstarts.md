---
repo: "anthropics/claude-quickstarts"
name: "Claude Quickstarts"
genre: "agent-framework"
url: "https://github.com/anthropics/claude-quickstarts"
license: "MIT"
stars: 20218
language: "Python"
created: "2024-08-29"
updated: "2026-11-06"
forks: 3373
open_issues: 240
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 28
size_kb: 5848
archived: false
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日時、サンプルの動作、回答精度、実利用時の費用は未確認。MITはリポジトリ単位のAPI計測値。各サンプルの条件は個別に確認が必要で、自律コーディング例のREADMEには『Internal Anthropic use.』と記載がある。https://github.com/anthropics/claude-quickstarts/blob/main/autonomous-coding/README.md"
pricing_detail: "Claude APIの料金はモデルと入出力トークン量に応じる。Amazon Bedrock側の料金は未確認。https://platform.claude.com/docs/en/about-claude/pricing"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/N01ennn/status/2117681136306393357"]
fetched_at: "2026-11-10T10:18:36Z"
---

# Claude Quickstarts — Anthropic公式のClaude API実装例集

## 出来ること

- カスタマーサポート例では、Claudeによるチャット応答、Amazon Bedrockで取得した知識ベースの情報、参照元の表示を組み合わせる構成を確認できる。機能の記述は提供元READMEに基づく。https://github.com/anthropics/claude-quickstarts/blob/main/customer-support-agent/README.md

## 目的・背景

- Claude APIを使ったアプリを作る際に、用途別の実装例を起点にできる。https://raw.githubusercontent.com/anthropics/claude-quickstarts/main/README.md

## 依存関係

- カスタマーサポート例にはNode.js 20以上、Anthropic TypeScript SDK、Claude APIキーが必要。知識ベース検索にはAmazon Bedrockの設定が必要。https://github.com/anthropics/claude-quickstarts/blob/main/customer-support-agent/README.md

## 実行条件

- カスタマーサポート例はローカル開発サーバーを起動し、ブラウザーでlocalhostのポート3000を開く構成。READMEで手順を確認した。https://github.com/anthropics/claude-quickstarts/blob/main/customer-support-agent/README.md

## 最短手順

- リポジトリのcustomer-support-agentディレクトリで `npm install` を行い、READMEに従って `.env.local` にClaude APIとBedrockの設定を入れる。
- `npm run dev` で起動し、`http://localhost:3000` のチャットで知識ベースに含まれる内容を質問する。アプリがAnthropic TypeScript SDK経由でClaude APIを呼び出す。https://github.com/anthropics/claude-quickstarts/blob/main/customer-support-agent/README.md

## 変更履歴

- 2026-11-10: 初回登録
