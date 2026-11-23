---
name: "Spark"
genre: "3d-motion"
url: "https://github.com/sparkjsdev/spark"
repo: "sparkjsdev/spark"
license: "MIT"
stars: 3938
language: "TypeScript"
created: "2025-05-23"
updated: "2026-11-19"
forks: 595
open_issues: 115
commits_30d: 8
commit_cadence: "weekly"
commits_90d: 100
size_kb: 105010
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・依存関係。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xCarrera/status/2123762450935771202"]
fetched_at: "2026-11-22T04:46:42.393928+00:00"
---

# Spark

## 出来ること

- READMEによると、THREE.jsの描画パイプラインに統合し、スプラットとメッシュを組み合わせて描画できます。PLY、SPZ、SPLAT、KSPLAT、SOGなど主要形式の読込み、複数スプラットのソート描画、複数視点の同時描画、スプラットの変形・編集・アニメーション、色編集や変位、スケルタルアニメーション、GPU上でスプラットを編集するシェーダーグラフに対応すると説明されています。

## 目的・背景

- World Labsが開発する、THREE.js向けの3D Gaussian Splattingレンダラーです。

## 依存関係

- READMEのローカルビルド手順ではRustをインストールし、npm install、npm run build:wasm、npm run buildを実行します。npmパッケージとしてはnpm install @sparkjsdev/sparkで導入できます。

## 実行条件

- READMEにはWebGL2対応を対象デバイスの98%以上とする記載があります。ローカルでサンプルを動かす場合はビルド後にnpm startを実行します。サンプルはリモートURLから素材を取得し、任意でnpm run assets:downloadにより素材をダウンロードしてキャッシュできます。

対応言語: 不明（確認資料に明記なし）。
日本語対応: 不明（確認資料に明記なし）。

## 最短手順

- READMEの例では、Three.jsとSparkのモジュールをimportmapで読み込み、SparkRendererを作成してシーンに追加し、SplatMeshにスプラットのURLを指定して描画します。CDNを使う場合はREADME記載のimportmapを設定します。npm利用の場合はnpm install @sparkjsdev/sparkで導入します。

## 変更履歴

- 2026-11-23: 初回登録
