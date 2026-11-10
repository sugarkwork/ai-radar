---
repo: "facebookresearch/demucs"
name: "Demucs"
genre: "tts-audio"
url: "https://github.com/facebookresearch/demucs"
license: "MIT"
stars: 10406
language: "Python"
created: "2019-10-25"
updated: "2024-04-24"
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 1674
open_issues: 275
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 78580
archived: true
fetched_at: "2026-11-09T21:43:04Z"
last_release: ""
last_release_at: ""
---

# Demucs

## 出来ること

- 楽曲をボーカル／ドラム／ベース／その他（4ステム）に分離する音源分離モデル。v4 系の Hybrid Transformer Demucs（htdemucs）が既定。
- CLI 一発で分離できる: `demucs track.mp3` → `separated/htdemucs/track/{vocals,drums,bass,other}.wav`。
- 2ステム（ボーカル／インスト）モードや、独自データでの学習にも対応。

## 目的・背景

Meta の研究リポジトリ。**リポジトリは archived で、作者が Meta を離れたためメンテナンス終了と README に明記**されている。動作はするが、バグ修正・依存更新は見込めない。同等機能は torchaudio の HDemucs 実装でも提供されている（README に移行先として記載）。

## 依存関係

- Python 3.8 以上。分離だけなら `requirements_minimal.txt`。
- PyTorch、torchaudio、ffmpeg。
- `pip install -U demucs` で導入可能。

## 実行条件

- GPU 推奨。CPU でも動くが長尺曲は時間がかかる。
- 分離品質と速度のトレードオフは `--shifts` / `--overlap` で調整。
- 古い依存（torch 1.x 系前提の記述も残る）ため、新しい Python / torch では導入時に詰まることがある＝未確認。

## 最短手順

```bash
python3 -m pip install -U demucs
demucs --two-stems=vocals track.mp3
```

## 変更履歴

- 2026-11-03: 初回登録（star 10,402 / pushed 2024-04-24 / MIT / archived）
