---
repo: "OrchestratorInc/agent-orchestrator"
name: "Agent Orchestrator"
genre: "coding-agent"
url: "https://github.com/OrchestratorInc/agent-orchestrator"
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日時、クラウドと外部エージェントの料金は未確認。並列実行の性能、CIやレビュー指摘の差し戻し、モバイル通知と応答は公式文書の記載に基づき、実機では未検証。"
stars: 14373
forks: 1955
open_issues: 924
size_kb: 658927
language: "Go"
created: "2026-02-13"
updated: "2026-11-10"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/opensourcelab9/status/2117225240451535192"]
fetched_at: "2026-11-10T08:23:40+00:00"
---

# Agent Orchestratorで複数のコーディングエージェントとPRを管理する

## 出来ること

- プロジェクトのメインエージェントに依頼すると、作業を分割し、担当ワーカーを個別のブランチとGit worktreeで起動する。ボードはセッション、PR、CI、レビューの状態をもとに並べ替える。
- 公式READMEでは、CI失敗、レビュー指摘、マージ競合をブランチの担当ワーカーに戻せる。デスクトップとペアリングしたモバイルアプリでは、質問や承認依頼の通知を受けて応答できる。

## 目的・背景

- 複数のエージェントを並行稼働させる際に、作業ファイルの衝突を避け、各ブランチの進捗とPRの確認を一か所で追うためのツール。

## 依存関係

- リポジトリを扱うにはGit、GitHubのリポジトリやPRを操作するには認証済みのGitHub CLIが必要。Claude CodeやCodexなど外部エージェントを使う場合は、対応CLIを別途セットアップする。

## 実行条件

- 公式READMEにはmacOS、Windows、Linux向けのデスクトップ配布がある。デスクトップアプリがローカルのGoデーモンを起動する。Chatやレビューで使える機能はエージェントによって異なる。
- リポジトリはApache-2.0。クラウド実行は別サービスでアカウント条件があり、外部エージェントの利用条件は各提供元に従う。

## 最短手順

- 公式配布先からデスクトップ版を導入し、Add projectでローカルのGitリポジトリを選ぶ。Settings → HarnessでClaude CodeやCodexの準備状況を確認する。
- プロジェクトのメインエージェントに小さな実装を依頼し、ボードで担当セッションを確認する。CLIを導入済みの環境では、AIに `ao spawn --standalone --agent codex --name notes --prompt "Draft release notes"` を呼ばせると、リポジトリを必要としない作業を委任できる。スタンドアロンではPRを担当できない。

## 変更履歴

- 2026-11-10: 初回登録
