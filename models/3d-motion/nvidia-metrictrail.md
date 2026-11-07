---
type: "model"
name: "MetricTrail 1.0 (DINO-DPVO チェックポイント)"
genre: "3d-motion"
url: "https://huggingface.co/nvidia/MetricTrail"
author: "NVIDIA"
pricing: "free"
pricing_detail: "重みは無償公開だが、実体のライセンスは NVIDIA OneWay Noncommercial License（研究・評価目的の非商用のみ）。DPVO 由来部分は MIT、NVIDIA が権利を持つソースは Apache-2.0、DINOv3 は DINOv3 License"
signup_required: false
model: "nvidia/MetricTrail"
license: "other"
downloads: 168
likes: 20
format: "pytorch"
size: "13.1 MB (dino_dpvo.pth 1 ファイル、13,739,570 bytes)"
base_model: []
created: "2026-11-05"
updated: "2026-11-05"
added: "2026-11-07"
first_seen: "2026-11-06"
sources: ["https://x.com/HuggingPapers/status/2118268282495012971", "https://huggingface.co/nvidia/MetricTrail", "https://x.com/tokufxug/status/2118163149983781219"]
flags: []
risk_notes: "重みのライセンスは非商用 (NVIDIA OneWay Noncommercial License) で、コード (Apache-2.0 / DPVO 由来 MIT) とは条件が別。モデルカードはチェックポイントを別途 HF で公開予定と書くが、実際には dino_dpvo.pth が同リポジトリに含まれる（記載が古い）。推論コードは HF リポジトリに含まれず、記載のソースリビジョンに対応する公開リポジトリも特定できなかった (NVlabs 配下は 404)。DPVO の CUDA 拡張をソースビルドする必要があり CUDA 必須、動作確認は A100 のみ。"
fetched_at: "2026-11-07T10:19:15Z"
license_name: "nvidia-open-model-license"
source_post: "https://x.com/tokufxug/status/2118163149983781219"
---

# MetricTrail — 長い RGB 動画からカメラ軌跡とメートル深度を推定する視覚オドメトリ

## 出来ること

- 時系列 RGB 画像列からカメラ軌跡 (c2w / w2c, [N,4,4]) とフレーム毎のメートル深度を推定する。視覚オドメトリ (VO) と 3D 再構成の研究向け。
- 単眼（内部パラメータは供給値、または RGB からの推定）と較正済みステレオの計 3 通りで動く。RGB のみの場合は先頭フレーム区間から共有カメラモデルを推定し、以後固定する。
- 出力は軌跡 NPZ (c2w / w2c / intrinsics / frame_ids) と、フレーム毎深度 depth.f32・有効マスク mask.u8 のキャッシュ。密な点群・メッシュは書き出さない（評価側の別ワークフロー）。
- 任意のループ補正 (metrictrail.lc_cli) を CPU で後段実行できる。候補ペアは外部で生成して渡す方式で、自身は place retrieval を行わない。新ポストプロセッサはベンチマーク未検証と明記されている。
- 論文ではなくモデルカード＋評価表の形。KITTI Odometry の ATE は 14.05 m（内部パラメータを RGB から推定・LC なし）／9.78 m（LC あり）／7.39 m（内部パラメータ供給＋LC）／3.00 m（較正ステレオ＋LC）、TUM RGB-D は 8.4 cm（局所のみ）〜3.7 cm（グローバル BA＋refinement）。

## 目的・背景

- NVIDIA による研究用リリース（MetricTrail 1.0、Hugging Face に 2026-11-05 公開、downloads 168 / likes 20）。
- 構成は DPVO の sparse patch 対応ネットワーク＋学習済み residual adapter＋凍結 DINOv3-S/16＋凍結 MoGe-2（メートル深度）。MoGe-2 の深度予測を patch 深度の初期値かつ soft constraint として使い、多視点拘束で上書きしうる設計。
- 学習は TartanAir / TartanGround / CarlaOcc / LightwheelOcc / OmniWorld-Game の合成・ゲーム映像 240,000 クリップ（15 フレーム／クリップ）。A100 80GB ×16 で約 7 時間、DINOv3 は凍結、MoGe-2 は学習に使わない。
- 公開チェックポイントは 3,425,860 パラメータ（100 本の FP32 テンソル）の DINO-DPVO 部分のみ。DINOv3 本体・MoGe-2・（任意の）SALAD / RoMa は別途入手する。

## 収録ファイル

- dino_dpvo.pth — 13,739,570 bytes（約 13.1 MB）。SHA256 は d0aa57e165b159fc84bdb9d94918ad9b508c153acfb4c46f5058ab80421fb5f5 で、モデルカード記載値および HF 側のファイル etag と一致（2026-11-07 実測）。
- config.json — {"model_name": "MetricTrail", "checkpoint_file": "dino_dpvo.pth"} のみ。
- README.md / .gitattributes。推論コードは含まれない（4 ファイルのみ、usedStorage 13,739,570 bytes）。
- 別途必要な外部重み: DINOv3-S/16（dinov3_vits16_pretrain_lvd1689m-08c60483.pth、SHA256 08c60483…941d）、MoGe-2 ViT-L（Ruicheng/moge-2-vitl）。

## 実行条件

- ライセンス: 重みは NVIDIA OneWay Noncommercial License（研究・評価目的の非商用のみ）。カードは license: other / license_name: nvidia-open-model-license。DPVO 由来部分は MIT、NVIDIA が権利を持つソースは Apache-2.0、DINOv3 は DINOv3 License と、重み・コード・上流部品で条件が分かれる。gated ではなく同意なしで取得できる。
- 実行環境: Linux x86_64、Python 3.10 / PyTorch 2.5.1 / CUDA 12.4、xformers、OpenCV、SciPy。DPVO の CUDA 拡張（cuda_corr / cuda_ba / lietorch_backends）をソースからビルドする必要があり、nvcc と Eigen 3.4.0 が要る。CUDA 必須で、動作確認済みは A100（Ampere）のみ。
- 速度（KITTI-02、A100）: 12.70 FPS、ピーク 3.21 GB（内部パラメータ供給）／6.81 GB（RGB のみ、初回出力まで約 175 秒）。内部パラメータ供給時の初回出力は約 0.7 秒（いずれも配布元の自己申告値）。
- 既知の制約: 深度プロバイダ精度への依存、低視差・高速回転・ローリングシャッター・モーションブラーで対応付けが劣化、共有カメラモデルへの敏感さ。動的シーン（TUM-Dynamic）は主要手法に劣ると明記。

## 使い方

- 重みを取得し ckpt/dino_dpvo_multidataset15k.pth に置くか paths.dino_dpvo_checkpoint で指定する。DINOv3 と MoGe-2 も別途用意する。
- DPVO の CUDA 拡張（cuda_corr / cuda_ba / lietorch_backends）をビルドする。
- PYTHONNOUSERSITE=1 python -m metrictrail.cli --config <config.json> を実行（既定 device は cuda:0）。--preflight で外部ファイルと import を点検し、--stop-after {calibration,local} で段階実行できる。
- 出力は output_root/local/inference/（KITTI）または .../predictions/ 配下の軌跡 NPZ と完了記録。失敗ランはキャッシュや古い出力を残すため、完了記録で成功を判定する。
- ループ補正は別コマンド: python -m metrictrail.lc_cli --config <config.json> --case <case> --candidate-file <candidates.json> --candidate-sha256 <sha256>。

## 変更履歴

- 2026-11-07: 初回登録
