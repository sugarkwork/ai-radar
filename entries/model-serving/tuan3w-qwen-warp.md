---
type: "repo"
name: "qwen-warp"
genre: "model-serving"
url: "https://github.com/tuan3w/qwen-warp"
author: "tuan3w"
repo: "tuan3w/qwen-warp"
license: "MIT"
stars: 24
language: "Python"
created: "2026-11-01"
updated: "2026-11-09"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/ai_hakase_/status/2118149307970867503"]
flags: ["unverified"]
risk_notes: "元投稿が解説する「SpecPilot」(W12・ツリー検証・自律エージェント探索・4.46x→10.87x)は別リポジトリ StargazerX0/SpecPilot の内容で、本リポジトリは返信スレッドに別リンクとして挙がっているだけ。本リポジトリの速度・品質数値は作者が RTX 3090 1枚で自己計測したもので第三者検証はない(stars 3/forks 1、作成から5日)。RTX 3090(sm_86)専用で他の GPU は未テスト、同時1リクエストのみ、logprobs/structured output/bad_words は HTTP 400、モデル重みは別ライセンス(swift-open-license-1.0, gated)でリポジトリの MIT 対象外、エージェント多ターンの成功率は未計測と README に明記。"
forks: 4
open_issues: 2
commits_30d: 100
commit_cadence: "daily"
size_kb: 4919
archived: false
fetched_at: "2026-11-09T21:40:34Z"
last_release: "v0.9.1"
last_release_at: "2026-11-09"
commits_90d: 100
---

# qwen-warp — RTX 3090 1枚で Qwen3.8-27B を 262k コンテキスト・OpenAI 互換 API で動かす推論エンジン

## 出来ること

- RTX 3090 1枚で Qwen3.8-27B の INT4 チェックポイントを動かし、OpenAI 互換の HTTP API を :8000 に公開する。中身は vLLM 0.30.0 の OpenAI フロントエンドで、モデル名は `swift`、ルートは `/health`・`/v1/models`・`/v1/chat/completions`・`/v1/completions`(docs/USAGE.md「Endpoints」)。
- 262,144 トークンのコンテキストを 24GB の VRAM に収める。4-bit KV キャッシュ(トークンあたり 16.5KiB、bf16 は 64KiB)と、embedding/スコアリング用テーブルをホストの pinned メモリへ逃がす `--host-tables` による。`--profile long` で 196,608、`--max-model-len 262144 --prompt-lookup 0` で全長(README「Quick start」の表)。
- チェックポイント内蔵の MTP draft head が3トークン/ステップを提案し、1パスで検証する投機的デコーディング。greedy でもサンプリングでも出力分布は exact と README が主張。`--drafter dflash2` で別ドラフタも選べる(greedy のみ、実験的)。
- prompt lookup(プロンプト内の繰り返しを利用)と prefix reuse(同一会話の前ターンの prefill を省略)。長文エージェントの2ターン目以降を速くする狙い。
- サンプリングは temperature / top_p / top_k(1〜64) / min_p / presence・frequency・repetition_penalty / logit_bias / min_tokens / allowed_token_ids / seed / max_tokens / stop / n に対応。logprobs・bad_words・structured output・thinking_token_budget は HTTP 400 で明示的に拒否される(パラメータ名を返す)。
- `--api-key KEY` で Bearer 認証、Docker では `/health` のヘルスチェックと `unless-stopped` の再起動ポリシー付き。テストは `make test`(GPU と重みが必要)。

## 目的・背景

- 作者(tuan3w)が自分の RTX 3090 で Qwen3.8-27B を最大限使うための個人向け推論エンジン。汎用 serving ではなく「1 GPU・1モデル・1リクエスト・テキストのみ」に意図的に絞っている(README 冒頭)。
- 比較対象は HyperQwen(syv-ai/hyperqwen)。同一カード・同一日・同一プロンプトで測り、190k トークンのプロンプトで 102 tok/s、HyperQwen の 200k preset(28 tok/s)の 3.6 倍と README に記載。数字はすべて作者の自己計測で、第三者による再現は確認できない。
- 2026-11-01 作成、2026-11-06 までに v0.2.0〜v0.7.0 の6リリース。30日コミットは 91 件と開発は速いが、stars 3 / forks 1 で外部からの検証・利用実績はまだほとんどない。
- 重要: 元投稿が解説しているのは「SpecPilot」(自律エージェントで投機的デコーディングを最適化するフレームワーク)であり、W12 12-bit 重み・ツリー検証・4.46x→10.87x といった数値は本リポジトリの実装ではない。投稿の返信スレッドで SpecPilot とは別に qwen-warp のリンクが挙がっており、本項目はその後者だけを扱う。
- README は未計測項目(マルチGPU、他電力設定、エージェント多ターンの成功率、同時接続)を明示する方針で書かれており、誇張は少ない。

