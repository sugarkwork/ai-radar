---
type: "repo"
name: "Qwen-Image-2.1"
genre: image-gen
url: "https://github.com/QwenLM/Qwen-Image-2.1"
author: "QwenLM (Alibaba Qwen team)"
repo: "QwenLM/Qwen-Image-2.1"
license: "NOASSERTION"
stars: 2189
language: "Python"
created: "2026-09-14"
updated: "2026-10-14"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/Machinedelusion/status/2116624498933833758"]
flags: []
risk_notes: "ライセンスは Qwen Research License Agreement (NOASSERTION) で非商用限定。商用利用は model-business@notice.qwencloud.com への別途申請が必要 (LICENSE 20行目)。GitHub Releases は未作成のため版管理はコミット単位。重みは HF/ModelScope 側にありリポジトリに含まれない。2026-10-14 以降コミットが止まり、直近の変更はドキュメントのみ。発見源の投稿本文は別プロジェクト (HairDeck / アニメ髪カード生成) の説明で本リポジトリの内容と一致しない。README 内で dtype= と torch_dtype= の表記揺れがある。"
forks: 158
open_issues: 24
commits_30d: 3
commit_cadence: "monthly"
size_kb: 16711
archived: false
fetched_at: "2026-11-09T21:38:26Z"
last_release: ""
last_release_at: ""
commits_90d: 31
---

# Qwen-Image-2.1 — 透過RGBAと最大10枚参照の編集に対応した7B画像生成モデル（Diffusers / vLLM-Omni / SGLang で配信）

## 出来ること

- テキストからの画像生成（ネイティブ2K、既定 2048x2048 / 40 steps）
- 画像編集: 1枚入力の指示編集、最大10枚の参照画像によるマルチ被写体合成
- ローカル編集: 円・塗り注釈・マスクによる領域指定、人物/商品の同一性保持
- 透過RGBA画像の生成と透過レイヤーの編集（64ch RGBA VAE）
- プロンプト書き換えモデル（Qwen-Image-2.1-PE-T2I / PE-I2I、Qwen3.5-VL 9B ベース）を CLI / vLLM サーバで実行
- 8 steps で動く軽量チェックポイント Qwen-Image-2.1-Turbo
- 配信経路: Diffusers の QwenImage21Pipeline、vLLM-Omni（OpenAI 互換 /v1/images/generations）、SGLang、LightX2V、ComfyUI、Alibaba Cloud Model Studio のホストAPI

## 目的・背景

- Qwen ファミリーの統合型テキスト→画像生成＋画像編集モデル。視覚生成部は 7B / 32層の single-stream DiT。
- テキストエンコーダは Qwen3-VL 8B で、指示文と条件画像を統一表現に符号化する。
- 混合粒度アテンション＋prefix KV cache 再利用により、条件画像の符号化を初回ステップのみに削減。
- 生成・編集・透過素材の切り出しを1モデルに統合し、推論コストを下げるのが狙い。

## 依存関係

- Python + PyTorch>=2.4.0（bfloat16 推論、サンプルは .to('cuda') 前提）
- transformers>=5.17、accelerate、pillow
- diffusers は PyPI 版ではなく GitHub ソース（QwenImage21Pipeline を含む版）が必要
- 重み: HuggingFace Qwen/Qwen-Image-2.1（Turbo は Qwen/Qwen-Image-2.1-Turbo）、ModelScope ミラーあり。リポジトリには同梱されない
- 任意: vLLM-Omni（--omni）、SGLang-Diffusion、LightX2V、ComfyUI（Comfy-Org/Qwen-Image-2.1 の重み）
- プロンプト書き換えを使う場合のみ prompt_rewrite/requirements.txt（vLLM 版は vLLM 必須）

## 実行条件

- GPU メモリ: 公式に最小要件の明記なし（未検証）。7B 規模のため enable_model_cpu_offload 前提の運用も可
- ライセンス: 非商用のみ。商用は別途ライセンス契約が必要
- 既定解像度は 2048x2048。対応アスペクト比は 1:1 / 4:3 / 3:4 / 3:2 / 2:3 / 16:9 / 9:16（辺は32の倍数）
- 初回実行時に HF から重みを取得するため、相応のディスクとネットワークが必要（サイズ未検証）
- エージェントから使う場合は HTTP で叩ける vLLM-Omni の /v1/images/generations 経由が最も素直

## 最短手順

- 1) HTTP で呼ぶ最短経路: vLLM-Omni を入れた環境で `vllm serve Qwen/Qwen-Image-2.1 --omni --port 8091` を起動する。
- 2) 起動確認: 同じホストで `curl -sS http://localhost:8091/v1/models` を実行し、JSON に当該モデルが並ぶことを確認する。
- 3) 生成: リクエスト本文を body.json に書き、`curl -sS http://localhost:8091/v1/images/generations -H 'Content-Type: application/json' --data @body.json` を実行する。body の例: model に Qwen/Qwen-Image-2.1、prompt、size 1024x1024、num_inference_steps 40、seed 42。
- 4) 高速化: ステップ実行なら `vllm serve Qwen/Qwen-Image-2.1 --omni --port 8091 --step-execution --max-num-seqs 8`。8 steps でよければ model を Qwen/Qwen-Image-2.1-Turbo に差し替える（保存済みスケジュールが使われる）。
- 5) Python で呼ぶ場合: torch>=2.4.0 / transformers>=5.17 / accelerate / pillow を pip で入れ、diffusers は GitHub ソース（git+https://github.com/huggingface/diffusers）から入れる。次に QwenImage21Pipeline.from_pretrained に Qwen/Qwen-Image-2.1 と torch_dtype=torch.bfloat16 を渡して cuda に載せ、prompt・width・height・num_inference_steps を渡して images[0] を保存する。エージェントはこのスクリプトを .py に書いて python3 で実行すればよい。
- 6) 編集: 同じ pipeline の image 引数に PIL 画像（最大10枚のリスト可）と編集指示 prompt を渡す。透過が必要なときは prompt を「This is an RGBA image with transparency. <description>. The image has alpha channel and the background is transparent.」の形式にする。
- 7) プロンプト拡張（任意）: prompt_rewrite ディレクトリで requirements を入れ、run_vllm.py に --task t2i、--ckpt Qwen/Qwen-Image-2.1-PE-T2I、--input data/t2i_example.jsonl、--output out.jsonl を渡して実行する。出力の rewritten_prompt と wh_ratio を生成呼び出しに渡す。

## 変更履歴

- 2026-11-06: 初回登録
