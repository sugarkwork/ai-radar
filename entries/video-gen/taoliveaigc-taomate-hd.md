---
type: "repo"
name: "TaoLiveAIGC/TaoMate-HD"
genre: "video-gen"
url: "https://github.com/TaoLiveAIGC/TaoMate-HD"
author: "TaoLiveAIGC"
source_post: "https://x.com/Machinedelusion/status/2118752017824805138"
sources: ["https://x.com/machinedelusion/status/2118752017824805138?a=uN0B34qSmhTPi8nyOCc&s=46", "https://x.com/Machinedelusion/status/2118752017824805138", "https://taoliveaigc.github.io/TaoMate-HD/", "https://github.com/TaoLiveAIGC/TaoMate-HD", "https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview", "https://arxiv.org/abs/2611.03394", "https://huggingface.co/MiniMaxAI/MiniMax-H3"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "学習コード・データ・最終LoRAは未公開。1.6倍高速化とCER改善は論文自己報告。コードと重みにMiniMax H3系の独自条件・地域制限あり。 当方でインストール・推論・生成・ベンチ再現はしていない。"
repo: "TaoLiveAIGC/TaoMate-HD"
license: "NOASSERTION"
language: "Python"
created: "2026-11-02"
updated: "2026-11-03"
stars: 26
forks: 2
open_issues: 0
commits_30d: 2
commits_90d: 2
commit_cadence: "monthly"
size_kb: 4073
archived: false
fetched_at: "2026-11-09T21:46:41Z"
last_release: ""
last_release_at: ""
---

# TaoLiveAIGC/TaoMate-HD

## 出来ること

MiniMax H3 FL2VAを基に、480pで2回・768pで1回のデノイズをする音声映像の漸進解像度自己回帰生成の実装。

## 目的・背景

紹介対象は `TaoLiveAIGC/TaoMate-HD`。対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:30.737722+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

fork=false、archived=false。commit数は30日・90日それぞれ100件上限であり、100は100件以上を表す。starsやpushだけで保守品質を保証しない。

## 依存関係

公開は推論コードとpreview LoRA。基底MiniMax H3を別取得。例はH20 96GBを8枚用いる構成で単一GPU手順は未確認。

## 実行条件

学習コード・データ・最終LoRAは未公開。1.6倍高速化とCER改善は論文自己報告。コードと重みにMiniMax H3系の独自条件・地域制限あり。

コード本体の許諾と、基底モデル・同梱素材・外部API・音声/人物等の利用条件は別に確認する。

## 最短手順

1. [公式README](https://github.com/TaoLiveAIGC/TaoMate-HD#readme)で対応版と依存を確認する。
2. 上記の対象固有条件を満たす環境を用意し、配布元の手順を選ぶ。
3. 外部サービスの料金・認証・データ送信とライセンスを確認してから導入する。

本調査では導入・ビルド・起動をしていないため、成功済みのコマンドとしては掲載しない。

## 出典

- @Machinedelusion: https://x.com/Machinedelusion/status/2118752017824805138
- 対象資料: https://github.com/TaoLiveAIGC/TaoMate-HD
- 参照: https://taoliveaigc.github.io/TaoMate-HD/
- 参照: https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview
- 参照: https://arxiv.org/abs/2611.03394
- 参照: https://huggingface.co/MiniMaxAI/MiniMax-H3

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
