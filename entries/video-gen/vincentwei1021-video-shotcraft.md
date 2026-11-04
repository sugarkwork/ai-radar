---
repo: "Vincentwei1021/video-shotcraft"
name: "video-shotcraft"
genre: video-gen
url: "https://github.com/Vincentwei1021/video-shotcraft"
license: "Apache-2.0"
stars: 16970
language: "TypeScript"
created: "2026-07-19"
updated: 2026-10-29
added: "2026-11-03"
first_seen: "2026-11-03"
sources: []
flags: []
risk_notes: ""
forks: 1599
open_issues: 7
commits_30d: 10
commit_cadence: weekly
size_kb: 201181
archived: false
commits_90d: 44
fetched_at: "2026-11-04T22:51:48Z"
last_release: showcase-media
last_release_at: 2026-09-01
---

# video-shotcraft

## 出来ること

- Claude Code / Codex 向けの「動画制作スキル」。製品プロモのような映像を Remotion のコードとして出力するので、生成後にタイムラインやテキストを編集できる（ mp4 を吐いて終わりではない）。
- 152 枚のショットレシピカードと 209 本のモーションプレビュー（209 種類のスタイル）を同梱し、カメラワーク・トランジションの型を選んで組み合わせる。
- 音に合わせたカット割り（BGM のビート解析）、効果音の設計、字幕、ブランド要素の適用。
- 実写の mp4 をカードのヒーローとして組み込める ClipCard（`assets/lib/ClipCard.tsx`）があり、生成映像と実写素材を同じカードで扱える。
- 「Motion Workbench」でプレビューと調整。剪映（CapCut 中国版）向けの書き出しにも対応。
- ギャラリーサイトで仕上がり例を先に確認できる。

## 目的・背景

Remotion（React で動画を書くフレームワーク）を土台に、エージェントに「絵コンテ選び → 実装 → レンダリング → QA」までを一貫してやらせるためのスキル集。プロンプト一発の動画生成モデルではなく、編集可能な素材を作る方向。

## 依存関係

- Node.js と npm（Remotion のレンダリング、テンプレート、Workbench）。
- `ffmpeg` / `ffprobe`（フレーム確認と最終 QA）。
- `uv`（BGM のビート解析のみ。一度きりの Python スクリプト実行）。
- `puppeteer`（ページキャプチャを使う場合のみ。スクリプトがオンデマンドで入れる）。
- Remotion は初回レンダリング時に専用の headless Chrome を取得する。

## 実行条件

- Claude Code または Codex の skills ディレクトリに置く（`npx skills add` か symlink）。
- 動作検証は macOS が中心。ヘッドレス Linux / CI では `--concurrency=1` が必要、旧 headless モード廃止の影響でシステム Chromium ではなく `chrome-headless-shell` を使う、といった注意が README に列挙されている。
- リポジトリサイズが約 196MB と大きい（プレビュー素材を同梱しているため）。

## 最短手順

```bash
npx skills add Vincentwei1021/video-shotcraft
# もしくは手動で
git clone https://github.com/Vincentwei1021/video-shotcraft.git
ln -s "$(pwd)/video-shotcraft" ~/.claude/skills/video-shotcraft
```

## 変更履歴

- 2026-11-03: 初回登録（★16,517 / pushed 2026-10-29 / Apache-2.0）
- 2026-11-04: ショットカード152枚・プレビュー209本に増加、ClipCard を追記（showcase-media）
