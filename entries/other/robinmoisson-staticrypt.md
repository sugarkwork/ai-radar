---
name: "StatiCrypt"
genre: "other"
url: "https://github.com/robinmoisson/staticrypt"
repo: "robinmoisson/staticrypt"
license: "MIT"
stars: 8074
language: "HTML"
created: "2017-04-29"
updated: "2026-07-06"
forks: 502
open_issues: 34
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 669
archived: false
flags: ["unverified"]
risk_notes: "README says shareable links contain the hashed password and can auto-decrypt the file. Treat such links as credentials."
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/awe0_io/status/2118741912610029739"]
fetched_at: "2026-11-14T00:19:06.688704+00:00"
---

# StatiCrypt

## 出来ること

- 静的HTMLファイルをパスワードで暗号化し、パスワード入力画面を持つ静的HTMLを生成します。READMEによると、生成物はブラウザー内のJavaScriptで復号され、バックエンドなしで静的ホスティングに配置できます。CLIは複数ファイルやディレクトリの処理、復号、テンプレートのカスタマイズにも対応すると記載されています。

## 目的・背景

- READMEは、公開される静的HTMLの内容をパスワード保護し、NetlifyやGitHub Pagesなどの静的ホスティングで配信する用途を説明しています。

## 依存関係

- CLIの導入方法としてnpm経由のインストールを記載しています。v3はWebCryptoを使用します。

## 実行条件

- READMEによると、v3のWebCryptoはHTTPSまたはlocalhostでのみ利用可能です。HTTPでの利用が必要な場合はv2を使うよう案内されています。

## 最短手順

- README記載の手順は、npmでstaticryptを導入し、`staticrypt test.html`を実行して入力を暗号化することです。パスワードはプロンプト入力、引数、または`STATICRYPT_PASSWORD`環境変数で指定できます。

## 変更履歴

- 2026-11-14: 初回登録
