---
name: "vork"
genre: "3d-motion"
url: "https://github.com/voyager-so/vork"
repo: "voyager-so/vork"
license: "unknown"
flags: ["unverified"]
risk_notes: "READMEは「source-available」「research preview期間中は無料」と説明していますが、ライセンスの種類は確認できません。README記載の速度比較は作者による報告で、独立実測ではありません。 GitHub APIでライセンスを確認できていません。"
stars: 1611
forks: 134
open_issues: 5
size_kb: 28448
language: "Rust"
created: "2026-11-05"
updated: "2026-11-17"
archived: false
commits_30d: 14
commits_90d: 14
commit_cadence: "weekly"
type: "repo"
added: "2026-11-22"
first_seen: "2026-11-22"
sources: ["https://x.com/RoundtableSpace/status/2119207016069738968"]
fetched_at: "2026-11-17T11:11:43.832261+00:00"
---

# vork

## 出来ること

- AIエージェントがシーンをコードで記述し、GPUで3D/VFXをレンダリングするエンジン。READMEによると、シーンプログラムでマテリアル、カメラ、光の伝播、シミュレーション、コンポジットを定義できる。

## 目的・背景

- READMEは、エージェントがシーンを作成し、レンダリング結果を見てコードを直すワークフローを説明しています。エージェントが拡張できる小さなAPIを掲げています。

## 依存関係

- READMEによると、RustとSlangで実装され、VulkanおよびMetalを通じてGPUレンダリングを行います。

## 実行条件

- README記載のネイティブ対応OSはLinux、Windows、macOSです。クラウドGPUサービス「vork cloud」でのレンダリングも案内されています。初期化用のスターターシーンはダウンロード不要で、GPUなしで初期化できるとREADMEにあります。

## 最短手順

- README記載の手順：`vork init my-shot && cd my-shot`、`vork skills add`、`vork render scene.json --out render.png`。生成された`render.png`を確認し、`scene.json`の色やカメラ位置を変更して再レンダリングします。

## 変更履歴

- 2026-11-22: 初回登録
