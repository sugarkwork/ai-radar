---
type: "repo"
name: "shinyobjectz/raea"
genre: "video-gen"
url: "https://github.com/shinyobjectz/raea"
author: "shinyobjectz"
source_post: "https://x.com/awe0_io/status/2119067896978739412"
sources: ["https://x.com/awe0_io/status/2119067896978739412?a=czcGZB2A5B9cL6yTNqk&s=46", "https://x.com/awe0_io/status/2119067896978739412", "https://github.com/shinyobjectz/raea", "https://raea.io"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "canaryで日々の破壊的変更、Windowsは特に未検証と作者が注意。FSL-1.1-ALv2は競合利用制限があり2年後Apache移行、通常のApache OSSとは異なる。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "shinyobjectz/raea"
license: "NOASSERTION"
language: "Rust"
created: "2026-10-18"
updated: "2026-11-09"
stars: 1512
forks: 105
open_issues: 12
commits_30d: 100
commits_90d: 100
commit_cadence: "daily"
size_kb: 90679
archived: false
fetched_at: "2026-11-09T21:46:27Z"
license_detail: "原チェックのLICENSE/README解釈: FSL-1.1-ALv2。APIのSPDX判定とは別。利用前に現行本文を確認。"
last_release: "v0.1.0"
last_release_at: "2026-11-09"
---

# shinyobjectz/raea

## 出来ること

React/TypeScriptから動画・モーション・3D・小ゲームを書き、Bevy0.20/wgpuでローカルGPUレンダーするraea。

## 目的・背景

紹介対象は `shinyobjectz/raea`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:13.707269+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

CLIにrender/play/check/cut/init、切れ文字・コントラスト・ラウドネス等の検査とエージェント向けskillsを同梱。

## 実行条件

canaryで日々の破壊的変更、Windowsは特に未検証と作者が注意。FSL-1.1-ALv2は競合利用制限があり2年後Apache移行、通常のApache OSSとは異なる。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/shinyobjectz/raea#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @awe0_io: https://x.com/awe0_io/status/2119067896978739412
- 対象資料: https://github.com/shinyobjectz/raea
- 参照: https://raea.io

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
