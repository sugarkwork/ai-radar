---
name: "VoxMel"
genre: "tts-audio"
url: "https://github.com/VoxDance-Lab/VoxMel"
repo: "VoxDance-Lab/VoxMel"
license: "unknown"
stars: 29
language: "Python"
created: "2026-11-11"
updated: "2026-11-12"
forks: 2
open_issues: 0
commits_30d: 12
commit_cadence: "weekly"
commits_90d: 12
size_kb: 6507
archived: false
flags: ["unverified"]
risk_notes: "README does not state the repository license; the supplied API measurement reports license as unknown. The README says model weights, experiment config, and Vocos weights are not included in the checkout and must be supplied separately. GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/cutetoxicguy/status/2121037830960922877"]
fetched_at: "2026-11-13T08:09:42.027959+00:00"
---

# VoxMel

## 出来ること

- メルスペクトログラムを固定の二軸Haar変換で分解し、Coarse-Melを自己回帰生成、時間・周波数残差を非自己回帰で予測して再構成し、Vocos vocoderで音声に変換する音声合成フレームワーク。READMEは英語・中国語のゼロショット音声クローニングを説明している。変換の可逆性は生成音声やvocoder再構成の損失がないことを保証しない。

## 目的・背景

- 学習済み音響トークナイザーを使わずに、メルスペクトログラムを連続自己回帰音声生成の対象として扱う。READMEは、音響情報の整理方法によって高次元音声生成を扱う手法として説明している。

## 依存関係

- Python 3.10–3.12。README記載の元環境はtorch/torchaudio 2.4.1、CUDA 12.1。requirements.txtはパッケージインストーラーと共有され、Vocosを含む。推論には互換性のある実験configとVoxMel checkpoint、Vocosのconfigと重みを別途用意する必要がある。

## 実行条件

- リポジトリrootでpip install -e .を実行して導入し、Python APIまたはvoxmel CLIから利用する。device="auto"はCUDA、MPS、CPUの順に選択する。READMEはMPSの演算子対応と性能について、使用するcheckpointでの検証が必要と記載している。音声継続クローニングでは参照音声とその正確な転記テキストが必要。

## 最短手順

- 1. Python 3.10–3.12と、使用ハードウェアに対応するPyTorch・torchaudioを用意する。2. リポジトリrootでpip install -e .を実行する。3. 互換性のあるVoxMel実験ディレクトリ（config.yaml、model_L_final.pt）とVocosディレクトリ（config.yaml、pytorch_model.bin）を用意する。4. READMEのPython APIまたはCLI例にmodel、tokenizer、vocosのパスと、合成テキスト・参照音声・転記テキストを指定して生成する。

## 変更履歴

- 2026-11-13: 初回登録
