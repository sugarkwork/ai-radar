---
name: "RAGFlow"
genre: "rag"
url: "https://github.com/infiniflow/ragflow"
repo: "infiniflow/ragflow"
license: "Apache-2.0"
stars: 94266
language: "Go"
created: "2023-12-12"
updated: "2026-11-17"
forks: 11333
open_issues: 1307
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 194244
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119131518920433826"]
fetched_at: "2026-11-17T02:24:05.373003+00:00"
---

# RAGFlow

## 出来ること

- 文書の知識抽出とテンプレートベースのチャンク分割、文書・データセット単位の知識コンパイル、複数段階の検索、根拠参照と引用の提示、複数形式のデータ取り込みを提供するとREADMEに記載されています。出典: https://github.com/infiniflow/ragflow#-key-features

## 目的・背景

- LLM向けのコンテキスト層を構築するオープンソースのRAGエンジンとして紹介されています。READMEは、複雑なデータからAIシステムを構築するためのRAGワークフローとエージェント機能を掲げています。出典: https://github.com/infiniflow/ragflow#-what-is-ragflow

## 依存関係

- DockerデプロイにはDocker 24.0.0以上、Docker Compose v2.26.1以上が必要です。ソースから起動する場合はgo.mod記載のGoバージョンが必要で、フロントエンド開発にはNode.jsとnpmも必要です。出典: https://github.com/infiniflow/ragflow#-local-deployment

## 実行条件

- Dockerの推奨開始構成は4 CPUコア、RAM 16 GB、空きディスク50 GBです。実際の必要量は文書エンジン、データ量、解析タスク、同時実行数により異なり、ローカルモデル等の追加コンポーネントには追加リソースが必要となる場合があります。Elasticsearchを使う場合、Dockerホストのvm.max_map_countを262144以上に設定します。出典: https://github.com/infiniflow/ragflow#-docker-deployment-prerequisites

## 最短手順

- READMEのDockerデプロイ手順を参照してください。READMEに記載された前提条件を満たし、Elasticsearchを利用する場合はホストのvm.max_map_countを確認・設定してからサーバーを起動します。出典: https://github.com/infiniflow/ragflow#-docker-deployment

## 変更履歴

- 2026-11-22: 初回登録
