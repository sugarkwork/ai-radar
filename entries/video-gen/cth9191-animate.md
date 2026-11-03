---
repo: "cth9191/animate"
name: "Animate"
genre: "video-gen"
url: "https://github.com/cth9191/animate"
license: "MIT"
stars: 1441
language: "JavaScript"
created: "2026-10-04"
updated: 2026-10-05
added: "2026-11-03"
sources:
  - "https://x.com/daaihq/status/2117446567284367459"
flags: []
risk_notes: ""
forks: 186
open_issues: 6
commits_30d: 1
commits_90d: 10
commit_cadence: monthly
size_kb: 9385
archived: false
fetched_at: "2026-11-03T15:43:10Z"
---

# Animate

## 出来ること

- 1枚の `<canvas>` をコードで描き、フレーム単位で決定的に生成して MP4 に書き出す Claude Code スキル。解説動画・歴史もの・小さな物語に向く。
- 内蔵スタイル7種: 切り絵（cut paper）／クロスハッチ＋インク／リソ（孔版印刷）／スケッチブック／数学／ピクセル／アイソメトリック。参照画像から新スタイルを起こすこともできる（8つ目の枠）。
- 制作前に3段階の承認を挟む: ①構成（ビート表・事実は Web 検証）→ ②ルック（実寸のスタイルフレーム2〜4枚）→ ③絵コンテ（各ビートのキーフレームと音・トランジション）。
- 納品時に計測チェックを付ける: カットがビートグリッドに乗っているか、物語のラウドネス弧、主役の固定、無音後の最大音量、ナレーション速度。

## 目的・背景

2026-10 公開。`examples/history-of-ai/` に 60 秒の切り絵作品（1950年のチューリングから2025年まで15時代）が完全なサンプルとして入っている。

## 依存関係

- Node 18 以上、Playwright の Chromium、ffmpeg（PATH 上）。
- ナレーションを付ける場合のみ Python の `faster-whisper`（語単位のタイミング）と、任意で Claude の ElevenLabs コネクタ。
- フォントは OS のシステムフォント＋フォールバック（Windows / macOS / Linux 対応）。

## 実行条件

- レンダリングはヘッドレスブラウザ＋ffmpeg のローカル処理。GPU・API キーは不要。
- 出力形式は 9:16 / 1:1 / 16:9 を1本の素材から同時書き出し（`--formats`）。
- 参照画像からスタイルを作る場合、参照の権利は利用者責任。

## 最短手順

```bash
npm i -g playwright && npx playwright install chromium
# プラグインとして導入
/plugin install animate@animate
# または
SKILL=~/.claude/skills/animate
node $SKILL/tools/build.mjs pieces/my-piece
node $SKILL/tools/export.mjs pieces/my-piece --share --formats 9:16,1:1,16:9
```

## 変更履歴

- 2026-11-03: 初回登録（star 1,441 / pushed 2026-10-05 / MIT / Node 18+）
