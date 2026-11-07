---
type: "repo"
name: "FLUX.2"
genre: "other"
url: "https://github.com/black-forest-labs/flux2"
repo: "black-forest-labs/flux2"
license: "Apache-2.0"
stars: 2842
language: "Python"
created: "2025-11-24"
updated: 2026-03-12
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 発見元の「Klein 4B は Apache-2.0 の重み」は半分だけ正しい。Apache-2.0 なのは klein 4B（蒸留）と klein 4B Base の2つだけで、9B / 9B KV / 9B Base / FLUX.2 [dev]（32B）は FLUX Non-Commercial License（HF の license_name は flux-non-commercial-license）。② repo の LICENSE.md は Apache-2.0 だがこれは推論コードのみ。重みは README が model_licenses/ 配下に別建てしており、コードのライセンスは重みに及ばない。③ README の表は 9B 系のライセンス欄を LICENSE-FLUX-NON-COMMERICAL にリンクしつつ本文では「FLUX.2-dev Non-Commercial License」と書いており、実ファイルも v2.0 の LICENSE-FLUX-DEV と v2.1 の LICENSE-FLUX-NON-COMMERICAL が併存して食い違う（HF カードが指すのは v2.1 系）。④ 8GB VRAM という記述は 4B の transformer 単体の話で、CLI は ae.safetensors を非商用ゲート付きの FLUX.2-dev から取り、さらに klein でも Mistral-Small-3.2-24B を mod 判定/アップサンプリング用に常時ロードする。結果として 4B を試すだけでも HF ログインと 24B 分のメモリが要る。⑤ 直近30日 commit 0、最終 push 2026-03-12。一方 HF 側の重みは 2026-02〜03 に更新されており、新しい派生や diffusers 側の対応はこの repo の外で進む。⑥ cli.py は torch.device('cuda') 固定で CPU/MPS 経路が無い（cpu_offloading も CUDA 前提）。⑦ 蒸留モデルは guidance / num_steps の上書きを拒否する。⑧ 商用の本番利用は BFL の商用ライセンスが別途必要（非商用定義は「商用主体の非本番環境での評価・研究」までを許す）。⑨ 透かし埋め込みと C2PA は推奨のみで、cli.py の embed_watermark 呼び出しはコメントアウトされている。"
forks: 220
open_issues: 43
commits_30d: 0
size_kb: 46457
archived: false
commits_90d: 0
commit_cadence: stale
fetched_at: "2026-11-07T05:24:50Z"
---

# FLUX.2 — 4BはApache-2.0、9Bと[dev]は非商用という二重構造の画像生成・編集推論コード

## 出来ること

- テキスト→画像、単一参照画像の編集、複数参照画像の編集を1つのモデルで扱う（全バリアント共通）
- klein 4B / 9B / 9B KV は guidance・timestep 蒸留済みで 4 step 生成。README は「最新ハードで1秒未満」とうたう
- klein 9B KV は KV キャッシュ（docs/flux2_klein_kv_cache.md）で、複数参照の編集では 4B より速いとされる
- klein 4B Base / 9B Base は蒸留なしの 50 step。ファインチューニングと LoRA 学習向け
- FLUX.2 [dev] は 32B の flow matching transformer。品質優先枠で、単一参照・複数参照の編集も可
- 対話 CLI（scripts/cli.py）でモデル選択、プロンプト、参照画像、シード、解像度（既定 1360x768）を指定
- --cpu_offloading で transformer をステップ間だけ CPU に退避
- プロンプトのアップサンプリングをローカル（Mistral-Small-3.2-24B-Instruct-2506）か OpenRouter 経由で実行
- 出力は EXIF に "AI generated;flux2" を書き込み、モデル側の mod フィルタが flag した画像は保存しない

## 目的・背景

