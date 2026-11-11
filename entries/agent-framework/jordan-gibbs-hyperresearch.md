---
repo: "jordan-gibbs/hyperresearch"
name: "hyperresearch"
genre: "agent-framework"
url: "https://github.com/jordan-gibbs/hyperresearch"
last_release: "v0.13.1"
flags: ["unverified"]
risk_notes: "READMEの250件以上はpremier設定に関する開発元の説明。収集件数と引用監査の精度は独立に実測していない。READMEでは引用監査の対象範囲に関する記述が一致せず、全件を点検するかは未確認。最新GitHubリリースの公開日時は未確認。"
stars: 4482
forks: 462
open_issues: 15
size_kb: 6644
language: "Python"
created: "2026-04-09"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 27
commits_90d: 71
commit_cadence: "daily"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/opensourcelab9/status/2116296617716486320"]
fetched_at: "2026-11-10T13:06:39Z"
---

# hyperresearch — Claude Codeで出典付きレポートを作り、資料を再利用する調査スキル

## 出来ること

- 問いを起点に公開資料を収集し、出典付きの調査レポートを作る。フル調査では、4つの批評役による並行レビューと、引用先が本文の主張を支えるかを点検する工程がある。
- 資料ノートをMarkdownで保存し、SQLiteの索引で全文検索できる。後続の調査は新規取得の前に蓄積済みの資料を検索する。

## 目的・背景

- 調査を問いの分解、資料収集、分析、執筆、監査に分け、Claude Codeが工程ごとのスキルを呼ぶ構成。開発元が掲げる250件以上はpremier設定の説明で、収集量は設定や問いに依存する。

## 依存関係

- Claude Codeで使う場合はPythonとhyperresearch CLIが必要。READMEのインストール欄に記載されたPythonの範囲は3.11〜3.14。標準の取得方式はHTTPで、ExaやTavilyを選ぶ場合は各サービスのAPIキーが必要。

## 実行条件

- 公開資料を取得するためのネットワーク接続と、スキルや資料ノートを書き込める作業ディレクトリが必要。リポジトリはMITライセンス。Claude Codeや任意の外部サービスの利用条件・料金は各サービスに従う。

## 最短手順

- 作業ディレクトリで `pip install hyperresearch`、続けて `hyperresearch install` を実行する。
- 同じディレクトリでClaude Codeを開き、`/hyperresearch <調べたい問い>` を入力する。起動済みでスキルが認識されない場合は、同じディレクトリでClaude Codeを再起動する。
- MCP対応クライアントから同じ資料庫を使う場合は、`pip install 'hyperresearch[mcp]'` で追加依存を入れ、クライアントのstdioサーバーに `hyperresearch mcp` を設定する。

## 変更履歴

- 2026-11-11: 初回登録
