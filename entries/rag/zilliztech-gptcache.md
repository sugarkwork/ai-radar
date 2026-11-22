---
name: "GPTCache"
genre: "rag"
url: "https://github.com/zilliztech/GPTCache"
flags: ["unverified"]
risk_notes: "READMEは開発中でAPIが変更される可能性があると説明している。また、新しいAPIやモデルの追加サポートは行わない旨が記載されている。キャッシュによるコスト・速度改善の数値はREADMEの主張であり、独立した実測結果としては確認していない。"
repo: "zilliztech/GPTCache"
stars: 8228
forks: 608
open_issues: 103
size_kb: 24343
language: "Python"
created: "2023-03-24"
updated: "2026-09-22"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 10
commit_cadence: "monthly"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:16:36.562968+00:00"
---

# GPTCache

## 出来ること

- LLMへの問い合わせと応答をキャッシュし、完全一致または類似検索でキャッシュ済みの応答を取得する。READMEには、OpenAI APIとの利用例、温度パラメーターによるキャッシュ検索の制御例、LangChainとの統合、および言語を問わず利用できるGPTCacheサーバーの案内がある。コストを10分の1、速度を100倍にするという記述はREADME上の宣伝文句で、独立した実測としては確認していない。

## 目的・背景

- READMEでは、LLMアプリケーションの利用増加に伴うAPI呼び出し費用や応答時間の課題に対し、LLM応答を保存するセマンティックキャッシュとして紹介されている。

## 依存関係

- 基本的なキャッシュ機能には限定されたライブラリのみをインストールし、追加機能が必要な場合は関連ライブラリを自動インストールするとREADMEにある。類似検索の例ではOnnx、SQLite、FAISSを使用している。

## 実行条件

- README記載の最低Pythonバージョンは3.8.1。OpenAI APIを使う例ではOPENAI_API_KEY環境変数の設定が必要。

## 最短手順

- README記載の導入コマンドは `pip install gptcache`。OpenAI APIとの例では `from gptcache import cache` と `from gptcache.adapter import openai` を読み込み、`cache.init()` と `cache.set_openai_key()` を呼び出している。

## 変更履歴

- 2026-11-22: 初回登録
