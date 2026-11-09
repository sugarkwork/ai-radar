---
type: "repo"
name: "OpenBMB/VoxCPM"
genre: "tts-audio"
url: "https://github.com/OpenBMB/VoxCPM"
author: "OpenBMB"
source_post: "https://x.com/Chenfacai0/status/2118859224348500186"
sources: ["https://x.com/chenfacai0/status/2118859224348500186?a=8f9NUfFnCfee6S-wF9g&s=46", "https://x.com/Chenfacai0/status/2118859224348500186", "https://github.com/OpenBMB/VoxCPM", "https://github.com/OpenBMB/VoxCPM/releases", "https://github.com/OpenBMB/VoxCPM/blob/main/README.md", "https://x.com/manorgw/status/2118861993281286621?a=ckCiZ8tJo04gsnzxn2I&s=46", "https://x.com/Manorgw/status/2118861993281286621", "https://api.github.com/repos/OpenBMB/VoxCPM", "https://raw.githubusercontent.com/OpenBMB/VoxCPM/main/README.md", "https://huggingface.co/api/models/openbmb/VoxCPM2"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "RTX4090のRTF約0.3やVRAM約8GBは配布元の記述。トレンド1位は未確認。本人または許諾済み音声だけを利用し、コード・重み以外の権利も確認する。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "OpenBMB/VoxCPM"
license: "Apache-2.0"
language: "Python"
created: "2025-09-16"
updated: "2026-11-05"
stars: 41797
forks: 4763
open_issues: 173
commits_30d: 2
commits_90d: 23
commit_cadence: "monthly"
size_kb: 4267
archived: false
fetched_at: "2026-11-09T00:30:35.134775+00:00"
---

# OpenBMB/VoxCPM

## 出来ること

VoxCPM2の音声合成コード。テキストの声設計と短い参照音声からの制御付き複製、30言語、48kHz出力を案内。

## 目的・背景

紹介対象は `OpenBMB/VoxCPM`。対象固有の機能・制約の説明は2026-11-07, 2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:35.134775+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

Python3.10〜3.12、PyTorch2.5+、CUDA12+。MiniCPM-4バックボーンとAudioVAE V2、モデル重みが別途必要。

## 実行条件

RTX4090のRTF約0.3やVRAM約8GBは配布元の記述。トレンド1位は未確認。本人または許諾済み音声だけを利用し、コード・重み以外の権利も確認する。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/OpenBMB/VoxCPM#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Chenfacai0: https://x.com/Chenfacai0/status/2118859224348500186
- @Manorgw: https://x.com/Manorgw/status/2118861993281286621
- 対象資料: https://github.com/OpenBMB/VoxCPM
- 参照: https://github.com/OpenBMB/VoxCPM/releases
- 参照: https://github.com/OpenBMB/VoxCPM/blob/main/README.md
- 参照: https://x.com/Manorgw/status/2118861993281286621
- 参照: https://api.github.com/repos/OpenBMB/VoxCPM
- 参照: https://raw.githubusercontent.com/OpenBMB/VoxCPM/main/README.md
- 参照: https://huggingface.co/api/models/openbmb/VoxCPM2

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
