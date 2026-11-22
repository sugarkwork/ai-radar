---
name: "AKShare"
genre: "finance-quant"
url: "https://github.com/akfamily/akshare"
repo: "akfamily/akshare"
license: "MIT"
stars: 23360
language: "Python"
created: "2019-10-01"
updated: "2026-11-16"
forks: 3577
open_issues: 2
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 9631
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118857714390733011"]
fetched_at: "2026-11-16T21:49:55Z"
last_release: "v1.20.65"
last_release_at: "2026-11-15"
---

# AKShare

## 出来ること

- Pythonから財経データを取得し、オフラインのインターフェースレジストリをキーワード検索できます。READMEには株価データ取得、検索結果・インターフェース情報の表示、mplfinanceによるチャート描画の例があります。出典: https://github.com/akfamily/akshare

## 目的・背景

- 財経データの取得を簡単にし、Pythonのデータ分析・量化投研の用途で利用するライブラリです。出典: https://github.com/akfamily/akshare

## 依存関係

- READMEの利用例ではPythonパッケージとしてakshareを読み込みます。プロット例では別途mplfinanceをインストールします。AKShare本体はMCPサーバーではなく、MCPサーバー機能は別プロジェクトのAKToolsが提供するとREADMEに記載されています。出典: https://github.com/akfamily/akshare

## 実行条件

- README記載の要件は64-bit Python 3.11.5以上です。データ取得の例はインターフェースを呼び出してデータを取得します。出典: https://github.com/akfamily/akshare

## 最短手順

- README記載のインストール例: `uv pip install akshare --upgrade`。使用例では `import akshare as ak` の後、`ak.stock_zh_a_hist_em(...)` などのインターフェースを呼び出します。出典: https://github.com/akfamily/akshare

## 変更履歴

- 2026-11-14: 初回登録
