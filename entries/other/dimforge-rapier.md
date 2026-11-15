---
name: "Rapier"
genre: "other"
url: "https://github.com/dimforge/rapier"
repo: "dimforge/rapier"
stars: 6074
forks: 439
open_issues: 105
size_kb: 83368
language: "Rust"
created: "2020-08-25"
updated: "2026-11-01"
archived: false
license: "Apache-2.0"
commits_30d: 0
commits_90d: 17
commit_cadence: "monthly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Y0urDumble/status/2121980122743861421"]
fetched_at: "2026-11-15T15:21:34.741429+00:00"
---

# Rapier

## 出来ること

- ゲーム、アニメーション、ロボティクス向けの2D・3D物理エンジンを提供する。Rust向けのcrateとしてrapier2d、rapier3d、rapier2d-f64、rapier3d-f64がある。READMEでは、SIMDによる制約ソルバーと接触処理、および`parallel`機能による物理ステップのマルチスレッド化を説明している。

## 目的・背景

- Rustで利用できる2D・3D物理エンジン群。C、JavaScript、Python向けバインディングとBevyプラグインも案内されている。

## 依存関係

- READMEは`parallel`機能がrayonを通じたマルチスレッド処理を使うと説明している。その他の依存関係は添付READMEから確認できない。

## 実行条件

- Rust利用時の例として、`rapier3d = { version = "*", features = ["parallel"] }`を示している。Pythonバインディングは3Dエンジンを32-bit floatでラップし、2Dおよびf64のPythonバインディングはないとREADMEに記載されている。

## 最短手順

- 公式READMEは、ユーザーガイドを読み、`cargo run --release --bin all_examples2`または`cargo run --release --bin all_examples3`で例を試す手順を案内している。

## 変更履歴

- 2026-11-15: 初回登録
