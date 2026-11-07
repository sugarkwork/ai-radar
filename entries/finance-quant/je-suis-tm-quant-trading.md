---
repo: "je-suis-tm/quant-trading"
name: "quant-trading"
genre: finance-quant
url: "https://github.com/je-suis-tm/quant-trading"
license: "Apache-2.0"
stars: 11190
language: "Python"
created: "2018-04-03"
updated: 2026-06-20
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 1954
open_issues: 1
commits_30d: 0
commit_cadence: stale
size_kb: 13020
archived: false
commits_90d: 0
fetched_at: "2026-11-03T23:05:54Z"
---

# quant-trading

## 出来ること

- テクニカル指標ベースの売買戦略を、1戦略1スクリプトで17本そろえた実装集。
  - MACD、ペアトレード、平均足（Heikin-Ashi）、London Breakout、Awesome Oscillator、Dual Thrust、パラボリック SAR。
  - ボリンジャーバンドと RSI のパターン認識、モンテカルロ、オプション・ストラドル、VIX 計算、ポートフォリオ最適化。
  - ほかに原油の在庫データを使う Oil Money、スマート農業、群衆の知恵といった実験的プロジェクト。
- 各スクリプトが独立していて、部分だけ読んで手法を学べる。バックテストとフォワードテストのコードがセットになっている。
- データ取得用のスクレイパ（CME、LME、Macrotrends、WallStreetBets など）は別リポジトリで公開されている。

## 目的・背景

「テクニカル指標の自動売買」を、考え方の説明とコードを並べて読める形で残した個人プロジェクト。README は指標の背景（行動経済学的な自己成就性など）にも紙幅を割いている。

## 依存関係

- Python（pandas / numpy / matplotlib など）。共通パッケージとして配布されているわけではなく、スクリプトごとに import を揃える必要がある。
- データは各自で用意: yfinance、Stooq、HistData、Quandl、Macrotrends など。Bloomberg / Eikon は有料契約が必要。

## 実行条件

- **README が明記している前提: 手数料・スリッページを考慮しない「摩擦なし」のヒストリカル・バックテスト**。この結果をそのまま実運用の成績として読むことはできない。
- HFT は対象外（超高頻度データが高価であることを理由に明記）。実装は Python で、C++ ではない。
- 最終 push は 2026-06-20 で、以後の更新は止まっている。依存ライブラリの仕様変更には追随していない可能性がある。

## 最短手順

```bash
git clone https://github.com/je-suis-tm/quant-trading.git
cd quant-trading
# 戦略ごとにスクリプトを個別に実行（例: MACD oscillator.py）
```

## 変更履歴

- 2026-11-03: 初回登録（★11,190 / pushed 2026-06-20 / Apache-2.0）
