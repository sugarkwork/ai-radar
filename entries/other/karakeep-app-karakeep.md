---
repo: "karakeep-app/karakeep"
name: "Karakeep"
genre: "other"
url: "https://github.com/karakeep-app/karakeep"
last_release: "v0.34.1"
flags: ["unverified"]
risk_notes: "リリースの公開日時は未確定。タグ付け・要約の精度、検索品質、処理時間、MCP 接続の実動作は未測定。発見投稿の Grok Bot との連携は未確認。"
stars: 30436
forks: 1630
open_issues: 726
size_kb: 146871
language: "TypeScript"
created: "2024-02-06"
updated: "2026-11-10"
archived: false
license: "AGPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:12:44+00:00"
---

# Karakeep — AI でタグ付けできるセルフホスト型ブックマーク管理

## 出来ること

- リンク、メモ、画像、PDF を保存し、リストで整理する。公式 README は全文検索、セマンティック検索、LLM による自動タグ付け・要約を案内している。
- 公式 MCP サーバーを使うと、対応する AI クライアントから保存済みブックマークを検索し、内容を取得できる。

## 目的・背景

- 後で読み返す資料を一か所に保存し、手作業で分類する負担を減らすためのアプリ。自動タグ付けと要約には LLM、セマンティック検索には埋め込みモデルを使う。

## 依存関係

- 標準構成には Docker と Docker Compose が必要。全文検索に Meilisearch、Web ページのクロールに Chrome を使う。AI 機能には OpenAI 互換プロバイダーまたは Ollama を設定する。

## 実行条件

- Ollama を使う場合、Karakeep コンテナから Ollama に接続できるようにする。セマンティック検索を使う場合は埋め込みモデルを設定し、自動インデックス化を有効にする。
- 本体は AGPL-3.0。外部の推論 API を使う場合は、提供元の料金と利用条件を確認する。Ollama によるローカル推論には自前の計算資源が必要。

## 最短手順

- 公式 Docker ガイドの Compose ファイルを用意する。`.env` に `NEXTAUTH_SECRET` と `MEILI_MASTER_KEY` を別々のランダム値で設定し、`NEXTAUTH_URL` を自分のサーバーの URL に合わせる。
- OpenAI を使う場合は `.env` に `OPENAI_API_KEY` を設定する。Ollama を使う場合は公式の AI プロバイダー設定ガイドに従う。`docker compose up -d` で起動し、Web UI でリンクを保存してタグを確認する。
- AI から呼ぶには、Karakeep の設定で API キーを発行し、Claude Desktop などの MCP 対応クライアントに `npx @karakeep/mcp` を登録する。`KARAKEEP_API_ADDR` に自分のインスタンスの URL、`KARAKEEP_API_KEY` に発行したキーを設定し、AI に `search-bookmarks` で保存済みリンクを探すよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
