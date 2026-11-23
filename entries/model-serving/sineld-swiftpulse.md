---
name: "SwiftPulse"
genre: "model-serving"
url: "https://github.com/sineld/SwiftPulse"
repo: "sineld/SwiftPulse"
stars: 2
forks: 0
open_issues: 0
size_kb: 2487
language: "Swift"
created: "2026-11-07"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 4
commits_90d: 4
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/sineld/status/2119203224909500565"]
fetched_at: "2026-11-19T08:09:14.680649+00:00"
---

# SwiftPulse

## 出来ること

- サーバーのライブメトリクスをダッシュボードに表示し、SSHターミナル、SFTPファイルブラウザー、ポート転送、Dockerパネル、再利用可能なスニペットを提供する。AIエージェント向けMCPサーバーも含み、変更ごとに利用者の承認を求めるとREADMEに記載されている。

## 目的・背景

- SSH経由で複数のサーバーを管理するためのネイティブmacOSアプリ。メトリクスの収集ではサーバーに何もインストールせず、1回のポーリングを1つのSSHコマンドで行うとREADMEに記載されている。

## 依存関係

- SwiftUI、SwiftDataを使用し、SSHとSFTPにCitadel、ターミナルにSwiftTermを利用するとREADMEに記載されている。

## 実行条件

- macOS 15 Sequoia以降が必要。サーバー側にはSSHサーバーが必要で、ライブメトリクスの対象ホストはLinuxとmacOS。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README記載の手順: 最新リリースからSwiftPulseのDMGを取得し、開いてアプリケーションフォルダーへドラッグする。起動後、接続先のホスト、ポート、認証方法などを設定してサーバーへ接続する。READMEはアプリがDeveloper IDで署名されAppleに公証済みと述べている。

## 変更履歴

- 2026-11-23: 初回登録
