---
type: model
model: Linzhan/UniMate
name: UniMate チェックポイント
genre: 3d-motion
url: https://huggingface.co/Linzhan/UniMate
author: Linzhan Mou ほか（Princeton / UC Berkeley / MIT / NTU）
license: CC-BY-NC-4.0
base_model: []
format: pytorch
size: "チェックポイント1本あたり約0.77GB（.pt、計84ファイル）"
downloads: 629
likes: 87
created: 2026-09-27
updated: 2026-09-27
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/cutetoxicguy/status/2118116327093072374
sources:
  - https://github.com/Friedrich-M/UniMate
  - https://huggingface.co/datasets/Linzhan/UniML3D
pricing: free
pricing_detail: "重み無料・非商用（CC BY-NC 4.0）。コードは MIT"
signup_required: false
---

# UniMate チェックポイント

## 出来ること

- [UniMate](https://github.com/Friedrich-M/UniMate)（任意骨格向けテキスト→モーション）の**学習済みチェックポイント配布**。設定 JSON・正規化統計（.npy）・各ステップの `.pt` が入る。
- 学習段階ごとに系統が分かれている:
  - `unimate_mixamo_f60_v2` — Mixamo 人型データで学習
  - `unimate_truebones_f60_v2` — Truebones ZOO（動物）で学習
  - `unimate_uniml3d_f60_v1_preview` — UniML3D 初期プレビュー
  - `unimate_uniml3d_f60_v2` / `_v2_cross_attn` — UniML3D v2（cross-attn 変種あり）
  - `unimate_uniml3d_f60_v3` / `_v3_cross_attn` — UniML3D v3（cross-attn 変種あり）
- 推論には `checkpoint_step_150000.pt` などを使い、同じフォルダの JSON / npy とセットで読み込む。
- MLX 変換版（`mlx-community/unimate-uniml3d-f60-v3-bf16` ほか）もコミュニティから出ている（Apple Silicon 向け、未検証）。

## 目的・背景

研究コードと重みを分離して配布する構成。コードは GitHub（MIT）だが、**重みは CC BY-NC 4.0 で非商用**というライセンスの切り分けになっている。学習データ UniML3D は別途データセットとして公開（約88GB）。2026-09-27 公開、11-04 時点で 629 ダウンロード・87 likes。

## 収録ファイル

- 系統ごとの `checkpoints/checkpoint_step_*.pt`（各約0.77GB）
- 系統ごとの `config.json`、正規化統計 `.npy`
- リポジトリ直下に `LICENSE`（CC BY-NC 4.0）と `config.json`

## 実行条件

- **非商用ライセンス**（CC BY-NC 4.0）。業務・製品利用は不可、または別途許諾が必要
- 推論側の環境は UniMate リポジトリに従う（Python 3.10、CUDA GPU、`requirements.txt`）
- チェックポイント単体では動かず、**UniMate のコードとセット**で使う
- 学習データ由来の制約: Truebones ZOO のモーションは商用アセットで再配布されていない。Mixamo / Objaverse 系も各配布元の条件に従う
- 出力品質は研究段階（物理的な接地や重量配分は保証されない）

## 使い方

```bash
# 推論に必要なファイルだけ取得する例
hf download Linzhan/UniMate --repo-type model --local-dir outputs \
  --include "unimate_uniml3d_f60_v3/*.json" --include "unimate_uniml3d_f60_v3/*.npy" \
  --include "unimate_uniml3d_f60_v3/checkpoints/checkpoint_step_150000.pt"
```

## 変更履歴

- 2026-11-04: 初回登録
