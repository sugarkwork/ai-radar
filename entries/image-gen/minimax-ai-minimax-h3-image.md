---
name: "MiniMax-H3-Image"
genre: "image-gen"
url: "https://github.com/MiniMax-AI/MiniMax-H3-Image"
repo: "MiniMax-AI/MiniMax-H3-Image"
license: "unknown"
flags: ["unverified"]
risk_notes: "READMEはライセンスを示すバッジとLICENSEへのリンクを掲載していますが、ライセンス名や利用条件は確認できません。 GitHub APIでライセンスを確認できていません。"
stars: 85
forks: 2
open_issues: 0
size_kb: 11715
language: "unknown"
created: "2026-11-09"
updated: "2026-11-10"
archived: false
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/bei351009016/status/2120333007949267319"]
fetched_at: "2026-11-11T04:09:44.778055+00:00"
---

# MiniMax-H3-Image

## 出来ること

- READMEでは、テキストからの画像生成と、1枚以上の参照画像を使った画像編集を、単一のチェックポイントで行うモデルと説明されています。生成と編集はいずれもMiniMax-H3-Imageの機能として記載されています。

## 目的・背景

- 作者は、クリエイティブな意図を画像に反映し、キャラクター・場面・雰囲気を作る用途を挙げています。また、約16メガピクセルの画像をアップスケーラーなしで生成できることや、最大16枚の参照画像に対応することをREADMEで主張しています。これらは作者の説明であり、独立した性能検証結果ではありません。

## 依存関係

- READMEのモデル構成では、MiniMax-H3のQwen3-VLテキストエンコーダーを使用します。このエンコーダーは本リポジトリに含まれず、MiniMaxAI/MiniMax-H3から取得します。README記載のモデル容量は、画像モデルのチェックポイントが68.65 GB、テキストエンコーダーが66.7 GBです。

## 実行条件

- READMEはローカル推論用フレームワークとしてSGLang、vLLM、diffusers、ComfyUIを列挙し、SGLangの1 GPUでの起動例を掲載しています。モデルファイルは大容量で、README記載では画像モデル一式が約68.65 GB、別途テキストエンコーダーが66.7 GBです。具体的なGPUメモリ要件はREADMEに示されていません。

## 最短手順

- README記載の手順は、Hugging Face CLIで `hf download MiniMaxAI/MiniMax-H3-Image` と `hf download MiniMaxAI/MiniMax-H3 --include "text_encoder/*"` を実行してモデルを取得し、SGLangを使う場合は `sglang serve --model-path MiniMaxAI/MiniMax-H3-Image --host 0.0.0.0 --port 30000 --warmup-mode off` で起動する方法です。ここでは手順の掲載内容を要約しており、実行確認はしていません。

## 変更履歴

- 2026-11-11: 初回登録
