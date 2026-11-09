---
type: "model"
name: "Lyricccco/FLUX.2-klein-base-9B-TailSteer"
genre: "image-gen"
url: "https://huggingface.co/Lyricccco/FLUX.2-klein-base-9B-TailSteer"
author: "Lyricccco"
source_post: "https://x.com/cutetoxicguy/status/2118878604574499107"
sources: ["https://x.com/cutetoxicguy/status/2118878604574499107?a=rqNNifMzvaFQgAUBeho&s=46", "https://x.com/cutetoxicguy/status/2118878604574499107", "https://github.com/Lyricccco/tailsteer", "https://api.github.com/repos/Lyricccco/tailsteer", "https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md", "https://arxiv.org/abs/2611.06741", "https://huggingface.co/api/models?search=tailsteer", "https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source", "https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve", "https://huggingface.co/Lyricccco/FLUX.2-klein-base-9B-TailSteer"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "ライセンスotherで基底モデル条件を継承。10ターン後の保持改善は作者ベンチであり独立追試なし。具体的なVRAM要件は未確認。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "Lyricccco/FLUX.2-klein-base-9B-TailSteer"
license: "other"
base_model: ["black-forest-labs/FLUX.2-klein-base-9B"]
downloads: 71
likes: 7
format: "safetensors"
size: "配布中の重みファイル 9本・合計34,706,828,614 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-04"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:30:46.586714+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "flux-non-commercial-license"
---

# Lyricccco/FLUX.2-klein-base-9B-TailSteer

## 出来ること

FLUX.2 klein Base9BにTailSteerを適用した画像編集重み。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:46.586714+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:46.586714+00:00）。重み 9本。

- `text_encoder/model-00001-of-00004.safetensors` — 4,902,257,696 bytes
- `text_encoder/model-00002-of-00004.safetensors` — 4,915,960,368 bytes
- `text_encoder/model-00003-of-00004.safetensors` — 4,983,068,496 bytes
- `text_encoder/model-00004-of-00004.safetensors` — 1,580,230,264 bytes
- `transformer/diffusion_pytorch_model-00001-of-00004.safetensors` — 4,732,234,168 bytes
- `transformer/diffusion_pytorch_model-00002-of-00004.safetensors` — 4,798,294,944 bytes
- `transformer/diffusion_pytorch_model-00003-of-00004.safetensors` — 4,833,950,304 bytes
- `transformer/diffusion_pytorch_model-00004-of-00004.safetensors` — 3,792,711,496 bytes
- ほか1本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/Lyricccco/FLUX.2-klein-base-9B-TailSteer/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

元の対応パイプラインでモデルIDを置換すると作者は説明。9B級モデルと基底モデルの実行依存が必要。

ライセンスotherで基底モデル条件を継承。10ターン後の保持改善は作者ベンチであり独立追試なし。具体的なVRAM要件は未確認。

## 使い方

[公式モデルカード](https://huggingface.co/Lyricccco/FLUX.2-klein-base-9B-TailSteer)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @cutetoxicguy: https://x.com/cutetoxicguy/status/2118878604574499107
- 対象資料: https://huggingface.co/Lyricccco/FLUX.2-klein-base-9B-TailSteer
- 参照: https://github.com/Lyricccco/tailsteer
- 参照: https://api.github.com/repos/Lyricccco/tailsteer
- 参照: https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md
- 参照: https://arxiv.org/abs/2611.06741
- 参照: https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source
- 参照: https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
