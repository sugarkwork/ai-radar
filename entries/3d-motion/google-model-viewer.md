---
name: "Google model-viewer"
genre: "3d-motion"
url: "https://github.com/google/model-viewer"
repo: "google/model-viewer"
license: "Apache-2.0"
stars: 8351
language: "TypeScript"
created: "2018-10-18"
updated: "2026-11-18"
forks: 964
open_issues: 119
commits_30d: 11
commit_cadence: "weekly"
commits_90d: 19
size_kb: 4478236
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/0xCarrera/status/2123762450935771202"]
fetched_at: "2026-11-22T04:49:14.084776+00:00"
---

# Google model-viewer

## 出来ること

- `<model-viewer>` Webコンポーネントを中心に、関連するPostProcessingプラグイン、ドキュメントサイト、描画忠実度のテストツール、共有アセット、エディタを含むプロジェクト群。

## 目的・背景

- 3Dモデルをウェブ上で扱う`<model-viewer>`と関連プロジェクトを開発・提供するリポジトリ。

## 依存関係

- リポジトリ全体の開発にはGit、Node.js、npmが必要。セットアップ時は`npm install`または`npm ci`を実行する。

## 実行条件

- READMEはWindows 10/11でのセットアップにWSL2を推奨し、Node.js/npmはNVM経由での導入を案内している。テスト実行にはWSL上で`CHROME_BIN`の設定が必要。描画忠実度テストにはGUIサポートが必要と記載されている。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- 開発用にはリポジトリをcloneし、ディレクトリに移動して`npm install`を実行する。READMEでは履歴の大部分が約3GBの描画忠実度画像で占められるため、`--depth=1`を指定したclone例を掲載している。

## 変更履歴

- 2026-11-23: 初回登録
