---
name: "F5-TTS"
genre: "tts-audio"
url: "https://github.com/SWivid/F5-TTS"
repo: "SWivid/F5-TTS"
license: "MIT"
stars: 15588
language: "Python"
created: "2024-10-08"
updated: "2026-11-03"
forks: 2280
open_issues: 69
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 7
size_kb: 2429
archived: false
flags: ["unverified"]
risk_notes: "READMEのベンチマーク値は単一のL20 GPU、26組の入力、16 NFEという条件での報告です。別環境での性能は確認できません。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/noa_gpt/status/2121774600321486897"]
fetched_at: "2026-11-15T05:29:04.266720+00:00"
---

# F5-TTS

## 出来ること

- READMEでは、GradioアプリとCLIによる音声合成、チャンク推論、複数スタイル・話者の生成、音声を参照した生成、学習・ファインチューニング、評価を案内しています。GradioアプリにはQwen2.5-3B-Instructを利用するVoice Chat機能も記載されています。

## 目的・背景

- F5-TTSはConvNeXt V2を用いたDiffusion Transformerによる音声合成として説明されています。READMEはE2 TTSも紹介し、F5-TTS v1 Baseについて2025年3月に学習・推論性能を改善したモデルとして告知しています。

## 依存関係

- READMEのインストール案内はPython 3.10以上、FFmpeg、および利用デバイスに合わせたPyTorchとtorchaudioを示しています。GPU別の導入例もあります。

## 実行条件

- READMEの例では、Python環境を作成し、FFmpegとデバイスに対応するPyTorchを導入してから、pipパッケージまたはeditable installを選びます。Dockerでの起動例もあります。NVIDIA GPU、AMD GPU（Linux）、Intel GPU、Apple Silicon向けの注意や導入例が記載されています。

## 最短手順

- READMEのCLI例では、環境と依存関係を用意した後に `pip install f5-tts` を実行し、`f5-tts_infer-cli --model F5TTS_v1_Base --ref_audio "provide_prompt_wav_path_here.wav" --ref_text "The content, subtitle or transcription of reference audio." --gen_text "Some text you want TTS model generate for you."` の形式で推論します。

## 変更履歴

- 2026-11-15: 初回登録
