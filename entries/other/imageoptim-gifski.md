---
name: "gifski"
genre: "other"
url: "https://github.com/ImageOptim/gifski"
repo: "ImageOptim/gifski"
license: "unknown"
stars: 5710
language: "Rust"
created: "2017-11-01"
updated: "2026-06-17"
forks: 183
open_issues: 38
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 709
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIのライセンス値はunknown。READMEにはAGPL 3 or laterと記載されているが、商用ライセンスの条件・料金は確認できない。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/taki_auto/status/2122162883320848580"]
fetched_at: "2026-11-16T05:24:34.784426+00:00"
---

# gifski

## 出来ること

- 動画フレームをGIFアニメーションに変換するCLIツール。PNGフレームの入力にも対応し、Cライブラリとして他のアプリから利用できる。幅・高さや品質設定を調整できる。

## 目的・背景

- pngquantの機能を使い、フレーム間で効率的なパレットを共有し、時間方向のディザリングを行ってGIFを生成する。READMEはGIFの圧縮では大きな品質低下に対してファイルサイズの削減が小さい場合があると説明している。

## 依存関係

- ソースからの基本ビルドにはRustが必要。動画をffmpegからストリーム入力する手順にはffmpegが必要。動画の直接デコード機能は既定で有効ではなく、ffmpeg 6.x、libclangおよびヘッダー類が必要。

## 実行条件

- CLIとして利用できる。README記載のrustup経由のビルド要件はRust 1.63以上。動画の直接デコード機能を使う場合は追加依存関係が必要で、READMEは導入が難しい場合があると説明している。

## 最短手順

- ffmpegから動画を渡す例: `ffmpeg -i video.mp4 -f yuv4mpegpipe - | gifski -o anim.gif -`。PNGフレームから作る場合は `gifski -o anim.gif frame*.png`。READMEでは `-` が標準入力を表すと説明している。

## 変更履歴

- 2026-11-16: 初回登録
