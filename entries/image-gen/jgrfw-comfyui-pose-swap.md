---
repo: JGRFW/comfyui-aicg3d-PoseSwap
name: ComfyUI AICG3D PoseSwap
genre: image-gen
url: https://github.com/JGRFW/comfyui-aicg3d-PoseSwap
license: MIT
stars: 330
language: HTML
created: 2026-10-30
updated: "2026-11-01"
added: 2026-11-05
first_seen: 2026-11-05
source_post: https://x.com/servasyy_ai/status/2118524399582371985
sources: []
flags: []
risk_notes: "同梱の約4,300枚の参照画像（頭・ポーズ・衣装）は第三者図庫由来で、コードのMITとは別の利用条件がある。画像を含めた再配布・商用利用は不可。"
forks: 47
open_issues: 1
commits_30d: 7
commits_90d: 7
commit_cadence: "weekly"
size_kb: 385305
archived: false
fetched_at: "2026-11-09T21:38:16Z"
last_release: ""
last_release_at: ""
---

# ComfyUI AICG3D PoseSwap

## 出来ること

- ComfyUI で**顔・ポーズ・衣装を個別に差し替える**ワークフロー。3つの参照図庫（**1,499 頭部 / 1,439 ポーズ / 1,407 衣装**）を内蔵し、クリックで参照画像をノードに流し込める。
- 処理は「頭 → ポーズ → 衣装」の3段構成で、**それぞれ独立したスイッチ**を持つ。ポーズだけ変えたいときはポーズ段だけオンにできる。
- 画像編集モデルは Qwen Image 2.1。頭部は BF16 で精度重視、衣装は INT8 量子化版で速度重視（1段20秒台）。テキストエンコーダは Qwen3-VL 8B、ポーズ段には PoseStudio V1.1 LoRA を併用。
- 図庫はノードに直結しており、正面・横顔・髪型での絞り込み、ポーズ・衣装のカテゴリ検索ができる。
- 単項置換と3段フル流程のワークフローJSONを同梱。

## 目的・背景

漫画のコマ割り、ショートドラマのキャラクター定盤など、同じ顔・体型・衣装で**姿勢だけを変えた絵**を繰り返し作る作業を1本のフローにまとめる。すべてを1つのプロンプトに詰め込む方式ではなく、参照画像を段ごとに分けて渡す設計。

## 依存関係

- ComfyUI。Qwen Image 2.1（BF16 / INT8）、Qwen3-VL 8B、PoseStudio V1.1 LoRA のモデルファイルが必要。
- リポジトリサイズは約385MB（画像図庫を含むため）。

## 実行条件

- **図庫の権利**: コードは MIT だが、約4,300枚の画像は第三者図庫由来で別ライセンス。**画像込みの再配布・商用利用は不可**、自分で使う範囲に留める。
- 衣装替えでは色差が出ることがある。既定20ステップを上げると改善するが、完全には消えない。独立スイッチは「他の要素が絶対に変わらない」保証ではない（局部リドロー）。
- ★148・2026-10-30 公開。ワークフローは同梱JSONを読み込んでモデルを割り当てる。

## 最短手順

```text
1. ComfyUI/custom_nodes にリポジトリを配置
2. 同梱のワークフローJSON（単項 or 3段フル）を読み込む
3. Qwen Image 2.1（BF16/INT8）、Qwen3-VL 8B、PoseStudio LoRA を割り当て
4. 図庫から顔・ポーズ・衣装を選択し、必要な段のスイッチだけオン
5. 生成（衣装段は20ステップ以上を推奨）
```

## 変更履歴

- 2026-11-05: 初回登録（★148 / pushed 2026-11-01 / MIT / 図庫は別ライセンス）
