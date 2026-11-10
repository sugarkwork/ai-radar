---
repo: "nuxt/ui"
name: "Nuxt UI"
genre: "other"
url: "https://github.com/nuxt/ui"
author: "nuxt"
license: "MIT"
stars: 7061
language: "TypeScript"
created: "2021-11-15"
updated: "2026-11-09"
forks: 1154
open_issues: 187
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 151393
archived: false
last_release: "v4.12.0"
last_release_at: "2026-10-15"
homepage: "https://ui.nuxt.com"
type: "repo"
flags: []
risk_notes: "「ページの JS が最大27%減」は本家 v4.12.0 リリースノートのベンダー計測で、公式ドキュメントサイトの JS gzip 251.9→183.9 kB（27.0%減）／生の JS 871.6→549.6 kB（36.9%減）という比較表の数字。利用者のアプリで同じ削減率になる保証ではなく、第三者による独立計測もない。Chart は @tanstack/charts（^1、optional peer）を別途インストールしないと使えない。投稿の「Nuxt の言語設定を見て」は正確には @nuxtjs/i18n が入っている場合の挙動で、peerDependencies には含まれない。投稿の「折れ線とドーナツ」は動画で確認できるが、実際のデモは area と bar も含む4種類。"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2113518286113767883"]
fetched_at: "2026-11-09T21:41:20Z"
---

# Nuxt UI — Vue/Nuxt 向け UI ライブラリ、v4.12 で TanStack Charts ベースの Chart を追加

## 出来ること

- Reka UI・Tailwind CSS・Tailwind Variants の上に作られた、型付きでアクセシブルな Vue コンポーネント集。Nuxt ではモジュールとして、素の Vue アプリでは Vite プラグインとして動く（README 冒頭）。
- v4.12.0 で Chart コンポーネントが加わった。line / area / bar / donut の4種類をサーバー側で SVG に描画し、系列色は --ui-chart-* の CSS 変数でテーマとカラーモードに追従する。props で足りないときは definition に TanStack Charts の定義をそのまま渡せる。
- UApp は @nuxtjs/i18n が入っていると現在のロケールに追従し、i18n.locales に列挙したロケールぶんだけをバンドルする。import * as locales で全ロケールを entry chunk に載せる書き方をやめられる。明示的な locale prop は今も優先される。
- オーバーレイ（Header / Sidebar / DashboardSidebar のメニュー、DashboardSearch / ContentSearch のコマンドパレット、Toaster のトースト）が遅延読み込みになり、他ページ専用コンポーネントのコードも読まなくなった。
- テンプレート集が10種あり、Chat（Vercel AI SDK 製で GitHub 認証と履歴永続つきの AI チャット）も含まれる。
- AI から部品仕様を引くための MCP サーバー（https://ui.nuxt.com/mcp）が公開されている。search-components で部品を探し、get-component / get-component-metadata で props・slots・events を取り、get-example で実例コードを取れる。

## 目的・背景

- Nuxt 公式チーム（GitHub の nuxt org）が開発する UI ライブラリ。現行は v4 ブランチで、v3 / v2 は別ブランチに残っている。MIT、2021-11-15 作成、stars 7,060 / forks 1,154、open issues 188（2026-11-09 取得）。
- v4.12.0 は 2026-10-15 公開。リリースノートの Highlights の筆頭が Chart で、CHANGELOG にも「Chart: new component (#7022)」と記録されている。同日 15:04 UTC に作者 @benjamincanac が告知投稿（likes 226 / views 14,328）。
- 日本語の紹介投稿（@opensourcelab9, 2026-10-23）は、その告知と同じ3点（Chart / 自動ロケール / 27%減）を日本語でまとめた二次的な解説。
- 投稿が挙げる「管理画面でグラフだけ別の道具に頼る」という状況への差分は、フォーム・テーブル・ダッシュボード部品と同じパッケージに Chart が入り、色やダークモードの扱いを他の部品と揃えられる点。
- 開発は活発で、直近30日だけで API の取得上限（100件）に達するコミットがある（最古の100件目が 2026-10-15）。最終 push は 2026-11-06。

## 依存関係

- Tailwind CSS v4（peerDependencies で tailwindcss: ^4）。
- Chart を使う場合のみ @tanstack/charts ^1。optional peer（peerDependenciesMeta で optional: true）なので、使わないプロジェクトには入らない。
- @nuxtjs/i18n は peerDependencies に含まれない。インストール済みのときだけ自動ロケールが効く任意統合。
- Editor 系は @tiptap/* ^3、AI チャット部品は ai ^6 || ^7 が、いずれも任意 peer。
- ライセンスは MIT（LICENSE.md・package.json・GitHub API の SPDX がすべて MIT）。npm の @nuxt/ui として無料で、課金・API キー・アカウント登録は不要。

## 実行条件

- Node ^20.19.0 または >=22.12.0（package.json の engines）。
- Nuxt プロジェクト、または Vue 3 + Vite の構成。Tailwind CSS v4 が必須。
- Chart は @tanstack/charts を追加インストールした場合だけ使える。SSR で SVG を返す設計なので、サーバー描画のある構成（Nuxt / Vite SSR）が前提。
- 料金は無料（MIT の OSS）。有料プランや利用上限はない。

## 最短手順

- 1. `pnpm add @nuxt/ui tailwindcss`（npm / yarn / bun でも同じ）
- 2. nuxt.config.ts に `modules: ['@nuxt/ui']` と `css: ['~/assets/css/main.css']` を書き、main.css に `@import "tailwindcss";` と `@import "@nuxt/ui";` を入れる
- 3. Chart を使うなら `pnpm add @tanstack/charts` も実行する（入れないと Chart だけ動かない）
- 4. `<UChart type="line" :data="data" index="month" :categories="categories" />` のように使う。type は line / area / bar / donut、積み上げ棒は `stacked`
- 5. 素の Vue なら vite.config.ts に `@nuxt/ui/vite` のプラグインを、main.ts に `@nuxt/ui/vue-plugin` を `app.use()` する
- 6. AI エージェントから仕様を引くなら MCP を登録する: `claude mcp add --transport http nuxt-ui https://ui.nuxt.com/mcp`（Cursor は .cursor/mcp.json に `{"mcpServers":{"nuxt-ui":{"type":"http","url":"https://ui.nuxt.com/mcp"}}}`）。search-components → get-component → get-example の順で調べる
- 7. リポジトリを触る場合のみ、AGENTS.md と skills/nuxt-ui/SKILL.md が同梱されている（利用者向けの実行ツールではなくコントリビュート用の指示書）

## 変更履歴

- 2026-11-09: 初回登録
