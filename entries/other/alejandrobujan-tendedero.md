---
name: "Tendedero"
genre: "other"
url: "https://github.com/alejandrobujan/tendedero"
repo: "alejandrobujan/tendedero"
license: "unknown"
stars: 3198
language: "Swift"
created: "2026-10-07"
updated: "2026-11-12"
forks: 290
open_issues: 32
commits_30d: 62
commit_cadence: "daily"
commits_90d: 100
size_kb: 117755
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/awe0_io/status/2118740875417371015"]
fetched_at: "2026-11-13T23:19:39.918997+00:00"
---

# Tendedero

## 出来ること

- macOSのメニューバー付近にラインを表示し、スクリーンショットやコピーしたテキスト・リンク・画像を一時保持する。項目のコピー、Markupでの編集、プレビュー、アプリやフォルダへのドラッグ、共有、ピン留め、検索に対応する。スクリーン録画の保持とトリミング、画像内テキストの検索もREADMEに記載されている。

## 目的・背景

- スクリーンショットをデスクトップに散らかさず、撮影した内容を画面上部のラインに保持する。READMEは、コピーした内容も同じ場所で扱い、必要なものだけをドラッグして保存できる設計を説明している。

## 依存関係

- Swift、AppKit、SwiftUIで構築。ソースからビルドする場合はSwift toolchainが必要で、Xcodeは任意。READMEにはmacOS 27のCommand Line Tools利用時にSDKのフォールバックがある旨も記載されている。

## 実行条件

- macOS 14 Sonoma以降、Apple siliconおよびIntelに対応。無料。コードはMITライセンスと記載されており、名称とアイコンはライセンス対象外。READMEによるとアプリはMac上で動作し、ネットワークアクセスはない。

## 最短手順

- README記載の導入方法は、最新リリースのディスクイメージを開いてTendederoをApplicationsへドラッグする方法、または `brew install tendedero`。ソースからビルドする場合は `git clone git@github.com:alejandrobujan/tendedero.git`、`cd tendedero`、`scripts/build-app.sh`、`open build/Tendedero.app` を実行する。

## 変更履歴

- 2026-11-14: 初回登録
