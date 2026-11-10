---
repo: "truongxxxx/jev-polymarket-test"
name: "jev-polymarket-test"
genre: "finance-quant"
url: "https://github.com/truongxxxx/jev-polymarket-test"
stars: 0
forks: 0
open_issues: 0
size_kb: 764
language: "Python"
created: "2026-10-10"
updated: "2026-10-10"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 2
commit_cadence: "stale"
flags: ["unverified"]
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
risk_notes: ""
sources: ["https://x.com/thegreatest_sv/status/2115461838607659474"]
fetched_at: "2026-11-10T12:20:49+00:00"
---

# jev-polymarket-test — Jevの予測をPolymarketの価格と比較する評価コード

## 出来ること

- 市場の質問と解決ルールだけを渡す条件と、24時間前のYes価格も渡す条件でJevを比較する。市場価格を基準にBrierスコア、対数損失、AUC、校正を評価できる。

## 目的・背景

- 著者は解決済み26,174市場を評価。モデル公開後に解決した9,138市場では、AUCは市場価格0.844、テキストのみのJev 0.615、価格付きのJev 0.794だった。
- 著者報告の応答時間中央値は284 ms。約0.79米ドルはテキストのみの条件の費用で、READMEでは全体を2米ドル未満と記載している。

## 依存関係

- Python 3.11以上、typesafe-sdk、NumPy、SciPy、scikit-learn、Matplotlib。市場一覧はPolymarketの公開Gamma API、価格履歴は公開CLOB APIを利用する。

## 実行条件

- Jevへの実リクエストには環境変数または.envのTYPESAFE_API_KEYが必要。コードはMITで、READMEによると市場データは同梱して再配布していない。

## 最短手順

- 既存の結果はjev/report.mdで読める。再評価する場合は、READMEに沿ってfetch_markets.pyとfetch_prices.pyで市場と価格履歴を取得し、jev/make_dataset.pyで入力を作る。
- AIエージェントからはシェル経由で `python jev/run_jev.py --variant blind --dry-run` を使って入力を確認する。実リクエストを行う場合は、キーを環境で設定し、同スクリプトをblindとpricedの各条件で実行してから `python jev/evaluate.py` で集計する。

## 変更履歴

- 2026-11-10: 初回登録
