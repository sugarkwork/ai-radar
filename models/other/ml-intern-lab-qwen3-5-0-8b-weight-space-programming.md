---
type: model
model: ML-Intern-lab/Qwen3.5-0.8B-weight-space-programming
name: Qwen3.5-0.8B weight-space-programming
genre: other
url: https://huggingface.co/ML-Intern-lab/Qwen3.5-0.8B-weight-space-programming
author: ML Intern lab（@_akhaliq ほか）
license: Apache-2.0
base_model: [Qwen/Qwen3.5-0.8B]
format: safetensors
size: "0.8B パラメータ（transformers 形式）"
downloads: 35
likes: 45
created: 2026-11-02
updated: 2026-11-03
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/HuggingModels/status/2117748410623427041
sources:
  - https://rikiyat.github.io/blog/weight-space-programming/
  - https://huggingface.co/spaces/akhaliq/weight-space-programming-demo
pricing: free
pricing_detail: "重み無料（Apache-2.0）"
signup_required: false
---

# Qwen3.5-0.8B weight-space-programming

## 出来ること

- **学習せずに重みを直接編集して、モデルの病的な挙動を直したチェックポイント**。Qwen3.5-0.8B が数学問題でトークン上限までループする症状を、勾配降下も微調整も使わずに修正している。
- 手法: フロンティア LLM（"Astra"）が Qwen3.5-0.8B の重みを読み、ループの原因を診断。**layer 15 と 19 の `down_proj` の MLP 出力列 64本ずつ、合計 131,072 個の重み**を手で書き換えた。
- 検証（ブログのプロトコル: vLLM、thinking on、temperature 0.6、top_p 0.95、top_k 20、presence_penalty 1.5、最大32,768トークン、seed 0、最後の `\boxed{}` を math-verify 0.9.0 で採点）:
  - MATH-500 精度: ベース 5.0%（25問スモーク、ブログ値 7.9）→ **51.0%**（ブログ値 48.1）
  - 32kトークンで打ち切られた回答: 95% → **31.6%**
- フル MATH-500（500問×4サンプル = 2,000生成、4,340万トークン、H200 で51分）の生スコアと生成例を `eval/` に同梱。
- ブラウザで触れるデモ（ベースがループする横で、編集版が解く）が公開されている。

## 目的・背景

「重み空間プログラミング（weight-space programming）」— プロンプトやファインチューニングではなく、推論モデルが重みを読んで直接書き換えるアプローチの実証。ブログ *Sparks of Weight Space Programming* の Experiment 8 で、記事では公開されなかったチェックポイントを再現・検証して公開したもの。2026-11-02 公開。同名の別ミラー（`RikiyaT/...`）も存在する。

## 収録ファイル

- transformers 形式の重み（`config.json`、`chat_template.jinja`、tokenizer 一式）
- `eval/` — MATH-500 のベース／編集後の生成サンプルとスコア

## 実行条件

- transformers / vLLM で読める 0.8B モデル。GPU 推論を想定（検証は H200、vLLM）
- 検証設定を揃えないと数値が再現しない（temperature / top_p / top_k / presence_penalty / 最大トークン / 採点器のバージョンまで指定されている）
- 効果はこのチェックポイント固有。他のモデルやタスクに同じ編集が効く保証は無い
- ベースの 5.0% は25問スモークの値で、ブログの 7.9% とは条件が違う点に注意

## 使い方

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("ML-Intern-lab/Qwen3.5-0.8B-weight-space-programming")
model = AutoModelForCausalLM.from_pretrained(
    "ML-Intern-lab/Qwen3.5-0.8B-weight-space-programming", dtype="bfloat16", device_map="auto")
```

```text
デモ: https://huggingface.co/spaces/akhaliq/weight-space-programming-demo
```

## 変更履歴

- 2026-11-04: 初回登録
