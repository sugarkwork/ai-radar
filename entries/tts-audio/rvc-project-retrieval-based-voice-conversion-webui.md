---
repo: "RVC-Project/Retrieval-based-Voice-Conversion-WebUI"
name: "RVC (Retrieval-based Voice Conversion WebUI)"
genre: "tts-audio"
url: "https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI"
license: "MIT"
stars: 39138
language: "Python"
created: "2023-03-27"
updated: "2026-08-04"
added: "2026-11-03"
sources:
  - "https://x.com/RoundtableSpace/status/2117357328152350832"
flags: []
risk_notes: ""
forks: 5349
open_issues: 593
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 15453
archived: false
fetched_at: "2026-11-09T21:43:33Z"
last_release: "2.3.260718"
last_release_at: "2026-07-21"
---

# RVC (Retrieval-based Voice Conversion WebUI)

## 出来ること

- 10分程度の音声データから声質変換（Voice Conversion）モデルを学習できる。歌声・話し声の両方に対応。
- Gradio の WebUI で学習から推論まで完結。リアルタイムのボイスチェンジにも対応（音声デバイス入出力）。
- 学習済みモデルの共有・読み込み（`.pth` + `.index`）が前提の運用も可能。

## 目的・背景

2023-03 公開の RVC 実装。声質変換の事実上の定番で、派生 UI・モデル配布が大量にある。現在の README は **Python 3.12 x64 前提**に更新されており、古い解説記事（Python 3.8〜3.10 前提）とは手順が異なる点に注意。

## 依存関係

- Python 3.12 x64（Ubuntu 24.04 x86_64 を推奨環境として明記）。
- PyTorch 2.7.1 + torchaudio 2.7.1（CUDA 11.8 版 or 12.8 版。RTX 50 系は cu128 一択）。
- システムパッケージ: `ffmpeg`、`libsndfile1`、`libportaudio2`、`python3.12-dev` など。
- 依存は `requirments_cu118_py312.txt` / `requirments_cu128_py312.txt` / `requirments_cpu_py312.txt` に分かれている（ファイル名の綴りは原文ママ）。

## 実行条件

- 学習には NVIDIA GPU が実質必須（README に VRAM の具体値は無し＝未確認）。推論は CPU でも動くが遅い。
- ディスク: リポジトリ約 15MB だが、学習用の事前モデル（hubert / rmvpe 等）とデータセットが別途必要。
- 学習データの権利（声の本人同意）は利用者の責任。README に法的注意の記載は無い。

## 最短手順

```bash
sudo apt install -y python3.12 python3.12-venv python3.12-dev ffmpeg unzip libsndfile1 libportaudio2
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI.git
cd Retrieval-based-Voice-Conversion-WebUI
python3.12 -m venv .venv && source .venv/bin/activate
pip install torch==2.7.1+cu118 torchaudio==2.7.1+cu118 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirments_cu118_py312.txt
python infer-web.py
```

## 変更履歴

- 2026-11-03: 初回登録（star 39,028 / pushed 2026-08-04 / MIT / Python 3.12 前提に更新済み）
