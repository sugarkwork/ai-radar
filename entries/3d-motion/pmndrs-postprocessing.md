---
name: "Post Processing"
genre: "3d-motion"
repo: "pmndrs/postprocessing"
url: "https://github.com/pmndrs/postprocessing"
last_release: "v6.39.6"
flags: ["unverified"]
risk_notes: ["実機での描画、GPU別の性能差、発見投稿が紹介したAI制作フロー全体は未検証。"]
stars: 2963
forks: 258
open_issues: 30
size_kb: 262336
language: "JavaScript"
created: "2015-12-08"
updated: "2026-11-01"
archived: false
license: "Zlib"
commits_30d: 6
commits_90d: 22
commit_cadence: "weekly"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117956876369264741"]
fetched_at: "2026-11-10T11:07:00+00:00"
---

# Post ProcessingでThree.jsの描画にブルームと被写界深度を加える

## 出来ること

- 描画済みのシーンにブルーム、被写界深度、色補正などの全画面エフェクトを適用できる。

## 目的・背景

- EffectComposerが描画パスを管理し、RenderPassで描画したシーンにEffectPassで効果を適用する。READMEでは、効果をまとめて描画処理の回数を抑える設計と説明している。

## 依存関係

- Three.jsがピア依存。v6.39.6の対応範囲は0.168.0以上、0.188.0未満。ライブラリはZlibライセンス。

## 実行条件

- WebGLが利用できるブラウザと、Three.jsのレンダラー、シーン、カメラが必要。READMEでは、暗部のバンディングや高輝度のクリッピングを避けたい場合にHalfFloatTypeの中間バッファを案内している。

## 最短手順

- 既存のThree.jsプロジェクトにnpm install three postprocessingで導入し、threeが対応範囲内か確認する。
- 既存のWebGLRendererからEffectComposerを作り、RenderPass(scene, camera)、EffectPass(camera, new BloomEffect())の順に追加する。
- アニメーションループでcomposer.render()を呼ぶ。コーディングエージェントを使う場合は、既存の描画ループをこの構成に変更するよう依頼できる。

## 変更履歴

- 2026-11-10: 初回登録
