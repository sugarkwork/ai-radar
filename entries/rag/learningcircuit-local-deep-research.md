---
type: "repo"
name: "Local Deep Research"
genre: "rag"
url: "https://github.com/LearningCircuit/local-deep-research"
repo: "LearningCircuit/local-deep-research"
license: "MIT"
stars: 9556
language: "Python"
created: "2025-02-09"
updated: "2026-11-09"
added: "2026-11-07"
first_seen: "2026-11-07"
sources: ["https://x.com/abir35627/status/2118648224202551573"]
flags: []
risk_notes: "① 「SimpleQA ~95%」は 95.7%（287/300）でサンプル300問。README 冒頭の n=500 は本文の表・HF の公開データセット（total=300）と一致しない。検索は Serper（クラウド・有料）で、ローカルなのは推論のみ＝検索まで含めた fully local ではない。実行はメンテナ自身の投稿1件（2026-05-01, qwen3.6:27b, LDR 1.6.7）で、README も小サンプル・採点ノイズ・SimpleQA 汚染を caveat として明記。② open issue 1,384 件は star の約14%。③ 2.0.0（FastAPI 化）は 2026-11-07 に正式リリースされ、GitHub release・PyPI・Docker の `latest` が 2.0.0 で揃った。DB リビジョンが上がるため v1.10.7 では開けず、上げた後に v1.10.7 を起動すると内蔵バックアップを消すことがある。④ LDR_BOOTSTRAP_ALLOW_UNENCRYPTED=true はパスワード検証をしない開発用。⑤ MCP サーバは認証・レート制限なしの STDIO 前提でネットワーク公開不可と明言。⑥ egress 制御は best-effort で air gap ではない。⑦ CPU は AVX 必須、faiss-cpu は 1.13 系固定（1.14 は AVX2 非対応で SIGILL）。⑧ --network host は Linux ネイティブ専用。"
forks: 910
open_issues: 1415
commits_30d: 100
size_kb: 128023
archived: false
last_release: "v2.0.0"
last_release_at: "2026-11-07"
commits_90d: 100
commit_cadence: "daily"
fetched_at: "2026-11-09T21:42:24Z"
---

# Local Deep Research — 自前ホストの検索エージェント兼ナレッジベース

## 出来ること

- 質問から検索→読解→引用付きレポートまで自動。Quick Summary（30秒〜3分）、Detailed Research、Report Generation、Chat Mode（マルチターン）を選べる
- `langgraph-agent` 戦略では LLM が検索語と使うエンジンを自分で決めて反復する。arXiv / PubMed / Semantic Scholar を適宜切り替え、パイプライン型より多くのソースを集めるのが売り
- 検索源は無料9種（arXiv, PubMed, Semantic Scholar, Wikipedia, SearXNG, GitHub, Elasticsearch, The Guardian, Wikinews）＋有料3種（Tavily, Google via SerpAPI/PSE, Brave）＋ローカル文書＋任意の LangChain retriever（FAISS / Chroma / Pinecone / Weaviate 等）＋メタ検索。2.0 で Serply（Google の web/News/Scholar）、Webz.io のニュース検索、Federal Register が加わり、DuckDuckGo は廃止、Wayback は検索エンジンからエージェント用のアーカイブ取得（`fetch_archive`）に降格
- 2.0 で「停止」が実効化: 研究・チャット・インデックス・ベンチマークを実行中に止めると、走っている LLM・埋め込み処理も打ち切る
- 新しいローカルインデックスの既定埋め込みは GTE ModernBERT。FAISS インデックスは次回書き込み時に新形式へ変換される（再埋め込みは不要）
- 見つけたソースをライブラリへ取り込み、抽出・インデックス・埋め込みまで行う。次回は自分の文書と Web を同じクエリで横断できる
- SQLCipher（AES-256）でユーザーごとに独立 DB。パスワードは保存せず「復号できたらログイン」で、DB ファイルだけでは読めない。LLM の API キーも個人 DB 内に暗号化
- Egress Scope（Adaptive / Public only / Private only / Strict / Unprotected）でエンジン・クラウド推論の可否・取得 URL を実行単位で制限。Strict と Private only はソケット遮断も張る
- MCP サーバ（`ldr-mcp`、STDIO）が search / quick_research / detailed_research / generate_report / analyze_documents など8ツールを公開。`search` は LLM を通さず生の結果だけ返すので監視用途は課金ゼロ
- 認証＋CSRF 付き REST API、WebSocket 進捗、PDF/Markdown 書き出し、購読ダイジェスト、コスト分析ダッシュボード、OpenAlex/DOAJ 由来21万件超のジャーナル品質スコア
- `quick_summary()` はサーバ不要で in-process 動作。既存の retriever をそのまま渡せる

