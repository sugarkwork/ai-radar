---
type: "repo"
repo: "jtydhr88/ComfyUI-InstantHMR"
name: "ComfyUI-InstantHMR — 写真・動画・ライブ人物モーション推定"
genre: "3d-motion"
url: "https://github.com/jtydhr88/ComfyUI-InstantHMR"
author: "jtydhr88"
license: "Apache-2.0"
language: "JavaScript"
stars: 52
forks: 10
open_issues: 0
created: "2026-11-07"
updated: "2026-11-08"
commits_30d: 19
commits_90d: 19
commit_cadence: "weekly"
size_kb: 711
archived: false
risk_notes: "コードはApache-2.0だが重みはSAM License。nano/tiny/small/mediumは追加で非商用限定。商用用途はmedium_commercialを選びSAM条件を確認する。投稿の約2.5ms/人・40fps超は作者の報告で測定条件やエンドツーエンド性能を当方は再現していない。 当方でインストール・動作・性能の実行検証はしていない。"
sources: ["https://x.com/jtydhr88/status/2119464947864207559", "https://github.com/jtydhr88/ComfyUI-InstantHMR", "https://github.com/jtydhr88/ComfyUI-InstantHMR/blob/main/README.md", "https://github.com/jtydhr88/ComfyUI-InstantHMR/blob/main/LICENSE"]
added: "2026-11-09"
first_seen: "2026-11-08"
source_post: "https://x.com/jtydhr88/status/2119464947864207559"
fetched_at: "2026-11-09T21:31:07Z"
flags: ["unverified"]
last_release: "v1.1.0"
last_release_at: "2026-11-08"
---

# ComfyUI-InstantHMR — 写真・動画・ライブ人物モーション推定

## 出来ること

写真・動画・Webカメラ・同一LANのスマホ映像から人物ごとの3D姿勢、体形、70点の2D/3DキーポイントとMHRメッシュを推定する。MHR_POSE_DATAをComfyUI標準のSAM 3D Body平滑化・描画・アニメ書き出しノードへ渡す。ライブビューのキャラクター駆動と、先頭人物のVMC送信を備える。

## 目的・背景

InstantHMRの20–32Mパラメータ級モデルをComfyUIから使う非公式統合。SAM 3D Bodyと同じMHR表現を出すため既存処理へ接続できる。v1.1.0のパッケージ定義を確認。

## 依存関係

ComfyUIのネイティブ3DノードとInstantHMRチェックポイント。複数人物にはRT-DETRのperson検出またはSAM3追跡を接続する。描画スタイルbody_mesh/bones_onlyとBVHはSAM 3D Body loaderが必要。顔表情の補助にはMediaPipeと別ノードを使う。

## 実行条件

重みはmodels/detectionへ配置。ブラウザのカメラはlocalhostまたはHTTPSが必要で、スマホは同一ネットワークとHTTPSが前提。ネットワーク推定の時間と、検出・追跡・描画・通信を含むFPSを分けて考える。

## 最短手順

公式READMEに従ってノードと用途に合う重みを導入し、example_workflows/instanthmr_image.json、instanthmr_video.json、instanthmr_live.jsonを選ぶ。複数人動画ではSAM3追跡で人物indexを維持する。ライブ設定はmodel・detector・cameraを選んでStart。

## 注意点

コードはApache-2.0だが重みはSAM License。nano/tiny/small/mediumは追加で非商用限定。商用用途はmedium_commercialを選びSAM条件を確認する。投稿の約2.5ms/人・40fps超は作者の報告で測定条件やエンドツーエンド性能を当方は再現していない。

## 変更履歴

- 2026-11-09: 初回収録。公式資料を確認し、未実行の範囲を明記。
