---
repo: "dgtlmoon/changedetection.io"
name: "changedetection.io"
genre: "mcp-server"
url: "https://github.com/dgtlmoon/changedetection.io"
stars: 35707
forks: 2230
open_issues: 386
size_kb: 78237
language: "Python"
created: "2021-01-27"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "0.70.3"
flags: ["unverified"]
risk_notes: "公開資料の記載を確認した。最新リリースの公開日時は年とタイムゾーンまで確認できていない。監視の検出精度・通知遅延、MCP接続の実動作、発見投稿のGrok Botとの連携は未検証。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2117960732184633699"]
fetched_at: "2026-11-10T11:12:36+00:00"
---

# changedetection.io｜Webページの変更履歴をMCPでAIから参照

## 出来ること

- 公開ページの価格表示や在庫表示、JSON APIの値を監視し、差分を履歴に残す。CSS、XPath、JSONPath、jqで監視範囲を絞り、変更時はApprise経由で通知できる。

## 目的・背景

- 監視で蓄積した差分をMCP対応アシスタントに渡し、価格表示がいつ変わったかなどを履歴に基づいて調べられる。取得できる内容は対象ページとフェッチャーの設定に依存する。

## 依存関係

- Docker ComposeまたはPythonパッケージで導入できる。通常の取得には内蔵HTTPフェッチャーを使え、Browser StepsやVisual SelectorにはPlaywrightが必要。

## 実行条件

- セルフホスト版はApache-2.0。公式の有料ホスト版にもMCPが含まれる。MCPは初期状態で無効で、Web版クライアントから接続するには到達可能なHTTPSエンドポイントが必要。

## 最短手順

- 公式READMEの手順で `docker compose up -d` を実行し、`http://127.0.0.1:5000` の画面で公開URLをウォッチに登録する。必要ならCSSセレクターで監視対象を絞る。
- インスタンスでMCPを有効にする。Claudeなどの対応クライアントにインスタンスのHTTPS URL `https://<host>/mcp/v1?readonly=1` をカスタムコネクタとして追加し、OAuthでウォッチの読み取り権限を付与する。履歴がたまったら「このウォッチの直近の変更点と検知日時を教えて」と依頼する。

## 変更履歴

- 2026-11-10: 初回登録
