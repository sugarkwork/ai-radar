---
type: "model"
name: "m-a-p/YuE2-3B"
genre: "tts-audio"
url: "https://huggingface.co/m-a-p/YuE2-3B"
author: "m-a-p"
source_post: "https://x.com/eris_create_lab/status/2118948825125597550"
sources: ["https://x.com/eris_create_lab/status/2118948825125597550?a=1o_QGmbWv64MQt8co2c&s=46", "https://x.com/eris_create_lab/status/2118948825125597550", "https://x.com/i/article/2118941631386996736", "https://huggingface.co/m-a-p/YuE2-3B", "https://huggingface.co/api/models/m-a-p/YuE2-3B", "https://github.com/multimodal-art-projection/YuE", "https://x.com/ShinobuFujimoto/status/2119297842452038107"]
first_seen: "2026-11-07"
amplifiers: []
added: "2026-11-09"
flags: ["unverified"]
risk_notes: "重みはCC BY-NC4.0で非商用。Suno比較やWildSongBench best-of-8の数値は作者測定。Mac動作は第三者MLXポートの別環境で、公式同条件ではない。 当方でインストール・推論・生成・ベンチ再現はしていない。"
model: "m-a-p/YuE2-3B"
license: "cc-by-nc-4.0"
base_model: []
downloads: 23237
likes: 1244
format: "safetensors"
size: "配布中の重みファイル 1本・合計7,261,441,640 bytes（複数形式・量子化・派生を含む。必要メモリではない）"
created: "2026-09-09"
updated: "2026-10-06"
fetched_at: "2026-11-09T00:30:59.072470+00:00"
pricing: "free"
pricing_detail: "重みのダウンロードに利用料金の表示なし。ライセンス・用途・地域・商用許諾と実行費用は別途確認。"
signup_required: false
---

# m-a-p/YuE2-3B

## 出来ること

歌詞・スタイルからボーカル付き楽曲を生成し、ABC譜面によるメロディ/コード編集も案内するYuE2。

## 目的・背景

対象固有の機能・制約の説明は2026-11-08のチェック記録を基にしている。メタ情報は2026-11-09T00:30:59.072470+00:00に公式APIを取得した値。API取得とREADME確認は動作試験ではない。

公式README/モデルカードも取得済み。性能表・デモは配布元の報告として扱い、独立測定へ読み替えない。

## 収録ファイル

公式APIの現行一覧（2026-11-09T00:30:59.072470+00:00）。重み 1本。

- `model.safetensors` — 7,261,441,640 bytes

[ファイル一覧](https://huggingface.co/m-a-p/YuE2-3B/tree/main)。配布容量とロード後の必要メモリ、TE/VAE等の外部依存は区別する。

## 実行条件

約7.26GB safetensors、48kHzステレオ。公式の動作確認はLinux/NVIDIAで非量子化24GB GPU。コードと重みは別配布。

重みはCC BY-NC4.0で非商用。Suno比較やWildSongBench best-of-8の数値は作者測定。Mac動作は第三者MLXポートの別環境で、公式同条件ではない。

## 使い方

[公式モデルカード](https://huggingface.co/m-a-p/YuE2-3B)から対応する実装・形式と必要な基底モデルを選ぶ。ファイル一覧は取得したが、重みのダウンロード・ロード・推論は実施していない。 custom_code / trust_remote_codeを使う例がある場合は実装の内容を確認してから許可する。

## 出典

- @Eris_Create_Lab: https://x.com/Eris_Create_Lab/status/2118948825125597550
- @ShinobuFujimoto: https://x.com/ShinobuFujimoto/status/2119297842452038107
- 対象資料: https://huggingface.co/m-a-p/YuE2-3B
- 参照: https://x.com/i/article/2118941631386996736
- 参照: https://huggingface.co/api/models/m-a-p/YuE2-3B
- 参照: https://github.com/multimodal-art-projection/YuE
- 参照: https://x.com/ShinobuFujimoto/status/2119297842452038107

## 変更履歴

- 2026-11-09: 初回収録用の概要を作成。原チェックと公式メタ情報の取得範囲を区別して記載。実行追試なし。
