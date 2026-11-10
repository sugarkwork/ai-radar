---
repo: "wshobson/agents"
name: "wshobson/agents"
genre: "coding-agent"
url: "https://github.com/wshobson/agents"
license: "MIT"
stars: 42378
forks: 4476
open_issues: 11
size_kb: 5072
language: "Python"
created: "2025-07-24"
updated: "2026-11-09"
archived: false
commits_30d: 34
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "最新リリース、導入後の動作、ホスト間の機能差、トークン削減量や生成品質への効果は未確認。MITはリポジトリのライセンスで、外部配布項目やホストの利用条件・料金は未確認。90日コミット数は100件以上を示す。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/N01ennn/status/2117681136306393357"]
fetched_at: "2026-11-10T10:18:28+00:00"
---

# wshobson/agents — AIコーディングツール向けスキルとサブエージェント集

## 出来ること

- Python開発などの用途別プラグインを導入し、テスト設計のスキルや専門エージェントを作業に使える。 [プラグイン一覧](https://github.com/wshobson/agents/blob/main/docs/plugins.md)

## 目的・背景

- Claude Code形式の共通ソースを管理し、アダプターで複数のコーディングツール向けに配布する。必要なプラグインだけを導入する設計で、コンテキスト消費の削減量は今回の確認範囲外。 [README](https://raw.githubusercontent.com/wshobson/agents/main/README.md) [設計資料](https://github.com/wshobson/agents/blob/main/docs/architecture.md)

## 依存関係

- 以下の手順にはClaude Codeが必要。Codex CLIなどではホスト別の導入手順を使う。 [ホスト別セットアップ](https://github.com/wshobson/agents/blob/main/docs/harnesses.md)

## 実行条件

- マーケットプレイスを追加するとカタログが登録され、個別プラグインを導入するとそのスキルやエージェントが利用可能になる。Claude Codeは導入済みスキルをタスクに応じて読み込むと公式ガイドに記載されている。 [利用ガイド](https://github.com/wshobson/agents/blob/main/docs/usage.md)

## 最短手順

- Claude Codeで `/plugin marketplace add wshobson/agents` を実行し、続けて `/plugin install python-development` でPython開発プラグインを導入する。 [導入手順](https://github.com/wshobson/agents/blob/main/docs/plugins.md)
- Claude Codeに『python-testing-patterns スキルの方針で、この関数のpytestテストケースを提案して』と依頼する。公式ガイドでは、Claudeがタスクに応じて導入済みスキルを選ぶ。 [利用ガイド](https://github.com/wshobson/agents/blob/main/docs/usage.md)

## 変更履歴

- 2026-11-10: 初回登録
