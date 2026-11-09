---
name: "FFmpeg"
genre: "video-gen"
url: "https://ffmpeg.org/"
author: "FFmpeg project"
pricing: "free"
pricing_detail: "無料。LGPL-2.1 以降、GPL 部分（libx264 等）を有効にすると全体が GPL-2.0 以降。本家はソースのみ配布し、バイナリは各 Linux ディストリ、Linux static builds、gyan.dev / BtbN の Windows ビルド、macOS static builds を利用する。アカウント・課金・レンダー課金はなく、任意の寄付のみ。最新安定版は 9.0.2（2026-09-18）。"
signup_required: false
flags: []
risk_notes: "LGPL でリンク・再配布する場合は --enable-gpl / --enable-nonfree を付けず、動的リンクとソース開示などの条件を満たす必要がある。GPL 部分を有効にすると全体が GPL になり、プロプライエタリ配布と両立しない。FFmpeg は商標であり、名称の扱いに注意。ffmpeg.org は取得時に一度接続タイムアウトし、再試行で 200 を得た（サーバー側の一時的な不調）。"
type: "link"
added: "2026-11-09"
first_seen: "2026-11-09"
sources: ["https://x.com/Y0urDumble/status/2114084322227503206"]
fetched_at: "2026-11-09T14:21:50Z"
---

# FFmpeg — 動画・音声の変換/編集をコマンド1本で行うフリーソフト

## 目的

- 動画・音声の録画、変換、ストリーミングを行うクロスプラットフォームのツール群。投稿の CGI スタックでは、完成した映像を 16:9・9:16・1:1 などの納品フォーマットに変換する『DELIVER』工程を担う。
- 編集ソフトではなく CLI/ライブラリなので、AI エージェントからはシェルコマンドとして呼び出す。HyperFrames のレンダーも内部で FFmpeg を使ってエンコードする。

## 何ができるか

- コンテナ変換（mp4/mov/webm など）、コーデック変換（H.264/H.265/AV1/ProRes など）、解像度・アスペクト比の変更、クロップ、トリム、連結、音声の抽出・ミックス、字幕の焼き込み、フレーム抽出ができる。
- `-vf scale=1080:1920` や `-filter_complex` で 1 本の入力から複数フォーマットを書き出せる。投稿の『one command → 16:9 hero, 9:16 reel, 1:1 feed』はこの種のフィルタ/出力指定で実現する。
- ハードウェアアクセラレーション（NVENC/QSV/VAAPI/Vulkan など）に対応し、GPU エンコードも選べる。FFmpeg 8.x 系では Vulkan compute ベースのコーデックも追加された。
- AI から使う形態は CLI 実行が基本。Python の `ffmpeg-python` や各言語のラッパー、HyperFrames のように内部で呼ぶツールもある。MCP サーバーや公式 API は提供していない。

## 料金

- 無料。LGPL-2.1 以降のフリーソフトで、GPL 部分を有効にすると GPL-2.0 以降になる。
- 本家はソースコードのみを配布し、コンパイル済みバイナリは各 Linux ディストリ、Linux static builds、Windows の gyan.dev / BtbN ビルド、macOS static builds から入手する。いずれも無料。
- レンダー課金・席課金・API 課金はない。プロジェクトへの寄付は任意。

## 登録の要否

- 不要。アカウントもログインもなく、ダウンロードページからソースやビルドへのリンクを辿れる。
- Linux は `apt install ffmpeg` などディストリのパッケージ、macOS は Homebrew の `ffmpeg`、Windows は gyan.dev / BtbN のビルドを展開して PATH に通す。
- 再配布する場合はライセンス条件（LGPL なら動的リンク・ソース開示、GPL 部分を有効にした場合は GPL 全体）を確認する。

## 変更履歴

- 2026-11-09: 初回登録
