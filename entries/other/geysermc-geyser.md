---
name: "Geyser"
genre: "other"
url: "https://github.com/GeyserMC/Geyser"
repo: "GeyserMC/Geyser"
license: "MIT"
stars: 5973
language: "Java"
created: "2019-07-08"
updated: "2026-11-18"
forks: 963
open_issues: 345
commits_30d: 52
commit_cadence: "daily"
commits_90d: 100
size_kb: 40686
archived: false
flags: ["unverified"]
risk_notes: "READMEは、異なるゲーム間でネットワークパケットを変換する性質上、すべてが完全に動作するとは限らないと説明している。具体的な制限事項はREADMEからリンクされたCurrent Limitationsを参照。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119339139116216675"]
fetched_at: "2026-11-19T11:17:01.023577+00:00"
---

# Geyser

## 出来ること

- Minecraft: Bedrock EditionとMinecraft: Java Editionサーバーの間をプロキシとして中継し、Bedrock Editionの利用者がJava Editionサーバーに参加できるようにする。README記載の対応バージョンはBedrock 26.40〜26.65、Java 26.3。

## 目的・背景

- 異なるゲーム間のネットワークパケットを変換し、Bedrock EditionからJava Editionサーバーへできるだけシームレスに参加できるようにするプロジェクト。READMEは、完全な動作を保証するものではないと説明している。

## 依存関係

- READMEはAdventure Text Library、CloudburstMC Bedrock Protocol Library、GeyserMCのJava Protocol Library、TerminalConsoleAppender、slf4jを使用ライブラリとして挙げている。ソースからビルドする場合はサブモジュールの取得も必要。

## 実行条件

- READMEには対応ゲームバージョンとしてBedrock 26.40〜26.65、Java 26.3と記載。古いJavaバージョンはサポートバージョンガイドを参照するよう案内されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 利用環境に合わせたセットアップ手順はREADMEからリンクされた公式セットアップガイドを参照。ソースからビルドする場合はリポジトリをcloneし、ルートで `git submodule update --init --recursive` を実行してから `gradlew build` を実行し、`bootstrap/build` を確認する。

## 変更履歴

- 2026-11-23: 初回登録
