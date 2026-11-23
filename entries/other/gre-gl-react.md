---
name: "gl-react"
genre: "other"
url: "https://github.com/gre/gl-react"
repo: "gre/gl-react"
license: "MIT"
stars: 3016
language: "TypeScript"
created: "2015-08-17"
updated: "2026-11-17"
forks: 162
open_issues: 21
commits_30d: 39
commit_cadence: "daily"
commits_90d: 93
size_kb: 136471
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 有効性・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:13:43.208943+00:00"
---

# gl-react

## 出来ること

- ReactコンポーネントとしてWebGLシェーダーを記述・合成し、画像・動画（gl-react-dom）・canvas（gl-react-dom）などのテクスチャを扱えます。JavaScriptからGLSLのuniformへ値をバインドできます。

## 目的・背景

- READMEでは、低レベルで命令的・可変なOpenGL APIを、Reactの宣言的・不変な記述方法で扱うライブラリとして説明されています。

## 依存関係

- 利用先に合わせた具体的な実装との組み合わせが必要です。READMEにはReact DOM向けのgl-react-dom、React Native向けのgl-react-nativeまたはgl-react-expo、Node.js向けのgl-react-headlessが挙げられています。

## 実行条件

- React DOM、React Native、またはNode.jsで利用する場合、それぞれ対応する実装を選びます。READMEのVite向け注意事項では、typedarray-poolがNode.jsのglobalを参照するため、vite.config.jsでglobalをglobalThisに定義する設定例が示されています。

## 最短手順

- gl-reactからShaders、Node、GLSLを読み込み、Shaders.createでフラグメントシェーダーを定義します。利用環境に対応した実装からSurfaceを読み込み、その内側にNodeを描画するReactコンポーネントを配置します。READMEの例では、Surfaceに幅・高さを指定してシェーダーを表示しています。

## 変更履歴

- 2026-11-23: 初回登録
