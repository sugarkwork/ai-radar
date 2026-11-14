---
name: "Motrix"
genre: "other"
url: "https://github.com/agalwood/Motrix"
repo: "agalwood/Motrix"
license: "unknown"
stars: 58239
language: "TypeScript"
created: "2018-12-18"
updated: "2026-11-09"
forks: 5150
open_issues: 160
commits_30d: 95
commit_cadence: "daily"
commits_90d: 100
size_kb: 106671
archived: false
flags: ["unverified"]
risk_notes: "READMEには更新前に既存プロフィールとダウンロードのバックアップが必要と記載されています。v2エンジンはSQLiteをschema 6へ更新し、旧エンジンではschema 6を開けないため、ダウングレードの可能性がある場合は更新前バックアップを保持してください。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118761581547012468"]
fetched_at: "2026-11-14T03:10:58.387536+00:00"
---

# Motrix

## 出来ること

- HTTP・FTP・BitTorrent・magnetリンクなどのダウンロードを管理するデスクトップアプリです。READMEには、ファイル単位の選択、トラッカー管理、速度制限、再起動後のダウンロード復元、ブラウザー拡張からのダウンロード引き渡し、ヘッドレスサーバー、URL Resolverプラグインなどが記載されています。出典: https://github.com/agalwood/Motrix

## 目的・背景

- READMEは、シンプルな操作性を保つフル機能のダウンロードマネージャーと説明しています。デスクトップアプリとヘッドレスサーバーで共通のダウンロードコアを使い、MDXP（JSON-RPC 2.0ベース）を介して拡張機能やCLIが通信する構成です。出典: https://github.com/agalwood/Motrix

## 依存関係

- READMEに記載された構成要素は、デスクトップアプリのElectron・React・TypeScript、ヘッドレス実行用Node.jsまたはDocker、プラグイン実行用QuickJSサンドボックスです。CLIのクイックスタートにはNode.js 22以降が必要とあります。出典: https://github.com/agalwood/Motrix

## 実行条件

- デスクトップ版はmacOS、Windows、Linux向けです。ヘッドレスサーバーはデスクトップ環境なしでNode.jsまたはDocker上で実行できます。BitTorrentのWindows環境でのインプレース有効化には、対応するローカルNTFSボリュームと明示的な認可が必要とREADMEに記載されています。出典: https://github.com/agalwood/Motrix

## 最短手順

- デスクトップ版は公式サイトまたはGitHub ReleasesからOSに合うパッケージを選びます。CLIを使う場合はNode.js 22以降で `npm install -g @motrix/cli` を実行し、`motrix add https://example.com/file.iso --save-dir ~/Downloads` でダウンロードを追加できます。更新前にはプロフィールとダウンロードのバックアップが推奨されています。出典: https://github.com/agalwood/Motrix

## 変更履歴

- 2026-11-14: 初回登録
