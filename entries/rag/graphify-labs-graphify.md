---
repo: "Graphify-Labs/graphify"
name: "Graphify"
genre: "rag"
url: "https://github.com/Graphify-Labs/graphify"
license: "Apache-2.0"
stars: 144984
language: "Python"
created: "2026-04-03"
updated: "2026-11-09"
forks: 13875
open_issues: 1623
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 35258
archived: false
last_release: "v0.9.105"
last_release_at: "2026-11-09"
author: "Graphify Labs (YC S26)"
homepage: "https://www.graphify.com"
flags: ["unverified"]
risk_notes: "投稿の数値と実測の差分: 投稿は「134k stars」とするが、2026-11-09T15:03Z の GitHub API 実測は 144,862 stars（13,858 forks, 1,646 open issues）。投稿日 2026-10-25 時点より増えており、投稿は star を過小に述べている（誇張ではない）。ただし作成 2026-04-03 から約7か月で14万 stars という伸びは異常に速く、YC ページでは「116K+ stars（約5か月）」、創業者プロフィールでは「108K+」と時期により数値が動く。star の内訳（組織的・自動的な star の有無）は未認証 API では取得できず監査していない。ベンチマークは開発元自身のハーネス（mem0/supermemory をアダプタとして内包）による自己申告で、独立した第三者追試は見つからない。LOCOMO の QA accuracy では supermemory 49.7% が graphify 45.3% を上回るため「top10に約50%正解」は recall@10=0.497 の話であり、回答精度そのものが最高という主張ではない。投稿の「コード部分はローカル完結」「モデルクレジット0」はコードのみのグラフ構築に限られ、docs/PDF/画像は設定した LLM バックエンドへ送信され、Kimi は中国リージョンにルーティングされる。音声/動画は faster-whisper でローカル文字起こしだが、yt-dlp による取得を伴う。ホスト版 Graphify Cloud は有料（Free/Pro $10-15/月・Teams $20-29/seat/月）で、README 冒頭の「token spend 80%削減」はホスト版の主張。API の /releases/latest は 404 を返したため、最新版は releases 一覧の先頭 v0.9.104 を採用した。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114326860326723736"]
fetched_at: "2026-11-09T21:42:14Z"
---

# Graphify — コードベースをローカル解析で知識グラフ化し、エージェントがgrepの代わりに辿る

## 出来ること

- フォルダを指定すると、コード・設定・SQLスキーマ・ドキュメント・PDF・画像・音声/動画を1つの知識グラフにまとめ、graphify-out/ に graph.html（ブラウザで開くクリック可能な地図）、GRAPH_REPORT.md（要点・意外なつながり・推奨質問）、graph.json（エージェントが問い合わせる完全なグラフ）の3ファイルを出力する。
- コードは tree-sitter の AST でローカルかつ決定論的に解析し、LLM を使わない。calls / imports / inherits / mixes_in などの辺を約40言語にわたりファイル横断で解決する。
- すべての辺に EXTRACTED（ソースに明示されていた）か INFERRED（graphify が解決した）のタグが付き、どこまでが原文由来かを区別できる。
- ベクトルDBも埋め込みも使わず、実グラフをたどる。`graphify query "<質問>"` でスコープ付きサブグラフ、`graphify path A B` で2概念間の最短経路、`graphify explain "<名前>"` で1概念の説明を返す。
- Leiden によるコミュニティ検出（サブシステム分割）、god nodes（最も接続の多い概念）、LLM 不要のコミュニティラベルを提供する。
- `graphify install` で Claude Code / Cursor / Codex / Gemini CLI / GitHub Copilot など20以上のアシスタントに skill を登録し、`/graphify .` で呼べる。Claude Code ではグラフを見る前に grep やファイル読みを促す hook（strict モードあり）も入る。
- `graphifyy[mcp]` で MCP stdio サーバが入り、MCP クライアントから同じグラフを query できる。`graphify watch` や git hook で差分更新もできる。

## 目的・背景

