---
repo: "anthropics/claude-plugins-official"
name: "claude-plugins-official"
genre: agent-framework
url: "https://github.com/anthropics/claude-plugins-official"
license: "Apache-2.0"
stars: 45988
language: "Python"
created: "2025-11-20"
updated: 2026-11-03
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 4784
open_issues: 1266
commits_30d: 100
commit_cadence: daily
size_kb: 18548
archived: false
commits_90d: 100
fetched_at: "2026-11-03T23:05:38Z"
---

# claude-plugins-official

## 出来ること

- Anthropic が管理する Claude Code プラグインのマーケットプレイス。`/plugins`（Anthropic 製）と `/external_plugins`（パートナー・コミュニティ製）の2系統で構成される。
- Claude Code から `/plugin install {plugin-name}@claude-plugins-official` で導入、または `/plugin` → Discover で一覧から選ぶ。
- プラグインの標準構成（`.claude-plugin/plugin.json`、任意の `.mcp.json`、`commands/`、`agents/`、`skills/`）と、社内プラグインの参照実装（`plugins/example-plugin`）を同梱。自作プラグインをここに合わせて書ける。
- 外部プラグインは提出フォーム経由で審査を受けて掲載される。

## 目的・背景

Claude Code のプラグイン配布を一箇所に集約する公式ディレクトリ。サードパーティのプラグインを探すときの一次窓口になる。

## 依存関係

- Claude Code 本体（プラグイン機構）。
- プラグインごとに依存は異なる。MCP サーバーを含むものはそのサーバーの要件に従う。

## 実行条件

- **Anthropic はプラグインの中身を検証していない**。README に「導入前に信頼できるか確認すること。Anthropic はプラグインに含まれる MCP サーバーやファイルを制御できず、意図通り動くこと・変わらないことを保証しない」と明記されている。これは外部プラグインに限らず読むべき注意書き。
- 掲載＝安全の保証ではない。認証情報を扱うプラグインは特に、提供元とコードを確認する。
- 作者・ライセンスはプラグイン単位で異なる（ディレクトリ全体が Apache-2.0 でも、各プラグインの権利は別）。

## 最短手順

```
/plugin
# Discover から選ぶ、または
/plugin install {plugin-name}@claude-plugins-official
```

## 変更履歴

- 2026-11-03: 初回登録（★45,987 / pushed 2026-11-03 / Apache-2.0）
