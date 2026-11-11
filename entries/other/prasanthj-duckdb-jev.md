---
repo: "prasanthj/duckdb-jev"
name: "duckdb-jev"
genre: "other"
url: "https://github.com/prasanthj/duckdb-jev"
last_release: "v0.2.2"
flags: ["unverified"]
risk_notes: "性能値は開発者が合成データで計測したもので、独立再測定、実データでの分類精度、TypeSafeの現行料金・データ保持条件は未確認。公開リリースのタグは確認済みで、公開日時と配布物の動作は未確認。"
stars: 14
forks: 3
open_issues: 2
size_kb: 1390
language: "C++"
created: "2026-09-20"
updated: "2026-10-21"
archived: false
license: "Apache-2.0"
commits_30d: 2
commits_90d: 39
commit_cadence: "monthly"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2116142322543198271"]
fetched_at: "2026-11-10T12:55:22Z"
---

# duckdb-jev — DuckDBのSQLからJevで行を分類・採点する

## 出来ること

- SQLから二値判定、候補ラベルへの分類、順序付き尺度での採点を行う。テキスト、JSON、DuckDBのSTRUCT・LIST・ARRAYを入力にできる。

## 目的・背景

- jev_streamは複数行の判定をHTTPリクエストにまとめ、DuckDBのチャンクをまたいで並行処理する。
- 開発者がmacOS arm64上のDuckDB 1.5.5とjev-1.13.0で行った合成データの計測では、同じ100行の分類がバッチ1・並列度1で中央値16.828秒、バッチ25・並列度10で0.211秒。別の2,049行の試行ではバッチ100・並列度10で0.991秒だった。

## 依存関係

- DuckDBのバージョンとプラットフォームに合うネイティブ拡張が必要。ソースビルドにはuv、Git、C++17コンパイラ、libcurlの開発用ヘッダーとライブラリを使う。拡張のライセンスはApache-2.0。

## 実行条件

- 推論にはTypeSafe APIの認証情報と外部通信が必要で、判定対象データはTypeSafeへ送信される。DuckDBで外部アクセスを無効にするとリクエストできない。配布バイナリのロードには未署名拡張を許可したDuckDBセッションが必要。

## 最短手順

- GitHub Releasesで手元のDuckDBとOS・CPUに合う配布物を選び、公開チェックサムを照合する。DuckDBを `duckdb -unsigned` で起動し、`LOAD '/path/to/jev.duckdb_extension'` を実行する。
- 一時的なDuckDBのjevシークレットにTypeSafe APIキーを設定する。SQLを実行できるAIエージェントからは、設定済みのDuckDB接続で `SELECT jev('Customer requests a refund', 'Is a refund requested?', 0.8)` を実行して真偽値を受け取る。

## 変更履歴

- 2026-11-11: 初回登録
