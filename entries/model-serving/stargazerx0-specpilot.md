---
type: "repo"
name: "SpecPilot"
genre: "model-serving"
url: "https://github.com/StargazerX0/SpecPilot"
author: "StargazerX0"
repo: "StargazerX0/SpecPilot"
license: "Apache-2.0"
stars: 169
language: "Python"
created: "2026-11-02"
updated: "2026-11-03"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/ai_hakase_/status/2118149307970867503"]
flags: []
risk_notes: "H100 80GB SXM5（sm_90）または RTX PRO 6000 Blackwell（sm_120a）の実機専用で、CUDA カーネルはこの2アーキ向けにビルドされるため他 GPU・CPU では動かない。リリース・タグが無く（/releases/latest は 404）、main 1ブランチ・コミットは初回の1件（2026-11-02）のみなので、バージョン固定はコミット SHA でしか行えない。配布物は自律探索ループ本体ではなく、そのループが発見した6デプロイ分の最終エンジンと検証スクリプト（探索フレームワークの公開予定は issue #2 で未回答）。初回起動は CUDA/Triton/DeepGEMM の JIT コンパイルで、README 自身が初回計測が 10–15% 遅いと注記しており warm-up が必須。"
forks: 9
open_issues: 2
commits_30d: 1
commit_cadence: "unknown"
size_kb: 8531
archived: false
fetched_at: "2026-11-06T19:46:05Z"
last_release: ""
last_release_at: ""
---

# SpecPilot — 投機的デコーディングをデプロイ毎に最適化した推論エンジン群（SGLang ベース / OpenAI 互換）

## 出来ること

- 投機的デコーディング構成6通り（Qwen3.8-27B BF16 + DFlash2 / + DSpark を H100 と RTX PRO 6000 で、Qwen3.8-27B FP8 の batching 2通り、Muse-Glimmer-30B + DFlash2）について、最適化済みエンジン（settings/<setting>/files/ を stock エンジンに重ねたもの）と stock（未最適化の DFlash2/DSpark）・AR（自己回帰）を同一サーバー条件で比較できる。
- README の表では AR 比 8.86〜10.87倍（単一リクエスト4設定）、stock 比 1.93〜2.52倍。H100 の4設定は fresh clone からの再現値も別表で公開（8.91x / 9.48x / 3.96x / 3.91x、95% bootstrap CI 付き）。
- 最適化の中身は W12（BF16 重みを実測 12.01–12.02 bit/weight でストリームする可逆フォーマット、GEMM 内でレジスタ復号）、32ノードの wide draft tree verify、TLV（二段階検証）、certified exact-argmax LM head、L2 weight prefetch、ragged draft tree など。設定ごとの内訳は settings/<setting>/README.md。
- SGLang を削った stock エンジン（python/、2688ファイル）と overlays/dspark_stock/ を持ち、scripts/build_engine.py が設定ごとのエンジンツリーを組み立てて内容ハッシュを出力する。
- 起動したサーバーは SGLang HTTP と OpenAI 互換 API を 127.0.0.1:<port> で喋るので、エージェントやクライアントから model 名 qwen3.8-27b でそのまま呼べる。
- 検証まで一式: bench.sh（論文の workload、per-request の tokens/latency/verify steps/output ids を記録）、compare.py speed（速度比・τ・出力一致を bootstrap CI 付きで算出）、score.py（gsm8k/math500 は \boxed{}、humaneval/mbpp はサンドボックスでテスト実行）。

## 目的・背景

- リリース済みの投機的デコーディング実装は速度を使い切れておらず、最適な修正はデプロイごとに異なる。SpecPilot はコストモデルで現在の系と上限の差を特定し、並列エージェントが方向を探索・統合、カーネル担当サブエージェントが帯域上限から最も遠いカーネルを調整する自律ループで、学習なし・lossless の最適化を発見する（README / arXiv:2611.02501）。
- lossless の担保は「greedy で target モデルが毎トークン決める」ことと、コミットした全トークンを stock と突き合わせる token forcing。README は AR とビット単位一致しない点（verify 時の batched GEMM/attention の reduction 順が違うため near-tie が反転しうる）も明記している。
- 本リポジトリが配るのは探索の結果（6デプロイ分の最終エンジン）であって探索ループ本体ではない。エージェント側の公開予定は issue #2「Plans to release the agent framework and prompts?」に未回答。
- 2026-11-02 作成、arXiv 論文と project page（stargazerx0.github.io/specpilot-project-page、40秒の概要動画）が同時公開。169 stars / 9 forks（取得時点）。