- エージェントに毎回ファイルを開かせたり grep させたりする代わりに、コードベースの構造を地図として渡し、コンテキスト選択の精度を上げるためのツール。作者は Graphify Labs（Y Combinator Summer 2026、San Francisco、創業者 Safi Shamsi）。
- OSS エンジン（このリポジトリ）は Apache-2.0 で無料、アカウント不要、テレメトリなし。常時更新・PRレビュー・形式検証を付けたホスト版 Graphify Cloud は別課金の商用サービス。
- 実測（2026-11-09）: 作成 2026-04-03、144,862 stars、13,858 forks、1,646 open issues、言語 Python、サイズ約32MB。直近30日・90日ともコミット100件以上（取得上限）で daily ペース。最新リリース v0.9.104（2026-11-08）、PyPI の graphifyy も 0.9.104。
- 効果の根拠は開発元の BENCHMARKS.md（最終更新 2026-07-05）。LOCOMO(n=300) の recall@10 は 0.497 で mem0 0.048・supermemory 0.149・BM25 0.362 を上回るが、QA accuracy は 45.3% で supermemory 49.7% に劣る。LongMemEval-S(n=50) は 76% で dense RAG と同点。グラフ構築の LLM クレジットは 0。
- 投稿の「公開メモリベンチマークでtop10に約50%正解（mem0は5%未満）」は recall@10 の 0.497 / 0.048 と一致する。ただし自社ハーネスでの自己申告値で、独立追試は確認できない。

## 依存関係

- Python 3.10 以上。推奨インストーラは uv（`uv tool install graphifyy`）、代替は pipx、pip も可。
- コード解析: tree-sitter と各言語のグラマー。コミュニティ検出: graspologic（Python 3.13 未満）またはネイティブバックエンド。
- extras（必要時のみ）: pdf / office（docx, xlsx）/ video（faster-whisper + yt-dlp）/ sql / postgres / terraform / ocaml / commonlisp / robot / mcp / watch / neo4j / falkordb / svg / leiden / ollama / openai / gemini / anthropic / bedrock / azure / chinese / all。
- ドキュメント・PDF・画像のセマンティック抽出には LLM バックエンドが必要（GEMINI_API_KEY か GOOGLE_API_KEY、MOONSHOT_API_KEY、ANTHROPIC_API_KEY、OPENAI_API_KEY、DEEPSEEK_API_KEY、Ollama、AWS 認証、または claude CLI）。コードのみなら API キー不要。
- PyPI の公式パッケージ名は graphifyy（y が2つ）。CLI コマンド名は graphify。他の graphify* パッケージは非提携と README が明記している。

## 実行条件

- macOS / Linux / Windows で動作。GPU は不要（Ollama をローカル推論に使う場合を除く）。
- コードのみのグラフは完全オフラインで作れる（`graphify extract . --code-only`、または GRAPHIFY_BACKEND=none）。ハイブリッド構成では docs/PDF/画像だけが外部モデルへ送られる。
- データ境界: バックエンドは API キーの有無で自動選択され、選んだ環境変数を stderr に表示する。Kimi（MOONSHOT_API_KEY）は中国リージョンのサーバへルーティングされる。機密コードは `GRAPHIFY_BACKEND=ollama` か `--code-only` を使う。
- `graphify query` / `path` / `explain` / MCP の `query_graph` は ~/.cache/graphify-queries.log に JSONL で記録される（GRAPHIFY_QUERY_LOG_DISABLE=1 で無効化）。
- 料金: OSS CLI は無料（Apache-2.0、アカウント不要、テレメトリなし）。ホスト版は Free $0（3リポジトリ、25,000ノード/リポジトリ）、Pro $10/月（年払い）〜$15/月、Teams $20〜29/seat/月、Enterprise は要相談。
- 規模の目安: 大規模 monorepo や常時更新はホスト版の想定。ローカルは1リポジトリ単位で、更新は watch / hook / `graphify update` を自分で回す。

## 最短手順

- 1. インストール: `uv tool install graphifyy`（代替: `pipx install graphifyy`）。
- 2. アシスタント登録: `graphify install`（Claude Code 既定。他は `graphify install --platform codex` など）。
- 3. AI 側で実行: `/graphify .`（Codex は `$graphify .`）。graphify-out/ に graph.html・GRAPH_REPORT.md・graph.json が出る。
- 4. CLI で直接確認: `graphify explain "APIRouter"`、`graphify path "FastAPI" "ModelField"`、`graphify query "認証はどこで処理される?"`。
- 5. AI から MCP で呼ぶ場合: `uv tool install "graphifyy[mcp]"` で MCP stdio サーバを入れ、MCP クライアント（Claude Code / Cursor など）にローカルサーバとして登録する。ツール名は接続先サーバが公開するもの（`query_graph` など）に従う。
- 6. コードだけをオフラインで索引: `graphify extract . --code-only`。Docs/PDF も含めるなら目的のバックエンドの API キーを設定してから `graphify extract .`。

## 変更履歴

- 2026-11-09: 初回登録
