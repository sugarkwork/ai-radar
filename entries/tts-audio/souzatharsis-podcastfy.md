---
type: "repo"
name: "Podcastfy"
genre: "tts-audio"
url: "https://github.com/souzatharsis/podcastfy"
repo: "souzatharsis/podcastfy"
license: "Apache-2.0"
stars: 6782
language: "Python"
created: "2024-09-30"
updated: 2026-05-04
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 保守は低調: 最終push 2026-05-04、直近30日commit 0、PyPI最新は0.4.3、CHANGELOGの最終項目は0.4.0（2024-11-16）で約1年半更新なし。open issue 124。② README等で語られる「Web UI」はリポジトリ内に無い。存在するのはFastAPI（Dockerfile_api、beta扱い）とnotebook、外部ホストのデモ（openpod.fly.dev）のみ。Streamlitアプリはソースツリーに含まれない。③ pipのextrasは無い（PyPIのprovides_extraが空、pyprojectにoptional-dependenciesも無い）ので `pip install podcastfy` 一発で全部入る代わりに、langchain/vertexai/pandas等を含む重い依存を強制される。④ ffmpegはPythonラッパーでしか宣言されておらず、システムバイナリは別途導入が必要。⑤ 既定構成がGemini（文字起こし）+OpenAI（TTS）の2キー前提で、無料で試すにはlocal LLM+edge TTSへ寄せる必要がある。⑥ 最高品質とされるgeminimultiはGoogle Cloudの許可リスト制で、有償サポート契約が無いと403になる。⑦ 画像のローカルパス指定は0.3.3でセキュリティ理由により廃止（URL指定のみ）。⑧ クローンは351,909KB（約344MB）で、大半がdata/audioのmp3と13.9MBのnotebook。--depth 1前提。⑨ ローカルLLM手順はllamafile（localhost:8080）前提で、README自身が「出力がTTSにそのまま渡せないことがある」と警告している。"
forks: 792
open_issues: 124
commits_30d: 0
size_kb: 351909
archived: false
commits_90d: 0
commit_cadence: stale
fetched_at: "2026-11-07T05:25:16Z"
last_release: v0.4.0
last_release_at: 2024-11-16
---

# Podcastfy — URL・PDF・YouTube・画像を2人の会話ポッドキャストに変換するPythonパッケージ

## 出来ること

- URL、PDF、YouTube動画、画像、生テキスト、あるいは「話題」だけを渡すと、2話者が掛け合う会話形式のポッドキャスト（mp3＋文字起こし）を生成する
- ショート（2〜5分）と longform（20〜30分以上）を切り替え可能。longformは入力をチャンク分割し、前段の文脈を次チャンクに渡して一貫性を保つ
- 文字起こしはlitellm経由で100以上のLLMに対応（既定は `gemini-2.5-flash`）。`llm_model_name` と `api_key_label` で差し替える
- 音声は5バックエンド: `openai`（既定・`tts-1-hd`）、`elevenlabs`、`gemini`（Journey系）、`geminimulti`（Studio MultiSpeaker）、`edge`（キー不要）。話者ごとに声を分けられる
- `conversation_config.yaml` で話者の役割（要約役/質問役）、対話構造、口調、創造性、出力言語、チャンク上限を制御。ElevenLabsなら自分の声も使える
- Python API `generate_podcast(...)`、CLI `python -m podcastfy.client`、FastAPI（`Dockerfile_api`、ベータ）、Colab notebook の4経路

## 目的・背景

- NotebookLMのポッドキャスト機能に対するオープンソースの代替。README が明言する通り、差別化点はUI製品ではなく「プログラマブルであること」— 多形式の入力をコードから大量に、あるいは自前サービスに埋め込んで生成する用途を狙う
- 作者は Tharsis T. P. Souza（金融ML系の研究者）。JOSS形式の論文とNOTICEを同梱し、Apache-2.0で商用組込みが可能
- 既にOpenNotebook、SurfSense、Podcast-llmなどの外部プロダクトに組み込まれている

## 依存関係

- Python 3.11以上4.0未満（クラシファイアは3.11〜3.14）。`pip install podcastfy` のみで、extrasは存在しない
- システムの `ffmpeg` バイナリ（`pydub` と `ffmpeg` ラッパーが音声の結合・変換に使う。Pythonパッケージ側だけでは動かない）
- 文字起こし用LLMキー: `GEMINI_API_KEY`（既定）、`OPENAI_API_KEY`、Anthropic等はlitellmのプロバイダ名に従う。`.env` に置く
- 音声用TTSキー: `openai`→`OPENAI_API_KEY`、`elevenlabs`→`ELEVENLABS_API_KEY`、`gemini`/`geminimulti`→Google Cloud TTS APIの有効化＋APIキーの制限追加、`edge`→キー不要
- ローカルLLMは llamafile を `localhost:8080` で `--server` 起動する手順が用意され、`--local` で利用

## 実行条件

- 入力URLの取得とLLM/TTSのAPI呼び出しにネットワークが要る（`edge` もMicrosoftのエンドポイントを叩くためオフライン不可）
- 既定構成はGeminiとOpenAIの2キーが必須。キー無しで回すなら「llamafile＋edge」の組み合わせのみ
- `geminimulti` はGoogle Cloudの許可リスト制。有償サポート契約が無いプロジェクトでは `403 Multi-speaker voices are only available to allowlisted projects` で落ちる
- 保守状況: 最終push 2026-05-04、直近30日commit 0、PyPI 0.4.3、CHANGELOGは0.4.0（2024-11-16）で止まっている。破綻はしていないが、issue 124件に対する応答は期待しない方がよい
- クローンは351,909KB（約344MB）。大半が `data/audio` のmp3と13.9MBのnotebookなので `--depth 1` 前提
- 音声生成は利用側のAPI契約による従量課金。長尺ほどTTS呼び出し回数が増える

## 最短手順

```bash
python -m venv .venv && . .venv/bin/activate
pip install podcastfy

# 音声結合に使うシステムバイナリ（Debian/Ubuntu系）
sudo apt-get install -y ffmpeg

printf 'GEMINI_API_KEY=...\nOPENAI_API_KEY=...\n' > .env

# 既定構成（Geminiで文字起こし → OpenAI TTS）
python -m podcastfy.client --url https://example.com/article --url https://example.com/article2

# 課金を抑える: ローカルLLM + キー不要のedge TTS、音声は作らず文字起こしだけも可
python -m podcastfy.client --url https://example.com/article --transcript-only --local
python -m podcastfy.client --url https://example.com/article --tts-model edge

# 長尺・声や構成の変更
python -m podcastfy.client --url https://example.com/article --longform
python -m podcastfy.client --url https://example.com/article --tts-model elevenlabs --conversation-config path/to/custom_config.yaml

# Pythonから
python -c "from podcastfy.client import generate_podcast; print(generate_podcast(urls=['https://example.com/article']))"

# リポジトリごと使う場合（約344MBなので浅く取る）
git clone --depth 1 https://github.com/souzatharsis/podcastfy.git
```

- Web画面が欲しい場合、リポジトリ内にあるのはFastAPI（`Dockerfile_api`、ベータ）とnotebookだけ。公開デモの openpod.fly.dev は別ホストのアプリで、ローカルには同梱されない

## 変更履歴

- 2026-11-07: 初回登録
