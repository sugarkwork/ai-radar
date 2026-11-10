---
repo: "karpathy/nanochat"
name: "nanochat"
genre: "other"
url: "https://github.com/karpathy/nanochat"
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日は未確認。学習時間とCOREスコアはプロジェクトの報告で、独立再現は行っていない。実際のGPU利用料金、学習データの個別の利用条件、CLIの実行動作は未検証。"
pricing_detail: "READMEの約48米ドルはH100を8基、1基あたり毎時約3米ドルで約2時間利用する想定の概算。コードはMITライセンス。"
stars: 60415
forks: 8471
open_issues: 137
size_kb: 2520
language: "Python"
created: "2025-10-13"
updated: "2026-09-07"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:52:22Z"
---

# nanochat — トークナイザー学習から対話までを追えるLLM実験リポジトリ

## 出来ること

- トークナイザー学習、事前学習、教師あり微調整、評価、対話推論を一つのリポジトリで実施できる。

## 目的・背景

- 単一GPUノードを想定した改変しやすい実験基盤。README掲載のリーダーボードでは、H100を8基使った1.65時間の実行でDCLM COREが0.2626、比較対象のGPT-2が0.256525。比較の範囲はこの評価指標。

## 依存関係

- Python環境はuvで管理し、GPU用とCPU・MPS用の依存セットがある。参照スクリプトは学習データのシャードを取得し、torchrunで分散学習を起動する。

## 実行条件

- GPT-2比較用の参照手順はH100を8基搭載する単一ノード向け。データ取得用のネット接続と、データおよび中間生成物を保存する領域が必要。GPU費用は利用単価と稼働時間で変わる。

## 最短手順

- 公式リポジトリを取得し、H100を8基搭載したノードで `bash runs/speedrun.sh` を実行する。学習後は `source .venv/bin/activate` で仮想環境を有効にし、`python -m scripts.chat_cli` で対話する。
- AIから呼ぶ手順。端末実行権限のあるAIエージェントは、学習済みチェックポイントを利用できる環境で `python -m scripts.chat_cli -p 'Why is the sky blue?'` を起動し、標準出力を受け取る。

## 変更履歴

- 2026-11-10: 初回登録
