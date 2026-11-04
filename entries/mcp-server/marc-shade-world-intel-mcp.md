---
repo: "marc-shade/world-intel-mcp"
name: "World Intelligence MCP"
genre: mcp-server
url: "https://github.com/marc-shade/world-intel-mcp"
license: "MIT"
stars: 1063
language: "Python"
created: "2025-11-29"
updated: 2026-10-18
added: "2026-11-04"
first_seen: "2026-11-04"
sources: []
flags: []
risk_notes: ""
forks: 177
open_issues: 0
size_kb: 4483
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: daily
last_release: v0.10.0
fetched_at: "2026-11-04T22:53:21Z"
last_release_at: 2026-09-02
---

# World Intelligence MCP

## 出来ること

- 30以上の領域をカバーする **160個の MCP ツール**を1つのサーバーで提供する。データは無料の公開 API のみ（有料 API キー不要、と README に明記）。
- 領域の例: 市場・流動性、予測市場、SEC 提出書類、紛争・軍事、航空機の動向（早期警戒）、移民・国境、サイバー、気候、ニュース。
- 取得した観測値は日付付きで履歴として残り、「その時点で何が分かっていたか」を後から引ける。改訂値・遅行相関の確認を想定した設計。
- Qdrant のベクトルストアと組み合わせて、蓄積したデータに対する自然文検索（例:「台湾周辺の軍事活動」）ができる。
- **29個の MCP プロンプト**（調べ方の手順書。使うツールと守るべき上限を明記）と、3つの MCP リソース（ツール一覧から自動生成したガイド、指標の用語集、データ源の健全性）。
- SSE のダッシュボードと CLI も同梱。

## 目的・背景

エージェントに「世界の現在」を持たせるための情報系 MCP。1ツール1 API の小さなサーバーを何本も入れる代わりに、無料 API を束ねた1本で済ませる構成。観測値に日付と出所を持たせている点を設計上の売りにしている。

## 依存関係

- Python 3.11 以降。`pip install -e .` で導入。
- 追加 extras: `[dashboard]`（運用ダッシュボード）、`[vector]`（Qdrant ＋ FastEmbed）、`[dev]`。
- ベクトル検索を使う場合は Qdrant を別途用意する。

## 実行条件

- ライセンスは MIT。★1,059、fork 177、issue 0（2026-11 時点）。
- 各データ源は無料公開 API のため、レート制限や仕様変更の影響を受ける。データの正確性は各提供元に依存し、このリポジトリが検証しているわけではない。
- 投稿の文言は「132 の MCP ツール」だが、現在の README と説明は **160 ツール**。バージョン差によるもので、登録は実測の 160 を採る。

## 最短手順

```bash
git clone https://github.com/marc-shade/world-intel-mcp.git
cd world-intel-mcp
pip install -e ".[vector]"
# README の手順で MCP サーバーとして起動し、Claude Code などから接続する
```

## 変更履歴

- 2026-11-04: 初回登録（★1,059 / MIT / 最終push 2026-10-18 / v0.10.0。ツール数は投稿の132ではなくREADMEの160を記載）
