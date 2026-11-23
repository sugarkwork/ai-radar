---
name: "Pinky"
genre: "agent-framework"
url: "https://github.com/DIYgod/pinky"
repo: "DIYgod/pinky"
stars: 2645
forks: 277
open_issues: 18
size_kb: 58247
language: "Go"
created: "2026-11-06"
updated: "2026-11-22"
archived: false
license: "Apache-2.0"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/Leviwoyun/status/2119412710240878949"]
fetched_at: "2026-11-22T04:31:56.048232+00:00"
---

# Pinky

## 出来ること

- MCP対応エージェントからiPhoneやAndroid端末を操作でき、画面を見ながら危険な操作を承認したり、操作を引き継いだりできる。Pinkyアプリ単独で、利用者が選んだAIモデルを使ってタスクを実行する機能もREADMEに記載されている。銀行・ウォレット・パスワード管理アプリは既定でエージェントから見えず、パスワードやワンタイムコード欄への入力もできない。

## 目的・背景

- AIエージェントによるスマートフォン操作を、利用者が監視・承認・中断できる形で行うためのアプリ。READMEではpre-alphaとされており、一部機能は利用者による試行待ちと説明されている。

## 依存関係

- エージェント連携にはMCPサーバーを利用できるエージェントが必要。Android端末はUSBケーブルが必要で、Windowsでは機種によってUSBドライバー、LinuxではUSBアクセス設定が必要な場合がある。Pinkyアプリ単独利用では利用者が選ぶAIモデルを使用する。

## 実行条件

- macOS 13以降（Apple siliconまたはIntel）、Windows 10/11 64-bit、またはx86-64のLinux（Ubuntu 20.04、Debian 11以降相当、glibc 2.29以降、GTK 3）が対象。Androidは10〜17、iPhone/iPadはiOS 17.4以降。iOS 17.4〜26でiPhone上のPinkyアプリを使う場合は、MacとXcodeを使った初回導入が必要とREADMEに記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- GitHubの最新リリースからOSに合った配布物を入手してインストールし、端末を接続してPinkyを起動する。Settings › Agentsから対応エージェントを接続し、エージェントに端末上の操作を依頼する。READMEにはHomebrew、Windowsのポータブル版、Debian/Ubuntu向けdebパッケージなどの導入方法も記載されている。

## 変更履歴

- 2026-11-23: 初回登録
