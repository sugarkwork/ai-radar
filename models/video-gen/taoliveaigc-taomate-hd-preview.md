---
type: "model"
name: "TaoLiveAIGC/TaoMate-HD-preview"
genre: "video-gen"
url: "https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview"
author: "TaoLiveAIGC"
source_post: "https://x.com/Machinedelusion/status/2118752017824805138"
sources: ["https://x.com/machinedelusion/status/2118752017824805138?a=uN0B34qSmhTPi8nyOCc&s=46", "https://x.com/Machinedelusion/status/2118752017824805138", "https://taoliveaigc.github.io/TaoMate-HD/", "https://github.com/TaoLiveAIGC/TaoMate-HD", "https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview", "https://arxiv.org/abs/2611.03394", "https://huggingface.co/MiniMaxAI/MiniMax-H3"]
first_seen: "2026-11-06"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "MiniMax H3 Community Licenseの地域・商用条件を継承。previewのみで最終モデル・学習データは未公開、品質・速度は未再現。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "TaoLiveAIGC/TaoMate-HD-preview"
license: "other"
base_model: ["MiniMaxAI/MiniMax-H3"]
downloads: 100
likes: 10
format: "safetensors"
size: "配布中の重みファイル 1本・合計2,480,973,992 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-02"
updated: "2026-11-03"
fetched_at: "2026-11-09T00:30:30.894442+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "minimax-h3-community"
---

# TaoLiveAIGC/TaoMate-HD-preview

## 出来ること

TaoMate-HDのpreview LoRA。rank128/alpha128のadapter_model.safetensors約2.48GBが紹介対象。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:30.894442+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:30.894442+00:00）。重み 1本。

- `adapter_model.safetensors` — 2,480,973,992 bytes

[ファイル一覧](https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

MiniMax H3 FL2VA本体とTaoMate-HD推論コードが別途必要。フルモデルの単独配布ではない。

MiniMax H3 Community Licenseの地域・商用条件を継承。previewのみで最終モデル・学習データは未公開、品質・速度は未再現。

## 使い方

[公式モデルカード](https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @Machinedelusion: https://x.com/Machinedelusion/status/2118752017824805138
- 対象資料: https://huggingface.co/TaoLiveAIGC/TaoMate-HD-preview
- 参照: https://taoliveaigc.github.io/TaoMate-HD/
- 参照: https://github.com/TaoLiveAIGC/TaoMate-HD
- 参照: https://arxiv.org/abs/2611.03394
- 参照: https://huggingface.co/MiniMaxAI/MiniMax-H3

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
