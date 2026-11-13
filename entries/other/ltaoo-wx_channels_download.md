---
name: "微信视频号下载器"
genre: "other"
url: "https://github.com/ltaoo/wx_channels_download"
repo: "ltaoo/wx_channels_download"
license: "unknown"
stars: 10534
language: "Go"
created: "2024-09-30"
updated: "2026-11-12"
forks: 1748
open_issues: 12
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 30
size_kb: 28748
archived: false
flags: ["unverified"]
risk_notes: "README記載の利用には管理者権限での実行と証明書のインストールが必要です。ライセンスはAPIでunknownと確認されています。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/bkdgiffug/status/2118637513862783231"]
fetched_at: "2026-11-13T06:23:43.862958+00:00"
---

# 微信视频号下载器

## 出来ること

- READMEによると、微信PC版で再生中の视频号動画をダウンロードできます。通常のダウンロードボタンは現在再生中の品質を選び、ドロップダウンから別の品質も選べます。

## 目的・背景

- READMEでは、本プロジェクトを技術交流・学習・研究目的のオープンソースプロジェクトと説明し、利用者に法令遵守を求めています。

## 依存関係

- READMEには依存関係の一覧はありません。前端の復号処理はWechatVideoSniffer2.0、後端の復号コードはWechatSphDecryptを参考・利用したと記載されています。

## 実行条件

- README記載ではmacOSとWindowsに対応し、ビルド済みパッケージを管理者権限で実行します。初回起動時に証明書をインストールしてサービスを開始します。開発時は管理者権限のターミナルから `go run main.go` を実行します。

## 最短手順

- READMEの手順：ビルド済みパッケージを管理者として起動し、端末に「代理服务启动成功」と表示されるまで待ちます。微信PC版で対象動画を開いて再生し、一時停止してダウンロードボタンを押します。ボタンが表示されない場合はページ側面または下部のフローティングボタンを使います。

## 変更履歴

- 2026-11-13: 初回登録
