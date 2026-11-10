---
type: "repo"
repo: "kgmkm/muse-irodori-voice"
name: "muse-irodori-voice — CPUで固有音声を作るIrodoriキット"
genre: "tts-audio"
url: "https://github.com/kgmkm/muse-irodori-voice"
author: "kgmkm"
license: "MIT"
language: "Python"
stars: 9
forks: 0
open_issues: 0
created: "2026-10-31"
updated: "2026-10-31"
commits_30d: 4
commits_90d: 4
commit_cadence: "weekly"
size_kb: 43
archived: false
risk_notes: "コードはMITだが重みと音声利用条件は別。READMEは特定声優・キャラクターへの模倣を禁じ、同意のない他者のなりすまし等にも注意する。このONNX経路ではSilentCipher透かしが入らないと説明されているためAI音声であることを明示する。速度・同一性・品質は作者の測定で当方未追試。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/memuringo7544/status/2119369839806411188", "https://github.com/kgmkm/muse-irodori-voice", "https://github.com/kgmkm/muse-irodori-voice/blob/main/README.md", "https://github.com/kgmkm/muse-irodori-voice/blob/main/LICENSE"]
added: "2026-11-09"
first_seen: "2026-11-08"
source_post: "https://x.com/memuringo7544/status/2119369839806411188"
fetched_at: "2026-11-09T21:43:13Z"
flags: ["unverified"]
last_release: ""
last_release_at: ""
---

# muse-irodori-voice — CPUで固有音声を作るIrodoriキット

## 出来ること

Irodori-TTS v4.1-Small-MFのONNX int8推論をCPUで使い、キャプションで候補を生成、選んだ声を参照潜在npzで固定する。長文は70–80字程度に分割生成し、間隔0.4秒で結合する手順とスクリプトを収録。

## 目的・背景

Muse VMでエージェントの音声ファイルを作るための第三者キット。アプリのライブ音声会話の声を差し替えるものではなく、事前生成するボイスメモ・ナレーション向け。

## 依存関係

Linux x86_64、Python3.12、onnxruntime1.31.1、numpy/soundfile/pyloudnorm/scipy、トークナイザのための公式Aratako/Irodori-TTS環境。重みはRyoppiのint8配布とraratuのOnsei-iOS-Models等から別途取得する。

## 実行条件

作者の計測環境は2vCPU AVX-512 VNNI・RAM7.7GB。約7.5秒の音声にint8生成37秒・合計約59秒という報告で、リアルタイム対話の性能ではない。float経路を公式と比較してからint8へ移る検証手順を示す。

## 最短手順

公式README/SKILL.mdのdownload_models.sh、venv、tokenize_text.py、infer_onnx.pyの順に進む。キャプション固定で声候補を選び、make_ref_latents.pyで固定し、楽しい文・悲しい文で声と感情を確認してから長文へ使う。

## 注意点

コードはMITだが重みと音声利用条件は別。READMEは特定声優・キャラクターへの模倣を禁じ、同意のない他者のなりすまし等にも注意する。このONNX経路ではSilentCipher透かしが入らないと説明されているためAI音声であることを明示する。速度・同一性・品質は作者の測定で当方未追試。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
