---
repo: "deepseek-ai/DeepInfer"
name: "DeepInfer"
genre: "model-serving"
url: "https://github.com/deepseek-ai/DeepInfer"
license: "Apache-2.0"
stars: 25757
language: "Python"
created: "2026-10-16"
updated: "2026-11-03"
forks: 3161
open_issues: 247
commits_30d: 6
commit_cadence: "weekly"
commits_90d: 6
size_kb: 3212
archived: false
flags: ["unverified"]
risk_notes: "公開版はオフライン推論用。起動と公表性能の再現は未確認。"
type: "repo"
added: "2026-11-10"
first_seen: "2026-11-10"
sources: ["https://x.com/bernvadell/status/2112534880819290613"]
fetched_at: "2026-11-10T04:14:00.414Z"
---

# DeepInfer

## 出来ること

- DeepSeek-V4.1-Flashをオフラインで推論し、構造化出力などを扱う。

## 目的・背景

- AttentionとMoEの並列処理や非同期スケジューリングを使う。公開版には完全な推論サービスに必要な一部機能が含まれない。

## 依存関係

- TileLang、Transformers、xgrammar、ハードウェアに応じたPyTorch。

## 実行条件

- Linux、GCC 13以上、Python 3.12。NVIDIA SM100とCUDA 13、またはAscend 950とCANN 9.2。

## 最短手順

- 公式READMEの対象ハードウェア別のビルド手順とオフライン実行例を参照する。

## 変更履歴

- 2026-11-10: 初回登録
