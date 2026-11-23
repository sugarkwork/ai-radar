---
name: "QMD (Query Markup Documents)"
genre: "rag"
url: "https://github.com/tobi/qmd"
repo: "tobi/qmd"
license: "MIT"
stars: 31265
language: "TypeScript"
created: "2025-12-08"
updated: "2026-11-18"
forks: 1973
open_issues: 267
commits_30d: 25
commit_cadence: "daily"
commits_90d: 100
size_kb: 9502
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:10:04.593064+00:00"
---

# QMD (Query Markup Documents)

## 出来ること

- READMEによると、Markdownのメモ、会議の議事録、ドキュメント、ナレッジベースを索引化し、BM25全文検索、ベクトル意味検索、LLMによる再ランキングを組み合わせて検索できます。CLIのほか、MCPサーバーとして`query`、`get`、`multi_get`、`status`、`metadata`を提供します。

## 目的・背景

- 手元の文書をキーワードまたは自然言語で検索し、エージェントのワークフローでも利用できる検索エンジンとして紹介されています。READMEは検索処理をローカルで実行すると説明しています。

## 依存関係

- READMEには、LLM処理が`node-llama-cpp`とGGUFモデルを使うとあります。インストール方法としてNodeまたはBunが記載されています。個別のモデル取得条件や必要なハードウェアは、提示されたREADME抜粋からは確認できません。

## 実行条件

- README記載の導入方法は`npm install -g @tobilu/qmd`または`bun install -g @tobilu/qmd`です。コレクションを追加し、`qmd embed`で埋め込みを生成してから、`qmd search`、`qmd vsearch`、`qmd query`などで検索します。MCP HTTPサーバーは既定でlocalhostにバインドし、別ホストから到達可能にする場合は認証を利用者側で前置きするようREADMEが説明しています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- `npm install -g @tobilu/qmd`で導入し、`qmd collection add ~/notes --name notes`でコレクションを追加、`qmd embed`で埋め込みを生成します。その後、例として`qmd query "quarterly planning process"`でハイブリッド検索できます。

## 変更履歴

- 2026-11-23: 初回登録
