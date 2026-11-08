---
type: repo
repo: MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
name: GLM-5.3-Flash 2×RTX PRO 6000 配備レシピ（TensorFold）
genre: model-serving
url: https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
author: MiaAI-Lab
license: Apache-2.0
language: Docker / Zig / CUDA
created: 2026-10-31
updated: 2026-11-07
stars: 20
archived: false
added: 2026-11-08
first_seen: 2026-11-08
source_post: https://x.com/MiaAI_lab/status/2119115546285552046
sources: ["https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold", "https://github.com/ashhart/TensorFold", "https://huggingface.co/api/models/zai-org/GLM-5.3-Flash"]
flags: ["unverified"]
risk_notes: "2×96GBのRTX PRO 6000（Blackwell sm_120）が必須で、RTX A4000 16GB×2・RAM 96GBの環境では実行できない。チェックポイント約164GiB、Dockerイメージ約40GiB。TensorFold（ashhart/TensorFold、Zig/CUDA）をDockerでビルドし、GLM-5.3-FlashのEXL3 4bpw量子化を配備する。既定のdrafterはCC BY-NC-ND 4.0（非商用）で、商用はDRAFTER=mtp/noneに切り替える。投稿のKV 973K→1.05M、再起動後約1秒で会話復元、thinking off時の出力短縮、誤ネット設定の自動修正はREADMEと方向性が一致するが数値は自己申告で未検証。当方でビルド・実行は未実施。"
fetched_at: "2026-11-08T06:40:00Z"
---

# GLM-5.3-Flash 2×RTX PRO 6000 配備レシピ（TensorFold）

## 出来ること

- GLM-5.3-Flash（基底モデル `zai-org/GLM-5.3-Flash`、MIT）を、2枚の RTX PRO 6000（96GB×2、Blackwell sm_120）で動かすための配備レシピ。
- TensorFold（`ashhart/TensorFold`、Zig/CUDA）を Docker でビルドし、EXL3 4bpw 量子化で配備する。
- KV キャッシュを 973K → 1.05M トークンに拡張、会話をディスクに保存して再起動後約1秒で復元、thinking off 時の出力短縮、誤ったネットワーク設定の自動修正、という改善を主張。

## 目的・背景

- 大規模 MoE を 2枚のワークステーションGPUに載せるための、量子化・配備・起動設定のレシピ集。個人ラボ（MiaAI-Lab）による公開リポジトリで、2026-10-31 作成、2026-11-07 更新、20 stars。
- 投稿は「RTX PRO 6000 の番だ」として更新内容を告知するもの。数値は README と方向性が一致するが、独立検証はない。

## 依存関係

- Docker、NVIDIA Container Toolkit、CUDA（sm_120 / Blackwell）。
- TensorFold（Zig/CUDA）をイメージ内でビルド。
- GLM-5.3-Flash のチェックポイント（約164GiB）と、配布イメージ（約40GiB）。

## 実行条件

- **2×RTX PRO 6000 96GB（合計192GB VRAM）**、または同等のBlackwell環境が必須。DGX Spark 2台向けの別レシピもある。
- 既定の drafter は **CC BY-NC-ND 4.0（非商用）**。商用利用は `DRAFTER=mtp` または `DRAFTER=none` に変更する。
- **RTX A4000 16GB×2 / RAM 96GB では実行不可**（VRAM・チェックポイントサイズが足りない）。
- 当方でビルド・推論は未実施。README の手順と数値をそのまま信じず、実機で確認する。

## 最短手順

```bash
git clone https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
cd GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
# README の Docker ビルド手順に従う（TensorFold をイメージ内でビルド）
# チェックポイントを取得し、DRAFTER を用途に合わせて指定
DRAFTER=mtp docker compose up   # 商用可の例。非商用なら既定の drafter でも可
```

## 変更履歴

- 2026-11-08: 初回登録（実行環境が合わないため「保留」だったものを、配備情報として収録）
