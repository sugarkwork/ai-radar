---
repo: "ccxt/ccxt"
name: "CCXT"
genre: finance-quant
url: "https://github.com/ccxt/ccxt"
license: "MIT"
stars: 44774
language: "Python"
created: "2017-05-14"
updated: 2026-11-06
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 8956
open_issues: 772
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 8895675
archived: false
fetched_at: "2026-11-06T22:54:18Z"
last_release: v4.5.92
last_release_at: 2026-11-04
---

# CCXT

## 出来ること

- 100以上の暗号資産取引所と予測市場（Polymarket / Kalshi / Hyperliquid / Limitless / Myriad）を、1つの統一 API で扱うライブラリ。
- 公開 API と私有 API の両方、REST と WebSocket に対応。取引所ごとに異なる通貨コード・注文形式・レスポンスを正規化し、取引所間の比較やアービトラージに使える形にする。
- 対応言語は JavaScript / TypeScript / Python / C# / PHP / Go / Java / Rust。Node 18+、Python 3、PHP 8.1+、Go 1.20+、Java 21+ で動く。
- マーケットデータの取得・保存、指標計算、バックテスト、ボット実装までを同じインターフェースで書ける。
- **公式 MCP サーバ**: `npx -y ccxt-mcp` で stdio の MCP サーバが起動し、100以上の取引所と予測市場のマーケットデータ・残高をエージェントから扱える。取引・出金・生エンドポイントは既定オフの別ケーパビリティ層で、確認フロー・上限額・監査ジャーナル付き。API キーはローカルに留まり、モデルにはアカウント名だけを渡す。v4.5.92 で `fetch_route` / `execute_route`（OrderRouter 経由）が加わった。
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
- 2026-11-06: 公式 MCP サーバ（`ccxt-mcp`）と OrderRouter の `fetch_route` / `execute_route` を追記（v4.5.92 / 31077）
