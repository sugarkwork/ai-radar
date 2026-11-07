---
type: "repo"
name: "Local Deep Research"
genre: "rag"
url: "https://github.com/LearningCircuit/local-deep-research"
repo: "LearningCircuit/local-deep-research"
license: "MIT"
stars: 9514
language: "Python"
created: "2025-02-09"
updated: 2026-11-07
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 「SimpleQA ~95%」は 95.7%（287/300）でサンプル300問。README 冒頭の n=500 は本文の表・HF の公開データセット（total=300）と一致しない。検索は Serper（クラウド・有料）で、ローカルなのは推論のみ＝検索まで含めた fully local ではない。実行はメンテナ自身の投稿1件（2026-05-01, qwen3.6:27b, LDR 1.6.7）で、README も小サンプル・採点ノイズ・SimpleQA 汚染を caveat として明記。② open issue 1,376 件は star の約14%。③ README（main）は 2.0.0 前提だが、GitHub release / PyPI / Docker latest は 1.10.7（2026-08-28）で 2.0.0 は Docker の prerelease タグのみ。DB リビジョンが上がり v1.10.7 へ戻せない。④ LDR_BOOTSTRAP_ALLOW_UNENCRYPTED=true はパスワード検証をしない開発用。⑤ MCP サーバは認証・レート制限なしの STDIO 前提でネットワーク公開不可と明言。⑥ egress 制御は best-effort で air gap ではない。⑦ CPU は AVX 必須、faiss-cpu は 1.13 系固定（1.14 は AVX2 非対応で SIGILL）。⑧ --network host は Linux ネイティブ専用。"
forks: 904
open_issues: 1376
commits_30d: 100
size_kb: 135582
archived: false
last_release: v1.10.7
last_release_at: 2026-08-28
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-07T05:24:45Z"
---

# Local Deep Research — 自前ホストの検索エージェント兼ナレッジベース

## 出来ること

- 質問から検索→読解→引用付きレポートまで自動。Quick Summary（30秒〜3分）、Detailed Research、Report Generation、Chat Mode（マルチターン）を選べる
- `langgraph-agent` 戦略では LLM が検索語と使うエンジンを自分で決めて反復する。arXiv / PubMed / Semantic Scholar を適宜切り替え、パイプライン型より多くのソースを集めるのが売り
- 検索源は無料10種（arXiv, PubMed, Semantic Scholar, Wikipedia, SearXNG, GitHub, Elasticsearch, Wayback, The Guardian, Wikinews）＋有料3種（Tavily, Google via SerpAPI/PSE, Brave）＋ローカル文書＋任意の LangChain retriever（FAISS / Chroma / Pinecone / Weaviate 等）＋メタ検索
- 見つけたソースをライブラリへ取り込み、抽出・インデックス・埋め込みまで行う。次回は自分の文書と Web を同じクエリで横断できる
- SQLCipher（AES-256）でユーザーごとに独立 DB。パスワードは保存せず「復号できたらログイン」で、DB ファイルだけでは読めない。LLM の API キーも個人 DB 内に暗号化
- Egress Scope（Adaptive / Public only / Private only / Strict / Unprotected）でエンジン・クラウド推論の可否・取得 URL を実行単位で制限。Strict と Private only はソケット遮断も張る
- MCP サーバ（`ldr-mcp`、STDIO）が search / quick_research / detailed_research / generate_report / analyze_documents など8ツールを公開。`search` は LLM を通さず生の結果だけ返すので監視用途は課金ゼロ
- 認証＋CSRF 付き REST API、WebSocket 進捗、PDF/Markdown 書き出し、購読ダイジェスト、コスト分析ダッシュボード、OpenAlex/DOAJ 由来21万件超のジャーナル品質スコア
- `quick_summary()` はサーバ不要で in-process 動作。既存の retriever をそのまま渡せる

## 目的・背景

