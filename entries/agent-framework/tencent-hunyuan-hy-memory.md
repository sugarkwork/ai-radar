---
repo: "Tencent-Hunyuan/Hy-Memory"
name: "Hy Memory"
genre: "agent-framework"
url: "https://github.com/Tencent-Hunyuan/Hy-Memory"
author: "Tencent Hunyuan"
license: "Apache-2.0"
stars: 2020
forks: 146
language: "Python"
created: "2026-10-15"
updated: "2026-11-09"
open_issues: 153
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 23605
archived: false
last_release: "v1.0.6"
last_release_at: "2026-11-06"
flags: ["unverified"]
risk_notes: "投稿の数値のうち multi-hop recall 50%→90% は Tencent 公式サイトの導入事例グラフ（「多跳召回提升 40 个百分点」、棒グラフ50→90）と Tencent AI 公式X投稿で確認した。記憶量51.8%減・呼び出しトークン39.3%減は Tencent AI 公式X投稿（2026-10-16）の文言にのみ存在し、README・製品サイト・公開論文アブストラクトには該当記述が見つからず、第三者検証もない。pip install hy-memory==2.0.3 は実在（PyPI公開 2026-10-17）するが最新は 2.0.14（READMEも2.0.4以上を案内）。MemHub は preview 段階で、macOS は arm64 のみ・Windows非対応。GitHub API の license は Other/NOASSERTION を返すが、LICENSE 本文と README は Apache-2.0 と明記している。"
type: "repo"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/opensourcelab9/status/2113601359564230784"]
fetched_at: "2026-11-09T21:35:02Z"
---

# Hy Memory — LLMエージェント向け記憶エンジンと MemHub（Codex/Cursor 間で記憶を共有）

## 出来ること

- LLMエージェント向けの長期記憶エンジンと Python SDK（hy-memory）。チャット・仕事・コーディングの3シーン別に記憶パイプラインを持つ。
- Chat は L0〜L7 の階層記憶（生会話・原子事実・要約・スキーマ・意図）、Working は「事実＋再利用できる経験」の2層、Coding は同じ2層にコードの版差分チェーンを追加。
- add()/search() の2 API で書き込みと検索。lite（LLMなし・生文検索）/ pro（LLM抽出）/ ultra（知識グラフ＋夜間整理）の3モードを選べる。
- ベクトル保存先は ChromaDB（既定）・Qdrant・FAISS、グラフは Kuzu（既定）・Neo4j、作業/コード記憶のメタデータはローカル SQLite。
- MemHub は Codex・Cursor・Claude Code・OpenCode・Qwen Code などの会話/コーディング履歴を1つのローカル記憶にまとめ、各アプリから同じ記憶を引けるようにするデスクトップアプリ＋CLI。

## 目的・背景

- 「正しい一節を検索する」だけの記憶ではなく、信念の更新・因果のつながり・領域横断の抽象化まで扱う二重プロセス（System 1 が日中の書き込み、System 2 が夜間のスキーマ誘導）の認知記憶として設計されている。
- EMNLP 2026 採録の DCPM 論文（arXiv 2606.09483）と、記憶書き込み専用モデル Hy-Memory-30B-A3B の技術報告（arXiv 2610.22196）、コード記憶ベンチマーク CMB を伴う。
- Tencent 自社製品（自選株のAIアシスタント、iWiki、Tencent News など）に導入済みと公式サイトが説明。同サイトの事例グラフでは multi-hop recall が 50%→90%（+40pt）と示されている。
- 投稿が挙げる記憶量51.8%減・呼び出しトークン39.3%減は Tencent AI 公式アカウントの投稿文言にあるが、一次資料（論文本文・README）での裏取りと第三者検証はできていない。

## 依存関係

- Python 3.9 以上。必須依存は pydantic、numpy、openai>=1.40、chromadb>=1.5.9、kuzu、tiktoken、scikit-learn、rank-bm25、jieba など。
- オプション extra: qdrant（qdrant-client/fastembed）、faiss、graph（neo4j）、mysql、rerank（torch/transformers）。
- 記憶の抽出・検索に OpenAI 互換の LLM API と埋め込み API が必要（DeepSeek・DashScope などの例が README にある）。
- MemHub は macOS arm64 の署名済み DMG、または Linux x64/arm64 の Runtime。Windows は非対応。開発ビルドには Node.js 24・pnpm 11・Python 3.12・uv が要る。

## 実行条件

- MEMORY_LLM_API_KEY / MEMORY_LLM_BASE_URL / MEMORY_LLM_MODEL と、MEMORY_EMBEDDER_*（または OPENAI_API_KEY）の設定が前提。モデルは OpenAI 互換エンドポイントなら何でもよい。
- MemHub は preview 扱い。macOS 版は Developer ID 署名と公証を経た arm64 アプリで、GitHub Release の DMG と release-manifest.json / checksums.txt で配布。
- 初回起動時は既存記憶の点検・整理で数分かかることがあり、その間の強制終了は非推奨（v1.0.6 リリースノート）。
- SDK の最新版は 2.0.14。投稿の 2.0.3 は 2026-10-17 公開の旧版で、インストールは可能だが最新の修正は入らない。

## 最短手順

- 1. SDK: pip install hy-memory==2.0.14 （ChromaDB と Kuzu 同梱。Qdrant/FAISS/Neo4j は hy-memory[qdrant] などの extra）
- 2. 資格情報: export MEMORY_LLM_API_KEY=... / MEMORY_LLM_BASE_URL=https://api.deepseek.com / MEMORY_LLM_MODEL=deepseek-chat、埋め込み側も MEMORY_EMBEDDER_* を設定（OpenAI だけなら OPENAI_API_KEY 1本でも可）
- 3. Python から: from hy_memory import HyMemoryClient; client = HyMemoryClient(mode="pro"); client.add("…", user_id="user_1"); client.search("…", user_ids=["user_1"], limit=10) → client.close()
- 4. コーディング記憶: add() に tool_calls を含むメッセージと scene="coding"、workspace_id / branch を渡し、search() も同じ scene で呼ぶ。
- 5. AI アプリから共有記憶を使う: MemHub を導入し（macOS は DMG、CLI は npm の memhub-cli）、memhub install → memhub start。Codex・Cursor・Claude Code など対応アプリを接続すると、同じローカル記憶が各アプリのタスクから参照される。MCP / Skill / Hook / プラグイン接続は host-bridge と plugins（Hermes・OpenClaw など）が担う。

## 変更履歴

- 2026-11-09: 初回登録
