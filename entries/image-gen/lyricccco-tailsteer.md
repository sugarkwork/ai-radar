---
type: "repo"
name: "Lyricccco/tailsteer"
genre: "image-gen"
url: "https://github.com/Lyricccco/tailsteer"
author: "Lyricccco"
source_post: "https://x.com/cutetoxicguy/status/2118878604574499107"
sources: ["https://x.com/cutetoxicguy/status/2118878604574499107?a=rqNNifMzvaFQgAUBeho&s=46", "https://x.com/cutetoxicguy/status/2118878604574499107", "https://github.com/Lyricccco/tailsteer", "https://api.github.com/repos/Lyricccco/tailsteer", "https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md", "https://arxiv.org/abs/2611.06741", "https://huggingface.co/api/models?search=tailsteer", "https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source", "https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "主な保持定量評価は10ターン。編集精度RISEが低下した値も公開され、保持と指示追従の両方が一律に向上したわけではない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "Lyricccco/tailsteer"
license: "Apache-2.0"
language: "Python"
created: "2026-11-06"
updated: "2026-11-09"
stars: 49
forks: 1
open_issues: 0
commits_30d: 11
commits_90d: 11
commit_cadence: "weekly"
size_kb: 248600
archived: false
fetched_at: "2026-11-09T21:38:19Z"
last_release: ""
last_release_at: ""
---

# Lyricccco/tailsteer

## 出来ること

反復画像編集で未編集領域の保持を改善するTailSteerの学習コード。軌跡の早期は元モデルに近づけ、末尾で保持補正を学ぶ。

## 目的・背景

紹介対象は `Lyricccco/tailsteer`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:46.400658+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

編集モデル自身のon-policy rolloutと未編集領域を参照する。対応重みへ差し替えれば推論時の追加アダプタ不要とREADMEは説明。

## 実行条件

主な保持定量評価は10ターン。編集精度RISEが低下した値も公開され、保持と指示追従の両方が一律に向上したわけではない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/Lyricccco/tailsteer#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @cutetoxicguy: https://x.com/cutetoxicguy/status/2118878604574499107
- 対象資料: https://github.com/Lyricccco/tailsteer
- 参照: https://api.github.com/repos/Lyricccco/tailsteer
- 参照: https://raw.githubusercontent.com/Lyricccco/tailsteer/main/README.md
- 参照: https://arxiv.org/abs/2611.06741
- 参照: https://huggingface.co/api/datasets/Lyricccco/TailSteer-Source
- 参照: https://huggingface.co/api/datasets/Lyricccco/Add-and-Preserve

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
