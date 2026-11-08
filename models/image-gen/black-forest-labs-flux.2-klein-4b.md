---
name: "FLUX.2 [klein] 4B"
model: "black-forest-labs/FLUX.2-klein-4B"
genre: "image-gen"
url: "https://huggingface.co/black-forest-labs/FLUX.2-klein-4B"
author: "Black Forest Labs"
license: "Apache-2.0"
downloads: 435063
likes: 1098
created: "2026-01-14"
updated: "2026-02-24"
format: "safetensors"
size: "23.7 GB"
base_model: []
pricing: "free"
pricing_detail: "重みはApache-2.0で無償・商用可。公式ホストAPIは従量課金（FLUX.2 [klein] 4B: 1枚目1MP $0.014、追加MP $0.001、参照画像 $0.001/MP）。"
signup_required: false
flags: []
risk_notes: "VRAM要件がモデルカード（約13GB）と公式コードリポジトリREADME（約8GB）で一致しない。速度・品質はベンダー主張で独立した第三者実測は未確認。同ファミリーの9B系とFLUX.2 [dev]はFLUX Non-Commercial Licenseなので混同しないこと。投稿のmedia画像3枚は他項目（OpenCreator / Social Media Research Skills / Local Deep Research）の紹介でFLUX.2の情報を含まない。"
type: "model"
added: "2026-11-08"
first_seen: "2026-11-08"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
fetched_at: "2026-11-08T02:03:00Z"
---

# FLUX.2 [klein] 4B — Apache-2.0で商用可の4B画像生成・編集モデル

## 出来ること

- テキストプロンプトから画像を生成する（モデルカードの例は1024×1024、4ステップ、guidance_scale=1.0）。
- 参照画像1枚での編集と、複数参照画像を使った編集・生成を同一モデルで行う。
- 商用利用可能なApache-2.0の重みとして、ローカル実行・ファインチューニング・プロダクト組み込みに使える。
- Diffusers（Flux2KleinPipeline）、ComfyUI、Black Forest LabsのホストAPI（従量課金）のいずれでも呼び出せる。
- 公式APIの価格はFLUX.2 [klein] 4Bで1枚目1MPあたり$0.014、追加MP $0.001、参照画像 $0.001/MP。

## 目的・背景

- Black Forest LabsのFLUX.2ファミリーのうち、速度と小型化を優先したKlein系の4Bモデル。2026-01-14公開。
- Klein系は生成と編集を1つのコンパクトなアーキテクチャに統合し、コンシューマGPUでのリアルタイム用途を狙う。
- ライセンスはモデルごとに異なり、4B（および4B Base）はApache-2.0、9B系とFLUX.2 [dev]はFLUX Non-Commercial License。投稿の「Klein 4BはApacheライセンス」という主張はモデルカードと公式リポジトリの両方で確認できた。
- 第三者による独立評価はモデルカードに無く、品質・速度の記述はベンダー主張。

## 収録ファイル

- flux-2-klein-4b.safetensors — 単一ファイル重み（7.75GB、diffusion-single-fileタグ）。
- transformer/diffusion_pytorch_model.safetensors — DiT本体（7.75GB）。
- text_encoder/model-00001-of-00002.safetensors と model-00002-of-00002.safetensors — テキストエンコーダ（計約8.0GB）。
- vae/diffusion_pytorch_model.safetensors — VAE（168MB）。
- tokenizer/（tokenizer.json、vocab.json、merges.txt、chat_template.jinja ほか）、scheduler/scheduler_config.json、model_index.json。
- LICENSE.md（Apache License 2.0全文）、README.md（モデルカード）、realism.jpg / editing.jpg / others.jpg（作例）。
- リポジトリ合計は約23.7GB（LFSサイズの合計）。

## 実行条件

- GPU: NVIDIA RTX 3090/4070以上。VRAM要件はモデルカードが約13GB、公式コードリポジトリのREADMEが約8GBと記載しており食い違うため、13GB以上を見込むのが安全。
- Python + PyTorch（bfloat16、CUDA）。公式推論コードはCUDA 12.9 / Python 3.12でテスト済みとREADMEに記載。
- Diffusersの最新版（Flux2KleinPipeline同梱）が必要。
- Hugging Face上はgated=falseで、ログインや利用申請なしに重みを取得できる。
- 公式APIを使う場合はbfl.aiのアカウントとAPIキーが必要。

## 使い方

- DiffusersをGitHubから入れる: pip install git+https://github.com/huggingface/diffusers.git
- from diffusers import Flux2KleinPipeline; pipe = Flux2KleinPipeline.from_pretrained("black-forest-labs/FLUX.2-klein-4B", torch_dtype=torch.bfloat16); pipe.enable_model_cpu_offload() でVRAMを節約。
- 生成例: pipe(prompt="A cat holding a sign that says hello world", height=1024, width=1024, guidance_scale=1.0, num_inference_steps=4, generator=torch.Generator(device="cuda").manual_seed(0)).images[0]
- 公式リポジトリ black-forest-labs/flux2 をcloneし、pip install -e . の後、PYTHONPATH=src python scripts/cli.py で対話的に生成・編集できる（環境変数KLEIN_4B_MODEL_PATHを設定しない場合は重みを自動取得）。
- ComfyUIでも利用できる（モデルカードに「ComfyUI and Diffusers で利用可能」との記載）。ComfyUI側の対応状況・必要カスタムノードはインストール環境により異なるため、導入時に確認する。

## 変更履歴

- 2026-11-08: 初回登録
