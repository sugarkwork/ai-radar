---
type: "model"
name: "flyfront/FFF_MOSS-Alba"
genre: "image-gen"
url: "https://huggingface.co/flyfront/FFF_MOSS-Alba"
author: "flyfront"
source_post: "https://x.com/aiaicreate/status/2118893341630992619"
sources: ["https://x.com/aiaicreate/status/2118893341630992619?a=uN7SYJHTNovwoE2-g3g&s=46", "https://x.com/aiaicreate/status/2118893341630992619", "https://civitai.com/models/3034445/fffmoss-alba", "https://huggingface.co/flyfront/FFF_MOSS-Alba", "https://huggingface.co/api/models/flyfront/FFF_MOSS-Alba"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "学習1377画像・506steps等は作者説明。赤面が出やすく1boyが女性化しやすいとカードに注意。背景・文字品質も独立確認なし。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "flyfront/FFF_MOSS-Alba"
license: "apache-2.0"
base_model: ["OpenMOSS-Team/MOSS-Image-SFT"]
downloads: 0
likes: 0
format: "safetensors"
size: "配布中の重みファイル 7本・合計31,825,828,028 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-10-22"
updated: "2026-11-06"
fetched_at: "2026-11-09T00:30:49.721267+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# flyfront/FFF_MOSS-Alba

## 出来ること

MOSS-Image SFTをFFF_ANIMA-Alba画風でfull fine-tuneした画像モデル。LoRA・トリガーワード不要と説明。

2026-11-09確認のモデルカードでは、full fine-tuneのv1.1に加えて別チェックポイント向けのstyle-v2.1 LoRA（rank64）も配布。full checkpointを使う場合はLoRA不要だが、配布全体がLoRAを含まないわけではない。LoRAはINT8/FP8への適用を推奨し、BF16への丸めで差分が落ちると作者が説明。赤面が少し減ったというv1.1も独立追試はない。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:49.721267+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:49.721267+00:00）。重み 7本。

- `FFF_MOSS-Alba-style-v1.safetensors` — 74,406,432 bytes
- `FFF_MOSS-Alba-style-v2.1.safetensors` — 297,355,152 bytes
- `FFF_MOSS-Alba-style-v2.safetensors` — 297,355,008 bytes
- `FFF_MOSS-Alba-v1.1.safetensors` — 10,164,656,392 bytes
- `FFF_MOSS-Alba-v1.1_int8_convrot.safetensors` — 5,413,699,358 bytes
- `FFF_MOSS-Alba-v1.safetensors` — 10,164,656,328 bytes
- `FFF_MOSS-Alba-v1_int8_convrot.safetensors` — 5,413,699,358 bytes

[ファイル一覧](https://huggingface.co/flyfront/FFF_MOSS-Alba/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

bf16約9.47GB/int8_convrot約5.04GB。Qwen3.5-9B TE、FLUX.2 small-decoder VAE、Euler25〜30steps、CFG3、約2.4MPを推奨。

学習1377画像・506steps等は作者説明。赤面が出やすく1boyが女性化しやすいとカードに注意。背景・文字品質も独立確認なし。

## 使い方

[公式モデルカード](https://huggingface.co/flyfront/FFF_MOSS-Alba)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @aiaicreate: https://x.com/aiaicreate/status/2118893341630992619
- 対象資料: https://huggingface.co/flyfront/FFF_MOSS-Alba
- 参照: https://civitai.com/models/3034445/fffmoss-alba
- 参照: https://huggingface.co/api/models/flyfront/FFF_MOSS-Alba

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
