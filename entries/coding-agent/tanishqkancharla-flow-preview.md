---
name: "Flow Preview"
genre: "coding-agent"
url: "https://github.com/tanishqkancharla/flow-preview"
repo: "tanishqkancharla/flow-preview"
flags: ["unverified"]
risk_notes: "README記載の要件はNode.js 24以降、npm、および生成されたプレビューの依存関係をインストールするためのレジストリアクセス。個別プロジェクトでの適合性や動作結果は未確認。"
stars: 37
forks: 3
open_issues: 0
size_kb: 133
language: "TypeScript"
created: "2026-10-23"
updated: "2026-11-06"
archived: false
license: "Apache-2.0"
commits_30d: 13
commits_90d: 13
commit_cadence: "weekly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/sumika45379/status/2116870373019103693"]
fetched_at: "2026-11-10T14:05:19.744940+00:00"
---

# Flow Preview

## 出来ること

- ユーザージャーニーを、実際のUI状態を示すインタラクティブなキャンバスとしてプレビューする。状態ごとのサムネイル、アニメーション付きナビゲーション、ズーム、アウトライン、ブラウザーに保存されるレビュー印を含む。

## 目的・背景

- READMEによると、Halo PR #606 から抽出されたジェネレーター、キャンバス、Viteヘルパー、ブラウザーテストを、単独配布向けのリポジトリとして提供する。

## 依存関係

- Node.js 24以降、npm、生成されたプレビューの依存関係をインストールするためのレジストリアクセスが必要。キャンバスはReactとMauiを使用する。

## 実行条件

- READMEでは、生成器はNode.js組み込み機能を使い、Haloのチェックアウト、ワークスペース設定、Amp orbを必要としないと説明されている。プレビューはローカルでViteを使って実行できる。

## 最短手順

- Skills CLIで `npx skills add tanishqkancharla/flow-preview` を実行し、使用するコーディングエージェントを選ぶ。対象プロジェクトから `node .agents/skills/flow-preview/scripts/generate.mjs preferences-flow 4180`、続けて `npm --prefix tmp/preferences-flow install --workspaces=false` と `npm --prefix tmp/preferences-flow run dev` を実行する。生成後は `tmp/preferences-flow/scenario.tsx` を編集して状態を定義する。

## 変更履歴

- 2026-11-11: 初回登録
