---
type: model
model: PrunaAI/P-H3-Image
name: P-H3-Image
genre: video-gen
url: https://huggingface.co/PrunaAI/P-H3-Image
author: PrunaAI
license: other
license_name: minimax-h3-community-license-agreement
base_model: [MiniMaxAI/MiniMax-H3]
format: diffusers
size: "bf16 約100GB（transformer 66GB＋text encoder 9GB＋upsampler 19GB＋VAE 5.6GB）/ Comfy版 int8 21GB・w4a8 13GB"
downloads: 111
likes: 65
created: 2026-10-27
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/alacheng/status/2117768798023397467
sources:
  - https://huggingface.co/PrunaAI/P-H3-Image-Comfy
  - https://www.pruna.ai/blog/oss-p-h3-image-launch
pricing: free
pricing_detail: "重み無料（MiniMax-H3 Community License）"
signup_required: false
amplifiers:
  - https://x.com/sep_is_heim/status/2118127103782887436
---

# P-H3-Image

## 出来ること

- 動画モデル **MiniMax-H3** を画像生成・画像編集モデルに転用したもの。PrunaAI が H3 から蒸留・再構成し、約7分の1のサイズ・約5倍の速度（同社比較）を主張している。
- **テキスト→画像**と**画像編集**の両方。編集は最大8枚の入力に対応し、1枚目が編集対象、2枚目以降が参照（Picture 2, Picture 3…）。
- 8MP で最も良い結果が出る。既定は 2912×2912。2MP / 4MP も使えるが、顔・手・細部の破綻が増える。編集は 4MP か 8MP が推奨。
- プロンプト・アップサンプラを同梱（任意）。ネガティブプロンプトや guidance_scale は無く、8ステップ固定のサンプリンググリッドを使う。
- 得意分野はフォトリアル、シネマ/エディトリアル調、短い引用テキスト入りのグラフィック。苦手は小さく密集した文字（本文・長いコード）で、疑似文字になる。
- 単体画像のみ（動画・音声は生成しない）。

## 目的・背景

SOTA 動画モデルを画像モデルへ転用する試み。PrunaAI のブログと技術レポートで、H3 の映像知識を画像生成・編集に再利用する手法と、量子化を含む効率化を説明している。2026-10-27 公開、11-04 時点で 111 ダウンロード・65 likes。ComfyUI ネイティブ対応版（`P-H3-Image-Comfy`）も別リポジトリで配布。

## 収録ファイル

- `transformer/` 7分割 合計66.3GB（bf16）、`text_encoder/` 8.9GB、`prompt_upsampler/` 18.8GB、`vae/` 5.6GB
- ComfyUI 版（`PrunaAI/P-H3-Image-Comfy`）: `p-h3-image_bf16.safetensors` 40.5GB / `_int8_convrot` 21.2GB / `_w4a8` 13.4GB、テキストエンコーダ・アップサンプラ・VAE も各量子化版あり

## 実行条件

- bf16 のフル構成は B200 1枚・8MP・バッチ1で、画像生成 約9秒／ピーク 83GB。プロンプトアップサンプラを使うと 6〜11秒追加、ピーク 101GB。
- 自動 CPU オフロードを使えば 80GB 級1枚（H100 等）で動作し、8MP 時のピークは約76GB。
- メモリの少ない GPU では ComfyUI 版の int8 / w4a8 を使う。
- プロンプトに敏感。誇張語や長すぎるプロンプトは品質を下げ、短すぎるプロンプトはアップサンプラ無しだと弱い。
- 手や背景の小さな人物は破綻しうる。8MP にすると軽減する。
- ライセンスは **MiniMax-H3 Community License**。

## 使い方

```python
import torch
from diffusers import ComponentsManager, ModularPipeline

manager = ComponentsManager()
manager.enable_auto_cpu_offload(device="cuda")
pipe = ModularPipeline.from_pretrained("PrunaAI/P-H3-Image", components_manager=manager)
pipe.load_components(dtype=torch.bfloat16)
image = pipe(prompt=prompt, height=3360, width=2496, output="images")[0]
```

```text
ComfyUI: PrunaAI/P-H3-Image-Comfy の diffusion_models / text_encoders / vae を
それぞれのフォルダに置き、同梱のワークフローを使う（int8・w4a8 は軽量環境向け）
```

## 変更履歴

- 2026-11-04: 初回登録
