---
name: "Konva"
genre: "other"
url: "https://github.com/konvajs/konva"
repo: "konvajs/konva"
license: "unknown"
stars: 14961
language: "TypeScript"
created: "2015-01-09"
updated: "2026-11-10"
forks: 1074
open_issues: 3
commits_30d: 26
commit_cadence: "daily"
commits_90d: 100
size_kb: 23555
archived: false
flags: ["unverified"]
risk_notes: "GitHub APIでライセンスを確認できていません。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-15T03:20:11.463195+00:00"
---

# Konva

## 出来ること

- 対話型2D Canvas描画のためのシーングラフを提供します。図形ごとのイベント、ドラッグ操作、変形、アニメーション、キャッシュ、書き出しを利用でき、デザインエディタ、ホワイトボード、図表、注釈、地図などの視覚ツールに使えます。React、Vue、Svelte、Angular向け連携パッケージも案内されています。

## 目的・背景

- Web向けに対話型グラフィックス、エディタ、図表を構築するためのオープンソース2D Canvasフレームワークです。READMEによると、リポジトリはKineticJSのGitHubフォークとして始まりました。

## 依存関係

- ブラウザで利用する場合はnpmパッケージ `konva` またはUMD CDN読み込みを利用できます。Node.jsでレンダリングする場合は `canvas` または `skia-canvas` を別途インストールし、対応するバックエンドを読み込みます。

## 実行条件

- ES2018に対応する現代的なモバイルまたはデスクトップブラウザで動作します。Node.jsでのサーバーサイド描画はcanvasまたはskia-canvasバックエンドが必要です。DOMイベントにはブラウザが必要で、Canvas機能の対応範囲は選択したバックエンドに依存します。

## 最短手順

- `npm install konva` で導入し、`import Konva from 'konva'` で読み込みます。`Stage` と `Layer` を作成し、`Rect` などの図形をLayerに追加してStageに登録します。Node.js描画では先に `canvas` または `skia-canvas` を導入して対応バックエンドを読み込みます。

## 変更履歴

- 2026-11-15: 初回登録
