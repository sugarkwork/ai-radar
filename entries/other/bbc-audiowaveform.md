---
name: "audiowaveform"
genre: "other"
url: "https://github.com/bbc/audiowaveform"
flags: ["unverified"]
risk_notes: "READMEによると、継続開発は https://codeberg.org/chrisn/audiowaveform に移っています。この候補の対象URLは指定どおりGitHubリポジトリです。"
repo: "bbc/audiowaveform"
stars: 2171
forks: 253
open_issues: 43
size_kb: 4496
language: "C++"
created: "2013-10-14"
updated: "2025-08-24"
archived: false
license: "GPL-3.0"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:17:01.587116+00:00"
---

# audiowaveform

## 出来ること

- MP3、WAV、FLAC、Ogg Vorbis、Opus形式の音声から波形データを生成します。データは.datまたはJSON形式で保存でき、波形データを入力として、時間位置とズームを指定したPNG画像を描画できます。

## 目的・背景

- 音声を視覚的に表現する波形データを作り、オーディオ編集アプリケーションに似た表示に利用できます。READMEでは、入力チャンネルをモノラルにまとめ、--zoomで指定したサンプル数ごとに最小値と最大値を計算すると説明しています。

## 依存関係

- ソースからのビルドにはCMake 2.8.7以降、g++ 4.6.3以降、Boost 1.46.0以降が必要とREADMEに記載されています。実行時依存としてlibmad、libsndfile、libid3tag、gd、Boostが挙げられています。

## 実行条件

- READMEにはUbuntu、Debian、RHEL系、Arch Linux、macOS、Windows、Amazon Linux向けの配布・導入情報があります。ソースビルド時の依存パッケージや手順はOSごとに異なります。

## 最短手順

- UbuntuではREADME記載の手順でPPAを追加し、`sudo apt-get update`、`sudo apt-get install audiowaveform`を実行します。Dockerの例では、作業ディレクトリを`/tmp`にマウントし、`awf -i input.wav -o output.png`でPNGを生成します。

## 変更履歴

- 2026-11-23: 初回登録
