---
repo: "TauricResearch/TradingAgents"
name: "TradingAgents"
genre: "finance-quant"
url: "https://github.com/TauricResearch/TradingAgents"
stars: 121734
forks: 23299
open_issues: 133
size_kb: 6566
language: "Python"
created: "2024-12-28"
updated: "2026-11-04"
archived: false
license: "Apache-2.0"
commits_30d: 34
commits_90d: 100
commit_cadence: "daily"
last_release: "v0.7.1"
last_release_at: "2026-10-27"
flags: ["unverified"]
risk_notes: "現行版のCLI実行、データ取得の安定性、論文結果の独立再現、実取引での成績は未確認。LLMや外部データの料金・利用条件は提供元と設定に依存し、個別条件は未確認。90日コミット数は計測上限のため100件以上を表す。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/PayneL_AI/status/2117231964495221130"]
fetched_at: "2026-11-10T08:27:27+00:00"
---

# TradingAgents — 複数のLLMエージェントによる銘柄調査

## 出来ること

- 銘柄と分析日を指定すると、選択したアナリストが財務、相場、ニュース、ソーシャル投稿などを調査する。強気・弱気のリサーチャーが報告を討論し、トレーダーとリスク管理チームが判断をまとめる。CLIからHTMLレポートを保存できる。

## 目的・背景

- 取引会社の役割分担をLLMで模した研究用フレームワーク。著者の論文は比較実験で累積リターン、シャープレシオ、最大ドローダウンの改善を報告している。今回の確認は公開資料の閲覧に限り、現行版での再現性や実取引での成績は未検証。

## 依存関係

- Python 3.11以上。主要依存にLangGraph、LangChain系パッケージ、pandas、yfinanceがある。財務諸表の既定の取得順はSEC EDGAR、Yahoo Finance。リポジトリはApache-2.0で、モデルと外部データには各提供元の利用条件が適用される。

## 実行条件

- 利用するLLMプロバイダーとモデルを設定し、必要な認証を用意する。外部プロバイダーやデータソースを利用する構成ではネットワーク接続が必要で、選択によって費用が発生し得る。

## 最短手順

- 公式リリースのwheelをpipで導入し、利用するLLMの認証とモデル設定を済ませて、`tradingagents` を起動する。対話画面で銘柄と分析日を指定する。
- シェル実行機能を持つAIエージェントからは、プロバイダー、モデル、出力言語、討論ラウンド数などを `TRADINGAGENTS_*` 環境変数で設定した環境で、`tradingagents --ticker NVDA --date 2026-09-23 --analysts market,news,fundamentals --save --no-show` を呼び出し、保存されたレポートを読む。

## 変更履歴

- 2026-11-10: 初回登録
