---
name: "@react-three/fiber"
genre: "3d-motion"
url: "https://github.com/pmndrs/react-three-fiber"
repo: "pmndrs/react-three-fiber"
license: "MIT"
stars: 33655
language: "TypeScript"
created: "2019-02-25"
updated: "2026-10-21"
forks: 2098
open_issues: 37
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 44
size_kb: 31505
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/thegreatest_sv/status/2118374136799985771"]
fetched_at: "2026-11-11T23:05:24.740159+00:00"
---

# @react-three/fiber

## 出来ること

- React renderer for Three.js. Reactの状態に反応する再利用可能なコンポーネントで3Dシーンを宣言的に構築でき、READMEの例ではCanvas上にメッシュを置き、フレームごとの回転やクリック・ポインター操作を実装しています。出典: https://github.com/pmndrs/react-three-fiber

## 目的・背景

- Three.jsの機能をReactのJSXで表現し、コンポーネントをReactのエコシステムに組み込むためのレンダラーです。READMEでは、JSXの`<mesh />`が`new THREE.Mesh()`に対応すると説明しています。出典: https://github.com/pmndrs/react-three-fiber

## 依存関係

- READMEの導入例は`three`、`@types/three`、`@react-three/fiber`をnpmでインストールします。Reactのメジャーバージョンとの対応は、fiber v8がReact 18、fiber v9がReact 19と記載されています。出典: https://github.com/pmndrs/react-three-fiber

## 実行条件

- READMEは利用前にReactとThree.jsの基礎知識を得ることを勧めています。React Nativeの例ではReact 18とExpo CLIを使用し、`useLoader`やDreiの`useGLTF`・`useTexture`でアセットを使う場合はMetro bundlerの設定が必要になることがあると記載されています。出典: https://github.com/pmndrs/react-three-fiber

## 最短手順

- README記載のインストール例: `npm install three @types/three @react-three/fiber`。Webの例では`Canvas`と`useFrame`を`@react-three/fiber`から読み込み、`<Canvas>`内にThree.js要素をJSXで記述します。出典: https://github.com/pmndrs/react-three-fiber

## 変更履歴

- 2026-11-11: 初回登録
