---
repo: nomadoor/ComfyUI-Panorama-Stickers
name: ComfyUI Panorama Stickers
genre: video-gen
url: https://github.com/nomadoor/ComfyUI-Panorama-Stickers
author: nomadoor（@noma_door）
license: MIT
stars: 182
language: JavaScript
created: 2026-03-01
updated: "2026-11-05"
added: 2026-11-04
first_seen: 2026-11-03
source_post: https://x.com/noma_door/status/2117646383863972084
sources: []
forks: 17
open_issues: 1
commits_30d: 84
commits_90d: 93
commit_cadence: "daily"
size_kb: 16331
archived: false
fetched_at: "2026-11-09T21:46:04Z"
last_release: ""
last_release_at: ""
---

# ComfyUI Panorama Stickers

## 出来ること

- 360°パノラマの中に画像・動画・3Dを配置し、任意の視点から撮影する ComfyUI ノード群。撮った一部を画像生成モデルで修正し、**元の位置に戻す**往復をワークフロー内で完結できる。
- 中核の **Panorama Studio** はパノラマを「遠景（Sky）」、3Dを「奥行きのある空間（World）」として同時に扱う。Sky に貼ったものはカメラが動いても同じ方向に留まり、World に置いたものはカメラ位置で見え方が変わる。
- 入力は `background`（パノラマ画像/動画）、`world`（メッシュ / ガウシアンスプラット / MoGe 等で推定した形状）、`sticker`（画像・動画・3D。エディタへのドロップでも可）、`scene`（別 Studio のシーン引き継ぎ）。
- エディタでステッカーとカメラを**タイムラインのキーフレーム**で動かし、マスクを描き、カメラで撮影する。出力はパノラマ（360°/180°）または通常カメラ視点（Frame）。
- 主な用途: 画像を貼ってパノラマを作り、パノラマ LoRA 系の生成モデルに周囲を埋めさせる／パノラマの一部を Frame で切り出して修正し、`sticker_state` と一緒に次の Studio に渡して元の位置へ戻す／画像・動画を別角度から撮り直す／そのまま動画にする。
- 補助ノード: **Panorama Preview**（パノラマ画像・動画・Studio の `scene` を別ウィンドウで見回す）、**Panorama Seam Prep**（左右の継ぎ目を中央へ移動し、修正用マスクを作る）。旧ノード（Panorama Stickers / Cutout / Preview legacy）も従来どおり動作。
- 2.0 系で Studio と新 Preview が入り、3D（メッシュ・ガウシアンスプラット・MoGe/DA3 の深度グリッド）とタイムライン編集に対応。2.0.3 では上流 Studio から渡ったオブジェクトの選択・編集（オーバーライド保存）、`sticker_state` で戻したショットが常に Sky に戻る修正、ペイントの回転、軌道中心マークと緯度経度グリッドなどが追加された。
- **2.1.0**: Studio のビューで Alt+ホイール／トラックパッドのピンチにより画角（FOV）を変えられ、数値表示とリセットボタンが付く。Studio は常に新しいエディタで開くようになり、旧設定はなくなった。タイムラインではボックスの範囲選択ができる。

## 目的・背景

nomadoor による個人プロジェクト。単眼画像から 3D を起こすと別角度で隙間だらけになるため、その隙間を画像編集モデルや MiniMax H3 などで自然に埋める、という使い方を作者が想定している。2026-03-01 作成、11-04 時点で 179 star。

## 依存関係

- ComfyUI **0.35.0 以降**
- パノラマ生成にはパノラマ LoRA 対応の生成モデル、3D 入力には MoGe / DA3 などの深度・形状推定、または自分で用意したメッシュ／ガウシアンスプラット
- 画像編集での往復には、マスク編集に対応した画像編集モデル

## 実行条件

- レンダリングは WebGL。ブラウザ側でエディタを操作するため、ComfyUI のフロントエンドが動く環境が必要。
- 3D の読み込み形式・サイズは ComfyUI 側の 3D ノード群に依存する（README に個別の上限記載は無し）。
- 動画を扱う場合、入力動画の長さ・解像度は VRAM と生成モデル側の制約に従う。

## 最短手順

```text
ComfyUI Manager → "Panorama Stickers" を検索してインストール → ComfyUI 再起動
```

```text
ワークフロー例:
background(パノラマ) + world(MoGe等) + sticker(画像/動画/3D) → Panorama Studio
  → Camera=Frame で修正箇所を撮影 → 画像編集モデル → sticker_state と共に次の Studio へ
```

## 変更履歴

- 2026-11-04: 初回登録（2.0.3、3D・タイムライン対応時点）
- 2026-11-06: 2.1.0 — 画角（FOV）のズーム操作とリセット、Studio が新エディタで開く変更、タイムラインの範囲選択を追記（36f5eb0）
