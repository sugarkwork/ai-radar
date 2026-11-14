---
name: "React Three Rapier"
genre: "3d-motion"
url: "https://github.com/pmndrs/react-three-rapier"
repo: "pmndrs/react-three-rapier"
license: "MIT"
stars: 1613
language: "TypeScript"
created: "2022-04-30"
updated: "2026-10-12"
forks: 106
open_issues: 55
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 2355
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/thegreatest_sv/status/2118724335905148990"]
fetched_at: "2026-11-13T21:14:36.468889+00:00"
---

# React Three Rapier

## 出来ること

- Rapier の WASM 物理エンジンを react-three/fiber のシーンに組み込み、剛体、形状コライダー、衝突イベント、センサー、ジョイントを扱えます。メッシュ形状に基づく自動コライダー生成や、インスタンスごとの剛体作成にも対応するとREADMEに記載されています。

## 目的・背景

- Rapier を react-three/fiber のパイプラインに組み込みやすくするラッパーとして説明されています。READMEは、高速な物理エンジンと簡潔なAPIを目標として掲げています。

## 依存関係

- READMEが示す利用環境は React、react-three/fiber、Rapier の WASM 物理エンジンです。例では @react-three/drei も使われています。react-three/rapier v2 は react-three/fiber v9 と React v19 に対応し、React v18 の場合は v1 と react-three/fiber v8 が必要と記載されています。

## 実行条件

- READMEによると、<Physics /> は <Suspense /> でラップする必要があります。Rapier は遅延初期化されます。

## 最短手順

- @react-three/rapier から Physics、RigidBody、必要な Collider を読み込み、Canvas 内で <Suspense><Physics>…</Physics></Suspense> を構成します。物理対象のメッシュを <RigidBody> で囲み、必要に応じて Collider を追加します。公式READMEの基本例では、Torus を剛体として配置し、CuboidCollider を床として配置しています。

## 変更履歴

- 2026-11-14: 初回登録
