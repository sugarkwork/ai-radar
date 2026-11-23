---
name: "p5.capture"
genre: "other"
url: "https://github.com/tapioca24/p5.capture"
repo: "tapioca24/p5.capture"
license: "MIT"
stars: 318
language: "TypeScript"
created: "2022-02-17"
updated: "2026-04-15"
forks: 9
open_issues: 13
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 327
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:17:41.269915+00:00"
---

# p5.capture

## 出来ること

- p5.jsのdraw関数にフックして描画フレームを記録し、WebM、GIF、MP4、PNG、JPG、WebPとして書き出せる。GUIでの録画開始・停止のほか、APIで録画を制御できる。READMEでは、画面録画に比べてフレームレートが不安定になりにくいと説明しているが、これは作者の説明であり独立実測ではない。

## 目的・背景

- p5.jsアニメーションの録画機能を、スケッチにコードを追加せずに利用できるようにすることを目的としている。READMEには、GUIに加えてAPIからの組み込みにも対応するとある。

## 依存関係

- READMEに記載された書き出し形式ごとの利用ライブラリは、WebMがwebm-writer-js、GIFがgif.js、MP4がh264-mp4-encoder。PNG・JPG・WebPは画像をZIPファイルにまとめて出力する。

## 実行条件

- READMEの導入例では、p5.jsを読み込んだ後にp5.captureのUMDファイルを読み込む。p5.captureはブラウザ上で利用する構成として説明されている。形式ごとに利用可能な設定が異なり、bitrateはMP4のみ、qualityはWebM・GIF・JPG・WebPのみ、autoSaveDurationはPNG・JPG・WebPのみ。

## 最短手順

- HTMLでp5.jsを読み込み、その後にREADME記載のp5.captureスクリプトを追加する。初期状態ではGUIから録画を開始・停止できる。コードから操作する場合は`P5Capture.getInstance()`でインスタンスを取得し、`start()`と`stop()`を呼び出す。既定オプションの変更はp5.jsの初期化前に`P5Capture.setDefaultOptions()`で行う。

## 変更履歴

- 2026-11-23: 初回登録
