---
name: "Primitive Pictures"
genre: "image-gen"
url: "https://github.com/fogleman/primitive"
repo: "fogleman/primitive"
stars: 13594
forks: 671
open_issues: 55
size_kb: 2348
language: "Go"
created: "2016-09-13"
updated: "2024-07-22"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/awe0_io/status/2118741744045146377"]
fetched_at: "2026-11-14T00:14:10.193556+00:00"
---

# Primitive Pictures

## 出来ること

- 入力画像を三角形、矩形、楕円などの図形を一つずつ追加して再現します。PNG・JPG・SVG・GIFを出力でき、図形の種類や反復回数を指定できます。READMEでは、形状候補を評価し、対象画像との差を小さくするよう探索すると説明されています。

## 目的・背景

- 幾何学的な図形を重ねて、元画像を抽象的な画像として再構成するツールです。READMEによると、対象画像との差の評価にはRMSEを使い、形状の変更を試す hill climbing で次の図形を選びます。

## 依存関係

- コマンドライン利用にはGoのインストールが必要です。GIF出力にはImageMagickの`convert`コマンドが必要です。

## 実行条件

- 入力画像と出力ファイル名を指定します。READMEは小さな入力画像（例：256×256ピクセル）を推奨しています。出力サイズ、図形数、図形のモードなどをオプションで指定できます。

## 最短手順

- Goをインストールし、README記載の手順で取得します。

`go get -u github.com/fogleman/primitive`

入力画像からPNGを生成する例：

`primitive -i input.png -o output.png -n 100`

## 変更履歴

- 2026-11-14: 初回登録
