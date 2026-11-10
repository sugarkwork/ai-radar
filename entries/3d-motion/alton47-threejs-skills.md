---
repo: "alton47/threejs-skills"
name: "Three.js AI Skills"
genre: "3d-motion"
url: "https://github.com/alton47/threejs-skills"
license: "MIT"
stars: 18
forks: 6
open_issues: 1
size_kb: 96
language: "unknown"
created: "2026-03-24"
updated: "2026-03-25"
archived: false
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
flags: ["unverified"]
risk_notes: "エージェント別の導入とスキル読込、生成コードの動作、スキル有無による品質差、対応バージョンは未検証。閲覧した公開リリース一覧には掲載がなかったが、最新リリースのAPI確認は未実施。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/CryptooGG_/status/2119312343892976064"]
fetched_at: "2026-11-10T12:11:00+00:00"
---

# Three.js AI Skills — AIエージェント向けのThree.js実装ガイド

## 出来ること

- ブラウザー向け3Dシーンの実装時に、レンダラー、カメラ、照明、GLTF読み込み、GLSLシェーダー、描画負荷の計測などのガイドを参照できる。

## 目的・背景

- Three.jsの実装知識を用途別のAgent Skillsとして配布する。READMEにはシーン初期化のコード例がある。生成品質の改善は実測していない。

## 依存関係

- CLIで導入する場合はnpxを使う。READMEの基本例はthreeパッケージと、そのアドオンのOrbitControlsを参照する。Reactや物理演算のスキルでは用途に応じた追加ライブラリが挙げられている。

## 実行条件

- スキルを読み込めるエージェント環境と、生成したWebGLコードを動かすブラウザー環境を用意する。リポジトリはMITライセンス。利用するエージェントの料金は未確認。

## 最短手順

- READMEの手順に沿って、利用環境で npx skills add https://github.com/alton47/threejs-skills を使って導入する。
- 導入先のエージェントに『threejs-coreを参照して、回転する立方体を表示するThree.jsシーンを作って』と依頼し、生成コードをブラウザーで確認する。

## 変更履歴

- 2026-11-10: 初回登録
