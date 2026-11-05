---
repo: antfu/skills-pack
name: "@antfu/skills（npm で配るスキル詰め合わせ）"
genre: agent-framework
url: https://github.com/antfu/skills-pack
license: MIT
stars: 334
language: TypeScript
created: 2026-09-25
updated: 2026-10-30
added: 2026-11-05
first_seen: 2026-10-22
source_post: https://x.com/opensourcelab9/status/2113155901104542124
sources: []
flags: []
risk_notes: ""
forks: 4
open_issues: 0
size_kb: 124
archived: false
---

# @antfu/skills（npm で配るスキル詰め合わせ）

## 出来ること

- 複数の配布元のエージェントスキルを1つの npm パッケージにまとめ、`pnpm i` のたびに同期する。導入は依存に `@antfu/skills` と `skills` を足し、`prepare` に `skills experimental_sync -y` を置くだけ。
- スキルは `.agents/skills/<name>` に入り、マシン上で検出されたエージェント（Claude Code / Cursor / Codex / OpenCode など）のスキルディレクトリへリンクされる。`-a claude-code cursor` で対象を明示できる。
- `skills-lock.json` に「どのスキルがどこから来たか」が残る。**これをコミットする**のが前提で、チーム全員が同じ版になる。
- 依存から外すと、次の同期でスキルも消える（消し忘れが出ない）。
- 収録は workflow 系（`grill-me` / `handoff` / `to-questionnaire` / `writing-for-agents` / `code-review` / `tdd` / `research` / `improve` / `dry-refactoring`）、antfu 自身の規約系（`antfu` / `antfu-create-pr` / `antfu-issue-triage` / `antfu-simplify` / `antfu-query`）、文章系（`simple-english`）など。

## 目的・背景

スキルを「フォルダをコピーして配る」運用から、**依存関係として管理する**運用に変える試み。版ずれと「誰の手元に何が入っているか分からない」問題を、lock ファイルと npm の解決に寄せる。中身は自作ではなく、mattpocock/skills・shadcn/improve・jscpd・antfu/skills などの既存配布を束ねている。

## 依存関係

- Node.js と pnpm（npm でも可）。
- `skills` CLI（`^1.7.4` 以降）。`skills-npm` から移行した経緯があり、旧来の利用者は `npx skills-npm migrate` で切り替える。
- 同期先のエージェントが入っていること。

## 実行条件

- MIT。リポジトリ自体は 124KB で、中身はスキル定義のみ。
- 上流は各リポジトリの既定ブランチを追うため、**lock を固定しないと upstream の変更がそのまま入る**。README も `pnpx skills update` で明示更新する手順を用意している。
- スキルはエージェントが実行する手順そのものなので、外部由来のものを無確認で同期しない運用ルールを別途決めておくのが無難。

## 最短手順

```json
{
  "scripts": { "prepare": "skills experimental_sync -y" },
  "devDependencies": { "skills": "^1.7.4", "@antfu/skills": "^1.0.0" }
}
```

```bash
pnpm i          # 初回同期（以降の install でも同期される）
pnpx skills update   # 上流の最新を取り込む
```

## 変更履歴

- 2026-11-05: 初回登録（★334 / MIT / TypeScript / 最終push 2026-10-30）
