---
type: "repo"
name: "AI YouTube Shorts Generator"
genre: "video-gen"
url: "https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator"
repo: "Anil-matcha/AI-Youtube-Shorts-Generator"
license: "MIT"
stars: 5788
language: "Python"
created: "2024-06-28"
updated: 2026-11-06
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "①「free」はサブスク・クレジット・透かし無しの意味で、既定の --mode api は MuAPI の従量課金キーが必須（未設定なら RuntimeError で停止）。クレジットを買わないと既定構成では1本も出力できない。②完全ローカルは --mode local のみ。ただしハイライト選定の LLM 呼び出しだけは OpenAI か Gemini の有料キーが必要で、ローカル LLM バックエンドは未実装＝完全オフライン不可。③ポーリングのタイムアウトが README 1800秒／config.py 600秒で不一致。長尺は API モードで10分で落ちうる。④縦型化は OpenCV Haar cascade の顔検出で、話者1名・正面構図が前提。字幕焼き込み、BGM、話者分離、B-roll、テロップ装飾は無い。⑤yt-dlp をライブラリとして素で呼ぶだけで cookies / PO token を渡さないため、年齢制限・メンバー限定・bot 判定の動画は失敗しやすい。⑥30日で5コミット、open issue 26件。README の clone URL は旧ハンドル SamurAIGPT 名義（リダイレクト）。"
forks: 1054
open_issues: 26
commits_30d: 5
size_kb: 1360
archived: false
commits_90d: 12
commit_cadence: weekly
fetched_at: "2026-11-07T05:25:12Z"
---

# AI YouTube Shorts Generator — 長尺YouTubeを9:16ショートに切り抜くCLI

## 出来ること

- YouTube URL（または `file://` / ローカルパス）を渡すと、縦型 mp4 を N 本出力。各クリップに 0-100 のバイラルスコア、冒頭フック文、選定理由の一文が付く
- 文字起こし → コンテンツ種別判定（ポッドキャスト／インタビュー／チュートリアル等）→ ハイライト候補抽出 → 重複排除（50%超のオーバーラップは高スコア側を残す）→ 上位N本を裁剪、というパイプライン
- 30分超の動画は20分チャンク＋60秒オーバーラップに分割し、境界をまたぐ候補の取りこぼしを防ぐ
- 2モード。既定の `--mode api` はダウンロード・Whisper・ランキング・オートクロップを MuAPI に投げる。`--mode local` は yt-dlp + faster-whisper + ffmpeg + OpenCV で手元処理
- ローカルモードは文字起こしを `.srt`、元動画を `source_<video_id>.mp4` として `output/` にキャッシュし、再実行時は変換をスキップ
- CLI と Python ライブラリ（`generate_shorts(...)`）の両対応。`--output-json` で文字起こし・全候補・最終クリップを JSON に落とせるので `xargs` で一括処理しやすい
- アスペクト比は任意（9:16、1:1 など）。書き出し解像度は元動画の取得段で 360/480/720/1080 から選ぶ（既定 720）

## 目的・背景

- Opus Clip / Vidyo.ai / Klap / SubMagic 等のオープンソース代替として、月額20-300ドルと分数上限を避ける目的で作られた MIT の CLI。元は SamurAIGPT 名義のリポジトリ
- 「無料」の実体は「サブスクなし・クリップ毎クレジットなし・透かしなし」で、計算資源を自分で持つという意味。既定モードは MuAPI の従量課金 API を叩くため、比較表の「Free + open source」だけを読むと構成を誤る
- ハイライト抽出の評価軸（`VIRALITY_CRITERIA`）とシステムプロンプトがソースで公開されており、商用ツールのブラックボックス部分を差し替えられるのが売り。チャンク長・長尺閾値・オーバーラップも定数で調整できる
- README 冒頭に muapi.ai のバッジと SaaS 向け API 導線があり、リポジトリ自体が自社 API のリファレンス実装という性格が強い。ローカルモードは後から追加された逃げ道と見るのが妥当

## 依存関係

- Python 3.10 以上
- `requirements.txt`（API モード）: requests>=2.31、python-dotenv>=1.0 のみ
- `requirements-local.txt`: yt-dlp>=2024.1.1、faster-whisper>=1.0.0、openai>=1.0.0、google-genai>=1.0.0、opencv-python>=4.8.0（torch は CUDA 利用時のみ任意）
- 外部バイナリ: ffmpeg（libx264 と aac が使えるもの）。PATH 上に必要
- キー: API モードは `MUAPI_API_KEY`。ローカルモードは `OPENAI_API_KEY` か `GEMINI_API_KEY`（`LLM_PROVIDER` で選択）
- Whisper: faster-whisper 経由。モデルは tiny / base / small / medium / large-v3 から選択、既定は base。初回実行時に Hugging Face から取得。CPU は int8、CUDA は float16 で動く

## 実行条件

- リポジトリは 1,360KB と軽い。ただしソース動画・出力 mp4・Whisper モデル（base で約150MB、large-v3 で数GB）が `output/` と HF キャッシュに積まれる
- ネットワーク: ローカルモードでも LLM 呼び出しは外部。完全オフラインでは動かない（ローカル LLM バックエンドが無い）。初回は Whisper モデルの取得も必要
- API モードの実費は MuAPI のクリップ単価。ポーリング間隔5秒、タイムアウトはコード上600秒（README は1800秒と記載）なので、長い動画を既定値で流すと途中で切れやすい
- yt-dlp はライブラリとして素で呼ぶだけで、cookies / PO token / EJS を渡さない。年齢制限・メンバー限定・bot 判定のかかった動画は失敗する前提で、その場合はローカルに落としたファイルを渡す
- 縦型化は OpenCV の Haar cascade 顔検出＋移動平均。話者1名が正面を向いている構図が前提で、画面分割・複数人被写・スライド主体の動画では破綻しやすい
- 字幕焼き込み、BGM、話者分離、B-roll、テロップ装飾は無い。出力は素の縦型カットのみ

## 最短手順

```bash
git clone https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator.git
cd AI-Youtube-Shorts-Generator
python3.10 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-local.txt   # --mode local を使う場合
cp .env.example .env                    # キーを記入

# 既定（MuAPI、クレジット消費）
python main.py "https://www.youtube.com/watch?v=VIDEO_ID" --num-clips 3

# 手元処理（MuAPI 不要、LLM キーのみ）
python main.py "https://www.youtube.com/watch?v=VIDEO_ID" --mode local \
    --num-clips 5 --aspect-ratio 9:16 --output-json result.json

# ローカルファイル／一括処理
python main.py ./input.mp4 --mode local
xargs -a urls.txt -I{} python main.py "{}" --mode local
```

- `.env` のローカル側: `LLM_PROVIDER=openai|gemini`、`OPENAI_MODEL=gpt-4o-mini`（既定）、`GEMINI_MODEL=gemini-2.5-flash`（既定）、`LOCAL_WHISPER_MODEL=base`、`LOCAL_WHISPER_DEVICE=auto|cpu|cuda`、`LOCAL_OUTPUT_DIR=output`
- 出力は `output/short_01.mp4`、`short_02.mp4` … の連番。文字起こしと元動画はキャッシュされ、再実行時は再利用される
- 音声が拾えない／Whisper がセグメントを返さない場合は `--language en` などで自動判定を止める

## 変更履歴

- 2026-11-07: 初回登録
