---
name: "paper-reel"
genre: "video-gen"
url: "https://github.com/haiderfarooq3/paper-reel"
repo: "haiderfarooq3/paper-reel"
stars: 141
forks: 23
open_issues: 1
size_kb: 5214
language: "JavaScript"
created: "2026-10-23"
updated: "2026-10-27"
archived: false
license: "MIT"
commits_30d: 3
commits_90d: 3
commit_cadence: "monthly"
flags: []
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
risk_notes: ""
sources: ["https://x.com/dextune/status/2119059798167531717"]
fetched_at: "2026-11-16T13:11:32.118823+00:00"
---

# paper-reel

## 出来ること

- Claude Codeにトピックを渡してスクリプトを作成し、音声・シーンを組み立ててMP4を書き出す。READMEでは、音声を基準にwhisper.cppで単語のタイミングを取り、シーンの小道具や字幕を同期させる仕組みを説明している。

## 目的・背景

- 紙の切り絵風の9:16解説リールを、コードで描画してMac上で生成するためのClaude Codeスキル。

## 依存関係

- README記載の構成要素はNode.js、ffmpeg、whisper.cpp、Kokoro（kokoro-onnxとモデルファイル）、HTML canvas、Playwright。renderer、frame tools、kit coreはanimateからvendorされたものと記載。

## 実行条件

- READMEの必要条件はmacOS、Node.js 18以上、ffmpeg、whisper.cpp。doctorコマンドは不足しているwhisperモデル、kokoro-onnx対応Python、Kokoroモデルファイルを確認すると記載されている。

## 最短手順

- READMEのInstall手順に従ってリポジトリを配置し、npm install、npx playwright install chromium、brewでffmpegとwhisper-cppを導入してからbin/reel doctorを実行する。生成はreel newでスターターを作成し、script.jsonとscenes.jsを編集、reel voice、reel check、reel exportの順で進める。

## 変更履歴

- 2026-11-16: 初回登録
