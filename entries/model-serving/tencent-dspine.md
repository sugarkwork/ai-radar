---
type: "repo"
name: "Tencent/DSpine"
genre: "model-serving"
url: "https://github.com/Tencent/DSpine"
author: "Tencent"
source_post: "https://x.com/NFT_Chen/status/2119393299987648936"
sources: ["https://x.com/NFT_Chen/status/2119393299987648936", "https://github.com/Tencent/DSpine"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "READMEのApacheバッジに対し原チェックのLICENSEは404・API NOASSERTION。許諾を確定せずライセンス本文と依存を確認する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "Tencent/DSpine"
license: "NOASSERTION"
language: "Python"
created: "2026-10-15"
updated: "2026-11-08"
stars: 88
forks: 7
open_issues: 2
commits_30d: 6
commits_90d: 6
commit_cadence: "weekly"
size_kb: 852
archived: false
fetched_at: "2026-11-09T00:31:37.628476+00:00"
license_detail: "原チェックのLICENSE/README解釈: unknown (README Apache-2.0 badge; LICENSE not confirmed)。APIのSPDX判定とは別。利用前に現行本文を確認。"
---

# Tencent/DSpine

## 出来ること

DSpineの投機的デコード実装。Qwen3.8-27B等のドラフト重みと対応する。

## 目的・背景

紹介対象は `Tencent/DSpine`。対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:37.628476+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

SGLang0.5.22、対象モデルとGPU推論環境が必要。codeと重みは別配布。

## 実行条件

READMEのApacheバッジに対し原チェックのLICENSEは404・API NOASSERTION。許諾を確定せずライセンス本文と依存を確認する。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/Tencent/DSpine#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @NFT_Chen: https://x.com/NFT_Chen/status/2119393299987648936
- 対象資料: https://github.com/Tencent/DSpine

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
