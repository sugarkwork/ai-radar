---
name: "Knowlective"
genre: "other"
url: "https://github.com/knowlective-org/knowlective"
repo: "knowlective-org/knowlective"
license: "AGPL-3.0"
stars: 0
language: "TypeScript"
created: "2026-10-05"
updated: "2026-11-19"
forks: 0
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 4823
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/TomoYatsunami/status/2123308713910182281"]
fetched_at: "2026-11-19T08:10:49.655839+00:00"
---

# Knowlective

## 出来ること

- 文書とナレッジを共有し、BlockNoteベースのブロックエディターとYjs・Hocuspocusによるリアルタイム共同編集ができます。ページをツリー状に整理し、グループ単位の閲覧・編集・管理権限を設定できます。管理者が許可した場合はページをインターネットに公開でき、公開ページはログインなしで閲覧できます。

## 目的・背景

- チームの知識を集約・共有するための、自己ホスト可能なオープンソースの文書・ナレッジ共有ツールとして説明されています。

## 依存関係

- README記載の構成要素は、Next.js、BlockNote（Tiptap/ProseMirrorベース）、Yjs、Hocuspocus、PostgreSQL、Redis、SeaweedFSです。開発用Docker Composeには、意味検索用pgvectorを含むPostgreSQL、Redis、SeaweedFSが含まれます。

## 実行条件

- 初期セットアップにはDocker Compose、pnpm、環境変数ファイルが必要です。READMEの手順では、サーバーキーとストレージキーを生成して.envに設定し、サービス起動、依存関係のインストール、Prismaクライアント生成、DBマイグレーション、デモデータ投入を行います。初回アクセス時にマスターパスワード、サイトの公開URL、既定言語を設定します。READMEはサポート対象の自然言語一覧を示していません。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- リポジトリのREADMEに従い、.env.exampleを.envにコピーします。pnpm gen:server-keyを実行して出力をKNOWLECTIVE_SERVER_KEYに設定し、pnpm gen:storage-keyを2回実行して出力をSeaweedFSのアクセスキー・シークレットキーに設定します。続けてdocker compose up -d、pnpm install、pnpm db:generate、pnpm db:migrate、pnpm db:seedを実行します。初回アクセス時に/setupでマスターパスワード、公開URL、既定言語を設定します。

## 変更履歴

- 2026-11-23: 初回登録
