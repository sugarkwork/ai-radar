---
name: "flubber"
genre: "other"
url: "https://github.com/veltman/flubber"
repo: "veltman/flubber"
stars: 6966
forks: 171
open_issues: 19
size_kb: 241
language: "JavaScript"
created: "2017-06-09"
updated: "2022-11-08"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/RealMarvelX/status/2118330503040221345"]
fetched_at: "2026-11-11T20:08:22.531588+00:00"
---

# flubber

## 出来ること

- SVGパス文字列または[x, y]点列を入力に、形状間の補間関数を作成する。円・矩形への変形、単一形状と複数形状の分割・結合、複数形状同士の補間、点列からSVGパス文字列への変換などのAPIがある。READMEによれば、補間は「best-guess」であり、穴や複数形状を含むパス文字列では最初の外側形状以外は無視される。

## 目的・背景

- 形状同士の座標やパスの対応が十分でない場合に起こりうる、予測しにくい反転や急な変化を避け、任意の形状間で比較的滑らかなアニメーションを作ることを目的としている。READMEは効果をbest-guessと説明しており、あらゆる形状での結果を保証していない。

## 依存関係

- READMEにはD3を使う例と、D3を使わずrequestAnimationFrameで描画する例がある。D3は例で使用されるが、必須依存とは記載されていない。

## 実行条件

- ブラウザではREADME記載のunpkgスクリプトを読み込んでflubberグローバルを利用できる。npm install flubberで導入し、CommonJSまたはES6 importで利用する方法も記載されている。入力形状はSVGパス文字列または[x, y]点列。

## 最短手順

- npm install flubberで導入し、flubber.interpolate(fromShape, toShape)で補間関数を作成する。関数に0から1の値を渡して中間形状を得て、SVG要素のd属性などに反映する。READMEではD3のtransitionとattrTweenを使う例、およびrequestAnimationFrameで更新する例を示している。

## 変更履歴

- 2026-11-11: 初回登録
