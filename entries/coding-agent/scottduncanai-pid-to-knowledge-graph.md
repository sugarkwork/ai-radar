---
name: "P&ID to Knowledge Graph"
genre: "coding-agent"
url: "https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph"
repo: "ScottDuncanAI/PID-to-Knowledge-Graph"
license: "MIT"
stars: 265
language: "Python"
created: "2026-11-08"
updated: "2026-11-08"
forks: 55
open_issues: 1
commits_30d: 3
commit_cadence: "monthly"
commits_90d: 3
size_kb: 393
archived: false
flags: ["unverified"]
risk_notes: "Python 3.13以降ではOCRによる照合と自動ページ方向調整が利用できない。抽出品質は図面の判読性に依存し、制御説明文や原因・結果分析にのみあるロジックは抽出対象外とREADMEに記載されている。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/GitTrend0x/status/2121566394286248121"]
fetched_at: "2026-11-14T15:09:20.986873+00:00"
---

# P&ID to Knowledge Graph

## 出来ること

- Claude Code向けスキル `pid-to-kg` は、PDF形式のP&IDおよびPFDを読み取り、プロセス知識グラフを作成する。READMEによれば、グラフには機器・配管の上流下流関係、計測器と計測対象・位置、センサーから制御機器・最終要素までの制御ループを含める。`summary.md`、`graph.json`、`graph.duckdb`を出力し、Neo4jやGraphMLにもエクスポートできると説明されている。出典: https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph

## 目的・背景

- 化学製造プロセスの図面を、LLMアプリケーションが質問に利用できるコンテキスト層の一部にすることを目的としている。各項目は元の図面シートを記録し、回答を図面まで追跡可能にする。これはREADMEに記載された用途説明であり、独立した性能評価ではない。出典: https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph

## 依存関係

- README記載の必要環境はClaude Code（デスクトップアプリまたは端末版）とPython 3.10以降。Python 3.12が推奨され、3.13以降ではスキルは動作するがOCR照合と自動ページ方向調整が利用できないと説明されている。初回実行時に必要なPythonパッケージをClaudeがインストールする。個別パッケージ名は添付READMEの確認範囲で特定できない。出典: https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph

## 実行条件

- デジタルPDFとスキャンPDFの両方を対象とする。図面の判読性が抽出品質に影響し、低解像度スキャンでは小さな文字が失われる可能性があるためフラグ付けされる。判読不能な項目は推測せず、その旨を記録するとREADMEに記載されている。大きな図面セットは処理に時間がかかる場合がある。出典: https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph

## 最短手順

- READMEの手順: GitHubページのCodeからDownload ZIPを選んで展開し、`skills/pid-to-kg`フォルダーを個人用Claudeスキルフォルダー（Windowsは`C:\Users\<ユーザー名>\.claude\skills\`、macOSは`/Users/<ユーザー名>/.claude/skills/`）へコピーする。P&ID PDFをプロジェクトフォルダーに置き、そのフォルダーをClaude Codeで開いて変換を依頼する。初回は依存Pythonパッケージのインストールが行われ、コマンド実行前に許可を求めるとREADMEに記載されている。出典: https://github.com/ScottDuncanAI/PID-to-Knowledge-Graph

## 変更履歴

- 2026-11-14: 初回登録
