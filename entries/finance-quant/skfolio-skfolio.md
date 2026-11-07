---
repo: skfolio/skfolio
name: skfolio
genre: finance-quant
url: https://github.com/skfolio/skfolio
license: BSD-3-Clause
stars: 2593
language: Python
created: 2023-12-14
updated: 2026-10-29
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://skfolio.org
flags: []
risk_notes: ""
forks: 301
open_issues: 37
commits_30d: 87
commits_90d: 100
commit_cadence: daily
size_kb: 17498
archived: false
fetched_at: "2026-11-05T22:02:06Z"
last_release: v1.12.5
last_release_at: 2026-10-29
---

# skfolio

## 出来ること

- **ポートフォリオ最適化を scikit-learn の API で**扱うライブラリ。`fit` / `predict` / `get_params` がそのまま使え、`Pipeline` や `GridSearchCV` に組み込める。
- 手法の幅が広い: 平均分散最適化（MVO）、整合的リスク指標、左裾リスク、分布ロバスト最適化（DRO）、リスクパリティ、階層クラスタリング（HRP/HERC）、Nested Clusters Optimization、Stacking。
- ファクターモデル（時系列・特性ベースのクロスセクション）と、ウォークフォワード／コンビネーションベースの交差検証を同梱。
- 制約（ウェイト上限、取引コスト、ターンオーバー）を最適化に直接入れられる。

## 目的・背景

ポートフォリオ最適化の実装は論文ごとにAPIがバラバラで、バックテストに組み込むたびに配線し直すことになる。skfolio は scikit-learn の推定器として統一し、前処理（リターン推定）→最適化→評価をパイプラインとして扱えるようにする。2023年末公開、学術書 "Portfolio Optimization: Theory and Application" のコード例にも使われている。

## 依存関係

- Python 3.10〜3.14、scikit-learn、NumPy、pandas、SciPy。
- `pip install skfolio`。

## 実行条件

- 入力はリターンの時系列（資産×時間）。価格のまま渡さない。
- 最適化の前にリターン推定器（平均・共分散、収縮推定量など）を置く構成が前提。推定誤差がそのままウェイトに効くため、交差検証で評価する。
- ★2,593・直近30日で89コミットと開発は活発。v1.12.5。

## 最短手順

```bash
pip install skfolio
```

```python
from skfolio.datasets import load_sp500_dataset
from skfolio.optimization import MeanRisk
from skfolio.preprocessing import prices_to_returns

prices = load_sp500_dataset()
X = prices_to_returns(prices)

model = MeanRisk()          # 既定は最小分散
model.fit(X)
print(model.weights_.head())

portfolio = model.predict(X)
print(portfolio.summary())
```

## 変更履歴

- 2026-11-05: 初回登録（★2,593 / pushed 2026-10-29 / BSD-3-Clause / v1.12.5）
