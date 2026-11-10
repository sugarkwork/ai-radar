---
repo: thesysdev/openui
name: OpenUI
genre: agent-framework
url: https://github.com/thesysdev/openui
license: MIT
stars: 15026
language: TypeScript
created: 2024-12-02
updated: "2026-11-09"
added: 2026-11-05
first_seen: 2026-10-21
source_post: https://x.com/opensourcelab9/status/2112793520318914852
sources:
  - https://www.openui.com
flags: []
risk_notes: ""
forks: 998
open_issues: 203
size_kb: 431034
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:35:16Z"
last_release: "@openuidev/server@0.4.1"
last_release_at: "2026-11-09"
---

# OpenUI

## 出来ること

- モデルに返させる UI を **OpenUI Lang** という専用の記法で書かせる。JSON ではなくストリーミング前提の言語で、README では「同等の JSON より最大67%トークンが少ない」としている。
- 自分が登録した部品（カード、グラフ、フォームなど）だけを使わせる指示文を、部品定義から自動生成する（`createLibrary` / `lib.prompt()`）。登録外の部品は出てこないので、画面が崩れにくい。
- React / Vue / Svelte / Angular のランタイムが同梱され、トークンが届くたびに少しずつ描画する。ボタン押下などの結果はエージェント側に返せる。
- 既製の部品集（チャート・フォーム・テーブル・レイアウト）とチャット UI が React 向けに用意されている。
- LangChain / LangGraph 連携、A2UI プロトコル対応のパッケージもある。

## 目的・背景

「LLM の出力をテキストとしてしか扱わない」状態をやめ、**モデルが組み立てた UI をそのまま流して描く**ための標準を作るプロジェクト。部品を登録して指示文を生成する側（サーバー／エッジ）と、描画する側（フロント）を分けているので、手元で動かすモデルでもホスト型のモデルでも同じ構成が使える。

## 依存関係

- Node.js と npm。用途別にパッケージが分かれている:
  - `@openuidev/react-lang` + `@openuidev/react-ui`（React の描画と部品）
  - `@openuidev/lang-core`（フレームワーク非依存の指示文生成）
  - `@openuidev/vue-lang` / `@openuidev/svelte-lang` / `@openuidev/angular-lang`
  - `@openuidev/langchain`（LangChain / LangGraph 連携）
- 部品の型は Zod スキーマで定義する。

## 実行条件

- MIT。ただしリポジトリは 428MB と大きい（サンプルとアセット込み）。
- README に「公式の暗号通貨・トークンは存在しない。同名の資産は無関係」という注意書きがある。
- 生成される UI の品質は、登録する部品の設計にそのまま依存する。部品を登録しないと汎用の HTML を返すだけになる。

## 最短手順

```bash
npm install @openuidev/react-lang @openuidev/react-ui
# フレームワーク非依存で指示文だけ作る場合
npm install @openuidev/lang-core
```

## 変更履歴

- 2026-11-05: 初回登録（★14,787 / MIT / TypeScript / 最終push 2026-11-05）