- OpenAI / Google の Deep Research に対する「自分でホストする」代替。テレメトリ・解析・トラッキングを持たず、通信は自分が設定した検索・LLM・通知だけだと明記している
- 2025-02 作成、Python、MIT、⭐9,514 / fork 904。検索エンジン層・戦略層・保存層を差し替え可能にした枠組みで、単なる UI ラッパーではない
- ベンチマークの主張は「単一 RTX 3090（Qwen3.6-27B）で完全ローカル、SimpleQA ~95% を最初に報告した OSS」。出所は HF の `local-deep-research/ldr-benchmarks`（公開 CSV、生 YAML は GitHub 側）で、2026-05-01 の実行が SimpleQA 95.7%（287/300）、xbench-DeepSearch 77.0%（77/100）。ただしこの実行の検索は Serper で、ローカルなのは推論のみ。README も小サンプル・採点ノイズ・汚染リスクを併記している
- 比較対象は Perplexity 系の UI ではなく、検索源と保存先を自分で決めたい用途の制御盤

## 依存関係

- Python 3.12 以上 3.15 未満（`requires-python = ">=3.12,<3.15"`）
- LLM: Ollama / LM Studio / llama.cpp（`llama-server` の OpenAI 互換 API）/ OpenAI / Anthropic / Gemini / OpenRouter / Requesty / OpenAI・Anthropic 互換エンドポイント
- 検索: SearXNG（推奨・無料）か Tavily / Serper / Brave 等の API キー。ローカル文書とライブラリだけならクラウド検索は不要
- 主要パッケージ: langchain 1.2 系、playwright + patchright、sentence-transformers、faiss-cpu、SQLAlchemy 2.0 + alembic、pypdf、trafilatura
- SQLCipher は pip 版もホイール同梱でコンパイル不要。PDF 書き出しは WeasyPrint 経由で Windows は Pango が要る
- MCP 利用時のみ `local-deep-research[mcp]`（mcp[cli]）
- CPU は AVX 必須（Sandy Bridge / Bulldozer 以降）。ARM64 対応。faiss-cpu は 1.13 系固定（1.14 は AVX2 非対応 CPU で SIGILL、#4480）

## 実行条件

- Docker（Linux ネイティブまたは Docker Desktop）か pip。リポジトリは 135,582KB（約132MB）で、別途モデル重みとデータ領域
- 既定ポートは 5000（Web UI）、Ollama 11434、SearXNG 8080
- `--network host` は Linux ネイティブ専用。Docker Desktop（macOS / Windows / WSL2）では port 5000 が出ず localhost も LDR 自身を指すため、compose か FAQ のレシピを使う
- 安定版は v1.10.7（2026-08-28、GitHub release・PyPI・Docker latest が一致）。main は 2.0.0（FastAPI 化）で Docker は `prerelease` タグのみ。2.0.0 は DB リビジョンが上がり v1.10.7 に戻せないため、試す前に `encrypted_databases/backups/` を別領域へ退避する
- `LDR_BOOTSTRAP_ALLOW_UNENCRYPTED=true` は SQLCipher が使えない時だけ平文 SQLite に落ちる開発用。パスワード検証をしないので共有環境向けではない
- MCP サーバは STDIO・ローカル専用で認証もレート制限も無い。ネットワークに晒さない
- egress 制御は air gap ではない。セルフホストの SearXNG も上流へ問い合わせるため「public engine」扱いで、Private only では使えない
- MIT、テレメトリ無し。LLM と検索 API の費用、クラウド検索時のクエリ送出は利用側の管理

## 最短手順

- Docker Compose（全プラットフォーム・CPU）:
```bash
curl -O https://raw.githubusercontent.com/LearningCircuit/local-deep-research/main/docker-compose.yml
docker compose up -d    # NVIDIA GPU は docker-compose.gpu.override.yml を -f で重ねる
# 約30秒後に http://localhost:5000
```
- pip:
```bash
python3.12 -m venv .venv && . .venv/bin/activate
pip install "local-deep-research[mcp]"
python -m local_deep_research.web.app    # http://localhost:5000（2.0.0 系は ldr-web）
```
- Claude Code から MCP で使う（`.mcp.json`）:
```json
{"mcpServers":{"local-deep-research":{"command":"ldr-mcp","env":{"LDR_LLM_PROVIDER":"ollama","LDR_LLM_OLLAMA_URL":"http://localhost:11434"}}}}
```
- 起動後: Settings → LLM でモデルを指定（`llm.model` に既定値は無く、未設定だと調査は明示エラーで止まる）→ Egress Scope を確認 → 戦略に `langgraph-agent` を選ぶ

## 変更履歴

- 2026-11-07: 初回登録
