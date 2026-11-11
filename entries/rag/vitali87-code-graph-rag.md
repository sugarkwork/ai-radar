---
name: "Code-Graph-RAG"
genre: "rag"
url: "https://github.com/vitali87/code-graph-rag"
repo: "vitali87/code-graph-rag"
license: "MIT"
stars: 5347
language: "Python"
created: "2025-06-16"
updated: "2026-11-11"
forks: 711
open_issues: 463
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 603274
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/JeremyCMorgan/status/2118569326563258441"]
fetched_at: "2026-11-11T04:12:02.437129+00:00"
---

# Code-Graph-RAG

## 出来ること

- Tree-sitterを基盤に複数言語のコードから関数、クラス、メソッド、モジュールとその関係を抽出し、埋め込みグラフデータベースに保存する。自然言語でコードについて質問し、構造に基づく回答を得るほか、コード取得、差分プレビュー付き編集、最適化、デッドコード検出、ASTパターンによる検索・書き換えに利用できる。実行時トレースをグラフに重ねる機能もREADMEに記載されている。

## 目的・背景

- 混在言語のモノレポを単一のグラフスキーマで扱い、コードの構造と関係をもとに検索や編集を支援する。READMEによると、Tree-sitterが解析の基盤で、利用可能なツールチェーンがある場合はコンパイラーフロントエンドを追加し、動的トレースは実行されたコードの呼び出しを反映する。トレースは実行されたコードのみを観測し、コンパイラーフロントエンドはツールチェーンでビルド可能な範囲に限られる。

## 依存関係

- READMEに記載された基本要件はPython 3.12以上とripgrep。インストール例では、Tree-sitter文法、追加言語向けast-grep、ベクトル検索向けsemanticの各extrasを指定している。グラフは既定で埋め込みSQLiteに保存され、MemgraphとNeo4jは任意のバックエンドとして記載されている。

## 実行条件

- README記載の導入方法はuv toolまたはpipx。基本的な導入例は `uv tool install "code-graph-rag[treesitter-full,ast-grep,semantic]"`。READMEには `cgr start --update-graph` でリポジトリをグラフ化し、`cgr start` で質問や編集を行う例がある。

## 最短手順

- README記載の手順: 1. `uv tool install "code-graph-rag[treesitter-full,ast-grep,semantic]"` で導入する。2. 対象リポジトリで `cgr start --update-graph` を実行してグラフを作成・更新する。3. `cgr start` で質問や編集を行う。Python 3.12以上とripgrepが必要。

## 変更履歴

- 2026-11-11: 初回登録
