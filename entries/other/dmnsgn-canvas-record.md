---
name: "canvas-record"
genre: "other"
url: "https://github.com/dmnsgn/canvas-record"
repo: "dmnsgn/canvas-record"
license: "MIT"
stars: 434
language: "JavaScript"
created: "2019-06-18"
updated: "2026-11-13"
forks: 25
open_issues: 4
commits_30d: 4
commit_cadence: "weekly"
commits_90d: 11
size_kb: 27752
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0x5668_nft/status/2123395042471710938"]
fetched_at: "2026-11-19T16:14:50.966129+00:00"
---

# canvas-record

## 出来ること

- Canvasの2D/WebGL/WebGPU領域を、ブラウザー内またはファイルシステムへ記録できます。READMEにはMP4、WebM、MKV、MOV、GIF、PNG/JPGシーケンスへの出力が記載されています。WebCodecs、Wasm、MediaStreamなどを利用する複数のエンコーダーが案内されています。

## 目的・背景

- Canvas上の描画を動画や画像シーケンスとして記録するためのライブラリです。

## 依存関係

- READMEの使用例では `canvas-record`、`canvas-context`、`media-codecs` を読み込んでいます。FFmpegエンコーダーはバイナリパスの指定が必要とREADMEに記載されています。

## 実行条件

- ブラウザーで利用します。利用可能な出力形式やコーデックはエンコーダーおよびブラウザー機能に依存します。READMEはWebCodecsの対応状況を確認する手段として `isWebCodecsSupported` と media-codecs の確認ページを案内しています。FFmpegエンコーダーではSharedArrayBufferを使用すると記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- `npm install canvas-record` で導入し、READMEの例のように `Recorder` を作成して `start()` を呼び、描画ごとに `step()` を進めます。出力形式やエンコード設定に応じてエンコーダーを選択してください。

## 変更履歴

- 2026-11-23: 初回登録
