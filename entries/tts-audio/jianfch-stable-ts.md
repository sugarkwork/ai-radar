---
repo: "jianfch/stable-ts"
name: "stable-ts"
genre: "tts-audio"
url: "https://github.com/jianfch/stable-ts"
author: "jianfch"
license: "MIT"
stars: 2282
language: "Python"
created: "2022-09-29"
updated: "2026-05-30"
forks: 249
open_issues: 0
size_kb: 5114
archived: true
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
last_release: "2.0.0"
last_release_at: "2023-03-17"
flags: []
risk_notes: "アーカイブ済みで開発は無期限停止（README 冒頭に明記、最終コード変更 2025-10-29、最終 push 2026-05-30 は休止告知コミット）。GitHub Releases は 2.0.0 (2023-03-17) で止まっており PyPI 最新 2.19.1 (2025-08-16) と乖離する。openai-whisper を <=20250625 にピン留めしているため将来の Whisper 更新には追従しない。README の「最大9倍高速」は著者の主張で一次ベンチマーク未提示、WER 改善の定量報告もなし（未検証）。当環境で音声推論・速度・VRAM は未実測。"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-07T18:38:44Z"
---

# stable-ts — Whisper の単語レベルタイムスタンプを補正し SRT/VTT/ASS に書き出す CLI/ライブラリ

## 出来ること

- Whisper 系モデルで文字起こしし、単語単位のタイムスタンプを付与（cross-attention + dynamic time warping）
- SRT / VTT / ASS / TSV / JSON / TXT へ出力。ASS は単語ハイライト、--karaoke でカラオケ風の段階表示に対応
- 既存台本への強制アライメント（--align/-a）と、--refine による最大 0.02 秒精度の再アライメント
- Silero VAD（--vad）または音量ベースの無音検出で、語の開始が早すぎる/終了が遅すぎるずれを補正（既定 suppress_silence=True）
- 句読点や無音ギャップに基づくセグメント再分割（regroup）と、特定の語を含む区間の検索（--locate）
- バックエンドを選択可能: 素の Whisper（既定）、faster-whisper（-fw）、Hugging Face Transformers（-hw）、MLX Whisper（-mlx）

## 目的・背景

- Whisper のタイムスタンプは語の実発話より早く始まり遅く終わることがあり、字幕用途では許容でも音声編集には精度が足りない。stable-ts は無音区間の境界を使って推論後の時刻を補正する
- 2.x では補正処理を推論後の後処理に変更したため、Whisper 以外の ASR の出力にも同じ補正を適用できる（examples/non-whisper.ipynb）
- 注意: リポジトリは archived で、README 冒頭に「Development on this repository is indefinitely paused.」と明記されている。最終コード変更は 2025-10-29、最終 push は休止告知コミット（2026-05-30）

## 依存関係

- pip install -U stable-ts（PyPI 最新 2.19.1、Python 3.8 以上）
- 必須: numpy, torch, torchaudio, tqdm, openai-whisper>=20230314,<=20250625
- オプション: pip install -U stable-ts[fw]（faster-whisper） / [hf]（transformers>=4.23.0,<=4.47.1, optimum, accelerate） / [mlx]（mlx-whisper、Apple Silicon 向け）
- Whisper を依存に含めない stable-ts-whisperless も配布されている
- FFmpeg が PATH に必要（音声/動画のデコード）。追加の denoiser を使う場合は別途導入

## 実行条件

- Python 3.8 以上。PyTorch 必須で、GPU を使うなら CUDA 対応版の PyTorch を先に入れる（未導入時は GPU 非対応版が入ることがある）
- CLI の --device は CUDA が利用可能なら cuda、なければ cpu を自動選択。CPU のみでも動作する
- モデルは tiny / base / small / medium / large-v1 / large-v2 / large-v3（CLI 既定は base）
- GPU なしで large 系を回すと時間がかかる（当方では速度・VRAM を実測していない）
- API キー不要・完全ローカル実行。料金は無料（MIT）

## 最短手順

- 前提: ffmpeg を導入し、pip install -U stable-ts（GPU 利用時は先に CUDA 対応 PyTorch を導入）
- 最小の CLI 実行: stable-ts audio.mp3 -o audio.srt
- 日本語・精度重視: stable-ts audio.mp3 -m medium --language ja --vad -o out.srt
- 複数フォーマット同時出力: stable-ts audio.mp3 -m medium --vad -f srt,vtt,ass -d ./subs
- Python から: import stable_whisper; model = stable_whisper.load_model('medium'); result = model.transcribe('audio.mp3', language='ja', vad=True); result.to_srt_vtt('out.srt'); result.to_ass('out.ass')
- 既存台本に合わせる: stable-ts audio.mp3 --align script.txt --language ja -o out.srt
- エージェントに渡す例: `stable-ts input.mp3 -m small --vad -f srt,json -o out.srt out.json` を実行させ、out.json を後段で加工。JSON から再出力する場合は `stable-ts out.json -f vtt -o out.vtt`
- 速度を優先する場合: -fw（faster-whisper）または -hw（Hugging Face）。Apple Silicon は pip install -U stable-ts[mlx] の上で -mlx

## 変更履歴

- 2026-11-07: 初回登録
