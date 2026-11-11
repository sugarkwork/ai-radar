---
name: "Gmail AutoAuth MCP Server"
genre: "mcp-server"
url: "https://github.com/GongRzhe/Gmail-MCP-Server"
repo: "GongRzhe/Gmail-MCP-Server"
flags: ["unverified"]
risk_notes: "READMEに記載のOAuth認証ではGoogle Cloudの設定と認証情報が必要。効果、依存関係の全容、料金はREADMEから確認できない。測定値ではリポジトリはアーカイブ済みで、直近30日・90日のコミットは0件。"
stars: 1169
forks: 416
open_issues: 70
size_kb: 141
language: "JavaScript"
created: "2024-12-26"
updated: "2025-08-06"
archived: true
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Y0urDumble/status/2116341413755453670"]
fetched_at: "2026-11-10T13:39:39.898168+00:00"
---

# Gmail AutoAuth MCP Server

## 出来ること

- READMEでは、メールの送信・下書き・読み取り、添付ファイルの送受信や保存、検索、ラベル管理、既読状態の変更、ラベル間の移動、削除、複数メールの一括操作を提供すると説明している。

## 目的・背景

- GmailとClaude DesktopをMCP経由で連携し、自然言語でGmailを操作するためのサーバーとして説明されている。

## 依存関係

- READMEにはGmail APIの有効化とOAuth 2.0認証情報の作成が記載されている。実装上の依存パッケージの全容はこの資料では確認できない。

## 実行条件

- READMEにはClaude DesktopのMCP設定例がある。認証時はブラウザーを開いてGoogle認証を行い、認証情報を保存すると説明されている。Dockerおよびクラウド環境向けの手順も記載されている。

## 最短手順

- README記載の手順では、Google CloudプロジェクトでGmail APIを有効化し、OAuthクライアント情報をgcp-oauth.keys.jsonとして用意する。続いてnpx @gongrzhe/server-gmail-autoauth-mcp authで認証し、Claude DesktopのmcpServersにgmailの設定を追加する。

## 変更履歴

- 2026-11-11: 初回登録
