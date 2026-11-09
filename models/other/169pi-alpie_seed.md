---
type: "model"
name: "169Pi/Alpie_seed"
genre: "other"
url: "https://huggingface.co/169Pi/Alpie_seed"
author: "169Pi"
source_post: "https://x.com/QwenAIFans/status/2118844454308356232"
sources: ["https://x.com/qwenaifans/status/2118844454308356232?a=l2btGsA-zihzh2IMc4U&s=46", "https://x.com/QwenAIFans/status/2118844454308356232", "https://huggingface.co/169Pi/Alpie_seed", "https://huggingface.co/api/models/169Pi/Alpie_seed", "https://huggingface.co/169Pi/Alpie_seed/raw/main/README.md", "https://ollama.com/169pi/alpie-seed/tags"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "61.20はMini-SWE-agent・thinking有効・再試行なし・temperature0のモデルカード自己報告。latestタグだけで画像入力可能とは判断しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "169Pi/Alpie_seed"
license: "apache-2.0"
base_model: ["Qwen/Qwen3.5-9B"]
downloads: 443
likes: 23
format: "safetensors"
size: "配布中の重みファイル 1本・合計18,819,722,392 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-10-23"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:30:32.866678+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# 169Pi/Alpie_seed

## 出来ること

Qwen3.5-9Bを基にしたAlpie_seed。OllamaとGGUF配布があり、紹介はSWE-Bench Verifiedのコーディング評価。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:32.866678+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:32.866678+00:00）。重み 1本。

- `model.safetensors` — 18,819,722,392 bytes

[ファイル一覧](https://huggingface.co/169Pi/Alpie_seed/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

Ollama latestはテキスト入力5.6GB、画像入力は別のvisionタグ6.6GBという原チェック記録。

61.20はMini-SWE-agent・thinking有効・再試行なし・temperature0のモデルカード自己報告。latestタグだけで画像入力可能とは判断しない。

## 使い方

[公式モデルカード](https://huggingface.co/169Pi/Alpie_seed)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @QwenAIFans: https://x.com/QwenAIFans/status/2118844454308356232
- 対象資料: https://huggingface.co/169Pi/Alpie_seed
- 参照: https://huggingface.co/api/models/169Pi/Alpie_seed
- 参照: https://huggingface.co/169Pi/Alpie_seed/raw/main/README.md
- 参照: https://ollama.com/169pi/alpie-seed/tags

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
