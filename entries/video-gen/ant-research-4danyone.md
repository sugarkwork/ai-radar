---
type: "repo"
name: "4DAnyone"
genre: "video-gen"
url: "https://github.com/ant-research/4DAnyone"
author: "ant-research (Ant Group)"
repo: "ant-research/4DAnyone"
license: "Apache-2.0"
stars: 1485
language: "Python"
created: "2026-08-10"
updated: "2026-10-14"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/tokufxug/status/2118171681437175920"]
flags: []
risk_notes: "発見源の投稿は4DGS圧縮・配信ツール「Faltwerk」の宣伝で、本リポジトリへの言及はない（t.co も投稿動画に戻る）。そのため本項目の数値・説明はGitHub APIとREADMEのみに依拠している。SMPL-X本体は別ライセンスで、無料アカウント登録とライセンス同意が必須。研究コードであり、MCPサーバや常駐APIは無く、利用はCLIかローカルGUIに限る。"
forks: 106
open_issues: 6
commits_30d: 1
commit_cadence: "monthly"
size_kb: 84270
archived: false
fetched_at: "2026-11-07T10:55:36Z"
last_release: ""
last_release_at: ""
---

# 4DAnyone — 単眼の人物動画から多視点4D動画を作る推論CLI

## 出来ること

- 人物が1人写った普通のモノキュラ動画から、同期した多視点動画を生成する。入力にカメラパラメータは不要で、固定カメラも要求しない。
- 視点数・ピッチ層・ヨー範囲を引数で指定できる（例: 6視点の一周、24視点、16視点×3層=48視点、正面180度の12視点×2層）。
- 出力は4DGS再構成に渡せる構成で、<clip>/cameras.json（各視点の内部・外部パラメータ）、skeletons/00..N-1.mp4（ポーズ条件）、videos/00..N-1.mp4（生成視点）、gvhmr/motion.json と motion.safetensors（再利用可能なモーション）、metadata.json（設定・所要時間・リソース）が揃う。
- 4DAnyone-Turbo（4ステップ蒸留）が既定で有効。README記載の実測では121フレームの動画をRTX 4090 1枚で平均27秒、CUDAメモリのピークは22GB。
- Gradio + Rerun ベースのGUI（app.py）で、推論の実行と結果の可視化ができる。
- 3DGS再構成の手順は docs/nerfstudio.md に、推論性能の比較は docs/inference_performance.md に付属する。

## 目的・背景

- SIGGRAPH Asia 2026 採択論文「4DAnyone: Create Anyone in 4D from a Casual Monocular Video」（arXiv:2608.20335）の公式実装。著者らは Yudong Jin ほか、Ant Group の ant-research 名義で公開されている。
- 狙いは、誰でも撮れる1本の動画から自由視点の4D人物素材を作り、下流の4DGS再構成につなぐこと。2026-08-10 公開、2026-11-07 時点で stars 1485 / forks 106。
- 更新は 2026-09 に集中しており、GUI公開（9/16）、24GB未満へのメモリ削減（9/5）、Turbo による5.58倍の高速化（9/2）、32GB未満化（8/28）がREADMEのNewsに記録されている。直近30日のコミットは1件（2026-10-14、Windowsの出力ロック修正）。

## 依存関係

- Python 3.11（conda 環境を README が想定）。
- requirements.txt: torch 2.8〜2.9 / torchvision 0.23 / transformers 5.17 / pytorch-lightning 2.3 / ultralytics 8.3.253 / smplx 0.1.28 / hydra-core / kornia / opencv-python / safetensors / huggingface-hub など。
- git submodule third_party/GVHMR（姿勢・モーション復元に使用。git submodule update --init が必要）。
- SMPL-X のニュートラル体モデル（SMPLX_NEUTRAL.npz）。本体は別ライセンスで、公式サイトの無料アカウント登録とライセンス同意が要る。scripts/download_smplx.py が対話式ダウンロードと --archive_path 指定のオフライン導入の両方を提供する。
- モデル重みとサンプル動画は初回利用時に自動ダウンロードされる（手動なら scripts/download_model.py / scripts/download_example.py）。
- GUI を使う場合のみ requirements-gui.txt（Gradio + Rerun）。任意で FlashAttention-3 または SageAttention を入れると高速化される（無くても SDPA で動く）。

## 実行条件

- CUDA GPU が必須。README記載のピークは約22GBで、RTX 4090 クラスの consumer GPU を想定。Turbo無効時や視点数が多い場合は余裕が要る。
- 入力動画の条件: 人物1人、全身または上半身、大きなカメラ移動なし、1080p以上、9:16の縦長、121フレーム以上。
- SMPL-X のアカウント（無料）とライセンス同意が事前に必要。ここが最初の関門で、同意なしでは推論が開始できない。
- 初回はモデルとサンプルのダウンロードが走るため、ネットワーク接続と相応の空きディスクが必要。
- ディストリビューションは研究コードで、常駐APIやMCPサーバは提供されない。呼び出しはCLI（inference.py）かローカルGUI（127.0.0.1:7860）。

## 最短手順

- git clone https://github.com/ant-research/4DAnyone.git && cd 4DAnyone && git submodule update --init third_party/GVHMR
- conda create -n 4danyone python=3.11 -y && conda activate 4danyone && pip install -r requirements.txt
- SMPL-X を導入する。非対話で済ませるなら公式サイトで取得した models_smplx_v1_1.zip を渡す: python scripts/download_smplx.py --archive_path /path/to/models_smplx_v1_1.zip
- （任意）python scripts/download_model.py && python scripts/download_example.py で重みとサンプルを先に取得しておくと、初回推論が止まりにくい。
- エージェントからはCLIをそのまま叩く: python inference.py --video_path data/source/pexels/2785536-uhd_2160_3840_25fps.mp4 --output_dir data/fdanyone/sample --views_per_layer 24 。視点構成は --views_per_layer / --layer_pitches / --start_yaw / --yaw_span で調整し、全オプションは python inference.py --help で確認できる。
- 成功判定は出力ディレクトリの videos/00.mp4〜<N-1>.mp4 と metadata.json の生成。所要時間・使用メモリは metadata.json に記録されるので、そこを読めば成否と性能を機械的に確認できる。
- 見た目を確認したいときだけ GUI: pip install -r requirements-gui.txt && python app.py --output_dir data/fdanyone/sample --server_port 7860 （http://127.0.0.1:7860）。

## 変更履歴

- 2026-11-07: 初回登録
