---
repo: "QoderAI/better-harness"
name: "Better Harness"
genre: "coding-agent"
url: "https://github.com/QoderAI/better-harness"
flags: ["unverified"]
risk_notes: "公開文書で仕様を確認した。実行時の動作、ホスト間の互換性、導入前後の改善効果、最新リリースのタグと公開日は未確認。MITはリポジトリのライセンスで、ホストの利用条件・料金は未確認。"
stars: 2444
forks: 204
open_issues: 11
size_kb: 11392
language: "JavaScript"
created: "2026-07-21"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 12
commits_90d: 100
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/N01ennn/status/2117681136306393357"]
fetched_at: "2026-11-10T10:20:01Z"
---

# Better HarnessでAIコーディング工程を点検する

## 出来ること

- プロジェクトの設定や成果物と、対応ホストで取得できるセッションの証拠を整理し、優先度付きの指摘と検証方法をレポートにまとめる。

## 目的・背景

- コード差分に加えて、タスク理解、実行の制御、変更の検証、デリバリー、学びの蓄積を点検する。作業前の指示と作業後の検証結果を結び付け、改善前後の比較に使う基準を作る。

## 依存関係

- 対応するコーディングエージェントが必要。導入と出力はホストごとに異なり、Qoder Desktopには組み込まれている。

## 実行条件

- 分析対象のリポジトリをホストで開く。Claude Codeは既定でHTML、Markdown、JSONのレポートを出力し、ファイル出力を避ける場合はチャット内での出力を指定できる。セッション証拠の取得範囲はホストと利用可能な記録に依存する。

## 最短手順

- Qoder Desktopで対象リポジトリを開いて新規セッションを開始し、エージェントの入力欄で `/better-harness` を呼び出して、根拠付きの作業工程レポートを依頼する。レポートで指摘の根拠と検証方法を確認する。

## 変更履歴

- 2026-11-10: 初回登録
