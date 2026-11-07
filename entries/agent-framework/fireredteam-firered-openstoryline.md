---
repo: "FireRedTeam/FireRed-OpenStoryline"
name: "FireRed-OpenStoryline"
genre: "agent-framework"
url: "https://github.com/FireRedTeam/FireRed-OpenStoryline"
license: "Apache-2.0"
stars: 3645
language: "Python"
created: "2026-02-07"
updated: "2026-07-31"
forks: 427
open_issues: 33
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 282
archived: false
flags: ["unverified"]
risk_notes: "インストール・実レンダリングは未実行で、記載は README / config.toml / requirements.txt / docs の原文にもとづく。2026-07-31 以降コミットがなく（30日0・90日0）、GitHub の Releases とタグは未作成（Docker Hub には v1.0.1 イメージあり）。LLM・VLM・（任意で）TTS/Pexels/AIトランジションのAPIキーが必須で、AIトランジションは外部動画生成APIの課金が発生し「コストが比較的高く結果は予測しづらい」とREADMEが明記している。"
type: "repo"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/heyrimsha/status/2118662273044807904"]
fetched_at: "2026-11-07T17:59:00Z"
---

# FireRed-OpenStoryline

## 出来ること

- 素材をアップロードするか、テーマだけを伝えると、素材検索（Pexels）→脚本生成→BGM/ナレーション/フォント推薦→タイムライン編成→動画レンダリングまでを会話で通す。
- 「空を撮っているカットを消して」「明るいBGMに変えて」「字幕の色を夕焼けに合わせて」のような一文の指示で、カットの差し替え・並べ替え・色/フォント/縁取り/位置の調整ができる。ガイドは工程の途中でも「意図の介入と部分的なやり直し（intent intervention and partial redo at any stage）」に対応し、最初からやり直さず該当ステップだけ再実行すると説明している。
- 編集ワークフロー全体を Skill として保存し、素材を差し替えて同じスタイルを再適用できる（Editing Skill Archiving）。同梱 Skill には default_editing_workflow / speech_rough_cut（ASR でフィラー・言い直しを除去）/ subtitle_imitation / ai_transition_editing / create_profile_style がある。
- 音声動画向けの ASR ラフカット、参照テキストから文体を寄せるコピー生成、前後カットの端点フレームから AI トランジションを生成する機能を持つ。
- MCP サーバ（既定 127.0.0.1:8001）として起動でき、Claude Code・OpenClaw・Codex などのエージェントから編集作業を呼び出せる。CLI（cli.py）と Web UI の両方がある。

## 目的・背景

- 手作業の編集操作を「意図を伝えるディレクティング」に置き換えることを狙った動画編集エージェント。自然言語インタフェース、LLM によるプランニング、ツールオーケストレーションを組み合わせ、人間が途中で介入できる透明性を重視すると README は説明している。
- 2026-02-10 にオープンソース化。Apache-2.0、Python 実装。Hugging Face Space と ModelScope のデモ、ホームページが用意されている。
- NEWS によれば 2026-03-12 に OpenClaw 連携（openstoryline-install / openstoryline-use の2 Skill）と Claude Code 向けの導入手順、2026-03-22 に ASR ラフカット、2026-04-02 に AI トランジション生成を追加した。

## 依存関係

- Python 3.11 以上（README は conda で python=3.11 の環境を作る手順を推奨）。
- requirements.txt の主要依存: langchain 1.2.4 / langchain-mcp-adapters 0.2.1 / langchain-openai / moviepy 2.2.1 / ffmpeg-python / av / librosa / faiss-cpu / sentence-transformers / transnetv2_pytorch（ショット分割）/ funasr・torchaudio（ローカル ASR を使う場合）。
- システム側: ffmpeg、wget、unzip、git（build_env.sh と download.sh が前提にする）。
- モデルとリソース: download.sh が .storyline/models（TransNetV2 の重みなど）と resource/（BGM・フォント・台本テンプレート）を外部から取得する。Python パッケージだけでは動かず、リソース取得が必須と Skill 側の手順にも明記。
- API キー: [llm]（OpenAI 互換。例として DeepSeek の deepseek-chat / https://api.deepseek.com/v1、国外向けには Gemini・Claude・ChatGPT を推奨）、[vlm]（GLM-4.6V または Qwen3-VL）、任意で Pexels（素材検索）、TTS（MiniMax / ByteDance / 302.ai のいずれか）、AI トランジション（MiniMax Hailuo または Alibaba Wan）。
- 課金: LLM・VLM・TTS・動画生成はいずれも各プロバイダの従量課金。README は AI トランジションについて「コストが比較的高く、結果はやや予測しづらい」として必要なときだけ有効化するよう注意している。

