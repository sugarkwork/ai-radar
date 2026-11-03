---
repo: "svc-develop-team/so-vits-svc"
name: "so-vits-svc"
genre: "tts-audio"
url: "https://github.com/svc-develop-team/so-vits-svc"
license: "AGPL-3.0"
stars: 28067
language: "Python"
created: "2023-03-10"
updated: 2023-11-11
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 5015
open_issues: 27
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 11145
archived: true
fetched_at: "2026-11-03T15:43:02Z"
---

# so-vits-svc

## 出来ること

- 歌声変換（Singing Voice Conversion）。SoftVC + VITS 構成で、声質だけを差し替える。
- 学習・前処理・推論のスクリプト一式（`preprocess` / `train` / `inference`）。
- **モデルは同梱されない**。README に「本プロジェクトはフレームワークであり、単体では音声合成機能を持たない。モデルは利用者が自分で学習する必要がある」と明記されている。

## 目的・背景

2023-03 公開、最終 push 2023-11-11 で **archived**。当時の歌声変換ブームの中心だった実装で、派生フォーク（so-vits-svc-fork など）が現在も更新されている。本家は更新停止しているため、新規に使う場合はフォークか後発手法を検討する。

## 依存関係

- Python 3.8.9 で動作確認（README 記載）。実際にはより新しい Python でも動くが未保証。
- PyTorch、torchaudio、librosa、fairseq など（`requirements.txt`）。
- 学習には事前学習モデル（ContentVec / hubert 等）を別途ダウンロードする必要がある。

## 実行条件

- 学習には NVIDIA GPU 必須。VRAM 溢れを避けるため音声クリップは 5〜15 秒に切るよう README が推奨。
- ブランチは `4.1-Stable` が既定。
- 声の権利・肖像権まわりは利用者責任。学習データの同意が前提。

## 最短手順

```bash
git clone -b 4.1-Stable https://github.com/svc-develop-team/so-vits-svc.git
cd so-vits-svc
pip install -r requirements.txt
python preprocess_flist_config.py
python train.py -c configs/config.json -m 44k
```

## 変更履歴

- 2026-11-03: 初回登録（star 28,067 / pushed 2023-11-11 / AGPL-3.0 / archived・モデル非同梱）
