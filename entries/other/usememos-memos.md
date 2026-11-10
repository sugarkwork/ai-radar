---
repo: "usememos/memos"
name: "Memos"
genre: "other"
url: "https://github.com/usememos/memos"
last_release: "26.11.0"
flags: ["unverified"]
risk_notes: "Docker起動、MCPクライアントからの接続、検索結果の品質や応答速度は独立実測していない。発見投稿にあるGrok Botとの接続は未確認。"
stars: 64375
forks: 4946
open_issues: 62
size_kb: 49158
language: "Go"
created: "2021-12-08"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 74
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:13:54+00:00"
---

# Memos — 手元のMarkdownメモをMCP経由で検索する

## 出来ること

- Markdownでメモを残し、タイムラインやタグから探せる。内蔵MCPにはメモの検索・取得に加え、作成・更新・削除のツールもある。

## 目的・背景

- 短いアイデアや作業記録を自分のサーバーに蓄積し、必要なメモをAIアシスタントから参照する。ツールがアクセスできる範囲は、接続に使うアカウントの権限に従う。

## 依存関係

- 最短構成はDockerと永続データ用ディレクトリ。既定のデータベースはSQLiteで、MySQLとPostgreSQLにも対応する。AI連携にはStreamable HTTP対応のMCPクライアントを使う。

## 実行条件

- アプリ本体はMITライセンス。手元で試す場合はポート5230をローカルに割り当て、データをホスト側に永続化する。MCPクライアントからインスタンスに到達できることと、対象メモを読めるアカウントの個人アクセストークンが必要。

## 最短手順

- Dockerで `docker run -d --name memos -p 127.0.0.1:5230:5230 -v ~/.memos:/var/opt/memos neosmemo/memos:26.11.0` を実行し、`http://localhost:5230` で初期アカウントを作り、検索用のメモを1件保存する。
- ユーザー設定で個人アクセストークンを発行する。MCPクライアントに、クライアントから到達できるインスタンスの `/mcp` をStreamable HTTPで登録し、`Authorization: Bearer <token>` を設定する。AIに `memo_list_memos` で先ほどのメモを検索させ、結果に出ることを確認する。

## 変更履歴

- 2026-11-10: 初回登録
