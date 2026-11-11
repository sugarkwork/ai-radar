---
name: "open-source-hands"
genre: "coding-agent"
url: "https://github.com/abouchedidxcode/open-source-hands"
repo: "abouchedidxcode/open-source-hands"
license: "MIT"
stars: 205
language: "TypeScript"
created: "2026-11-03"
updated: "2026-11-03"
forks: 30
open_issues: 1
commits_30d: 2
commit_cadence: "monthly"
commits_90d: 2
size_kb: 5838
archived: false
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-11"
first_seen: "2026-11-11"
sources: ["https://x.com/tokufxug/status/2118212439187804520"]
fetched_at: "2026-11-11T04:14:50.856077+00:00"
---

# open-source-hands

## 出来ること

- READMEによると、Google MediaPipe Hand Landmarkerの21点を使い、20種のポーズ、16種の動き、5種の両手ジェスチャー、およびピンチ強度や手の位置などの連続値をゲーム入力に変換するTypeScriptキットを提供する。三.js製のゲーム用テンプレート、Gesture Lab、デモ、サンプルゲームも含む。READMEは、映像は端末外へ送信されず、処理はブラウザー内で行われると説明している。

## 目的・背景

- READMEでは、ブラウザーで手を使うゲームを作るための技術基盤として説明されている。既存ゲームへのキット導入や、コーディングエージェントにテンプレートと制作ガイドを使わせる方法も示されている。

## 依存関係

- キットは依存関係なしのTypeScriptと説明されているが、手追跡にはGoogle MediaPipe Hand Landmarkerを使用する。既存プロジェクトへ導入する例では @mediapipe/tasks-vision@1.1.0、MediaPipeのモデルファイルおよびWASMファイルを配置する。ゲームテンプレートは三.jsを使用する。

## 実行条件

- README記載の手順ではNode.js/npmを使う。カメラ利用にはHTTPSまたはlocalhostが必要で、ブラウザーでカメラを開始するにはユーザー操作（クリック）が必要。カメラなしのテスト手段として合成手を使う方法も記載されている。

## 最短手順

- README記載のゲーム作成手順は、npx degit abouchedidxcode/open-source-hands/templates/game my-game、cd my-game、npm install、npm run dev。起動後はスターターのREADMEと制作ガイドを参照する。

## 変更履歴

- 2026-11-11: 初回登録
