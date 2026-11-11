---
repo: "open-pencil/open-pencil"
name: "OpenPencil"
genre: "mcp-server"
url: "https://github.com/open-pencil/open-pencil"
stars: 9747
forks: 1051
open_issues: 151
size_kb: 78421
language: "TypeScript"
created: "2026-02-27"
updated: "2026-11-10"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
last_release: "v0.16.0"
flags: ["unverified"]
risk_notes: ".figの往復保存でレイアウトや変数がどこまで保持されるか、MCP接続と生成結果の品質は実機未検証。リリースの正確な公開日時は未確認。コミット数は各期間100件で打ち切り。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116241528737693741"]
fetched_at: "2026-11-10T13:03:10+00:00"
---

# OpenPencil — Claude CodeからMCPで編集できるデザインエディター

## 出来ること

- .figの読み書きと対応する.pen文書の読み込みができる。MCP経由でデザイン文書の調査・編集ができ、CLIでは文書検査やデザイントークンの抽出もできる。

## 目的・背景

- デザイン文書をノードツリーとして扱い、GUI編集とスクリプトやAIエージェントによる操作を同じ文書に適用できる。公式READMEは.figの読み書きを案内している。互換性や出力品質の独立実測は行っていない。

## 依存関係

- Claude Codeからstdioで接続するには、Claude Codeとnpmで導入する@open-pencil/mcpを用意する。内蔵チャットで外部モデルを使う場合は対応プロバイダーのAPIキーが必要で、料金は接続先の契約による。本体のライセンスはMIT。

## 実行条件

- 以下のMCP手順ではデスクトップ版を起動し、文書を開いておく。公式READMEのデスクトップ要件はmacOS 13以降（Safariを更新）、Windows 10以降、またはWebKitGTK 2.40以降を備えたLinux。v0.16.0のリリースノートはアプリとMCPパッケージを一緒に更新するよう案内している。

## 最短手順

- OpenPencilデスクトップ版で編集用の文書を開く。`npm install -g @open-pencil/mcp`でMCPパッケージを導入する。
- `claude mcp add --scope user open-pencil -- openpencil-mcp`で登録し、`claude mcp list`で接続を確認する。
- Claude Codeに『open-pencil MCPで現在のページを調べ、小さなヒーローセクションを追加して』と依頼し、求められたツール実行を承認する。編集結果はキャンバスで確認する。

## 変更履歴

- 2026-11-11: 初回登録
