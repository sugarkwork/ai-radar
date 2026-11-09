---
type: "model"
name: "BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI"
genre: "video-gen"
url: "https://huggingface.co/BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI"
author: "BennyDaBall"
source_post: "https://x.com/BennyDaBall_OG/status/2119203032973901970"
sources: ["https://x.com/BennyDaBall_OG/status/2119203032973901970", "https://huggingface.co/BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "重みはMiniMax H3 Community License。RTX5090・1344×768・124frames・6step46.1秒/疎注意38秒等は作者測定で他GPUの保証ではない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI"
license: "other"
base_model: ["VideoRebirthAI/hyperflow-h3-flash"]
downloads: 387
likes: 12
format: "safetensors"
size: "配布中の重みファイル 2本・合計32,218,881,072 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-08"
fetched_at: "2026-11-09T00:31:31.342030+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "minimax-h3-community-license-agreement"
---

# BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI

## 出来ること

HyperFlow H3 FlashをComfyUIで使うための非公式INT8変換重み。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:31.342030+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:31.342030+00:00）。重み 2本。

- `minimax_h3_fl2va_hyperflow_flash_int8_convrot.safetensors` — 15,894,225,896 bytes
- `minimax_h3_ref2va_hyperflow_flash_int8_convrot.safetensors` — 16,324,655,176 bytes

[ファイル一覧](https://huggingface.co/BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

fl2va約15.89GB/ref2va約16.32GB、専用INT8ノードとTE/VAE等を取得する。baseはVideoRebirthAI/hyperflow-h3-flash。

重みはMiniMax H3 Community License。RTX5090・1344×768・124frames・6step46.1秒/疎注意38秒等は作者測定で他GPUの保証ではない。

## 使い方

[公式モデルカード](https://huggingface.co/BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @BennyDaBall_OG: https://x.com/BennyDaBall_OG/status/2119203032973901970
- 対象資料: https://huggingface.co/BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
