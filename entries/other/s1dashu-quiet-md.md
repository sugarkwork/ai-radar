---
name: "Quiet.md"
genre: "other"
url: "https://github.com/s1dashu/quiet-md"
repo: "s1dashu/quiet-md"
license: "MIT"
stars: 1740
language: "Rust"
created: "2026-11-01"
updated: "2026-11-13"
forks: 157
open_issues: 76
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 30807
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-13"
first_seen: "2026-11-13"
sources: ["https://x.com/Ryrenz/status/2118645832056541192"]
fetched_at: "2026-11-13T07:21:55.847216+00:00"
---

# Quiet.md

## 出来ること

- RustとGPUIで描画するローカルノートアプリ。見出し、リスト、To-do、表、コード、数式、画像、添付ファイルなどを含むリッチテキスト編集、全文検索、文書ツリーでの整理ができる。MarkdownとFeishu (Lark) DocxXMLのインポート、MarkdownとPDFへのエクスポートに対応する。

## 目的・背景

- ノートをユーザーのコンピューター上の通常のフォルダーに保存し、アカウントやクラウドを使わずに管理することを掲げている。READMEによると、既定ではネットワーク通信を行わず、任意の更新確認を除く。

## 依存関係

- README記載の描画技術はRustとGPUI。実行時にWebView、Electron、バックグラウンドサービスを使わないとREADMEは説明している。その他の依存関係は添付READMEから確認できない。

## 実行条件

- macOSは13以降（Apple SiliconまたはIntel）、Windowsはx64でWindows 10 version 2004以降。Linuxは実験的対応で、x86_64、glibc 2.35以降が要件。LinuxではFUSEがない場合、READMEは`--appimage-extract-and-run`の使用を案内している。ベータ版。

## 最短手順

- 対象OS向けの配布パッケージを入手して起動する。macOSはZIPを展開して`quiet.md.app`をApplicationsへ移動。Windowsはインストーラーを実行。LinuxはAppImageに実行権限を付けて起動する。初回起動時、空のライブラリーにはGetting startedガイドが追加される。

## 変更履歴

- 2026-11-13: 初回登録
