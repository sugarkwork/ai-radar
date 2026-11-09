---
type: "model"
name: "kakaocorp/kanana-2-v-decide-3b-2611"
genre: "eval"
url: "https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611"
author: "kakaocorp"
source_post: "https://x.com/DeepTechTR/status/2118943836684620055"
sources: ["https://x.com/deeptechtr/status/2118943836684620055?a=-Syy5Aady0SmsgZU-IQ&s=46", "https://x.com/DeepTechTR/status/2118943836684620055", "https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611", "https://huggingface.co/api/models/kakaocorp/kanana-2-v-decide-3b-2611", "https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611/raw/main/README.md", "https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611/raw/main/LICENSE"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "独自Kanana Open LicenseでAPI再販・SI・組込み等の商用提供に別許諾、表示・派生名等に条件。Decision Index61.23等はKakao自己評価。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "kakaocorp/kanana-2-v-decide-3b-2611"
license: "other"
base_model: []
downloads: 545
likes: 25
format: "safetensors"
size: "配布中の重みファイル 1本・合計7,330,945,212 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-10-26"
updated: "2026-11-06"
fetched_at: "2026-11-09T00:30:58.853287+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
license_name: "kanana-open-license"
---

# kakaocorp/kanana-2-v-decide-3b-2611

## 出来ること

文章/JSON/チャットと最大10画像を受け、選択肢・yes/no・スコアの確率分布を返す3.67Bの判定モデル。長文テキストを生成するものではない。

2026-11-09確認のモデルカードでは状態と各候補を埋め込みにし、cosine similarityのsoftmaxから確率を返すと説明。ko/enの表記。生成文がないことと、判定が常に正しいことは別である。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:58.853287+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:58.853287+00:00）。重み 1本。

- `model.safetensors` — 7,330,945,212 bytes

[ファイル一覧](https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

7.33GBの重み、20480トークン入力、transformers/custom_code。trust_remote_code使用前に実装確認が必要。

独自Kanana Open LicenseでAPI再販・SI・組込み等の商用提供に別許諾、表示・派生名等に条件。Decision Index61.23等はKakao自己評価。

## 使い方

[公式モデルカード](https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。 custom_code / trust_remote_codeを使う例がある場合は実装の内容を確認してから許可する。

## 出典

- @DeepTechTR: https://x.com/DeepTechTR/status/2118943836684620055
- 対象資料: https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611
- 参照: https://huggingface.co/api/models/kakaocorp/kanana-2-v-decide-3b-2611
- 参照: https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611/raw/main/README.md
- 参照: https://huggingface.co/kakaocorp/kanana-2-v-decide-3b-2611/raw/main/LICENSE

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
