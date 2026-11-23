---
name: "three-mesh-bvh"
genre: "other"
url: "https://github.com/gkjohnson/three-mesh-bvh"
repo: "gkjohnson/three-mesh-bvh"
license: "MIT"
stars: 3576
language: "JavaScript"
created: "2018-01-19"
updated: "2026-11-18"
forks: 352
open_issues: 100
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 158554
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 依存関係・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:11:53.272129+00:00"
---

# three-mesh-bvh

## 出来ること

- three.jsのメッシュでBounding Volume Hierarchy（BVH）を使い、レイキャストを高速化し、空間クエリを実行する。READMEにはポイント、ライン、スキンメッシュ、シーン全体のBVH、シリアライズ、非同期生成などの例がある。READMEの例では、80,000ポリゴンのモデルに500本のレイを60fpsでキャストすると説明しているが、これはREADME記載の主張であり、独立した実測ではない。

## 目的・背景

- three.jsのジオメトリに対するレイキャストや空間クエリをBVHで扱うためのライブラリ。

## 依存関係

- READMEの使用例ではthree.jsをimportしている。その他の依存関係は添付READMEから確認できない。

## 実行条件

- READMEにはWebWorkerによる非同期生成の例がある。WebWorker構文はバンドラーによって対応状況が異なり、対応しない場合もあると記載されている。

## 最短手順

- READMEの例に従い、three-mesh-bvhからcomputeBoundsTree、disposeBoundsTree、acceleratedRaycastをimportして、THREE.BufferGeometry.prototype.computeBoundsTreeとTHREE.Mesh.prototype.raycastに割り当てる。ジオメトリでcomputeBoundsTree()を呼び出した後、RaycasterでintersectObjects()を実行する。

## 変更履歴

- 2026-11-23: 初回登録
