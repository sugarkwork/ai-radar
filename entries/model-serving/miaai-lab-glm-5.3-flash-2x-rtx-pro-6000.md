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
updated: "2026-11-07"
stars: 23
archived: false
added: 2026-11-08
first_seen: 2026-11-08
source_post: https://x.com/MiaAI_lab/status/2119115546285552046
sources: ["https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold", "https://github.com/ashhart/TensorFold", "https://huggingface.co/api/models/zai-org/GLM-5.3-Flash", "https://x.com/miaai_lab/status/2119115546285552046?a=aZCeYam55LT49ehTNgs&s=46", "https://x.com/MiaAI_lab/status/2119115546285552046", "https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104", "https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold", "https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104", "https://raw.githubusercontent.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold/main/README.md"]
flags: ["unverified"]
risk_notes: "2×96GBのRTX PRO 6000（Blackwell sm_120）が必須。チェックポイント約164GiB、Dockerイメージ約40GiB。TensorFold（ashhart/TensorFold、Zig/CUDA）をDockerでビルドし、GLM-5.3-FlashのEXL3 4bpw量子化を配備する。既定のdrafterはCC BY-NC-ND 4.0（非商用）で、商用はDRAFTER=mtp/noneに切り替える。投稿のKV 973K→1.05M、再起動後約1秒で会話復元、thinking off時の出力短縮、誤ネット設定の自動修正はREADMEと方向性が一致するが数値は自己申告で未検証。当方でビルド・実行は未実施。"
fetched_at: "2026-11-09T21:40:09Z"
forks: 2
open_issues: 1
commits_30d: 16
commits_90d: 16
commit_cadence: "weekly"
size_kb: 2964
amplifiers: []
last_release: ""
last_release_at: ""
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
- 指定の複数GPUと大容量チェックポイントの保存領域が必要。
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

- 2026-11-08: 初回登録（注意点を明記して収録）

## 追加出典・確認範囲（2026-11-09）

TensorFoldをDockerビルドしてGLM-5.3-Flash EXL3 4bpwを2枚のRTX PRO6000へ配備する個人ラボのレシピ。

2×96GB Blackwell、チェックポイント約164GiB、イメージ約40GiB。

既定drafterはCC BY-NC-ND4.0で商用条件が別。KV容量や復元時間は自己申告、未追試。

対象固有の機能・制約の説明は2026-11-07のチェック記録を基にしている。メタ情報は2026-11-09T00:31:15.897796+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

### 今回取得した公式メタ情報

既存フロントマターの過去値は維持し、今回の取得値を下に併記する。どちらも実行・性能の追試ではない。

| 項目 | 値 |
|---|---|
| repo | MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold |
| url | https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold |
| license | Apache-2.0 |
| language | Shell |
| created | 2026-10-31 |
| updated | 2026-11-07 |
| stars | 22 |
| forks | 2 |
| open_issues | 1 |
| commits_30d | 16 |
| commits_90d | 16 |
| commit_cadence | weekly |
| size_kb | 2964 |
| archived | False |
| fetched_at | 2026-11-09T00:31:15.897796+00:00 |


- @MiaAI_lab: https://x.com/MiaAI_lab/status/2119115546285552046
- 対象資料: https://github.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
- 参照: https://github.com/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
- 参照: https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold
- 参照: https://api.github.com/repos/MiaAI-Lab/GLM-5.3-Flash-DGX-Sparks-1104
- 参照: https://raw.githubusercontent.com/MiaAI-Lab/GLM-5.3-Flash-2x-RTX-PRO-6000-TensorFold/main/README.md
- 参照: https://huggingface.co/api/models/zai-org/GLM-5.3-Flash

- 2026-11-09: 関連出典と確認範囲を追記。既存の記述・過去の数値・原文プロンプトは維持。今回の実行確認なし。
