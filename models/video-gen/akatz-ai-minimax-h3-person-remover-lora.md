---
type: "model"
name: "akatz-ai/MiniMax-H3-Person-Remover-LoRA"
genre: "video-gen"
url: "https://huggingface.co/akatz-ai/MiniMax-H3-Person-Remover-LoRA"
author: "akatz-ai"
source_post: "https://x.com/Phantom_202601/status/2119191066033508440"
sources: ["https://x.com/Phantom_202601/status/2119191066033508440", "https://huggingface.co/akatz-ai/MiniMax-H3-Person-Remover-LoRA"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "人物除去の品質・背景保持は未実行確認。Character Swapの強度や8stepレシピを根拠なくこの別LoRAへ流用しない。基底モデルの条件も別途適用。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "akatz-ai/MiniMax-H3-Person-Remover-LoRA"
license: "other"
base_model: ["Comfy-Org/MiniMax-H3"]
downloads: 3270
likes: 95
format: "safetensors"
size: "配布中の重みファイル 1本・合計155,110,584 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-10-08"
updated: "2026-10-17"
fetched_at: "2026-11-09T00:31:29.242197+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "minimax-h3-community-license-agreement"
---

# akatz-ai/MiniMax-H3-Person-Remover-LoRA

## 出来ること

MiniMax H3の動画から人物を除去する用途のPerson Remover LoRA。

2026-11-09確認のモデルカードではSAM 3.1で人物を追跡してマスクを緑色にし、重なりのある窓で背景を生成する。元動画と、人物を除去した最初のフレームが必要。公開ショーケースは成功例の選択でベンチではなく、背景・影・カメラ・カットが変化し得ると作者自身が明記。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:29.242197+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:29.242197+00:00）。重み 1本。

- `H3-Person-Remover-V1.safetensors` — 155,110,584 bytes

[ファイル一覧](https://huggingface.co/akatz-ai/MiniMax-H3-Person-Remover-LoRA/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

約160MBのLoRAで、単独モデルではない。対応H3本体と配布元のワークフロー・マスク等の要件を確認する。

人物除去の品質・背景保持は未実行確認。Character Swapの強度や8stepレシピを根拠なくこの別LoRAへ流用しない。基底モデルの条件も別途適用。

## 使い方

[公式モデルカード](https://huggingface.co/akatz-ai/MiniMax-H3-Person-Remover-LoRA)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @Phantom_202601: https://x.com/Phantom_202601/status/2119191066033508440
- 対象資料: https://huggingface.co/akatz-ai/MiniMax-H3-Person-Remover-LoRA

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
