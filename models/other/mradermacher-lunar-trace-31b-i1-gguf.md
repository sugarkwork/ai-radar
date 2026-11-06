---
type: "model"
name: "Lunar-Trace-31B (i1 GGUF)"
genre: "other"
url: "https://huggingface.co/mradermacher/Lunar-Trace-31B-i1-GGUF"
author: "mradermacher"
pricing: "free"
pricing_detail: "Hugging Face から無料ダウンロード。実行はローカル(llama.cpp / Ollama / LM Studio 等)で、API 課金は無し。"
signup_required: false
model: "mradermacher/Lunar-Trace-31B-i1-GGUF"
license: "apache-2.0"
downloads: 1035
likes: 0
format: "gguf"
size: "18.7GB (i1-Q4_K_M) / 7.2-25.2GB・23量子化"
base_model: ["Cyclone-Labs/Lunar-Trace-31B"]
created: "2026-11-04"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/HuggingModels/status/2118374284120949020"]
flags: []
risk_notes: "ライセンスは配布元・元モデル・上流 gemma-4-31B-it のいずれも apache-2.0 表記で一致するが、マージ元の一つ TeichAI/gemma-4-31B-it-Claude-Opus-Distill-v2 は Claude Opus 出力による蒸留データセット由来で、その学習データの権利関係は各リポジトリの apache-2.0 表記だけでは確認できない。カードにベンチマーク・評価結果の記載は無く、公開から2日・likes 0 の新規リポジトリ。元モデルのカードは『プロンプトで要求していないのに暗い心理的テーマに寄る傾向がある』と自作テストで言及しており、用途によっては内容の抑制が必要。vision 対応を謳うが本リポジトリに mmproj は含まれず、画像入力には別リポジトリ mradermacher/Lunar-Trace-31B-GGUF の mmproj ファイルが要る。推奨量子化でも 18.7GB のファイルと相応の RAM/VRAM を要する。"
fetched_at: "2026-11-06T08:38:08Z"
---

# Lunar-Trace-31B i1 GGUF — ロールプレイ/創作向け31Bをローカル実行する量子化版

## 出来ること

- Gemma-4-31B-it を土台に4モデルをマージした31Bモデルを、量子化してローカルで動かせる(チャット・ロールプレイ・創作・長編ストーリー)
- IQ1_S(7.2GB)からQ6_K(25.2GB)まで23種の量子化が揃い、GPU メモリや RAM に合わせて精度とサイズを選べる
- imatrix(重要度行列)を使った i1 量子化で、同サイズの静的量子化より品質を保ちやすい
- コンテキスト長 262144 トークン(gemma4 アーキテクチャ)で長い会話・長編の続きを扱える
- llama.cpp / Ollama / LM Studio / KoboldCpp など GGUF 対応ランタイムでそのまま読み込める
- 量子化の作り直しや自分用チューニングのため imatrix ファイル(Lunar-Trace-31B.imatrix.gguf)も同梱

## 目的・背景

- 元モデル Cyclone-Labs/Lunar-Trace-31B は 2026-10-30 公開のマージモデル。google/gemma-4-31B-it を base に、Starlight-Synthesis-31B・G4-LuneLight-31B・gemma-4-31B-it-Claude-Opus-Distill-v2 を mergekit の mdr 方式で重み付け統合している(マージ設定 YAML は元カードに公開)
- 本リポジトリはその量子化版で、量子化作者 mradermacher が 2026-11-04 に公開。元モデルは bf16 safetensors(約62GB)でしか配布されておらず、そのままでは一般の PC では動かせない
- 位置づけは『キャラクター性のある文章生成』。元カードの想定用途はロールプレイ、創作、ストーリーテリング、インタラクティブフィクションの4つ
- 発見元は X の HuggingModels アカウントによる『31B のロールプレイ/物語向けモデルの GGUF 版、ローカル利用向け』という紹介投稿

## 収録ファイル

- Lunar-Trace-31B.i1-IQ1_S.gguf — 7.16GB(カード表記 7.3GB、非常用)
- Lunar-Trace-31B.i1-IQ2_M.gguf — 10.92GB
- Lunar-Trace-31B.i1-IQ3_S.gguf — 13.76GB(カード曰く Q3_K 系より上)
- Lunar-Trace-31B.i1-IQ4_XS.gguf — 16.74GB
- Lunar-Trace-31B.i1-Q4_K_S.gguf — 17.76GB / Lunar-Trace-31B.i1-Q4_K_M.gguf — 18.69GB(カード推奨)
- Lunar-Trace-31B.i1-Q5_K_M.gguf — 21.85GB / Lunar-Trace-31B.i1-Q6_K.gguf — 25.20GB
- Lunar-Trace-31B.imatrix.gguf — 0.03GB(自分で量子化する場合の imatrix。推論には不要)
- 合計24個の GGUF(23量子化+imatrix)・約334.8GB(全量子化の合算。1つだけ落とせばよい)
- 注意: mmproj(視覚入力用)は本リポジトリに含まれず、別リポジトリ mradermacher/Lunar-Trace-31B-GGUF に mmproj-f16 / mmproj-Q8_0 として置かれている

## 実行条件

- GGUF を読めるランタイム(llama.cpp / Ollama / LM Studio / KoboldCpp など)
- i1-Q4_K_M(18.7GB)なら 24GB 級 GPU、または 32GB 以上の RAM での CPU 実行。IQ2_M(10.9GB)なら 12〜16GB 級で現実的
- ディスク空き容量は落とす量子化と同程度以上(全種だと 335GB)
- 画像入力を使う場合は mmproj を別途ダウンロードし、ランタイムに一緒に渡す
- ライセンスは apache-2.0(元モデル・上流 gemma-4-31B-it も同表記)。商用利用の可否は各リポジトリの記載に従う

## 使い方

```bash
# llama.cpp の場合(推奨量子化 Q4_K_M を取得して対話起動)
pip install -U huggingface_hub
hf download mradermacher/Lunar-Trace-31B-i1-GGUF \
  Lunar-Trace-31B.i1-Q4_K_M.gguf --local-dir ./lunar-trace

# -ngl は GPU に載せる層数。VRAM に応じて調整(全部載るなら 99)
llama-cli -m ./lunar-trace/Lunar-Trace-31B.i1-Q4_K_M.gguf \
  -ngl 99 -c 8192 --chat-template gemma

# OpenAI 互換サーバとして立てる場合
llama-server -m ./lunar-trace/Lunar-Trace-31B.i1-Q4_K_M.gguf -ngl 99 -c 8192 --port 8080
# → http://localhost:8080/v1/chat/completions に model 名を指定して POST
```

```bash
# 画像入力も使う場合(mmproj は別リポジトリから)
hf download mradermacher/Lunar-Trace-31B-GGUF \
  Lunar-Trace-31B.mmproj-f16.gguf --local-dir ./lunar-trace
llama-mtmd-cli -m ./lunar-trace/Lunar-Trace-31B.i1-Q4_K_M.gguf \
  --mmproj ./lunar-trace/Lunar-Trace-31B.mmproj-f16.gguf --image photo.jpg \
  -p "Describe this image."
```

```bash
# Ollama で使う場合は Modelfile を作って登録
cat > Modelfile <<'EOF'
FROM ./lunar-trace/Lunar-Trace-31B.i1-Q4_K_M.gguf
PARAMETER num_ctx 8192
PARAMETER temperature 0.8
EOF
ollama create lunar-trace:31b -f Modelfile
ollama run lunar-trace:31b
```


## 変更履歴

- 2026-11-06: 初回登録