## 目的・背景

- OpenAI / Google の Deep Research に対する「自分でホストする」代替。テレメトリ・解析・トラッキングを持たず、通信は自分が設定した検索・LLM・通知だけだと明記している
- 2025-02 作成、Python、MIT、⭐9,516 / fork 904。検索エンジン層・戦略層・保存層を差し替え可能にした枠組みで、単なる UI ラッパーではない
- ベンチマークの主張は「単一 RTX 3090（Qwen3.6-27B）で完全ローカル、SimpleQA ~95% を最初に報告した OSS」。出所は HF の `local-deep-research/ldr-benchmarks`（公開 CSV、生 YAML は GitHub 側）で、2026-05-01 の実行が SimpleQA 95.7%（287/300）、xbench-DeepSearch 77.0%（77/100）。ただしこの実行の検索は Serper で、ローカルなのは推論のみ。README も小サンプル・採点ノイズ・汚染リスクを併記している
- 比較対象は Perplexity 系の UI ではなく、検索源と保存先を自分で決めたい用途の制御盤

## 依存関係

- Python 3.12 以上 3.15 未満（`requires-python = ">=3.12,<3.15"`）
- LLM: Ollama / LM Studio / llama.cpp（`llama-server` の OpenAI 互換 API）/ OpenAI / Anthropic / Gemini / OpenRouter / Requesty / QwenCloud（2.0 で追加）/ OpenAI・Anthropic 互換エンドポイント
- 検索: SearXNG（推奨・無料）か Tavily / Serper / Brave 等の API キー。ローカル文書とライブラリだけならクラウド検索は不要
- 主要パッケージ: langchain 1.2 系、FastAPI 0.136 系 + Uvicorn 0.34 系（2.0 の Web 層。Starlette も同時に固定）、playwright + patchright、sentence-transformers、faiss-cpu、SQLAlchemy 2.0 + alembic、pypdf、trafilatura、nltk
- SQLCipher は pip 版もホイール同梱でコンパイル不要。PDF 書き出しは WeasyPrint 経由で Windows は Pango が要る（2.0 は WeasyPrint 70 系＝GHSA-jf6q-chmf-3h3v の修正版）
- 非 Docker は NLTK データを一度取得する必要がある（`punkt_tab` と `averaged_perceptron_tagger_eng`）。Office / HTML / メール文書の解析が 2.0 から子プロセス化されたため。Docker イメージには同梱
- MCP 利用時のみ `local-deep-research[mcp]`（mcp[cli]）
- CPU は AVX 必須（Sandy Bridge / Bulldozer 以降）。ARM64 対応。faiss-cpu は 1.13 系固定（1.14 は AVX2 非対応 CPU で SIGILL、#4480）

## 実行条件

- Docker（Linux ネイティブまたは Docker Desktop）か pip。リポジトリは 135,582KB（約132MB）で、別途モデル重みとデータ領域
- 既定ポートは 5000（Web UI）、Ollama 11434、SearXNG 8080
- `--network host` は Linux ネイティブ専用。Docker Desktop（macOS / Windows / WSL2）では port 5000 が出ず localhost も LDR 自身を指すため、compose か FAQ のレシピを使う
- 安定版は 2.0.0（2026-11-07、GitHub release・PyPI・Docker の `latest` が一致）。2.0 は DB リビジョンが上がり v1.10.7 では開けないので、上げる前に暗号化 DB を別領域へ退避し、初回サインイン後に `encrypted_databases/backups/<user hash>/pre-migration/` を data ディレクトリの外へコピーする（既定の保持は1世代7日）
- 非コンテナ起動は既定で `127.0.0.1` にバインドする。LAN から使うなら `LDR_WEB_HOST=0.0.0.0`
- リバースプロキシ配下は `TRUST_PROXY_HEADERS=true` と、公開・CGNAT アドレスのプロキシなら `LDR_SERVER_FORWARDED_ALLOW_IPS` が要る（未設定だと全クライアントが1つのレート制限・ログインロックのバケットを共有する）。WebSocket は 2.0 で `/ws/socket.io` へ移動
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
- 2026-11-07: v2.0.0 の正式リリースに合わせ、検索エンジンの入れ替え（Serply / Webz.io / Federal Register 追加、DuckDuckGo 廃止、Wayback は取得ツールへ）、Stop の実効化、NLTK データ必須化、安定版の切り替えを反映
