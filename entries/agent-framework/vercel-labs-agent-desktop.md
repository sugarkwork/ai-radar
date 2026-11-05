---
repo: "vercel-labs/agent-desktop"
name: "agent-desktop"
genre: agent-framework
url: "https://github.com/vercel-labs/agent-desktop"
license: "Apache-2.0"
stars: 15030
language: "Rust"
created: "2026-02-19"
updated: 2026-11-04
added: "2026-11-05"
first_seen: "2026-11-04"
source_post: "https://x.com/naka_1717/status/2118100305825169893"
sources: []
flags: []
risk_notes: ""
forks: 1039
open_issues: 163
size_kb: 64069
archived: false
commits_30d: 74
commits_90d: 100
commit_cadence: daily
fetched_at: "2026-11-05T00:04:14Z"
last_release: v1.1.0
last_release_at: 2026-11-03
---

# agent-desktop

## 出来ること

- デスクトップアプリを AI エージェントから操作するための CLI / C ライブラリ。スクリーンショットも画像の位置合わせも使わず、OS のアクセシビリティツリーを読んで「操作できる要素」を ref 付きの JSON で返す。
- エージェントは `snapshot` で要素一覧を取り、`click @s8f3k3p2:e8` のように ref を指定して押す／入力する。UI が変わっていた場合は `STALE_REF` / `AMBIGUOUS_TARGET` が返るので、取り直してから再操作する（モデルは同梱していない。ループは呼び出し側のエージェントが持つ）。
- 60 コマンド（うち 56 が稼働）。観測（`snapshot` `find` `get` `is` `screenshot` `list-surfaces`）、要素操作（`click` `type` `set-value` `toggle` `scroll-to` など）、キーボード・マウス、アプリ／ウィンドウ管理、通知、クリップボード、待機、セッション／trace。
- `agent-desktop mcp` で全コマンドを stdio の MCP ツールとして公開する（`desktop_snapshot`、`desktop_click` など）。`agent-desktop skills get desktop` / `platform` で、そのバイナリのバージョンに合った使い方ガイドを出力する。
- 既定はヘッドレス（ポインタ移動もフォーカス移動もしない）。物理入力を模したいときだけ `--headed`。

## 目的・背景

画面を「見せて」座標を当てる方式は、解像度・スケール・テーマ・アニメーションでずれる。agent-desktop は代わりに OS のアクセシビリティ API（macOS は AX、Windows は UI Automation、Linux は AT-SPI）から要素の木を取るので、位置合わせに依存しない。Vercel Labs の製品で、`agent-browser` と同じ系譜のドキュメント（agent-browser.dev/desktop）を持つ。

## 依存関係

- npm パッケージ `agent-desktop`（x64 / ARM64 のネイティブバイナリ同梱）。Bun / Yarn / pnpm でも入る。macOS・Linux は Homebrew も可。Scoop の公式パッケージは無い。
- JS ランチャー無しで動かす場合は GitHub Releases のネイティブアーカイブを展開する。

## 実行条件

- macOS 13 以降（Intel / Apple Silicon）、Windows 10 1809 以降（x64 / ARM64）、Ubuntu 24.04 以降（X11 / Wayland）。
- macOS はアクセシビリティ権限が必要（`agent-desktop permissions --guide` が誘導する）。Linux / Windows でも権限や Wayland の制約で一部コマンドが動かない場合があり、README はプラットフォーム別ページで「ヘッドレスで動くもの／`--headed` が要るもの／拒否されるもの」を分けて書いている。
- スナップショット・クリップボード・スクリーンショット・コマンド出力には私的な画面内容が入る。README もログやアップロードに載せないよう注意している。

## 最短手順

```bash
npm install -g agent-desktop
agent-desktop status                 # プラットフォーム・権限・対応サーフェス
agent-desktop snapshot --app Finder -i
agent-desktop click @s8f3k3p2:e8
```

## 変更履歴

- 2026-11-05: 初回登録（★15,021 / Apache-2.0 / Rust / 最終push 2026-11-04）
