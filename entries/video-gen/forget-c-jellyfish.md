---
name: "Jellyfish"
genre: "video-gen"
url: "https://github.com/Forget-C/Jellyfish"
repo: "Forget-C/Jellyfish"
stars: 7185
forks: 1237
open_issues: 9
size_kb: 8929
language: "Python"
created: "2026-03-06"
updated: "2026-07-30"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118877847150616881"]
fetched_at: "2026-11-14T18:08:32.659611+00:00"
---

# Jellyfish

## 出来ること

- 脚本をショットに分割し、登場人物・シーン・小道具・衣装・台詞の抽出や整合性確認を行う。ショットの準備、共有アセットの管理と再利用、画像・動画生成タスクの実行、結果の管理、タスク状況の追跡を行う制作ワークスペース。

## 目的・背景

- READMEでは、脚本から絵コンテ準備、アセットの一貫性管理、生成実行、タスク追跡までを一つの制作フローで扱うことを目的としている。

## 依存関係

- README記載の構成要素は、フロントエンドがReactとVite、バックエンドがFastAPI。Docker Compose構成にはMySQL、Redis、RustFSが含まれる。生成機能を利用するためのモデルやプロバイダーの条件はREADMEからは特定できない。

## 実行条件

- READMEにはDocker Composeによる起動方法と、バックエンド・フロントエンドを個別に起動するローカル開発手順がある。環境変数ファイルの用意、バックエンドはuvによる依存関係同期、フロントエンドはpnpmによる依存関係インストールが記載されている。

## 最短手順

- Docker Composeの場合、README記載の手順は、deploy/compose/.env.exampleを.envへコピーし、deploy/compose/docker-compose.ymlを指定してdocker compose up --buildを実行すること。生成サービスの利用条件はREADMEからは特定できない。

## 変更履歴

- 2026-11-14: 初回登録
