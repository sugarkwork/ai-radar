---
repo: "quantopian/zipline"
name: "Zipline (Quantopian)"
genre: finance-quant
url: "https://github.com/quantopian/zipline"
license: "Apache-2.0"
stars: 20224
language: "Python"
created: "2012-10-19"
updated: "2024-02-13"
added: "2026-11-04"
first_seen: "2026-11-04"
sources: []
flags: []
risk_notes: ""
forks: 5064
open_issues: 368
size_kb: 170757
archived: false
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
fetched_at: "2026-11-09T21:37:41Z"
last_release: "1.4.1"
last_release_at: "2020-10-05"
---

# Zipline (Quantopian)

## 出来ること

- イベントドリブン型のバックテストエンジン。`TradingAlgorithm` を継承したクラスに `initialize` / `handle_data` を書き、`zipline run` で回す。
- データは「バンドル」として取り込み、日足・分足を同じ API で扱う。取引所カレンダー、スリッページ・手数料モデル、発注種別（成行・指値・逆指値）を内蔵。
- 成績は pandas の DataFrame で返り、pyfolio / alphalens での分析を前提にした設計。
- テクニカル指標・統計（移動平均、線形回帰など）をアルゴリズム内から直接呼べる。

## 目的・背景

Quantopian がホステッド型のバックテストサービスの中核として公開したライブラリ。当時は「ブラウザで戦略を書いてそのままバックテスト」という体験の土台だった。Quantopian のサービス自体は2020年に終了しており、本リポジトリの開発も事実上止まっている。

## 依存関係

- Python（README の記載は 2.7 / 3.5 / 3.6）。pip または conda で導入するが、通常のパッケージより手順が多い（C 拡張のビルドとデータバンドルの取得が必要）。
- 分析側で pandas、matplotlib、scipy、statsmodels、scikit-learn を使う前提。

## 実行条件

- **最終 push は 2024-02-13**、README の対応 Python は 3.6 まで。現行の Python 環境にそのまま入れるのは現実的でない。
- 現在も開発が続いている後継は **stefan-jansen/zipline-reloaded**（★約2,000、2026-11-02 に push）。新規に試すならそちら。
- ライセンスは Apache-2.0。商用利用時の条件はライセンス本文に従う。

## 最短手順

```bash
# 上流の quantopian/zipline は現行 Python で動かないため、維持されている後継を使う
pip install zipline-reloaded
```

## 変更履歴

- 2026-11-04: 初回登録（★20,200 / pushed 2024-02-13 / Apache-2.0。後継 zipline-reloaded の存在を確認）
