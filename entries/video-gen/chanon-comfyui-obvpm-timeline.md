---
repo: chanon/comfyui-obvpm-timeline
name: comfyui-obvpm-timeline
genre: video-gen
url: https://github.com/chanon/comfyui-obvpm-timeline
author: chanon
license: GPL-3.0
stars: 270
language: Python
created: 2026-09-03
updated: "2026-10-23"
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/ai_hakase_/status/2117856442866905109
sources:
  - https://comfyui-wiki.com/en/news/2026-09-21-obvpm-timeline
  - https://github.com/chanon/comfyui-obvpm
forks: 34
open_issues: 37
commits_30d: 5
commits_90d: 80
commit_cadence: "weekly"
size_kb: 1246
archived: false
fetched_at: "2026-11-09T21:44:18Z"
last_release: "v0.1.4"
last_release_at: "2026-10-13"
---

# comfyui-obvpm-timeline

## 出来ること

- **MiniMax H3 用の「タイムライン付きクリップ編集」ノード群**。生成したクリップをタイムラインに並べ、切る・繋ぐ・延ばす・間を埋めるを1つのUIで行う。タイムラインは簡易動画エディタとして動く。
- **Extend**（後ろへ延長）、**Prepend**（前を生成）、**Bridge**（2つのクリップの間を生成）、**Loop**（最後を最初に繋いでシームレスなループ）に対応。**Extend from a cut** で、出来の悪い末尾を切り落として良い部分から延長できる。
- 各テイクは MP4 と **`.mctx`（モーションコンテキスト）サイドカー**のペアで保存される。`.mctx` には生の映像・音声 latent とメタデータが入っており、続きは**再エンコードしたピクセルではなく元の latent から latent マスクで生成**する。継ぎ目で明るさが変わる・チラつくといった VAE 往復の劣化が起きない。ファイルはクリップの隣に残るので、数日後・数ヶ月後でも同じ品質で延長できる。
- **Snap cuts**: カットを latent のフレーム格子（17フレーム）に吸着させる。
- **Result preview**: 新しいクリップを隣接クリップと繋いだ状態で再生し、継ぎ目の滑らかさを評価してから採用／削除できる。**Live preview** はサンプリング中の絵を結果プレビューに出し、生成が破綻していないか早く判断できる。
- タイムライン全体を1本に書き出す **export** と、任意の**アップスケールパス**（latent upscaler）を内蔵。生成とアップスケールはグループ単位の Mute で切り替える。
- モーションコンテキストを持たない外部クリップも、ピクセルから再エンコードして延長できる（継ぎ目はピクセル級で、latent 級より劣化する）。

## 目的・背景

H3 は4〜15秒のクリップをネイティブステレオ音声付きで出せるが、長尺にするにはクリップを繋ぐ必要があり、従来の「最終フレームを画像で書き出して次の I2V に渡す」方式は VAE のデコード／エンコードを往復するたびに画質・服・顔が変わる。obvpm Timeline は**テイクの latent をそのまま保存して次の生成に渡す**ことで、この往復を無くす。作者は chanon（ChanonDevs）。2026-09-03 作成、10-23 時点で 255 star。Patreon 支援者には新機能・新ワークフローの先行アクセスがある。

## 依存関係

- **ComfyUI 0.35.0（2026-09-09）以降**（ワークフローの Model Optimization が core の `Model Sparse Attention` を使うため。docs/h3.md は 2026-08-13 以降と記載しており、README と表記が揃っていない）
- 追加の Python 依存は無し（torch / safetensors / av は ComfyUI 同梱）
- H3 Live Preview のデコード用に `models/vae_approx/taeh3.safetensors`（madebyollin の temporal 版、Kijai の 2D 版のいずれか）。無い場合は latent の色で粗く表示される
- 同梱ワークフローが使うカスタムノード:
  - `comfyui-obvpm` **0.2.16 以降**（Bundles / Settings Presets / スイッチ / Compatibility Check）
  - `ComfyUI-KJNodes`（Set/Get、Sage attention パッチ）
  - `Comfyui_Minimax_h3_latent_Upscaler`（アップスケール用。**Plus フォークではなくオリジナル**）
  - `ComfyUI-MiniMax-H3-Turbo`（larryvrh turbo の LoRA ローダー）
  - `ComfyUI-Spectrum-MiniMax-H3`（Spectrum 加速）
  - `rgthree-comfy`（Power Lora Loader）
- MiniMax H3 の重み・テキストエンコーダ・VAE（ワークフローのプリセットは int8 の ref2va 系など）

## 実行条件

- **クリップの解像度は揃える必要がある**。latent はリサイズできないため、サイズの違うクリップはタイムラインが受け付けない。
- 生成は 0.4〜0.6 メガピクセルの短いクリップで素材を作り、Extend / Bridge で繋いでから最後に export、アップスケールは後段でも可（配布スレッドの推奨手順）。
- **既知の競合**: `Comfyui_Minimax_h3_latent_Upscaler` の Plus フォークは同じ node id・名前で widget 構成が違い、保存済みワークフローの設定が1つずつずれる。`kat3ri/ComfyUI-MiniMax-H3-Extend` は import 時に core の関数（`MiniMaxH3.extra_conds` と `PackedLayout.__init__`）を置き換え、denoise マスクが落ちる。どちらも併用しない。
- アップスケールを伴う実行では、latent upscaler の temporal chunking を有効にしておく必要がある。切った状態の実行はサンプリング開始前に拒否される。
- ノード名はすべて `(obvpm)` 接尾辞付き。ノードメニューで `obvpm` と検索すると一覧が出る。
- `.mctx` を消したクリップ、インポートした動画、他ワークフローの出力は latent が無いため、ピクセル経由のフォールバックになる（継ぎ目は exact ではない）。

## 最短手順

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/chanon/comfyui-obvpm-timeline
# ComfyUI を再起動し、workflows/h3_obvpm_timeline_r2v_v0.1.4-007A.json を開く
# （comfyui-obvpm 0.2.16+ / このパック 0.1.4+ が必要）
```

```text
基本の流れ:
1. 通常の H3 ワークフローの終端を「H3 MCtx Trim and Save Video」に変えてルートテイクを保存
2. H3 MCtx Load で create_pins=extend (pin tail) → Apply Pins → サンプリング
3. 出来を Result Preview で確認してタイムラインへ追加
4. 全クリップを揃えて export（必要ならアップスケール）
```

## 変更履歴

- 2026-11-04: 初回登録（0.1.4 / ワークフロー 007A 時点）、H3 Live Preview 用の tiny VAE とアップスケール時の temporal chunking 必須を追記（v0.1.4）
