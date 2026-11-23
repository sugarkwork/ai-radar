---
name: "math"
genre: "other"
url: "https://github.com/pmndrs/math"
repo: "pmndrs/math"
stars: 1345
forks: 50
open_issues: 16
size_kb: 21727
language: "TypeScript"
created: "2021-10-29"
updated: "2026-11-16"
archived: false
license: "MIT"
commits_30d: 9
commits_90d: 100
commit_cadence: "weekly"
flags: ["unverified"]
risk_notes: "一次資料で未確認: 技術背景・有効性・依存関係・実行条件。"
type: "repo"
added: "2026-11-23"
first_seen: "2026-11-23"
sources: ["https://x.com/0xclayo/status/2123016316353155192"]
fetched_at: "2026-11-18T14:12:40.205749+00:00"
---

# math

## 出来ること

- ベクトル・クォータニオン・行列、図形と空間クエリ、幾何アルゴリズム、アニメーション用のイージングとスプリング、シード付き乱数、ノイズ、色変換、逆運動学のAPIを提供する。READMEでは、呼び出し側が用意した配列に結果を書き込むデータ指向の関数として説明されている。

## 目的・背景

- READMEは、Web向けの数学エンジンとして紹介し、WebGL・WebGPU・Wasmや各種レンダラーとの相互運用を掲げている。性能や小ささに関する説明は配布者の主張であり、ここでは独立した計測結果として扱わない。

## 依存関係

- READMEに記載された依存関係の情報は確認できない。

## 実行条件

- JavaScript/TypeScriptの利用例とnpmによる導入手順がREADMEにある。対応ランタイムやバージョン要件はREADMEから確認できない。

## 最短手順

- `npm install math`で導入する。例では`import { type Vec3, vec3 } from 'math'`として読み込み、`vec3.create()`で出力配列を作り、`vec3.add(out, a, b)`で結果を書き込む。用途別のサブパスとして`math/noise`、`math/random`、`math/time`、`math/ik`なども記載されている。

## 変更履歴

- 2026-11-23: 初回登録
