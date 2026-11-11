---
name: "OpenHands Agent Canvas"
genre: "agent-framework"
url: "https://github.com/OpenHands/OpenHands"
repo: "OpenHands/OpenHands"
license: "MIT"
stars: 93244
language: "TypeScript"
created: "2024-03-13"
updated: "2026-11-11"
forks: 12457
open_issues: 1168
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 659682
archived: false
flags: ["unverified"]
risk_notes: "Direct installation runs the agent server on the host with full filesystem access. The README recommends a Docker sandbox; its example mounts the selected projects directory and stores settings, secrets, and conversations in a named volume. Self-hosting security hardening is linked in the README."
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118325722850697573"]
fetched_at: "2026-11-11T19:06:00.619117+00:00"
---

# OpenHands Agent Canvas

## 出来ること

- OpenHands Agent Canvas は、OpenHands、Claude Code、Codex、Gemini CLI、Pi、OpenCode、および ACP 対応エージェントを利用するセルフホスト型の開発者向けコントロールセンターです。ローカル、Docker、VM、企業内環境などのバックエンドを切り替えられます。Slack へのレポート公開や GitHub issue のタスク分解などの自動化を作成し、スケジュールまたは webhook イベントで実行できます。これらは README に記載された機能で、独立した効果測定ではありません。

## 目的・背景

- コーディングエージェントとの会話や日常的な開発作業の自動化を、一つのセルフホスト型の開発者向け画面から扱うことを目的としています。ローカルマシンのほか、常時稼働するサーバーや複数のエージェントバックエンドで運用する構成が説明されています。

## 依存関係

- サンドボックスなしのローカル実行には Node.js 24 以降と uv が必要です。Docker サンドボックス構成には macOS/Windows の Docker Desktop、または Linux の Docker Engine/Docker Desktop が必要です。

## 実行条件

- README はローカル、Docker、VM、クラウドなどのバックエンド構成を案内しています。サンドボックスなしではエージェントサーバーがホスト上で動作し、ファイルシステム全体にアクセスできます。Docker 例では設定・秘密情報・会話を名前付きボリュームに保存し、プロジェクトを /projects にマウントします。Linux Docker Engine では uid 10001 がワークスペースを読み書きできる必要があります。

## 最短手順

- サンドボックスなしの場合、Node.js 24 以降と uv を用意し、README の手順に従って `npm install -g @openhands/agent-canvas` の後に `agent-canvas` を実行します。Docker を使う場合は、README の Docker サンドボックス手順に従い、ワークスペースを準備して Agent Canvas コンテナを起動します。起動コマンドの実行はここでは行っていません。

## 変更履歴

- 2026-11-11: 初回登録
