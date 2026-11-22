---
name: "Agent HUD"
genre: "coding-agent"
url: "https://github.com/jazzenchen/agent-hud-open"
repo: "jazzenchen/agent-hud-open"
license: "Apache-2.0"
stars: 553
language: "Rust"
created: "2026-10-22"
updated: "2026-11-16"
forks: 81
open_issues: 21
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 21272
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/Ryrenz/status/2120095383393067096"]
fetched_at: "2026-11-16T21:44:57Z"
last_release: "v0.6.6"
last_release_at: "2026-11-16"
---

# Agent HUD

## 出来ること

- 画面上でエージェントの進捗、クォータ、残高、直近24時間のトークン使用状況、セッションを表示します。許可要求への応答や質問への回答、セッションへの復帰に対応します。組み込みMCPサーバーを使ったエージェント間メッセージ送信、セッション開始、HUD表示のカスタマイズもREADMEに記載されています。

## 目的・背景

- エージェントの作業状況をMac上やiPhone、Apple Watchから確認し、利用者の判断が必要なときに応答できるようにするHUDとして説明されています。

## 依存関係

- README記載のインストール方法の一つはNode.jsを使います。MacではHomebrewによるインストール方法も案内されています。ソースからのビルドに必要な依存関係は、提示されたREADME本文では確認できません。

## 実行条件

- READMEはmacOS 14以降を案内し、WindowsとLinuxはプレビューと記載しています。Homebrewの手順はMac向けです。Node.jsを使うインストール方法はMac、Windows、Linux向けとされています。iPhoneとApple Watch向けの機能も記載されています。

## 最短手順

- Node.jsがある環境では `npx @agenthud/install` を実行します。Macでは `brew install --cask jazzenchen/tap/agent-hud` でもインストールできます。READMEによると、どちらの方法もベータを含む最新リリースをインストールし、Macではアプリがその後自動更新します。

## 変更履歴

- 2026-11-11: 初回登録
