---
type: "model"
name: "akatz-ai/MiniMax-H3-Character-Swap-LoRA"
genre: "video-gen"
url: "https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA"
author: "akatz-ai"
source_post: "https://x.com/Phantom_202601/status/2118812967517208975"
sources: ["https://x.com/phantom_202601/status/2118812967517208975?a=NX4nndbLF-nwoJsmUwo&s=46", "https://x.com/Phantom_202601/status/2118812967517208975", "https://make-profit.net/2026/11/06/genai-lab-54-blender-mixamo-h3-soft-body-mannequin-three-angles-regenerated/", "https://x.com/OJI3_NIKKE/status/2118372636707455412", "https://api.github.com/repos/toyxyz/toyxyz_RGBMocap", "https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/README.md", "https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/LICENSE", "https://huggingface.co/api/models/akatz-ai/MiniMax-H3-Character-Swap-LoRA", "https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/raw/main/README.md", "https://api.github.com/repos/akatz-ai/h3-relay", "https://x.com/Phantom_202601/status/2119191066033508440", "https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "LoRA単体では動かない。重みはMiniMax H3 Community Licenseでコードのライセンスと別。人物・作品の許諾と生成の誤認防止が必要。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "akatz-ai/MiniMax-H3-Character-Swap-LoRA"
license: "other"
base_model: ["Comfy-Org/MiniMax-H3"]
downloads: 143514
likes: 750
format: "safetensors"
size: "配布中の重みファイル 2本・合計310,221,112 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-09-25"
updated: "2026-10-17"
fetched_at: "2026-11-09T00:30:32.350003+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "minimax-h3-community-license-agreement"
---

# akatz-ai/MiniMax-H3-Character-Swap-LoRA

## 出来ること

参照動画の人物を別キャラクターに置換するMiniMax H3用LoRA。v1/v1.5を配布しv1.5・強度1を推奨。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:32.350003+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:32.350003+00:00）。重み 2本。

- `h3_character_swap_pro4500_1000.safetensors` — 155,110,320 bytes
- `h3_character_swap_v1.5.safetensors` — 155,110,792 bytes

[ファイル一覧](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

Ref2VA INT8本体、Turbo 8step LoRA、H3 Relay 2.0、参照画像・動画とSAMマスク等のワークフローが必要。作者レシピは8steps/CFG1/er_sde/normal。

LoRA単体では動かない。重みはMiniMax H3 Community Licenseでコードのライセンスと別。人物・作品の許諾と生成の誤認防止が必要。

## 使い方

[公式モデルカード](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @Phantom_202601: https://x.com/Phantom_202601/status/2118812967517208975
- @Phantom_202601: https://x.com/Phantom_202601/status/2119191066033508440
- 対象資料: https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA
- 参照: https://make-profit.net/2026/11/06/genai-lab-54-blender-mixamo-h3-soft-body-mannequin-three-angles-regenerated/
- 参照: https://x.com/OJI3_NIKKE/status/2118372636707455412
- 参照: https://api.github.com/repos/toyxyz/toyxyz_RGBMocap
- 参照: https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/README.md
- 参照: https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/LICENSE
- 参照: https://huggingface.co/api/models/akatz-ai/MiniMax-H3-Character-Swap-LoRA
- 参照: https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/raw/main/README.md
- 参照: https://api.github.com/repos/akatz-ai/h3-relay
- 参照: https://x.com/Phantom_202601/status/2119191066033508440

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
