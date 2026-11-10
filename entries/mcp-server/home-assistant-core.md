---
repo: "home-assistant/core"
name: "Home Assistant Core"
genre: "mcp-server"
url: "https://github.com/home-assistant/core"
stars: 92120
forks: 39255
open_issues: 3854
size_kb: 937536
language: "Python"
created: "2013-09-17"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日時、候補投稿に登場する自作 Grok Bot との互換性、実機での接続と操作は未確認。コミット件数は両期間とも取得上限の100件に達している。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:15:00+00:00"
---

# Home Assistant Core — MCP で家庭内機器を AI クライアントにつなぐ

## 出来ること

- 対応機器の状態を確認し、自動化に組み込める。公式 MCP サーバーの Device control を使うと、音声アシスタント向けに公開した機器やセンサーを対応 AI クライアントから参照でき、設定に応じて操作もできる。

## 目的・背景

- ローカル制御とプライバシーを重視するオープンソースのホームオートメーション基盤。機器や操作への対応はモジュール式の統合で追加する。Core のライセンスは Apache-2.0。

## 依存関係

- 稼働中の Home Assistant、対象機器に対応する統合、MCP サーバーに接続できる AI クライアントが必要。クラウド上で動作するクライアントには、Home Assistant へインターネットから到達できる構成が必要。

## 実行条件

- 公式の導入方法は、対応機器や仮想マシンで動かす Home Assistant OS と、Docker などで動かす Home Assistant Container。MCP は OAuth 2.0 と PKCE に対応する。メイン URL は初期設定で全ツールを公開し、管理者アカウントを要求する。

## 最短手順

- Home Assistant を導入し、対象機器の統合を追加する。
- 設定の「システム → AI」で Model Context Protocol を有効にする。統合の設定でメイン URL のツールを Device control に絞り、読み取り専用を有効にして、対象センサーだけを音声アシスタントに公開する。
- メイン URL を対応 AI クライアントに登録し、OAuth 認証を済ませる。公開したセンサーの現在値を尋ね、Home Assistant の表示と照合する。

## 変更履歴

- 2026-11-10: 初回登録
