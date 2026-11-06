---
type: "model"
name: "Ripple-65B Preview"
genre: "other"
url: "https://huggingface.co/ricursiveAI/Ripple-65B-Preview"
author: "Ricursive Intelligence（ricursiveAI）"
pricing: "freemium"
pricing_detail: "重みは Apache-2.0 かつ gated=false のため無料・登録不要で取得可。ホスト型 API は OpenRouter 実測（2026-11-06T12:16Z）で入力 $0.20 / 出力 $0.60 / cache read $0.05（いずれも100万トークンあたり、GMICloud の bf16）。公式サイトに料金ページはなく /pricing と /ripple/pricing は 404。Together AI・Fireworks・GMI Cloud 各社の料金は未確認。"
signup_required: false
model: "ricursiveAI/Ripple-65B-Preview"
license: "Apache-2.0"
downloads: 2013
likes: 301
format: "safetensors"
size: "129.6GB（BF16、HF API usedStorage）"
created: "2026-11-04"
updated: "2026-11-06"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://www.ricursive.com/ripple", "https://huggingface.co/ricursiveAI/Ripple-65B-Preview", "https://openrouter.ai/ricursiveai/ripple-65b-preview", "https://x.com/KBlueleaf/status/2116459910347313274"]
flags: ["unverified"]
risk_notes: "ベンチマーク（TerminalBench 2.1 で 80.52、米国 open-weight SOTA 等）はすべて配布元の自己申告で第三者検証がない。モデルカードにローカル推論手順の記載はなく、実行手順はリポジトリ内 inference/server/README.md（2xB200 + SGLang 0.5.19 前提）のみで、DGX Spark 単機で動くという記述の実測裏付けはない。独自アーキテクチャ（custom_code、model_type=ricursive）のため transformers での自前ロードは未検証。OpenRouter の提供元は GMICloud 1 社のみで、2026-11-06T12:17Z 時点の status は -5・直近30分の uptime は 0（一時的な可能性あり）。発見源の X 投稿本文は Tokenomos（vLLM のスケジューラ／KV キャッシュ最適化）の公開告知で Ripple に言及がなく、対象との対応は投稿内リンクの展開に依存している。"
fetched_at: "2026-11-06T12:17:45Z"
---

# Ripple-65B Preview（65B dense・1M コンテキストのオープンウェイトモデル）

## 出来ること

- ローカル serving: リポジトリ同梱の inference/server/serve.py（SGLang 0.5.19 ベース）で OpenAI 互換の /v1/chat/completions を立てられる。tools / tool_choice による関数呼び出し、message.reasoning_content と message.content の分離、ストリーミングに対応し、最大 1,048,576 トークンのコンテキストを扱う。
- ホスト型 API: OpenRouter 経由で model="ricursiveai/ripple-65b-preview" として呼べる。エンドポイントは /api/v1/chat/completions、/completions、/messages、/responses で、tools・tool_choice・response_format・seed・logprobs・top_logprobs に対応。エージェントのバックエンドモデルとして差し替え可能。
- 重みの取得: Hugging Face の ricursiveAI/Ripple-65B-Preview から Apache-2.0・gated なしで取得できる。NVFP4 版、Base 版（pretrain のみ）、DFlash2 版が別リポジトリで公開されており、用途別に選べる。
- 仕様: 65B の dense Transformer（d_model 5120 / 80 層、MoE ではない）、12T トークンで事前学習、tools 対応 ChatML テンプレートを同梱。配布元は 2xB200 batch=8 で 250 tok/s と記載（自己申告・未検証）。
- 向く用途: 長いリポジトリ文脈を渡すコーディングエージェント、ツール呼び出しを伴う自動化。配布元は TerminalBench 2.1 で 80.52 と主張している（自己申告）。

## 目的・背景

