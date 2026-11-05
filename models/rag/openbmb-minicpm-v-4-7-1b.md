---
type: model
model: openbmb/MiniCPM-V-4.7-1B
name: MiniCPM-V 4.7（1B・オンデバイス VLM）
genre: rag
url: https://huggingface.co/openbmb/MiniCPM-V-4.7-1B
author: OpenBMB（清華大学 THUNLP / ModelBest）
license: Apache-2.0
base_model: []
format: safetensors
size: "約6.3GB（配布全体）。GGUF / AWQ / GPTQ / FP8 / int4 の派生あり"
downloads: 293175
likes: 413
created: 2026-10-06
updated: 2026-10-30
added: 2026-11-05
first_seen: 2026-10-21
source_post: https://x.com/opensourcelab9/status/2113035113537970380
sources:
  - https://github.com/OpenBMB/MiniCPM-V
  - https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B
  - https://huggingface.co/openbmb/MiniCPM-V-4.7-1B-gguf
pricing: free
pricing_detail: "重み無料（Apache-2.0）"
signup_required: false
flags: []
risk_notes: ""
---

# MiniCPM-V 4.7（1B・オンデバイス VLM）

## 出来ること

- 画像・複数画像・動画を読む VLM の 1B 版。単体の GPU やスマートフォンの上で動くことを狙った設計。
- 視覚エンコーダの**内部で早めに視覚トークンを圧縮**する（LLaVA-UHD v4 の intra-ViT early compression）。4倍／16倍の混合圧縮を切り替えられるので、精度と推論コストのバランスをタスクごとに選べる。
- 対応プラットフォームは iOS / Android / HarmonyOS。Rockchip・Houmo・Intel・AMD・Arm のチップ向けに day-0 対応をうたっている。
- 推論は SGLang / vLLM / llama.cpp / Ollama、学習は SWIFT / LLaMA-Factory。GGUF・BNB・AWQ・GPTQ・FP8 の量子化版が配布されている。
- 同系列に **35B-A3B** 版があり、そちらは 140.9GB（downloads 553,116 / likes 1,110）。用途が違うので重みは別リポジトリ。

## 目的・背景

「性能と推論効率のパレートフロンティア」を 1B クラスで押し上げるのが狙い。カードでは Instruct モードで Qwen3.5 0.8B を総合スコアと推論効率の両方で上回るとしている（**作者の主張**）。文書や撮影画像を端末の外に出さずに読ませる用途を想定している。

## 収録ファイル

- `model-*.safetensors`（BF16、合計 約6.3GB）と `config.json`・processor 関連
- 派生リポジトリ: `-gguf`（llama.cpp / Ollama 用）、`-AWQ` / `-GPTQ` / `-int4` / `-FP8`、`-DSpark`（投機的デコード版）
- ライセンスは Apache-2.0（1B）。35B-A3B 版は別途カードの条件を確認する

## 実行条件

- 1B でも BF16 で 6.3GB 前後。量子化版なら端末側に収まる。モデルカードは「iPhone 17 Pro Max でメモリ3GB・毎秒13トークン以上」としているが、これは**カード／投稿側の計測値**で、実機での追試は未確認。
- `transformers` の該当バージョン（`minicpmv4_7` アーキテクチャ）が要る。GGUF 経路は llama.cpp / Ollama の対応版が必要。
- 画像の OCR 精度はカードの OCRBench 90.4 が根拠。これは「画像情報を16分の1に圧縮した条件」での値だと投稿は説明している。
- 長い文書を丸ごと渡す用途では、4x/16x の圧縮率と分割の設計が精度を左右する。

## 使い方

```bash
# 量子化版（端末・CPU 向け）の例
hf download openbmb/MiniCPM-V-4.7-1B-gguf --local-dir ./minicpm-v-4.7-1b-gguf
# Ollama で動かす場合はカードの Modelfile 手順に従う
```

## 変更履歴

- 2026-11-05: 初回登録（downloads 293,175 / likes 413 / Apache-2.0 / 更新 2026-10-30）
