---
repo: polakowo/vectorbt
name: vectorbt
genre: finance-quant
url: https://github.com/polakowo/vectorbt
license: Apache-2.0 + Commons Clause（販売不可）
stars: 9692
language: Python
created: 2017-11-14
updated: 2026-11-03
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://vectorbt.dev/
flags: []
risk_notes: "Apache-2.0 に Commons Clause が付き、このライブラリの機能を主要価値とする製品・サービスを有償提供することはできない。有償版の vectorbt PRO が別に存在する。"
forks: 1258
open_issues: 135
commits_30d: 53
commits_90d: 65
commit_cadence: daily
size_kb: 759947
archived: false
fetched_at: "2026-11-05T22:01:17Z"
last_release: v1.2.0
last_release_at: 2026-10-19
---

# vectorbt

## 出来ること

- **ベクトル化されたバックテストエンジン**。値動き・シグナル・注文・ポジションを NumPy 配列として一括処理し、Numba でコンパイルして回す。ループで1本ずつ検証するより桁違いに速い。
- パラメータの総当たり（数千通りのエントリー／イグジット条件）を現実的な時間で回せる。`Portfolio.from_signals` などのAPIで、手数料・スリッページ・分割注文まで含めた検証ができる。
- 結果の可視化（Plotly）と統計（勝率、ドローダウン、シャープレシオなど）。Jupyter 上での試行錯誤に向く。
- 同じコードで暗号資産・株式・FX のOHLCVデータを扱える（データ取得は別ライブラリ）。

## 目的・背景

「1つの戦略を丁寧に検証する」より「大量の仮説を高速にふるいにかける」ための研究エンジン。README の説明も "Run thousands of trading ideas before others finish one" と、探索速度を前面に出している。開発の中心は有償版の vectorbt PRO に移っており、OSS版は安定版として維持されている。

## 依存関係

- Python 3.10 以上、NumPy / pandas / Numba / Plotly。
- `pip install vectorbt`（Docker イメージ `polakowo/vectorbt` も配布）。

## 実行条件

- **ライセンスは Apache-2.0 + Commons Clause**。「vectorbt の機能に価値の大半を依存する製品・サービスを有償で第三者に提供する」ことが禁止される。社内利用・研究・自己売買は可。商用SaaSにするなら vectorbt PRO の契約が別途必要。
- Numba の初回コンパイルに時間がかかる。大量のパラメータを一度に回すとメモリを食うので、分割実行する。
- ★9,692・直近30日のコミット53。OSS版の更新は緩やか。

## 最短手順

```bash
pip install vectorbt

python - <<'PY'
import numpy as np, pandas as pd, vectorbt as vbt

price = pd.Series(np.cumsum(np.random.randn(500)) + 100)
fast, slow = price.rolling(10).mean(), price.rolling(30).mean()
entries, exits = fast > slow, fast < slow

pf = vbt.Portfolio.from_signals(price, entries, exits, fees=0.001)
print(pf.stats())
PY
```

## 変更履歴

- 2026-11-05: 初回登録（★9,692 / pushed 2026-11-03 / Apache-2.0+Commons Clause / v1.2.0）
