---
name: "@shadcn/lint"
genre: "coding-agent"
url: "https://github.com/shadcn-ui/lint"
repo: "shadcn-ui/lint"
license: "MIT"
stars: 3366
language: "TypeScript"
created: "2026-09-02"
updated: "2026-11-02"
forks: 76
open_issues: 12
commits_30d: 36
commit_cadence: "daily"
commits_90d: 96
size_kb: 1064
archived: false
flags: ["unverified"]
risk_notes: "README記載の評価結果とコスト削減率は作者による報告で、独立した実測としては確認していない。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/awe0_io/status/2119116454360658418"]
fetched_at: "2026-11-17T00:12:57.025052+00:00"
---

# @shadcn/lint

## 出来ること

- Tailwind v4のデザインシステム向けに、コンポーネントごとのスタイル規則やテーマ値の利用を設定できるリンター。違反を診断し、コンポーネント、variant、themeに基づく修正案をエラーに含められる。ESLintとOxlintに対応し、React、Svelte、Vueで利用可能とREADMEに記載。出典: https://github.com/shadcn-ui/lint/blob/main/README.md

## 目的・背景

- READMEでは、通常の型エラーは許可されないスタイルを示せても、デザインシステム内で何を使うべきかまでは伝えにくいとしている。@shadcn/lintは規則と修正案を診断に含め、エージェントがUIコードを書く際の手掛かりにすることを目的としている。評価結果やコスト削減率はREADMEに記載された作者の報告。出典: https://github.com/shadcn-ui/lint/blob/main/README.md

## 依存関係

- READMEのReact向けESLint例では、@shadcn/lint、eslint、@typescript-eslint/parserを開発依存としてインストールする。既存フレームワークがESLintのparser設定を行う場合は、その設定を維持してplugin、rule、component overrideを追加する。出典: https://github.com/shadcn-ui/lint/blob/main/README.md

## 実行条件

- Node.js 20.19以降と、使用するリンターがサポートするバージョンが必要。Bun 1.3以降も利用可能とREADMEに記載。ESLintを使う場合はESLint 9.30以降が必要。出典: https://github.com/shadcn-ui/lint/blob/main/README.md

## 最短手順

- コーディングエージェントに「Read https://github.com/shadcn-ui/lint/blob/main/SETUP.md and set up @shadcn/lint in this project.」と指示するQuickstartがREADMEに記載されている。導入後、規則を選び、デザインシステムで許可する内容を設定する。出典: https://github.com/shadcn-ui/lint/blob/main/README.md

## 変更履歴

- 2026-11-22: 初回登録
