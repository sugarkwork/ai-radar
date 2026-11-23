---
name: "FinRL-X"
genre: "finance-quant"
url: "https://github.com/AI4Finance-Foundation/FinRL-Trading"
repo: "AI4Finance-Foundation/FinRL-Trading"
license: "Apache-2.0"
stars: 3952
language: "Python"
created: "2020-07-26"
updated: "2026-09-18"
forks: 1138
open_issues: 53
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 4
size_kb: 218941
archived: false
flags: ["unverified"]
risk_notes: "The README reports historical backtest results for Jan 2018–Oct 2025 and Alpaca paper-trading results for Oct 2025–Mar 2026. These figures and performance claims have not been independently verified."
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/ruyi3699/status/2119255838049104106"]
fetched_at: "2026-11-18T05:14:23.912035+00:00"
---

# FinRL-X

## 出来ること

- READMEでは、株式選定、ポートフォリオ配分、タイミング調整、リスク制御を組み合わせ、目標ポートフォリオの重みを共通インターフェースとしてバックテストやブローカー実行につなぐ仕組みと説明されています。等ウェイト、平均分散、最小分散、PPO/SACによる配分、KAMAタイミングの例があります。また、NASDAQ-100銘柄の選定とDRL配分、複数資産のローテーション戦略も掲載されています。README掲載の成績はプロジェクト側の報告で、独立検証はしていません。

## 目的・背景

- READMEによると、FinRL-Xはデータ処理、戦略構成、バックテスト、ブローカー実行を、重み中心のインターフェースで統合する定量取引基盤です。元のFinRLに続く、LLMやエージェント型AI時代を想定した基盤として紹介されています。

## 依存関係

- READMEには、バックテストエンジンがbtを利用するとあります。データ取得元としてFMP、Yahoo Finance、WRDS、キャッシュ用ストレージとしてSQLiteが挙げられています。全依存パッケージの一覧や各機能の利用条件は、このREADME抜粋では確認できません。

## 実行条件

- READMEのバッジにはPython 3.11+と記載されています。Alpaca連携による実行例が掲載されていますが、必要なアカウント、認証情報、料金、完全な環境設定はこのREADME抜粋では確認できません。

## 最短手順

- README掲載の例では、リポジトリのルートで `./deploy.sh --strategy adaptive_rotation --mode backtest --start 2023-01-01 --end 2024-12-31` を実行してバックテストします。Alpacaのペーパートレード例は `./deploy.sh --strategy adaptive_rotation --mode paper --dry-run` です。実行は確認していません。

## 変更履歴

- 2026-11-23: 初回登録
