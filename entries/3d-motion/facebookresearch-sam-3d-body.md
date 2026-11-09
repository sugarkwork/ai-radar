---
type: "repo"
name: "facebookresearch/sam-3d-body"
genre: "3d-motion"
url: "https://github.com/facebookresearch/sam-3d-body"
author: "facebookresearch"
source_post: "https://x.com/LidaMidorin/status/2118996429163450822"
sources: ["https://x.com/lidamidorin/status/2118996429163450822?a=62XkeJF-pXiiS-fxjH4&s=46", "https://x.com/LidaMidorin/status/2118996429163450822", "https://github.com/toyxyz/toyxyz_RGBMocap", "https://github.com/toyxyz/toyxyz_RGBMocap/blob/main/THIRD_PARTY_NOTICES.md", "https://github.com/zju3dv/GVHMR/blob/main/LICENSE", "https://github.com/twehrbein/ExMR/blob/main/LICENSE", "https://github.com/flowhmr/flowhmr", "https://huggingface.co/fafsaf1/flowhmr-0.46B", "https://github.com/facebookresearch/sam-3d-body", "https://x.com/L_ARCH_01/status/2119383964167409667?a=zKpg53m3GHtXbyQgu6M&s=20", "https://x.com/L_ARCH_01/status/2119383964167409667", "https://github.com/facebookresearch/sam3", "https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE", "https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE", "https://huggingface.co/facebook/sam3.1", "https://huggingface.co/facebook/sam-3d-body-dinov3"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "独自SAM LicenseはMIT/Apacheではなく用途・再配布・法令・プライバシー等に条件。非商用専用と断定する根拠はない。人体動画の同意と権利を確認する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "facebookresearch/sam-3d-body"
license: "NOASSERTION"
language: "Python"
created: "2025-07-29"
updated: "2026-02-19"
stars: 3698
forks: 437
open_issues: 76
commits_30d: 0
commits_90d: 0
commit_cadence: "stale"
size_kb: 22833
archived: false
fetched_at: "2026-11-09T00:31:04.097785+00:00"
---

# facebookresearch/sam-3d-body

## 出来ること

一枚の画像から体・手・足を含む3D人体メッシュを推定するSAM 3D Bodyの公式実装。

## 目的・背景

紹介対象は `facebookresearch/sam-3d-body`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:04.097785+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

MHRとfacebook/sam-3d-body-dinov3等の指定重み。配布重みは手動承認ゲートがある。

## 実行条件

独自SAM LicenseはMIT/Apacheではなく用途・再配布・法令・プライバシー等に条件。非商用専用と断定する根拠はない。人体動画の同意と権利を確認する。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/facebookresearch/sam-3d-body#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @LidaMidorin: https://x.com/LidaMidorin/status/2118996429163450822
- @L_ARCH_01: https://x.com/L_ARCH_01/status/2119383964167409667
- 対象資料: https://github.com/facebookresearch/sam-3d-body
- 参照: https://github.com/toyxyz/toyxyz_RGBMocap
- 参照: https://github.com/toyxyz/toyxyz_RGBMocap/blob/main/THIRD_PARTY_NOTICES.md
- 参照: https://github.com/zju3dv/GVHMR/blob/main/LICENSE
- 参照: https://github.com/twehrbein/ExMR/blob/main/LICENSE
- 参照: https://github.com/flowhmr/flowhmr
- 参照: https://huggingface.co/fafsaf1/flowhmr-0.46B
- 参照: https://x.com/L_ARCH_01/status/2119383964167409667
- 参照: https://github.com/facebookresearch/sam3
- 参照: https://raw.githubusercontent.com/facebookresearch/sam3/main/LICENSE
- 参照: https://raw.githubusercontent.com/facebookresearch/sam-3d-body/main/LICENSE
- 参照: https://huggingface.co/facebook/sam3.1
- 参照: https://huggingface.co/facebook/sam-3d-body-dinov3

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
