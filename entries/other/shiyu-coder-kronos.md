---
repo: "shiyu-coder/Kronos"
name: "Kronos"
genre: other
url: "https://github.com/shiyu-coder/Kronos"
license: "MIT"
stars: 46488
language: "Python"
created: "2025-07-01"
updated: 2026-04-13
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 7660
open_issues: 295
commits_30d: 0
commits_90d: 0
commit_cadence: stale
size_kb: 9539
archived: false
fetched_at: "2026-11-03T22:57:50Z"
---

# Kronos

## 出来ること

- K線（OHLCV）専用の自己回帰型基盤モデル。連続値のK線を階層的な離散トークンに量子化する専用トークナイザと、そのトークンで事前学習した Transformer の2段構成。
- `KronosPredictor` に過去のK線 DataFrame とタイムスタンプを渡すだけで、正規化・推論・逆正規化までを一括で行い将来のK線を予測する。
- モデルは4サイズ: Kronos-mini（4.1M, 文脈2048）/ small（24.7M）/ base（102.3M）（いずれも文脈512）/ large（499.2M, **非公開**）。mini・small・base は Hugging Face の `NeoQuasar/*` で公開。
- BTC/USDT の24時間予測を見せるライブデモと、独自データへ適応させるファインチューニング用スクリプトを公開。

## 目的・背景

金融時系列は汎用の時系列基盤モデルが前提とする性質と違い、ノイズが大きく非定常。そこに合わせて「市場の言語」としてのK線列を扱うために作られたモデルで、45以上の取引所のデータで学習している。論文は arXiv 2508.02739、AAAI 2026 に採択（リポジトリ記載）。予測単体ではなく、定量タスク全般の基盤として使うことを想定している。

## 依存関係

- Python 3.10 以上。
- `pip install -r requirements.txt`（PyTorch を含む）。
- モデル重みは初回実行時に Hugging Face から取得。

## 実行条件

- 入力の `max_context` は small / base で **512**。`lookback` もこの範囲に収める（超過分は Predictor 側で切り捨て）。
- 入力 DataFrame に必要な列は `open` / `high` / `low` / `close`。`volume` / `amount` は任意。
- GPU があると速いが、モデルが小さいため CPU でも動作する（README に所要時間の記載はなし）。
- 予測精度の独立した検証結果は公開されていない。投資判断への利用は自己責任。

## 最短手順

```bash
git clone https://github.com/shiyu-coder/Kronos.git
cd Kronos
pip install -r requirements.txt
```

```python
from model import Kronos, KronosTokenizer, KronosPredictor

tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = Kronos.from_pretrained("NeoQuasar/Kronos-small")
predictor = KronosPredictor(model, tokenizer, max_context=512)
```

## 変更履歴

- 2026-11-03: 初回登録（star 46,488 / pushed 2026-04-13 / MIT）
