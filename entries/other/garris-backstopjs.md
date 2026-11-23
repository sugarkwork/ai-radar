---
name: "BackstopJS"
genre: "other"
url: "https://github.com/garris/BackstopJS"
repo: "garris/BackstopJS"
license: "MIT"
language: "JavaScript"
created: "2014-10-15"
updated: "2026-10-10"
forks: 617
open_issues: 577
commits_30d: 0
commit_cadence: "stale"
commits_90d: 1
size_kb: 62184
archived: false
flags: ["unverified"]
risk_notes: "READMEに新しいメンテナー／オーナーを募集する記載がある。"
stars: 7205
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/RealMarvelX/status/2119329098929426902"]
fetched_at: "2026-11-19T07:32:52.495006+00:00"
---

# BackstopJS

## 出来ること

- Webアプリのスクリーンショットを取得し、テスト画像と基準画像を比較して視覚的な差分をレポートする。READMEによると、レポートには基準・テスト・差分の確認機能があり、Chrome Headlessでの描画、PlaywrightまたはPuppeteerによる操作、JUnitレポート、CI連携にも対応する。

## 目的・背景

- CSS変更などによる画面表示の変化を繰り返し確認し、承認した画面を次回以降の比較基準にするためのビジュアルリグレッションテストツール。READMEは新しいメンテナー／オーナーを募集している。

## 依存関係

- READMEに記載された導入方法はnpmを使う。描画にはChrome Headlessを使用し、操作シナリオにはPlaywrightまたはPuppeteerを利用できる。Dockerによる描画方法も案内されている。

## 実行条件

- Node.js/npm環境でグローバルまたはローカルにインストールする。テスト対象のURL、少なくとも1つのviewport、各シナリオのlabelとurlを設定する。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- `npm install -g backstopjs`で導入し、対象プロジェクトで`backstop init`を実行して設定を作る。`backstop test`でテスト画像を生成・比較し、差分を確認してよければ`backstop approve`で基準画像を更新する。

## 変更履歴

- 2026-11-23: 初回登録
