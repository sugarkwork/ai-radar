---
type: "repo"
name: "lovisdotio/video-to-texture"
genre: "3d-motion"
url: "https://github.com/lovisdotio/video-to-texture"
author: "lovisdotio"
source_post: "https://x.com/dextune/status/2118871058363343263"
sources: ["https://x.com/dextune/status/2118871058363343263?a=L_Y9WsGtRLPHZtoqZ-4&s=46", "https://x.com/dextune/status/2118871058363343263", "https://github.com/lovisdotio/video-to-texture", "https://api.github.com/repos/lovisdotio/video-to-texture", "https://github.com/lovisdotio/video-to-texture/blob/HEAD/README.md"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "4096²・120フレームを55.8秒等は作者申告。SfM不要でも元メッシュ・既知カメラ・有料生成が必要で、ゼロ費用ではない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "lovisdotio/video-to-texture"
license: "MIT"
language: "Python"
created: "2026-10-27"
updated: "2026-10-27"
stars: 45
forks: 2
open_issues: 0
commits_30d: 6
commits_90d: 6
commit_cadence: "weekly"
size_kb: 20685
archived: false
fetched_at: "2026-11-09T00:30:45.427305+00:00"
---

# lovisdotio/video-to-texture

## 出来ること

Blenderでメッシュの粘土オービットを描き、Seedream5 Pro/Seedance2.5で再スタイルし、既知カメラのままUVへ焼き付ける実装。

## 目的・背景

紹介対象は `lovisdotio/video-to-texture`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:45.427305+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Blender headless、Python3.10+、ffmpeg、FAL_KEYを使う有料fal環境。掲載ベンチはH100。中間データを欠く研究スナップショット部分もある。

## 実行条件

4096²・120フレームを55.8秒等は作者申告。SfM不要でも元メッシュ・既知カメラ・有料生成が必要で、ゼロ費用ではない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/lovisdotio/video-to-texture#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @dextune: https://x.com/dextune/status/2118871058363343263
- 対象資料: https://github.com/lovisdotio/video-to-texture
- 参照: https://api.github.com/repos/lovisdotio/video-to-texture
- 参照: https://github.com/lovisdotio/video-to-texture/blob/HEAD/README.md

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
