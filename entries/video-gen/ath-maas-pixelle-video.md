---
repo: "ATH-MaaS/Pixelle-Video"
name: "Pixelle-Video"
genre: video-gen
url: "https://github.com/ATH-MaaS/Pixelle-Video"
license: "Apache-2.0"
stars: 29762
language: "Python"
created: "2025-11-07"
updated: 2026-06-14
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 4322
open_issues: 175
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 28868
archived: false
fetched_at: "2026-11-04T22:50:29Z"
last_release: v0.1.15
last_release_at: 2026-01-27
---

# Pixelle-Video

## 出来ること

- テーマを1つ入れると、文案 → AI 配图/動画 → 音声ナレーション → BGM → 合成までを自動で行い、縦型・横型のショート動画を作る。
- 画像・動画・音声の生成手段を差し替えられる: ローカル ComfyUI ワークフロー、クラウドの RunningHub（48GB 級GPU）、または DashScope / OpenAI / Seedream / Seedance / Kling などの直連 API。
- TTS は Edge-TTS / Index-TTS など複数対応。テンプレートによる画風切替、素材のアップロード、過去履歴、バッチ生成。
- 拡張モジュールとして「数字人口播」「图生视频」「动作迁移」を追加済み（2026-01 の更新）。
- Streamlit 製 WebUI と Windows 一键整合包。

## 目的・背景

「テーマ入力だけで完結する縦型ショート動画エンジン」を掲げるプロジェクト。自前でモデルを抱えず、ComfyUI ワークフローか外部 API を原子部品として組み合わせる設計で、画像生成・動画生成・TTS・VLM をそれぞれ差し替えられる点が特徴。

## 依存関係

- Python と `uv`（ソースから入れる場合）。`ffmpeg` が必須。
- 画像/動画生成は次のいずれか: ローカルの ComfyUI（既定 `http://127.0.0.1:8188`）、RunningHub の API キー、各社の直連 API キー。
- LLM の API キー（GPT / 通義千問 / DeepSeek / Ollama など）は脚本生成に必要。

## 実行条件

- ローカル ComfyUI を使わない構成なら、画像・動画生成はクラウド課金が前提。
- 一键整合包は Python / uv / ffmpeg を同梱するため、初回は API キーの設定だけで動く。
- リポジトリ内のリンク（Releases・clone 先）は旧 org 名 `AIDC-AI/Pixelle-Video` を指したまま。現在の API 上の canonical は `ATH-MaaS/Pixelle-Video`。
- 最終 push は 2026-06-14 で、以後の更新は止まっている。

## 最短手順

```bash
git clone https://github.com/ATH-MaaS/Pixelle-Video.git
cd Pixelle-Video
uv run streamlit run web/app.py
# http://localhost:8501 の「⚙️ システム構成」で LLM と画像生成を設定
```

## 変更履歴

- 2026-11-03: 初回登録（star 29,735 / pushed 2026-06-14 / Apache-2.0）
