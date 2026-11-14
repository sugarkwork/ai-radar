---
name: "Rowboat"
genre: "agent-framework"
url: "https://github.com/rowboatlabs/rowboat"
repo: "rowboatlabs/rowboat"
flags: ["unverified"]
risk_notes: "READMEは「Expect breaking changes while we dogfood」としており、wire contractの互換性は今後変更される可能性がある。"
stars: 18231
forks: 1824
open_issues: 240
size_kb: 160283
language: "TypeScript"
created: "2025-01-13"
updated: "2026-11-13"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118704706897736102"]
fetched_at: "2026-11-13T19:10:10.908899+00:00"
---

# Rowboat

## 出来ること

- 人とエージェントが共有スペースやグループチャットで協働する。エージェントはメッセージ、スレッド、ファイル、タスク一覧などを共有できる。HarborはSpacesのサーバーで、MCP経由の接続にも対応する。デスクトップアプリはローカルの作業情報をインデックス化し、メール、ノート、ブラウザー、コード作業、会議メモなどに使うとREADMEは説明している。これらはREADME上の機能説明であり、独立した効果測定ではない。

## 目的・背景

- エージェントをチームの一員として共有スペースに参加させ、人とエージェントの会話や作業を一か所で扱う。既存のエージェントを接続するか、新たに起動できるとREADMEに記載されている。

## 依存関係

- Harborの永続化にはPostgresを使用する。サーバーはNode.jsのパッケージ管理・ビルド手順として`pnpm install`と`pnpm build`を案内している。MCP接続にはOAuth 2.1対応クライアントを利用できる旨の説明がある。その他の依存条件はREADME抜粋からは確認できない。

## 実行条件

- ローカル開発用Harborは`apps/harbor`からビルドし、`packages/server`で開発サーバーを起動する。READMEではメモリ上の単一組織サーバーがポート4272で起動し、開発用トークンを使うと説明している。永続化する場合は`DATABASE_URL`を設定する。デプロイ時は`HARBOR_MODE=deployment`、`APEX_DOMAIN`、信頼するOIDC発行者の`AUTH_ISSUER`などを設定する。READMEは、dev tokensを公開してはならないと明記している。

## 最短手順

- README記載のローカル起動手順：`cd apps/harbor`、`pnpm install && pnpm build`、`cd packages/server`、`pnpm dev`。開発用サーバーはポート4272で起動する。READMEは開発用トークンのサーバーを公開しないよう注意している。

## 変更履歴

- 2026-11-14: 初回登録
