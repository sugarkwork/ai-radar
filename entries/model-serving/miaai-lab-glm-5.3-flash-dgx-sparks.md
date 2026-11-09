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
sources: ["https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104", "https://huggingface.co/api/models/zai-org/GLM-5.3-Flash", "https://x.com/miaai_lab/status/2119115546285552046?a=aZCeYam55LT49ehTNgs&s=46", "https://x.com/MiaAI_lab/status/2119115546285552046", "https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold", "https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold", "https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104", "https://raw.githubusercontent.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold/main/README.md"]
flags: ["unverified"]
risk_notes: "DGX Spark 2台（計128GB統一メモリ級）が必須。チェックポイント約164GiB、イメージ約40GiB。既定drafterはCC BY-NC-ND 4.0（非商用）で、商用はDRAFTER=mtp/none。投稿のKV拡張・再起動復元・thinking off短縮は自己申告で未検証。当方でビルド・実行は未実施。"
fetched_at: "2026-11-08T06:40:00Z"
forks: 17
open_issues: 20
commits_30d: 43
commits_90d: 43
commit_cadence: "daily"
size_kb: 6561
amplifiers: []
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

- **DGX Spark 2台**が必須。
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

- 2026-11-08: 初回登録（注意点を明記して収録）

## 追加出典・確認範囲（2026-11-09）

GLM-5.3-FlashをDGX Spark2台へ配備するTensorFoldの個人ラボレシピ。

モデル約164GiBとDocker環境。コードApache-2.0とモデル・drafterの利用条件を分ける。

既定drafterは非商用。商用はDRAFTER=mtp/none等の条件確認が必要。短縮・復元の数値は自己申告。

対象固有の機能・制約の説明は2026-11-07のチェック記録を基にしている。メタ情報は2026-11-09T00:31:15.927314+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104 |
| url | https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104 |
| license | Apache-2.0 |
| language | Shell |
| created | 2026-11-04 |
| updated | 2026-11-08 |
| stars | 93 |
| forks | 17 |
| open_issues | 20 |
| commits_30d | 43 |
| commits_90d | 43 |
| commit_cadence | daily |
| size_kb | 6561 |
| archived | False |
| fetched_at | 2026-11-09T00:31:15.927314+00:00 |


- @MiaAI_lab: https://x.com/MiaAI_lab/status/2119115546285552046
- 対象資料: https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
- 参照: https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
- 参照: https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
- 参照: https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
- 参照: https://raw.githubusercontent.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold/main/README.md
- 参照: https://huggingface.co/api/models/zai-org/GLM-5.3-Flash

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
