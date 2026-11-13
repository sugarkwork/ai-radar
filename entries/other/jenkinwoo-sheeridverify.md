---
name: "sheeridVerify"
genre: "other"
url: "https://github.com/JenkinWoo/sheeridVerify"
flags: ["unverified"]
risk_notes: "実際のプラットフォームで使うには必要な許可が必要。README は SheerID や学校との公式な関係・承認を否定し、検証成功も保証していない。"
repo: "JenkinWoo/sheeridVerify"
stars: 2515
forks: 1310
open_issues: 0
size_kb: 408
language: "JavaScript"
created: "2026-11-06"
updated: "2026-11-06"
archived: false
license: "ISC"
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/mingzi206/status/2118686234587607352"]
fetched_at: "2026-11-13T16:15:34.105623+00:00"
---

# sheeridVerify

## 出来ること

- ローカル Web 作業台でタスクを作成・キューイング・停止・再開・削除できる。Node.js の fetch による状態照会と、必要に応じたブラウザフォーム操作または原本資料のアップロードを行う。資料を生成・変更せず、インタラクティブな本人確認はユーザーが行う。出典: https://github.com/JenkinWoo/sheeridVerify

## 目的・背景

- README は教学・学術研究・許可を得たフローのテストを用途として掲げる。実プラットフォームの利用には許可と適用される規則・規約の遵守が必要で、身元や在籍情報・資料の偽造、他人の情報の使用、資格審査の回避を禁じている。出典: https://github.com/JenkinWoo/sheeridVerify

## 依存関係

- Node.js >= 22.15 と npm が必要。セットアップ手順では npm ci と npm run browser:install を実行する。出典: https://github.com/JenkinWoo/sheeridVerify

## 実行条件

- 設定ファイル config/sheerid.local.json に許可された国・学校・メールドメイン・資料ソースを設定して実行する。Web/API モードと CLI で設定方法が異なる。Linux で画面付きブラウザを使う場合は利用可能なデスクトップ環境が必要。出典: https://github.com/JenkinWoo/sheeridVerify

## 最短手順

- README の手順は、リポジトリを取得し、プロジェクトルートで npm ci と npm run browser:install を実行、config/sheerid.example.json を config/sheerid.local.json にコピーして必要な設定を行い、npm run web を起動する流れ。出典: https://github.com/JenkinWoo/sheeridVerify

## 変更履歴

- 2026-11-13: 初回登録
