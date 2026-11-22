---
name: "Copilot for Obsidian"
genre: "coding-agent"
url: "https://github.com/logancyang/obsidian-copilot"
repo: "logancyang/obsidian-copilot"
license: "AGPL-3.0"
stars: 8005
language: "TypeScript"
created: "2023-03-31"
updated: "2026-11-16"
forks: 775
open_issues: 168
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 184616
archived: false
flags: ["unverified"]
risk_notes: "利用可能なモデルやサービス上限は変わるため、現在のプランや利用条件はREADME記載の料金ページまたはアプリ内表示で確認が必要。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/stewy0x/status/2121929768996110590"]
fetched_at: "2026-11-16T21:45:32Z"
last_release: "4.0.20"
last_release_at: "2026-11-13"
---

# Copilot for Obsidian

## 出来ること

- READMEによると、Copilot V4はOpenCode、Claude Code、CodexをObsidianに接続し、ノートの調査、執筆、ナレッジ作業に使えるエージェント機能を提供する。エージェントはノートを参照し、ツールを使い、Obsidianファイルを作成できる。Quick Chat、Quick Ask、Projects、共有Skills、Commandsにも対応する。

## 目的・背景

- ObsidianのVault内で、調査・執筆・知識作業のためのエージェントやチャット機能を利用するプラグイン。

## 依存関係

- エージェント機能はOpenCode、Claude Code、またはCodexのいずれかを接続して使う。モデルはCopilotホスト、利用者自身のプロバイダーキー、またはローカルモデルを選べる。Claude CodeとCodexはそれぞれのCLIログインを使う。

## 実行条件

- Agentはローカルプロセスを使うためデスクトップ機能。Quick Chat、カスタムCommands、Quick Askはモバイルでも利用できる。利用するモデルやサービスによって、プロンプトと含めたコンテキストの処理先が異なる。

## 最短手順

- READMEの手順: 1. Obsidian Community PluginsからCopilotをインストール。2. Settings → Copilot → Basic → Agentsを開く。3. OpenCodeをダウンロードするか、Claude CodeをAuto-detectで接続するか、Codex用アダプターをインストールする。4. Agentリボンアイコンを選ぶか、Open Copilot Agent Chat windowを実行する。

## 変更履歴

- 2026-11-15: 初回登録
