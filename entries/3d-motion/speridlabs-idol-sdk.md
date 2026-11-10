---
type: "repo"
name: "Idol (image-to-3D Gaussian splat SDK)"
genre: "3d-motion"
url: "https://github.com/speridlabs/idol-sdk"
author: "speridlabs"
repo: "speridlabs/idol-sdk"
license: "Apache-2.0"
stars: 945
language: "Python"
created: "2026-10-28"
updated: "2026-11-09"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/speridlabs/status/2115890658636656826"]
flags: []
risk_notes: "PyPI 未公開・タグ/リリース無しのため clone して pip install -e . で導入する（README の記載どおり）。条件付けに入力エンコーダ2件の HF アクセス承認が必要で、未認証時は EncoderAccessError で停止する。CUDA GPU 必須。直近30日のコミットは 1 件で commit_cadence は stale 扱い。"
forks: 95
open_issues: 4
commits_30d: 5
commit_cadence: "weekly"
size_kb: 6866
archived: false
fetched_at: "2026-11-09T21:31:45Z"
last_release: ""
last_release_at: ""
commits_90d: 5
---

# Idol — 1枚の画像から3Dガウシアンスプラットを生成する推論SDK

## 出来ること

- 1枚の画像（写真・レンダリング画像・生成画像）から3D Gaussian Splattingを生成し、標準的な3DGS .plyとして保存する
- 背景除去（BiRefNet）とオブジェクトの自動フレーミングを内蔵し、画像に写っていない側面も補完する
- ガウシアン数を32,768〜1,048,576で指定可能（デフォルト262,144、32の倍数）
- --mode synthetic（CG・生成画像）/ real（実写写真）でクロップ条件を切り替え
- 画像1枚でもフォルダ一括でも処理でき、各画像につき .ply / 前処理後画像 / 推定カメラcamera.jsonを出力
- Python API（IdolPipeline）とGradioデモ（demo/app.py、Hugging Face Spaceと同一実装）を同梱

## 目的・背景

- 単一画像からの3Dオブジェクト生成を、コンシューマGPU（ピーク7.2GB VRAM）で動く規模に抑えることを狙った推論SDK
- 学習済み重み・推論コード・デモをApache-2.0で公開（Hugging Face: speridlabs/idol、ライセンス表記apache-2.0）
- TripoSplatを土台に、DINOv3 ViT-H+/16とFLUX.2 VAEで画像条件付けし、Euler 50 steps / CFG 3.0 / time shift 3.0でサンプリング
- READMEにTripoSplat・TRELLIS・LGMとの比較ベンチマークとGPU別の実行時間表を掲載

## 依存関係

- Python >= 3.10、PyTorch >= 2.5、torchvision >= 0.20
- transformers >= 4.56、diffusers >= 0.36、huggingface_hub >= 0.34、safetensors >= 0.4
- tensordict >= 0.8、numpy >= 1.26、pillow >= 10.0、plyfile >= 1.0、tqdm >= 4.66
- デモ用extra: gradio==5.49.1、spaces（pip install -e "[demo]"）
- モデル重み: Hugging Faceのsperidlabs/idol（初回利用時に自動ダウンロード、gated=false）
- 条件付け用に facebook/dinov3-vith16plus-pretrain-lvd1689m と black-forest-labs/FLUX.2-dev へのアクセス承認と hf auth login が必須
- 任意: flash-attn（無い場合はPyTorchのscaled_dot_product_attentionにフォールバック、ATTN_BACKENDで切替）

## 実行条件

- CUDA GPUが必要（README実測: RTX 3080 10GBで46.2秒、RTX 4090 24GBで19.1秒、ピークVRAM 7.2GB）
- 初回実行時に重み（合計~3.7-4.4GB）をHugging Faceから取得するため、ネットワークとHF認証が必要
- PyPI未公開・タグ/リリース無しのため、リポジトリをcloneして pip install -e . で導入する
- GPU実行時はtorch.compile等の高速化がデフォルト有効。プロセス内の1枚目のみコンパイルで遅い
- 出力は3DGSビューア（SuperSplat等）で開ける.ply。Apache-2.0のため商用利用可

## 最短手順

- 1. 導入: git clone https://github.com/speridlabs/idol-sdk && cd idol-sdk && pip install -e . （Python 3.10以上 / PyTorch 2.5以上のGPU環境）
- 2. HF認証: DINOv3 ViT-H+ と FLUX.2-dev のアクセス承認後に hf auth login を実行（未認証だと EncoderAccessError で停止する）
- 3. AIからCLIを呼ぶ: python -m idol.sample --image /abs/path/photo.jpg --mode real --num_gaussians 1048576 --out /abs/path/out をサブプロセス実行し、stdoutの <name>: <out>/<name>.ply 行で成功を判定する
- 4. 生成物を受け取る: /abs/path/out/<name>.ply（3DGS）、<name>_input.png（前処理後画像）、<name>_camera.json（推定カメラ）。.plyのパスをそのまま次の処理に渡せる
- 5. フォルダ一括: python -m idol.sample --image /abs/path/renders --mode synthetic --out /abs/path/out
- 6. Python APIから呼ぶ: from idol import IdolPipeline / p = IdolPipeline.from_pretrained("speridlabs/idol") / out = p("photo.jpg", mode="real", seed=42, num_gaussians=1048576) / out.gaussian.save_ply("photo.ply")
- 7. まず試すだけなら https://huggingface.co/spaces/speridlabs/idol （ZeroGPU）で同一モデルをブラウザ実行できる

## 変更履歴

- 2026-11-06: 初回登録
