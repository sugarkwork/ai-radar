---
repo: "debpalash/VoiceStudio"
name: "VoiceStudio"
genre: tts-audio
url: "https://github.com/debpalash/VoiceStudio"
license: "AGPL-3.0"
stars: 106057
language: "Python"
created: "2026-04-09"
updated: "2026-11-09"
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 11773
open_issues: 99
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 204303
archived: false
fetched_at: "2026-11-09T21:42:58Z"
last_release: "v0.5.7"
last_release_at: "2026-10-26"
---

# VoiceStudio

## 出来ること

- ローカル完結の音声スタジオ。声質複製（voice cloning）、声質設計、動画の吹き替え（タイミングを元音声に合わせる）、ディクテーション、文字起こし、オーディオブック / ナレーション、バッチ生成を1つのアプリで扱う。
- 646言語に対応（README 表記）。エンジンは複数を切り替えられ、モデルマネージャから必要なものだけダウンロードする。ダウンロード前に確認を取る。
- 配布形態: macOS（Homebrew cask / DMG / ワンコマンドインストーラ）、Windows / Linux（インストーラ、Docker イメージは GHCR）、iOS / Android（プレビュー版の APK / 署名なし IPA）。
- GPU がなくても CPU で動く（遅くなる）。セットアップは NVIDIA ドライバの有無を判定し、無ければ CPU 版 PyTorch を入れる（必要な空き容量は約5GB、CUDA 版は約9GB）。GGUF 系エンジンは Vulkan 経由で AMD / Intel / NVIDIA の GPU を利用でき、Windows / Linux では OmniVoice GGUF が GPU とモデルサイズを自動選択する。
- スマホ版（iOS 17 / Android 10 以降、プレビュー）はモデルを端末内で動かし、音声合成・声質複製・ディクテーション・吹き替えを、モデル取得後はオフラインで実行できる。PC 版とペアリングすると処理ごとに端末側か PC 側かを選べる。

## 目的・背景

ElevenLabs のローカル代替を掲げ、音声を作る・直す・書き起こす・吹き替える作業をデスクトップアプリ1つにまとめる。ブラウザ版ではなく Electron アプリと Docker、スマホ用プレビューアプリを配る構成で、モデルは各エンジンの実装（GGUF など）を内部で使い分ける。

## 依存関係

- OS 別のインストーラ（Python 環境の構築は不要）。
- モデルは初回利用時にアプリ内からダウンロード。

## 実行条件

- macOS は Apple Silicon / macOS 13.3 以上（Metal）。Windows / Linux はインストーラまたは Docker。
- スマホ版はストア未掲載のプレビュー。Android は APK（Obtainium / F-Droid リポジトリ対応）、iOS は署名なし IPA をサイドロードする（無料の Apple ID では7日で失効）。モデルは端末ごとにダウンロードする。
- ワンコマンドインストーラは `curl -fsSL https://voicestudio.sh/install | sh` 方式。中身を確認したい場合は `--version` / `--main` などのオプション付きで実行するか、リポジトリのスクリプトを読む。
- ライセンスは **AGPL-3.0**。組み込んで配布する場合はソース公開義務が及ぶ点に注意。
- 声質複製は参照話者の同意が前提。公開人物の声の複製は各国の法規・規約に従う。

## 最短手順

```bash
# macOS (Apple Silicon)
brew tap debpalash/tap
brew trust --cask debpalash/tap/voicestudio
brew install --cask debpalash/tap/voicestudio
# または
curl -fsSL https://voicestudio.sh/install | sh
```

## 変更履歴

- 2026-11-03: 初回登録（star 100,012 / pushed 2026-11-03 / AGPL-3.0）
- 2026-11-04: スマホ版（iOS/Android プレビュー）と GPU なし向け CPU ビルドを追記（v0.5.7）
