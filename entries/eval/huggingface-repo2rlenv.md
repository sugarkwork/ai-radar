---
name: "Repo2RLEnv"
genre: "eval"
url: "https://github.com/huggingface/Repo2RLEnv"
repo: "huggingface/Repo2RLEnv"
license: "Apache-2.0"
stars: 799
language: "Python"
created: "2026-05-05"
updated: "2026-11-16"
forks: 128
open_issues: 13
commits_30d: 58
commit_cadence: "daily"
commits_90d: 100
size_kb: 11687
archived: false
flags: ["unverified"]
risk_notes: "PR差分パイプラインの採点には判定モデルが必要で、利用できない場合は未採点になる。Dockerを使ったタスク実行にもDockerが必要。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ai_hakase_/status/2119400802389205299"]
fetched_at: "2026-11-20T04:14:54.865781+00:00"
---

# Repo2RLEnv

## 出来ること

- 既存リポジトリのマージ済みPR、コミット履歴、セキュリティ勧告、関数、端末記録などをもとに、コーディングエージェントの学習・評価向けタスク環境を生成する。READMEは24種類の生成器とHarbor形式への出力を説明している。

## 目的・背景

- READMEによると、強化学習用タスクを手作業で作る負担を減らし、実タスクに取り組んだ結果をプログラムで判定できる環境を作ることを目的としている。

## 依存関係

- READMEのQuickstartでは、最初のPR差分生成にPython 3.12以上とGitHub CLIを使用する。タスクの実行にはDockerが必要。PR差分の採点には判定モデルが必要で、例ではANTHROPIC_API_KEYを設定している。

## 実行条件

- READMEの例では、repo2rlenv[harbor]をインストールし、GitHub CLIで認証してから、repo2rlenv generateでタスクを生成し、repo2rlenv validateで検証する。生成例はpallets/clickの最近のマージ済みPRを3件対象にする。Dockerで実行する例も記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 1. `pip install 'repo2rlenv[harbor]'` でインストール。2. `gh auth login` でGitHub CLIを認証。3. `repo2rlenv generate --repo pallets/click --pipeline pr_diff --pipeline-opt limit=3 --out ./tasks` でタスクを生成。4. `repo2rlenv validate ./tasks --oracle` で構造とoracle資材を検証する。

## 変更履歴

- 2026-11-23: 初回登録