## 依存関係

- GPU: RTX 3090(24GB)。カーネルは sm_86 向けにビルドされ、他の GPU は未テストと明記。
- OS/ドライバ: Linux、NVIDIA ドライバ 580 以上。
- Docker 経路: Docker Engine + NVIDIA container toolkit。イメージは約24GB(コードとコンパイル済みエンジンのみ、重みはマウント)。
- ネイティブ経路: CUDA toolkit 13.0(13.0 のみ検証)、uv、gcc/build-essential。`make setup` はクリーンなマシンで約27分。
- モデル: Hugging Face の `ukisai/Swift-1.5-Qwen3.8-27b-INT4`(gated、約19GB、ライセンスは `swift-open-license-1.0` でリポジトリの MIT 対象外)。事前にライセンス同意と `hf auth login` が必要。
- ホスト RAM: 長文プロファイルで約5GiB の pinned メモリ(テーブル4.7GiB + スナップショット)。ディスク: 重み19GB + ネイティブ環境 約8GB / Docker イメージ 約24GB。
- Python 依存は uv.lock で固定(vLLM 0.30.0、torch は cu130 ビルド)。vLLM を手動で上げるとエンジンが壊れると README が警告。

## 実行条件

- RTX 3090 実機が必須。CI・クラウドの別 GPU・CPU では動かない(カーネルが sm_86 専用)。
- 起動時に空き VRAM を実測し、`--max-model-len` が収まらなければ約10秒で「収まる長さ」を示して拒否する。デスクトップが約0.6GiB 使う前提の数値なので、他の GPU ジョブは先に止める。
- 同時に処理できるのは1リクエストのみ(残りはキュー)。連続バッチングと画像入力は PR #6 が open で未マージ。
- 初回の長文プロンプトは prefill に時間がかかる(190k で約3分、262k で約4.5分)。2ターン目以降は prefix cache で短縮。
- logprobs・structured output(JSON schema)・bad_words に依存するワークフローには使えない(HTTP 400)。ツール呼び出しは動くが、最小スキーマで well-formed 率 92%(n=200、README)。
- 速度・品質の数値は作者の単一カード計測。エージェントの多ターン成功率は未計測と README に明記されており、導入判断は自己責任。

## 最短手順

- 1. 重みを取得(要 HF ログインとライセンス同意): `uvx --from huggingface_hub hf auth login` → `uvx --from huggingface_hub hf download ukisai/Swift-1.5-Qwen3.8-27b-INT4 --local-dir ~/models/swift-1.5-int4`
- 2. 起動(Docker): リポジトリ直下で `docker compose up --build`。既定で `--profile long`(196,608 コンテキスト)のまま :8000 に立つ。
- 3. 起動(ネイティブ): `make setup` → `uv run server/serve.py --profile long --port 8000`
- 4. 動作確認: `curl localhost:8000/health`(200)、`curl localhost:8000/v1/models`(served name は `swift`)、`curl localhost:8000/v1/chat/completions -H 'content-type: application/json' -d '{"model":"swift","messages":[{"role":"user","content":"Say hello."}],"max_tokens":1000}'`
- 5. AI から呼ぶ: サーバーは OpenAI 互換なので、エージェントやクライアントのプロバイダ設定を base_url `http://localhost:8000/v1`、model `swift`、api_key は任意値(`--api-key` を付けた場合のみ検証)に向ける。README は「OpenAI API を話すツールなら何でも動く」と明記し、コンテキスト長は起動時の値(`--profile long` なら 196,608)を設定する。
- 6. 全長 262,144 を使う場合: `--profile long --max-model-len 262144 --prompt-lookup 0`(`EXTRA_ARGS` でも可)。思考トークンが `max_tokens` を食うので、切れる場合は `"chat_template_kwargs": {"enable_thinking": false}` を付ける。

## 変更履歴

- 2026-11-06: 初回登録
