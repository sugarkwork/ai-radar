---
name: "Shotcut"
genre: "other"
url: "https://github.com/mltframework/shotcut"
repo: "mltframework/shotcut"
license: "GPL-3.0"
stars: 15654
language: "C++"
created: "2012-04-23"
updated: "2026-11-11"
forks: 1565
open_issues: 48
commits_30d: 51
commit_cadence: "daily"
commits_90d: 100
size_kb: 161803
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/RealMarvelX/status/2118330503040221345"]
fetched_at: "2026-11-11T20:11:14.585112+00:00"
---

# Shotcut

## 出来ること

- クロスプラットフォームの動画編集ソフトです。READMEには、バイナリの配布先として https://www.shotcut.org/download/ が記載されています。

## 目的・背景

- READMEでは、Shotcutを無料のオープンソース動画編集ソフトと説明しています。AI生成機能についての説明は確認できません。

## 依存関係

- README記載の直接依存関係は、MLT、Qt 6（最低6.4）、FFTW、FFmpeg、Frei0r、SDLです。間接依存関係と同梱依存関係を含む一覧はcreditsページを参照するよう案内されています。

## 実行条件

- ビルドにはQt、MLT、frei0rなどのライブラリとヘッダーファイルを見つけられるよう、依存関係とパスの設定が必要です。READMEはビルドをベータテスターまたは開発貢献者向けとしています。インストールしない場合、実行時にQMLファイルを見つけられず起動に失敗することがあると説明しています。

## 最短手順

- 開発版を試す方法としてQt Creatorを案内しています。コマンドラインでは、ソースとは別のビルドディレクトリで `cmake -DCMAKE_INSTALL_PREFIX=/usr/local/ /path/to/shotcut` を実行し、続けて `cmake --build .`、`cmake --install .` を実行します。Ninjaジェネレーターの使用が推奨されています。

## 変更履歴

- 2026-11-11: 初回登録
