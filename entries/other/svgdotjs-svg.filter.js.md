---
name: "svg.filter.js"
genre: "other"
url: "https://github.com/svgdotjs/svg.filter.js"
repo: "svgdotjs/svg.filter.js"
license: "MIT"
stars: 224
language: "JavaScript"
created: "2013-07-11"
updated: "2026-09-15"
forks: 52
open_issues: 5
commits_30d: 0
commit_cadence: "monthly"
commits_90d: 12
size_kb: 385
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:14:58.449847+00:00"
---

# svg.filter.js

## 出来ること

- svg.jsで作成した要素にSVGフィルターを適用できます。READMEにはガウスぼかし、彩度・色調の変更、ドロップシャドウ、ライティングなどの例があり、フィルターの解除、再利用、値のアニメーションにも対応する方法が記載されています。これらはREADMEに記載された機能・例であり、個別環境での動作は確認していません。

## 目的・背景

- svg.jsにフィルター機能を追加するプラグインです。

## 依存関係

- svg.jsが必要です。スクリプトタグで使う場合は、svg.jsの後にこのプラグインを読み込みます。

## 実行条件

- READMEにはnpmまたはYarnでの導入と、バンドラーを使わずにリリース配布物をscriptタグで読み込む方法が記載されています。

## 最短手順

- npmの場合は `npm i @svgdotjs/svg.filter.js` を実行します。次にsvg.jsを読み込んだ後、このプラグインを読み込み、要素に `filterWith` を使います。例: `image.filterWith(function (add) { add.gaussianBlur(30) })`

## 変更履歴

- 2026-11-23: 初回登録
