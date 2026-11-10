---
repo: "jrouwe/JoltPhysics"
name: "Jolt Physics"
genre: "3d-motion"
url: "https://github.com/jrouwe/JoltPhysics"
license: "MIT"
stars: 12261
language: "C++"
created: "2021-08-12"
updated: "2026-11-09"
forks: 1013
open_issues: 8
commits_30d: 49
commit_cadence: "daily"
commits_90d: 89
size_kb: 31832
archived: false
last_release: "v5.6.0"
flags: ["unverified"]
risk_notes: "リリースタグは公式の最新リリースページで確認したが、公開日時は未確認。ビルド、性能、AIツールとの連携は実行検証していない。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/okapi_fukugyo/status/2117616982518559161"]
fetched_at: "2026-11-10T09:55:54Z"
---

# Jolt Physics — 3Dシーンに衝突・剛体・軟体シミュレーションを組み込むC++ライブラリ

## 出来ること

- 球や箱などの剛体の衝突、関節でつないだラグドール、布などの軟体をシミュレートできる。

## 目的・背景

- ゲームやVR向けに設計され、公式READMEは衝突クエリを物理更新と並行して処理できると説明している。実世界の挙動には近似を使う。

## 依存関係

- ライブラリ本体はC++17と標準ライブラリを使用する。公式の組み込み例はCMake FetchContentを使う。MITライセンスで、再配布時は著作権表示と許諾文を保持する。

## 実行条件

- 公式READMEが挙げるコンパイラはVisual Studio 2022以降、Clang 16以降、GCC 12以降。x86/x64の最低要件はSSE2で、ビルド設定によって追加のCPU命令が必要になる。

## 最短手順

- 公式のHelloWorldで初期化と物理更新の流れを確認し、CMake FetchContent版の例に沿ってC++プロジェクトへ組み込む。AIから利用する場合は、生成したシーン情報をボディの形状・位置・種別に変換し、ホスト側からJoltのC++ APIを呼ぶ。まず静的な床と動的な球で落下と接触を確認する。

## 変更履歴

- 2026-11-10: 初回登録
