---
repo: bmoscon/cryptofeed
name: cryptofeed
genre: other
url: https://github.com/bmoscon/cryptofeed
license: AGPL-3.0
stars: 2976
language: Python
created: 2017-12-16
updated: 2026-11-06
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources: []
flags: []
risk_notes: "AGPL-3.0。改変版をネットワークサービスとして提供する場合はソース公開義務が生じる。取引所のAPI利用規約とレート制限に従うこと。"
forks: 783
open_issues: 0
commits_30d: 50
commits_90d: 86
commit_cadence: daily
size_kb: 1157596
archived: false
fetched_at: "2026-11-06T22:53:19Z"
last_release: v3.0.4
last_release_at: 2026-11-06
---

# cryptofeed

## 出来ること

- 暗号資産取引所の**WebSocketフィードを正規化してコールバックに流す**ライブラリ。取引・板・ticker・資金調達率・建玉などを、取引所ごとの差異を吸収した共通形式で受け取れる。
- WebSocket がない／不安定な取引所は REST ポーリングでも取得できる。
- 対応取引所は30超（Binance 現物・先物・US・Delivery、Bybit、OKX、Kraken・Kraken Futures、Coinbase、Bitfinex、Bitstamp、Bitget、Gate・Gate Futures、HTX・HTX Swap、KuCoin、MEXC、Deribit、Gemini、Crypto.com、Upbit、Bithumb、bitFlyer、Poloniex、Phemex、dYdX v4、Hyperliquid、Independent Reserve など）。
- 受けたデータをそのまま各種バックエンドへ流せる（Redis、PostgreSQL、Kafka、RabbitMQ、ZeroMQ、InfluxDB、MongoDB、ElasticSearch、Arctic、UDP、syslog など）。
- **Windows 対応**（3.0.4）: シグナル処理と import を Windows でも動くようにした。

## 目的・背景

取引所ごとに異なるWebSocketのメッセージ形式・再接続・ハートビートを自前で書くと、ボット本体より接続層の方が大きくなる。cryptofeed はその接続と正規化だけを担い、戦略側は「正規化されたイベントを受ける」ことに集中できるようにする。2017年から継続している定番。

## 依存関係

- Python 3.13 以上（README のバッジ表記）。
- `pip install cryptofeed`。
- バックエンドを使う場合はそれぞれのクライアント（redis、psycopg、aiokafka など）を追加で導入する。

## 実行条件

- **ライセンスは AGPL-3.0**（GitHub API は NOASSERTION だが LICENSE は AGPL）。改変してSaaSとして提供する用途では、ソース公開の義務を確認する必要がある。
- 取引所ごとのレート制限・規約に従う。板の全量購読は帯域とCPUを食う。
- ★2,968・直近30日で46コミット。活発だが、取引所側のAPI変更には追随が必要。

## 最短手順

```bash
pip install cryptofeed

python - <<'PY'
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Coinbase, Kraken
from cryptofeed.defines import TRADES, L2_BOOK

async def trade(t, receipt_timestamp):
    print(f"{t.exchange} {t.symbol} {t.side} {t.amount} @ {t.price}")

async def book(b, receipt_timestamp):
    print(f"{b.exchange} {b.symbol} bid={b.bid[-1][0]} ask={b.ask[-1][0]}")

fh = FeedHandler()
fh.add_feed(Coinbase(symbols=["BTC-USD"], channels=[TRADES],
                     callbacks={TRADES: trade}))
fh.add_feed(Kraken(symbols=["BTC-USD"], channels=[L2_BOOK],
                   callbacks={L2_BOOK: book}))
fh.run()
PY
```

## 変更履歴

- 2026-11-05: 初回登録（★2,968 / pushed 2026-11-05 / AGPL-3.0 / v3.0.3）
- 2026-11-06: Windows 対応（シグナル処理・import）を追記（v3.0.4 / 926cf727）
