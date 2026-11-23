---
name: "pixi-ease"
genre: "other"
url: "https://github.com/davidfig/pixi-ease"
repo: "davidfig/pixi-ease"
license: "MIT"
stars: 105
language: "JavaScript"
created: "2017-09-12"
updated: "2026-11-06"
forks: 11
open_issues: 0
commits_30d: 6
commit_cadence: "weekly"
commits_90d: 6
size_kb: 14215
archived: false
flags: []
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
risk_notes: ""
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:08:42.955105+00:00"
---

# pixi-ease

## 出来ること

- PixiJSのパラメーターを補間してアニメーションできます。READMEによると、tintを含む任意のPixiJSパラメーター、数値パラメーター、scaleやskewの一括変更、Penner関数やユーザー定義関数、反復・反転、イベントを扱えます。shakeパラメーターも含まれます。

## 目的・背景

- PixiJS向けのeasing・tweening・animationライブラリです。READMEでは、v4はPixiJS v8対応で、旧バージョンのPixiJSにはpixi-ease v3を使うよう案内しています。

## 依存関係

- v4はpeerDependencyとしてpixi.js ^8を指定しています。READMEのインストール例は `npm i pixi-ease pixi.js` です。

## 実行条件

- READMEのv4移行情報ではPixiJS v8が必要です。tickerを指定した場合はrequestAnimationFrameを使用しないと説明されています。

## 最短手順

- `npm i pixi-ease pixi.js` で導入し、`import { Ease, ease } from 'pixi-ease'` として利用します。READMEの例では `ease.add(target, properties, options)` で対象のプロパティとduration、ease関数を指定しています。

## 変更履歴

- 2026-11-23: 初回登録
