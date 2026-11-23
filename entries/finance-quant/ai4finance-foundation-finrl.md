---
name: "FinRL"
genre: "finance-quant"
url: "https://github.com/AI4Finance-Foundation/FinRL"
repo: "AI4Finance-Foundation/FinRL"
license: "MIT"
stars: 17123
language: "Jupyter Notebook"
created: "2020-07-26"
updated: "2026-11-03"
forks: 3658
open_issues: 329
commits_30d: 7
commit_cadence: "weekly"
commits_90d: 37
size_kb: 84571
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ruyi3699/status/2119255838049104106"]
fetched_at: "2026-11-18T05:13:47.840391+00:00"
---

# FinRL

## 出来ること

- READMEでは、金融市場環境、DRLエージェント、金融アプリケーションの3層で構成される、教育・実験・研究プロトタイピング向けの金融強化学習フレームワークと説明されています。チュートリアルには、株価データの前処理、A2C・DDPG・PPO・TD3・SACの学習、MVOおよびDJIAとのバックテスト手順があります。説明されている機能はREADME記載の範囲です。

## 目的・背景

- READMEによると、このリポジトリはFinRLの従来型ワークフローを教育、実験、研究プロトタイピング向けに維持しています。READMEは本リポジトリを本番向けの次世代構成とは区別し、新規の本番志向の利用者にはFinRL-Tradingを案内しています。

## 依存関係

- チュートリアルはリポジトリをクローンし、仮想環境で `pip install -e .` を実行する手順を示しています。学習手順ではStable Baselines 3を使用すると記載されています。README抜粋から、その他の依存関係の全容は確認できません。

## 実行条件

- READMEのチュートリアルは `python3 -m venv venv` で仮想環境を作成し、環境を有効化してからインストールする手順です。実機での動作確認は行っていません。

## 最短手順

- README記載の手順は、リポジトリをクローンして `cd FinRL`、仮想環境を作成・有効化し、`pip install -e .` を実行する流れです。その後、READMEにあるデータ前処理、学習、バックテストの各スクリプトを順に実行します。

## 変更履歴

- 2026-11-23: 初回登録
