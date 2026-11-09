---
type: "model"
name: "UntMods/FaceSwap_MiniMaxH3_REF2VA"
genre: "video-gen"
url: "https://huggingface.co/UntMods/FaceSwap_MiniMaxH3_REF2VA"
author: "UntMods"
source_post: "https://x.com/PhotogenicWeekE/status/2119181133833449858"
sources: ["https://x.com/photogenicweeke/status/2119181133833449858?a=w4aGawemQW6rPSr011A&s=46", "https://x.com/PhotogenicWeekE/status/2119181133833449858", "https://huggingface.co/UntMods/FaceSwap_MiniMaxH3_REF2VA", "https://huggingface.co/api/models/UntMods/FaceSwap_MiniMaxH3_REF2VA", "https://civitai.com/api/v1/models/2940916", "https://github.com/PGCRT/CRT-Nodes"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "HFカードのApache表記は基底H3の独自条件まで解除しない。顔が大きくなる等の作例上の欠点、肖像権・同意・誤認防止に注意。品質は未検証。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "UntMods/FaceSwap_MiniMaxH3_REF2VA"
license: "apache-2.0"
base_model: []
downloads: 0
likes: 215
format: "safetensors"
size: "配布中の重みファイル 1本・合計65,623,904 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-09-15"
updated: "2026-09-20"
fetched_at: "2026-11-09T00:31:27.634775+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# UntMods/FaceSwap_MiniMaxH3_REF2VA

## 出来ること

MiniMax H3 Ref2VA向け顔交換LoRA。triggerはFaceswap、強度1を作者が推奨し、JSON/zipワークフローを同梱。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:27.634775+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:27.634775+00:00）。重み 1本。

- `SS_FaceSwap_MiniMax_H3_REF2VA.safetensors` — 65,623,904 bytes

[ファイル一覧](https://huggingface.co/UntMods/FaceSwap_MiniMaxH3_REF2VA/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

約65.6MBの重み。基底H3モデルとComfyUI等が必要。P-H3編集で利用した第三者の作例も紹介される。

HFカードのApache表記は基底H3の独自条件まで解除しない。顔が大きくなる等の作例上の欠点、肖像権・同意・誤認防止に注意。品質は未検証。

## 使い方

[公式モデルカード](https://huggingface.co/UntMods/FaceSwap_MiniMaxH3_REF2VA)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @PhotogenicWeekE: https://x.com/PhotogenicWeekE/status/2119181133833449858
- 対象資料: https://huggingface.co/UntMods/FaceSwap_MiniMaxH3_REF2VA
- 参照: https://huggingface.co/api/models/UntMods/FaceSwap_MiniMaxH3_REF2VA
- 参照: https://civitai.com/api/v1/models/2940916
- 参照: https://github.com/PGCRT/CRT-Nodes

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
