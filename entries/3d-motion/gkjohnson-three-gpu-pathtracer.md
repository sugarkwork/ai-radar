---
repo: "gkjohnson/three-gpu-pathtracer"
name: "three-gpu-pathtracer"
genre: "3d-motion"
url: "https://github.com/gkjohnson/three-gpu-pathtracer"
license: "MIT"
flags: ["unverified"]
risk_notes: ["GitHub の最新リリースは未確認。依存関係と導入手順は main ブランチの公開資料に基づく。", "描画速度、収束時間、画質、端末別の互換性、特定のAIモデルとの連携は実測していない。"]
stars: 2037
forks: 200
open_issues: 58
size_kb: 955374
language: "JavaScript"
created: "2021-11-03"
updated: "2026-11-10"
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:55:26+00:00"
---

# three-gpu-pathtracer — Three.js のシーンを WebGPU でパストレーシング

## 出来ること

- 既存の Three.js シーンとカメラを使い、物理ベースの材質、面光源、被写界深度を含むシーンを描画できる。

## 目的・背景

- three-mesh-bvh と WebGPU のコンピュートシェーダーを使い、サンプルを積み重ねて画像を描画する。公式 README では、環境マップを事前にぼかすと収束が早まる場合がある一方、反射の鮮明さが失われると説明している。

## 依存関係

- main の package.json にあるピア依存は three >=0.187.0、three-mesh-bvh >=0.9.18、xatlas-web ^0.1.0。リポジトリのコードは MIT ライセンス。

## 実行条件

- README の基本例には WebGPU が必要。対応するメッシュ材質は MeshStandardMaterial と MeshPhysicalMaterial。スポットライト、平行光源、点光源を使うには多重重点サンプリング（MIS）が必要。

## 最短手順

- Three.js プロジェクトに `npm install three-gpu-pathtracer` で追加し、導入するバージョンのピア依存を確認する。
- `three/webgpu` の `WebGPURenderer` を初期化し、`three-gpu-pathtracer/webgpu` の `WebGPUPathTracer` に渡す。`setScene(scene, camera)` で既存のシーンを登録し、描画ループで `renderSample()` を呼ぶ。
- AIコーディングエージェントに組み込みを任せる場合は、公式 API 文書と既存のシーン初期化コードを渡し、上記の初期化とサンプル描画を実装するよう依頼する。呼び出しは生成・編集された JavaScript から行う。 https://gkjohnson.github.io/tools/docs/three-gpu-pathtracer/webgpu/WebGPUPathTracer/

## 変更履歴

- 2026-11-10: 初回登録
