---
name: "three.quarks"
genre: "3d-motion"
url: "https://github.com/Alchemist0823/three.quarks"
flags: ["unverified"]
risk_notes: "GitHubの最新リリースと公開日は未確認。バッチ描画による描画呼び出し削減は作者の説明に基づき、削減量やフレームレートは未計測。Three.jsの対応バージョン範囲とAIエージェントとの連携動作も未検証。"
repo: "Alchemist0823/three.quarks"
stars: 1192
forks: 76
open_issues: 13
size_kb: 9601
language: "TypeScript"
created: "2019-06-16"
updated: "2026-05-21"
archived: false
license: "MIT"
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:56:09Z"
---

# three.quarks — Three.js向けパーティクルVFXライブラリ

## 出来ること

- 火や煙などのパーティクル効果をThree.jsのシーンに追加できる。ビルボード、メッシュ、軌跡の描画に対応し、粒子の寿命に沿って色やサイズを変えられる。
- エディターから書き出したVFXのJSONをQuarksLoaderで読み込める。

## 目的・背景

- ゲームやインタラクティブなWeb表現向けのリアルタイムVFXを扱う。作者は、複数のパーティクルシステムをまとめて描画し、描画呼び出しを抑える設計と説明している。

## 依存関係

- 公式導入ガイドではthree.quarksとthreeをnpmで導入する。React Three Fiber向けには別パッケージのquarks.r3fがある。

## 実行条件

- npmで導入する場合はNode.jsとnpmを用意し、Three.jsのシーンと描画ループに組み込む。リポジトリのライセンスはMIT。

## 最短手順

- 既存のThree.jsプロジェクトで `npm install three.quarks three` を実行する。
- READMEのQuick Startに沿ってBatchedRendererをシーンに追加し、ParticleSystemのエミッターをシーンに追加して、システムをBatchedRendererに登録する。描画前に毎フレーム `batchRenderer.update(delta)` を呼ぶ。
- コーディングエージェントを使う場合は、対象のThree.jsプロジェクトと公式READMEを渡し、既存の描画ループへ同じJavaScript APIの呼び出しを組み込むよう依頼する。

## 変更履歴

- 2026-11-10: 初回登録
