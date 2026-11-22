---
name: "Swarm Rebuild"
genre: "other"
url: "https://github.com/DhvanilPatel/swarm-cursors"
repo: "DhvanilPatel/swarm-cursors"
license: "unknown"
stars: 3428
language: "JavaScript"
created: "2026-10-14"
updated: "2026-11-11"
forks: 378
open_issues: 21
commits_30d: 7
commit_cadence: "weekly"
commits_90d: 9
size_kb: 20455
archived: false
flags: ["unverified"]
risk_notes: "READMEには「None yet」とあり、ライセンスは設定されていない。コードの再利用条件は権利者への確認が必要。 GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-16"
first_seen: "2026-11-16"
sources: ["https://x.com/awe0_io/status/2119017257707941899"]
fetched_at: "2026-11-16T21:59:31Z"
last_release: ""
last_release_at: ""
---

# Swarm Rebuild

## 出来ること

- Chrome拡張機能として、ページを一時的に覆い、DOMのスナップショットをもとにテキスト、図形、線、メディア、重複要素をカーソル群が組み立てる様子を表示する。スクロールに追従し、速度変更、音、録画用の自動スクロール、再生・終了にも対応する。再構築は視覚表現で、元ページのスクリプトは再構築レイヤー内では動作しない。

## 目的・背景

- Swarm（Joel Califa作）へのトリビュート。元サイトのカーソルや群れの動き、構成の一部を取り入れ、任意のページを再構築するためのDOMスナップショット機能と拡張機能を加えている。

## 依存関係

- README記載では、Manifest V3の拡張機能で、スナップショット・描画・群れの処理は依存関係のない単一コンテンツスクリプト。音声はWeb Audio APIで合成する。

## 実行条件

- Chromeで拡張機能をインストールする。最新版を使う場合はリポジトリを取得し、chrome://extensions でDeveloper modeを有効にして swarm-rebuild/ をLoad unpackedする。自動再生は対象サイトへのアクセス許可が必要。chrome://、Chrome Web Store、PDFビューアでは動作しない。

## 最短手順

- Chrome Web Storeからインストールしてツールバーにピン留めし、対象ページで拡張機能アイコンをクリックするか Alt+Shift+S を押す。終了はEsc、✕、またはアイコン再クリック。

## 変更履歴

- 2026-11-16: 初回登録