## 実行条件

- OS: Linux / macOS / Windows。自動セットアップの build_env.sh は Linux と macOS のみ（Windows は models.zip と resource.zip を手動展開）。同梱のインストール Skill は macOS / Linux / WSL（POSIX シェル）前提と明記している。
- GPU: README・config.toml・Dockerfile のいずれにも GPU/VRAM 要件の記載はなく、config.toml はショット分割を transnet_device="cpu" にし、Dockerfile は python:3.11-slim + ffmpeg で CUDA を含まない。GPU 高速化は TODO 項目。CPU のみでも構成できる想定だが、実測はしていない。
- ポート: MCP サーバ 8001、Web UI 8005（uvicorn 例）。Docker イメージと run.sh は 7860 で待ち受ける。
- 初回はモデル/リソースのダウンロードと pip インストールに時間がかかり、実行時は LLM/VLM の外部 API 呼び出しのためネットワーク接続が必須。
- ライセンス: コードは Apache-2.0。download.sh で取得するモデル重みと resource/ のアセットは別配布物で、README はフォント・音楽などのオープンソース資産にライセンス制約があり、商用グレードの資産は自前のアセットライブラリ追加で導入するよう案内している（重み個別のライセンス表記は未確認）。

## 最短手順

- 取得と環境作成: git clone https://github.com/FireRedTeam/FireRed-OpenStoryline.git → cd FireRed-OpenStoryline → conda create -n storyline python=3.11 → conda activate storyline
- 依存とリソース: Linux/macOS は sh build_env.sh。手動なら chmod +x download.sh → ./download.sh → pip install -r requirements.txt。Windows は models.zip を .storyline へ、resource.zip を resource へ展開してから pip install -r requirements.txt
- API キー設定: config.toml の [llm] と [vlm] に model / base_url / api_key を記入（例: DeepSeek なら model=deepseek-chat、base_url=https://api.deepseek.com/v1）。Web のモデル選択で Custom Model を選んでも同じ設定になる
- 起動: MCP サーバは PYTHONPATH=src python -m open_storyline.mcp.server、会話 UI は CLI なら python cli.py、Web なら uvicorn agent_fastapi:app --host 127.0.0.1 --port 8005
- Docker で動かす場合: docker pull openstoryline/openstoryline:v1.0.1 の後、リポジトリ直下で docker run -v ./config.toml:/app/config.toml -v ./outputs:/app/outputs -v ./run.sh:/app/run.sh -p 7860:7860 openstoryline/openstoryline:v1.0.1 を実行し、http://0.0.0.0:7860 を開く
- Claude Code から使う: リポジトリのルートで Claude Code を起動し /openstoryline-install → /openstoryline-use。グローバル設定に入れるなら mkdir -p ~/.claude/skills の後、cp -R .claude/skills/openstoryline-install ~/.claude/skills/ と cp -R .claude/skills/openstoryline-use ~/.claude/skills/ を実行
- Codex から使う（README では実験的扱い）: npx skills add FireRedTeam/FireRed-OpenStoryline --skill openstoryline-install --agent codex → npx skills add FireRedTeam/FireRed-OpenStoryline --skill openstoryline-use --agent codex。全プロジェクトで使うなら --global を付ける
- OpenClaw から使う: openclaw skills install openstoryline-install → openclaw skills install openstoryline-use（未対応版では npx clawhub install に切り替える）

## 変更履歴

- 2026-11-07: 初回登録
