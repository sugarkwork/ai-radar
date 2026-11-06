---
repo: "D4Vinci/Scrapling"
name: "Scrapling"
genre: "mcp-server"
url: "https://github.com/D4Vinci/Scrapling"
license: "BSD-3-Clause"
stars: 98348
language: "Python"
created: "2024-10-13"
updated: "2026-11-05"
added: "2026-11-06"
first_seen: "2026-11-06"
sources: ["https://x.com/AISuperDomain/status/2118353773701849567"]
flags: []
risk_notes: "スクレイピングツールのため、対象サイトの利用規約・robots.txt・著作権・個人情報保護を確認し、レート制限を守ること。Cloudflare 等の突破機能は規約違反や損害賠償リスクになり得る。"
forks: 10301
open_issues: 14
commits_30d: 100
commit_cadence: "daily"
size_kb: 16790
archived: false
fetched_at: "2026-11-06T07:24:00Z"
last_release: "v0.5.1"
last_release_at: "2026-11-04"
---

# Scrapling — AIエージェントから呼べるステルスWebスクレイピング基盤

## 出来ること

- HTTP 取得・ステルスブラウザ・JS レンダリングを1つの Python ライブラリで扱い、静的/動的ページ双方からデータ抽出できる。
- 内蔵 MCP サーバ（コマンド `scrapling-mcp`、README の mcp-name は io.github.D4Vinci/Scrapling）を Claude Desktop / Claude Code / Cursor 等から起動できる。
- MCP は17ツール構成: `make_request`、`browser_fetch_once`、`browser_fetch`、`browser_actions`、`browser_screenshot`、`browser_network_requests` など（docs/ai/mcp-server.html 記載）。
- Agent Skill「scrapling-official」を同梱。SKILL.md＋references/＋examples/ 構成で、コーディングエージェントに現行 API を教える。
- アダプティブ要素追跡（ページ変更後の要素再特定）、類似要素マッチング、CSS/XPath/正規表現選択、Markdown 出力に対応。
- Spider による並列クロール、プロキシローテーション、自動リトライ、AutoThrottle、中断/再開、JSON/JSONL/CSV/XML エクスポート。
- CLI と対話シェルを提供: `scrapling extract get <url> out.md --css-selector ...`、`scrapling shell`。
- MCP 側に広告・トラッカー約3,500ドメインのブロックと、隠し要素・ゼロ幅文字等を除去するプロンプトインジェクション対策を実装。

## 目的・背景

- スクレイピングの取得（HTTP/ブラウザ）、解析、クロール、エクスポートを別々のライブラリで組む手間を1つにまとめる目的のフレームワーク。
- AI エージェントが古い学習データの API を推測して壊れたコードを書く問題に対し、Skill で現行 API を同梱配布する設計。
- MCP はエージェントが自分でブラウザ操作・ネットワーク履歴調査・スクリーンショット取得まで行えるよう、セッション管理を提供する。
- BSD-3-Clause のオープンソースで、作者 Karim Shoair が個人で主導。PyPI・Docker・GitHub の3経路で配布。

## 依存関係

- Python 3.10 以上（PyPI の requires_python は >=3.10）。
- `pip install scrapling` だけではパーサのみ。fetchers/spiders を使うには `scrapling[fetchers]` が必要。
- MCP サーバは `pip install "scrapling[ai]"` の追加依存で有効になる。
- ブラウザ系 fetcher は `scrapling install` でブラウザ本体とシステム依存を取得する（HTTP のみなら不要）。
- 任意: 対話シェル/`extract` コマンドは `scrapling[shell]`、RAG 用途は `scrapling[rag]`、全部入りは `scrapling[all]`。
- Skill は Node 製 CLI `npx skills add ...`、OpenClaw なら `clawhub install scrapling-official`、手動なら ZIP 展開。

## 実行条件

- 無料・オープンソース（BSD-3-Clause）。API キーやアカウント登録は不要。
- MCP の `browser_*` 系と `scrapling install` には Chromium 等のブラウザ実体とディスク容量が必要。
- プロキシは任意。CDP 接続やプロキシ認証情報は利用者側で用意する（Skill 側も「外部ソルバ不要」と明記）。
- Docker 利用可: `docker pull pyd4vinci/scrapling` または `ghcr.io/d4vinci/scrapling:latest`。
- クラウド実行の場合、GUI なし環境では headless 前提。具体的なメモリ要件は README に記載なし（未確認）。

## 最短手順

```bash
# 1) MCP サーバ導入（ブラウザ依存も取得）
pip install "scrapling[ai]" && scrapling install

# 2) クライアントへ登録（Claude Code の例）
claude mcp add ScraplingServer "$(which scrapling-mcp)"

# 3) Agent Skill を導入（skills.sh CLI）
npx skills add D4Vinci/Scrapling --skill scrapling-official
```


## 変更履歴

- 2026-11-06: 初回登録
