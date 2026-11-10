---
repo: ARahim3/DigUp
name: DigUp
genre: rag
url: https://github.com/ARahim3/DigUp
author: ARahim3
license: MIT
stars: 6341
language: Swift
created: 2026-10-08
updated: "2026-10-26"
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/Fluyeporlaweb/status/2117544561861972226
sources:
  - https://digup.arahim.dev
forks: 501
open_issues: 102
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 15983
archived: false
fetched_at: "2026-11-09T21:42:05Z"
last_release: "v0.6.2"
last_release_at: "2026-10-21"
---

# DigUp

## 出来ること

- パソコンの中身を「ファイル名」ではなく**中身**で探すデスクトップ検索アプリ。写真・スクリーンショット・PDF・文書・表計算・スライド・音声・動画・コードを横断し、該当ページや再生位置まで案内する。
- 検索は自然文。Google DeepMind の **EmbeddingGemma 2**（2026-10 公開のマルチモーダル埋め込みモデル）を llama.cpp の 8bit ビルドで動かし、画像・PDF ページ・文章・動画フレーム・音声30秒を同じ 768 次元空間のベクトルにする。テキストだけの検索ではなく「浜辺の犬」で犬の写真や動画の該当秒に当たる。
- 読み取り対象: 画像（JPEG/PNG/HEIC/WebP 等）、PDF（スキャン含む。長いものは先頭30ページ→残り。1ファイル最大5,000ページ）、文書（txt/md/typ/rtf/docx/odt/html、Mac は doc も）、表計算・スライド（xlsx/ods/pptx/odp の各シート名・行・スライド本文・ノート）、任意長の音声（30秒窓で分割、一致した瞬間を指す）、任意長の動画（数秒ごと・ショットごとのフレーム＋音声）。
- 取り込みは**指定したフォルダのみ**。処理はすべてローカルで、モデルも含めて外部送信しない。ベクトルとキーワード索引は 1 つの SQLite に保存し、コード検索用に別の索引も持つ。
- Mac ではスクリーンショット内の文字も読む。Windows / Linux では現時点でスクリーンショット OCR、旧 Word の doc、RAW 写真、SVG の読み取りが未対応。

## 目的・背景

Spotlight や Windows Search がファイル名・テキスト・メタデータで探すのに対し、**見た目・話している内容**で探すのが違い。検索語も同じモデルのテキスト側（約250MB、検索中のみ読み込み）で埋め込み、最近傍ベクトルと完全一致語を併用する。2026-10-08 作成、10-26 時点で 6,200 star。Swift 製で Trendshift の日間1位（Swift）にも載った。

## 依存関係

- macOS: Apple Silicon、macOS 14 以降（DMG または `brew install --cask arahim3/tap/digup`）
- Windows: 64bit Windows 10/11（ベータ、署名なしインストーラ）
- Linux: Ubuntu / Debian / Mint 系（.deb、ベータ）
- モデル同梱のためダウンロードは約865MB（テキスト 310MB ＋ 画像・音声エンコーダ 555MB）。アプリ本体は Mac 約20MB、Windows/Linux は同梱リーダーの分 40〜140MB
- GPU がある場合は Metal（Mac）/ Vulkan（Windows・Linux）を使い、起動時チェックで CPU より速くなければ CPU にフォールバックする

## 実行条件

- 索引対象はユーザーが選んだフォルダのみ。クラウド同期フォルダを含めるかは利用者次第。
- 長い PDF は先頭30ページを先に索引し、残りは後追い。音声・動画は 30 秒／数秒単位に切って埋め込むため、細かい台詞の一言を狙う用途より「その話題の箇所」を探す用途に向く。
- ベータ版の Windows / Linux は機能差あり（上記の未対応形式）。
- ダウンロード元は GitHub Releases と公式サイトのみと明記。第三者配布のインストーラは使わないよう注意喚起している。

## 最短手順

```bash
# macOS (Apple Silicon)
brew install --cask arahim3/tap/digup
# または Releases の DMG / Windows の setup.exe / Linux の .deb を導入し、
# アプリで対象フォルダを選んで索引を作成 → 自然文で検索
```

## 変更履歴

- 2026-11-04: 初回登録（v0.7.0-beta.3 時点）
