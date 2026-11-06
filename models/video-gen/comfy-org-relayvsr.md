---
type: model
model: Comfy-Org/RelayVSR
name: RelayVSR（ComfyUI 向け 2x/4x 動画アップスケーラ）
genre: video-gen
url: https://huggingface.co/Comfy-Org/RelayVSR
author: Comfy-Org
license: Apache-2.0
base_model: [kopper/RelayVSR, lightx2v/RelayVSR_X2]
format: safetensors（int8 / fp32）
size: "x2 lightx2v int8 / x4 int8 の拡散モデル ＋ VAE（fp32）各1"
downloads: 0
likes: 24
created: 2026-11-05
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/BennyDaBall_OG/status/2118472181747220682
sources:
  - https://huggingface.co/kopper/RelayVSR
flags: [unverified]
risk_notes: "速度・画質の比較数値は投稿者（RTX 5090）の計測で、モデルカードに計測条件の記載がない。第三者追試は未確認。"
---

# RelayVSR

## 出来ること

- **AI 動画向けの 2倍 / 4倍アップスケーラ**。ComfyUI で使えるように再パッケージされたモデルファイル一式。
- 配布物は4ファイル: `relayvsr_x2_lightx2v_int8_convrot.safetensors`、`relayvsr_x4_int8_convrot.safetensors`（拡散モデル）と、`relayvsr_flash_vae_x2_fp32.safetensors`、`relayvsr_flash_vae_x4_fp32.safetensors`（VAE）。
- 置き場所は `ComfyUI/models/diffusion_models/` と `ComfyUI/models/vae/`。ComfyUI のワークフローから呼び出す。
- 1-step 系の拡散モデルで、キーフレームに対して動かす構成（投稿の説明）。RTX Video Super Resolution のようなフィードフォワードCNNと違い、**ディテールを足す**方向のアップスケール。

## 目的・背景

MiniMax H3 などで生成した動画は、解像度を上げるとディテールが甘くなる。従来のアップスケーラ（RTX VSR）は速いが、元動画のフリッカーをそのまま通し、顔も保持する代わりに情報を足さない。RelayVSR は拡散モデルでディテールを再構成する方向を狙う。kopper の原モデルを Comfy-Org が ComfyUI 用に整えたもの。

## 収録ファイル

- `diffusion_models/relayvsr_x2_lightx2v_int8_convrot.safetensors`
- `diffusion_models/relayvsr_x4_int8_convrot.safetensors`
- `vae/relayvsr_flash_vae_x2_fp32.safetensors`
- `vae/relayvsr_flash_vae_x4_fp32.safetensors`

## 実行条件

- ComfyUI が必要。int8 版のため VRAM 消費は fp16 より軽いが、投稿者の計測では **11.6GB**（2688×1536・124フレーム）。
- 投稿の比較（RTX 5090・同一H3クリップ）: 処理時間 5.8秒 vs RTX VSR 1.3秒、VRAM 11.6GB vs 2.9GB、ディテール 4.8x vs 2.7x、フリッカー 0.98 vs 1.18、顔一致 0.87 vs 0.97。**これは投稿者の計測で、カードに条件の記載はない**。
- ライセンスは Apache-2.0（再パッケージ側）。原モデル kopper/RelayVSR の条件も確認する。
- 2026-11-05 公開（DL 0・likes 24、取得時点）。

## 使い方

```text
ComfyUI/
├── models/diffusion_models/relayvsr_x2_lightx2v_int8_convrot.safetensors
├── models/diffusion_models/relayvsr_x4_int8_convrot.safetensors
├── models/vae/relayvsr_flash_vae_x2_fp32.safetensors
└── models/vae/relayvsr_flash_vae_x4_fp32.safetensors
```

ComfyUI を再起動し、アップスケール用のワークフローでモデルとVAEを選択する。

## 変更履歴

- 2026-11-05: 初回登録（likes 24 / Apache-2.0 / 公開同日）
