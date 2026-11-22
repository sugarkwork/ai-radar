---
name: "Inkstone"
genre: "other"
url: "https://github.com/shuaiplus/inkstone"
repo: "shuaiplus/inkstone"
stars: 1188
forks: 1095
open_issues: 36
size_kb: 784
language: "TypeScript"
created: "2026-07-30"
updated: "2026-10-07"
archived: false
license: "unknown"
commits_30d: 0
commits_90d: 39
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/awe0_io/status/2119116478322737573"]
fetched_at: "2026-11-17T00:13:30.162964+00:00"
---

# Inkstone

## 出来ること

- ブラウザー上でMarkdownノートを作成・整理・同期・バックアップする自己ホスト型アプリ。ライブプレビュー、全文検索と任意のセマンティック検索、双方向リンク、オフライン編集、複数端末同期、AIアクセス、公開共有、オフサイトバックアップなどを提供するとREADMEに記載されています。出典: https://github.com/shuaiplus/inkstone

## 目的・背景

- ノートをプレーンなMarkdownとして保ちながら、書く・整理する・同期する・バックアップするためのアプリです。デプロイ者がデータベース、添付ファイル、実行環境を管理します。出典: https://github.com/shuaiplus/inkstone

## 依存関係

- README記載の構成要素はCloudflare D1、添付ファイル用のCloudflare R2またはWorkers KV、OAuth用Workers KV、任意の埋め込み生成用Workers AI、ブラウザーIndexedDB、通知用SyncHub Durable Object、バックアップ資格情報の暗号化キー用CredentialVault Durable Objectです。オフサイトバックアップ先としてWebDAVまたはS3ストレージを利用できます。出典: https://github.com/shuaiplus/inkstone

## 実行条件

- Cloudflare Workers上で動作します。READMEのR2構成ではビルドに `npm run build`、デプロイに `npm run deploy` を指定します。KV構成ではデプロイコマンドを `npm run deploy:kv` に変更します。出典: https://github.com/shuaiplus/inkstone

## 最短手順

- README記載の手順: 1) GitHubアカウントにリポジトリをフォーク。2) Cloudflare Workers & PagesでGitHub連携し、フォークしたリポジトリを選択。3) R2構成ならビルドコマンド `npm run build` とデプロイコマンド `npm run deploy` を設定（KV構成なら `npm run deploy:kv`）。4) デプロイ後、生成されたWorkers URLを開く。出典: https://github.com/shuaiplus/inkstone

## 変更履歴

- 2026-11-22: 初回登録
