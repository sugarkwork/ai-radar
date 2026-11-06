---
type: "model"
name: "Idol"
genre: "3d-motion"
url: "https://huggingface.co/speridlabs/idol"
author: "speridlabs"
pricing: "free"
pricing_detail: "重み・コード・デモは Apache-2.0 で無償公開。ただし入力エンコーダ2件 (DINOv3 ViT-H+、FLUX.2-dev VAE) は HF 上でゲートされており規約同意とトークンが必要"
signup_required: true
model: "speridlabs/idol"
license: "Apache-2.0"
downloads: 17180
likes: 827
format: "safetensors"
size: "3.08 GB (weights; repo total 3.57 GB)"
base_model: []
created: "2026-10-28"
updated: "2026-10-29"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/speridlabs/status/2115890658636656826"]
flags: []
risk_notes: "重み・コード・デモは Apache-2.0 で無償公開（HF API の gated=false を確認）。ただし実行には入力エンコーダ2件（facebook/dinov3-vith16plus-pretrain-lvd1689m、black-forest-labs/FLUX.2-dev の VAE）の HF アクセス承認と hf auth login が必須で、未認証だと EncoderAccessError で停止する。VRAM ピーク 7.2GB（配布元記載）のため 8GB 級 GPU では余裕が少ない。CPU 実行は想定されていない。"
fetched_at: "2026-11-06T08:07:10Z"
---

# Idol — 1枚の画像から3D Gaussian splat を生成する image-to-3D モデル

## 出来ること

- 物体が写った1枚の画像 (写真・レンダリング・生成画像) から、最大 1,048,576 個の 3D Gaussian を生成し、標準的な 3DGS の .ply として出力する
- 見えていない側面も補完して『完全な3D物体』を作る (single-image novel view / 3D completion)
- 背景除去 (BiRefNet) とオブジェクトのフレーミングを前処理として内蔵。--mode synthetic|real で切り抜き余白を切り替える
- 入力画像から推定したカメラ情報を <name>_camera.json として同時に出力し、生成に使われた前処理後画像も保存する
- CLI (python -m idol.sample) と Python API (IdolPipeline) の両方から呼べるので、エージェントのツールとして組み込める

## 目的・背景

- 1枚絵から3Dアセットを作る image-to-3D タスクを、コンシューマGPUで動く規模に落とし込むことを狙ったモデル
- 3D-DiT (denoiser) + octree decoder + Gaussian decoder の構成で、拡散/フローモデルにより潜在表現から Gaussian を直接生成する
- 重み・推論コード・Gradio デモがすべて Apache-2.0 で公開されており、クローズドな3D生成APIに依存せずローカルで回せる

## 収録ファイル

- denoiser.safetensors — 1,482,258,308 bytes (3D-DiT 本体、370.6M params)
- decoder_gs.safetensors — 949,083,036 bytes (Gaussian decoder、237.3M params)
- decoder.safetensors — 203,171,696 bytes (octree decoder、50.8M params)
- birefnet.safetensors — 444,466,856 bytes (背景除去、220.7M params)
- config.json — モデル構成 (denoiser/decoder/decoder_gs、image_size 1024、max_voxel_level 8、使用エンコーダ指定)
- README.md、assets/gallery/*.webp (8枚の作例)、assets/reel.mp4 (34.7 MB の紹介動画)

## 実行条件

- Python 3.10+、PyTorch 2.5+、CUDA 対応 NVIDIA GPU (CPU 実行は想定されていない)
- VRAM ピーク 7.2 GB (配布元記載)。8 GB クラスの GPU では余裕が少ない
- 事前準備: facebook/dinov3-vith16plus-pretrain-lvd1689m と black-forest-labs/FLUX.2-dev (VAE のみ使用) の規約に HF アカウントで同意し、hf auth login または HF_TOKEN を設定
- 初回実行時に重み約3 GBと上記エンコーダが自動ダウンロードされる (別途ダウンロード手順は無い)
- 速度は自己申告: B300 3.4秒 / H100 6.7秒 / RTX 4090 19.1秒 / RTX 3080 46.2秒 (262,144 Gaussians、50 steps、8枚の中央値)

## 使い方

- git clone https://github.com/speridlabs/idol-sdk && cd idol-sdk && pip install -e .
- python -m idol.sample --image photo.jpg --mode real  # 写真は real、レンダ/生成画像は synthetic (デフォルト)
- python -m idol.sample --image renders/ --mode synthetic --out outputs  # ディレクトリ一括処理
- Python: from idol import IdolPipeline; pipeline = IdolPipeline.from_pretrained("speridlabs/idol"); out = pipeline("photo.jpg", mode="real", seed=42, num_gaussians=1_048_576); out.gaussian.save_ply("photo.ply")
- 主なフラグ: --steps (既定50)、--cfg_strength (3.0)、--num_gaussians (32,768〜1,048,576、32の倍数)、--seed、--weights、--no_optimize (既定で torch.compile 等による約1.7倍高速化が有効)
- 出力 .ply は任意の Gaussian splat ビューアで開ける。Web で試すだけなら https://huggingface.co/spaces/speridlabs/idol

## 変更履歴

- 2026-11-06: 初回登録
