---
name: "Molt"
genre: "agent-framework"
url: "https://github.com/NVIDIA-NeMo/labs-molt"
repo: "NVIDIA-NeMo/labs-molt"
stars: 1355
forks: 149
open_issues: 21
size_kb: 4146
language: "Python"
created: "2026-06-23"
updated: "2026-11-17"
archived: false
license: "Apache-2.0"
commits_30d: 55
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/alacheng/status/2122247047881400738"]
fetched_at: "2026-11-17T08:29:15.274343+00:00"
---

# Molt

## 出来ること

- Gymnasiumに沿ったEnv.step()またはChatAgent.run()のAPIで、採点器、マルチターンのツール利用、VLM環境、既存エージェントを扱うagentic RLの学習を構成する。READMEによると、Rayがプロセス配置と非同期キューを担い、vLLMがロールアウトを生成し、NeMo AutoModelとFSDP2が単一actorを学習する。トークンID、log-prob、action範囲、報酬、マルチモーダルテンソルをロールアウトから学習まで扱う設計。出典: https://github.com/NVIDIA-NeMo/labs-molt

## 目的・背景

- agentic RL研究向けに、エージェントや報酬をPythonで記述し、ロールアウトと学習を同じ実行基盤で扱うことを目的としている。READMEは、Hugging Face形式のモデルを使い、同じチェックポイントをvLLMとtrainerに渡せると説明している。これらはREADMEに記載された機能説明であり、独立した実測結果ではない。出典: https://github.com/NVIDIA-NeMo/labs-molt

## 依存関係

- README記載の構成要素はRay、vLLM、NeMo AutoModel、PyTorch、FSDP2。コンテナ構成にはCUDA 13、torch 2.14、TransformerEngine、flash-attn、mamba、DeepEP、NeMo AutoModelが挙げられている。出典: https://github.com/NVIDIA-NeMo/labs-molt

## 実行条件

- READMEによると、ローカルインストールにはCUDA 13とtorch==2.14.0+cu130が必要で、CUDA 12環境は動作しない。580未満のホストドライバーでは、CUDA forward-compatibility layerを含み自動で有効化するコンテナを使うよう案内されている。READMEはA100、H100、H200、B200、GB200向けのコンテナを記載している。出典: https://github.com/NVIDIA-NeMo/labs-molt

## 最短手順

- README記載の導入手順は、`git clone https://github.com/NVIDIA-NeMo/labs-molt.git`、`cd labs-molt`の後、コンテナを使う場合は`docker pull hijkzzz/molt:latest`、ローカル開発の場合は`pip install -e ".[vllm]"`を実行する。READMEはPyPIの`molt-rl`をサポート対象の導入方法としていない。出典: https://github.com/NVIDIA-NeMo/labs-molt

## 変更履歴

- 2026-11-22: 初回登録
