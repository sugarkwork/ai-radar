---
repo: "gmpetrov/agent-screenplay"
name: "Screenplay"
genre: video-gen
url: "https://github.com/gmpetrov/agent-screenplay"
license: "MIT"
stars: 23
language: "TypeScript"
created: "2026-11-02"
updated: 2026-11-03
added: "2026-11-04"
first_seen: "2026-11-04"
sources: []
flags: []
risk_notes: ""
forks: 0
open_issues: 0
size_kb: 4941
archived: false
commits_30d: 22
commits_90d: 0
commit_cadence: daily
last_release: "v0.1.7"
---

# Screenplay

## 出来ること

- エージェントに「こういうデモ動画を作って」と頼むと、対象サイト（自社でも他人のものでも）やデスクトップアプリを操作し、**演出付きのスクリーンレコーディング**を作る。
- エージェントが短い「シナリオ」を書き、Screenplay がブラウザ（またはデスクトップアプリ）で再生して撮影し、動画として編集する。
- 編集は Screen Studio 相当を狙う: カーソルの滑らかな移動、操作に追従する自動ズーム、クリックエフェクト、コールアウト、スポットライト、字幕、タイトルカード、任意でナレーション。
- **本体に AI は入っていない**（モデルの API キーも不要）。考えるのはエージェント側、撮影と編集が Screenplay の役割という分担。
- MCP サーバーとして動き、Claude Code / Codex / Cursor など MCP クライアントから呼べる。MCP レジストリに登録済み。

## 目的・背景

プロダクトデモ動画の作成を、画面収録＋手編集の作業から「エージェントへの1プロンプト」に置き換える試み。2026-11-02 公開の新しいプロジェクトで、公開直後の登録。

## 依存関係

- Node.js（npm パッケージ `agent-screenplay`）。
- 初回の `init` で Chromium をダウンロードする（デスクトップアプリの撮影にも使う）。
- エージェント側は MCP クライアントであればよい。

## 実行条件

- ライセンスは MIT。
- **★23・公開から2日**のため、実利用の報告はまだほとんどない。API は v0.1 系で変わりやすい。
- 他人のサイトを撮影する場合、そのサイトの利用規約と著作権に注意する。

## 最短手順

```bash
npx agent-screenplay init     # Chromium 取得 + MCP サーバー登録 + ガイド導入
# エージェントを再起動し、「〜を紹介する動画を作って」と依頼する
```

## 変更履歴

- 2026-11-04: 初回登録（★23 / MIT / 公開 2026-11-02 / v0.1.7）
