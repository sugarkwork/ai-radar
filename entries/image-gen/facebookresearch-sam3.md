---
type: "repo"
name: "facebookresearch/sam3"
genre: "image-gen"
url: "https://github.com/facebookresearch/sam3"
author: "facebookresearch"
source_post: "https://x.com/L_ARCH_01/status/2119383964167409667"
sources: ["https://x.com/L_ARCH_01/status/2119383964167409667?a=zKpg53m3GHtXbyQgu6M&s=20", "https://x.com/L_ARCH_01/status/2119383964167409667", "https://github.com/facebookresearch/sam3", "https://github.com/facebookresearch/sam-3d-body", "https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE", "https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE", "https://huggingface.co/facebook/sam3.1", "https://huggingface.co/facebook/sam-3d-body-dinov3"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "独自SAM Licenseで標準MIT/Apacheではない。重みのmanual gateや利用条件を確認し、複数人モーションのデモを本体の実行試験としない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "facebookresearch/sam3"
license: "NOASSERTION"
language: "Python"
created: "2025-07-17"
updated: "2026-10-23"
stars: 12242
forks: 1854
open_issues: 378
commits_30d: 2
commits_90d: 11
commit_cadence: "monthly"
size_kb: 61937
archived: false
fetched_at: "2026-11-09T00:31:36.073396+00:00"
---

# facebookresearch/sam3

## 出来ること

画像/動画内の対象分離・追跡に関わるSAM3系公式実装。

## 目的・背景

紹介対象は `facebookresearch/sam3`。対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:36.073396+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

対応するSAM3.1等の重みを別途取得する。人体メッシュを出すsam-3d-bodyとは別の実装。

## 実行条件

独自SAM Licenseで標準MIT/Apacheではない。重みのmanual gateや利用条件を確認し、複数人モーションのデモを本体の実行試験としない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/facebookresearch/sam3#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @L_ARCH_01: https://x.com/L_ARCH_01/status/2119383964167409667
- 対象資料: https://github.com/facebookresearch/sam3
- 参照: https://github.com/facebookresearch/sam-3d-body
- 参照: https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE
- 参照: https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE
- 参照: https://huggingface.co/facebook/sam3.1
- 参照: https://huggingface.co/facebook/sam-3d-body-dinov3

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
