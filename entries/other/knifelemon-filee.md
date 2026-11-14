---
name: "Filee"
genre: "other"
url: "https://github.com/KnifeLemon/Filee"
repo: "KnifeLemon/Filee"
stars: 26944
forks: 1546
open_issues: 108
size_kb: 49177
language: "C#"
created: "2026-09-29"
updated: "2026-11-14"
archived: false
license: "MIT"
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/bkdgiffug/status/2118810151167856808"]
fetched_at: "2026-11-14T10:12:34.239777+00:00"
---

# Filee

## 出来ること

- カーソル位置に形式メニューを表示し、ファイルを形式にドロップして変換するデスクトップアプリ。READMEは画像、文書、動画・音声、アーカイブ、CAD、3Dモデルなど270形式への対応、オフライン動作、元ファイルと同じ場所への保存を説明している。ほかに一括変換、監視フォルダー、トリミング、変換設定、ブラウザーからのファイルやリンクの取り込み、CLIを記載。出典（作者の説明）: https://github.com/KnifeLemon/Filee

## 目的・背景

- READMEでは、アプリ画面を開かず、キーを押しながらファイルをドラッグしてカーソル位置のドーナツ型メニューから変換形式を選ぶ方式として紹介されている。出典（作者の説明）: https://github.com/KnifeLemon/Filee

## 依存関係

- READMEはWindows版のセットアップについて、追加ソフト不要と記載。Linux x64/ARM64版はUbuntu 22.04以降でPython 3が必要。各形式に必要な変換エンジンを追加できる旨も記載されているが、エンジンごとの依存関係はこの資料では特定できない。出典: https://github.com/KnifeLemon/Filee

## 実行条件

- README記載の対象環境はWindows 10/11、macOS 13以降（preview）、Linux x64/ARM64（Ubuntu 22.04以降）。Linuxでドラッグ操作を使うにはX11が必要で、Waylandではドロップゾーンまたはファイルマネージャーの右クリックメニューを使う。macOS版は未公証のため、初回起動時にプライバシーとセキュリティ設定から許可する手順が案内されている。出典: https://github.com/KnifeLemon/Filee

## 最短手順

- READMEの案内: Releasesから対象OSの配布物を取得する。Windowsはセットアップを実行するかPortable ZIPを展開してFilee.exeを起動。macOSはパッケージを展開して./install.shを実行するか、DMG内のアプリをApplicationsへ移動。Linuxはパッケージを展開して./install.shを実行する。その後、キーを押しながらファイルをドラッグし、表示された形式へドロップする。出典: https://github.com/KnifeLemon/Filee

## 変更履歴

- 2026-11-14: 初回登録
