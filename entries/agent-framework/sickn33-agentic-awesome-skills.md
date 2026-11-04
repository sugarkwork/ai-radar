---
repo: sickn33/agentic-awesome-skills
name: agentic-awesome-skills（AAS）
genre: agent-framework
url: https://github.com/sickn33/agentic-awesome-skills
license: MIT
language: Python
created: 2026-01-14
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/csaba_kissi/status/2117522406730572218
flags: []
risk_notes: ""
stars: 49107
forks: 7130
open_issues: 7
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 440042
archived: false
fetched_at: "2026-11-04T01:24:02Z"
last_release: v20.4.0
last_release_at: 2026-11-02
---

# agentic-awesome-skills（AAS）

## 出来ること

- **2,884本以上のエージェントスキル**をまとめたカタログ。Claude Code / Codex / Cursor / Gemini CLI で使えるものを、Anthropic・Vercel 公式のスキルも含めて収録する。
- 「AAS Core」として、ローカルのカタログ探索、エージェント自身によるスキル選択、実行前のプラン表示を提供する。
- CLI・MCP・プラグインの3形態で配布。必要なスキルだけを入れられる。

## 目的・背景

2026-01 公開、★49,107 / fork 7,130、v20.4.0。スキルが乱立して「どれが動くのか分からない」状態になったため、実行検証済みのものを集約する索引として成長した。件数だけを追うリストではなく、エージェントに選ばせる仕組みを持つ点が特徴。

## 依存関係

- Python（CLI）
- 各エージェント（Claude Code / Codex / Cursor / Gemini CLI）
- MCP クライアント（MCP 形態を使う場合）

## 実行条件

- リポジトリは約440MB（全スキル同梱）。
- 一括導入するとコンテキストを圧迫するため、Core の選択機能か個別導入を使う。
- 2,884本すべてが同じ品質ではない。実行検証の有無は個別に確認する。

## 最短手順

```bash
git clone https://github.com/sickn33/agentic-awesome-skills
# README の CLI / MCP / プラグイン手順から好みの形態で導入
```

## 変更履歴

- 2026-11-04: 初回登録（★49,107 / v20.4.0 / MIT / 30日100+コミット）
