---
name: "Firecrawl"
genre: "agent-framework"
url: "https://github.com/firecrawl/firecrawl"
flags: ["unverified"]
risk_notes: "README記載の性能やカバー率は独立に検証していない。利用条件や料金もこの資料だけでは確認できない。"
repo: "firecrawl/firecrawl"
stars: 200407
forks: 10543
open_issues: 783
size_kb: 190416
language: "TypeScript"
created: "2024-04-15"
updated: "2026-11-10"
archived: false
license: "AGPL-3.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118043980420030914"]
fetched_at: "2026-11-10T16:21:38.616964+00:00"
---

# Firecrawl

## 出来ること

- Web検索と検索結果ページの取得、URLのMarkdown・HTML・スクリーンショット・構造化JSONへの変換、取得したページ上での操作、サイトのクロールとURL検出、複数URLの一括取得、変更通知、PDFやDOCXなどの文書解析を提供するとREADMEに記載。

## 目的・背景

- READMEでは、AIエージェント向けにWeb上の情報を取得・操作するAPIとして説明されている。

## 依存関係

- READMEにはPython・Node.js SDK、cURL、CLI、およびMCPクライアント向けの接続例がある。各方法の依存パッケージや対応バージョンはこの資料では確認できない。

## 実行条件

- Quick Startではfirecrawl.devでサインアップしてAPIキーを取得する手順が案内されている。APIキーを使う例と、CLI・MCPの設定例がREADMEにある。

## 最短手順

- READMEのPython例では、`from firecrawl import Firecrawl`で読み込み、APIキーを渡してクライアントを作成し、`app.search("firecrawl", limit=5)`または`app.scrape('firecrawl.dev')`を呼び出す。実行はしていない。

## 変更履歴

- 2026-11-11: 初回登録
