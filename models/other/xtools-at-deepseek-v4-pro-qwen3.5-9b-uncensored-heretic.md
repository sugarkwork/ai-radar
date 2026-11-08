---
type: model
model: xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
name: DeepSeek-V4-Pro-Qwen3.5-9B UNCENSORED（Heretic ARA）
genre: other
url: https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
author: xtools-at（表示名 Colonel Panic）
license: Apache-2.0
base_model: [Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B, unsloth/Qwen3.5-9B]
format: safetensors
size: "BF16 4分割＋mtp 計19.31GB／第三者GGUF Q4_K_M 5.63GB"
downloads: 1369
likes: 564
created: 2026-10-30
updated: 2026-11-08
pricing: free
pricing_detail: "重み無料（Apache-2.0）。上流のQwen3.5-9BとJackrong版もApache-2.0、教師のDeepSeek-V4-ProはMIT。Heretic本体はAGPL-3.0（ツール側）。"
signup_required: false
added: 2026-11-08
first_seen: 2026-11-07
source_post: https://x.com/EngMoElgaraihy/status/2118905683261128755
sources: ["https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic", "https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B", "https://huggingface.co/mradermacher/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF", "https://x.com/nahid_pro09/status/2118896473119318363"]
flags: ["unverified", "low-quality"]
risk_notes: "モデルとライセンスは実在（HF APIで2026-11-08に確認: DL 1,369・likes 564・apache-2.0・Qwen3_5ForConditionalGeneration）。ただし投稿の主張は未検証か誤りを含む: 『Hugging Faceのサーバーが落ちた』は障害記録がなく誤り。『拒否率100/100→3/100』『KL 0.0422』『25万点蒸留』『知能を1点も失わない』はモデルカードの自己申告で第三者追試なし。カードのGSM8K 94.50%/MMLU-Pro 90.53%は拒否除去前のJackrong版の数字で、heretic版の能力評価は未提出。公式リポジトリはBF16のみでGGUFは第三者変換。そのQ4_K_M 5.63GBは変換時点でconfig.jsonのmtp_num_hidden_layers=1と実ウェイトが食い違い、llama.cppがGGML_ASSERTで落ちる（作者が11/08にMTPテンソルを復元したが再量子化は未実施）。『どの端末でも数秒』は誇張で、CPUのみは変換者計測で約1 t/s。同名の非公式再アップロードが複数あり、クローンからの取得は避ける。当方でGPU推論・llama.cpp実行は未実施（runs_verified=false）。"
fetched_at: "2026-11-08T06:40:00Z"
---

# DeepSeek-V4-Pro-Qwen3.5-9B UNCENSORED（Heretic ARA）

## 出来ること

- Qwen3.5-9B をベースに、DeepSeek-V4-Pro の推論を約25万件の数学・STEMサンプルで蒸留した `Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B` に対し、Heretic v2.0.0.dev0 の **ARA（Arbitrary-Rank Ablation）** を適用して拒否方向を除去した重み。
- 画像入力にも対応する `Qwen3_5ForConditionalGeneration`（image-text-to-text）。テキスト生成・会話・reasoning 用。
- 公式配布は **BF16 safetensors 4分割＋mtp、計19.31GB**。GGUF は無く、`mradermacher` による Q4_K_M 変換（5,629,111,968 B = 5.63GB / 5.24GiB）が第三者が公開している。
- 追加学習はしていない。Heretic は重みの方向を直接編集するツールで、この版自体に SFT/RL は入っていない。

## 目的・背景

- 「拒否傾向を消しても知能を落とさない」という Heretic の主張を、9B の実用モデルで試した派生版。ARA パラメータ（start_layer_index=9、end_layer_index=24、preserve_good_behavior_weight=0.8264、steer_bad_behavior_weight=0.0003 など）がモデルカードに公開されている。
- 2026-10-30 公開、2026-11-08 時点で DL 1,369・likes 564。投稿者は「HFが落ちるほど拡散」と表現したが、これは確認できない。
- ライセンスは Apache-2.0。上流2段も Apache-2.0、教師の DeepSeek-V4-Pro は MIT の公開重みなので、閉鎖API蒸留の規約問題は生じない。

## 収録ファイル

- `model-0000x-of-00004.safetensors` ほか BF16 4分割、`mtp.safetensors`（775キー中 mtp 15個）、`config.json`、tokenizer、chat template。
- 第三者 GGUF: `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q4_K_M.gguf`（5.63GB）＋ vision 用 `mmproj`（約0.62GB）。

## 実行条件

- BF16 版は 19.31GB の重み＋KV キャッシュ。16GB VRAM 単体には収まらず、CPU offload か量子化が必要。
- GGUF Q4_K_M は 5.63GB。8Kコンテキストの KV を概算1.2GBとして合計約7.5GBで、**8GB VRAM はぎりぎり、12GB で快適**。CPUのみは変換者計測で約1 t/s（i5-9300H）。
- **2026-11-08 時点の GGUF は動かない可能性が高い**: 10/31 変換時点で `config.json` の `mtp_num_hidden_layers=1` と実ウェイトが食い違い、llama.cpp がロード時に `GGML_ASSERT` で落ちる。作者は 11/08 03:36 に MTP テンソルを復元したが、量子化ファイルの再生成は未実施（月曜確認予定）。急ぐなら BF16 版を使う。
- 成人向け・違法用途は各法域の法律と配布元の規約に従う。脱検閲モデルであること自体が利用許諾を広げるわけではない。

## 使い方

```bash
# 公式 BF16（要 transformers / GPU メモリ確保）
hf download xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic \
  --local-dir models/heretic-9b

# 第三者 GGUF（ロードできるかは上記の MTP 問題を確認）
hf download mradermacher/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-GGUF \
  --include "*Q4_K_M.gguf" --include "*mmproj*" --local-dir models/heretic-9b-gguf
llama-cli -m models/heretic-9b-gguf/*Q4_K_M.gguf -p "Hello"
```

## 注意点（未確認・誇張）

- **「Hugging Face のサーバーが落ちた」は誤り。** 障害記録はなく、DL規模（本体1,369＋GGUF合計約9万）でも説明できない。
- **「拒否率 100/100 → 3/100」「KL 0.0422」「25万点蒸留」は自己申告。** 3/100 は Heretic 既定の100プロンプトを著者が回した数値で、プロンプト集合は非公開。独立追試はない。
- **「知能を1点も失わない」「プログラミングで優越」は根拠なし。** カードの GSM8K 94.50% / MMLU-Pro 90.53% は拒否除去前の Jackrong 版の数字で、heretic 版のベンチは未提出。カード自身も「コード教師データなし・向上は小幅かつ予備的」と明記している。
- **「どの端末でも数秒」は誇張。** CPUのみでは約1 t/s。
- 同名の非公式再アップロードが11/07以降に複数出現（DL 0）。公式に pickle 形式はないが、クローン経由の供給網リスクは残る。公式リポジトリと `mradermacher` 以外から取らない。
- 当方で GPU 推論・llama.cpp 実行は未実施。動作確認は利用者側で行うこと。

## 変更履歴

- 2026-11-08: 初回登録（「保留」扱いだったものを、未確認範囲を明示して収録）
