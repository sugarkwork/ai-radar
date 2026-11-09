---
type: "model"
name: "sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4"
genre: "model-serving"
url: "https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4"
author: "sakamakismile"
source_post: "https://x.com/Tono_Ken3/status/2118976295799558232"
sources: ["https://x.com/tono_ken3/status/2118976295799558232?a=Bn4jZj34rtUx_KGEWAg&s=46", "https://x.com/Tono_Ken3/status/2118976295799558232", "https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4", "https://huggingface.co/api/models/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4", "https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4/raw/main/README.md", "https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4/raw/main/recipe.yaml", "https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "画像説明の検証はBF16展開でありNVFP4 vision配信の確認ではない。ロード9.65GiB・29.35tok/s等はRTX PRO2000 Blackwellでの作者試験。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4"
license: "apache-2.0"
base_model: ["xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic"]
downloads: 52
likes: 5
format: "safetensors"
size: "配布中の重みファイル 6本・合計11,198,703,656 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:31:01.371690+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4

## 出来ること

xtools-atの9B Heretic重みをNVFP4 E2M1/FP8ブロックスケールへweight-only量子化した派生。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:01.371690+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:01.371690+00:00）。重み 6本。

- `model-00001-of-00006.safetensors` — 2,034,237,568 bytes
- `model-00002-of-00006.safetensors` — 2,034,237,592 bytes
- `model-00003-of-00006.safetensors` — 1,994,662,464 bytes
- `model-00004-of-00006.safetensors` — 1,992,951,696 bytes
- `model-00005-of-00006.safetensors` — 1,994,063,800 bytes
- `model-00006-of-00006.safetensors` — 1,148,550,536 bytes

[ファイル一覧](https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

6シャード約11.2GB、vision/attention/embedding等はBF16保持。作者のネイティブ配信はvLLM0.33.0/Marlinでtext-only。

画像説明の検証はBF16展開でありNVFP4 vision配信の確認ではない。ロード9.65GiB・29.35tok/s等はRTX PRO2000 Blackwellでの作者試験。

## 使い方

[公式モデルカード](https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @Tono_Ken3: https://x.com/Tono_Ken3/status/2118976295799558232
- 対象資料: https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4
- 参照: https://huggingface.co/api/models/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4
- 参照: https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4/raw/main/README.md
- 参照: https://huggingface.co/sakamakismile/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-NVFP4/raw/main/recipe.yaml
- 参照: https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
