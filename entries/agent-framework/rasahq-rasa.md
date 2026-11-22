---
name: "Rasa Open Source"
genre: "agent-framework"
url: "https://github.com/RasaHQ/rasa"
repo: "RasaHQ/rasa"
flags: ["unverified"]
risk_notes: "現在メンテナンスモード。READMEは後継としてHello RasaとCALMを案内している。"
stars: 21388
forks: 4906
open_issues: 161
size_kb: 1707110
language: "Python"
created: "2016-10-14"
updated: "2026-07-24"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119161717586366650"]
fetched_at: "2026-11-17T06:33:53.672949+00:00"
---

# Rasa Open Source

## 出来ること

- テキストおよび音声ベースの会話を自動化する文脈型アシスタントを構築できる。Facebook Messenger、Slack、Google Hangouts、Webex Teams、Microsoft Bot Framework、Rocket.Chat、Mattermost、Telegram、Twilio、および独自の会話チャネルに対応するとREADMEに記載されている。

## 目的・背景

- 複数のやり取りを含む文脈型会話を扱うためのオープンソース機械学習フレームワーク。READMEによると、Rasa Open Sourceは現在メンテナンスモードで、将来のエージェント開発先としてHello RasaとCALMが案内されている。

## 依存関係

- 開発時のパッケージングと依存関係管理にはPoetryを使用するとREADMEに記載されている。

## 実行条件

- 開発用インストール手順ではPoetryを導入し、ソースからmake installを実行する。READMEはmacOSでコンパイラ問題が起きた場合、インストール前にSYSTEM_VERSION_COMPAT=1を設定するよう案内している。

## 最短手順

- 開発環境では、公式Poetryガイドに従ってPoetryを導入し、リポジトリでmake installを実行する。READMEはテスト用依存関係の準備とテスト実行に、Ubuntu/Debianではmake prepare-tests-ubuntu、macOSではmake prepare-tests-macos、その後make testを案内している。

## 変更履歴

- 2026-11-22: 初回登録
