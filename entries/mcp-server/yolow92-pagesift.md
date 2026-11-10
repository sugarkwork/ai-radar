---
type: "repo"
name: "pagesift"
genre: "mcp-server"
url: "https://github.com/YOLOW92/pagesift"
author: "YOLOW92"
repo: "YOLOW92/pagesift"
license: "AGPL-3.0"
stars: 256
language: "Rust"
created: "2026-10-20"
updated: "2026-11-09"
added: "2026-11-06"
first_seen: "2026-11-05"
sources: ["https://x.com/Ryrenz/status/2118161886894080121"]
flags: ["unverified"]
risk_notes: "AGPL-3.0 のため、改変してネットワーク越しに提供する場合はソース開示義務。プロプライエタリ製品への組み込みは別途商用ライセンス。README のベンチマーク数値（2.4ms/ページ、20.49倍、32MB 等）はすべて著者自身の計測で第三者検証なし＝カタログの事実としては採用せず flag 扱い。リポジトリは 2026-10-20 作成で履歴が浅く、v1.1.3 は検証当日リリース。pip 版 CLI のサブコマンドは mcp/scrape/convert のみで、README が示す crawl/extract/doctor やローカル PDF/Office の直接パースは cargo ビルド版の機能（pip 版 scrape は http(s) のみ受け付け、ローカルファイルは convert で HTML のみ）。"
forks: 32
open_issues: 0
commits_30d: 100
commit_cadence: "daily"
size_kb: 34774
archived: false
fetched_at: "2026-11-09T21:39:21Z"
last_release: "v1.2.4"
last_release_at: "2026-11-09"
commits_90d: 100
---

# pagesift — URL・PDF・Office を Markdown/JSON に変換する自己ホスト型 MCP サーバ

## 出来ること

- URL を取得し、本文抽出した Markdown もしくは JSON（links / images / metadata / スキーマ抽出）で返す
- PDF（スキャン頁は OCR）、Word / Excel / PowerPoint、EPUB などの電子書、eml・mbox などのメール、zip などの圧縮書庫を 1 つの呼び出しで処理
- MCP サーバとして stdio / HTTP の両方で動作し、pagesift_scrape / batch_scrape / crawl / crawl_status / map / interact / interact_stop の 7 ツールを公開
- Firecrawl v1/v2 互換の /v2/scrape・/v2/parse と Jina Reader 互換の /r/・/s/ を提供するので、既存のクラウド向けコードは URL 差し替えで移行できる
- CLI（scrape / convert）、Python・Node.js SDK、エージェントが自分でクロールして回答する /v2/agent を同梱

## 目的・背景

- RAG やエージェントの「入力づくり」で、爬虫類クローラ・PDF パーサ・OCR・Office 変換を別々に繋いでいた工程を 1 バイナリにまとめるのが狙い
- Firecrawl などの従量課金クラウドの置き換え／併用を想定したセルフホスト構成で、per-page 課金を避けられる
- 投稿の「Firecrawl の月額が浮く」「pypdf より 20 倍速い」といった訴求は投稿者・著者の主張であり、本項目では一次情報の事実として採用していない

## 依存関係

- 配布形態: pip（pagesift 1.1.3）／npm（@pagesift/node 1.1.3）／cargo install pagesift --locked／Docker イメージ ghcr.io/yolow92/pagesift:1.1.3
- HTTP・PDF・Office の基本処理は追加ランタイム不要（Python / JVM / Node を内部に持たない自前実装）
- 任意: JavaScript ページ用のブラウザ（Chrome 系）、OCR 用の NVIDIA GPU、/v2/agent 用の自前モデル設定

## 実行条件

- セルフホスト前提。稼働には外向き HTTP アクセス（対象サイトへの到達性）が必要
- robots.txt と per-host レート制限を守る実装で、拒否されたページは内容ではなくエラーを返す（裏取りで robots 拒否サイトは取得不可なことを明記）
- ライセンスは AGPL-3.0。改変版をネットワークサービスとして提供するとソース開示義務が生じ、プロプライエタリ組み込みは商用ライセンス契約が必要
- 性能・品質の各数値は README の著者計測値であり、独立検証はされていない

## 最短手順

- 1. インストール: `pip install pagesift`（検証済み。`pagesift --version` が 1.1.3 を返す）
- 2. AI に MCP として繋ぐ（stdio・最短）: エージェント設定に `claude mcp add pagesift -- pagesift mcp` を追加、または MCP 設定 JSON の command に `pagesift`、args に `["mcp"]` を書く
- 3. 常駐させて複数エージェントで共有する場合: `pagesift mcp --transport http --port 3003` を起動し、`claude mcp add --scope user --transport http pagesift http://127.0.0.1:3003/mcp` で登録（--port を明示するのは、ヘルプ上の既定値が 3001 でドキュメントの 3003 と食い違うため）
- 4. 接続後に AI が呼ぶツール: 既知の 1 ページは pagesift_scrape、複数 URL は pagesift_batch_scrape、サイト内 URL 探索は pagesift_map、サイト全体は pagesift_crawl → pagesift_crawl_status
- 5. CLI で単発確認: `pagesift scrape https://example.com`（本文のみの Markdown を返すことを検証済み）。手元の HTML は `pagesift convert page.html`
- 6. ローカル PDF / Office の直接パース・crawl・extract・doctor を使う場合は README 記載の cargo 版（`cargo install pagesift --locked`）または Docker 版を使う（pip 版 CLI のサブコマンドは mcp / scrape / convert のみで、scrape は http(s) URL 以外を受け付けない）

## 変更履歴

- 2026-11-06: 初回登録
