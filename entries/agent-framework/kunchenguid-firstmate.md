---
name: "firstmate"
genre: "agent-framework"
url: "https://github.com/kunchenguid/firstmate"
repo: "kunchenguid/firstmate"
license: "MIT"
stars: 8753
language: "Shell"
created: "2026-06-12"
updated: "2026-11-10"
forks: 2734
open_issues: 2663
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 57032
archived: false
flags: ["unverified"]
risk_notes: "実際の効果や、記載された要件以外の依存関係・実行条件は未検証。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/opensourcelab9/status/2116862853928095838"]
fetched_at: "2026-11-10T14:03:09.098793+00:00"
---

# firstmate

## 出来ること

- 単一のエージェントとの対話を窓口に、タスクごとにエージェントを起動し、各自のgit worktreeで並行作業させて完了まで監督する。成果物としてPR、承認済みのローカルマージ、または調査レポートを扱う。

## 目的・背景

- 複数タスクを並行して進める際に、複数セッションの管理やコンテキストの受け渡しが必要になる問題に対し、firstmateがエージェント群を運用する構成を提供する。READMEではモデル、ハーネス、スキル、MCPサーバー、CLIではなく、エージェント用の指示・スキル・ツール・ポリシー・状態規約をまとめたディストリビューションと説明している。

## 依存関係

- README記載の要件は、対応するエージェントハーネス（Claude Code、Grok、Pi、pi-signed、Oh My Pi、Codex、OpenCode、Cursor Agent CLI、Antigravity CLIのいずれか）、Git、認証済みGitHub CLI、および選択するランタイムバックエンドのCLIと依存ツール。tmuxが標準バックエンドとして記載されている。

## 実行条件

- README記載の対応プラットフォームはmacOSとLinux。リポジトリをクローンし、そのディレクトリを作業場所として対応ハーネスを起動する。Grokではクローンごとのtrust設定、Piでは初回のプロジェクトtrust承認、Cursor Agent CLIでは--trust付きの起動がフック読み込み条件として記載されている。

## 最短手順

- READMEのQuick Startに従い、`gh auth login`、`git clone https://github.com/kunchenguid/firstmate`、`cd firstmate`を実行し、対応ハーネス（例：`claude`、`grok --trust`、`pi`）を起動する。

## 変更履歴

- 2026-11-11: 初回登録
