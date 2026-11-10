---
repo: "coqui-ai/TTS"
name: "Coqui TTS"
genre: "tts-audio"
url: "https://github.com/coqui-ai/TTS"
license: "MPL-2.0"
stars: 46195
language: "Python"
created: "2020-05-20"
updated: "2024-08-16"
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 6163
open_issues: 2
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 170196
archived: false
fetched_at: "2026-11-09T21:42:56Z"
last_release: "v0.22.0"
last_release_at: "2023-12-12"
---

# Coqui TTS

## 出来ること

- 多言語・多話者の TTS ツールキット。Tacotron2 / VITS / Glow-TTS / XTTS など複数アーキテクチャを同一 API で扱う。
- 数秒の参照音声から声を複製するゼロショット音声複製（XTTS v2 系）を含む。
- モデルの学習・ファインチューニング用スクリプトと、`tts` CLI、Python API を提供。

## 目的・背景

Mozilla TTS の後継として Coqui が開発。**最終 push は 2024-08 で、Coqui 社の活動終了後は実質メンテナンス停止**（archived ではないが更新なし）。とはいえ導入の容易さとモデル数の多さから、ローカル TTS の定番として今も参照される。

## 依存関係

- Python 3.9 以上 3.12 未満（README が明記）。
- PyTorch、`pip install TTS`。
- モデルは初回利用時に自動ダウンロード（`tts --model_name ...` または Python API）。

## 実行条件

- 学習には GPU 必須。推論は CPU でも可（XTTS は GPU 推奨）。
- **ライセンスは二層**: リポジトリは MPL-2.0 だが、XTTS などの一部モデルはモデル固有ライセンス（Coqui Public Model License）で商用利用に条件が付く。利用前にモデルカードを確認すること。
- 依存の固定が古く、Python 3.12 以降では入らない（README の範囲外）。

## 最短手順

```bash
pip install TTS
tts --text "こんにちは" --model_name tts_models/ja/kokoro/tacotron2-DDC --out_path out.wav
```

## 変更履歴

- 2026-11-03: 初回登録（star 46,180 / pushed 2024-08-16 / MPL-2.0 / 更新停止）
