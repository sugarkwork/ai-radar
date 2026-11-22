---
name: "MCode Stack"
genre: "coding-agent"
url: "https://github.com/MiniMax-AI/mcode-stack"
repo: "MiniMax-AI/mcode-stack"
license: "MIT"
language: "JavaScript"
archived: false
stars: 725
forks: 49
open_issues: 1
size_kb: 8645
created: "2026-10-28"
updated: "2026-11-11"
commits_30d: 16
commits_90d: 16
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/AIExplorerTim/status/2118910064606233060"]
fetched_at: "2026-11-16T21:46:05Z"
last_release: ""
last_release_at: ""
---

# MCode Stack

## 出来ること

- MiniMax Codeチームの開発ワークフローとスキルを提供する。内容には、作業のサブエージェント分割、コンテキストやツールの監査、長時間セッション・コマンドの管理、コードレビュー、評価実験、エージェントへの作業依頼とレビューなどがある。READMEでは、スキルは共通のSKILL.md形式で、対応する他のエージェントでも多くが動作すると説明している。

## 目的・背景

- チームが日常的に使う手順やスキルを公開し、インストールして利用できるようにする。READMEは、一般的なベストプラクティスの一覧やプロンプト集ではなく、チームで実際に使う内容だと説明している。

## 依存関係

- READMEに記載された導入方法では、Claude CodeまたはCodexのプラグイン機能を使う方法がある。リポジトリのscripts/install.shは、claudeまたはcodexがPATHにあれば利用し、どちらもなければスキルを~/.agents/skills/へコピーすると記載されている。個別スキルはSKILL.mdを含むフォルダーとして扱う。

## 実行条件

- Claude Codeではプラグインのインストールコマンドを、Codexではマーケットプレイス追加後にプラグイン追加コマンドを使う手順が記載されている。READMEには、MiniMax Codeの現行マーケットプレイス機能は段階的に提供中で、利用環境のバージョンによっては使えない場合があるとの記載もある。

## 最短手順

- Claude Codeのシェルで `claude plugin install ronny --marketplace MiniMax-AI/mcode-stack` を実行する。Codexでは `codex plugin marketplace add MiniMax-AI/mcode-stack` の後に `codex plugin add ronny@mcode-stack` を実行する。`ronny`は`jiachen`、`req-tpm`、`youfang`に置き換えて各スタックを選べる。

## 変更履歴

- 2026-11-15: 初回登録
