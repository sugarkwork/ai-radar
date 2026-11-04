---
type: model
model: third-intelligence/Haas-ja-v1.0
name: Haas-ja-v1.0
genre: tts-audio
url: https://huggingface.co/third-intelligence/Haas-ja-v1.0
author: Third Intelligence
license: Apache-2.0
base_model: []
format: nemo
size: "615.8M パラメータ（.nemo 1ファイル）"
downloads: 1532
likes: 56
created: 2026-10-08
updated: 2026-10-30
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/HuggingModels/status/2117771059265225040
sources:
  - https://github.com/third-intelligence/Haas-ASR
  - https://huggingface.co/datasets/third-intelligence/asr-ja-bench
pricing: free
pricing_detail: "重み無料（Apache-2.0）"
signup_required: false
---

# Haas-ja-v1.0

## 出来ること

- **日本語音声認識（ASR）モデル**。NVIDIA Parakeet-TDT 系の構成（FastConformer エンコーダ＋ TDT デコーダ）で、予測ネットワークの LSTM を **Kimi Delta Attention（KDA）** に置き換えている。
- TDT は各トークンの継続長も予測するため、エンコーダのフレームを1つずつではなく数フレームまとめて進める。KDA 化で推論速度をほぼ変えずに精度を上げた、としている。
- 入力は 16kHz モノラル、128-bin ログメル（25ms 窓・10ms ホップ）。エンコーダは FastConformer 24層・hidden 1024・8ヘッド・8倍サブサンプリング（80ms/フレーム）。
- 公表ベンチマーク **asr-ja-bench v1.1**（5データセット、18,318発話、23.38時間）で、重み付き CER strict **6.12%**。評価したオープンモデルの中では最良で、商用 API の GPT-Transcribe（6.07%）と同水準。MAI-Transcribe 2 / Scribe v2 / Gemini 3.1 Pro には及ばない。
- 長尺音声のデモ（HF Space）と、ベンチマーク再現スクリプトを公開。

## 目的・背景

「速くて正確な日本語 ASR」をオープンに提供する目的で Third Intelligence が公開。学習データは ReazonSpeech と YODAS。CER は表記ゆれを正規化する `jacer` で計算し、strict / flex / kana の3種を報告している（strict は漢字・かなの選択違いも誤りに数える）。2026-10-08 公開、11-04 時点で 1,532 ダウンロード・56 likes。

## 収録ファイル

- `Haas-ja-v1.0.nemo` — NeMo 形式のモデル本体（615.8M パラメータ）
- `config.yaml`、`assets/`（アーキテクチャ図・CER 表・CER vs コスト・CER vs RTFx）

## 実行条件

- **Linux + NVIDIA GPU**。Python 3.11+、NeMo 2.7
- 予測ネットワークが `flash-linear-attention` のカーネル（Triton + CUDA）に依存するため、**CPU と macOS は非対応**
- 推論パッケージは GitHub（Haas-ASR）から `uv sync` で導入する形。`pip install "haas-asr @ git+…"` も可
- ベンチマークの CER は自前の正規化ライブラリ `jacer` に依存するため、他モデルとの比較時は前処理の違いに注意

## 使い方

```bash
git clone https://github.com/third-intelligence/Haas-ASR.git
cd Haas-ASR
uv sync
uv run python examples/quickstart.py --model third-intelligence/Haas-ja-v1.0 example.wav
```

## 変更履歴

- 2026-11-04: 初回登録
