---
name: "Satori"
genre: "other"
url: "https://github.com/vercel/satori"
repo: "vercel/satori"
license: "MPL-2.0"
stars: 14195
language: "TypeScript"
created: "2022-01-27"
updated: "2026-11-12"
forks: 404
open_issues: 169
commits_30d: 5
commit_cadence: "weekly"
commits_90d: 100
size_kb: 21000
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RealMarvelX/status/2119161121387020570"]
fetched_at: "2026-11-17T06:28:43.811227+00:00"
---

# Satori

## 出来ること

- JSXまたはReact要素風オブジェクトを入力し、レイアウトやフォントを処理してSVG文字列を生成する。PNGなどの画像形式にする場合はSharpを使う方法がREADMEに記載されている。

## 目的・背景

- HTML/CSSの一部をSVGに変換するライブラリ。READMEでは、OG画像やソーシャルカード生成の案内先としてVercelの資料を紹介している。

## 依存関係

- PNG出力例ではSharpを使用する。フォントを使う場合はBufferまたはArrayBufferとして読み込んだデータを指定する。

## 実行条件

- 入力は純粋でステートレスなJSX要素に限られ、ReactのuseStateやuseEffectは非対応。CSSとHTMLは限定的なサブセットで、ブラウザー描画との完全一致は保証されない。実験的なWebGL canvas機能はNode.js 20.16以降でglパッケージを利用できるほか、ブラウザーとWeb WorkersではOffscreenCanvasを使う。

## 最短手順

- satoriを読み込み、要素とwidth、height、fontsを渡してawait satori(element, options)を呼び出す。返るSVG文字列をPNGにする場合は、SharpにBuffer.from(svg)を渡してpng().toBuffer()を呼び出す。

## 変更履歴

- 2026-11-22: 初回登録
