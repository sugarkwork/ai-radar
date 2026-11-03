---
repo: "ccxt/ccxt"
name: "CCXT"
genre: other
url: "https://github.com/ccxt/ccxt"
license: "MIT"
stars: 44704
language: "Python"
created: "2017-05-14"
updated: 2026-11-03
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 8940
open_issues: 756
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 8891466
archived: false
fetched_at: "2026-11-03T22:59:04Z"
last_release: v4.5.91
last_release_at: 2026-10-29
---

# CCXT

## 出来ること

- 100以上の暗号資産取引所と予測市場（Polymarket / Kalshi / Hyperliquid / Limitless / Myriad）を、1つの統一 API で扱うライブラリ。
- 公開 API と私有 API の両方、REST と WebSocket に対応。取引所ごとに異なる通貨コード・注文形式・レスポンスを正規化し、取引所間の比較やアービトラージに使える形にする。
- 対応言語は JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust。Node 18+、Python 3、PHP 8.1+、Go 1.20+、Java 21+ で動く。
- マーケットデータの取得・保存、指標計算、バックテスト、ボット実装までを同じインターフェースで書ける。
- Web 版の CCXT Terminal（別サービス）への導線あり。

## 目的・背景

取引所ごとに API 仕様がバラバラだと、戦略を1つ書くたびに接続コードを書き直すことになる。CCXT は取引所アダプタを吸収する層を提供し、コードを変えずに取引所を差し替えられるようにする。暗号資産の文脈で事実上の標準として使われている。

## 依存関係

- `pip install ccxt` / `npm install ccxt` / 各言語のパッケージマネージャ。
- 私有 API を使う場合は取引所の API キーとシークレット。

## 実行条件

- リポジトリが非常に大きい（API 上 約8.9GB）。clone して使うより、パッケージとして入れる方が現実的。
- 取引所ごとに対応状況が異なる。使う予定のメソッドがその取引所で実装済みか、マニュアルの対応表で確認する。
- 実際の発注は自己責任。API キーの権限は出金不可など最小限にする。

## 最短手順

```bash
pip install ccxt
```

```python
import ccxt
ex = ccxt.binance()
print(ex.fetch_ticker("BTC/USDT")["last"])
```

## 変更履歴

- 2026-11-03: 初回登録（star 44,704 / pushed 2026-11-03 / MIT）
