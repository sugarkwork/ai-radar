---
type: "repo"
name: "multimodal-art-projection/YuE"
genre: "tts-audio"
url: "https://github.com/multimodal-art-projection/YuE"
author: "multimodal-art-projection"
source_post: "https://x.com/eris_create_lab/status/2118948825125597550"
sources: ["https://x.com/eris_create_lab/status/2118948825125597550?a=1o_QGmbWv64MQt8co2c&s=46", "https://x.com/eris_create_lab/status/2118948825125597550", "https://x.com/i/article/2118941631386996736", "https://huggingface.co/m-a-p/YuE2-3B", "https://huggingface.co/api/models/m-a-p/YuE2-3B", "https://github.com/multimodal-art-projection/YuE", "https://x.com/ShinobuFujimoto/status/2119297842452038107"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "コードのApache-2.0をYuE2重みへ適用しない。YuE2重みはCC BY-NC4.0。世代違いの要件・評価を混入しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "multimodal-art-projection/YuE"
license: "Apache-2.0"
language: "Python"
created: "2025-01-23"
updated: "2026-11-01"
stars: 13285
forks: 1532
open_issues: 43
commits_30d: 39
commits_90d: 94
commit_cadence: "daily"
size_kb: 33179
archived: false
fetched_at: "2026-11-09T21:43:25Z"
last_release: "yue2-v0.1.6"
last_release_at: "2026-09-09"
---

# multimodal-art-projection/YuE

## 出来ること

YuE/YuE2の歌詞付き音楽生成に関連する公式コード。YuE2重みとは別の配布対象。

## 目的・背景

紹介対象は `multimodal-art-projection/YuE`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:59.455525+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Pythonと対応音声・GPU環境、利用する世代のモデルを個別に確認する。YuE2はLinux/NVIDIAでの確認が主。

## 実行条件

コードのApache-2.0をYuE2重みへ適用しない。YuE2重みはCC BY-NC4.0。世代違いの要件・評価を混入しない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/multimodal-art-projection/YuE#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Eris_Create_Lab: https://x.com/Eris_Create_Lab/status/2118948825125597550
- @ShinobuFujimoto: https://x.com/ShinobuFujimoto/status/2119297842452038107
- 対象資料: https://github.com/multimodal-art-projection/YuE
- 参照: https://x.com/i/article/2118941631386996736
- 参照: https://huggingface.co/m-a-p/YuE2-3B
- 参照: https://huggingface.co/api/models/m-a-p/YuE2-3B
- 参照: https://x.com/ShinobuFujimoto/status/2119297842452038107

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
