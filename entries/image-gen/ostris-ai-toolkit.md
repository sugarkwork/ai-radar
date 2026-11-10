---
type: "repo"
name: "ostris/ai-toolkit"
genre: "image-gen"
url: "https://github.com/ostris/ai-toolkit"
author: "ostris"
source_post: "https://x.com/ai_hakase_/status/2118660440918020128"
sources: ["https://x.com/ai_hakase_/status/2118660440918020128?a=IUVIJ6ofEzgfl52Apj4&s=46", "https://x.com/ai_hakase_/status/2118660440918020128", "https://github.com/ostris/ai-toolkit/commit/883d676b17c6ba51d2b2a1aa0f4cae46b9a340ef", "https://api.github.com/repos/ostris/ai-toolkit", "https://huggingface.co/PrunaAI/P-H3-Image", "https://huggingface.co/api/models/PrunaAI/P-H3-Image", "https://github.com/ostris/ai-toolkit"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "MITはツールのコードに関する条件で、学習元重み・画像・生成物の条件とは別。学習速度・VRAM・成果は未再現。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "ostris/ai-toolkit"
license: "MIT"
language: "Python"
created: "2023-07-05"
updated: "2026-11-09"
stars: 12595
forks: 1616
open_issues: 83
commits_30d: 55
commits_90d: 100
commit_cadence: "daily"
size_kb: 34696
archived: false
fetched_at: "2026-11-09T21:38:21Z"
last_release: ""
last_release_at: ""
---

# ostris/ai-toolkit

## 出来ること

画像・動画拡散モデルの微調整をGUIまたはCLIで行う学習ツール。2026-11-04のP-H3-Image学習アダプタ追加が紹介対象。

## 目的・背景

紹介対象は `ostris/ai-toolkit`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:24.525110+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

対象の基底重みと学習データが別途必要。P-H3編集学習ではコントロール画像を含めると編集モードになり、最大8参照画像に対応とREADMEで説明。

## 実行条件

MITはツールのコードに関する条件で、学習元重み・画像・生成物の条件とは別。学習速度・VRAM・成果は未再現。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/ostris/ai-toolkit#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @ai_hakase_: https://x.com/ai_hakase_/status/2118660440918020128
- 対象資料: https://github.com/ostris/ai-toolkit
- 参照: https://github.com/ostris/ai-toolkit/commit/883d676b17c6ba51d2b2a1aa0f4cae46b9a340ef
- 参照: https://api.github.com/repos/ostris/ai-toolkit
- 参照: https://huggingface.co/PrunaAI/P-H3-Image
- 参照: https://huggingface.co/api/models/PrunaAI/P-H3-Image

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
