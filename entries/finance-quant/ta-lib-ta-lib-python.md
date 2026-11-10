---
repo: TA-Lib/ta-lib-python
name: TA-Lib Python
genre: finance-quant
url: https://github.com/TA-Lib/ta-lib-python
license: BSD-2-Clause
stars: 12395
language: Cython
created: 2012-03-23
updated: "2026-11-09"
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://ta-lib.org/
flags: []
risk_notes: ""
forks: 2009
open_issues: 88
commits_30d: 36
commits_90d: 60
commit_cadence: "daily"
size_kb: 86934
archived: false
fetched_at: "2026-11-09T21:37:59Z"
last_release: "v0.8.3"
last_release_at: "2026-10-28"
---

# TA-Lib Python

## 出来ること

- テクニカル分析の計算を**C実装のまま Python から呼ぶ**ラッパー。ADX、MACD、RSI、ストキャスティクス、ボリンジャーバンドなど **200以上の指標**をカバーする。
- NumPy 配列・pandas Series をそのまま渡せる。`talib.RSI(close, timeperiod=14)` のように関数として呼ぶ形と、指標の状態を保持して1本ずつ更新する **Streaming API** の両方がある。
- Cython で書かれているため、pandas の `rolling().apply()` で同じ計算をするより速い。大量の銘柄・長い期間のバックテスト前処理に向く。

## 目的・背景

テクニカル指標の計算は定義が細かく、実装ごとに初期値や端の扱いが違う。TA-Lib は C の老舗ライブラリ（ta-lib.org）を正とし、Python 側はその薄いラッパーに徹することで、他言語・他ツールと同じ数値になることを狙う。

## 依存関係

- **TA-Lib の C ライブラリ本体（0.4 系）が別途必要**。Python パッケージだけでは動かない。
  - macOS: `brew install ta-lib`
  - Ubuntu/Debian: `apt install ta-lib`（無い場合はソースから）
  - conda: `conda install -c conda-forge ta-lib`（C ライブラリも同時に入る）
- Python 3.9 以上、NumPy。pandas 連携は任意。

## 実行条件

- C ライブラリが見つからないと `pip install TA-Lib` がビルドで落ちる。先に本体を入れるか、conda-forge を使う。
- 指標の一部は入力の長さが足りないと NaN を返す（例: 200期間のSMAは最初の199本が NaN）。バックテストでは先頭を捨てる前提で組む。
- ★12,369・直近30日で38コミット。v0.8.3。

## 最短手順

```bash
# C ライブラリを先に入れる（例: conda）
conda install -c conda-forge ta-lib
# または brew install ta-lib / apt install ta-lib

pip install TA-Lib
```

```python
import pandas as pd, talib
close = pd.read_csv("ohlcv.csv")["close"]
df = pd.DataFrame({
    "rsi": talib.RSI(close, timeperiod=14),
    "macd": talib.MACD(close, 12, 26, 9)[0],
    "upper": talib.BBANDS(close, 20, 2, 2)[0],
})
print(df.tail())
```

## 変更履歴

- 2026-11-05: 初回登録（★12,369 / pushed 2026-11-05 / BSD-2-Clause / v0.8.3）
