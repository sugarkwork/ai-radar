---
type: "model"
name: "facebook/sam3.1"
genre: "image-gen"
url: "https://huggingface.co/facebook/sam3.1"
author: "facebook"
source_post: "https://x.com/L_ARCH_01/status/2119383964167409667"
sources: ["https://x.com/L_ARCH_01/status/2119383964167409667?a=zKpg53m3GHtXbyQgu6M&s=20", "https://x.com/L_ARCH_01/status/2119383964167409667", "https://github.com/facebookresearch/sam3", "https://github.com/facebookresearch/sam-3d-body", "https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE", "https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE", "https://huggingface.co/facebook/sam3.1", "https://huggingface.co/facebook/sam-3d-body-dinov3"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "独自SAM Licenseは商用を一律禁止していないが再配布・法令・プライバシー等に条件。実機の対象分離精度・追跡性能は未試験。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "facebook/sam3.1"
license: "other"
base_model: []
downloads: 187407
likes: 1433
format: "pytorch"
size: "配布中の重みファイル 1本・合計3,502,755,717 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-03-26"
updated: "2026-03-27"
fetched_at: "2026-11-09T00:31:36.868055+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: true
license_name: "unknown"
---

# facebook/sam3.1

## 出来ること

SAM3.1の配布重み。複数人モーション制作例では対象を分離する前段として紹介される。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:36.868055+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式APIのメタ情報は取得できたがREADME/モデルカードの取得はHTTP 401で失敗。本文の現行内容は未確認。取得制限やファイル未掲載を、対象そのものの不存在とは扱わない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:36.868055+00:00）。重み 1本。

- `sam3.1_multiplex.pt` — 3,502,755,717 bytes

[ファイル一覧](https://huggingface.co/facebook/sam3.1/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

facebookresearch/sam3の対応コードと配布条件への同意・手動承認が必要というHF確認記録。

独自SAM Licenseは商用を一律禁止していないが再配布・法令・プライバシー等に条件。実機の対象分離精度・追跡性能は未試験。

## 使い方

[公式モデルカード](https://huggingface.co/facebook/sam3.1)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @L_ARCH_01: https://x.com/L_ARCH_01/status/2119383964167409667
- 対象資料: https://huggingface.co/facebook/sam3.1
- 参照: https://github.com/facebookresearch/sam3
- 参照: https://github.com/facebookresearch/sam-3d-body
- 参照: https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE
- 参照: https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE
- 参照: https://huggingface.co/facebook/sam-3d-body-dinov3

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
