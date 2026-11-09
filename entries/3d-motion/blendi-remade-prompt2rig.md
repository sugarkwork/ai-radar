---
type: "repo"
repo: "blendi-remade/prompt2rig"
name: "prompt2rig — プロンプトから3Dキャラクター動作を生成"
genre: "3d-motion"
url: "https://github.com/blendi-remade/prompt2rig"
author: "blendi-remade"
license: "Apache-2.0"
language: "JavaScript"
stars: 534
forks: 79
open_issues: 0
created: "2026-10-19"
updated: "2026-10-21"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 9255
archived: false
risk_notes: "コードはApache-2.0だが、HQパスの依存関係が商用を制限。GVHMR=教育・研究・非営利のみ。SMPL-X=非商用（商用はMeshcapadeから別途）。WiLoR=CC-BY-NC-ND。MANO=非商用。Ultralytics YOLO=AGPL-3.0（コピーレフト、エンタープライズライセンス別途）。MediaPipe・three.jsは商用可。Webアプリ・ライブプレビュー・動画生成は商用可能。HQパスを商用で使うには依存関係の置き換えまたは別途ライセンスが必要。動画モデル（FLUX 3 Max/H3 Max Turbo）はfalおよびモデル提供元の条件に従う。当方未実行。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/cutetoxicguy/status/2119595833691897981", "https://github.com/blendi-remade/prompt2rig", "https://github.com/blendi-remade/prompt2rig/blob/main/README.md", "https://github.com/blendi-remade/prompt2rig/blob/main/LICENSE"]
added: "2026-11-09"
first_seen: "2026-11-09"
source_post: "https://x.com/cutetoxicguy/status/2119595833691897981"
fetched_at: "2026-11-09T03:14:33+00:00"
flags: ["unverified"]
---

# prompt2rig — プロンプトから3Dキャラクター動作を生成

## 出来ること

テキストで動作を指定→動画モデルが演技→GPUで3Dボディ/指の動作を推定→Mixamo互換リグのキャラクターで再生→Blender/UnityへGLB出力。MediaPipeでブラウザ即時プレビュー、GVHMRでHQボディ、WiLoRで指。

## 目的・背景

手作りアニメーションやモーキャプ前に、プロンプトで素早くアクションをキャラクターに試させる。単一カメラ・プレーン背景・全身が見える設定が前提。

## 依存関係

FLUX 3 Max / H3 Max Turbo（falで動画生成）、MediaPipe Pose（ブラウザ即時プレビュー）、GVHMR→SMPL回転→Mixamo（HQボディ、RTX 4090で~3.5-4s/5sクリップ）、WiLoR（指、+~0.3s、MediaPipeフォールバックあり）。

## 実行条件

Node 18+、fal API key。HQパス: Windows、NVIDIA GPU、uv、FFmpeg（PATH通し）、~5GBチェックポイント。SMPL-X v1.1 NPZ（無料登録要）をhq/body_models/smplx/へ。WiLoR要MANO（無料登録要）。

## 最短手順

git clone→cp .env.example .env（FAL_KEY設定）→node server.mjs。HQ: hq/setup.ps1でvenv・CUDA PyTorch・GVHMR+チェックポイント。WiLoR: hq/setup_hands.pyでMANO展開。hq/worker.py起動。

## 注意点

コードはApache-2.0だが、HQパスの依存関係が商用を制限。GVHMR=教育・研究・非営利のみ。SMPL-X=非商用（商用はMeshcapadeから別途）。WiLoR=CC-BY-NC-ND。MANO=非商用。Ultralytics YOLO=AGPL-3.0（コピーレフト、エンタープライズライセンス別途）。MediaPipe・three.jsは商用可。Webアプリ・ライブプレビュー・動画生成は商用可能。HQパスを商用で使うには依存関係の置き換えまたは別途ライセンスが必要。動画モデル（FLUX 3 Max/H3 Max Turbo）はfalおよびモデル提供元の条件に従う。当方未実行。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
