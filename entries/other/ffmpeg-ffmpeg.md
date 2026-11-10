---
repo: "FFmpeg/FFmpeg"
name: "FFmpeg"
genre: "other"
url: "https://github.com/FFmpeg/FFmpeg"
flags: ["unverified"]
risk_notes: "GitHubの最新リリース情報、個別ビルドで利用できるコーデック、処理速度・出力品質、AIエージェントからの実行は未検証。READMEはGitHubの公開rawファイルで確認した。 GitHub APIでライセンスを確認できていません。"
stars: 66858
forks: 14558
open_issues: 3
size_kb: 506833
language: "C"
created: "2011-04-14"
updated: "2026-11-10"
archived: false
license: "unknown"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/nuannuan_share/status/2119640438135242817"]
fetched_at: "2026-11-10T09:31:04Z"
---

# FFmpegでAI生成素材を変換・検査する

## 出来ること

- ffmpegで映像・音声の変換やストリームの抽出を行い、ffprobeで出力の形式やストリームを検査できる。

## 目的・背景

- 生成した素材を後工程で扱える形式にそろえる用途に使える。libavcodecがコーデックを、libavformatがコンテナ形式と入出力を扱う。

## 依存関係

- ソースからのビルドにはGNU Make 3.81以降が必要。libx264などの外部依存は既定で無効。

## 実行条件

- 利用する環境にffmpegとffprobeを用意し、目的の形式に必要なコーデックがビルドで有効か確認する。公式ライセンス文書では主にLGPL 2.1以降が適用され、GPL対象のオプションを有効にすると適用条件が変わる。 [公式ライセンス文書](https://ffmpeg.org/doxygen/trunk/md_LICENSE.html)

## 最短手順

- ローカルコマンドの実行機能を持つAIエージェントに、手元の動画から音声を取り出すよう依頼する。例として、入力に音声がある場合に引数配列で `ffmpeg -n -i input.mp4 -vn output.wav` を呼び、成功後に `ffprobe -v error -show_streams -of json output.wav` を呼んで音声ストリームを確認する。これらのコマンドは今回実行していない。

## 変更履歴

- 2026-11-10: 初回登録
