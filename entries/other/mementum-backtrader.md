---
repo: "mementum/backtrader"
name: "backtrader"
genre: other
url: "https://github.com/mementum/backtrader"
license: "GPL-3.0"
stars: 23666
language: "Python"
created: "2015-01-10"
updated: 2024-08-19
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 5320
open_issues: 64
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 22460
archived: false
fetched_at: "2026-11-04T22:53:27Z"
---

# backtrader

## 出来ること

- Python のバックテスト／ライブトレード基盤。`Cerebro` エンジンにデータフィードと戦略を登録して回す。
- 複数データフィード、複数戦略、複数時間軸の同時実行。リサンプリングとリプレイ（日足を分割して日中を模擬する等）、Renko などのフィルタ。
- 指標一式を内蔵し、TA-Lib の指標も使える（`ta-lib` の別途導入が必要）。自作指標の追加が容易。
- アナライザ（TimeReturn、Sharpe Ratio、SQN など）と pyfolio 連携、matplotlib によるチャート出力。
- ライブ取引: Interactive Brokers（`IbPy`）、Oanda（`oandapy`）、Visual Chart。

## 目的・背景

2015年から使われている老舗のバックテストフレームワーク。メタクラスを駆使した宣言的な API と、バックテストとライブを同じコードで扱える設計が特徴。日本語の解説記事も多い。

## 依存関係

- Python 3、`pip install backtrader`。
- チャートに matplotlib。TA-Lib 指標には `ta-lib`、IB 連携には `IbPy` と `pytz`、Oanda 連携には `oandapy`。

## 実行条件

- **最終 push は 2024-08-19** で、以後の更新は止まっている。新規プロジェクトで採用する場合はメンテ状況を踏まえて判断する（フォークや後継の選択肢もある）。
- ライセンスは **GPL-3.0**。組み込んで配布する場合は GPL の条件が及ぶ。
- README の Yahoo データ取得に関する注記は 2018-11-16 時点のもの。現在の Yahoo Finance 側の仕様変更でそのままは動かない可能性がある。

## 最短手順

```bash
pip install backtrader
```

```python
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)
cerebro.run()
cerebro.plot()
```

## 変更履歴

- 2026-11-03: 初回登録（star 23,659 / pushed 2024-08-19 / GPL-3.0）
