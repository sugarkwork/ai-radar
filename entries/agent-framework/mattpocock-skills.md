---
repo: mattpocock/skills
name: Skills for Real Engineers
genre: agent-framework
url: https://github.com/mattpocock/skills
license: MIT
stars: 313998
language: Shell
created: 2026-02-03
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/mattpocockuk/status/2117947025354539286
sources:
  - https://aihero.dev/skills
  - https://skills.sh/mattpocock/skills
flags: []
risk_notes: ""
forks: 26327
open_issues: 214
commits_30d: 49
commits_90d: 100
commit_cadence: daily
size_kb: 2267
archived: false
fetched_at: "2026-11-05T10:18:14Z"
last_release: v1.3.2
last_release_at: 2026-10-29
---

# Skills for Real Engineers（mattpocock/skills）

## 出来ること

- コーディングエージェント向けのスキル集。**小さく合成可能**であることを優先し、プロセス全体を所有するフレームワーク（GSD / BMAD / Spec-Kit など）とは対極に置いている。モデル非依存。
- 収録は4分類（2026-11 時点）:
  - **engineering（20）** — `grill-with-docs` / `tdd` / `diagnosing-bugs` / `code-review` / `pr` / `to-spec` / `to-tickets` / `triage` / `implement` / `implement-spec` / `domain-modeling` / `codebase-design` / `improve-codebase-architecture` / `prototype` / `research` / `retro` / `wayfinder` / `wizard` / `ask-matt` / `setup-matt-pocock-skills`
  - **productivity（7）** — `grill-me` / `grilling` / `handoff` / `teach` / `to-questionnaire` / `wait-what` / `writing-for-agents`
  - **misc（4）** — `git-guardrails-claude-code` / `migrate-to-shoehorn` / `scaffold-exercises` / `setup-pre-commit`
  - **in-progress（8）** — `chief-of-staff` / `claude-handoff` / `loop-me` / `setup-ts-deep-modules` / `software-factory` / `writing-beats` / `writing-fragments` / `writing-shape`（実験枠）
- 中心にあるのは**着手前の詰め**。`/grill-me`（非コード向け）と `/grill-with-docs`（コード向け）で、エージェントに質問させて要件のズレを潰す。`/grill-with-docs` は共有語彙（glossary）と ADR の整備まで含む。
- フィードバックループ系は `/tdd`（red-green-refactor）と `/diagnosing-bugs`（段階ごとにゲートするデバッグループ）。
- 設計系は `/codebase-design`、`/domain-modeling`、`/improve-codebase-architecture`。エージェントがソフトウェアのエントロピーを加速させる前提で、毎日の設計投資を組み込む。

## 目的・背景

Matt Pocock（TypeScript 教育者）が自分の `.agents` ディレクトリから公開したもの。README では「vibe coding ではなく real engineering」と位置づけ、失敗モードを4つ（意図のズレ／過剰な冗長性／コードが動かない／泥団子化）に分け、それぞれに対応するスキルを説明している。投稿時点で **★313,998**（取得時）と、スキル集としては最大規模。

## 依存関係

- スキルを読めるエージェント。README に導線があるのは Claude Code、Codex、GitHub Copilot（CLI / VS Code）、Gemini CLI、その他（Cursor / OpenCode / Devin / Windsurf / Amp / Pi）。
- 実行時の外部依存はエージェント側に準じる。`setup-pre-commit` など一部は pre-commit を前提にする。

## 実行条件

- 導入は**エージェントごとに1つだけ**選ぶ（プラグインと `skills.sh` の手動コピーを両方入れると全スキルが二重になる）。
- リポジトリ単位で `/setup-matt-pocock-skills` を1回実行する。Issue トラッカー（GitHub / GitLab / ローカルファイル / その他）、トリアージ用ラベル、ドキュメントの保存先を聞かれる。
- `skills/in-progress/` は実験枠、`skills/deprecated/` は廃止済み。使う前にどちらに入っているか確認する。
- MIT。★31万・fork 2.6万と極端に大きいため、issue（213件）とリリース差分の追跡は必要。

## 最短手順

```bash
# Claude Code（自動更新）
claude plugin install mattpocock-skills@claude-plugins-official

# Codex
codex plugin marketplace add mattpocock/skills
codex plugin add mattpocock-skills@mattpocock

# その他のエージェント（cursor / opencode / devin / windsurf / amp / pi）
npx skills@latest add mattpocock/skills -a <agent>

# 導入後、リポジトリごとに1回
/setup-matt-pocock-skills
```

## 変更履歴

- 2026-11-05: 初回登録（★313,998 / pushed 2026-11-04 / MIT）
