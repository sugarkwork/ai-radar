---
name: "Ultralytics YOLO26とSAHIによるスライス推論ガイド"
genre: "article"
url: "https://docs.ultralytics.com/guides/sahi-tiled-inference"
published: "2023-11-12"
flags: ["unverified"]
risk_notes: "このガイドのSAHI連携は非推奨です。Ultralyticsは学習・検証・予測で標準のtile引数を使うよう案内しています。掲載された小物体検出やメモリ使用に関する効果は公式資料の説明であり、特定データや環境での独立検証結果ではありません。"
type: "article"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/tokufxug/status/2118896163554488397"]
fetched_at: "2026-11-14T22:11:05.313244+00:00"
---

# Ultralytics YOLO26とSAHIによるスライス推論ガイド

## テーマ

- Ultralytics YOLO26とSAHI（Slicing Aided Hyper Inference）を使い、高解像度画像を分割して物体検出する方法を説明する公式ガイドです。

## 著者の主張

- ガイドでは、画像を小領域に分けて推論し、検出位置を元画像へ戻すスライス推論を説明しています。小物体が画像全体の縮小後に検出しにくくなる場合に役立ち、領域ごとの処理で大画像のメモリ負荷を抑えられるとしています。SAHIのget_sliced_prediction例では、slice_heightとslice_width、重なり率を指定します。

## 裏取り・注意点

- ページはSAHI連携ガイドを非推奨とし、Ultralytics標準のtile引数を案内しています。標準機能ではtile=Trueがimgszを窓サイズに使い、正の整数で窓サイズを個別指定できます。重なり率や窓サイズは対象物の大きさに合わせた調整が必要です。ガイドの効果説明は公式資料の記述であり、ここで独立実測した結果ではありません。

## 出典

- Ultralytics公式ガイド「Using YOLO26 with SAHI for Sliced Inference」: https://docs.ultralytics.com/guides/sahi-tiled-inference
Ultralytics公式「High Resolution Tiling with Ultralytics YOLO」: https://docs.ultralytics.com/guides/high-resolution-tiling

## 変更履歴

- 2026-11-14: 初回登録
