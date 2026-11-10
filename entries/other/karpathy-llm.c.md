---
repo: "karpathy/llm.c"
name: "llm.c"
genre: "other"
url: "https://github.com/karpathy/llm.c"
stars: 31421
forks: 3814
open_issues: 231
size_kb: 2151
language: "Cuda"
created: "2024-04-08"
updated: "2025-06-26"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "最新リリースの版と日時は未確認。CPUデモの実行、PyTorchとの照合、CUDA版の速度と学習費用は独立に検証していない。外部の重みとデータの利用条件は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:52:24Z"
---

# llm.c — GPT-2の学習処理をCとCUDAで読む

## 出来ること

- CPUのFP32参照実装で、GPT-2 124Mの既存重みを使った追加学習を試せる。READMEに掲載された著者のCPU実行例では、40ステップで検証損失が約5.25から約4.11に下がった。
- CUDA版ではGPUでの事前学習を試せる。公式Discussion #481に著者のGPT-2 124M再現手順がある。

## 目的・背景

- 順伝播、逆伝播、パラメータ更新をCコードで追い、CUDA版やPyTorch参照実装と読み比べられる。READMEにはロジットと損失をPyTorchと照合するテストもある。

## 依存関係

- CPUデモはCコンパイラ、make、GPT-2の重みとトークン化済みtinyshakespeareデータを使う。付属のスクリプトで重みとデータを取得できる。Pythonで入力を生成する経路ではrequirements.txtの依存関係が必要。複数GPUの手順ではMPIとNCCLを使う。
- リポジトリのコードはMITライセンス。外部の重みやデータの利用条件、GPUの費用は利用環境と配布元による。

## 実行条件

- CPU経路はGPUなしで試せる。CUDA経路にはCUDA対応GPUとCUDAのビルド環境が必要。READMEには単一GPU向けのFP32手順もある。

## 最短手順

- CPUではリポジトリ直下でREADMEのスターターパック手順に沿って重みとデータを用意し、`make train_gpt2`でビルドして`OMP_NUM_THREADS=8 ./train_gpt2`を実行する。開始時と終了時の検証損失と生成例を確認する。
- シェルを利用できるAIエージェントからは、入力とビルド済みバイナリがある作業ディレクトリで同じCPUコマンドを呼び出し、標準出力の検証損失を取得できる。

## 変更履歴

- 2026-11-10: 初回登録
