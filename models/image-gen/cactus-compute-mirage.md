---
type: "model"
name: "Cactus-Compute/mirage"
genre: "image-gen"
url: "https://huggingface.co/Cactus-Compute/mirage"
author: "Cactus-Compute"
source_post: "https://x.com/nahid_pro09/status/2119030921110392842"
sources: ["https://x.com/nahid_pro09/status/2119030921110392842?a=x-kiLrrom_mKcAJekmc&s=46", "https://x.com/nahid_pro09/status/2119030921110392842", "https://cactuscompute.com/blog/mirage", "https://huggingface.co/Cactus-Compute/mirage", "https://huggingface.co/api/models/Cactus-Compute/mirage", "https://github.com/cactus-compute/cactus", "https://api.github.com/repos/cactus-compute/cactus", "https://pypi.org/pypi/cactus-compute/json"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "22MBは量子化cactのサイズで全形式ではない。GalaxyS26 NPU74ms/CPU107msはベンダー測定で、日本語対応やブラウザ動作の独立試験なし。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "Cactus-Compute/mirage"
license: "apache-2.0"
base_model: []
downloads: 6133
likes: 77
format: "safetensors / cact"
size: "配布中の重みファイル 2本・合計237,981,547 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-05"
updated: "2026-11-06"
fetched_at: "2026-11-09T00:31:07.840656+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# Cactus-Compute/mirage

## 出来ること

51.3Mパラメータの端末向け視覚モデルMirage。scene記述、検出、OCR、分割、空間関係等を一パスで扱うと説明。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:07.840656+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:07.840656+00:00）。重み 2本。

- `mirage.cact` — 21,611,043 bytes
- `mirage.safetensors` — 216,370,504 bytes

[ファイル一覧](https://huggingface.co/Cactus-Compute/mirage/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

mirage.cact約21.6MBとsafetensors約216MB。cactus-computeの対応ランタイム、7言語en/de/fr/es/it/nl/plを案内。

22MBは量子化cactのサイズで全形式ではない。GalaxyS26 NPU74ms/CPU107msはベンダー測定で、日本語対応やブラウザ動作の独立試験なし。

## 使い方

[公式モデルカード](https://huggingface.co/Cactus-Compute/mirage)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @nahid_pro09: https://x.com/nahid_pro09/status/2119030921110392842
- 対象資料: https://huggingface.co/Cactus-Compute/mirage
- 参照: https://cactuscompute.com/blog/mirage
- 参照: https://huggingface.co/api/models/Cactus-Compute/mirage
- 参照: https://github.com/cactus-compute/cactus
- 参照: https://api.github.com/repos/cactus-compute/cactus
- 参照: https://pypi.org/pypi/cactus-compute/json

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
