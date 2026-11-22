---
repo: "lightseekorg/tokenspeed"
name: "TokenSpeed"
genre: "model-serving"
url: "https://github.com/lightseekorg/tokenspeed"
license: "MIT"
stars: 2930
language: "Python"
created: "2026-05-06"
updated: "2026-11-16"
forks: 416
open_issues: 93
commits_30d: 100
commit_cadence: "daily"
commits_90d: 100
size_kb: 63101
archived: false
flags: ["unverified"]
risk_notes: "コミット数は集計上限100。性能は開発元測定で、起動と追試は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/bernvadell/status/2110318450082017517"]
fetched_at: "2026-11-16T21:56:45Z"
last_release: "v0.1.1"
last_release_at: "2026-10-06"
---

# TokenSpeed

## 出来ること

- モデルをGPUで動かしOpenAI互換APIで提供する。

## 目的・背景

- 長いコンテキストと多ターンの推論処理を最適化する。

## 依存関係

- Python実行系、C++スケジューラ、バックエンド別カーネル。

## 実行条件

- 公式ガイドではCUDA 13または対応ROCm環境。nightly wheelはPython 3.11–3.13。

## 最短手順

- 公式Getting Startedに沿って対応GPU環境に導入し、サーバーを起動してOpenAI互換クライアントを接続する。 https://lightseek.org/tokenspeed/guides/getting-started

## 変更履歴

- 2026-11-10: 初回登録
