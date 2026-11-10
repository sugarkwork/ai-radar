---
repo: "m-bain/whisperX"
name: "WhisperX"
genre: "tts-audio"
url: "https://github.com/m-bain/whisperX"
stars: 25190
forks: 2543
open_issues: 220
size_kb: 41993
language: "Python"
created: "2022-12-09"
updated: "2026-10-22"
archived: false
license: "BSD-2-Clause"
commits_30d: 6
commits_90d: 9
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "最新版のタグと公開日時、対象音声での速度・単語境界の精度、投稿で紹介された動画制作工程との統合は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2117030430507401326"]
fetched_at: "2026-11-10T08:17:21+00:00"
---

# WhisperXで単語タイムスタンプ付き字幕を作る

## 出来ること

- 音声を文字起こしし、単語単位のタイムスタンプを取得する。CLIはSRTやJSONを出力でき、単語を強調するSRTも生成できる。

## 目的・背景

- 文字起こし結果を言語別の音素モデルで音声に強制アラインメントし、字幕で使う単語の時刻を求める。READMEには著者による字幕同期の比較例がある。速度や精度の独立した実測は行っていない。

## 依存関係

- PythonパッケージをPyPIから導入する。アラインメントには対象言語に対応するモデルが必要で、環境によってはFFmpegなどの追加導入が必要。

## 実行条件

- CPUではint8の実行例がある。GPUを使う場合、確認したREADMEはCUDA Toolkit 12.8の事前導入を案内している。話者分離を使う場合は、Hugging Faceの対象モデルの利用条件への同意と読み取りトークンが必要。リポジトリのコードはBSD-2-Clause。

## 最短手順

- `pip install whisperx` で導入する。
- `whisperx narration.wav --device cpu --compute_type int8 --output_format srt --highlight_words True` で単語強調付きSRTを出力する。
- シェル実行権限のあるAIエージェントからは同じCLIを入力音声のパスとともに呼び出す。単語時刻を後続処理に渡す場合は `--output_format json` に切り替え、生成したJSONを読み取る。

## 変更履歴

- 2026-11-10: 初回登録
