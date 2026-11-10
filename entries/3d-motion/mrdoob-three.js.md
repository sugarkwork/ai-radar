---
repo: "mrdoob/three.js"
name: "Three.js"
genre: "3d-motion"
url: "https://github.com/mrdoob/three.js"
license: "MIT"
stars: 118014
forks: 36937
open_issues: 412
size_kb: 1702728
language: "JavaScript"
created: "2010-03-23"
updated: "2026-11-10"
archived: false
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
flags: ["unverified"]
risk_notes: "最新リリースのタグと公開日時、端末別の描画性能、投稿で言及されたAIとの連携は未確認。描画例は公式資料で確認し、この精査でコードは実行していない。コミット件数は各期間100件で打ち止め。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:54:27+00:00"
---

# Three.jsでブラウザ上の3Dシーンとカメラワークを試作する

## 出来ること

- メッシュを配置した3Dシーンをブラウザで描画し、カメラの位置や向きを変えて構図と動きを確認できる。公式チュートリアルには回転する立方体の例がある。

## 目的・背景

- Three.jsはシーン、カメラ、レンダラーを組み合わせてWeb向けの3D表現を実装するJavaScriptライブラリ。AIにシーン用のJavaScriptを書かせる場合も、まず小さな描画例で構図と動きを確認できる。

## 依存関係

- npmで導入する場合はNode.js環境で `three` を追加し、開発サーバーにViteを使える。公式マニュアルにはCDNからモジュールを読み込む方法もある。
- ライブラリ本体はMITライセンス。取り込むモデルやテクスチャには各素材の利用条件が適用される。

## 実行条件

- 公式の最小例で使う `WebGLRenderer` には、WebGL 2を利用できるブラウザ環境が必要。

## 最短手順

- 公式の Installation に沿って `npm install three` と `npm install -D vite` で導入し、HTMLからJavaScriptをモジュールとして読み込む。
- Creating a scene の例に沿って `Scene`、`PerspectiveCamera`、`WebGLRenderer` と立方体を用意し、`npx vite` で表示する。
- AIコーディング支援を使う場合は、この最小例をベースに、開始と終了のカメラ位置、注視点、移動時間を指定してJavaScriptの差分を作らせる。ブラウザで立方体が表示され、カメラが指定した方向に動くことを確認する。

## 変更履歴

- 2026-11-10: 初回登録