- Black Forest Labs のオープンウェイト配布用リポジトリ。2025-11-25 に FLUX.2 [dev]（32B）、2026-01-15 に klein ファミリを公開
- 位置づけは「最小限の推論コード」。学習・量子化・サービングの仕組みは含まず、ホスト型 API（docs.bfl.ai）に対するローカル実行の参照実装という立ち位置
- klein は速度と VRAM のパレート frontier を狙った系列で、consumer GPU と edge 配置が主眼。dev は遅延を許容して品質を取る枠
- ライセンス設計は明確に二層。4B を Apache-2.0 で開放して組み込み・商用の入口を作り、9B 以上は非商用に留めて商用契約へ誘導する
- autoencoder（ae.safetensors）は Apache-2.0 で別配布。モデル本体のライセンスとは独立している

## 依存関係

- Python >=3.10,<3.13（README の検証は 3.12、GB200 + CUDA 12.9）
- torch==2.8.0 / torchvision==0.23.0 / transformers==4.56.1 / einops==0.8.1 / safetensors==0.4.5 / fire==0.7.1 / openai==2.8.1 / accelerate==1.12.0（すべて pyproject.toml で固定）
- diffusers は repo の依存に入っていない。量子化した [dev] を 4090 で動かす手順（docs/flux2_dev_hf.md）でのみ外部から使う
- テキストエンコーダはモデル毎に別途取得。klein は Qwen3-4B-FP8 / Qwen3-8B-FP8、[dev] は Mistral-Small-3.2-24B-Instruct-2506
- klein でも CLI は Mistral-Small-3.2-24B を mod 判定兼アップサンプリング用に読み込む
- 重みは Hugging Face から取得。ae.safetensors は black-forest-labs/FLUX.2-dev（ゲート付き）に置かれている

## 実行条件

- ライセンス: klein 4B（蒸留）と klein 4B Base の重みが Apache-2.0、HF 上もゲートなし。klein 9B / 9B KV / 9B Base / [dev] は FLUX Non-Commercial License で、HF 側は gated=auto（規約同意とトークンが要る）
- 非商用の定義は「直接・間接の対価を得ない利用」で、営利企業でも非本番環境での評価・非商用 R&D は含まれる。本番商用は別途 BFL の商用ライセンス
- 出力の所有権は BFL が主張しない旨がライセンスに明記されている
- README の記載: klein 4B は約 8GB VRAM（RTX 3090/4070 以上）に収まる。ただしこれは transformer 単体の話で、Qwen3 と Mistral-24B は別枠
- [dev] の同梱スクリプトは H100 相当の GPU を前提とし、4090 向けには量子化版＋リモートのテキストエンコーダという構成が案内されている
- HF トークン: 4B 本体は不要だが、ae.safetensors が非商用ゲート付き repo にあるため CLI の自動ダウンロード経路では結局ログインが要る
- CUDA 必須。cli.py は cuda デバイスを固定で使い、--cpu_offloading も CUDA 前提

## 最短手順

```bash
git clone --depth 1 https://github.com/black-forest-labs/flux2.git && cd flux2
python3.12 -m venv .venv && source .venv/bin/activate
pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --no-cache-dir

# ae.safetensors がゲート付き repo にあるため、規約同意後にログイン
hf auth login

# 対話モード（モデルを番号か名前で選択）
PYTHONPATH=src python scripts/cli.py

# 非対話で 4B を 1 枚だけ生成
PYTHONPATH=src python scripts/cli.py --model_name flux.2-klein-4b \
  --prompt "a photo of a forest with mist" --single_eval

# 参照画像つき編集（複数指定可）
PYTHONPATH=src python scripts/cli.py --model_name flux.2-klein-9b-kv \
  --input_images ref1.png --input_images ref2.png --prompt "same scene at night" --single_eval
```

- 重みを事前に落としている場合は FLUX2_MODEL_PATH / AE_MODEL_PATH / KLEIN_4B_MODEL_PATH などの環境変数で場所を指定できる（未設定なら自動ダウンロード）
- 選べる名前は src/flux2/util.py の FLUX2_MODEL_INFO が正: flux.2-klein-4b / flux.2-klein-9b / flux.2-klein-9b-kv / flux.2-klein-base-4b / flux.2-klein-base-9b / flux.2-dev
- 蒸留モデルは既定の num_steps=4, guidance=1.0 から変えると起動時に弾かれる

## 変更履歴

- 2026-11-07: 初回登録
