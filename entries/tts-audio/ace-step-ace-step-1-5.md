---
type: "repo"
name: "ACE-Step 1.5"
genre: "tts-audio"
url: "https://github.com/ace-step/ACE-Step-1.5"
repo: "ace-step/ACE-Step-1.5"
license: "MIT"
stars: 14491
language: "Python"
created: "2025-09-04"
updated: 2026-10-11
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 発見元ポストは「ACE-Step 1.5」とだけ書くが、同名の旧リポジトリ ace-step/ACE-Step（v1、★5.0k、Apache-2.0）が別に存在し、本エントリの 1.5 が現行。旧リポジトリは 2026-02-15 から更新停止。② 「A100 で1曲2秒未満／RTX 3090 で10秒未満」は README の主張で、第三者計測ではない。③ 「Suno v4.5〜v5 の間の品質」もベンダーの自己評価。④ 「4GB 未満の VRAM で動く」は 2B turbo ＋ INT8量子化 ＋ CPU オフロード時の構成で、素の推論要件ではない（XL 4B は重みだけで約9GB、オフロード込みで12GB以上）。⑤ コードは MIT だが、重み（HF: ACE-Step/Ace-Step1.5、XL 系は acestep-v15-xl-*）のライセンスは別建てで、モデルカードで確認が要る。⑥ 最終 push 2026-10-11、直近30日のコミットは 0。⑦ ROCm on Windows は Python 3.12 固定、macOS は MLX 経由で別スクリプト。⑧ 同名の商用サイト acemusic.ai を README 自身が案内しており、ローカル版と混同しやすい。⑨ Docker 対応（v0.1.8）は Release 本文とリポジトリ直下の Dockerfile にしか書かれておらず、README と docs のインストール手順には載っていない（2026-10-11 時点の main）。"
forks: 1920
open_issues: 162
commits_30d: 0
size_kb: 14295
archived: false
fetched_at: "2026-11-07T22:46:00Z"
last_release: v0.1.8
last_release_at: 2026-05-18
commits_90d: 15
commit_cadence: monthly
---

# ACE-Step 1.5 — LM が曲の設計図を書き、DiT が音にする音楽生成モデル

## 出来ること

- Text2Music: 短い説明文からフルコーラス付きの曲を生成する。Simple Mode は説明文だけ、上級モードではタグ・歌詞・BPM・キー・拍子・長さを指定する。
- 長さは10秒〜600秒（10分）。バッチで最大8曲を同時生成する。
- 参照音源を渡してスタイルを寄せる、カバー生成、リペイント（区間だけ再生成）、トラック分離（ステム出力）、レイヤー追加（マルチトラック生成）、ボーカルから伴奏を作る Vocal2BGM。
- 音源理解: 既存音源から BPM・キー・拍子・キャプションを抽出する（Audio Understanding）。生成曲には LRC 形式の歌詞タイムスタンプを付けられる。
- LoRA 学習を Gradio UI から実行できる。README の記載は「8曲・RTX 3090（12GB）で1時間」。
- 生成物の品質スコアリングを内蔵し、候補を自動採点する。
- 歌詞は50言語以上。日本語を含む多言語ドキュメント（API / Gradio / 推論 / チュートリアル / LoRA 学習）が同梱されている。
- Retake と Flow-Edit（v1 から移植）: Retake は拡散の開始ノイズを混ぜ直してバリエーションを作る（`retake_variance` 0.0〜1.0）。Flow-Edit は既存音源をプロンプトで編集する機能で、Remix のオーバーレイとして実装されている。
- 呼び出し口は4つ: Gradio UI（7860）、REST API（8001、非同期ジョブ）、Python API、対話式 CLI。v0.1.8 で公式 Docker イメージ（`ghcr.io/ace-step/ace-step-1.5`）が加わり、5つになった。DAW 連携用の VST3 は別リポジトリ（ace-step/acestep.vst3）。

## 目的・背景

- ACE Studio と StepFun による音楽生成基盤モデル。技術レポートは arXiv 2602.00744。旧 v1（arXiv 2506.00045）の後継で、2025-09 にリポジトリが分離され、2026-01-28 に v1.5 の重みが公開、2026-04-02 に XL（4B DiT）が追加された。
- 構成の要点は「LM をプランナーにする」こと。5Hz の軽量 LM（0.6B / 1.7B / 4B）がユーザーの短い指示を曲の設計図（メタデータ・歌詞・キャプション）に展開し、その設計図が DiT（2B または XL 4B）を条件付ける。長さ・構成の一貫性を LM 側で担保する作り。
- 差分の中心は編集系。v1 にもあったリペイントに加え、カバー生成・ステム分離・レイヤー追加・Vocal2BGM が入り、DAW 的な後工程をカバーする。
- README は acemusic.ai（無料のホスト版）を併記しており、ローカル実行とホスト版が同じモデル系列で提供されている。

