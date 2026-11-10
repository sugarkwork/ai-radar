---
repo: "lakimi-ai-systems/lab-tts"
name: "lab-tts"
genre: "tts-audio"
url: "https://github.com/lakimi-ai-systems/lab-tts"
stars: 8
forks: 0
open_issues: 0
size_kb: 812
language: "Python"
created: "2026-11-03"
updated: "2026-11-03"
archived: false
license: "Apache-2.0"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "最新リリース、実行時の動作と必要VRAM、公開結果の再現性は未確認。Audio8の休止時間は日常文1例での著者報告。モデルの利用条件はリポジトリREADMEの記載を確認した範囲。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/bernvadell/status/2117565104040321039"]
fetched_at: "2026-11-10T09:33:29+00:00"
---

# lab-ttsで比較するスペイン本土のスペイン語TTS

## 出来ること

- Qwen3-TTS 1.7B VoiceDesignで文章の指示から合成参照音声を作り、0.6B Baseでその声を使って別の文を読み上げる。Audio8などと発音、長文での安定性、休止を比較できる。

## 目的・背景

- 発音評価にはWhisperの単語誤り率と、スペイン語向けwav2vec2 CTCによる近似音素表記の誤り率を併用する。READMEは、Whisperが発音の誤りを補正する場合があると説明している。
- 著者の日常文1例の比較では、同じ参照音声を使ったAudio8とQwenの合計休止時間はそれぞれ5.2秒と2.6秒だった。

## 依存関係

- 標準環境はuvで固定し、READMEの記載ではPyTorch 2.8とCUDA 12.8を使用する。ffmpegは動画ツールでのみ必要。Mingの評価には別の仮想環境を使う。

## 実行条件

- READMEの目安はLinuxまたはWSL2と、空きVRAM約10 GBのNVIDIA GPU。コードはApache-2.0で、モデルには個別のライセンスが適用される。READMEではQwen3-TTSとAudio8をApache-2.0、MingをMITと記載している。

## 最短手順

- リポジトリ直下で `uv sync` を実行し、参照音声の設計は `uv run python experiments/01-voice-design/run.py`、発音比較は `uv run python experiments/02-phonetics/run.py` で実行する。
- シェルを使えるAIエージェントからは、同じ作業ディレクトリで対象の実験コマンドを呼び出し、`results/<experiment>/results.json` から評価値と実行環境を読み取る。

## 変更履歴

- 2026-11-10: 初回登録
