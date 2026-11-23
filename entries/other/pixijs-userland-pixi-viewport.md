---
name: "pixi-viewport"
genre: "other"
url: "https://github.com/pixijs-userland/pixi-viewport"
repo: "pixijs-userland/pixi-viewport"
license: "MIT"
stars: 1222
language: "TypeScript"
created: "2017-08-29"
updated: "2026-11-14"
forks: 184
open_issues: 10
commits_30d: 27
commit_cadence: "daily"
commits_90d: 27
size_kb: 47118
archived: false
flags: ["unverified"]
risk_notes: "READMEによると、2026年10月以降、Claudeがコード編集を支援し、メンテナーが各変更をリリース前にレビューしている。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:15:47.998057+00:00"
---

# pixi-viewport

## 出来ること

- pixi.js向けの設定可能な2D viewport／カメラです。ドラッグ、ピンチやホイールによるズーム、慣性ドラッグ、対象追従、アニメーション、点やズーム倍率へのスナップ、境界制限、端でのバウンス、画面端でのマウス移動に対応するとREADMEに記載されています。各機能は設定・取り外し可能です。

## 目的・背景

- pixi.jsのシーンを移動・拡大縮小するviewportを提供します。v7.0.0はpixi.js v8.22でテストされ、多数の修正と挙動変更を含むメジャーリリースと説明されています。

## 依存関係

- pixi.jsを使用します。入力機能にはpixiのEventSystemが必要です。

## 実行条件

- READMEの例はブラウザーでpixi.js v8系のApplicationを初期化し、renderer.eventsをViewportに渡します。READMEではv7.0.0をpixi.js v8.22でテストしたとしています。

## 最短手順

- `npm i pixi-viewport`で導入し、`import { Viewport } from "pixi-viewport"`で読み込みます。`new Viewport({ screenWidth, screenHeight, worldWidth, worldHeight, events: app.renderer.events })`で作成してstageに追加し、`viewport.drag().pinch().wheel().decelerate()`でプラグインを有効にします。

## 変更履歴

- 2026-11-23: 初回登録