- Ricursive Intelligence が、自社の AI チップ設計プラットフォームを支えるモデルの汎用版として公開した 65B パラメータのオープンウェイト LLM。12T トークンで事前学習し、thin-and-deep（狭い d_model 5120・80 層）の dense 構成を採る。
- 設計思想は「学習と serving のインフラ複雑性を下げる」こと。MoE ではなく dense を選び、独自カーネルや量子化なしの BF16 で学習している。パラメータ数が小さいぶん DGX Spark のような単機ローカル環境でも動かせる規模を狙っており、NVFP4 チェックポイントと Colab も用意するとカードに記載がある。
- カタログ上は、読者が自分のエージェントに組み込める実体（重み＋OpenAI 互換サーバ＋ホスト型 API）があるため「使える道具」に該当する。ただし発見源の X 投稿は Tokenomos の公開告知で、本モデルの紹介ではない。投稿は発見源に留め、事実は HF API と配布元ページで確定させた。

## 収録ファイル

- model-00001-of-00016.safetensors 〜 model-00016-of-00016.safetensors: BF16 のシャード重み。合計 64,782,689,360 パラメータ、HF の usedStorage は 129,565,519,472 バイト（約129.6GB）。
- model.safetensors.index.json: シャードのインデックス。
- config.json / configuration_ricursive.py / modeling_ricursive.py: model_type=ricursive の独自実装（custom_code）。transformers 標準のモデルクラスでは読めない。
- chat_template.jinja: tools に対応した ChatML テンプレート。reasoning と最終回答、tool_calls を分離して出力する。
- tokenizer.json / tokenizer_config.json / special_tokens_map.json: トークナイザ一式（OpenRouter 側の表記は tokenizer=Other）。
- inference/server/serve.py, model.py, ripple_format.py, README.md: SGLang 0.5.19 上で 2xB200 向けに起動するランチャと、reasoning / tool-call パーサ。
- LICENSE: Apache-2.0。兄弟リポジトリとして Ripple-65B-Preview-NVFP4、Ripple-65B-Base-Preview、Ripple-65B-Preview-DFlash2 が公開されている。

## 実行条件

- 重みのサイズは BF16 で約129.6GB（HF API 実測）。同梱手順の前提は 2 枚の NVIDIA B200（TP=2 が既定）で、これより小さい構成での動作は未検証。
- serve.py の実行には Linux、CUDA Toolkit 13、C++ コンパイラ、uv が必要（README 記載）。依存は uv が自動導入する。既定で --context-length 1048576、DFlash2 ドラフトは 16Ki トークン窓を使用。
- ホスト型 API を使う場合は OpenRouter のアカウントと API キーが必要。2026-11-06T12:17Z 時点で提供元は GMICloud 1 社のみ、status=-5・直近30分の uptime 0 のため、API 経由の可用性は保証されない。
- ライセンスは Apache-2.0（HF tags とカード記載が一致）。重みの取得自体は gated=false で登録不要。
- 独自アーキテクチャのため transformers での直接ロードは未検証。動かす場合は同梱の SGLang ベース手順を使うのが確実。

## 使い方

- ローカルで立てる場合（inference/server ディレクトリで実行、README のコマンド）:
```bash
export CUDA_HOME=/usr/local/cuda-13.0
export PATH="$CUDA_HOME/bin:$PATH"

CUDA_VISIBLE_DEVICES=0,1 uv run --script serve.py \
  --model-path /path/to/target \
  --speculative-draft-model-path /path/to/draft
```

- サーバは 127.0.0.1:30000 で待ち受ける。OpenAI 互換なので、既存クライアントの base_url を http://127.0.0.1:30000/v1 に向ければそのまま使える。
```bash
curl http://127.0.0.1:30000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"ripple","messages":[{"role":"user","content":"Hello"}],"max_tokens":128}'
```

- ツール呼び出しは OpenAI 形式の tools と tool_choice: "auto" を渡す。返ってきた assistant メッセージをそのまま履歴に戻し、tool_call_id と結果文字列を持つ tool メッセージを追加して再送する（テンプレートが同じトークンに再描画するため、メッセージを書き換えない）。
- ホスト型で試す場合は OpenRouter の OpenAI 互換エンドポイント（base_url https://openrouter.ai/api/v1、model ricursiveai/ripple-65b-preview）に API キーを付けて同じ形式で送る。

## 変更履歴

- 2026-11-06: 初回登録
