---
repo: "exa-labs/exa-mcp-server"
name: "Exa MCP Server"
genre: "mcp-server"
url: "https://github.com/exa-labs/exa-mcp-server"
license: "MIT"
stars: 5221
forks: 414
open_issues: 8
size_kb: 4415
language: "TypeScript"
created: "2024-11-27"
updated: "2026-11-05"
archived: false
commits_30d: 9
commits_90d: 20
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "GitHub の最新リリース用 URL は一覧に転送され、最新リリースのタグと公開日時は確認できなかった。README は GitHub の raw ファイルで確認した。検索精度、本文取得の成功率、匿名枠の具体的な上限、発見投稿が述べる YouTube のトレンド検出や動画制作・収益化の成果は未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/Y0urDumble/status/2114798387249717600"]
fetched_at: "2026-11-10T11:38:25+00:00"
---

# Exa MCP Server — AI エージェントに Web 検索と本文取得を追加

## 出来ること

- 既定の web_search_exa で関連ページを探し、web_fetch_exa で指定 URL の本文を Markdown として取得する。
- 任意の web_search_advanced_exa ではドメインや日付などで検索を絞り込める。

## 目的・背景

- AI エージェントが関連ページの発見から本文確認までを行えるよう、Exa の検索と取得機能を MCP 経由で提供する。ツールの機能は公式仕様に基づく。検索結果の関連性や取得品質は実測していない。

## 依存関係

- ホスト版には Streamable HTTP に対応する MCP クライアントとネット接続が必要。ローカルの stdio パッケージは Node.js 20 以上を要求し、MCP SDK と exa-js に依存する。

## 実行条件

- ホスト版の検索と本文取得はレート制限付きで匿名利用できる。Exa Agent には OAuth または API キーが必要。
- リポジトリのコードは MIT。Exa の公式料金ページには無料クレジット付きの Starter と従量課金の Developer が掲載されている。取得したページを転載する際は、各ページの権利と利用条件を確認する。

## 最短手順

- 対応する MCP クライアントに、接続先 https://mcp.exa.ai/mcp を Streamable HTTP として追加する。
- AI に『web_search_exa で調査テーマの公式資料を探し、候補の URL を web_fetch_exa で読んで、出典付きで要約して』と依頼する。

## 変更履歴

- 2026-11-10: 初回登録
