---
name: "Instatic"
genre: "other"
url: "https://github.com/CoreBunch/Instatic"
repo: "CoreBunch/Instatic"
license: "MIT"
language: "TypeScript"
created: "2026-04-30"
updated: "2026-11-18"
open_issues: 217
commit_cadence: "daily"
size_kb: 197460
archived: false
flags: ["unverified"]
risk_notes: "機能・効果の説明はREADMEに記載された配布者の説明で、独立した動作確認はしていない。"
stars: 9140
forks: 873
commits_30d: 83
commits_90d: 100
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/bkdgiffug/status/2119299374672904224"]
fetched_at: "2026-11-18T21:09:42.605992+00:00"
---

# Instatic

## 出来ること

- READMEでは、ビジュアルキャンバスによるサイト編集、コンテンツ・メディア・フォームの管理、プラグイン、ページ公開を備えた自己ホスト型CMSと説明されています。ビジュアルコンポーネントやテンプレート、静的サイトのインポート、AIエージェントによる編集機能も紹介されています。これらは配布者の説明で、独立した動作確認はしていません。

## 目的・背景

- READMEは、CMS・フレームワーク・ホスティングなど複数サービスを組み合わせる構成に対し、編集、コンテンツ管理、メディア、認証、フォーム、公開を1つのBunサーバーにまとめる方針を示しています。

## 依存関係

- READMEではBunサーバーとして説明され、SQLiteまたはPostgresを利用すると記載されています。AIエージェント機能ではClaude、OpenAI、OpenRouter、ローカルOllamaのモデルを利用できると配布者が述べています。

## 実行条件

- READMEによると、セルフホスト運用にはBunサーバーとSQLiteまたはPostgresを使います。Railway、Render、Docker/VPSのデプロイ先が案内され、DockerではREADME記載のイメージとCompose設定を使う手順があります。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEは、Railwayのテンプレートを選んでデプロイする方法を最短手順として案内しています。Dockerを使う場合は `INSTATIC_IMAGE=ghcr.io/corebunch/instatic:latest docker compose -f compose.prod.yml -f compose.sqlite.yml up -d` を実行する例が記載されています。

## 変更履歴

- 2026-11-23: 初回登録
