---
repo: duckdb/duckdb
name: DuckDB
genre: other
url: https://github.com/duckdb/duckdb
license: MIT
stars: 42850
language: C++
created: 2018-06-26
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://duckdb.org/
flags: []
risk_notes: ""
forks: 4163
open_issues: 1121
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 575106
archived: false
fetched_at: "2026-11-05T22:09:44Z"
last_release: v2.0.0
last_release_at: 2026-10-21
---

# DuckDB

## 出来ること

- **プロセス内で動く分析用SQLデータベース**。サーバーを立てず、Python/R/Java/Node/WASM から埋め込みで使う。列指向＋ベクトル化実行で、集計クエリが速い。
- **Parquet / CSV / JSON を直接SQLで読める**。`SELECT * FROM 'trades.parquet'` のようにファイルをそのままテーブル扱いでき、ロード不要。S3等のリモートも読める。
- pandas / Arrow とゼロコピーで相互変換できる。大量のティック・OHLCVを pandas で扱うよりメモリ効率が良く、バックテスト前の集計に向く。
- トランザクション、ビュー、ウィンドウ関数、CTE、JSON関数など、分析用SQLの機能は一通り揃っている。拡張機能（httpfs、parquet、iceberg など）を追加できる。

## 目的・背景

「分析用のデータがCSV/Parquetで手元にあるのに、毎回DBサーバーを立てるのは重い」という隙間を埋める。SQLite がOLTP向けなのに対し、DuckDB はOLAP（集計・スキャン）に振っている。データサイエンスの前処理で pandas の代替として使われることが増えた。

## 依存関係

- Python なら `pip install duckdb`（ホイール同梱、外部依存なし）。
- 他言語も公式バインディングあり（R の DBI、Java JDBC、Node、WASM、CLI）。
- バージョンは **v2.0.0**（2026-11 時点）。

## 実行条件

- **単一プロセス・単一ライター**の設計。同時書き込みが大量にあるサービス用途ではなく、分析・バッチ向け。読み取りは並列可。
- メモリ上限（`memory_limit`）と一時ディレクトリ（`temp_directory`）を設定しないと、大きな結合でOOMになりやすい。
- データを「ファイルのまま」読む場合、スキーマ変更や型の揺れ（CSVの日付など）は自分で指定する。

## 最短手順

```bash
pip install duckdb
```

```python
import duckdb

# Parquet を直接集計
df = duckdb.sql("""
    SELECT symbol, date_trunc('day', ts) AS d, sum(size) AS volume, avg(price) AS vwap
    FROM 'trades/*.parquet'
    WHERE ts >= '2026-01-01'
    GROUP BY ALL
    ORDER BY d, symbol
""").df()

# pandas をそのまま参照
import pandas as pd
orders = pd.DataFrame({"symbol": ["BTC-USD"], "qty": [0.5]})
print(duckdb.sql("SELECT * FROM orders WHERE qty > 0.1").df())
```

## 変更履歴

- 2026-11-05: 初回登録（★42,849 / pushed 2026-11-05 / MIT / v2.0.0）
