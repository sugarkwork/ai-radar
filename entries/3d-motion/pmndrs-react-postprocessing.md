---
name: "react-postprocessing"
genre: "3d-motion"
url: "https://github.com/pmndrs/react-postprocessing"
repo: "pmndrs/react-postprocessing"
stars: 1589
forks: 164
open_issues: 12
size_kb: 16933
language: "TypeScript"
created: "2020-05-07"
updated: "2026-10-21"
archived: false
license: "MIT"
commits_30d: 7
commits_90d: 64
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-14"
first_seen: "2026-11-14"
sources: ["https://x.com/thegreatest_sv/status/2118724335905148990"]
fetched_at: "2026-11-13T21:14:13.076162+00:00"
---

# react-postprocessing

## 出来ること

- React Three Fiber 向けの postprocessing ラッパー。READMEにはBloom、DepthOfField、Noise、VignetteをEffectComposer内で組み合わせる例がある。READMEは、複雑なエフェクトのオーケストレーションを目的としたものではないと説明している。
出典: https://github.com/pmndrs/react-postprocessing

## 目的・背景

- READMEによると、単純なエフェクトチェーンを少ないコードで構成できる。利用するpostprocessingライブラリについては、EffectPassがエフェクトの組み合わせを整理・統合してレンダー操作を減らせること、全画面処理に単一三角形を使うことを紹介している。これらはREADMEに引用されたpostprocessing側の説明であり、独立した実測結果ではない。
出典: https://github.com/pmndrs/react-postprocessing
引用元としてREADMEに記載: https://github.com/pmndrs/postprocessing#performance

## 依存関係

- READMEはpostprocessingと@react-three/fiberのラッパーと説明し、利用例では@react-three/postprocessingと@react-three/fiberをimportしている。依存パッケージの網羅的な一覧やバージョン条件は、このREADME抜粋では確認できない。
出典: https://github.com/pmndrs/react-postprocessing

## 実行条件

- READMEにはnpm install @react-three/postprocessingによる導入例と、React Three FiberのCanvas内にEffectComposerと各種エフェクトを配置する例がある。READMEはWebGL2 MSAAがデフォルトであると記載しているが、詳細な対応環境・バージョン条件はこの資料では確認できない。
出典: https://github.com/pmndrs/react-postprocessing

## 最短手順

- 1. npm install @react-three/postprocessing
2. React Three FiberのCanvas内にEffectComposerを置き、BloomやNoiseなどのエフェクトを子要素として追加する。
README掲載のコード例では、EffectComposer内にDepthOfField、Bloom、Noise、Vignetteを指定している。
出典: https://github.com/pmndrs/react-postprocessing

## 変更履歴

- 2026-11-14: 初回登録
