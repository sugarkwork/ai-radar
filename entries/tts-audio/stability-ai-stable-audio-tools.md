---
repo: "Stability-AI/stable-audio-tools"
name: "Stable Audio Tools"
genre: "tts-audio"
url: "https://github.com/Stability-AI/stable-audio-tools"
license: "MIT"
stars: 3898
language: "Python"
created: "2023-05-23"
updated: 2026-11-01
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 489
open_issues: 134
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 1642
archived: false
fetched_at: "2026-11-03T15:42:57Z"
---

# Stable Audio Tools

## 出来ること

- 条件付き音声生成モデル（Stable Audio 系）の推論・学習コード。テキスト条件付きの音楽／効果音生成と、潜在拡散モデルの学習を扱う。
- 音声のオートエンコーダ、拡散／フローマッチング、テキストエンコーダ（T5 系）を組み合わせた構成をモジュール単位で差し替えられる。
- 学習ログは Weights & Biases 前提。マルチ GPU / マルチノードは PyTorch Lightning 経由。

## 目的・背景

Stability AI の音声生成リポジトリ。2023-05 作成、2026-11-01 まで更新が続いている（音声系では珍しく現役）。モデルの重みは HuggingFace 側で別配布され、本リポジトリはコード（と学習基盤）が主。

## 依存関係

- PyTorch 2.5 以上（Flash Attention / Flex Attention 対応のため）。開発は Python 3.10。
- 依存管理は `uv` 前提（README 推奨）。
- `pip install "stable-audio-tools[train]"` で学習用の依存まで入る。
- 学習には W&B アカウントが必要。

## 実行条件

- 推論は GPU 推奨。学習は VRAM 次第でバッチ・勾配蓄積の調整が必要（具体的なしきい値は README に記載なし＝未確認）。
- モデル重みは HuggingFace から別途取得（リポジトリには含まれない）。
- 生成物のライセンスはモデル側の条件に従う。

## 最短手順

```bash
pip install uv
uv pip install "stable-audio-tools[train]"
wandb login
python ./run_gradio.py --pretrained-name stabilityai/stable-audio-open-small
```

## 変更履歴

- 2026-11-03: 初回登録（star 3,898 / pushed 2026-11-01 / MIT）