## 依存関係

- Python 3.11〜3.12。パッケージ管理は uv（README の手順は `uv sync`）。
- GPU バックエンド: CUDA（NVIDIA）を推奨。MPS（Apple Silicon、MLX 経由の専用スクリプト）、ROCm（AMD）、Intel XPU、CPU も動作対象。Windows の ROCm は Python 3.12 必須。
- LM バックエンドは PyTorch（`pt`）または vLLM。VRAM が少ない構成では LM を無効化して DiT のみで動かす。
- モデルは初回起動時に Hugging Face から自動取得。DiT（2B / XL 4B）と LM（0.6B / 1.7B / 4B）を別々に選ぶ。
- Gradio（UI）と FastAPI（REST API）は同梱。追加の外部 API キーは不要で、生成は完全にローカルで完結する。

## 実行条件

- VRAM の目安（README の表）: 6GB以下は 2B turbo ＋ LM 無効 ＋ INT8量子化 ＋ CPU オフロード、6〜8GBは 2B turbo ＋ LM 0.6B、8〜16GBは 2B ＋ LM 0.6B/1.7B（vLLM）、16〜20GBは 2B sft か XL turbo（XL は CPU オフロード前提）、20〜24GBで XL がオフロードなしで載る。XL の重みは約9GB（2B は約4.7GB）。
- 「4GB未満で動く」は上記の最小構成の話。XL を使うなら12GB以上（量子化＋オフロード）か20GB以上（オフロードなし）が要る。
- 速度は README の自己申告: A100 で1曲2秒未満、RTX 3090 で10秒未満（think モードと diffusion steps に依存し0.5〜10秒）。
- Docker はリポジトリ同梱の汎用 CUDA Dockerfile（x86_64 Linux + NVIDIA GPU 前提）を使う。イメージは `ghcr.io/ace-step/ace-step-1.5`（タグは `0.1.8` / `0.1` / `latest`）で、リリース毎に CI が自動ビルドする。`--gpus all` と `-v $(pwd)/checkpoints:/app/checkpoints` を渡す。7860 が Gradio、API は `-e ACESTEP_MODE=api` で 8001
- ディスクはモデル次第。DiT と LM を複数落とすと数十GB規模になる。
- コードは MIT。重みのライセンスはモデルカード側で別に確認する。生成物の権利は自国法域の扱いによる。

## 最短手順

- `curl -LsSf https://astral.sh/uv/install.sh | sh` で uv を入れる（Windows は PowerShell 版）。
- `git clone https://github.com/ACE-Step/ACE-Step-1.5.git && cd ACE-Step-1.5 && uv sync`
- `uv run acestep` で Gradio UI（http://localhost:7860）、`uv run acestep-api` で REST API（http://localhost:8001）。初回はモデルが自動ダウンロードされる。
- モデル・ポート・UI 言語を固定するなら `cp .env.example .env` して `ACESTEP_CONFIG_PATH`（例: acestep-v15-turbo）・`ACESTEP_LM_MODEL_PATH`（例: acestep-5Hz-lm-1.7B）・`PORT`・`LANGUAGE` を書く。リポジトリ更新後も設定が残る。
- OS 別の起動スクリプト（`start_gradio_ui.sh` / `.bat` / `_macos.sh`、API 版も同様）が同梱。Windows と macOS には依存関係込みのポータブル版も配布されている。
- Docker:
```bash
docker run --gpus all -p 7860:7860 -v ./checkpoints:/app/checkpoints ghcr.io/ace-step/ace-step-1.5:0.1.8
```
- API から叩く場合は docs/en/API.md の非同期ジョブ手順に従う。バッチ生成は UI の Batch か API の複数リクエストで行う。

## 変更履歴

- 2026-11-07: 初回登録（v1 のエントリとは別に、現行の 1.5 として登録）
- 2026-11-07: v0.1.8 の Docker 対応（汎用 CUDA Dockerfile・ghcr イメージ・CI 自動ビルド）、Retake / Flow-Edit の移植、raw remix・DCW サンプラ・コミュニティ VAE 差し替えを反映
