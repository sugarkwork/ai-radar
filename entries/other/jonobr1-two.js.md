---
name: "Two.js"
genre: "other"
url: "https://github.com/jonobr1/two.js"
repo: "jonobr1/two.js"
license: "MIT"
stars: 8726
language: "JavaScript"
created: "2012-09-05"
updated: "2026-11-13"
forks: 472
open_issues: 34
commits_30d: 22
commit_cadence: "daily"
commits_90d: 47
size_kb: 21722
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-15T03:18:16.822736+00:00"
---

# Two.js

## 出来ること

- ブラウザー向けの2D描画API。READMEによると、同じAPIからWebGL、Canvas 2D、SVGの各レンダラーで描画できます。図形やアニメーションを扱う例として、矩形を作成して更新イベントで回転させる手順が示されています。

## 目的・背景

- モダンブラウザー向けに、レンダラーに依存しない2D描画APIを提供します。READMEには2012年から運用されていると記載されています。

## 依存関係

- ブラウザー利用時の追加依存関係はREADMEに明記されていません。独自ビルドにはNode.jsとnpm installで導入する開発用ライブラリが必要です。ヘッドレス実行ではNode Canvasが必要で、Two.jsの依存関係には含まれないとREADMEに記載されています。

## 実行条件

- ブラウザーではビルド済みライブラリーをHTMLに読み込むか、npmで導入して使用します。ES6 importはREADMEによるとv0.7.5以降に対応しています。ヘッドレス環境ではNode Canvasを別途導入する必要があります。

## 最短手順

- README記載のnpm導入手順は `npm install --save two.js`。HTMLから使う場合は `two.min.js` を読み込み、`new Two({ fullscreen: true, autostart: true }).appendTo(document.body)` で初期化します。

## 変更履歴

- 2026-11-15: 初回登録
