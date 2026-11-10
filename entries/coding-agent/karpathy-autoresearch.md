---
repo: "karpathy/autoresearch"
name: "autoresearch"
genre: "coding-agent"
url: "https://github.com/karpathy/autoresearch"
flags: ["unverified"]
risk_notes: "独立実行による改善幅、試行回数、H100以外での動作、GPU・エージェントの利用料金は未確認。READMEはMITと記載しているが、親のGitHub API測定値はunknown。学習データの利用条件は未確認。 GitHub APIでライセンスを確認できていません。"
last_release: ""
last_release_at: ""
stars: 99728
forks: 13741
open_issues: 196
size_kb: 530
language: "Python"
created: "2026-03-06"
updated: "2026-03-26"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/thegreatest_sv/status/2115051970251628961"]
fetched_at: "2026-11-10T11:53:15Z"
---

# autoresearch — コーディングエージェントで小規模LLMの学習実験を反復する

## 出来ること

- エージェントが train.py のモデル構成や学習設定を変更し、検証データの val_bpb（1バイトあたりのビット数）が下がった変更を残す。

## 目的・背景

- nanochat を単一GPU向けに簡略化し、prepare.py のデータ準備と評価を固定したまま学習コードの変更を比較する。人間は program.md に実験方針を書く。

## 依存関係

- READMEの要件は NVIDIA GPU 1基、Python 3.10以上、uv。学習には PyTorch を使用し、初回準備でデータを取得してBPEトークナイザーを学習する。

## 実行条件

- READMEで著者が動作確認したGPUはH100。1試行の学習予算は実時間5分で、起動とコンパイルは予算外。比較は同一計算環境で行う。改善幅と夜間の試行回数は独立測定していない。
- READMEはMITと記載。親のAPI測定値はunknownで、データの利用条件と実行費用は未確認。公開のReleasesページにはリリースの掲載がない。

## 最短手順

- リポジトリの作業ディレクトリで uv sync、uv run prepare.py、uv run train.py の順に実行し、変更前の val_bpb を記録する。
- 同じ作業ディレクトリを開いたコーディングエージェントに program.md を読ませ、train.py の変更と評価を依頼する。基準値と実験ログを比較する。

## 変更履歴

- 2026-11-10: 初回登録
