---
type: repo
repo: MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
name: GLM-5.3-Flash DGX Spark 2台 配備レシピ
genre: model-serving
url: https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
author: MiaAI-Lab
license: Apache-2.0
language: Docker / Shell
created: 2026-11-04
updated: 2026-11-07
stars: 89
archived: false
added: 2026-11-08
first_seen: 2026-11-08
source_post: https://x.com/MiaAI_lab/status/2119115546285552046
sources: ["https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104", "https://huggingface.co/api/models/zai-org/GLM-5.3-Flash"]
flags: ["unverified"]
risk_notes: "DGX Spark 2台（計128GB統一メモリ級）が必須で、RTX A4000 16GB×2・RAM 96GBの環境では実行できない。チェックポイント約164GiB、イメージ約40GiB。既定drafterはCC BY-NC-ND 4.0（非商用）で、商用はDRAFTER=mtp/none。投稿のKV拡張・再起動復元・thinking off短縮は自己申告で未検証。当方でビルド・実行は未実施。"
fetched_at: "2026-11-08T06:40:00Z"
---

# GLM-5.3-Flash DGX Spark 2台 配備レシピ

## 出来ること

- GLM-5.3-Flash（`zai-org/GLM-5.3-Flash`、MIT）を、DGX Spark 2台で動かすための配備レシピ。
- Docker ベースで、量子化済みチェックポイントの取得・起動・KVキャッシュ設定をまとめる。
- 投稿では KV 973K → 1.05M、会話のディスク保存と再起動後約1秒の復元、thinking off 時の出力短縮、誤ネット設定の自動修正を主張。

## 目的・背景

- 2台のDGX Sparkを1つの推論環境として使うための個人ラボのレシピ。2026-11-04 作成、2026-11-07 更新、89 stars。RTX PRO 6000 版（20 stars）と対になる構成。
- 投稿は更新告知で、数値はREADMEと方向性が一致するが独立検証はない。

## 依存関係

- DGX Spark 2台、Docker、NVIDIA Container Toolkit。
- GLM-5.3-Flash のチェックポイント（約164GiB）と配布イメージ（約40GiB）。

## 実行条件

- **DGX Spark 2台**が必須。RTX A4000 16GB×2 / RAM 96GB では実行不可。
- 既定の drafter は **CC BY-NC-ND 4.0（非商用）**。商用は `DRAFTER=mtp` または `DRAFTER=none`。
- 当方でビルド・推論は未実施。実機のメモリ・ネットワーク設定を確認してから使う。

## 最短手順

```bash
git clone https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
cd GLM-5.3-Flash-DGX-Sparks-1104
# README の手順でチェックポイントを取得し、2台構成のネットワークを設定
DRAFTER=mtp docker compose up
```

## 変更履歴

- 2026-11-08: 初回登録（実行環境が合わないため「保留」だったものを、配備情報として収録）
