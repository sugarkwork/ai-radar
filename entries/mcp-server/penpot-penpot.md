---
repo: "penpot/penpot"
name: "Penpot"
genre: "mcp-server"
url: "https://github.com/penpot/penpot"
last_release: "2.19.0"
flags: ["unverified"]
risk_notes: "MCPの接続、編集結果、生成コードの忠実度や往復変換で保持される範囲は独立に実測していない。最新リリースのタグは公開ページで確認したが、年とタイムゾーンを含む公開日時は未確認。"
stars: 62245
forks: 4393
open_issues: 937
size_kb: 438276
language: "Clojure"
created: "2015-12-29"
updated: "2026-11-10"
archived: false
license: "MPL-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2114739076796428729"]
fetched_at: "2026-11-10T11:34:59+00:00"
---

# Penpot — 公式MCPでデザインを読み取り・編集する

## 出来ること

- ブラウザでUIをデザインし、プロトタイプを作る。公式MCPをつなぐと、AIクライアントから編集中のページの構造や要素を調べ、要素の作成やスタイル変更を依頼できる。

## 目的・背景

- 公式MCPサーバーは、専用プラグインとWebSocketで通信し、PenpotのPlugin APIを通じてデザインを操作する。既存画面の構造をコード実装の参考にしたり、AIにデザイン案を同じファイル上で具体化させたりできる。

## 依存関係

- Penpotのブラウザセッションと、MCPに対応したAIクライアントを使う。ローカルMCPのREADMEではNode.js v22系での動作確認が記載されている。Penpot本体のセルフホストでは、公式構成のMCPコンテナを用意し、enable-mcpを有効にする。

## 実行条件

- リモートMCPはアカウントのIntegrationsで有効化し、個人用MCPキーで接続する。操作対象はブラウザでフォーカス中のPenpotページ。リモート接続ではローカルパスからの画像取り込みや、ローカルパスへの直接書き出しに制約がある。
- リポジトリはMPL-2.0。公式料金表にはクラウドとセルフホストの両方に無料のProfessionalプランがあり、セルフホストではサーバーの用意と運用が必要。

## 最短手順

- Penpotのアカウント設定でIntegrations → MCP Serverを開いて有効化し、接続URLを取得する。
- Claude Codeなどの対応クライアントに、取得したURLをリモートMCPサーバーとして登録する。
- Penpotで対象ファイルを開き、File → MCP Server → Connectで接続する。AIクライアントに『現在のページの構造と主要な要素名を一覧にして。ファイルは変更しないで』と依頼し、対象ページを確認する。

## 変更履歴

- 2026-11-10: 初回登録
