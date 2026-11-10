---
type: "repo"
name: "Kablex/ComfyUI-Ref2VA-VSA"
genre: "video-gen"
url: "https://github.com/Kablex/ComfyUI-Ref2VA-VSA"
author: "Kablex"
source_post: "https://x.com/Forhanvv/status/2119186920228147368"
sources: ["https://x.com/forhanvv/status/2119186920228147368?a=0wJ7yiHbqAiBFgitLJI&s=46", "https://x.com/Forhanvv/status/2119186920228147368", "https://x.com/forhanvv/status/2119186920228147368", "https://github.com/Kablex/ComfyUI-Ref2VA-VSA", "https://github.com/Kablex/ComfyUI-Ref2VA-VSA/blob/main/LICENSE"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "RTX4090の約72秒warm/13.5GBは作者表。zero face driftは設計主張で独立証明なし。2026-09-05作成で今回の新作ではない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "Kablex/ComfyUI-Ref2VA-VSA"
license: "NOASSERTION"
language: "Python"
created: "2026-09-05"
updated: "2026-10-17"
stars: 1027
forks: 127
open_issues: 0
commits_30d: 1
commits_90d: 5
commit_cadence: "monthly"
size_kb: 4161
archived: false
fetched_at: "2026-11-09T21:45:15Z"
last_release: ""
last_release_at: ""
---

# Kablex/ComfyUI-Ref2VA-VSA

## 出来ること

FastVideo由来VSAゲートをRef2VAへ移植し、映像トークンを疎にして少ステップ生成を高速化する実験ComfyUIノード。

## 目的・背景

紹介対象は `Kablex/ComfyUI-Ref2VA-VSA`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:28.097679+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Ref2VA pruned INT8、Turbo4step LoRA、fasth3_vsa_gate、Qwen3VL32B TE、映像/音声VAE等が必要。

## 実行条件

RTX4090の約72秒warm/13.5GBは作者表。zero face driftは設計主張で独立証明なし。2026-09-05作成で今回の新作ではない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/Kablex/ComfyUI-Ref2VA-VSA#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Forhanvv: https://x.com/Forhanvv/status/2119186920228147368
- 対象資料: https://github.com/Kablex/ComfyUI-Ref2VA-VSA
- 参照: https://x.com/forhanvv/status/2119186920228147368
- 参照: https://github.com/Kablex/ComfyUI-Ref2VA-VSA/blob/main/LICENSE

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
