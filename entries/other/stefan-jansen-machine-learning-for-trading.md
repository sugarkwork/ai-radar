---
repo: "stefan-jansen/machine-learning-for-trading"
name: "machine-learning-for-trading"
genre: other
url: "https://github.com/stefan-jansen/machine-learning-for-trading"
license: "MIT"
stars: 21712
language: "Jupyter Notebook"
created: "2018-05-09"
updated: 2026-11-03
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 5758
open_issues: 0
commits_30d: 32
commit_cadence: daily
size_kb: 1294417
archived: false
commits_90d: 100
fetched_at: "2026-11-04T22:54:04Z"
last_release: v3.1.0-artifacts
last_release_at: 2026-09-20
---

# machine-learning-for-trading

## 出来ること

- 書籍『Machine Learning for Trading, 3rd Edition』（Stefan Jansen）の全コード。27章＋9つのケーススタディを、データ取得から執行・運用までの1本のワークフローとして通す。
- v3.1.0 のタグで、9つのケーススタディの予測・学習済みモデル・バックテスト・指標レジストリを事前計算済みアーティファクトとして配布している（合計約6.8GB）。`scripts/download_artifacts.py` で取得でき、再学習せずに結果を確認できる。
- モデル範囲が広い: 勾配ブースティング（XGBoost / LightGBM / CatBoost）、時系列深層モデル（PatchTST、iTransformer、TSMixer、TCN、Mamba）、表形式モデル（TabPFN、TabM）、自己符号化器。
- 戦略設計の章が独立して用意され、取引コストとリスク管理を経て「シグナル→サイズ決め→コスト・リスク考慮済みポートフォリオ」まで通す。
- 本番トラック: ライブ執行（Interactive Brokers / Alpaca / QuantConnect）、MLOps とガバナンス（ドリフト検出、安全なロールアウト、サーキットブレーカー、特徴量ストア、実験管理）。
- 生成 AI の章: SEC 提出書類を根拠にした RAG、ナレッジグラフ／Graph RAG、マルチエージェントのリサーチ系。
- 因果 ML（Double ML、ベイズ構造時系列）、強化学習（最適執行、在庫付きマーケットメイク、ディープヘッジ）、合成金融データ（TimeGAN、Tail-GAN、拡散モデル系）。

## 目的・背景

「研究アイデアが、運用できて維持できる戦略になるまで」を1本の道筋として扱う教科書のコード。チューニングと評価を分ける「証拠の境界（evidence boundary）」を明示し、エッジが減衰したら再学習・停止・引退させるフィードバックループまで含める。

## 依存関係

- Docker（依存を全部含む `ml4t` イメージ）か、`uv` によるローカル環境（macOS / Linux / WSL2）。README は `pip` ではなく `uv` の利用を推奨している。
- `uv` 経路は C/C++ コンパイラと Python ヘッダが必要（Ubuntu / WSL2 は `build-essential` と `python3-dev`、macOS は Xcode コマンドラインツール）。macOS は LightGBM 用に OpenMP ランタイム（`libomp`）も別途要る。
- データは別途ダウンロード（`data/download_all.py --free-only` で無料分 約4GB）。`.env.example` をコピーして使う。
- ノートブックは Jupytext 形式（`.py` と生成された `.ipynb` のペア）。

## 実行条件

- 一部の章は実 compute やライセンスが必要なデータを前提とする。何が1コマンドで再現でき、何ができないかは `docs/what-this-is.md` に明記されている（導入前に読む前提）。
- ディスク: Docker 経路はイメージ約13GB＋データ約4GB、`uv` 経路は約16GB（環境11GB＋データ4GB＋git履歴0.9GB）。リポジトリ自体は約1.26GB。
- インストール確認用に `scripts/verify_installation.py` があり、PASS/FAIL を項目別に出す。

## 最短手順

```bash
git clone https://github.com/stefan-jansen/machine-learning-for-trading.git
cd machine-learning-for-trading
cp .env.example .env
docker compose pull ml4t                 # Option A: Docker
# もしくは Option B: ローカル環境（要コンパイラ）
uv sync
uv run python data/download_all.py --free-only
uv run python scripts/verify_installation.py
uv run python scripts/download_artifacts.py   # 任意: 事前計算済みアーティファクト
docker compose up ml4t                   # http://localhost:8888
```

Docker 経路ではホストに Python が無いため、`uv run` を付けずに Jupyter のターミナルで同じコマンドを実行する。

## 変更履歴

- 2026-11-03: 初回登録（★21,700 / pushed 2026-11-03 / MIT / 第3版 v3.1.0-artifacts）
- 2026-11-04: 事前計算済みアーティファクトの配布と、コンパイラ・ディスク要件を追記（v3.1.0-artifacts）
