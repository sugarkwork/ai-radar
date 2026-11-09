---
type: "repo"
name: "pixiv/three-vrm"
genre: "3d-motion"
url: "https://github.com/pixiv/three-vrm"
author: "pixiv"
source_post: "https://x.com/dextune/status/2118994641798262815"
sources: ["https://x.com/dextune/status/2118994641798262815?a=k4I5bVlohbtFEvOKA-M&s=46", "https://x.com/dextune/status/2118994641798262815", "https://github.com/pixiv/three-vrm", "https://raw.githubusercontent.com/pixiv/three-vrm/dev/README.md", "https://api.github.com/repos/pixiv/three-vrm/releases/tags/v3.6.0-beta.0", "https://registry.npmjs.org/@pixiv/three-vrm"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "v3.6.0-beta.0のVRMC_springBone_limitはBeta拡張。MITはコードの条件で、各VRMの人物・衣装・モデルの権利は別。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "pixiv/three-vrm"
license: "MIT"
language: "TypeScript"
created: "2019-06-04"
updated: "2026-10-22"
stars: 2277
forks: 202
open_issues: 45
commits_30d: 3
commits_90d: 14
commit_cadence: "monthly"
size_kb: 127519
archived: false
fetched_at: "2026-11-09T00:31:03.855362+00:00"
---

# pixiv/three-vrm

## 出来ること

Three.jsのGLTFLoaderへVRMLoaderPluginを登録しVRMを読み込むpixivのライブラリ。

## 目的・背景

紹介対象は `pixiv/three-vrm`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:31:03.855362+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

TypeScript/Three.js。v3以降のWebGPURenderer対応はMToonNodeMaterialを使用しThree.js r167以降が必要。

## 実行条件

v3.6.0-beta.0のVRMC_springBone_limitはBeta拡張。MITはコードの条件で、各VRMの人物・衣装・モデルの権利は別。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/pixiv/three-vrm#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @dextune: https://x.com/dextune/status/2118994641798262815
- 対象資料: https://github.com/pixiv/three-vrm
- 参照: https://raw.githubusercontent.com/pixiv/three-vrm/dev/README.md
- 参照: https://api.github.com/repos/pixiv/three-vrm/releases/tags/v3.6.0-beta.0
- 参照: https://registry.npmjs.org/@pixiv/three-vrm

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
