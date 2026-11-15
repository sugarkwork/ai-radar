---
name: "gifenc"
genre: "image-gen"
url: "https://github.com/mattdesl/gifenc"
repo: "mattdesl/gifenc"
license: "MIT"
stars: 357
language: "JavaScript"
created: "2021-02-23"
updated: "2024-09-19"
forks: 29
open_issues: 11
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 1971
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-15T03:20:11.851899+00:00"
---

# gifenc

## 出来ること

- RGBAピクセルデータを色数削減し、パレットインデックスへ変換してGIFを作成する。静止画・アニメーション、透明度、フレームごとの設定に対応するとREADMEに記載。ブラウザーとNode.jsで利用可能。

## 目的・背景

- READMEでは、GIF.jsより低レベルなライブラリーだが、多くの画像で同等の見た目を保ちながら高速に動作すると作者が説明している。ディザリングには対応しておらず、写真や動画より単純なフラット調のベクター画像に適するとしている。速度や画質は独立検証値ではない。

## 依存関係

- READMEに実行時依存関係の一覧はない。

## 実行条件

- ブラウザーまたはNode.js（ESMおよびCommonJS）で利用可能とREADMEに記載。

## 最短手順

- READMEの例では、RGBAデータにquantize(data, 256)を適用し、applyPaletteで各ピクセルをインデックス化する。GIFEncoder()でストリームを作成し、writeFrame(index, width, height, { palette })、finish()の順に呼び出してbytes()からUint8Arrayを取得する。

## 変更履歴

- 2026-11-15: 初回登録
