---
name: "Irodori-TTS"
genre: "tts-audio"
url: "https://github.com/Aratako/Irodori-TTS"
repo: "Aratako/Irodori-TTS"
license: "MIT"
stars: 1586
language: "Python"
created: "2026-02-25"
updated: "2026-11-09"
forks: 188
open_issues: 18
commits_30d: 18
commit_cadence: "weekly"
commits_90d: 19
size_kb: 393
archived: false
flags: ["unverified"]
risk_notes: "READMEは、単一の長時間録音を使う形式は評価されておらず、複数の短い同一話者クリップで測定した結果と異なる場合があると記載している。必要なGPU・VRAMなどの具体的な実行条件は、提示されたREADME部分から確認できない。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/memuringo7544/status/2118972621866012726"]
fetched_at: "2026-11-11T00:15:06.933199+00:00"
---

# Irodori-TTS

## 出来ること

- Flow MatchingベースのTTSの学習・推論コード。READMEでは、参照音声からのゼロショット音声クローニング、v4-Smallでのテキスト・参照音声・captionによる音声設計、複数参照クリップの連結、対応チェックポイントでの絵文字による話し方制御、CLI・Gradio推論、PEFT/LoRA微調整、Speaker Inversionを説明している。SilentCipherが利用可能な場合、生成音声に自動でウォーターマークを付与する。

## 目的・背景

- Echo-TTSを主に参考にしたFlow Matching方式のTTS。生成対象にはDACVAEの連続潜在表現を使う。READMEによると、v4.1-Smallは従来のbase系とVoiceDesign系を一つのチェックポイントに統合し、テキスト、参照音声、captionの3系統の条件付けに対応する。

## 依存関係

- READMEの導入手順はuvを使用し、PyTorchバックエンドとしてNVIDIA CUDA 12.8、AMD ROCm、Intel XPU、CPU向けの相互排他的なextrasを案内している。macOSではcpu extraがPyPIのPyTorch wheelにフォールバックすると記載。GPU・VRAMなどの具体的要件は提示資料から確認できない。

## 実行条件

- READMEはLinux/Windows向けCUDA 12.8、Linux/WSL向けROCm、Linux/Windows向けXPU、CPU、およびmacOSのCPU/MPS経路を案内している。ROCm extraにはpytorch-triton-rocmを含め、READMEではtransformersからtorch._dynamoへのimport経路でtriton.languageを提供するためと説明している。

## 最短手順

- README記載の基本手順は、`git clone https://github.com/Aratako/Irodori-TTS.git`、`cd Irodori-TTS`、利用環境に合うbackend extraを指定して`uv sync --extra cu128`などを実行すること。その後、例では`uv run --no-sync python infer.py --hf-checkpoint Aratako/Irodori-TTS-v4.1-Small --text "こんにちは、私はAIです。これは音声合成のテストです。" --ref-wav path/to/reference.wav --output-wav outputs/sample.wav`で推論する。

## 変更履歴

- 2026-11-11: 初回登録
