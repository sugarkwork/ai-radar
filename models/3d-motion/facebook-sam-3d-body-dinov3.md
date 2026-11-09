---
type: "model"
name: "facebook/sam-3d-body-dinov3"
genre: "3d-motion"
url: "https://huggingface.co/facebook/sam-3d-body-dinov3"
author: "facebook"
source_post: "https://x.com/L_ARCH_01/status/2119383964167409667"
sources: ["https://x.com/L_ARCH_01/status/2119383964167409667?a=zKpg53m3GHtXbyQgu6M&s=20", "https://x.com/L_ARCH_01/status/2119383964167409667", "https://github.com/facebookresearch/sam3", "https://github.com/facebookresearch/sam-3d-body", "https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE", "https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE", "https://huggingface.co/facebook/sam3.1", "https://huggingface.co/facebook/sam-3d-body-dinov3"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "独自SAM Licenseの条件と人物の権利を確認する。SAM3.1の分割モデルとは別であり、映像全体のモーション品質は単独重みの保証ではない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "facebook/sam-3d-body-dinov3"
license: "other"
base_model: []
downloads: 12671
likes: 865
format: "pytorch"
size: "配布中の重みファイル 1本・合計696,110,248 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2025-11-17"
updated: "2025-12-10"
fetched_at: "2026-11-09T00:31:37.070024+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: true
license_name: "sam-license"
---

# facebook/sam-3d-body-dinov3

## 出来ること

SAM3D BodyのDINOv3系重み。単画像の体・足・手を含む人体メッシュ推定に用いる。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:37.070024+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式APIのメタ情報は取得できたがREADME/モデルカードの取得はHTTP 401で失敗。本文の現行内容は未確認。取得制限やファイル未掲載を、対象そのものの不存在とは扱わない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:37.070024+00:00）。重み 1本。

- `assets/mhr_model.pt` — 696,110,248 bytes

[ファイル一覧](https://huggingface.co/facebook/sam-3d-body-dinov3/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

facebookresearch/sam-3d-bodyとMHR等の構成が必要。HFはmanual gateで承認が必要。

独自SAM Licenseの条件と人物の権利を確認する。SAM3.1の分割モデルとは別であり、映像全体のモーション品質は単独重みの保証ではない。

## 使い方

[公式モデルカード](https://huggingface.co/facebook/sam-3d-body-dinov3)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @L_ARCH_01: https://x.com/L_ARCH_01/status/2119383964167409667
- 対象資料: https://huggingface.co/facebook/sam-3d-body-dinov3
- 参照: https://github.com/facebookresearch/sam3
- 参照: https://github.com/facebookresearch/sam-3d-body
- 参照: https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE
- 参照: https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE
- 参照: https://huggingface.co/facebook/sam3.1

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
