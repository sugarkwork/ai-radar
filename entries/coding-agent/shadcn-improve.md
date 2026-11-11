---
name: "improve"
genre: "coding-agent"
url: "https://github.com/shadcn/improve"
repo: "shadcn/improve"
license: "MIT"
stars: 10241
language: "unknown"
created: "2026-06-10"
updated: "2026-09-12"
forks: 425
open_issues: 17
commits_30d: 0
commit_cadence: "stale"
commits_90d: 1
size_kb: 17
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/TiagerBao/status/2120123324273745941"]
fetched_at: "2026-11-10T23:16:52.547704+00:00"
---

# improve

## 出来ること

- READMEでは、コードベースを監査して優先順位付きの指摘と実装計画を作成するAgent Skillとして説明されている。監査カテゴリには正確性、セキュリティ、性能、テスト網羅性、技術的負債、依存関係・移行、開発者体験、ドキュメント、方向性が含まれる。計画のレビュー、安価な実行エージェントへの委任、計画バックログの整理にも対応する。

## 目的・背景

- READMEの説明では、能力の高いモデルにコードベースの理解、判断、仕様化を担わせ、実装はより安価なモデルに渡す。成果物となる計画は自己完結したMarkdown仕様で、他のエージェントや人が利用できる。

## 依存関係

- READMEには、Agent Skills形式をサポートするエージェントで利用可能とある。インストール例は `npx skills add shadcn/improve`。その他の依存関係はREADMEに記載されていない。

## 実行条件

- README記載の利用例は、対象リポジトリでエージェントに `/improve` などのコマンドを実行する方法。`/improve execute <plan>` は隔離されたworktreeで実行エージェントを起動し、結果をレビューすると説明されている。実際の動作は独立検証していない。

## 最短手順

- 1. `npx skills add shadcn/improve` でインストールする。2. 対象リポジトリで `/improve quick` または `/improve` を実行する。3. 指摘から計画化する項目を選ぶ。4. 生成された `plans/` 内の計画を確認し、任意のエージェントに実装を依頼する。これらはREADME記載の手順であり、実行確認はしていない。

## 変更履歴

- 2026-11-11: 初回登録
