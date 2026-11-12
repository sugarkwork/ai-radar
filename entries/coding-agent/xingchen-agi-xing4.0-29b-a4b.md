---
name: "Xing4.0-29B-A4B"
genre: "coding-agent"
url: "https://github.com/XingChen-AGI/Xing4.0-29B-A4B"
repo: "XingChen-AGI/Xing4.0-29B-A4B"
license: "Apache-2.0"
stars: 106
language: "unknown"
created: "2026-09-17"
updated: "2026-11-10"
forks: 10
open_issues: 2
commits_30d: 7
commit_cadence: "weekly"
commits_90d: 35
size_kb: 1630
archived: false
flags: ["unverified"]
risk_notes: "READMEから最低限必要なハードウェア構成、依存パッケージのバージョン、利用料金は確認できない。評価値はREADME記載の作者側の報告で、独立実測ではない。"
type: "repo"
added: "2026-11-12"
first_seen: "2026-11-12"
sources: ["https://x.com/ai_hakase_/status/2118540382145228865"]
fetched_at: "2026-11-12T14:21:14.948119+00:00"
---

# Xing4.0-29B-A4B

## 出来ること

- 29B総パラメータ、トークンあたり4B活性のモデル。READMEは256Kのネイティブコンテキスト長と512Kへの拡張を記載している。マルチステップ計画やツール呼び出しを含むエージェント用途を想定し、README記載の評価結果にはSWE-bench Verified 75.0、Terminal-Bench 2.1 57.5などがある。評価値は作者報告であり、独立実測ではない。

## 目的・背景

- READMEによると、中国電信人工知能技術有限公司が開発し、Ascend NPU上でMindSporeを用いて訓練されたTeleChatの後継世代。複雑なエンジニアリングタスク向けに最適化したとしている。

## 依存関係

- ローカル推論例はPyTorchとTransformersのAutoModelForCausalLM、AutoTokenizerを使用し、モデル読込時にtrust_remote_code=Trueを指定する。サービング対応としてvLLM、SGLang、KTransformersを、ファインチューニング対応としてLLaMA-Factory、MindFormers、FlagOSをREADMEに列挙。必要なバージョンや完全な依存一覧はREADME抜粋から確認できない。

## 実行条件

- 例ではdevice_map="auto"、dtype=torch.bfloat16を指定する。READMEはAscend 910Cクラスタへの適応を記載し、llama.cppについてはGGUFをCPU/CUDAで利用できるとしている。ローカル実行に必要な最小メモリ・GPU構成は記載されていない。

## 最短手順

- READMEの例に従い、TransformersでAutoTokenizer.from_pretrained("XingChen-AGI/Xing4.0-29B-A4B", trust_remote_code=True)を読み込み、AutoModelForCausalLM.from_pretrainedでモデルをロードする。チャットテンプレートで入力を整形し、model.generateで生成する。README記載の例は依存関係や対応環境の導入手順を含まない。

## 変更履歴

- 2026-11-12: 初回登録
