---
name: "ZML"
genre: "model-serving"
url: "https://github.com/zml/zml"
repo: "zml/zml"
license: "Apache-2.0"
stars: 4261
language: "Zig"
created: "2024-09-17"
updated: "2026-11-18"
forks: 209
open_issues: 59
commits_30d: 99
commit_cadence: "daily"
commits_90d: 100
size_kb: 82330
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119310454266741105"]
fetched_at: "2026-11-19T00:21:30.807863+00:00"
---

# ZML

## 出来ること

- AIモデルの推論を実行するスタック。READMEでは、NVIDIA CUDA、AMD ROCm、Intel OneAPI、Google TPU、AWS Trainium／Inferentia 2、およびCPU向けのビルド設定を案内している。LLM例はLlama 3.1／3.2、Qwen 3.5、LFM 2.5に対応し、モデルをHugging Face、ローカルディレクトリ、S3から読み込める。

## 目的・背景

- READMEは、AIワークロードを特定のハードウェアから切り離す本番向け推論スタックと説明している。Zig、MLIR、Bazelを使用し、対応アクセラレータ向けにコンパイルする設計を掲げている。

## 依存関係

- README記載のビルド前提条件はBazelで、Bazelisk経由の導入を推奨している。

## 実行条件

- READMEの手順はmacOSまたはLinuxでのBazelisk導入を示している。LLM例ではモデル取得元や対象モデルに応じてHugging Face認証が必要な場合があり、gated repoにはログインまたはHF_TOKENを使う。GPU／TPU等を使う場合は対応するプラットフォームフラグを追加する。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載のMNISTスモークテストは `bazel run //examples/mnist`。LLMを直接実行する例は `bazel run //examples/llm -- --model=hf://meta-llama/Llama-3.2-1B-Instruct --prompt="What is the capital of France?"`。

## 変更履歴

- 2026-11-23: 初回登録
