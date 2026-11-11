---
name: "MoviePy"
genre: "video-gen"
url: "https://github.com/Zulko/moviepy"
repo: "Zulko/moviepy"
license: "MIT"
stars: 15136
language: "Python"
created: "2013-08-12"
updated: "2026-08-26"
forks: 2147
open_issues: 96
commits_30d: 0
commit_cadence: "stale"
commits_90d: 1
size_kb: 169976
archived: false
flags: ["unverified"]
risk_notes: "README says MoviePy is slower than using ffmpeg directly. Version 1 is no longer maintained; version 2 introduced breaking changes."
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/AIExplorerTim/status/2118242415219982564"]
fetched_at: "2026-11-11T08:18:27.582682+00:00"
---

# MoviePy

## 出来ること

- Pythonで動画のカット、結合、タイトル挿入、動画合成、動画処理、カスタムエフェクト作成ができる。音声・動画を読み込み、クリップを合成して出力できる。READMEの例では動画の一部を切り出し、音量を調整し、タイトルを重ねて書き出している。

## 目的・背景

- 動画フレーム、画像、音声をPythonオブジェクト（numpy配列）に変換し、ピクセルにアクセスして動画・音声エフェクトを定義できる。READMEは、柔軟で扱いやすい一方、データの読み込み・書き出し処理が重いためffmpegを直接使う場合より遅いと説明している。

## 依存関係

- Python 3.9以上。READMEは追加のインストールオプションとしてカスタムFFMPEGの利用に言及している。

## 実行条件

- Windows、Mac、Linuxで動作するとREADMEに記載。インストールは `pip install moviepy`。

## 最短手順

- `pip install moviepy` でインストールし、READMEの例のように `VideoFileClip` で動画を開いて `subclipped` で範囲を選び、`TextClip` と `CompositeVideoClip` でタイトルを重ね、`write_videofile` で出力する。

## 変更履歴

- 2026-11-11: 初回登録
