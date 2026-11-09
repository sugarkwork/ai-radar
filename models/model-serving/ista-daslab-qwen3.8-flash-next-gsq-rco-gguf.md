---
type: "model"
name: "ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF"
genre: "model-serving"
url: "https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF"
author: "ISTA-DASLab"
source_post: "https://x.com/sasasin_net/status/2118729264149491929"
sources: ["https://x.com/sasasin_net/status/2118729264149491929?a=tWrww52LyfJHPpXLuT4&s=46", "https://x.com/sasasin_net/status/2118729264149491929", "https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-IQ2_XS", "https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S", "https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "Unsloth版との性能比較は個人の感想で独立測定なし。量子化方式と条件の違いをファイルサイズだけで評価しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF"
license: "apache-2.0"
base_model: ["Qwen/Qwen3.8-Flash-Next"]
downloads: 6825140
likes: 1203
format: "gguf"
size: "配布中の重みファイル 9本・合計294,815,175,840 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-09-07"
updated: "2026-09-29"
fetched_at: "2026-11-09T00:30:30.158989+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF

## 出来ること

Qwen3.8-Flash-NextにGSQ-RCOを適用したGGUF量子化配布。体験記事の旧構成IQ3_Sは2分割で約77.9GiB。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:30.158989+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:30.158989+00:00）。重み 9本。

- `IQ2_XS/Qwen3.8-Flash-Next-GSQ-RCO-IQ2_XS-00001-of-00002.gguf` — 39,225,954,592 bytes
- `IQ2_XS/Qwen3.8-Flash-Next-GSQ-RCO-IQ2_XS-00002-of-00002.gguf` — 28,800,138,432 bytes
- `IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf` — 54,817,524,224 bytes
- `IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00002-of-00002.gguf` — 28,800,138,432 bytes
- `IQ3_XXS/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_XXS-00001-of-00002.gguf` — 47,039,860,096 bytes
- `IQ3_XXS/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_XXS-00002-of-00002.gguf` — 28,800,138,432 bytes
- `Q2_0/Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00001-of-00002.gguf` — 37,623,740,192 bytes
- `Q2_0/Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00002-of-00002.gguf` — 28,800,138,432 bytes
- ほか1本。複数形式・量子化・分割を含むため全量ダウンロードを推奨する意味ではない。

[ファイル一覧](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

対応するGGUFランタイムと全分割ファイル、モデル容量に応じたメモリが必要。

Unsloth版との性能比較は個人の感想で独立測定なし。量子化方式と条件の違いをファイルサイズだけで評価しない。

## 使い方

[公式モデルカード](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @sasasin_net: https://x.com/sasasin_net/status/2118729264149491929
- 対象資料: https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF
- 参照: https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/main/UD-IQ2_XS
- 参照: https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/main/IQ3_S

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
