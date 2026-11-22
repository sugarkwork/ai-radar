---
name: "QM"
genre: "agent-framework"
url: "https://github.com/yc-software/qm"
repo: "yc-software/qm"
stars: 15714
forks: 1963
open_issues: 1066
size_kb: 166789
language: "TypeScript"
created: "2026-07-29"
updated: "2026-11-16"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/bkdgiffug/status/2119031107567878386"]
fetched_at: "2026-11-16T21:41:45Z"
last_release: "v0.1.18"
last_release_at: "2026-11-11"
---

# QM

## 出来ること

- SlackとWebで使えるチーム向けエージェント基盤。個人・共有スコープ、管理者設定、Webアプリ、共有スキル、バックグラウンド処理を備える。READMEでは、社内情報の検索、内部アプリの作成、リポジトリでの作業、プロジェクトの追跡などの用途を挙げている。出典: https://github.com/yc-software/qm

## 目的・背景

- 個人向けアシスタントをチームで使う際の複雑さに対応するため、チーム利用を前提に設計。各ユーザーと各ルームに、スコープされたメモリ、ファイル、権限、永続サンドボックスなどを持たせる。出典: https://github.com/yc-software/qm

## 依存関係

- コアの永続化にPostgresが必要で、DATABASE_URLを設定する。エージェントループはPiを使用する。出典: https://github.com/yc-software/qm

## 実行条件

- コアはNode上でTypeScriptを実行し、HTTPにFastifyを使用する。Slack連携は任意のインプロセスプラグイン。READMEはNode 24.15+を示している。各デプロイは運用者自身のクラウドアカウントで実行する。出典: https://github.com/yc-software/qm

## 最短手順

- README記載の手順は、コーディングエージェントに「Let's deploy https://github.com/yc-software/qm」と依頼してデプロイガイドに従う方法。CLIを使う場合は、組織所有のデプロイ用リポジトリで `npm exec --yes --package=@yc-software/qm@latest -- qm init . --org <slug> --target <fly-or-aws>` を実行し、続けて `npm install` を行う。出典: https://github.com/yc-software/qm

## 変更履歴

- 2026-11-16: 初回登録
