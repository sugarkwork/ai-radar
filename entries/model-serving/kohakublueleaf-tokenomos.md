---
type: "repo"
name: "Tokenomos"
genre: "model-serving"
url: "https://github.com/KohakuBlueleaf/Tokenomos"
author: "KohakuBlueleaf (Shih-Ying Yeh)"
repo: "KohakuBlueleaf/Tokenomos"
license: "Apache-2.0"
stars: 26
language: "Python"
created: "2026-10-31"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/KBlueleaf/status/2116459910347313274"]
flags: []
risk_notes: "README の高速化数値（stock vLLM 比 2.2–4.8x 等）は作者自身の bench/ スクリプトと reports/ に基づく主張で、独立検証は確認していない。NVIDIA GPU（sm70〜sm120）と CUDA ドライバが必須で、CPU では動かない。tokenomos._rs のビルドに Rust toolchain が要る。初版 v0.0.1（2026-10-31）から日が浅く、API/引数は変わりうる。MCP サーバや Agent Skill は提供されておらず、連携は OpenAI 互換 HTTP と Python API のみ。"
forks: 0
open_issues: 0
commits_30d: 20
commit_cadence: "daily"
size_kb: 3299
archived: false
fetched_at: "2026-11-06T11:38:26Z"
last_release: "v0.0.1"
last_release_at: "2026-10-31"
---

# Tokenomos — 小型VLM向けのローカル推論エンジン（OpenAI互換サーバ付き）

## 出来ること

- 小型VLM（LFM3-VL 2B / Qwen3.5 4B・9B / Qwen3.8 27B / Gemma 4 E4B・12B・31B）を1枚のNVIDIA GPUでローカル推論する。
- OpenAI互換HTTPサーバを立てられる: POST /v1/chat/completions、POST /v1/completions、GET /v1/models、GET /health。stream でSSE、response_format の json_schema で出力をスキーマに拘束できる。
- 複数GPUを1ポートに束ねるルータ（python -m tokenomos.api.router --gpus 0,1,2,3）を持つ。
- Pythonから直接使うAPI（tokenomos.LLM / SamplingParams / models.configure）があり、チャット・生成・ストリーミング・JSONスキーマ拘束を呼べる。
- 量子化バックエンドを選択できる: bf16 / fp16 / fp32、MXFP8・NVFP4・FP8、INT8 W8A8（rotate 付き）。対応カードは sm70（Tesla）〜sm120（RTX 5090）。
- スケジューリング・KVページ管理・サンプリング・文法・終了判定をCUDAグラフ内のカーネルに載せ、ホスト側の1ステップあたり作業をバッチ数に依らずほぼ一定にする設計（README の主張）。

## 目的・背景

- 一般的なサービングエンジンは各デコードステップでホストが行のスケジューリング・トークン読み出し・停止判定・次ステップ入力書き込みを行い、そのコストが行数に比例してGPUを待たせる。
- Tokenomos はこれらの行単位の判断をデバイス側カーネルへ移し、ホストは次ステップをキューして1ステップ前のイベントを読むだけにして、GPUを遊ばせないことを狙う。
- 対象は「GPUが唯一のボトルネックになる」小型VLMの高スループット推論（画像キャプション的な大量バッチ処理を含む）。投稿の「数倍速い」という表現は README のベンチマーク主張であり、独立検証は本項目では行っていない。

## 依存関係

- Python 3.12 以上。
- torch>=2.11、torchvision、triton>=3.5（Windows では triton-windows>=3.5）、safetensors>=0.4、numpy>=2、tokenizers>=0.21。
- 任意extra: gpu = flashinfer-python>=0.6（Linux・sm90以上、MXFP8/NVFP4 GEMMとGDN prefill）、tensorcore = tilelang>=0.1.15（W8A8・fp16経路・sm70のmatmul。nvcc とホストCコンパイラが必要）。
- ビルドに Rust toolchain と maturin（拡張 tokenomos._rs を maturin develop --release でビルド）。
- NVIDIA GPU（sm70 以上）と対応する CUDA ドライバ。Linux または Windows 11。

## 実行条件

- NVIDIA GPU が必須（CPU推論の経路はない）。README の検証カードは RTX 5090 / 4090 / 3090 / 2080 Ti / Tesla PG503-216。
- HF形式のチェックポイントをローカルに用意する（例 /models/lfm3-vl-2b-mxfp8）。量子化ヘッドを使う場合は該当フォーマットの重みが必要。
- VRAM に余裕が要る。README の例では 4B 級を 19GiB 上限で回すため kv_leave / kv_reserve を調整している。
- Linux で MXFP8/NVFP4 を使うには sm100 以上（RTX 5090 等）、FP8 は sm89 以上、bf16 は sm80 以上。古いカードでは fp16/fp32/W8A8 に落ちる。
- 初回はソースからのビルド（uv pip install -e）と Rust 拡張のビルドが走るため、コンパイラ類が必要。

## 最短手順

- git clone https://github.com/KohakuBlueleaf/Tokenomos && cd Tokenomos
- uv venv -p 3.12 && uv pip install -e ".[gpu,tensorcore,dev]"（torch はドライバに合うインデックスから入れる）
- maturin develop --release  # Rust 拡張 tokenomos._rs をビルド
- python -m tokenomos.api.server --model /models/lfm3-vl-2b-mxfp8 --port 8000 --arch-kw '{"head": "mxfp8"}'
- AI/エージェントからは OpenAI 互換で叩く: curl -s http://localhost:8000/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"lfm3-vl-2b","messages":[{"role":"user","content":"hello"}],"max_tokens":64}'
- Python から使う場合: from tokenomos import LLM, SamplingParams, models; arch = models.configure(path, head="mxfp8"); with LLM(path, arch=arch, max_len=8192) as llm: llm.chat(conversations, SamplingParams(max_tokens=1024))
- スキーマ拘束は SamplingParams(max_tokens=64, json_schema=schema) を渡す。停止文字列は非対応で、stop_token_ids を使う。

## 変更履歴

- 2026-11-06: 初回登録
