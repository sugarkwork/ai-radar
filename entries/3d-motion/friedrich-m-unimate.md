---
repo: Friedrich-M/UniMate
name: UniMate
genre: 3d-motion
url: https://github.com/Friedrich-M/UniMate
author: Linzhan Mou ほか（Princeton / UC Berkeley / MIT / NTU）
license: MIT
stars: 2463
language: Python
created: 2026-07-22
updated: 2026-10-08
added: 2026-11-04
first_seen: 2026-11-04
source_post: https://x.com/cutetoxicguy/status/2118116327093072374
sources:
  - https://linzhanmou.com/unimate/
  - https://arxiv.org/abs/2609.05415
  - https://huggingface.co/datasets/Linzhan/UniML3D
forks: 262
open_issues: 10
commits_30d: 2
commits_90d: 21
commit_cadence: monthly
size_kb: 40387
archived: false
fetched_at: "2026-11-05T02:58:35Z"
---

# UniMate

## 出来ること

- **任意の骨格に対するテキスト→モーション生成**。人型・四足・鳥・海棲・昆虫・蛇・関節のある機械オブジェクトまで、骨格ごとの再学習やテスト時最適化なしで動かす（SIGGRAPH Asia 2026）。
- 機能: テキストからのモーション生成、異なる骨格への**ゼロショット転移**、自然言語による**モーション編集**、2ポーズ間の**インビトゥイーニング**、既存モーションの**延長**。
- 設計は **topology-aware Diffusion Transformer**。全キャラが同じボーン数だと仮定せず、骨格の接続構造を明示的に扱う:
  - **Graph-aware attention** — 関節の関係と骨格上の距離が、部位同士の相互作用に効く
  - **Spectral rotary embeddings** — 回転位置埋め込みをグラフラプラシアンで任意骨格へ一般化
  - **Global topology conditioning** — rest pose 骨格全体の表現で、キャラの構造を把握する
- **`rig_preprocess`**: 既存のリグ済み GLB / glTF / FBX（アニメーション有無は問わない）を UniMate 用の表現に変換する。関節ラベルと向きを人が確認するステップ付き。
- 付属のアプリケーション: インビトゥイーニング、テキスト編集、モーション延長。出力はアニメーション付き GLB と FBX（モーションごと）。

## 目的・背景

AI キャラクターアニメーションは人型・動物・モーション種別ごとにシステムが分断されてきた。UniMate は「まず骨格を理解し、その構造に合った動きを生成する」方向で一本化する。学習データは **UniML3D**（13,769本のテキスト付きモーション、7,430骨格、二足・四足・鳥・海棲・昆虫・蛇・関節物体）。Princeton / UC Berkeley / MIT / NTU の共同研究。2026-07-22 作成、10-08 が最終 push、2,462 star。

**リギングはしない。** 入力にはリグ済みアセットが必要で、リグの無いメッシュには使えない。骨格・スキニングを作る側は [UniRig](vast-ai-research-unirig.md) / [SkinTokens](vast-ai-research-skintokens.md) が担当する（役割が別）。

## 依存関係

- conda 環境（**Python 3.10**）、`setuptools<81`、`requirements.txt`（`--no-build-isolation` で導入）
- 学習済みチェックポイントは Hugging Face `Linzhan/UniMate`（推論用は `checkpoint_step_150000.pt` など）
- UniML3D データセット（約88GB、部分ダウンロード可）— データセット骨格で動かす場合のみ
- 自前アセットを使う場合は `data_process/rig_preprocess`
- CUDA GPU を想定（README に VRAM の明記は無し）

## 実行条件

- **リグ済みアセットが必須**。UniMate 自身はスケルトンを作らない
- 出力は物理的に正確な接地・重量配分・制作そのままの品質を保証しない。クリーンアップ前提
- 作者自身が「early step」と明記しており、**失敗するモーション・骨格は多い**。データ拡張（エージェント蒸留・動画生成）が今後の方向
- **コードは MIT、チェックポイントは CC BY-NC 4.0（非商用）**。商用利用は別途確認が必要
- UniML3D のキャプションは公開時に再処理されており、プロジェクトページや論文のプロンプトと一致しない場合がある
- Truebones ZOO のモーションは商用アセットで再配布不可。各自で購入してビルドスクリプトで再構成する

## 最短手順

```bash
conda create -n unimate python=3.10 -y
conda activate unimate
pip install "setuptools<81"
pip install -r requirements.txt --no-build-isolation

# 推論用チェックポイント（例）
hf download Linzhan/UniMate --repo-type model --local-dir outputs \
  --include "unimate_uniml3d_f60_v3/*.json" --include "unimate_uniml3d_f60_v3/*.npy" \
  --include "unimate_uniml3d_f60_v3/checkpoints/checkpoint_step_150000.pt"

# 自前キャラを使う場合
# data_process/rig_preprocess でリグ済み GLB / glTF / FBX を変換（関節ラベルを確認）
```

## 変更履歴

- 2026-11-04: 初回登録（SIGGRAPH Asia 2026、rig_preprocess 公開時点）
