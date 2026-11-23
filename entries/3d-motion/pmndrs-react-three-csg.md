---
name: "react-three-csg"
genre: "3d-motion"
url: "https://github.com/pmndrs/react-three-csg"
repo: "pmndrs/react-three-csg"
license: "MIT"
language: "TypeScript"
created: "2022-07-19"
updated: "2025-03-02"
open_issues: 11
commit_cadence: "stale"
archived: false
stars: 372
forks: 17
size_kb: 3081
commits_30d: 0
commits_90d: 0
flags: ["unverified"]
risk_notes: "一次資料で未確認: 実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:11:21.727949+00:00"
---

# react-three-csg

## 出来ること

- Reactのコンポーネントでthree.jsのBufferGeometryに対するCSG操作を構成する。Baseを形状の基礎にし、Addition（追加）、Subtraction（減算）、ReverseSubtraction（逆減算）、Intersection（共通部分）、Difference（負の共通部分）を順に適用できる。操作の入れ子・グループ化・変形にも対応し、useGroupsで操作ごとのマテリアルグループを生成できる。showOperationsまたはshowOperationで操作形状を表示できる。

## 目的・背景

- READMEでは、three-bvh-csgを包むReact向けの小さな抽象化として説明されている。

## 依存関係

- READMEはthree-bvh-csgを基盤として挙げている。実行時の依存パッケージ一覧はこの資料から確認できない。

## 実行条件

- READMEの導入例は `yarn add @react-three/csg`。Reactやthree.jsの対応バージョンなど、詳細な実行条件はこの資料に記載されていない。

## 最短手順

- `yarn add @react-three/csg` で導入し、`Geometry`内に`Base`とCSG操作コンポーネントを置く。例では`Base`に`boxGeometry`を指定し、その後に`Addition`などを配置する。実行中に形状を再計算する場合は、メインのGeometryに対して`update()`を呼ぶ。READMEは複雑さに応じて頻繁な実行時更新を避ける場合があると説明している。

## 変更履歴

- 2026-11-23: 初回登録
