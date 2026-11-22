---
name: "ComfyUI-PhotoDeblur"
genre: "image-gen"
url: "https://github.com/porfeng/ComfyUI-PhotoDeblur"
repo: "porfeng/ComfyUI-PhotoDeblur"
stars: 93
forks: 5
open_issues: 0
size_kb: 3099
language: "Python"
created: "2026-11-07"
updated: "2026-11-07"
archived: false
license: "MIT"
commits_30d: 13
commits_90d: 13
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/wildmindai/status/2119174858881785942"]
fetched_at: "2026-11-17T08:23:58.897740+00:00"
---

# ComfyUI-PhotoDeblur

## 出来ること

- ComfyUIにHI-DiffとMISCFilterの写真デブラー用ノードを追加します。元画像の解像度を保つタイル処理、タイル間のブレンド、任意のTTAに対応し、公式モデル重みのダウンロードと検証を行うノードも含みます。READMEの例では看板や建物の輪郭、夜景の光跡などを示しています。

## 目的・背景

- カメラぶれや動体ぶれのある写真を、色調整やトリミングなど後続の編集前に処理する用途として説明されています。READMEは少数の写真での作者の主観的観察として、夜景の看板や一部の構造エッジに改善が見られた一方、夜の人物写真では結果にばらつきがあり、小さく強くぼけた顔などでは改善が限られた例もあると記しています。

## 依存関係

- README記載の導入要件はComfyUIのPython環境でのrequirements.txtおよびrequirements-download.txtのインストールです。NVIDIA/CUDA 12でMISCFilterを使う場合はrequirements-misc-cu12.txt、トーンマッチングを使う場合はOpenCVが必要です。

## 実行条件

- ComfyUIを再起動してから、ワークフローに画像ローダー、対応するモデルローダー、Deblur Image (Tiled)、Save Imageを接続します。READMEはsRGBのTIFF/PNG入力を案内し、RAWは現像してから読み込むよう説明しています。タイルサイズ768、オーバーラップ96、TTAオフを開始設定として提示しています。TTAは8方向の予測を平均し、モデル計算量がおよそ8倍になるとの説明があります。

## 最短手順

- リポジトリをComfyUI/custom_nodesに配置し、ComfyUIのPythonでrequirements.txtとrequirements-download.txtをインストールします。ComfyUIを再起動し、example_workflowsのワークフローをキャンバスに読み込みます。画像を選び、ダウンローダーとモデルローダーのモデル・variantを合わせて実行します。重みを既に配置している場合、ダウンロードノードは省略できます。

## 変更履歴

- 2026-11-22: 初回登録
