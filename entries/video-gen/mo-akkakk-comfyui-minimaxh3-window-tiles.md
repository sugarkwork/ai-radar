---
repo: mo-akkakk/ComfyUI-MiniMaxH3-TemporalWindow-SpatialTiles
name: MiniMax H3 Temporal Window & Spatial Tiles
genre: video-gen
url: https://github.com/mo-akkakk/ComfyUI-MiniMaxH3-TemporalWindow-SpatialTiles
license: MIT
stars: 24
language: Python
created: 2026-10-25
updated: 2026-11-05
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/superfang119/status/2118332751975989486
sources:
  - https://registry.comfy.org/publishers/mo-akkakk
flags: []
risk_notes: ""
forks: 4
open_issues: 0
commits_30d: 19
commits_90d: 19
commit_cadence: weekly
size_kb: 495
archived: false
fetched_at: "2026-11-05T21:45:40Z"
---

# MiniMax H3 Temporal Window & Spatial Tiles

## 出来ること

- ComfyUI の MiniMax-H3 で**長尺・大画面を回すための1ノード**。モデルの外側で、時間方向と空間方向に分割してネイティブにサンプリングし、継ぎ目をブレンドする。
- **スライディング時間窓**: H3 の 17k+5 フレーム格子に合わせて窓を切り、前の窓の尾フレームを次窓のガイドにする。窓内は H3 が追従できる長さに保つので、長尺でも参照から外れにくい。
- **空間タイル**: 大画面をタイルに分けて個別にサンプリングし、羽根（feather）ブレンドで結合。1パス目の全デノイズにも、2パス目の高解像度リファインにも使える。
- モデル内部を書き換えない外側ラッパー。`KSampler` と `SamplerCustomAdvanced` の両方に対応し、窓とタイルを切ればネイティブ出力と一致する（単体テストあり）。
- 1.0.7 で `tile_carry` が追加され、タイルごとに「自分の未ブレンドフレーム」から次窓を続けられるようになった（ドリフト低減）。`blended` にすると 1.0.6 の挙動。
- `color_match`（タイル間・窓間の色ズレ補正）、`short_final_window`（最後の窓を短いまま使う）、`tile_audio`（音声の扱い）などのスイッチを持つ。

## 目的・背景

ローカルで H3 の長尺を作るとき、制約になるのは VRAM より「尺」で、窓を伸ばすほど参照映像から漂移してディテールが崩れる。このノードは「H3 が正確に追従できる長さの窓に切る」「タイルは参照映像にアンカーする」という前提で、外側から分割と結合だけを担う。

## 依存関係

- ComfyUI **v0.35.0 以上**（H3 ネイティブ対応版）。追加依存はなし。
- 2段構成の v2v（参照映像あり）が前提。純粋なテキストからの生成には向かない（タイルのアンカー先がない）。

## 実行条件

- **CLIP をこのノードに通す必要がある**。通さないと各窓が全尺の記述を読んでしまい、時間方向にズレる。
- 空や壁のような平面では、タイル境界にわずかな色差が残ることがある（README に明記）。`tile_overlap` を増やすか `color_match` を有効にする。
- ★24 / created 2026-10-25。10日で 1.0.0 → 1.0.7 まで進んだ新しいノードで、GitHub のリリース表記はなく README の changelog が正。

## 最短手順

```text
1. ComfyUI を v0.35.0 以降に更新
2. ノードを導入（ComfyUI Manager で "Temporal Window" / Registry の mo-akkakk から）
3. H3 のモデル → CLIP をこのノードに通す → 窓・タイルの設定 → guider/sampler
4. 参照映像（プレート）を接続し、窓とタイルを有効化してサンプリング
```

## 変更履歴

- 2026-11-05: 初回登録（★24 / pushed 2026-11-05 / MIT / README 1.0.7）
