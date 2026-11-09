---
repo: "microsoft/playwright-mcp"
name: "Playwright MCP"
genre: "mcp-server"
type: "repo"
url: "https://github.com/microsoft/playwright-mcp"
author: "Microsoft"
license: "Apache-2.0"
stars: 39376
language: "TypeScript"
created: "2025-03-21"
updated: "2026-11-06"
forks: 3409
open_issues: 3
commits_30d: 15
commits_90d: 41
commit_cadence: "weekly"
size_kb: 1974
archived: false
last_release: "v0.0.84"
last_release_at: "2026-10-31"
flags: []
risk_notes: "発見源は宣伝スレッド中の1行コマンドで、性能面の主張は無い。数値はすべて2026-11-09時点のGitHub API実測。README は『Playwright MCP is not a security boundary』と明記しており、任意サイトを操作してログイン情報を扱う用途では --isolated や専用 --user-data-dir での分離が必要。README 自身が coding agent では CLI+SKILLS の方がトークン効率が良いとしており、常時使う道具ではなく用途限定で採用するのが妥当。"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/thegreatest_sv/status/2114326860326723736"]
fetched_at: "2026-11-09T15:45:08Z"
---

# Playwright MCP — アクセシビリティスナップショットでブラウザを操作する Microsoft 公式 MCP サーバ

## 出来ること

- LLM／エージェントから MCP 経由で実ブラウザを操作する。browser_navigate、browser_click、browser_type、browser_fill_form、browser_select_option、browser_tabs など 72 個の browser_* ツールを提供する。
- browser_snapshot が Playwright のアクセシビリティツリーを ref 付きの構造化テキストで返す。スクリーンショットや vision モデルを使わずに要素を指定できるので、同じ手順が再現しやすい。
- Cookie・localStorage・sessionStorage の読み書き、browser_network_requests による通信の観測、browser_route によるリクエストの差し替え、トレース・動画・コンソールメッセージの取得までこなす。
- プロファイルは永続（既定）／--isolated の使い捨て／既存の Chrome・Edge に拡張機能で接続、の3通り。--headless、--browser chrome|firefox|webkit|msedge、--device 'iPhone 15'、--caps vision,pdf,devtools で挙動を切り替えられる。
- --port 8931 で HTTP トランスポートの常駐サーバとしても動く。Docker イメージ mcr.microsoft.com/playwright/mcp も配布されている（headless chromium のみ）。

## 目的・背景

- Microsoft が Apache-2.0 で公開する MCP サーバで、Playwright のブラウザ自動化を MCP のツール群として AI クライアントに渡す。リポジトリは 2025-03-21 作成、npm パッケージ名は @playwright/mcp。
- 設計の狙いは『AI に画面の画像を見せず、構造化された要素ツリーと ref を渡す』こと。README は vision モデル不要・決定的・軽量を長所として挙げる。
- README は用途の限界も明記する。coding agent では CLI+SKILLS（microsoft/playwright-cli）の方がトークン効率が良く、MCP は永続状態・詳細な内部観察・反復的な推論が必要な探索的自動化や自己修復テスト、長時間の自律ワークフロー向けと位置づけている。
- セキュリティ面は『not a security boundary』と明言され、任意の Web ページを操作できる前提で導入判断が必要。

## 依存関係

- Node.js 18 以上（README の Requirements と package.json の engines.node ">=18" が一致）。
- npm パッケージ @playwright/mcp（2026-11-09 時点の最新リリース v0.0.84）。npx で取得して起動する。
- 実行時依存は playwright と playwright-core（1.66.0-alpha 系）。ブラウザのバイナリは Playwright が管理し、初回起動時に取得される。
- MCP クライアント側が必要。Claude Code、VS Code、Cursor、Windsurf、Claude Desktop、Goose、Grok、Junie などの設定手順が README に用意されている。Docker 版は headless chromium のみ対応。

## 実行条件

- Node.js 18+ と npx が使えること。GUI の無いサーバや CI では --headless を付ける。
- 初回はパッケージとブラウザバイナリのダウンロードのためネットワークとディスクが必要（リポジトリの size は約 1.9MB、ブラウザ本体は別途）。
- ファイルアクセスは既定でワークスペースルート配下に制限され、file:// への遷移もブロックされる。解除するには --allow-unrestricted-file-access が必要。
- 同じワークスペースの永続プロファイルは同時に1ブラウザしか使えない。並列実行するなら各クライアントを --isolated にするか --user-data-dir を分ける。
- 認証情報を扱う操作では、サイト側の利用規約とレート制限に従う。MCP サーバ自体はセキュリティ境界ではない。

## 最短手順

- Claude Code から使う: ターミナルで `claude mcp add playwright npx @playwright/mcp@latest` を実行し、Claude Code を再起動する。
- 汎用の設定 JSON（Claude Desktop、Cursor、VS Code など）: {"mcpServers":{"playwright":{"command":"npx","args":["@playwright/mcp@latest"]}}} をクライアントの設定ファイルに追記する。
- ヘッドレス＋使い捨てプロファイルで動かす場合は args を ["@playwright/mcp@latest","--headless","--isolated"] にする。
- HTTP 常駐で複数クライアントから使う場合は `npx @playwright/mcp@latest --port 8931` を起動し、クライアント設定を {"mcpServers":{"playwright":{"url":"http://localhost:8931/mcp"}}} にする。
- 接続確認は、AI に『browser_navigate で https://example.com を開いて browser_snapshot を取って』と指示する。ref 付きの要素ツリーが返れば、その ref を browser_click の target に渡して操作を続けられる。

## 変更履歴

- 2026-11-09: 初回登録
