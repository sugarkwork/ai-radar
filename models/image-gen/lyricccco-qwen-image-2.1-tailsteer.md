---
type: "model"
name: "Lyricccco/Qwen-Image-2.1-TailSteer"
genre: "image-gen"
url: "https://huggingface.co/Lyricccco/Qwen-Image-2.1-TailSteer"
author: "Lyricccco"
source_post: "https://x.com/cutetoxicguy/status/2118878604574499107"
sources: ["https://x.com/cutetoxicguy/status/2118878604574499107?a=rqNNifMzvaFQgAUBeho&s=46", "https://x.com/cutetoxicguy/status/2118878604574499107", "https://github.com/Lyricccco/tailsteer", "https://api.github.com/repos/Lyricccco/tailsteer", "https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md", "https://arxiv.org/abs/2611.06741", "https://huggingface.co/api/models?search=tailsteer", "https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source", "https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve", "https://huggingface.co/Lyricccco/Qwen-Image-2.1-TailSteer"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "license otherで基底条件を確認する。RISE accuracy20.56→18.06という低下も論文にあり、保持改善だけを万能な性能向上としない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "Lyricccco/Qwen-Image-2.1-TailSteer"
license: "other"
base_model: ["Qwen/Qwen-Image-2.1"]
downloads: 110
likes: 36
format: "safetensors"
size: "配布中の重みファイル 8本・合計33,115,613,400 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-04"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:30:46.997010+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "qwen-research"
---

# Lyricccco/Qwen-Image-2.1-TailSteer

## 出来ること

Qwen-Image-2.1にTailSteerを適用した反復画像編集重み。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:46.997010+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:46.997010+00:00）。重み 8本。

- `text_encoder/model-00001-of-00004.safetensors` — 4,998,056,552 bytes
- `text_encoder/model-00002-of-00004.safetensors` — 4,915,962,464 bytes
- `text_encoder/model-00003-of-00004.safetensors` — 4,915,962,496 bytes
- `text_encoder/model-00004-of-00004.safetensors` — 2,704,357,976 bytes
- `transformer/diffusion_pytorch_model-00001-of-00003.safetensors` — 4,902,110,640 bytes
- `transformer/diffusion_pytorch_model-00002-of-00003.safetensors` — 4,999,628,920 bytes
- `transformer/diffusion_pytorch_model-00003-of-00003.safetensors` — 4,328,544,840 bytes
- `vae/diffusion_pytorch_model.safetensors` — 1,350,989,512 bytes

[ファイル一覧](https://huggingface.co/Lyricccco/Qwen-Image-2.1-TailSteer/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

対応Qwen画像編集パイプラインとモデルの依存ファイルを使用する。推論時追加アダプタ不要は作者説明。

license otherで基底条件を確認する。RISE accuracy20.56→18.06という低下も論文にあり、保持改善だけを万能な性能向上としない。

## 使い方

[公式モデルカード](https://huggingface.co/Lyricccco/Qwen-Image-2.1-TailSteer)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @cutetoxicguy: https://x.com/cutetoxicguy/status/2118878604574499107
- 対象資料: https://huggingface.co/Lyricccco/Qwen-Image-2.1-TailSteer
- 参照: https://github.com/Lyricccco/tailsteer
- 参照: https://api.github.com/repos/Lyricccco/tailsteer
- 参照: https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md
- 参照: https://arxiv.org/abs/2611.06741
- 参照: https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source
- 参照: https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
