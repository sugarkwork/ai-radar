---
type: model
model: Diffuspace/Clover-35B-A3B-Preview
name: Clover 35B-A3B（拡散型 MoE）
genre: other
url: https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview
author: DiffuSpace
license: Apache-2.0
base_model: [Qwen/Qwen3.6-35B-A3B]
format: safetensors
size: "BF16 重み 約69GB（26シャード）"
downloads: 3341
likes: 243
created: 2026-10-24
updated: 2026-10-28
added: 2026-11-05
first_seen: 2026-10-29
source_post: https://x.com/Av1dlive/status/2115776860714098937
sources:
  - https://diffuspace.ai/
  - https://diffuspace.ai/blog/clover-35b/
  - https://github.com/DiffuSpace/Clover-35B-A3B-Preview
  - https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview-GGUF
pricing: free
pricing_detail: "重み無料（Apache-2.0）"
signup_required: false
flags: [unverified]
risk_notes: "tok/s 比較は投稿者環境の一例で、モデルカードに計測条件の記載がない。"
---

# Clover 35B-A3B（拡散型 MoE）

## 出来ること

- **自己回帰ではなくブロック拡散で書く**テキスト生成モデル。1トークンずつ左から伸ばす代わりに、ブロック単位でマスクを置き、確信度の高い位置から並列に埋めて確定させる。
- Qwen3.6-35B-A3B を土台にした MoE（40層、ルーテッドエキスパート256、top-8、共有エキスパート各層1）。総35B・1トークンあたり約3Bが動く。
- **128K コンテキスト**（プロンプトと生成の合計で最大 131,072 トークン）。
- 双方向ブロック注意のための学習済みパラメータ（右畳み込み重み、softmax 制御）を追加しており、因果プレフィックスは保ったままノイズの入ったブロック内で参照し合える。
- HF 実装の既定は `block_size=32`、`threshold=0.95` の LowConfidence デコード。しきい値を超える位置が無い場合は最上位を1つ埋めて必ず進む。
- SGLang と llama.cpp 向けに**自己投機的デコード**の実装が公式リポジトリにある。GGUF 版も配布されている（2026-11-05 時点で downloads 50,750）。

## 目的・背景

DiffuSpace の最初の公開モデル。自己回帰の逐次生成を置き換え、並列生成・双方向モデリング・反復精錬で速度と制御性を取る路線。投稿は同一プロンプトで「clover 418 tok/s・9.4秒、qwen3.6-35B-A3B 147 tok/s・35.0秒」と比較しているが、これは**投稿者の環境での一例**で、モデルカードに計測条件の記載はない。

## 収録ファイル

- `model-00001-of-00026.safetensors` ほか計26シャード（BF16、合計 約69GB）
- `config.json` / `generation_config.json` / `chat_template.jinja`
- `configuration_clover_moe.py` / `modeling_clover_moe.py`（`trust_remote_code` で読む独自実装）
- `bd_gdn_conv_right_weight.safetensors` / `bd_gdn_softmax_scalars.safetensors`（双方向化の追加パラメータ）
- ATTRIBUTIONS.md、LICENSE

## 実行条件

- **BF16 の重みだけで約69GB**。収めるには 80GB 級の GPU、または分割して置ける環境が要る（量子化版は GGUF / AWQ / GPTQ などが別リポジトリ）。
- `transformers==5.19.0`、PyTorch 2.10 以降、CUDA 版。`trust_remote_code=True` が必須（独自アーキテクチャのため）。
- 量子化版や SGLang / llama.cpp 経路は**専用の実装が要る**。stock の llama.cpp でそのまま動くかは未確認なので、GGUF を使う場合は配布元の手順に従う。
- ライセンスは Apache-2.0（商用可）。土台の Qwen3.6 由来の表記は ATTRIBUTIONS.md にある。
- 速度の数値（tok/s、倍率）は投稿者・作者側の報告。第三者追試は確認していない。

## 使い方

```bash
pip install "transformers==5.19.0" accelerate safetensors
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Diffuspace/Clover-35B-A3B-Preview"
tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, dtype=torch.bfloat16, device_map="cuda:0"
).eval()

prompt = tok.apply_chat_template(
    [{"role": "user", "content": "What is diffusion?"}],
    tokenize=False, add_generation_prompt=True, enable_thinking=True,
)
inputs = tok(prompt, add_special_tokens=False, return_tensors="pt").to("cuda:0")
out = model.generate(**inputs, max_new_tokens=24576, block_size=32, threshold=0.95, do_sample=False)
```

## 変更履歴

- 2026-11-05: 初回登録（downloads 3,341 / likes 243 / Apache-2.0 / 更新 2026-10-28）
