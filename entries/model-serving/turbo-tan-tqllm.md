---
name: "tqLLM"
genre: "model-serving"
url: "https://github.com/turbo-tan/tqllm"
repo: "turbo-tan/tqllm"
flags: ["unverified"]
risk_notes: "READMEの1.6.0記載では、Qwen3.5/3.6のMoE GGUFは未検証。MoEモデルはネイティブWindowsで動作せず、WSL 2が必要。"
stars: 131
forks: 17
open_issues: 10
size_kb: 20198
language: "C++"
created: "2026-10-02"
updated: "2026-11-16"
archived: false
license: "Apache-2.0"
commits_30d: 46
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/NFT_Chen/status/2119152668119892110"]
fetched_at: "2026-11-17T04:18:33.018458+00:00"
---

# tqLLM

## 出来ること

- Qwen系モデルとTurboQuant GGUF重みをNVIDIA GPU（CUDA）およびApple Silicon（Metal）で推論し、OpenAI互換HTTPサーバーとして提供する。READMEは、対応モデルの一覧、ローカル実行、複数GPU・複数マシン利用、リクエスト状況を表示するモニターを案内している。

## 目的・背景

- 対応する量子化モデルをローカル環境で推論・提供し、対応アプリケーションやコーディングエージェントから利用するためのC++推論実装。

## 依存関係

- 実行構成によりCUDA対応NVIDIA GPUまたはApple Siliconが必要。Linuxでソースからビルドする手順ではCMakeとCUDAを使用する。モデル重みは別途用意する。

## 実行条件

- READMEの対応表では、モデルごとに対応する重み形式とハードウェアが異なる。例としてQwen3.8-27BはNVIDIAで16 GB以上、Flash-Nextは24 GB GPUと64 GB RAMまたはDGX Spark/GB10が記載されている。MoEモデルはネイティブWindowsでは動作せず、WindowsではWSL 2を使う。

## 最短手順

- LinuxとNVIDIA GPUの場合、対応するQwen GGUFを`models/model.gguf`に配置し、`cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_CUDA_ARCHITECTURES=native`、`cmake --build build --target tqserve -j4`を実行後、`./build/tqserve --model models/model.gguf --port 8086`でサーバーを起動する。READMEにはMac向けインストール手順とDocker手順もある。

## 変更履歴

- 2026-11-22: 初回登録
