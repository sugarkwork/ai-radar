---
type: "repo"
name: "NitroFusion2（1〜2ステップ text-to-image）"
genre: "video-gen"
url: "https://github.com/ChenDarYen/NitroFusion2"
author: "ChenDarYen"
repo: "ChenDarYen/NitroFusion2"
license: "Apache-2.0"
stars: 24
language: "Python"
created: "2026-10-27"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/Machinedelusion/status/2116668287656333409"]
flags: ["unverified"]
risk_notes: "発見元の投稿（x.com/Machinedelusion/...）は別プロジェクト WeVisCut の宣伝で、NitroFusion2 の説明は一切ない。本項目の根拠はリポジトリ/モデルカードの一次情報のみ。README の「1 step で sharp text」「比較画像」は著者の主張で、第三者計測や条件記載はない。必要 VRAM は README・モデルカードに記載がなく未検証（bf16 重みが約 12.3GB、Q2_K_4XS で約 2.0GB）。リリース/タグが無いため固定バージョンでの導入はできず、clone 時点の main に追従する。カタログに image-gen ジャンルが無いため、同じ扱いをしている画像系モデル（Anima RGBA 等）に合わせて video-gen に分類した（実体は text-to-image）。ライセンスは本体・重みとも Apache-2.0、土台の Tongyi-MAI/Z-Image-Turbo も apache-2.0。"
forks: 1
open_issues: 1
commits_30d: 5
commit_cadence: "weekly"
size_kb: 5012
archived: false
fetched_at: "2026-11-06T13:09:20Z"
last_release: ""
last_release_at: ""
---

# NitroFusion2 — 1〜2ステップで 1024px 画像を出す text-to-image 蒸留モデル

## 出来ること

- テキストプロンプトから 1024×1024 の画像を 1〜4 ステップで生成する（inference.py は 1/2/3/4 step のみ許可、step ごとに scheduler shift を 3.0/6.0/8.0/9.0 へ自動切替）
- 1 step でも文字や細部が描けることを売りにしている（README の比較画像は著者側の提示で、条件の記載はない）
- CLI: python inference.py --prompt "..." --steps 2 --width 1024 --height 1024 --seed 42 --out out.png
- Python API: from inference import load, generate で ZImagePipeline を組み、generate(pipe, prompt, steps=2) が PIL.Image を返す（--no-dedistill-lora で LoRA を切れる）
- ComfyUI 用ワークフロー JSON を4本同梱: workflows/nitrofusion2_1step.json / _2step.json / _1step_gguf.json / _2step_gguf.json
- GGUF 量子化を Q2_K_4XS（2.0GB）から Q8_0（7.2GB）まで16段階で配布（ComfyUI-GGUF 系ノード向け）
- de-distillation LoRA（nf2-dedistill-lora.safetensors、382MB）を step ごとに scale 0.5→0.0 と切り替えて 2 step の破綻を抑える（inference.py に実装済み）
- ブラウザで試せる Gradio デモ（huggingface.co/spaces/ChenDY/NitroFusion2）

## 目的・背景

- MMDiT では中間層の時点でテキストトークンが画像を読み込み、条件に沿った「生成内容の要約」になっている。NitroFusion2 はそのテキストストリーム側に adversarial loss を置き、画像特徴側の損失と併用する蒸留手法（arXiv:2611.05648、Chen & Song）。
- 要約がテキスト条件に紐づくため、同じ discriminator でも cue（typography / object / style）を差し替えるだけで別の観点を評価できる、というのが論文の主張。
- 土台は Tongyi-MAI/Z-Image-Turbo（Apache-2.0）。その transformer を 1〜4 step 用に蒸留した重みを ChenDY/NitroFusion2 として配布している。
- コード・重み・GGUF・ComfyUI ワークフロー・デモを 2026-11-03 に同時公開。GitHub リポジトリは 2026-10-27 作成、取得時点で stars 24 / forks 1 / open issues 1、HF 側 downloads 874 / likes 15。
- 論文リポジトリではあるが、単なる解説ではなく推論コードと重みが動く形で入っている（データセット配布ではない）。

## 依存関係

- Python + PyTorch（CUDA ビルド）。inference.py は torch.Generator("cuda") を直接使うため CPU 実行は不可
- diffusers（ZImagePipeline / ZImageTransformer2DModel / FlowMatchEulerDiscreteScheduler を含む版）。これらは比較的新しいクラスなので、古い diffusers では import が通らない
- transformers / accelerate / safetensors / huggingface_hub（モデル取得）
- 重み: ChenDY/NitroFusion2 の transformer サブフォルダ（約 12.3GB、3 シャード）と nf2-dedistill-lora.safetensors（382MB）
- ベースパイプライン: Tongyi-MAI/Z-Image-Turbo（VAE・テキストエンコーダ等をここから読む。gated ではない）
- ComfyUI で使う場合は ComfyUI 本体と、GGUF ワークフロー用の GGUF ローダノード（ワークフロー JSON は同梱、ノード側は各自の環境依存）
- ライセンス: コード・重みとも Apache-2.0（GitHub license API / HF cardData とも apache-2.0）

## 実行条件

- CUDA GPU 必須。README・モデルカードに必要 VRAM の記載はなく未検証（bf16 重みが約 12.3GB、GGUF Q2_K_4XS なら約 2.0GB なので、量子化版で下げる前提）
- 初回実行時に Hugging Face から重みを取得する。認証不要（gated=false）。bf16 で約 12.3GB、GGUF 最小 2.0GB のダウンロードが発生する
- リリース・タグが無い（releases/latest は 404、tags 空）ため、clone した main を使う。バージョン固定はできない
- steps は 1〜4 のみ。それ以外は assert で停止する（inference.py の SHIFT テーブル）
- guidance_scale は 0.0 固定（蒸留モデルのため CFG なし）。ネガティブプロンプトは使えない
- 生成物は PNG 1 枚。メタデータ等は書き出さないので、プロンプト・seed は呼び出し側で記録する必要がある

## 最短手順

- 1. 取得: git clone https://github.com/ChenDarYen/NitroFusion2 && cd NitroFusion2
- 2. 依存導入: pip install torch diffusers transformers accelerate safetensors（CUDA 版 PyTorch、ZImagePipeline が入る新しい diffusers）
- 3. AI から CLI を呼ぶ: python inference.py --prompt "a cat holding a sign that says hello world" --steps 2 --width 1024 --height 1024 --seed 42 --out /abs/path/out.png をサブプロセス実行し、終了コード 0 と /abs/path/out.png の生成で成功を判定する（stdout には進捗以外を出さないので、ファイルの存在とサイズで確認する）
- 4. 1 step で速く回す: 同じコマンドで --steps 1（shift 3.0、LoRA は自動で無効）。まず構図確認に使い、仕上げを 2 step にする運用が README の想定
- 5. Python から呼ぶ: from inference import load, generate / pipe = load() / img = generate(pipe, "<prompt>", steps=2, seed=7) / img.save("out.png")（load() は cpu offload を有効化しないので、必要なら pipe.enable_model_cpu_offload() を自前で呼ぶ）
- 6. ComfyUI で使う: workflows/nitrofusion2_2step.json を ComfyUI にドラッグし、transformer と LoRA を models/ 配下に置いてから実行（GGUF 版は _gguf.json と nf2-Q*_*.gguf）
- 7. 環境を作らず試す: https://huggingface.co/spaces/ChenDY/NitroFusion2 でブラウザから同一モデルを実行

## 変更履歴

- 2026-11-06: 初回登録
