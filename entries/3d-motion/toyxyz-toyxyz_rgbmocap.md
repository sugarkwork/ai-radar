---
type: "repo"
name: "toyxyz/toyxyz_RGBMocap"
genre: "3d-motion"
url: "https://github.com/toyxyz/toyxyz_RGBMocap"
author: "toyxyz"
source_post: "https://x.com/Phantom_202601/status/2118812815238803495"
sources: ["https://x.com/phantom_202601/status/2118812815238803495?a=XzF8AyVCyl1lI1wG9gQ&s=46", "https://x.com/Phantom_202601/status/2118812815238803495", "https://github.com/toyxyz/toyxyz_RGBMocap", "https://api.github.com/repos/toyxyz/toyxyz_RGBMocap", "https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/README.md", "https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/LICENSE", "https://x.com/phantom_202601/status/2118812967517208975?a=NX4nndbLF-nwoJsmUwo&s=46", "https://x.com/Phantom_202601/status/2118812967517208975", "https://make-profit.net/2026/11/06/genai-lab-54-blender-mixamo-h3-soft-body-mannequin-three-angles-regenerated/", "https://x.com/OJI3_NIKKE/status/2118372636707455412", "https://huggingface.co/api/models/akatz-ai/MiniMax-H3-Character-Swap-LoRA", "https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/raw/main/README.md", "https://api.github.com/repos/akatz-ai/h3-relay", "https://x.com/lidamidorin/status/2118996429163450822?a=62XkeJF-pXiiS-fxjH4&s=46", "https://x.com/LidaMidorin/status/2118996429163450822", "https://github.com/toyxyz/toyxyz_RGBMocap/blob/main/THIRD_PARTY_NOTICES.md", "https://github.com/zju3dv/GVHMR/blob/main/LICENSE", "https://github.com/twehrbein/ExMR/blob/main/LICENSE", "https://github.com/flowhmr/flowhmr", "https://huggingface.co/fafsaf1/flowhmr-0.46B", "https://github.com/facebookresearch/sam-3d-body"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "MITは自作コードのみ。ExMR/GVHMR/PromptHMRと登録ボディには非商用等の別条件。FlowHMRも重みは非商用であり、コードのApacheを重みに適用しない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "toyxyz/toyxyz_RGBMocap"
license: "NOASSERTION"
language: "Python"
created: "2026-10-26"
updated: "2026-11-09"
stars: 1159
forks: 153
open_issues: 15
commits_30d: 49
commits_90d: 49
commit_cadence: "daily"
size_kb: 42908
archived: false
fetched_at: "2026-11-09T21:31:48Z"
last_release: ""
last_release_at: ""
---

# toyxyz/toyxyz_RGBMocap

## 出来ること

動画からExMR・FlowHMR・GVHMR等で動作を取り、足接地補正・人体リターゲットを経てFBX/BVH/VMDやBlenderへ出すWindowsアプリ。

## 目的・背景

紹介対象は `toyxyz/toyxyz_RGBMocap`。対象固有の機能・制約の説明は2026-11-07, 2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:32.344333+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

64bit Windows、NVIDIA GPU/ドライバ、OpenGL4.3。Model Managerで重みを別取得し、一部は登録・規約同意。全体約68GBの記録。

## 実行条件

MITは自作コードのみ。ExMR/GVHMR/PromptHMRと登録ボディには非商用等の別条件。FlowHMRも重みは非商用であり、コードのApacheを重みに適用しない。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/toyxyz/toyxyz_RGBMocap#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Phantom_202601: https://x.com/Phantom_202601/status/2118812815238803495
- @Phantom_202601: https://x.com/Phantom_202601/status/2118812967517208975
- @LidaMidorin: https://x.com/LidaMidorin/status/2118996429163450822
- 対象資料: https://github.com/toyxyz/toyxyz_RGBMocap
- 参照: https://api.github.com/repos/toyxyz/toyxyz_RGBMocap
- 参照: https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/README.md
- 参照: https://raw.githubusercontent.com/toyxyz/toyxyz_RGBMocap/main/LICENSE
- 参照: https://x.com/Phantom_202601/status/2118812967517208975
- 参照: https://make-profit.net/2026/11/06/genai-lab-54-blender-mixamo-h3-soft-body-mannequin-three-angles-regenerated/
- 参照: https://x.com/OJI3_NIKKE/status/2118372636707455412
- 参照: https://huggingface.co/api/models/akatz-ai/MiniMax-H3-Character-Swap-LoRA
- 参照: https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA/raw/main/README.md
- 参照: https://api.github.com/repos/akatz-ai/h3-relay
- 参照: https://x.com/LidaMidorin/status/2118996429163450822
- 参照: https://github.com/toyxyz/toyxyz_RGBMocap/blob/main/THIRD_PARTY_NOTICES.md
- 参照: https://github.com/zju3dv/GVHMR/blob/main/LICENSE
- 参照: https://github.com/twehrbein/ExMR/blob/main/LICENSE
- 参照: https://github.com/flowhmr/flowhmr
- 参照: https://huggingface.co/fafsaf1/flowhmr-0.46B
- 参照: https://github.com/facebookresearch/sam-3d-body

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
