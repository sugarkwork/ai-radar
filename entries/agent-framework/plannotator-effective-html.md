---
repo: plannotator/effective-html
name: Effective HTML
genre: agent-framework
url: https://github.com/plannotator/effective-html
author: Plannotator（backnotprop）
license: MIT
stars: 3858
language: HTML
created: 2026-06-09
updated: 2026-10-31
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/awe0_io/status/2117992033130537470
sources:
  - https://www.effectivehtml.com/
forks: 265
open_issues: 6
commits_30d: 5
commits_90d: 8
commit_cadence: weekly
size_kb: 20188
archived: false
fetched_at: "2026-11-05T03:29:06Z"
---

# Effective HTML

## 出来ること

- **エージェントに「使えるHTML成果物」を作らせるスキル集**。ワイヤーフレーム、モックアップ、動くプロトタイプ、図、レポート、プレゼン、ランディングページまで、自己完結した HTML として出力する。
- 8つのスキルを同梱:
  - `html` — 幅広いHTML要求の入口。混在成果物・レポート・解説・プレゼン・LP・ツールを作り、専門スキルへ振り分ける
  - `big-pics-little-words` — 大きな図と最小限の文字で説明する（`bro` から移植）
  - `one-pager` — チームに早く共有する1枚もの（`bro` から移植）
  - `design-artifact` — ハウススタイルを押し付けず、題材ごとに方向性を決める
  - `html-wireframe` — 低忠実度のレイアウト案。内容・階層・導線・レスポンシブ構造を検証する
  - `html-prototype` — 現実的な状態・インタラクション・キーボード操作・レスポンシブを持つ動くプロトタイプ
  - `html-plan` — 計画・ロードマップ・ロールアウト・実装順序。元の約束を落とさない
  - `html-diagram` — アーキテクチャ、シーケンス、プロセス、状態、階層、タイムライン、システム図
- 「fat artifacts + fat context」の方針: プロンプトに長文を積む代わりに、成果物・リポジトリ・フォルダを指して文脈を渡す。HTML はほぼ何でも可視化できるため、文章の壁より明確になりやすい。
- インストールせず**リファレンスとして読むだけ**でも使える。`npx skills add`、Claude Code / Codex のプラグイン、個別スキル指定に対応。

## 目的・背景

コーディングエージェントの出力が「長いテキスト」に寄りがちなところを、**見て判断できる HTML 成果物**に寄せるためのスキル集。Plannotator（ローカルHTMLの閲覧・注釈ツール）と同じ作者で、成果物をそのまま開いて注釈できる導線がある。2026-06-09 作成、10-31 時点で 3,858 star。

## 依存関係

- Agent Skills 対応ホスト（Claude Code / Codex など）。`npx skills add plannotator/effective-html` で導入
- Claude Code: `/plugin marketplace add plannotator/effective-html` → `/plugin install plannotator-effective-html@effective-html`
- Codex: `codex plugin marketplace add plannotator/effective-html` → `codex plugin add ...`
- 生成物は自己完結 HTML。閲覧・注釈に Plannotator を使う場合は別途導入
- リポジトリ自体は HTML 中心で、ビルド用の独自ランタイムは無い

## 実行条件

- スキルの品質はホストのモデルに依存する。図やプロトタイプの精度を上げるには、対象リポジトリや資料を「fat context」として渡す前提
- `html-diagram` はアーキテクチャ図を HTML として作るもので、コードベースを自動解析して図にする専用ツールではない（解析はエージェント側の作業）
- 生成物のブラウザ互換性・アクセシビリティはスキルが担保するわけではない。実運用前に確認
- 移植元（`bro`）のスキルは MIT で、このリポジトリ内に取り込まれている

## 最短手順

```bash
# コレクションごと
npx skills add plannotator/effective-html

# 個別に（例: 図だけ）
npx skills add plannotator/effective-html --skill html-diagram

# Claude Code のプラグインとして
# /plugin marketplace add plannotator/effective-html
# /plugin install plannotator-effective-html@effective-html
```

## 変更履歴

- 2026-11-04: 初回登録（8スキル構成時点）
