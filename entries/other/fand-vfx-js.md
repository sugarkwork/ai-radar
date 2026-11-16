---
name: "VFX-JS"
genre: "other"
url: "https://github.com/fand/vfx-js"
repo: "fand/vfx-js"
license: "MIT"
stars: 1190
language: "TypeScript"
created: "2019-12-14"
updated: "2026-11-14"
forks: 40
open_issues: 8
commits_30d: 55
commit_cadence: "daily"
commits_90d: 55
size_kb: 110282
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/slashui/status/2122136865960562784"]
fetched_at: "2026-11-16T10:25:06.262014+00:00"
---

# VFX-JS

## 出来ること

- HTMLの画像・動画・テキストなどにWebGLエフェクトを適用し、エフェクトを重ねたりGLSLで独自エフェクトを書いたりできます。DOMをキャプチャしてページ遷移エフェクトを適用する機能も説明されています。出典: https://github.com/fand/vfx-js

## 目的・背景

- ウェブサイトの要素やページ遷移にWebGLエフェクトを追加するライブラリです。READMEには、ページ遷移終了後に対象要素が通常のDOMに戻ると記載されています。出典: https://github.com/fand/vfx-js

## 依存関係

- 要素エフェクトの例では npm パッケージ `@vfx-js/core` を使用し、プリセットの合成例では `@vfx-js/effects`、遷移例では `@vfx-js/transitions` を使用しています。出典: https://github.com/fand/vfx-js

## 実行条件

- WebGLが必要です。WebGLが使えない場合、`VFX.init()` は `null` を返します。HTML-in-CanvasによるDOMキャプチャはREADME上で実験的とされ、Chrome Canaryまたはフラグ付きChromeに限られます。他の環境ではSVG画像として複製する方式で、Webフォント、疑似要素、canvas内容などがキャプチャに含まれない場合があります。出典: https://github.com/fand/vfx-js

## 最短手順

- 要素エフェクトは `npm i @vfx-js/core` で導入し、`VFX` を作成して `vfx.add(img, { shader: "glitch", overflow: 100 })` のように対象要素へ適用します。出典: https://github.com/fand/vfx-js

## 変更履歴

- 2026-11-16: 初回登録
