---
name: "LlamaIndex Framework"
genre: "rag"
url: "https://github.com/run-llama/llama_index"
repo: "run-llama/llama_index"
license: "MIT"
stars: 52924
language: "Python"
created: "2022-11-02"
updated: "2026-11-14"
forks: 8570
open_issues: 1458
commits_30d: 9
commit_cadence: "weekly"
commits_90d: 73
size_kb: 529211
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119131518920433826"]
fetched_at: "2026-11-17T02:23:30.901039+00:00"
---

# LlamaIndex Framework

## 出来ること

- READMEでは、API・PDF・文書・SQLなどのデータコネクタ、データの構造化、検索・クエリを提供し、LLMアプリやRAGアプリを構築できると説明されています。高水準APIと、コネクタ・インデックス・検索器などを調整する低水準APIがあります。出典: https://github.com/run-llama/llama_index

## 目的・背景

- READMEは、独自データでLLMを補強するためのデータフレームワークとして位置付けています。また、現在の重点は文書解析・抽出に移り、OSSフレームワークはRAGやエージェントアプリ向けのツールキットとして提供されていると説明しています。出典: https://github.com/run-llama/llama_index

## 依存関係

- READMEは、llama-index-coreに必要な連携パッケージを追加する構成を案内しています。例としてllama-index-llms-openai、llama-index-llms-ollama、llama-index-embeddings-huggingfaceを示しています。出典: https://github.com/run-llama/llama_index

## 実行条件

- READMEにあるPythonでの導入例は、カスタム構成の場合に `pip install llama-index-core` と各連携パッケージを実行します。OpenAIの例では `OPENAI_API_KEY` とデータディレクトリを設定しています。出典: https://github.com/run-llama/llama_index

## 最短手順

- Pythonで始める場合、READMEはスターター構成として `pip install llama-index`、またはコアと必要な連携だけを使う構成として `pip install llama-index-core` を案内しています。OpenAI連携例では `pip install llama-index-llms-openai` も追加します。出典: https://github.com/run-llama/llama_index

## 変更履歴

- 2026-11-22: 初回登録
