---
repo: freqtrade/freqtrade
name: Freqtrade
genre: other
url: https://github.com/freqtrade/freqtrade
license: GPL-3.0
stars: 56500
language: Python
created: 2017-05-17
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/roundtablespace/status/2118172700757889191
sources:
  - https://www.freqtrade.io
  - https://doi.org/10.21105/joss.04864
flags: []
risk_notes: "暗号資産の自動売買は元本を失う可能性がある。README 自身が educational purposes only と明記し、dry-run から始めるよう警告している。取引所のAPI権限は出金不可のキーを使うこと。"
forks: 11676
open_issues: 24
commits_30d: 100
commits_90d: 100
commit_cadence: daily
size_kb: 832836
archived: false
fetched_at: "2026-11-05T22:44:05Z"
last_release: 2026.10
last_release_at: 2026-10-30
---

# Freqtrade

## 出来ること

- Python 製の**暗号資産トレーディングボット**。戦略の記述、バックテスト、ドライラン、実取引を1つのCLIで回す。
- **バックテスト**: 過去データでの検証、損益曲線のプロット、複数戦略の比較。
- **ドライラン**: 実際の相場データで注文をシミュレートし、資金を動かさずに挙動を確認。
- **ハイパーパラメータ最適化**（hyperopt）と、機械学習による戦略改善（FreqAI）。
- Telegram と WebUI から操作・監視。ポジション管理、ストップロス、トレーリング、資金管理を含む。
- 対応取引所は現物・先物合わせて20超（Binance、Bybit、OKX、Kraken、Gate、HTX、Bitget、BingX など）。Docker イメージも配布。

## 目的・背景

「ボットを書く」より「戦略を検証してから動かす」ことに重心を置いたフレームワーク。JOSS の論文があり、バックテストとドライランを必須の手順として README でも強く案内している。2017年から続く定番で、★5.6万。

## 依存関係

- Python 3.12 以上（2026.10 で Python 3.11 のサポートが終了した）。
- TA-Lib（テクニカル指標）と技術計算系の依存。Docker イメージなら同梱済み。
- 取引所のAPIキー（実取引のみ）。読み取り＋取引権限で足り、**出金権限は付けない**。

## 実行条件

- README の免責: **educational purposes only**。失って困る資金を入れない。まず dry-run。
- GPL-3.0。改変して配布する場合はソース公開義務。
- 高頻度の取引所API呼び出しになるため、レート制限と手数料をバックテストに反映させる（手数料を入れない検証は実運用と乖離する）。

## 最短手順

```bash
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade
./setup.sh -i                 # 仮想環境と依存を導入

freqtrade create-userdir --userdir user_data
freqtrade new-config --config user_data/config.json
freqtrade download-data --config user_data/config.json --timeframe 5m --days 90
freqtrade backtesting --config user_data/config.json --strategy SampleStrategy
freqtrade trade --config user_data/config.json --strategy SampleStrategy --dry-run
```

## 変更履歴

- 2026-11-05: 初回登録（★56,497 / pushed 2026-11-05 / GPL-3.0 / 2026.10）
- 2026-11-05: 2026.10 の要件を反映 — Python は 3.12 以上（3.11 のサポート終了）、注文板の websocket 対応、戦略パラメータはインスタンス単位（`self.<param>.value`）に変更（0789f5d）
