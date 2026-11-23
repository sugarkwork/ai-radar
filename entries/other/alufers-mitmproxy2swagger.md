---
name: "mitmproxy2swagger"
genre: "other"
url: "https://github.com/alufers/mitmproxy2swagger"
repo: "alufers/mitmproxy2swagger"
license: "unknown"
stars: 9730
language: "HTML"
created: "2022-05-11"
updated: "2026-11-16"
forks: 386
open_issues: 20
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 8984
archived: false
flags: ["unverified"]
risk_notes: "READMEはMITライセンスと記載していますが、取得済みGitHub API情報ではライセンスがunknownです。ライセンスの状態は確認できていません。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:24:40.351485+00:00"
---

# mitmproxy2swagger

## 出来ること

- mitmproxyの通信記録またはブラウザーDevToolsからエクスポートしたHARを処理し、REST APIのOpenAPI 3.0仕様を生成します。初回処理後にパスの採否やパラメーターを編集し、同じスキーマファイルで再実行する手順がREADMEに記載されています。

## 目的・背景

- アプリの通信を記録してREST APIの仕様を作成する用途として紹介されています。READMEでは、アプリを動かして通信を捕捉することでAPIをリバースエンジニアリングできると説明しています。

## 依存関係

- インストール手順ではPython 3とpip 3を案内しています。Dockerイメージをビルドして実行する方法も記載されています。mitmproxy方式では別途mitmproxyを使って通信を捕捉します。

## 実行条件

- mitmproxy方式では通信をflowファイルに保存し、APIのベースURLを表すapi_prefixを指定します。HAR方式ではブラウザーDevToolsからHARをエクスポートします。--examplesや--headersを使うとトークン、パスワード、個人情報などの機微情報がスキーマに含まれる可能性があるため注意が必要です。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 1. mitmproxyで通信を捕捉してflowファイルに保存するか、DevToolsからHARをエクスポートします。2. mitmproxy2swaggerを入力ファイル、出力スキーマ、APIプレフィックスを指定して実行します。3. 生成されたスキーマのx-path-templatesを編集し、生成したいパスのignore:を外します。4. 同じスキーマファイルを指定してもう一度実行します。

## 変更履歴

- 2026-11-23: 初回登録
