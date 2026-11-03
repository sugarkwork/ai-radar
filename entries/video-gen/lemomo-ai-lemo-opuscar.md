---
repo: "lemomo-ai/lemo-opuscar"
name: "Lemo-Opuscar"
genre: "video-gen"
url: "https://github.com/lemomo-ai/lemo-opuscar"
license: "MIT (コード) / CC BY 4.0 (スタイル記述)"
stars: 11571
language: "JavaScript"
created: "2026-09-26"
updated: 2026-10-31
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 1327
open_issues: 11
commits_30d: 60
commits_90d: 80
commit_cadence: daily
size_kb: 156727
archived: false
fetched_at: "2026-11-03T15:43:22Z"
last_release: thanks
last_release_at: 2026-10-12
---

# Lemo-Opuscar

## 出来ること

- コードで作る「映画のスタイル」66種のツールボックス。各スタイルは「スタイルプロンプト＋そのスタイルで実際に作った短編デモ」の組で、動画生成モデルを使わず Canvas 描画とコードで映像を作る。
- スタイルを選んで筋書きを渡すと、エージェントが絵コンテ・作画・音楽まで通して1本作る。自作スタイルの追加・保存にも対応（`~/lemo-my-styles/` に保存され、更新時も残る）。
- カテゴリ例: Edit & Documentary（実素材・文書・データから切る8種）、Evidence Films（数値に出典を付ける8種）。
- ギャラリーサイトで全スタイルのデモを再生できる。

## 目的・背景

Lemomo（@lemomo_ai）による 2026-09 公開、1.1万 star。**Claude Opus 5.5 向けに調整**されており、README が「他モデルでは再現性が落ちるので注意」と明記している点は導入判断の材料になる。

## 依存関係

- Node 20 以上、ffmpeg 7 以上、Python 3.11 以上（または uv）。残りの依存はエージェントが入れる。
- Ubuntu 24.04 の ffmpeg 6.1 は古すぎるため、静的ビルドを使うよう README が指示している。
- Claude Code のプラグイン機構（marketplace）を使う。

## 実行条件

- コードで描画するため GPU 不要。書き出しに ffmpeg とディスク容量を使う。
- ライセンスはコードが MIT、スタイル記述が CC BY 4.0 の二本立て。
- 生成物の品質はモデル依存（Opus 5.5 前提）。他モデルでの動作は未確認。

## 最短手順

```bash
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
# 導入後、Claude Code で /lemo-opuscar:lemo-opuscar を実行
```

## 変更履歴

- 2026-11-03: 初回登録（star 11,561 / pushed 2026-10-31 / MIT+CC BY 4.0）
