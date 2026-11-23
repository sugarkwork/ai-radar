---
name: "LangMem"
genre: "agent-framework"
url: "https://github.com/langchain-ai/langmem"
repo: "langchain-ai/langmem"
license: "MIT"
stars: 1777
language: "Python"
created: "2025-01-21"
updated: "2026-11-16"
forks: 207
open_issues: 83
commits_30d: 6
commit_cadence: "weekly"
commits_90d: 13
size_kb: 3966
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:10:55.245581+00:00"
---

# LangMem

## 出来ること

- 会話から重要な情報を抽出し、エージェントが会話中に情報を記録・検索するメモリツールや、知識を抽出・統合・更新するバックグラウンドのメモリ管理機能を提供します。LangGraphの長期メモリストアとの統合もあります。

## 目的・背景

- エージェントがやり取りを通じて適応し、長期メモリを維持するためのツール群です。READMEは、応答のパーソナライズやセッション間の一貫した振る舞いを目的として挙げています。

## 依存関係

- READMEの例ではLangGraphの`create_react_agent`と`InMemoryStore`、AnthropicのモデルおよびOpenAIの埋め込みモデルを使っています。APIキーの設定が必要で、別の対応LLMプロバイダーも利用できるとREADMEにあります。

## 実行条件

- READMEは`pip install -U langmem`によるインストールと、LLMプロバイダーのAPIキー設定を示しています。例の`InMemoryStore`はプロセス内メモリに保存され、再起動で失われます。再起動後も保持する用途にはAsyncPostgresStoreなどのDB-backed storeを使うよう説明されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 1. `pip install -U langmem`を実行します。
2. 利用するLLMプロバイダーのAPIキーを環境変数に設定します。
3. `create_manage_memory_tool`と`create_search_memory_tool`をエージェントに追加し、ストアを渡します。
4. エージェントに会話を渡して記憶の保存や検索を行います。

## 変更履歴

- 2026-11-23: 初回登録
