---
name: "Motion"
genre: "3d-motion"
repo: "motiondivision/motion"
url: "https://github.com/motiondivision/motion"
flags: ["unverified"]
risk_notes: "最新リリースの版と公開日時、ブラウザー上の描画性能、エージェントへのSkill導入とMCP接続の実動作は未確認。コミット件数の100は各期間で100件以上を表す。"
stars: 35043
forks: 1527
open_issues: 5
size_kb: 1668394
language: "TypeScript"
created: "2018-11-16"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:54:18+00:00"
---

# Motion — ReactのUIアニメーションとレイアウト遷移

## 出来ること

- Reactのコンポーネントに `layout` を付けると、リストの並べ替えやアコーディオンの開閉に伴う位置・サイズの変化をアニメーションにできる。 [公式レイアウトガイド](https://motion.dev/docs/react-layout-animations)

## 目的・背景

- 公式ガイドによると、Motionはレイアウトの変化を計測し、CSSの `transform` で位置と大きさの変化を補間する。拡縮中に子要素が歪む場合は子にも `layout` を付け、位置だけを補間したい場合は `layout="position"` を使う。描画性能の独立実測は行っていない。 [公式レイアウトガイド](https://motion.dev/docs/react-layout-animations)

## 依存関係

- React向けは `motion` パッケージとReact 18.2以上を使い、`motion/react` から読み込む。 [公式インストールガイド](https://motion.dev/docs/react-installation)

## 実行条件

- Next.js App Routerで `motion/react` を使う場合は、読み込むファイルを `use client` でクライアントコンポーネントにする。ライブラリ本体とエージェント向けSkillはMIT。公式READMEではドキュメント検索MCPを無料・アカウント不要と案内し、Motion+の追加APIやサンプルを有料枠としている。 [公式インストールガイド](https://motion.dev/docs/react-installation) [公式README](https://raw.githubusercontent.com/motiondivision/motion/main/README.md)

## 最短手順

- 既存のReactプロジェクトで `npm install motion` を実行し、`import { motion } from 'motion/react'` を追加する。並べ替え対象の要素を、安定した `key` を持つ `<motion.div layout>` にして、Reactの状態で順序を切り替える。 [公式インストールガイド](https://motion.dev/docs/react-installation) [公式レイアウトガイド](https://motion.dev/docs/react-layout-animations)
- Claude CodeなどREADME記載の対応エージェントでは、利用者が `npx motion-ai` で `/motion` SkillとMCP設定を導入できる。MCP対応クライアントから公式の `https://mcp.motion.dev` を設定する場合は、エージェントに `layout` の公式ドキュメントと並べ替えのサンプルを検索させ、その結果を参照して実装を依頼する。 [公式README](https://raw.githubusercontent.com/motiondivision/motion/main/README.md)

## 変更履歴

- 2026-11-10: 初回登録
