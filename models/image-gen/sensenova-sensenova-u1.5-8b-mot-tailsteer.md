---
type: "model"
name: "sensenova/SenseNova-U1.5-8B-MoT-TailSteer"
genre: "image-gen"
url: "https://huggingface.co/sensenova/SenseNova-U1.5-8B-MoT-TailSteer"
author: "sensenova"
source_post: "https://x.com/cutetoxicguy/status/2118878604574499107"
sources: ["https://x.com/cutetoxicguy/status/2118878604574499107?a=rqNNifMzvaFQgAUBeho&s=46", "https://x.com/cutetoxicguy/status/2118878604574499107", "https://github.com/Lyricccco/tailsteer", "https://api.github.com/repos/Lyricccco/tailsteer", "https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md", "https://arxiv.org/abs/2611.06741", "https://huggingface.co/api/models?search=tailsteer", "https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source", "https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve", "https://huggingface.co/sensenova/SenseNova-U1.5-8B-MoT-TailSteer"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Apache-2.0表記。RISE accuracy31.39→29.44という低下もあり、反復保持と単発編集品質を別に評価する。未実行。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "sensenova/SenseNova-U1.5-8B-MoT-TailSteer"
license: "apache-2.0"
base_model: ["sensenova/SenseNova-U1.5-8B-MoT"]
downloads: 116
likes: 4
format: "safetensors"
size: "配布中の重みファイル 8本・合計35,065,858,152 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-04"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:30:47.165120+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# sensenova/SenseNova-U1.5-8B-MoT-TailSteer

## 出来ること

SenseNova-U1.5-8B-MoTにTailSteerを適用した画像編集重み。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:47.165120+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:47.165120+00:00）。重み 8本。

- `model-00001-of-00008.safetensors` — 4,930,940,840 bytes
- `model-00002-of-00008.safetensors` — 4,932,725,600 bytes
- `model-00003-of-00008.safetensors` — 4,983,075,360 bytes
- `model-00004-of-00008.safetensors` — 4,949,521,032 bytes
- `model-00005-of-00008.safetensors` — 4,932,725,592 bytes
- `model-00006-of-00008.safetensors` — 4,999,870,768 bytes
- `model-00007-of-00008.safetensors` — 4,932,725,496 bytes
- `model-00008-of-00008.safetensors` — 404,273,464 bytes

[ファイル一覧](https://huggingface.co/sensenova/SenseNova-U1.5-8B-MoT-TailSteer/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

対応するSenseNova編集環境が必要。追加アダプタ不要という記述は配布元による案内。

Apache-2.0表記。RISE accuracy31.39→29.44という低下もあり、反復保持と単発編集品質を別に評価する。未実行。

## 使い方

[公式モデルカード](https://huggingface.co/sensenova/SenseNova-U1.5-8B-MoT-TailSteer)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。 custom_code / trust_remote_codeを使う例がある場合は実装の内容を確認してから許可する。

## 出典

- @cutetoxicguy: https://x.com/cutetoxicguy/status/2118878604574499107
- 対象資料: https://huggingface.co/sensenova/SenseNova-U1.5-8B-MoT-TailSteer
- 参照: https://github.com/Lyricccco/tailsteer
- 参照: https://api.github.com/repos/Lyricccco/tailsteer
- 参照: https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md
- 参照: https://arxiv.org/abs/2611.06741
- 参照: https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source
- 参照: https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
