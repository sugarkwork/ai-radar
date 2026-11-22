---
name: "Claude Trading Skills"
genre: "finance-quant"
url: "https://github.com/tradermonty/claude-trading-skills"
repo: "tradermonty/claude-trading-skills"
license: "MIT"
stars: 6234
language: "Python"
created: "2025-10-19"
updated: "2026-11-16"
forks: 1324
open_issues: 51
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 73281
archived: false
flags: ["unverified"]
risk_notes: "利用料金やアカウント要件はREADME記載時点の案内で、変更される可能性がある。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/GitTrend0x/status/2121566394286248121"]
fetched_at: "2026-11-16T21:51:16Z"
last_release: ""
last_release_at: ""
---

# Claude Trading Skills

## 出来ること

- 市場状況の確認、ポートフォリオレビュー、スイング候補の探索、リスク管理、トレード記録と振り返りのワークフローを提供する。READMEでは、AIに売買判断を委ねるのではなく、判断プロセスを構造化するためのツールキットと説明している。

## 目的・背景

- 作者自身のトレードプロセス改善のために始めた個人プロジェクト。時間の限られた個人投資家向けに、長期投資・ETF・配当株を中心とし、条件が整った場合に規律あるスイングトレードを補助する設計。

## 依存関係

- Claude Skillsを利用する。ワークフローによってFMP、FINVIZ Elite、Alpacaなどの連携が必要な場合がある。READMEに記載の5スキルのスターター経路は、有料の市場データAPI契約を必要としないが、公開CSV、チャート画像、ローカルファイルなどの外部データは必要。

## 実行条件

- Claude Web Skillsの利用可能プランやClaude Codeのアカウント要件はREADME記載の案内を参照。ワークフローにより必要なデータ入力やAPI連携が異なる。投資判断、ポジションサイズ、法令・税務上の確認、ブローカー利用は利用者の責任。

## 最短手順

- READMEは、まず目的に合う運用ワークフローを選び、対応するworkflows/*.yaml manifestに記載されたスキル、判断ゲート、成果物の順で進めるよう案内している。APIキーがない場合のスターター経路は、market-breadth-analyzer、uptrend-analyzer、position-sizer、trader-memory-core、signal-postmortemの5スキルを手動で実行する。

## 変更履歴

- 2026-11-14: 初回登録
