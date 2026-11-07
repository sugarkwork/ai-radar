---
repo: ranaroussi/quantstats
name: QuantStats
genre: finance-quant
url: https://github.com/ranaroussi/quantstats
license: Apache-2.0
stars: 7798
language: Python
created: 2019-05-01
updated: 2026-11-02
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources: []
flags: []
risk_notes: ""
forks: 1272
open_issues: 32
commits_30d: 1
commits_90d: 10
commit_cadence: monthly
size_kb: 5992
archived: false
fetched_at: "2026-11-05T22:02:16Z"
last_release: v0.0.86
last_release_at: 2026-09-27
---

# QuantStats

## 出来ること

- リターン系列から**ポートフォリオの成績とリスク指標**を一括で計算する。シャープ、ソルティノ、最大ドローダウン、勝率、ボラティリティ、月次リターンなど。
- 3つのモジュール構成: `quantstats.stats`（指標）、`quantstats.plots`（チャート）、`quantstats.reports`（HTMLティアシート）。
- **HTMLレポート**を1行で出力できる。資産曲線、ドローダウン、月次ヒートマップ、ローリング統計をまとめた1枚もの。
- Monte Carlo シミュレーション（`qs.stats.montecarlo`）で、破産確率・目標到達確率を確率的に評価できる。
- `qs.extend_pandas()` で pandas の Series/DataFrame に `.sharpe()` などを生やせる。

## 目的・背景

バックテストの結果を「数字の羅列」で終わらせず、人に見せられる形にするための分析層。バックテストエンジン（vectorbt、backtrader など）や実際の口座履歴から得たリターン系列を渡して使う。作者は yfinance と同じ ranaroussi。

## 依存関係

- Python 3.10 以上、pandas、NumPy、matplotlib、scipy。
- `pip install quantstats`。

## 実行条件

- 入力は**リターン**（日次なら `pct_change()` 済みの系列）。価格をそのまま渡すと指標が壊れる。
- 手数料・スリッページを含めたネットのリターンを渡すこと。グロスで出すと実運用より良く見える。
- ★7,798 だが直近30日のコミットは1件（v0.0.86）。メンテナンスは低調なので、pandas の新バージョンで挙動が変わる可能性がある。

## 最短手順

```bash
pip install quantstats
```

```python
import pandas as pd, quantstats as qs

returns = pd.read_csv("returns.csv", index_col=0, parse_dates=True)["strategy"]
benchmark = pd.read_csv("returns.csv", index_col=0, parse_dates=True)["spy"]

qs.reports.html(returns, benchmark=benchmark, output="report.html")
print(qs.stats.sharpe(returns), qs.stats.max_drawdown(returns))
```

## 変更履歴

- 2026-11-05: 初回登録（★7,798 / pushed 2026-11-02 / Apache-2.0 / v0.0.86）
