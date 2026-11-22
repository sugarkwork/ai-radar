---
name: "RouteLLM"
genre: "model-serving"
url: "https://github.com/lm-sys/RouteLLM"
repo: "lm-sys/RouteLLM"
license: "Apache-2.0"
stars: 5712
language: "Python"
created: "2024-06-03"
updated: "2024-08-10"
forks: 455
open_issues: 45
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 5472
archived: false
flags: ["unverified"]
risk_notes: "README記載の最大85%のコスト削減・ベンチマーク性能はプロジェクト側の報告であり、独立検証されていない。実際の効果はモデルの組み合わせ、クエリ、しきい値に依存する。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/irongiantXBT/status/2122709093102285099"]
fetched_at: "2026-11-17T23:21:23.356387+00:00"
---

# RouteLLM

## 出来ること

- LLMルーターの配信と評価を行うフレームワーク。READMEによると、OpenAIクライアントの置き換えやOpenAI互換サーバーとして利用でき、クエリを強力なモデルと低コストなモデルの間で振り分ける。ルーターの追加や複数ベンチマークでの比較にも対応する。コスト削減や性能に関する数値はプロジェクト側のベンチマーク報告で、利用環境での結果を保証するものではない。

## 目的・背景

- 高性能モデルは高コストになりやすく、小型モデルは品質が下がる可能性があるという課題に対し、クエリごとのコストしきい値で振り分ける方式を提供する。しきい値はコストと品質のトレードオフを制御し、クエリの種類やモデル構成に応じて調整する。

## 依存関係

- READMEのインストール例は `pip install "routellm[serve,eval]"`。モデル接続にはLiteLLMを利用すると説明されている。`mf` と `sw_ranking` ルーターで埋め込みを生成する場合は、モデル組み合わせによらず `OPENAI_API_KEY` が必要と記載されている。

## 実行条件

- READMEの例ではPython環境と利用するモデル提供元のAPIキーを設定する。OpenAI互換エンドポイントを使う場合は `openai/` をモデル名に付け、`--base-url` と `--api-key` を設定する。ローカルモデル用のOllama手順もREADMEから案内されている。

## 最短手順

- 1. `pip install "routellm[serve,eval]"` でインストールする。
2. 利用する提供元のAPIキーを設定し、Pythonから `Controller(routers=["mf"], strong_model="...", weak_model="...")` を初期化する。
3. `python -m routellm.calibrate_threshold --routers mf --strong-model-pct 0.5 --config config.example.yaml` などで用途に合わせてしきい値を調整する。
4. Chat Completionsの `model` に `router-mf-[THRESHOLD]` 形式を指定してリクエストする。

## 変更履歴

- 2026-11-22: 初回登録
