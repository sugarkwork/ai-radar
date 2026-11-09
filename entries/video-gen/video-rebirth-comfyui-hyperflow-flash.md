---
type: "repo"
name: "Video-Rebirth/ComfyUI-HyperFlow-Flash"
genre: "video-gen"
url: "https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash"
author: "Video-Rebirth"
source_post: "https://x.com/mapte_fireball/status/2118878741321687447"
sources: ["https://x.com/mapte_fireball/status/2118878741321687447?a=l2Xb1ZRD5GQIW06ngUQ&s=46", "https://x.com/mapte_fireball/status/2118878741321687447", "https://x.com/mapte_fireball/status/2118879117982695630", "https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash", "https://huggingface.co/api/models/VideoRebirthAI/hyperflow-h3-flash", "https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash/raw/main/README.md", "https://github.com/Video-Rebirth/hyperflow-h3-flash", "https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "ノードのGPL-3.0と重みのMiniMax H3 Community Licenseは別。他モデルやLoRAを同じ設定で動かせると仮定しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "Video-Rebirth/ComfyUI-HyperFlow-Flash"
license: "GPL-3.0"
language: "Python"
created: "2026-11-06"
updated: "2026-11-06"
stars: 15
forks: 3
open_issues: 0
commits_30d: 1
commits_90d: 1
commit_cadence: "monthly"
size_kb: 209
archived: false
fetched_at: "2026-11-09T00:30:48.130109+00:00"
---

# Video-Rebirth/ComfyUI-HyperFlow-Flash

## 出来ること

HyperFlow H3 FlashをComfyUIで利用する専用ノード。

## 目的・背景

紹介対象は `Video-Rebirth/ComfyUI-HyperFlow-Flash`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:48.130109+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

ComfyUI、Flash重み、ComfyUI-GGUF等とテキストエンコーダが別途必要。専用6step sigmas等はモデル側の指定を確認する。

## 実行条件

ノードのGPL-3.0と重みのMiniMax H3 Community Licenseは別。他モデルやLoRAを同じ設定で動かせると仮定しない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @mapte_fireball: https://x.com/mapte_fireball/status/2118878741321687447
- 対象資料: https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash
- 参照: https://x.com/mapte_fireball/status/2118879117982695630
- 参照: https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash
- 参照: https://huggingface.co/api/models/VideoRebirthAI/hyperflow-h3-flash
- 参照: https://huggingface.co/VideoRebirthAI/hyperflow-h3-flash/raw/main/README.md
- 参照: https://github.com/Video-Rebirth/hyperflow-h3-flash

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
