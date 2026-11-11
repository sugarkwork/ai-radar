---
repo: "usail-hkust/JevLight"
name: "JevLight"
genre: "eval"
url: "https://github.com/usail-hkust/JevLight"
license: "unknown"
stars: 11
language: "Python"
created: "2026-09-21"
updated: "2026-11-06"
forks: 2
open_issues: 0
commits_30d: 10
commit_cadence: "weekly"
commits_90d: 29
size_kb: 81755
archived: false
flags: ["unverified"]
risk_notes: "模擬実験を含めコードは実行していない。著者のSUMO集計はREADMEの記述を確認した範囲で、個別のスコア、独立再現、実道路での有効性、実APIの料金・利用条件、最新リリースは未確認。ライセンスは提供されたGitHub API実測値でunknown。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2115779290033803462"]
fetched_at: "2026-11-10T12:35:29Z"
---

# JevLight — SUMOで交通信号の意思決定モデルを比較する

## 出来ること

- SUMO内で交差点の次の信号フェーズを選ぶモデルを、交通シナリオと実験設定を指定して比較できる。

## 目的・背景

- LLMLight／CoLLMLightの観測・制御方式を踏襲する。交差点単体の情報を使う構成と、隣接交差点の情報を加える構成がある。
- 著者はSUMOのベンチマークを公開し、交通流とモードごとに3シードの平均と標本標準偏差を集計すると説明している。

## 依存関係

- Python 3.11以上、SUMO 1.20以上、TraCIとsumolib、環境管理にuvを使う。

## 実行条件

- 同梱のJinan設定で短い模擬実験を始められる。実モデルを使う場合は、選択した接続方式に応じてモデルサービスや認証情報が必要。

## 最短手順

- セットアップは `uv sync --locked --extra sumo`。
- AIエージェントのシェル実行ツールから `uv run python run_jevlight.py --config config/jev/jinan_smoke.json --print_config` を呼ぶと、SUMOの起動やAPI呼び出しをせずに設定を確認できる。
- 模擬実験は `uv run --extra sumo python run_jevlight.py --config config/jev/jinan_smoke.json`。

## 変更履歴

- 2026-11-11: 初回登録
