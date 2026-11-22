---
name: "Chonkie"
genre: "rag"
url: "https://github.com/feyninc/chonkie"
repo: "feyninc/chonkie"
license: "MIT"
stars: 4836
language: "Python"
created: "2025-03-29"
updated: "2026-11-17"
forks: 373
open_issues: 23
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 12
size_kb: 26863
archived: false
flags: []
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
risk_notes: ""
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:14:21.014185+00:00"
---

# Chonkie

## 出来ること

- RAG向けにテキストをトークン数、文、再帰的な規則、意味的類似性、コード構造などに基づいて分割できます。Pipelineで分割や重なり付与、埋め込み処理を連結でき、READMEには再利用可能なパイプラインを扱うAPIサーバーも記載されています。これらはREADMEの説明であり、性能値や効果は独立に検証していません。

## 目的・背景

- READMEは、独自のチャンク処理実装や大規模ライブラリのオーバーヘッドを避けたい用途に向けた、軽量なRAG用データ取り込みライブラリと説明しています。

## 依存関係

- 基本利用は `pip install chonkie` または `uv pip install chonkie`。全機能を含む追加依存は `chonkie[all]` として案内され、READMEは本番環境では推奨しないとしています。APIサーバー例では `chonkie[api,semantic,code,catsu]` を使います。

## 実行条件

- Pythonライブラリとしてインストールして利用します。READMEは対応PythonバージョンやOS要件をこの抜粋では示していません。

## 最短手順

- `pip install chonkie` の後、`from chonkie import RecursiveChunker`、`chunker = RecursiveChunker()`、`chunks = chunker("分割するテキスト")` の順で実行し、各チャンクの `text` や `token_count` を参照します。

## 変更履歴

- 2026-11-22: 初回登録
