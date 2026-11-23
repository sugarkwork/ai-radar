---
name: "anidoodle"
genre: "image-gen"
url: "https://github.com/alexgreensh/anidoodle"
repo: "alexgreensh/anidoodle"
license: "Apache-2.0"
language: "TypeScript"
created: "2026-09-22"
updated: "2026-11-05"
archived: false
flags: ["unverified"]
risk_notes: "READMEの抜粋は途中で終わっているため、最短手順や対応するエージェント、実行条件、依存関係の全容はこの資料だけでは確認できない。"
stars: 1861
forks: 166
open_issues: 7
size_kb: 48699
commits_30d: 36
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/flxrnc/status/2123392905934999811"]
fetched_at: "2026-11-20T03:13:46.477390+00:00"
---

# anidoodle

## 出来ること

- READMEによると、コードでイラスト、描画タイムラプス、映像、解説、インタラクティブなWebアートを作成する。32種類の描画スタイルを用意し、各スタイルで完成画像と描画過程の映像を同じソースから生成すると説明している。音楽や効果音もコードで作成できるとしている。

## 目的・背景

- 「手描き風のアートをコードで記述する」ことを掲げ、同じソースから各マシン・サイズで同じ絵を再描画できるとREADMEで説明している。

## 依存関係

- README抜粋にはNode.jsのコマンド例がある。任意のサウンドパックは373 MBのダウンロードと記載されている。その他の依存関係は抜粋から確認できない。

## 実行条件

- READMEはClaude Code、Codex、Grok Build、およびスキルを読めるエージェントで利用できると記載している。必要なバージョンや詳細な実行条件は抜粋から確認できない。

対応言語: READMEの言語表示は英語、日本語（README.ja-JP.md）、簡体字中国語、韓国語、フランス語、スペイン語。これはREADMEの翻訳言語であり、生成機能が受け付ける自然言語は確認できない。（出典: https://github.com/alexgreensh/anidoodle）
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- README抜粋では、インストール先と導入済み内容の確認に `node <skill>/engine/tools/soundfetch.mjs list` を、任意サウンドパックの取得に `node <skill>/engine/tools/soundfetch.mjs get all` を案内している。サウンドパック取得時はエージェントが事前確認すると記載。全体の導入手順は抜粋に含まれず確認できない。

## 変更履歴

- 2026-11-23: 初回登録
