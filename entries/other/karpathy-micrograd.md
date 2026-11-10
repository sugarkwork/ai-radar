---
repo: "karpathy/micrograd"
name: "micrograd"
genre: "other"
url: "https://github.com/karpathy/micrograd"
license: "MIT"
stars: 18805
language: "Jupyter Notebook"
created: "2020-04-13"
updated: "2026-08-03"
forks: 2993
open_issues: 84
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 241
archived: false
flags: ["unverified"]
risk_notes: "勾配の一致、分類デモの再現性、実行性能、Python バージョンごとの動作は独立実測していない。GitHub の公開 Releases 一覧にはリリースが表示されていないため、最新リリースの版と日時は未記載。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:50:45+00:00"
---

# microgradでスカラー演算の逆伝播をたどる

## 出来ること

- Python の Value でスカラーの計算グラフを組み立て、backward() で各入力の勾配を求められる。README には MLP を SGD で学習させる二値分類の例もある。

## 目的・背景

- 演算ごとの局所勾配を出力側から伝える逆モード自動微分を、加算や乗算の単位で追う教材。著者は PyTorch を参照に勾配を検証するテスト手順を示している。

## 依存関係

- 公開実装では自動微分と MLP の中核に外部ライブラリのインポートは見当たらない。公式の勾配テストには PyTorch と pytest、計算グラフの可視化には Graphviz を使う。

## 実行条件

- setup.py の宣言は Python 3.6 以上。ソースは MIT ライセンスで公開されている。

## 最短手順

- README に従って `pip install micrograd` で導入する。
- Python で `from micrograd.engine import Value` を実行し、`x = Value(3.0)` と `y = x * x` を作る。`y.backward()` を呼んで `x.grad` を確認する。期待値は x² の微分から 6.0。
- 学習ループまで追う場合は `demo.ipynb` で損失計算、逆伝播、SGD による更新の順に読む。

## 変更履歴

- 2026-11-10: 初回登録
