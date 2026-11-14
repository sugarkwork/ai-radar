---
name: "OpenCut"
genre: "other"
url: "https://github.com/OpenCut-app/OpenCut"
repo: "OpenCut-app/OpenCut"
flags: ["unverified"]
risk_notes: "このリポジトリの改修版が利用可能になる時期や、記載された開発手順が現在も動作するかはREADMEから確認できません。"
stars: 98341
forks: 9823
open_issues: 386
size_kb: 28243
language: "TypeScript"
created: "2025-06-22"
updated: "2026-09-24"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 1
commit_cadence: "stale"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/ruyi3699/status/2118847396427788789"]
fetched_at: "2026-11-14T14:08:32.163072+00:00"
---

# OpenCut

## 出来ること

- Web・デスクトップ・モバイル向けの無料オープンソース動画編集ソフトウェアとして説明されています。READMEでは現行リポジトリを全面改修中とし、Editor API、プラグイン、MCPサーバー、ヘッドレスモードなどは「今後予定」として記載しています。出典: https://github.com/OpenCut-app/OpenCut

## 目的・背景

- プラグインを重視したアーキテクチャを含む形で、ソフトウェアを一から書き直しているとREADMEにあります。現在使う版としてclassicリポジトリを案内しています。出典: https://github.com/OpenCut-app/OpenCut

## 依存関係

- 開発環境ではprotoのインストールと、リポジトリのルートでの `proto use` がREADMEに記載されています。出典: https://github.com/OpenCut-app/OpenCut

## 実行条件

- README記載の開発用コマンドはLinux、macOS、WSL、Windows（PowerShell）を対象にしています。Windowsではprotoのインストール方法が別途示されています。出典: https://github.com/OpenCut-app/OpenCut

## 最短手順

- READMEに従いprotoを導入してリポジトリのルートで `proto use` を実行し、Web開発サーバーは `moon run web:dev`（localhost:5173）、API開発サーバーは `moon run api:dev`（localhost:8787）で起動します。出典: https://github.com/OpenCut-app/OpenCut

## 変更履歴

- 2026-11-14: 初回登録
