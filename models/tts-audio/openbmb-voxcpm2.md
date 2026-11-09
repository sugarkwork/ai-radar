---
type: "model"
name: "openbmb/VoxCPM2"
genre: "tts-audio"
url: "https://huggingface.co/openbmb/VoxCPM2"
author: "openbmb"
source_post: "https://x.com/Manorgw/status/2118861993281286621"
sources: ["https://x.com/manorgw/status/2118861993281286621?a=ckCiZ8tJo04gsnzxn2I&s=46", "https://x.com/Manorgw/status/2118861993281286621", "https://github.com/OpenBMB/VoxCPM", "https://api.github.com/repos/OpenBMB/VoxCPM", "https://raw.githubusercontent.com/OpenBMB/VoxCPM/main/README.md", "https://huggingface.co/api/models/openbmb/VoxCPM2", "https://huggingface.co/openbmb/VoxCPM2"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Apache-2.0表記でも参照音声・人物の声の権利は別。速度・自然さ・クローン品質は未試聴・未追試。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "openbmb/VoxCPM2"
license: "apache-2.0"
base_model: []
downloads: 978473
likes: 1760
format: "safetensors / pytorch"
size: "配布中の重みファイル 2本・合計4,957,031,714 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-04-03"
updated: "2026-08-18"
fetched_at: "2026-11-09T00:30:35.416948+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# openbmb/VoxCPM2

## 出来ること

VoxCPM2の重み配布。文章で声を設計し、参照音声の声質と話し方を制御する2Bの多言語TTS。

## 目的・背景

対象固有の機能・制約の説明は2026-11-07のチェック記録を基にしている。メタ情報は2026-11-09T00:30:35.416948+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:35.416948+00:00）。重み 2本。

- `audiovae.pth` — 376,951,122 bytes
- `model.safetensors` — 4,580,080,592 bytes

[ファイル一覧](https://huggingface.co/openbmb/VoxCPM2/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

OpenBMB/VoxCPMのランタイム、AudioVAE V2と音声入出力環境が必要。48kHz・30言語はカードの仕様説明。

Apache-2.0表記でも参照音声・人物の声の権利は別。速度・自然さ・クローン品質は未試聴・未追試。

## 使い方

[公式モデルカード](https://huggingface.co/openbmb/VoxCPM2)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @Manorgw: https://x.com/Manorgw/status/2118861993281286621
- 対象資料: https://huggingface.co/openbmb/VoxCPM2
- 参照: https://github.com/OpenBMB/VoxCPM
- 参照: https://api.github.com/repos/OpenBMB/VoxCPM
- 参照: https://raw.githubusercontent.com/OpenBMB/VoxCPM/main/README.md
- 参照: https://huggingface.co/api/models/openbmb/VoxCPM2

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
