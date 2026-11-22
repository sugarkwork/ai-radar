---
name: "RustXNG"
genre: "agent-framework"
url: "https://github.com/sahenjp/RustXNG"
repo: "sahenjp/RustXNG"
license: "AGPL-3.0"
language: "Rust"
updated: "2026-11-16"
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
flags: ["unverified"]
risk_notes: "標準・Fullプロファイルは有効な外部検索プロバイダーへクエリを送信する。Fullには自動アクセス条件が制限的または未確認のプロバイダーが含まれる。利用するプロバイダーの条件確認が必要。"
stars: 978
forks: 82
open_issues: 16
size_kb: 6437
created: "2026-10-18"
archived: false
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Ryrenz/status/2118978267860382008"]
fetched_at: "2026-11-16T21:40:52Z"
last_release: "v0.31.2"
last_release_at: "2026-11-11"
---

# RustXNG

## 出来ること

- Rust製のセルフホスト型メタ検索エンジン。外部検索プロバイダーの結果をまとめ、JSON APIまたはMCPでAIエージェントに検索結果を提供する。MCPには検索と、検索結果URLの本文取得を行う読み取り専用ツールがある。Webスケールの検索インデックスは持たない。

## 目的・背景

- SearXNGを基に、複数の外部検索プロバイダーの結果を統合する。選択したサイトのローカルインデックスやWikipediaダンプを別途利用できる。

## 依存関係

- ソースからインストールする場合はRust 1.89以降とCビルドツールチェーンが必要。PDF本文抽出にはPopplerのpdftotextが必要で、スキャンPDFのOCRには別のOCRツールが必要。JavaScript描画ページ向けFirefoxレンダラーは任意で、単体リリースバイナリでは自動有効化されない。

## 実行条件

- リリースバイナリはLinux、macOS、Windows向け。標準プロファイルは設定された外部検索プロバイダーへクエリを送る。Cleanプロファイルは事前作成したローカルクロールおよびWikipediaダンプのインデックスのみを検索するが、明示的なページ取得などは外部通信を行う場合がある。既定ではループバックにバインドし、他ネットワークへ公開する場合はアクセス制御が必要。

## 最短手順

- リリースページから対象OS用バイナリを選び、実行前に対応するSHA-256サイドカーを確認する。起動例: `rustxng --bind 127.0.0.1 --port 29483`。別端末からJSON検索を試す。MCPサーバーは `rustxng mcp` で起動する。

## 変更履歴

- 2026-11-15: 初回登録
