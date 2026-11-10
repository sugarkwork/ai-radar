---
type: "repo"
name: "ExcelMcp（本物のExcelをCOM経由でAIに操作させるMCPサーバ／CLI）"
genre: "mcp-server"
url: "https://github.com/sbroenne/mcp-server-excel"
repo: "sbroenne/mcp-server-excel"
license: "MIT"
stars: 875
language: "C#"
created: "2025-10-19"
updated: "2026-11-09"
added: "2026-11-06"
first_seen: "2026-11-05"
sources: ["https://x.com/bkdgiffug/status/2118155587850559963", "https://excelmcpserver.dev/"]
flags: []
risk_notes: "動作要件が重い：Windows、Microsoft Excel 2016 以降、対話的デスクトップ、.NET 10 が必要。Linux・macOS・サーバ側のバッチ処理は非対応と明記されている（ヘッドレスサーバでは動かない）。投稿の『31ツール・326操作』は古く、README の取得時点の表記は『437 operations』。Excel の COM API をそのまま叩くため、VBA 実行や Python in Excel（`=PY()`）も AI から呼べる構成であり、信頼できないブックを開かせるとマクロが動く。実行は自分のデスクトップの Excel プロセス上なので、作業中のブックを閉じる必要がある（開いているファイルは Excel の判断で読み取り専用になる）。"
forks: 108
open_issues: 9
commits_30d: 100
commit_cadence: "daily"
size_kb: 35154
archived: false
fetched_at: "2026-11-09T21:39:09Z"
last_release: "v2.6.11"
last_release_at: "2026-11-03"
commits_90d: 100
---

# ExcelMcp — ファイルを解析するのではなく、実物のExcelをCOM APIで動かすMCPサーバとCLI

## 出来ること

- ファイルを読むだけのツールとは違い、**実際の Excel アプリケーションを公式の COM API 経由で操作する**。だから Power Query の更新、数式の再計算、DAX の評価、VBA の実行、Python in Excel（`=PY()`）まで動き、ピボットテーブルや条件付き書式も壊さずに保てる
- 対象領域：**データと分析**（Power Query、DAX、Power Pivot、Excel テーブル、ピボットテーブル、データ接続）、**セルとブック**（範囲、数式、書式、シート、ファイル、再計算、名前付き範囲）、**グラフと表示**（グラフ、スライサー、条件付き書式、スクリーンショット、図形、スパークライン）、**自動化と応用**（VBA、Python in Excel、Goal Seek、シナリオ、データテーブル、ウィンドウ、XMLマップ）
- 操作数は README の取得時点で **437 operations**
- 同じコマンド群を**2つの入口**で使える：MCPサーバ（ツール定義を読める任意のクライアント向け、永続セッション）と `excelcli`（ターミナルを叩けるエージェント向け。ツール定義を読み込まないぶんトークンが少なく、ヘルプも内蔵）
- 両方とも Excel コマンドを別ワーカープロセスで実行するので、ある操作が固まっても基本の制御が止まらない。CLI はバックグラウンドサービスを保つため、ブックのセッションがコマンドをまたいで残る
- **既に開いているブックに接続**できる：ディスカバリとアタッチを使えば、作業中のブックをそのまま対象にできる
- VS Code 拡張、Claude Desktop ほかの MCP クライアント、GitHub Copilot CLI のプラグイン（`copilot plugin install excel-mcp@awesome-copilot`）として導入できる
- 作業中の様子を Excel の画面でそのまま見られる（`"Show me Excel while you work."`）ので、結果を確認しながら手で続きを編集できる

## 目的・背景

- Excel 業務の自動化は、これまで「xlsx を Python で読み書きする」方向に寄りがちだった。だが実務のブックは Power Query・ピボット・マクロ・外部接続が絡んでおり、ファイル操作では再現できない。作者はそこを「本物の Excel を動かす」ことで埋めている
- 結果として要件は重くなる：Windows と Excel のライセンス、対話的デスクトップが必須。サーバサイドのバッチや Linux コンテナでは動かない、という割り切りがある
- 姉妹プロジェクトとして PowerPoint MCP Server、Windows MCP Server、OBS Studio MCP Server も公開されている

## 依存関係

- **Windows**、**Microsoft Excel 2016 以降**、**対話的デスクトップ**、**.NET 10**
- MCPサーバとして使う場合は MCP クライアント（Claude Desktop / Claude Code / Codex / Copilot など）
- CLI として使う場合はターミナル実行権限のみ
- 導入経路：VS Code 拡張（Marketplace の `sbroenne.excel-mcp`）、MCPサーバのインストーラ、CLI のインストーラ、GitHub Copilot CLI プラグイン

## 実行条件

- **Linux・macOS・サーバ側のバッチ処理は対象外**（README が明示）。クラウド上でヘッドレスに回す用途には使えない
- 使用前に開いているブックを閉じる必要がある。Excel が新規に開くファイルを読み取り専用と判断する場合がある
- 実 Excel を操作するので、**VBA と Python in Excel が AI から実行可能**。信頼できないブックを対象にする場合は、マクロの扱いを別途制限する必要がある
- ライセンスは MIT。課金は無いが、Excel 本体のライセンスが前提
- 投稿の「326操作」は取得時点の README と一致しない（README は 437 operations）。数は版で動くので、実際の一覧は CLI のヘルプか MCP のツール説明で確認する

## 最短手順

```powershell
# 1) 導入（用途別に選ぶ）
#    VS Code:      Marketplace の sbroenne.excel-mcp をインストール
#    MCP クライアント: https://excelmcpserver.dev/installation-mcp-server/
#    エージェントCLI:  https://excelmcpserver.dev/installation-cli/

# 2) Copilot CLI の場合
copilot plugin install excel-mcp@awesome-copilot     # MCP 経由
copilot plugin install excel-cli@awesome-copilot     # CLI 経由（トークン節約）

# 3) 開いているブックを閉じてから、自然言語で依頼する
#    「products.csv を Power Query で取り込んでデータモデルに読み込んで」
#    「地域別売上のピボットテーブルを作って、縦棒グラフを追加して」
#    「利益10万ドルになる価格を Goal Seek で求めて」
```

## 変更履歴

- 2026-11-06: 初回登録
