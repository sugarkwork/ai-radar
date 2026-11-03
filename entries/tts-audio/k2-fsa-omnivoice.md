---
repo: "k2-fsa/OmniVoice"
name: "OmniVoice"
genre: tts-audio
url: "https://github.com/k2-fsa/OmniVoice"
license: "Apache-2.0"
stars: 16256
language: "Python"
created: "2026-03-31"
updated: 2026-11-02
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 2379
open_issues: 78
commits_30d: 0
commits_90d: 1
commit_cadence: stale
size_kb: 1152
archived: false
fetched_at: "2026-11-03T22:58:14Z"
last_release: 0.2.1
last_release_at: 2026-07-16
---

# OmniVoice

## 出来ること

- 600言語以上に対応するゼロショット TTS。参照音声を数秒渡すだけで声質を複製（voice cloning）できる。
- 声質設計（voice design）: 性別・年齢・ピッチ・方言/アクセント・ささやき声などの属性を指定して声を作る。
- 非言語記号（`[laughter]` など）の埋め込みと、ピンインや音素による発音補正に対応。
- 推論が速く、README では RTF 0.025（実時間の約40倍）と記載。diffusion language model 風のアーキテクチャ。
- ローカル Web UI（`omnivoice-demo`）、Python API、CLI、Hugging Face Space、Colab、学習・評価スクリプトを同梱。

## 目的・背景

k2-fsa（icefall / sherpa 系の音声認識・合成チーム）による多言語 TTS。多言語対応とゼロショット声質複製を同時に狙い、参照音声の書き起こし（`ref_text`）を省略した場合は Whisper で自動転記する。話者の再利用（セッションを跨いだ声の保存）も API から行える。

## 依存関係

- PyTorch 2.8.0 + torchaudio（CUDA 12.8 / Apple Silicon / Intel XPU のいずれか）。
- `pip install omnivoice`、または `git clone` して `uv sync`。
- モデル重みは Hugging Face（`k2-fsa/OmniVoice`）から取得。

## 実行条件

- GPU 推奨。CPU でも動くが速度は落ちる。マルチ GPU 環境では Whisper の配置を `asr_device` で指定できる。
- Hugging Face へ繋がらない場合は `export HF_ENDPOINT="https://hf-mirror.com"`。
- RTF の数値は作者記載で、環境依存。独立したベンチマークは未確認。

## 最短手順

```bash
pip install torch==2.8.0+cu128 torchaudio==2.8.0+cu128 \
  --extra-index-url https://download.pytorch.org/whl/cu128
pip install omnivoice
omnivoice-demo --ip 0.0.0.0 --port 8001
```

## 変更履歴

- 2026-11-03: 初回登録（star 16,256 / pushed 2026-11-02 / Apache-2.0）
