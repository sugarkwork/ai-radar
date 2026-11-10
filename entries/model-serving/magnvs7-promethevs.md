---
type: "repo"
name: "Magnvs7/Promethevs"
genre: "model-serving"
url: "https://github.com/Magnvs7/Promethevs"
author: "Magnvs7"
source_post: "https://x.com/mapte_fireball/status/2118865992319377535"
sources: ["https://x.com/mapte_fireball/status/2118865992319377535?a=sy4m7maB0McU87OyILM&s=46", "https://x.com/mapte_fireball/status/2118865992319377535", "https://github.com/Magnvs7/Promethevs", "https://raw.githubusercontent.com/Magnvs7/Promethevs/main/README.md", "https://raw.githubusercontent.com/Magnvs7/Promethevs/main/RESULTS.md", "https://raw.githubusercontent.com/Magnvs7/Promethevs/main/engine-0.2/INSTALL.md"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "最良7.4tok/sと一致率98.33%は限定した作者試験。原本完全一致デコードは別の約2.14tok/s。エンジンApacheと報告・図表CC BYを区別する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "Magnvs7/Promethevs"
license: "CC-BY-4.0"
language: "unknown"
created: "2026-10-21"
updated: "2026-11-09"
stars: 161
forks: 10
open_issues: 9
commits_30d: 16
commits_90d: 16
commit_cadence: "weekly"
size_kb: 3474
archived: false
fetched_at: "2026-11-09T21:40:06Z"
license_detail: "原チェックのLICENSE/README解釈: Apache-2.0 (engine); CC-BY-4.0 (reports)。APIのSPDX判定とは別。利用前に現行本文を確認。"
last_release: "v0.2"
last_release_at: "2026-10-23"
---

# Magnvs7/Promethevs

## 出来ること

巨大MoEを圧縮して計算し、曖昧なトークンだけ原本重みで補正するcompress-then-correct推論エンジン。

## 目的・背景

紹介対象は `Magnvs7/Promethevs`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:38.138686+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Windows10/11、AVX2、RTX30/40系12GB、driver580+、約1.09TBの空き容量という作者要件。OpenAI互換APIを案内。

## 実行条件

最良7.4tok/sと一致率98.33%は限定した作者試験。原本完全一致デコードは別の約2.14tok/s。エンジンApacheと報告・図表CC BYを区別する。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/Magnvs7/Promethevs#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @mapte_fireball: https://x.com/mapte_fireball/status/2118865992319377535
- 対象資料: https://github.com/Magnvs7/Promethevs
- 参照: https://raw.githubusercontent.com/Magnvs7/Promethevs/main/README.md
- 参照: https://raw.githubusercontent.com/Magnvs7/Promethevs/main/RESULTS.md
- 参照: https://raw.githubusercontent.com/Magnvs7/Promethevs/main/engine-0.2/INSTALL.md

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
