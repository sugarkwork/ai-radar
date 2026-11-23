---
name: "Pixprite"
genre: "other"
url: "https://github.com/vicimpa/pixprite"
repo: "vicimpa/pixprite"
flags: ["unverified"]
risk_notes: "READMEでは「Early development」とされ、最新リリースは0.0.8と記載されています。"
stars: 36
forks: 3
open_issues: 1
size_kb: 3251
language: "TypeScript"
created: "2025-09-04"
updated: "2026-11-09"
archived: false
license: "MIT"
commits_30d: 58
commits_90d: 63
commit_cadence: "daily"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/dextune/status/2119422188369359086"]
fetched_at: "2026-11-22T04:54:55.163612+00:00"
---

# Pixprite

## 出来ること

- ブラウザーまたはデスクトップで動くピクセルアート編集ソフトです。描画、アニメーション、レイヤーや変形を使った編集、タイルマップ作成に対応し、`.pixprite`、`.aseprite`、PNG、GIF、APNG、WebM、スプライトシート、ZIP形式でファイルを扱えます。ローカルMCPサーバー経由で、対応クライアントからドキュメントの確認・編集、コマンド実行、書き出しもできます。これらはREADMEの説明で、独立した動作確認ではありません。

## 目的・背景

- ピクセルアート、アニメーション、タイルマップをブラウザーまたはデスクトップで作成・編集するための独立プロジェクトです。READMEでは開発初期段階と説明されています。

## 依存関係

- README記載のローカル開発ではBun 1.4.2を使用します。デスクトップ版のビルドにはRustとTauriの前提条件が必要です。MCPはネイティブRustプロセスで動作し、実行時にNode.jsやBunを必要としないとREADMEにあります。

## 実行条件

- ローカル起動手順は `bun install --frozen-lockfile` の後に `bun run dev` です。デスクトップ版の開発起動には `bun run desktop:dev`、現在のOS向けインストーラーの作成には `bun run desktop:build` を使います。デスクトップアプリの対象OSはmacOS、Windows、LinuxとREADMEに記載されています。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- Bun 1.4.2を用意し、リポジトリで `bun install --frozen-lockfile`、続けて `bun run dev` を実行してローカル開発版を起動します。READMEにある開発用URLは省略されているため、起動後のアクセス先はここでは確認できません。

## 変更履歴

- 2026-11-23: 初回登録
