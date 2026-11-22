---
name: "llama.cpp"
genre: "model-serving"
url: "https://github.com/ggml-org/llama.cpp"
repo: "ggml-org/llama.cpp"
license: "MIT"
stars: 135345
language: "C++"
created: "2023-03-10"
updated: "2026-11-16"
forks: 25656
open_issues: 2625
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 502924
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/naka_1717/status/2119034856676159987"]
fetched_at: "2026-11-16T21:56:21Z"
last_release: "v1.0.0"
last_release_at: "2026-11-13"
---

# llama.cpp

## 出来ること

- C/C++でLLMおよびVLMの推論を実行する。量子化、CPU・GPUハイブリッド推論、複数のハードウェア向けバックエンドに対応するとREADMEは説明している。`llama cli`によるモデル実行と、OpenAI互換APIサーバーの`llama serve`を利用できる。

## 目的・背景

- 幅広いハードウェアで、ローカルまたはクラウド上のLLM・VLM推論を、最小限のセットアップと高い性能を目指して実現することがREADMEに記載された主目的。

## 依存関係

- READMEは「Plain C/C++ implementation without any dependencies」と説明している。また、プロジェクトはggmlライブラリ上に構築されている。

## 実行条件

- 利用する実行バックエンドは対象デバイスに応じて選択する。READMEにはCPU、Apple Silicon、NVIDIA・AMDなどのGPU、および各種アクセラレータ向けバックエンドが記載されている。

## 最短手順

- README記載の例では、インストール後に`llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF`でHugging Face上のモデルを実行し、`llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF`でAPIサーバーを起動する。別の導入方法として、事前ビルド済みバイナリの取得やソースからのビルドも案内されている。

## 変更履歴

- 2026-11-16: 初回登録
