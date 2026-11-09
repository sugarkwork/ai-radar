---
type: "model"
name: "tencent/Qwen3.8-27B-DSpine-b16"
genre: "model-serving"
url: "https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16"
author: "tencent"
source_post: "https://x.com/NFT_Chen/status/2119393299987648936"
sources: ["https://x.com/NFT_Chen/status/2119393299987648936", "https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16"]
first_seen: "2026-11-08"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "AR比2.71〜3.84倍はカード測定。DFlash2も2.33〜3.17倍で、全条件で圧倒するとは言えない。速度・受入長は未追試。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "tencent/Qwen3.8-27B-DSpine-b16"
license: "apache-2.0"
base_model: ["Qwen/Qwen3.8-27B"]
downloads: 652
likes: 94
format: "safetensors"
size: "配布中の重みファイル 1本・合計4,051,831,880 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-11-07"
updated: "2026-11-07"
fetched_at: "2026-11-09T00:31:37.274866+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# tencent/Qwen3.8-27B-DSpine-b16

## 出来ること

Qwen3.8-27Bを高速化するDSpineの5層ドラフトモデル。block16、8192トークン滑り窓を案内。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08（原記録）のチェック記録を基にしている。メタ情報は2026-11-09T00:31:37.274866+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:31:37.274866+00:00）。重み 1本。

- `model.safetensors` — 4,051,831,880 bytes

[ファイル一覧](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

約4.05GB、SGLang0.5.22と対象Qwen本体が必要。単体チャットモデルではない。

AR比2.71〜3.84倍はカード測定。DFlash2も2.33〜3.17倍で、全条件で圧倒するとは言えない。速度・受入長は未追試。

## 使い方

[公式モデルカード](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。

## 出典

- @NFT_Chen: https://x.com/NFT_Chen/status/2119393299987648936
- 対象資料: https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
