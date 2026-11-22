---
name: "Babylon.js"
genre: "3d-motion"
url: "https://github.com/BabylonJS/Babylon.js"
repo: "BabylonJS/Babylon.js"
license: "Apache-2.0"
stars: 26380
language: "TypeScript"
created: "2013-06-27"
updated: "2026-11-16"
forks: 3739
open_issues: 22
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 1498005
archived: false
flags: ["unverified"]
risk_notes: "READMEのCDNは学習や小規模な実験向けで、本番環境では使用しないよう記載されている。READMEは実機での動作や対応環境の詳細を独立検証していない。"
type: "repo"
added: "2026-11-15"
first_seen: "2026-11-15"
sources: ["https://x.com/Feljoy_ix/status/2121787138455040333"]
fetched_at: "2026-11-16T21:32:05Z"
last_release: "9.37.0"
last_release_at: "2026-11-16"
---

# Babylon.js

## 出来ること

- READMEによると、Babylon.jsはブラウザーで3Dシーンを作成・描画するJavaScript/TypeScriptエンジン。Engine、Scene、FreeCamera、ライト、組み込みの球体・地面メッシュを使う例が掲載されている。また、PlaygroundでAPIを試せるほか、Sandboxで.babylonおよびglTFシーンを確認できる。出典: https://github.com/BabylonJS/Babylon.js

## 目的・背景

- 学習や実験向けのPlaygroundと、公式ドキュメント・デモを案内している。npmパッケージおよびES6パッケージの導入方法も示されている。出典: https://github.com/BabylonJS/Babylon.js

## 依存関係

- アプリでの利用手順としてnpm install babylonjs --saveを記載。開発・リポジトリへの貢献にはNode.js 22.22.2以降（Node 22系）、または24.16.0以降（Node 24系）、npm 11.18.0以降が必要とREADMEにある。これらは開発ツール要件で、公開ライブラリの実行要件とは別と明記されている。出典: https://github.com/BabylonJS/Babylon.js

## 実行条件

- READMEの使用例はブラウザーのcanvas要素を取得し、Babylon.jsのEngineとSceneを作成して描画ループを実行する。詳細なブラウザー・GPU対応条件はこのREADMEには記載されていない。出典: https://github.com/BabylonJS/Babylon.js

## 最短手順

- 1. npm install babylonjs --saveで導入する。2. babylonjsからEngine、Scene等をimportする。3. canvas要素をEngineに渡し、Scene、カメラ、ライト、メッシュを作成する。4. engine.runRenderLoopでscene.render()を呼び、resize時にengine.resize()を呼ぶ。READMEにはこの一連のコード例がある。出典: https://github.com/BabylonJS/Babylon.js

## 変更履歴

- 2026-11-15: 初回登録
