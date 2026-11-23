---
name: "Katana"
genre: "other"
url: "https://github.com/projectdiscovery/katana"
repo: "projectdiscovery/katana"
license: "MIT"
stars: 17874
language: "Go"
created: "2021-01-02"
updated: "2026-11-18"
forks: 1237
open_issues: 26
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 3433
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:29:02.186293+00:00"
---

# Katana

## 出来ること

- Webサイトをクロールするツール。標準モードとヘッドレスモード、JavaScriptファイルの解析・クロール、自動フォーム入力、クロール範囲の制御に対応します。出力先は標準出力、ファイル、JSONを指定できます。Knowledge baseではページ種別やフォームを分類し、モデルを自動ダウンロードすると説明されています。

## 目的・背景

- 自動化パイプラインでの実行を想定した、高速で設定可能なWebクローラー・スパイダーとして紹介されています。

## 依存関係

- READMEはインストールにGo 1.26.10以上が必要としています。CGO_ENABLED=1を指定するインストール例も記載されています。ヘッドレスモードではChromeを利用でき、Docker例ではローカルのChromeを使う-system-chromeオプションが示されています。

## 実行条件

- Goでインストールする方法と、リリースページからコンパイル済みバイナリを取得する方法が案内されています。クロール対象URLは-uで指定します。ヘッドレスモードは-headlessで有効にできます。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Go 1.26.10以上の環境で `CGO_ENABLED=1 go install github.com/projectdiscovery/katana/cmd/katana@latest` を実行し、続けて `katana -u https://example.com` のように対象URLを指定します。オプション一覧は `katana -h` で確認できます。

## 変更履歴

- 2026-11-23: 初回登録
