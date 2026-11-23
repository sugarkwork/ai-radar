---
name: "Obsidian Dataview"
genre: "other"
url: "https://github.com/blacksmithgu/obsidian-dataview"
repo: "blacksmithgu/obsidian-dataview"
stars: 9446
forks: 582
open_issues: 672
size_kb: 3583
language: "TypeScript"
created: "2021-01-13"
updated: "2025-11-17"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/rosemoni18/status/2119211334797840872"]
fetched_at: "2026-11-20T03:09:07.342058+00:00"
---

# Obsidian Dataview

## 出来ること

- MarkdownのfrontmatterとDataview形式のインラインフィールドからデータを取り出し、Dataview Query Language（DQL）、インライン式、DataviewJS、インラインJS式で検索できます。READMEには、フォルダやタグによる絞り込み、評価順の表、未完了タスク一覧、JavaScript APIを使ったグループ化の例があります。

## 目的・背景

- Obsidian Vaultをデータベースのように扱い、Markdownページの情報をクエリできるようにするものです。

## 依存関係

- 利用時の依存関係はREADMEから確認できません。READMEに記載された開発・ビルド手順ではNode.js、npm、rollupを使います。

## 実行条件

- Obsidian Vault内での利用を想定しています。通常のDataviewクエリはサンドボックス化される一方、DataviewJSおよびインラインJSは他のObsidianプラグインと同じ権限で動作し、ファイルの作成・変更・削除やネットワーク通信を行う可能性があるとREADMEに記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Markdownページにfrontmatterまたは`Key:: Value`形式のインラインフィールドを記録し、ページに`dataview`クエリブロックを追加します。例：```dataview\ntable time-played, length, rating\nfrom "games"\nsort rating desc\n```

## 変更履歴

- 2026-11-23: 初回登録