## 依存関係

- GPU: H100 80GB SXM5（sm_90）または RTX PRO 6000 Blackwell Server Edition 96GB（sm_120a）。1設定 = 1GPU（CUDA_VISIBLE_DEVICES で指定）。
- Python 3.11 + torch 2.13 / CUDA 13.0。パッケージは research/requirements.lock.txt で固定、setup_env.sh が uv で venv を作り stock エンジンを editable で入れる。R580 未満のドライバでは NVIDIA の cuda-compat-13-0 を取得して LD_LIBRARY_PATH に足す。
- モデル（Hugging Face、リビジョン固定）: Qwen/Qwen3.8-27B、Qwen/Qwen3.8-27B-FP8、z-lab/Qwen3.8-27B-DFlash2、RadixArk/Qwen3.8-27B-DSpark、meta-models/Muse-Glimmer-30B、incoai/Muse-Glimmer-30B-DFlash2。4件の HF リポジトリは API で 200 を確認済み。
- データ配置: SPECPILOT_DATA（既定 ~/specpilot_data）配下の shared/（venv・models・HF キャッシュ・CUDA compat・ビルドキャッシュ）と work/（組み立てたエンジン、ログ、bench 結果）。
- ライセンス: Apache-2.0（LICENSE 実体 11346 バイト）。python/ は SGLang（Apache-2.0）由来と README に明記。

## 実行条件

- 上記いずれかの GPU 実機が必須。カーネルは sm_90 / sm_120a 向けにビルドされ、README は「RTX PRO 6000 の final は sm_120a 専用、H100 の final は H100 で計測」と明記。CPU・AMD・他世代 NVIDIA では動かない。
- 初回に venv 構築とモデルダウンロード（27〜30B 級の target + drafter）、さらに初回起動時に CUDA/Triton/DeepGEMM カーネルの JIT コンパイルが走る。README の IMPORTANT で「各エンジンの初回ブート後に一度 benchmark を回してから計測する（batching final は初回 16 リクエストで 10–15% 遅かった）」と指示されている。
- リリース・タグが無く（/releases/latest は 404）、main 1ブランチ・コミット1件（初回 import、2026-11-02）。再現性はコミット SHA 78c42af で固定するしかない。
- bench は HF の dev split（gsm8k / humaneval / math500 / mbpp / mt-bench）と greedy・2048 new tokens を前提にし、single-request 設定は各 suite 先頭6件（ITEMS=20 で全100件）、batching 設定は 16/20/24 並列。
- Muse 設定は chat template がシステムプロンプトに現在日付を書くため、比較する全 arm を同一 UTC 日内に実行する必要がある。
- サーバーは 127.0.0.1 バインドで起動し、torch.distributed の store は port+1 を使う（scripts/stop.sh <port> で停止）。並列起動は research/autoresearch/cudaslot.py のマシン全体スロットで直列化される。

## 最短手順

- 1. 取得と環境構築: git clone https://github.com/StargazerX0/SpecPilot && cd SpecPilot && bash scripts/setup_env.sh
- 2. 重み取得（設定単位、または all）: bash scripts/download_models.sh h100_c1_qwen38-27b_dflash2
- 3. 起動: bash scripts/serve.sh h100_c1_qwen38-27b_dflash2 final 0 → 127.0.0.1:30000 で待ち受け（第2引数を stock / ar にすると同じ設定の比較対象が立つ）
- 4. AI から呼ぶ（OpenAI 互換）: サーバー起動中に base_url http://127.0.0.1:30000/v1、model 名 qwen3.8-27b（= HF 名の小文字、SERVED_MODEL_NAME）で叩く。例: curl -s http://127.0.0.1:30000/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"qwen3.8-27b","messages":[{"role":"user","content":"hello"}],"max_tokens":64}' 。疎通確認は http://127.0.0.1:30000/health 。
- 5. 計測と比較: bash scripts/bench.sh h100_c1_qwen38-27b_dflash2 final-1 0（結果は $SPECPILOT_WORK/bench/final-1.json）、続けて stock-1 / ar-1 を取り、cd $SPECPILOT_WORK/bench && python3 ~/SpecPilot/scripts/compare.py speed --ar ar-1.json --stock stock-1.json --final final-1.json、python3 ~/SpecPilot/scripts/score.py final-1.json stock-1.json。
- 6. 停止: bash scripts/stop.sh 30000

## 変更履歴

- 2026-11-06: 初回登録
