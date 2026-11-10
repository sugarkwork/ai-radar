---
repo: "cocopon/tweakpane"
name: "Tweakpane"
genre: "3d-motion"
url: "https://github.com/cocopon/tweakpane"
license: "MIT"
stars: 4669
language: "TypeScript"
created: "2016-05-10"
updated: "2026-03-15"
forks: 134
open_issues: 32
commits_30d: 0
commit_cadence: "stale"
commits_90d: 0
size_kb: 4397
archived: false
last_release: "4.0.5"
flags: ["unverified"]
risk_notes: "機能と手順は公式の記述とサンプルで確認した。実行検証、制作時間への効果、特定の描画ライブラリとの互換性、最新リリースの公開日時は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/RealMarvelX/status/2117956876369264741"]
fetched_at: "2026-11-10T11:08:18Z"
---

# Tweakpaneでブラウザー上のモーションを調整する

## 出来ること

- 数値や色を操作パネルにバインドし、速度や色などの調整値を変更できる。読み取り専用バインドで値の変化を監視でき、パネルの状態は exportState() で書き出せる。

## 目的・背景

- dat.GUI に着想を得たパラメーター調整用 GUI。モーション制作では、既存の描画処理が参照する値を画面上で調整する用途に使える。

## 依存関係

- README は実行時依存なしと説明している。公式の導入手順では、TypeScript 開発時に型定義用の @tweakpane/core を開発依存として追加する。ライセンスは MIT。

## 実行条件

- v4 は ES Modules を使う。ブラウザーでは type=module のスクリプトから読み込める。npm 経由で組み込む場合は tweakpane から Pane を import する。

## 最短手順

- 既存のブラウザー向けアニメーションに npm install --save tweakpane で追加し、Pane を import して new Pane() でパネルを作る。
- 速度を保持する params オブジェクトを用意し、pane.addBinding(params, 'speed', {min: 0, max: 3, step: 0.1}) でスライダーを追加する。描画ループで params.speed を参照する。
- コーディングエージェントで組み込む場合は、公式 Quick tour と既存の描画ループを示し、Pane API で速度のバインドを追加するよう依頼する。ブラウザーでスライダーを動かし、描画速度に反映されるか確認する。

## 変更履歴

- 2026-11-10: 初回登録
