---
repo: "karpathy/nanoGPT"
name: "nanoGPT"
genre: "other"
url: "https://github.com/karpathy/nanoGPT"
stars: 64598
forks: 11112
open_issues: 355
size_kb: 981
language: "Python"
created: "2022-12-28"
updated: "2025-11-12"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "最新リリース、現行の依存パッケージとの互換性、学習時間と検証損失の再現性は未確認。学習結果はREADMEの著者報告。MITはリポジトリのライセンスで、外部データや事前学習済み重みの利用条件は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:51:55+00:00"
---

# nanoGPTで小型GPTの学習から生成までをたどる

## 出来ること

- 文字単位の小型GPTをゼロから学習し、保存したチェックポイントからテキストを生成できる。既存のGPT-2チェックポイントを使った微調整の例もある。

## 目的・背景

- minGPTを書き直したPython実装。学習ループはtrain.py、GPTのモデル定義はmodel.pyにあり、設定を変えながら学習処理を追える。著者は2025年11月のREADME追記で非推奨と明記した。
- Shakespeareの文字単位モデルでは、著者がA100 1基で約3分、最良の検証損失1.4697と報告している。この値は同READMEの設定で得られた著者報告で、独立再現は未確認。

## 依存関係

- READMEの導入例はPyTorch、NumPy、transformers、datasets、tiktoken、wandb、tqdmを挙げる。transformersはGPT-2チェックポイントの読み込み、datasetsはOpenWebTextの取得と前処理に使い、wandbによるログ記録は任意。

## 実行条件

- 小規模なShakespeare例にはGPU向け設定と、モデルを縮小してコンパイルを無効化するCPU向け設定がある。GPT-2 124MをOpenWebTextで学習する別例では、READMEはA100 40GBを8基搭載したノードで約4日と報告している。
- リポジトリはMITライセンス。ローカルまたはクラウドでの計算資源は利用者が用意する。

## 最短手順

- リポジトリのルートで `pip install torch numpy transformers datasets tiktoken wandb tqdm` を実行し、`python data/shakespeare_char/prepare.py` で学習用と検証用のデータを準備する。
- GPU環境で `python train.py config/train_shakespeare_char.py` を実行する。CPU環境ではREADMEのCPU向け縮小設定を使う。
- `python sample.py --out_dir=out-shakespeare-char` で生成する。CPUでは `--device=cpu` を加える。シェル実行機能を持つAIエージェントからも、依存関係を導入済みの環境でリポジトリのルートを作業ディレクトリに指定して同じCLIを呼び出せる。

## 変更履歴

- 2026-11-10: 初回登録
