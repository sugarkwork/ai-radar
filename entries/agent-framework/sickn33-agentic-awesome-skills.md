---
repo: sickn33/agentic-awesome-skills
name: agentic-awesome-skills（AAS）
genre: agent-framework
url: https://github.com/sickn33/agentic-awesome-skills
license: MIT
language: Python
created: 2026-01-14
updated: "2026-11-09"
added: 2026-11-04
first_seen: 2026-11-04
sources:
  - https://x.com/csaba_kissi/status/2117522406730572218
flags: []
risk_notes: ""
stars: 49414
forks: 7167
open_issues: 0
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 451349
archived: false
fetched_at: "2026-11-09T21:34:53Z"
last_release: "v20.7.0"
last_release_at: "2026-11-09"
---

# agentic-awesome-skills（AAS）

## 出来ること

- **2,926本以上のエージェントスキル**をまとめたカタログ。Claude Code / Codex / Cursor / Gemini CLI で使えるものを、Anthropic・Vercel 公式のスキルも含めて収録する。
- 「AAS Core」として、ローカルのカタログ探索、エージェント自身によるスキル選択、実行前のプラン表示を提供する。
- CLI・MCP・プラグインの3形態で配布。必要なスキルだけを入れられる。
- v20.6.0 で映画制作（MiniCut Film Studio）・広告ライブラリ調査（LurkAPI）・macOS の Time Machine 復旧などのスキルが加わった。

## 目的・背景

2026-01 公開、★49,107 / fork 7,130、v20.5.0。スキルが乱立して「どれが動くのか分からない」状態になったため、実行検証済みのものを集約する索引として成長した。件数だけを追うリストではなく、エージェントに選ばせる仕組みを持つ点が特徴。

## 依存関係

- Python（CLI）
- 各エージェント（Claude Code / Codex / Cursor / Gemini CLI）
- MCP クライアント（MCP 形態を使う場合）

## 実行条件

- リポジトリは約440MB（全スキル同梱）。
- 一括導入するとコンテキストを圧迫するため、Core の選択機能か個別導入を使う。
- 2,923本すべてが同じ品質ではない。実行検証の有無は個別に確認する。

## 最短手順

```bash
git clone https://github.com/sickn33/agentic-awesome-skills
# README の CLI / MCP / プラグイン手順から好みの形態で導入
```

## 変更履歴

- 2026-11-04: 初回登録（★49,107 / v20.4.0 / MIT / 30日100+コミット）、収録スキル数を2,923本に更新（v20.5.0）
- 2026-11-06: 収録 2,926 本に更新、映画制作・広告調査・Time Machine 復旧のスキルを追加（v20.6.0 / 828257c）
