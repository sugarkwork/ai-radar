---
type: "model"
name: "Juggernaut Moss V1"
genre: "image-generation"
url: "https://civitai.com/models/3042282/juggernaut-moss"
license: "Apache-2.0"
model: "Juggernaut Moss V1"
downloads: "Civitai・HFから取得"
likes: "Civitai 294 downloads / 40 likes / 43 comments"
created: "2026-11-08"
updated: "2026-11-08"
format: "safetensors"
base_model: "MOSS-Image Base"
parameters: "5B"
quantization: "bf16 / int8 ConvRot"
size_gb: "10.0 / 5.4"
download_url: "https://huggingface.co/Kandoo/Juggernaut-Moss"
risk_notes: "当方で生成・品質検証はしていない。V1のため手・細部文字・群衆・一部アートスタイルに課題。投稿者のブラインドテスト結果（勝率73%）を記載。"
sources: ["https://x.com/aiaicreate/status/2119600990349590556", "https://civitai.com/models/3042282/juggernaut-moss", "https://huggingface.co/Kandoo/Juggernaut-Moss"]
added: "2026-11-09"
first_seen: "2026-11-09"
source_post: "https://x.com/aiaicreate/status/2119600990349590556"
fetched_at: "2026-11-09T03:14:33+00:00"
flags: ["unverified"]
---

# Juggernaut Moss V1

## 目的・背景

MOSS-Image Baseのフルファインチューン。自然な肌・信じられる光・現代的なフィルムルックの実写・シネマティック画像生成に特化。

## 出来ること

- ポートレート・シネマティックシーンの生成
- 光の方向と効果を指定（"soft window light from the left"など）
- レンズ・ショットタイプ指定（"85mm lens at f/2"、"close-up"、"cinematic film still, anamorphic"）
- 肌の質感指定（"visible pores"、"freckles"、"natural skin texture"）
- 画像内テキスト生成（引用符で囲んだ単語を指定）

## 収録ファイル

- BF16: フル品質 ~10GB
- int8 ConvRot: ~5.4GB、Comfy-Org公式int8と同形式、同seedで実質同じ出力

## 実行条件

ComfyUI環境が必要。Text EncoderとVAEは別途必要（Comfy-Org/MOSS-Imageのqwen3.5_9b_bf16またはqwen3.5_9b_w4a8_gptq、flux2-vae_small）。既存のMOSS-Image環境があればText Encoder/VAEを流用可。

推奨設定: 解像度~2MP（1344×1792 portrait、1792×1344 landscape、1536×1536、2048×1152）。1024×1024は弱い。Sampler: Euler、Steps: 30（25-50）、CFG: 3、Shift: 5、Skip Layer Guidance: Layer 22。

## 使い方

ComfyUI: `ComfyUI/models/diffusion_models/`へ配置し"Load Diffusion Model"で読み込み。既存のMOSS-Imageワークフローに差し替えるだけ。

## 出典

- Civitai: https://civitai.com/models/3042282/juggernaut-moss
- Hugging Face: https://huggingface.co/Kandoo/Juggernaut-Moss
- 紹介投稿: https://x.com/aiaicreate/status/2119600990349590556

## 注意点

V1のため以下に課題あり。複雑なポーズ・小物を持つ手、短い単語・看板は比較的良いが長文・極小文字は不安定。背景の群衆の顔がぼやける。風景・建築はBase同等（人物・光・シネマに特化した学習のため）。アートスタイルは明確に指定する必要あり。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
