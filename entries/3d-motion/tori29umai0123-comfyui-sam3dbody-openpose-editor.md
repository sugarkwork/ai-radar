---
name: "ComfyUI-SAM3DBody-openpose-editor"
genre: "3d-motion"
url: "https://github.com/tori29umai0123/ComfyUI-SAM3DBody-openpose-editor"
repo: "tori29umai0123/ComfyUI-SAM3DBody-openpose-editor"
license: "GPL-3.0"
stars: 30
language: "Python"
created: "2026-11-06"
updated: "2026-11-07"
forks: 5
open_issues: 0
commits_30d: 16
commit_cadence: "weekly"
commits_90d: 16
size_kb: 51596
archived: false
flags: ["unverified"]
risk_notes: "READMEでは必要モデルを初回使用時に自動ダウンロードすると説明しているが、モデルの配布条件・料金はREADMEから確認できない。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/tori29umai/status/2118716616267743545"]
fetched_at: "2026-11-13T20:15:17.228402+00:00"
---

# ComfyUI-SAM3DBody-openpose-editor

## 出来ること

- ComfyUIのAnalyzeノードで画像の人物姿勢を推定し、OpenPose互換のpose_keypointとbody_shape_keypointを出力する。動画フレームの解析・追跡と、参照画像に基づく人物ごとの体型比率調整にも対応するとREADMEに記載されている。RenderノードでOpenPose画像を生成できる。

## 目的・背景

- SAM 3D Bodyによる姿勢推定結果をOpenPose互換データとして利用し、参照画像の体型比率を反映した画像・動画ワークフローを構成するためのComfyUIカスタムノード。

## 依存関係

- ComfyUIのネイティブSAM 3.1動画トラッカーを利用する。READMEでは、SAM3DBody用モデル2点とSAM 3.1用モデル1点をComfyUIのモデルディレクトリから読み込み、未配置なら自動ダウンロードすると説明している。個別のPython依存パッケージ一覧は添付READMEに記載がない。

## 実行条件

- ComfyUI上で利用する。動画解析では動画ローダーから順序付きIMAGEフレームバッチを接続し、出力フレームから動画を作る場合は別途動画保存ノードを使う。READMEによると、SAM 3.1が人物を検出できない場合はAnalyzeがエラーを返す。GPUやモデルの具体的な要件は添付READMEから確認できない。

## 最短手順

- README記載のworkflows/sam3d_body_openpose_example.jsonをComfyUIで読み込み、Load Imageで画像を選び、Analyze→Render→Save Imageのワークフローを実行する。体型参照を使う場合はLoad ImageをAnalyzeのbody_shape_imagesへ接続する。

## 変更履歴

- 2026-11-14: 初回登録
