---
name: "Paper"
genre: "other"
url: "https://github.com/PaperMC/Paper"
repo: "PaperMC/Paper"
license: "unknown"
stars: 12815
language: "Java"
created: "2016-01-22"
updated: "2026-11-15"
forks: 3564
open_issues: 663
commits_30d: 58
commit_cadence: "daily"
commits_90d: 100
size_kb: 136122
archived: false
flags: ["unverified"]
risk_notes: "ライセンスは取得済みデータでunknownです。READMEにはライセンスの記載がありません。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/dextune/status/2119006954420842718"]
fetched_at: "2026-11-16T00:34:44.953711+00:00"
---

# Paper

## 出来ること

- READMEはPaperを、Minecraftサーバーとして、ゲームプレイやメカニクスの不整合の修正を目指すプロジェクトと説明しています。Paperclip jarをサーバー上で実行する方法と、プラグイン開発向けAPIを案内しています。

## 目的・背景

- READMEの説明では、Paperはゲームプレイとメカニクスの不整合を修正することを目指しています。

## 依存関係

- ソースからビルドする場合、READMEはJDK 25とインターネット接続が必要としています。プラグイン開発向けAPIをGradleで使う場合は、PaperMCのMavenリポジトリと`io.papermc.paper:paper-api`を指定する例があります。

## 実行条件

- サーバー管理者向けには、ダウンロードしたPaperclip jarを通常のjarファイルと同様にサーバー上で実行する手順が記載されています。ソースからビルドする手順は、`./gradlew applyPatches`の後に`./gradlew createPaperclipJar`を実行し、生成物を`paper-server/build/libs`で確認するものです。

## 最短手順

- サーバーとして使う場合は、READMEが案内するダウンロードページからPaperを取得し、Paperclip jarをサーバー上で実行します。ソースからビルドする場合はJDK 25とインターネット接続を用意し、`./gradlew applyPatches`、続けて`./gradlew createPaperclipJar`を実行します。

## 変更履歴

- 2026-11-16: 初回登録
